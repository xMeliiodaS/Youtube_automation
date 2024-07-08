from selenium.webdriver.common.by import By
from infra.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageAfterLogin(BasePage):
    VIDEO_LINK = '(//a[@id="video-title-link"])[1]'
    SHORT_LINK = '(//a[@title="Shorts"])[1]'

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_video_link(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.VIDEO_LINK)))
        element.click()

    def click_on_short_link(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.SHORT_LINK)))
        element.click()
