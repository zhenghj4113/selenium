from selenium.common import TimeoutException

from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time

from base.user_manage_page import UserManagePage
from tool.log_tool import get_logger
from base.login_page import LoginPage
from config.cfg import *

logger = get_logger(__name__)


class StudentManagePage(UserManagePage):


    ADD_STUDENT = (By.XPATH,'//span[contains(text(),"添加学生")]')
    STUDENT_NAME = (By.CSS_SELECTOR,'#student_name')
    PHONE = (By.CSS_SELECTOR,'#phone')
    STUDENT_NUMBER = (By.CSS_SELECTOR, '#student_number')
    CARD_NUMBER = (By.CSS_SELECTOR, '#card_number')
    CONFIRM_BUTTON = (By.XPATH,'//span[contains(text(),"确 定")]')
    TIP = (By.XPATH,'//div[@class="ant-message"]')


    def __init__(self,driver):
        super().__init__(driver)
        logger.info("StudentManagePage页面对象初始化完成")

    '''细颗粒度步骤'''
    def _click_add_student_button(self):
        self.click(self.ADD_STUDENT)
        logger.info("点击【添加学生】按钮，进入添加页面")

    def _input_student_name(self, student_name):
        self.type(self.STUDENT_NAME, student_name)
        logger.info(f"输入学生姓名：{student_name}")

    def _input_phone(self, phone):
        self.type(self.PHONE, phone)
        logger.info(f"输入手机号：{phone}")

    def _input_student_number(self, student_number):
        self.type(self.STUDENT_NUMBER, student_number)
        logger.info(f"输入学号：{student_number}")

    def _input_card_number(self, card_number):
        self.type(self.CARD_NUMBER, card_number)
        logger.info(f"输入卡号：{card_number}")

    def _click_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)
        logger.info("点击【确定】按钮，提交学生信息")

    '''整体方法'''

    def add_student(self,student_name,phone,student_number,card_number):
        self._click_add_student_button()
        self._input_student_name(student_name)
        self._input_phone(phone)
        self._input_student_number(student_number)
        self._input_card_number(card_number)
        self._click_confirm_button()
        logger.info(f"姓名{student_name}，手机号{phone}，学号{student_number}，卡号{card_number}，确定添加学生")

    def get_tip(self):
        try:
            tip = self.get_text(self.TIP)
            logger.info(f"提示{tip}")
            return tip
        except TimeoutException:
            logger.info(f"没找到提示信息{tip}")
            return  None







