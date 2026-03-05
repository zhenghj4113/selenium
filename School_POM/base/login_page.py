from time import sleep

from selenium.common import TimeoutException

from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):

    USERNAME = (By.ID,'normal_login_user')
    PASSWORD = (By.ID,'normal_login_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'.ant-btn.ant-btn-primary.login-form-button')
    HOME_PAGE = (By.CSS_SELECTOR,'.page_main')
    ERROR_TIP = (By.XPATH, "//span[contains(text(), '您还未注册')]")

    def __init__(self,driver):
        super().__init__(driver)

    def open_login_page(self,url):
        self.open(url)

    def login(self,username,password):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)
        time.sleep(5)

    def is_success_login(self):
        try:
            self.wait_visible(self.HOME_PAGE,timeout=5)
            return True
        except TimeoutException:
            return False

    def get_error_tip(self, timeout=3):
        """封装错误提示获取：加异常处理，返回空字符串而非报错"""
        try:
            return self.get_text(self.ERROR_TIP, timeout=timeout)
        except TimeoutException:
            return "没找到"