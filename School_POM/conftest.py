import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='module')
def driver():
    options=webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # 无界面模式（注释掉看操作）
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()  # 最大化窗口
        driver.implicitly_wait(10) # 隐式等待为10秒
        print('驱动初始化成功')
        yield driver
    except Exception as e:
        print(f'驱动初始化失败：{str(e)}')
        raise
    finally:
        if 'driver' in locals():
            driver.quit()