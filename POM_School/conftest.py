import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.service import Service
from base.login_page import LoginPage
# from base.student_manage_page import StudentManagePage
from tool.log_tool import get_logger
from webdriver_manager.chrome import ChromeDriverManager
from config.cfg import *

logger = get_logger(__name__)

@pytest.fixture(scope='module')
def driver():
    logger.info("========== 初始化Chrome浏览器 ==========")
    options=webdriver.ChromeOptions()
    service = Service(executable_path=driver_path)
    # options.add_argument("--headless=new")  # 无界面模式（调试时注释掉）
    options.add_argument("--no-sandbox") #禁用沙盒
    options.add_argument("--disable-dev-shm-usage") # 解决内存不足问题
    options.add_argument("--disable-extensions")  # 禁用扩展（减少加载项）
    options.add_argument("--disable-plugins")  # 禁用插件
    options.add_argument("--log-level=3")  # 禁用浏览器日志输出
    options.add_argument("--disable-gpu")  # 禁用GPU加速（无头模式必加）
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 禁用控制台日志
    options.add_experimental_option("detach", False)  # 禁止浏览器独立进程（避免残留）

    # 可选：禁用图片加载（非UI测试时打开，进一步提速）
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)

    driver = None
    try:
        driver = webdriver.Chrome(options=options,service=service)
        driver.maximize_window()    # 最大化窗口
        driver.implicitly_wait(10)  # 隐式等待为10秒
        logger.info('驱动初始化成功')
        yield driver    #返回空白浏览器的driver对象

    except Exception as e:
        logger.info(f'驱动初始化失败：{str(e)}',exc_info=True) # 输出完整异常栈
        raise

    finally:
        if driver is not None:
            logger.info("========== 关闭Chrome浏览器 ==========")
            driver.quit()

# @pytest.fixture(scope='module')
# def login_fixture(driver):
#     login_page = LoginPage(driver)
#     login_page.goto_login_page(login_url)
#     login_page.login(admin_username,admin_password)
#     yield driver    #返回登录成功的driver对象


# @pytest.fixture(scope='function')
# def person_manage_fixture(driver):
#     student_manage_page = StudentManagePage(driver)
#     student_manage_page.goto_student_manage_page()
