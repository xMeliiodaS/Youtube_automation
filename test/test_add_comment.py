import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page_after_login import HomePageAfterLogin
from logic.home_page_before_login import HomePageBeforeLogin
from logic.login_page import LoginPage
from logic.video_page import VideoPage
from infra.utils import Utils


class TestAddComment(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePageBeforeLogin(self.driver)

        login_page = LoginPage(self.driver)
        login_page.login_flow(self.config)

    def tearDown(self) -> None:
        self.driver.quit()

    # def login(self):
    #     # Wait for the page to load
    #     self.home_page.click_on_login_button()
    #
    #     login_page = LoginPage(self.driver)
    #     login_page.fill_username_input(self.config["email"])
    #     login_page.click_on_next_button()
    #
    #     login_page.fill_password_input(self.config["password"])
    #     time.sleep(1)
    #     login_page.click_on_next_button()
    #     time.sleep(7)

    def test_add_comment_successfully(self):
        # Arrange
        #   self.login()
        home_page_after_login = HomePageAfterLogin(self.driver)

        time.sleep(2)
        home_page_after_login.click_on_video_link()

        video_page = VideoPage(self.driver)

        # Act
        unique_comment = Utils.generate_unique_comment("Hi guys")
        video_page.fill_comment_input(unique_comment)
        time.sleep(5)
        video_page.click_on_comment_button()

        # Assert
        comment_present = video_page.is_comment_displayed(unique_comment)
        self.assertTrue(comment_present, f"Comment '{unique_comment}' was not found on the video page.")


if __name__ == "__main__":
    unittest.main()
