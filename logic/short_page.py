import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium import common as c
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShortPage(BasePageApp):
    LIKE_BUTTON = '(//button[contains(@aria-label,"like this video")])[1]'
    ALREADY_LIKED = '(//button[contains(@aria-label, "like this video along") and @aria-pressed="false"])[1]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            time.sleep(4)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_on_like_button(self):
        if not self.already_liked():
            element = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.LIKE_BUTTON)))

            element.click()

    def already_liked(self):
        try:
            WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ALREADY_LIKED)))
            return False
        except (NoSuchElementException, TimeoutException):
            return True
