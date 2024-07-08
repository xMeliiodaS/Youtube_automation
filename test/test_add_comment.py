import time
import unittest
import undetected_chromedriver as uc
from infra.config_provider import ConfigProvider
from logic.home_page_after_login import HomePageAfterLogin
from logic.home_page_before_login import HomePageBeforeLogin
from logic.login_page import LoginPage
from logic.video_page import VideoPage


class TestAddComment(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        # Initialize the undetected ChromeDriver
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        self.config = ConfigProvider.load_config_json()
        self.driver.get(self.config["url"])
        self.driver.execute_script("")
        self.home_page = HomePageBeforeLogin(self.driver)

    # def tearDown(self) -> None:
    #     self.driver.quit()

    def login(self):
        # Wait for the page to load
        self.home_page.click_on_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_username_input(self.config["email"])
        login_page.click_on_next_button()

        login_page.fill_password_input(self.config["password"])
        time.sleep(1)
        login_page.click_on_next_button()
        time.sleep(7)

    def test_add_comment_successfully(self):
        # Arrange
        self.login()
        home_page_after_login = HomePageAfterLogin(self.driver)

        time.sleep(2)
        home_page_after_login.click_on_video_link()

        video_page = VideoPage(self.driver)

        # Act
        video_page.fill_comment_input("Hi guys")
        time.sleep(5)
        video_page.click_on_comment_button()

        # Assert


if __name__ == "__main__":
    unittest.main()
