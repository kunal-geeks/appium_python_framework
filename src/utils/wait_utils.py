from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DEFAULT_TIMEOUT = 15

class WaitUtils:

    @staticmethod
    def wait_for_visible(driver, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_clickable(driver, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(driver, timeout).until(
            ec.element_to_be_clickable(locator)
        )

    @staticmethod
    def wait_for_presence(driver, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_for_elements(driver, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(driver, timeout).until(
            ec.presence_of_all_elements_located(locator)
        )
