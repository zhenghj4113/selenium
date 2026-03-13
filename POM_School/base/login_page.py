
from selenium.common import TimeoutException
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from tool.log_tool import get_logger
import time

logger = get_logger(__name__)

class LoginPage(BasePage):

    USERNAME = (By.ID,'normal_login_user')
    PASSWORD = (By.ID,'normal_login_password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'.ant-btn.ant-btn-primary.login-form-button')
    HOME_PAGE = (By.CSS_SELECTOR,'.page_main')
    TIP = (By.XPATH,'//div[@class="ant-message"]')

    def __init__(self,driver):
        super().__init__(driver)
        logger.info("LoginPage页面对象初始化完成")


    def _input_username(self,username):
        logger.info(f"尝试输入用户名")
        if self.type(self.USERNAME,username):
            logger.info(f"用户名{username}输入成功")
            return True
        else:
            logger.error(f"用户名{username}输入失败")
            return False

    def _input_password(self,password):
        logger.info(f"尝试输入密码")
        if self.type(self.PASSWORD,password):
            logger.info(f"密码{password}输入成功")
            return True
        else:
            logger.error(f"密码{password}输入失败")
            return False

    def _click_login_button(self):
        logger.info("尝试点击登录按钮")
        if self.click(self.LOGIN_BUTTON):
            logger.info("登录按钮点击成功")
            return True
        else:
            logger.error("登录按钮点击失败")
            return False

    def _goto_login_page(self,url):
        if self.open(url):
            if self.wait_visible(self.USERNAME):
                logger.info("登录页打开成功")
                return True
            else:
                logger.error("登录页打开成功，但用户名输入框未找到")
                return False
        else:
            logger.error("登录页打开失败")
            return False

    def login(self,url,username,password):
        if not self._goto_login_page(url):
            logger.error("登录页打开失败，终止登录流程")
            return False
        if not self._input_username(username):
            logger.error(f"用户名输入失败")
            return False
        if not self._input_password(password):
            logger.error(f"用户名密码输入失败")
            return False
        if not self._click_login_button():
            logger.error(f"登录按钮点击失败")
            return False

        logger.info("登录按钮已点击，等待登录结果")
        return True



    def is_success_login(self):

        if self.wait_visible(self.HOME_PAGE,timeout=5):
            logger.info("登录成功")
            return True
        else:
            logger.error("未检测到首页元素，登录失败")
            return False

    def get_tip(self):
        tip = self.get_text(self.TIP)
        if tip:
            logger.info(f"提示{tip}")
            return tip
        else:
            logger.error(f"没找到提示信息{tip}")
            return  ''