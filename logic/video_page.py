import time

from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium import common as c
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VideoPage(BasePageApp):
    CLICK_ON_INPUT = '//div[@id="placeholder-area"]'
    ADD_COMMENT_INPUT = '//div[@id="contenteditable-root"]'
    COMMENT_BUTTON = '//button[@aria-label="Comment"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            time.sleep(4)
            self._driver.execute_script("window.scrollBy(0, 500);")
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_on_input(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.CLICK_ON_INPUT)))

        element.click()

    def fill_comment_input(self, comment):
        self.click_on_input()

        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.ADD_COMMENT_INPUT)))

        element.send_keys(comment)

    def click_on_comment_button(self):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.COMMENT_BUTTON)))

        element.click()
