from src.tests.base_test import BaseTest


class TestSearch(BaseTest):

    def test_search(self, driver):
        self.onboarding.skip_onboarding()
        self.home.click_search()
        self.search.search("India")

        assert "India" in self.search.get_first_result()

