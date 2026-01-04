from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from src.pages.base_page import BasePage
from src.utils.wait_utils import WaitUtils
from src.utils.logger import get_logger

logger = get_logger("OnboardingPage")


class OnboardingPage(BasePage):
    SKIP_BTN = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")

    def skip_onboarding(self):
        logger.info("Checking for onboarding screen")

        try:
            WaitUtils.wait_for_visible(
                driver=self.driver,
                locator=self.SKIP_BTN,
                timeout=5
            )
            self.click(self.SKIP_BTN)
            logger.info("Onboarding skipped successfully")

        except TimeoutException:
            logger.info("Onboarding screen not present, continuing")
