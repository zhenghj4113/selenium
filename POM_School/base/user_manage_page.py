import time

from selenium.common import TimeoutException
from base.base_page import BasePage
from selenium.webdriver.common.by import By


from tool.log_tool import get_logger


logger = get_logger(__name__)

class UserManagePage(BasePage):
    PERSON_MANAGE = (By.XPATH,'//i[contains(@class,"icon-gx-renyuanguanli")]')
    STUDENT_MANAGE = (By.XPATH,'//span[contains(text(),"学生管理")]')
    TEACHER_MANAGE = (By.XPATH,'//span[contains(text(),"教师管理")]')
    STAFF_MANAGE = (By.XPATH,'//span[contains(text(),"职工管理")]')
    ADD_STUDENT = (By.XPATH, '//span[contains(text(),"添加学生")]')
    ADD_TEACHER = (By.XPATH, '//span[contains(text(),"添加教师")]')
    ADD_STAFF = (By.XPATH, '//span[contains(text(),"添加职工")]')

    def __init__(self,driver):
        super().__init__(driver)
        logger.info("人员管理页面对象初始化完成")

    def _click_person_manage(self):
        logger.info("等待3秒")
        time.sleep(3)
        self.wait_visible(self.PERSON_MANAGE)
        self.click(self.PERSON_MANAGE)
        logger.info("点击人员管理")

    def goto_student_manage_page(self):
        self._click_person_manage()
        self.click(self.STUDENT_MANAGE)
        self.wait_visible(self.ADD_STUDENT)
        logger.info("已进入学生管理页面")

    def goto_teacher_manage_page(self):
        self._click_person_manage()
        self.click(self.TEACHER_MANAGE)
        self.wait_visible(self.ADD_TEACHER)
        logger.info("已进入教师管理页面")

    def goto_staff_manage_page(self):
        self._click_person_manage()
        self.click(self.STAFF_MANAGE)
        self.wait_visible(self.ADD_STAFF)
        logger.info("已进入职工管理页面")