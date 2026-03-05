from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import platform
import time

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.default_timeout = 5
        # 根据系统来区分ctrl还是command
        self.select_all_key = Keys.CONTROL if platform.system() == 'Windows' else Keys.COMMAND

    def wait_clickable(self,locator,timeout = None):
        timeout = timeout or self.default_timeout
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"超时{timeout}秒：元素{locator}仍不可点击")

    def wait_visible(self,locator,timeout = None):
        timeout = timeout or self.default_timeout
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"超时{timeout}秒：元素{locator}仍不可见")

    def open(self,url):
        self.driver.get(url)

    def find(self,locator):
        return self.driver.find_element(*locator)

    def click(self,locator,timeout = None):
        self.wait_clickable(locator,timeout).click()

    def type(self,locator,value,timeout = None):
        ele = self.wait_visible(locator,timeout)
        ele.click()
        ele.send_keys(self.select_all_key + "a")
        ele.send_keys(Keys.BACKSPACE)
        ele.send_keys(value)

    def get_text(self,locator,timeout = None):
        return self.wait_visible(locator,timeout).text





