from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import platform
import time
from tool.log_tool import get_logger

logger = get_logger(__name__)

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.default_timeout = 5
        # 根据系统来区分ctrl还是command
        self.select_all_key = Keys.CONTROL if platform.system() == 'Windows' else Keys.COMMAND
        logger.info('BasePage初始化完成，driver对象已绑定')

    def wait_clickable(self,locator,timeout = None):
        timeout = timeout or self.default_timeout
        logger.info(f'等待元素可点击：{locator}，超时时间：{timeout}秒')
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
            logger.info(f'元素{locator}已可点击')
            return element
        except TimeoutException:
            logger.error(f"超时{timeout}秒：元素{locator}仍不可点击")
            # raise TimeoutException(f"超时{timeout}秒：元素{locator}仍不可点击")
            return False

    def wait_visible(self,locator,timeout = None):
        timeout = timeout or self.default_timeout
        logger.info(f'等待元素可见：{locator}，超时时间：{timeout}秒')
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            logger.info(f'元素{locator}已可见')
            return element
        except TimeoutException:
            logger.error(f"超时{timeout}秒：元素{locator}仍不可见")
            # raise TimeoutException(f"超时{timeout}秒：元素{locator}仍不可见")
            return False


    def open(self,url):
        logger.info(f'打开页面：{url}')
        try:
            self.driver.get(url)
            logger.info(f"页面{url}打开成功")
            return True
        except Exception as e:
            logger.error(f"页面{url}打开失败，失败原因{str(e)}")
            return False

    def find(self,locator):
        logger.info(f'定位元素：{locator}')
        return self.driver.find_element(*locator)

    def click(self,locator,timeout = None):
        logger.info(f'尝试点击元素{locator}')
        try:
            ele = self.wait_clickable(locator,timeout)
            if not ele:
                logger.error(f'元素{locator}点击失败')
                return False
            ele.click()
            logger.info(f'元素{locator}点击成功')
            return True

        except (ElementNotInteractableException,Exception) as e:
            logger.error(f'元素{locator}点击失败，失败原因{str(e)}')
            return False

    def type(self,locator,value,timeout = None):
        try:
            ele = self.wait_visible(locator,timeout)
            if not ele:
                logger.error(f"元素{locator}不可见，不可输入")
                return False
            ele.click()
            ele.send_keys(self.select_all_key + "a")
            ele.send_keys(Keys.BACKSPACE)
            ele.send_keys(value)
            logger.info(f'输入{value}完成')
            return True
        except (ElementNotInteractableException,AttributeError,Exception) as e:
            logger.error(f"向元素{locator}输入失败，失败原因：{str(e)}")
            return False

    def get_text(self,locator,timeout = None):
        logger.info(f'尝试获取元素{locator}的文本')
        try:
            ele =  self.wait_visible(locator,timeout)
            if not ele:
                logger.error(f"元素{locator}不可见，获取文本失败")
                return ''
            text = ele.text
            logger.info(f'获取到文本{text}')
            return text
        except (ElementNotInteractableException,AttributeError,Exception) as e:
            logger.error(f"获取元素{locator}文本失败，失败原因：{str(e)}")
            return ''




