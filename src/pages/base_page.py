from src.utils.wait_utils import WaitUtils

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WaitUtils.wait_for_clickable(self.driver, locator)
        element.click()

    def type(self, locator, text):
        element = WaitUtils.wait_for_visible(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = WaitUtils.wait_for_visible(self.driver, locator)
        return element.text

    def find(self, locator):
        return WaitUtils.wait_for_presence(self.driver, locator)

    def find_elements(self, locator):
        return WaitUtils.wait_for_elements(self.driver, locator)

    def is_visible(self, locator) -> bool:
        element = WaitUtils.wait_for_visible(self.driver, locator)
        return element.is_displayed()
