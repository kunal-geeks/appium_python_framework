from src.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class SearchPage(BasePage):
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    RESULT_TITLE = (AppiumBy.ID, "org.wikipedia:id/page_list_item_title")

    def search(self, text):
        self.type(self.SEARCH_INPUT, text)

    def get_first_result(self):
        return self.find_elements(self.RESULT_TITLE)[0].text
