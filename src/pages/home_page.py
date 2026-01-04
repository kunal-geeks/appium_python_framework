from src.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    SEARCH_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")

    def click_search(self):
        self.click(self.SEARCH_FIELD)

    def is_search_visible(self) -> bool:
        """
        Used by smoke tests to verify app launch
        """
        return self.is_visible(self.SEARCH_FIELD)