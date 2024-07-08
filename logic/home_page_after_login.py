from selenium.webdriver.common.by import By
from infra.utils import Utils
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageAfterLogin(BasePage):
    index = Utils.generate_random_string()
    VIDEO_LINK = '(//a[@id="video-title-link"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self._video_link = self._driver.find_element(By.XPATH, self.VIDEO_LINK)

    def click_on_video_link(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.VIDEO_LINK)))
        element.click()

