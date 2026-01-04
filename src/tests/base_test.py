import pytest

from src.pages.home_page import HomePage
from src.pages.search_page import SearchPage
from src.pages.onboarding_page import OnboardingPage


class BaseTest:
    driver = None
    home = None
    search = None
    onboarding = None

    @pytest.fixture(autouse=True)
    def _setup(self, driver):
        """
        This fixture runs before EACH test method.
        """
        self.driver = driver
        self.home = HomePage(driver)
        self.search = SearchPage(driver)
        self.onboarding = OnboardingPage(driver)

    def _init_pages(self):
        self.home = HomePage(self.driver)
        self.search = SearchPage(self.driver)
        self.onboarding = OnboardingPage(self.driver)
