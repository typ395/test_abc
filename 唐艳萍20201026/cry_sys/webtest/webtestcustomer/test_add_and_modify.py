import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\测试\\selenium')
from 唐艳萍20201026.cry_sys.base.usebrowser import UseBrowser
from 唐艳萍20201026.cry_sys.webpage.customermanager.customerpage import CustomerPage


class CustomerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cp=CustomerPage()

    def test_customer_add_success(self):
        self.cp.customer_add(name='jack',Birthday='2020-10-14 16:32:02',customerAddMan='dawei',Email='1431714026@qq.com')
        self.assertEqual(self.cp.add_alert_text(),'客户添加成功')
    def test_modif(self):
        self.cp.modify('15608318364')
        self.assertEqual(self.cp.add_alert_text(),'客户修改成功')

    def tearDown(self) -> None:
        UseBrowser().quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    # 创建case
    tset_case = unittest.TestLoader().loadTestsFromTestCase(CustomerTest)
    # 添加case
    suit.addTest(tset_case)
    print(time.localtime())
    now_time = time.strftime('%Y-%m-%d', time.localtime())
    with open('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\report\\customerpage' + now_time + '.html',
              'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description=None)
        # 运行case
        runner.run(suit)
