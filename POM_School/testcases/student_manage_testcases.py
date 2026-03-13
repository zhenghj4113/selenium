
import pytest
from base.login_page import LoginPage
from base.student_manage_page import StudentManagePage
from config.cfg import *
from tool.log_tool import get_logger
# 执行命令 pytest testcases/student_manage_testcases.py -vvs -p no:playwright


logger = get_logger(__name__)
# 格式：(测试用例名称, 账号, 密码, 预期提示文本, 预期是否登录成功)
student_info_data = [
    ('必填项正确填写登录','auto2','17777777778','002','002','操作成功')
]

# @pytest.mark.parametrize 会自动遍历测试数据，生成多个测试用例
@pytest.mark.parametrize("case_name,student_name,phone,student_number,card_number,expected_result",student_info_data)
def test_add_student_success(driver,case_name,student_name,phone,student_number,card_number,expected_result):
    logger.info(f"========== 开始执行用例：{case_name} ==========")

    login_page = LoginPage(driver)
    student_manage_page = StudentManagePage(driver)

    login_page.goto_login_page(login_url)
    login_page.login('admin','admin.pass')
    logger.info("管理员登录成功")

    # 进入学生管理页面
    student_manage_page.goto_student_manage_page()

    # 添加学生
    student_manage_page.add_student(student_name,phone,student_number,card_number)
    tip = student_manage_page.get_tip()
    assert expected_result in tip, f"用例{case_name}：提示不符，预期{expected_result}，实际{tip}"
    logger.info(f"========== 结束执行用例：{case_name} ==========\n")



