import sys
import time
import unittest
sys.path.append('D:\\测试\\selenium')
from 唐艳萍20201026.cry_sys.base.usebrowser import UseBrowser
from 唐艳萍20201026.cry_sys.util.operationExcel import OperationExcel
from 唐艳萍20201026.cry_sys.webpage.usermanger.loginpage import Login
from HTMLTestRunner import HTMLTestRunner

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.op=OperationExcel('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\conifg\\test_case.xlsx', '用例参数')
        self.login=Login(self.op.get_cell(1,1))

    def test_login_name_passwd_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        self.assertEqual(self.login.bo.alert_text(),self.op.get_cell(1,4))
    def test_name_null(self):
        self.login.login(self.op.get_cell(2,2), int(self.op.get_cell(2,3)))
        self.assertEqual(self.login.bo.alert_text(), self.op.get_cell(2,4))
    def test_password_null(self):
        self.login.login(self.op.get_cell(3,2), self.op.get_cell(3,3))
        self.assertEqual(self.login.bo.alert_text(), self.op.get_cell(3,4))
    def test_name_error(self):
        self.login.login(self.op.get_cell(4,2), int(self.op.get_cell(4,3)))
        self.assertEqual(self.login.bo.alert_text(), self.op.get_cell(4,4))
    def test_password_error(self):
        self.login.login(self.op.get_cell(5,2), int(self.op.get_cell(5,3)))
        self.assertEqual(self.login.bo.alert_text(), self.op.get_cell(5,4))
    def test_name_chinese(self):
        self.login.login(self.op.get_cell(6,2), int(self.op.get_cell(6,3)))
        self.assertEqual(self.login.bo.alert_text(), self.op.get_cell(6,4))
    def test_login_sucess(self):
        self.login.login(self.op.get_cell(7,2),int(self.op.get_cell(7,3)))
        correct_text=self.login.login_correct_text('topFrame','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div')
        self.assertEqual(correct_text, self.op.get_cell(7,4))

    def tearDown(self) -> None:
        UseBrowser().quit()
if __name__ == '__main__':
    suit = unittest.TestSuite()
    # 创建case
    tset_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # 添加case
    suit.addTest(tset_case)
    print(time.localtime())
    now_time = time.strftime('%Y-%m-%d', time.localtime())
    with open('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\report\\loginpage' + now_time + '.html',
              'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description=None)
        # 运行case
        runner.run(suit)
