
import pytest
from base.login_page import LoginPage
from config.cfg import *

# 执行命令cd pytest testcase/test_cases.py -xvs -p no:playwright

# 格式：(测试用例名称, 账号, 密码, 预期提示文本, 预期是否登录成功)
login_test_data = [
    # ('正确账号，错误密码登录','admin','admin','无效的密码',False),
    ('账号不存在','admin123','admin.pass','您还未注册',False),
    ('正确账号，正确密码登录','admin','admin.pass','登录成功',True)
]

# @pytest.mark.parametrize 会自动遍历测试数据，生成多个测试用例
@pytest.mark.parametrize("case_name,username,password,expected_result,is_success",login_test_data)
def test_login(driver,case_name,username,password,expected_result,is_success):
    login_page = LoginPage(driver)
    login_page.open_login_page(login_url)
    login_page.login(username,password)
    if is_success:
        assert login_page.is_success_login(),f"用例{case_name}：登录成功，预期成功"
    else:
        result = login_page.get_error_tip()
        assert expected_result in result , f"用例{case_name}：错误提示不符，预期{expected_result}，实际{result}"

