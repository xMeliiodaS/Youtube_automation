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

    SUBSCRIBE_BUTTON = '//button[contains(@aria-label, "Subscribe to")]'
    UNSUBSCRIBE_BUTTON = '//span[text() = "Subscribed"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            time.sleep(4)

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

    def is_comment_displayed(self, unique_comment):
        comment_xpath = f'//span[contains(text(), "{unique_comment}")]'
        comment_present = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.XPATH, comment_xpath)))
        return comment_present.is_displayed()

    def click_on_subscribe_button(self):
        try:
            element = WebDriverWait(self._driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.SUBSCRIBE_BUTTON)))
            element.click()
        except c.NoSuchElementException as e:
            print("Already subscribed !", e)

    def is_subscribed(self):
        try:
            elements = WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.UNSUBSCRIBE_BUTTON)))
            if len(elements) == 2:
                return True
            else:
                return False
        except c.NoSuchElementException as e:
            print("Already subscribed !", e)

    def scroll(self):
        time.sleep(4)
        self.scroll()