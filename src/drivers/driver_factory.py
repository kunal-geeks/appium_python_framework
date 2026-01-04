import os
import yaml
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options


def load_config():
    config_file = Path("src/config/config.yaml")
    with open(config_file, "r") as file:
        return yaml.safe_load(file)


def create_driver(device: str = None):
    config = load_config()

    # ===== Device selection =====
    target_device = (
        os.getenv("TARGET_DEVICE")
        or device
        or config.get("deviceType", "emulator")
    )

    app_path = Path(config["appPath"]).resolve()
    if not app_path.exists():
        raise FileNotFoundError(f"APK not found at {app_path}")

    # ===== Options =====
    options = UiAutomator2Options()

    # ===== Mandatory capabilities =====
    options.set_capability("platformName", config["platformName"])
    options.set_capability("automationName", config["automationName"])

    # ===== Device selection =====
    if target_device == "real":
        options.set_capability("udid", config["realDeviceUdid"])
        options.set_capability("deviceName", "Android")
    elif target_device == "emulator":
        options.set_capability("udid", config["emulatorUdid"])
        options.set_capability("deviceName", "Android Emulator")
    else:
        raise ValueError(f"Unknown device type: {target_device}")

    # ===== App =====
    app_path = Path(config["appPath"]).resolve()
    if not app_path.exists():
        raise FileNotFoundError(f"APK not found at {app_path}")

    options.set_capability("app", str(app_path))
    options.set_capability("appPackage", config["appPackage"])
    options.set_capability("appActivity", config["appActivity"])
    options.set_capability("appWaitActivity", config["appWaitActivity"])

    # ===== Reset / permissions =====
    options.set_capability("noReset", config["noReset"])
    options.set_capability("fullReset", config["fullReset"])
    options.set_capability("autoGrantPermissions", True)

    driver = webdriver.Remote(
        command_executor=config["appiumServerUrl"],
        options=options
    )

    driver.implicitly_wait(config.get("implicitWait", 10))
    return driver
