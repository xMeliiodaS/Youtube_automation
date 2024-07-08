import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@type="email"]'
    PASSWORD_INPUT = '//input[@name="Passwd"]'
    NEXT_BUTTON = '(//button[@type = "button" and @jsname="LgbsSe"])[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)

        self._next_button = self._driver.find_element(By.XPATH, self.NEXT_BUTTON)

    def fill_username_input(self, username):
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, self.EMAIL_INPUT)))
        self._email_input.send_keys(username)

    def fill_password_input(self, password):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_INPUT)))
        element.send_keys(password)

    def click_on_next_button(self):
        element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NEXT_BUTTON)))
        element.click()