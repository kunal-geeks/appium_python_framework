import pytest
from src.tests.base_test import BaseTest

@pytest.mark.parametrize("keyword", ["India", "Automation", "Selenium"])
class TestSearchData(BaseTest):

    def test_search_keywords(self, driver, keyword):
        self.onboarding.skip_onboarding()
        self.home.click_search()
        self.search.search(keyword)

        assert keyword in self.search.get_first_result()
