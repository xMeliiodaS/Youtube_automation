from selenium.webdriver.common.by import By
from infra.utils import Utils
from infra.base_page import BasePage


class HomePageAfterLogin(BasePage):
    index = Utils.generate_random_string()
    VIDEO_LINK = f'(//a[@id = "thumbnail" and contains(@href, "watch")])[{index}]'

    def __init__(self, driver):
        super().__init__(driver)
        self._video_link = self._driver.find_element(By.XPATH, self.VIDEO_LINK)

    def click_on_video_link(self):
        self._video_link.click()
