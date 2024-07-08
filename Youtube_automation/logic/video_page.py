
from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium import common as c


class VideoPage(BasePageApp):
    ADD_COMMENT_INPUT = '//div[@id="contenteditable-root"]'
    COMMENT_BUTTON = '//button[@aria-label="Comment"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._add_comment_input = self._driver.find_element(By.XPATH, self.ADD_COMMENT_INPUT)
            self._comment_button = self._driver.find_element(By.XPATH, self.COMMENT_BUTTON)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def fill_comment_input(self, user):
        self._add_comment_input.send_keys(user)

    def click_on_comment_button(self):
        self._comment_button.click()
