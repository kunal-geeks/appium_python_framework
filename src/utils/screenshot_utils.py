import os
from datetime import datetime

def take_screenshot(driver, test_name):
    folder = "reports/screenshots"
    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/{test_name}_{timestamp}.png"

    driver.save_screenshot(path)
    return path
