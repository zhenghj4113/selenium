
import pytest
from base.login_page import LoginPage
from config.cfg import *
from tool.log_tool import get_logger
# 执行命令 pytest testcases/login_testcases.py -vvs -p no:playwright


logger = get_logger(__name__)
# 格式：(测试用例名称, 账号, 密码, 预期提示文本, 预期是否登录成功)
login_test_data = [
    # ('正确账号，错误密码登录','admin','admin','无效的密码',False),
    ('账号不存在','admin123','admin.pass','您还未注册',False),
    ('正确账号，正确密码登录','admin','admin.pass','登录成功',True)
]

# @pytest.mark.parametrize 会自动遍历测试数据，生成多个测试用例
@pytest.mark.parametrize("case_name,username,password,expected_tip,is_success",login_test_data)
def test_login(driver,case_name,username,password,expected_tip,is_success):
    logger.info(f"========== 开始执行用例：{case_name} ==========")

    login_page = LoginPage(driver)
    try:
        login_result = login_page.login(login_url,username,password)
        if not login_result:
            logger.error(f"")
            raise AssertionError(f"用例{case_name}登录流程执行失败")

        if is_success:
            assert login_page.is_success_login(),f"用例{case_name}：登录失败，预期成功"
        else:
            tip = login_page.get_tip()
            assert expected_tip in tip , f"用例{case_name}：错误提示不符，预期{expected_tip}，实际{tip}"
        logger.info(f"用例{case_name}执行成功")
    except AttributeError as e:
        logger.error(f"用例{case_name}执行失败：{str(e)}")
        raise e
    finally:
        logger.info(f"========== 结束执行用例：{case_name} ==========\n")
