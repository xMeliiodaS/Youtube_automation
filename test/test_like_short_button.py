import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page_after_login import HomePageAfterLogin
from logic.home_page_before_login import HomePageBeforeLogin
from logic.login_page import LoginPage
from logic.short_page import ShortPage


class TestLikeShortButton(unittest.TestCase):
    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePageBeforeLogin(self.driver)

    # def tearDown(self) -> None:
    #     self.driver.quit()

    def login(self):
        # Wait for the page to load
        self.home_page.click_on_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_username_input(self.config["email"])
        login_page.click_on_next_button()

        time.sleep(1)
        login_page.fill_password_input(self.config["password"])
        time.sleep(1)
        login_page.click_on_next_button()
        time.sleep(7)

    def test_add_comment_successfully(self):
        # Arrange
        self.login()
        home_page_after_login = HomePageAfterLogin(self.driver)

        time.sleep(2)
        home_page_after_login.click_on_short_link()

        short_page = ShortPage(self.driver)

        # Act
        short_page.click_on_like_button()
        time.sleep(5)
        is_like = short_page.already_liked()

        # Assert
        self.assertTrue(is_like)


if __name__ == "__main__":
    unittest.main()
