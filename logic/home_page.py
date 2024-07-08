from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class HomePage(BasePage):
    LOGIN_BUTTON = '(//yt-button-shape//a)[1]'

    def __init__(self, driver):
        super().__init__(driver)
        WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)

    def click_on_login_button(self):
        self._login_button.click()
