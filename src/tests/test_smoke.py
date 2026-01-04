from src.tests.base_test import BaseTest

class TestSmoke(BaseTest):

    def test_app_launch(self, driver):
        self.onboarding.skip_onboarding()
        assert self.home.is_search_visible()
