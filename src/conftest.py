import os
import pytest
import yaml
from pathlib import Path

from src.drivers.driver_factory import create_driver
from src.utils.logger import get_logger
from src.utils.screenshot_utils import take_screenshot

logger = get_logger("PyTest")

# Session start → ensure reports directory
def pytest_sessionstart(session):
    os.makedirs("reports", exist_ok=True)
    logger.info("Reports directory ready!!!")


# CLI option: --device=real|emulator
def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        default=None,
        help="Target device: real | emulator"
    )

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


# Driver fixture (FUNCTION scoped → parallel safe)
@pytest.fixture(scope="function")
def driver(request, device):
    logger.info(f"Starting Appium Driver (device={device or 'config default'})")

    driver = create_driver(device=device)

    # attach driver to test node (for screenshots)
    request.node.driver = driver

    yield driver

    logger.info("Closing Appium Driver!!!")
    driver.quit()

# Logging hooks
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logger.info(f"===== START TEST: {item.name} =====")


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item):
    logger.info(f"===== END TEST: {item.name} =====")

# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            path = take_screenshot(driver, item.name)
            logger.error(f"Screenshot saved: {path}")
