import time

from selenium.webdriver.common.alert import Alert
import sys
sys.path.append('D:\\测试\\selenium')
from 唐艳萍20201026.cry_sys.conifg.log_crm import AutoLog
from 唐艳萍20201026.cry_sys.db.customerdb.customeroperdb import CustomerOperationDb
from 唐艳萍20201026.cry_sys.util.yaml_operation import YamlOperation
from 唐艳萍20201026.cry_sys.webpage.usermanger.loginpage import Login


class CustomerPage:
    def __init__(self):
        self.yamlOperation = YamlOperation('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\conifg\\test.yaml')
        self.lp = Login('http://www.summermori.icu:8080/crm/')
        self.lp.login('admin', '123456')
        self.log = AutoLog()
        self.co=CustomerOperationDb()

    def customer_add(self, **kwargs):
        self.kwargs=kwargs
        if self.check_db_name("select * from customer_info where customer_name='"+self.kwargs['name']+"'") is True:
            self.co.dele_customer("delete FROM customer_info WHERE customer_name='"+self.kwargs['name']+"'")
        time.sleep(1)
        self.lp.bo.change_frame(self.yamlOperation.get_locator('AddPage','frametop'))
        self.log.get_mes('切换框架', 'info')
        time.sleep(1)
        self.lp.bo.click_element(self.yamlOperation.get_locator('AddPage','user_info'))  # 客户信息
        self.log.get_mes('点击客户信息', 'info')
        self.lp.bo.change_frame(self.yamlOperation.get_locator('AddPage','framemain'))
        self.log.get_mes('切换框架', 'info')
        self.lp.bo.click_element(self.yamlOperation.get_locator('AddPage','add'))
        self.log.get_mes('点击添加', 'info')
        self.lp.bo.send_keys(self.yamlOperation.get_locator('AddPage','CustomerName'),kwargs.get('name',''))  # 姓名
        self.log.get_mes('添加姓名', 'info')
        self.lp.bo.driver.execute_script("window.document.getElementById('customerBirthday').readOnly=false")
        self.lp.bo.send_keys(self.yamlOperation.get_locator('AddPage','customerBirthday'), kwargs.get('Birthday', ''))  # 添加出生日期
        self.log.get_mes('添加出生日期', 'info')
        self.lp.bo.send_keys(self.yamlOperation.get_locator('AddPage','CustomerAddMan'),kwargs.get('customerAddMan', ''))  # 创建人
        self.log.get_mes('添加创建人', 'info')
        self.lp.bo.send_keys(self.yamlOperation.get_locator('AddPage','CustomerEmail'), kwargs.get('Email', ''))  # email
        self.log.get_mes('添加email', 'info')
        self.lp.bo.click_element(self.yamlOperation.get_locator('AddPage','Submit'))
        self.log.get_mes('点击提交', 'info')
    def check_db_name(self,sql):
        page_content =[]
        page_content.append(self.kwargs['name'])
        if page_content==self.co.add_customer_db_data(sql):
            return True
        return False



    def modify(self,phone):
        time.sleep(1)
        self.lp.bo.change_frame(self.yamlOperation.get_locator('Modify','TopFrame'))
        time.sleep(1)
        self.lp.bo.click_element(self.yamlOperation.get_locator('Modify','user_info'))
        self.log.get_mes('点击客户信息', 'info')
        time.sleep(1)
        self.lp.bo.change_frame(self.yamlOperation.get_locator('Modify','MainFrame'))
        self.lp.bo.click_element(self.yamlOperation.get_locator('Modify','Edit'))  # 点击编辑
        self.log.get_mes('点击编辑', 'info')
        self.lp.bo.clear(self.yamlOperation.get_locator('Modify','Clear'))  # 清除
        self.lp.bo.send_keys(self.yamlOperation.get_locator('Modify','CustomerMobile'),phone)#修改手机号
        self.log.get_mes('修改手机号', 'info')
        self.lp.bo.click_element(self.yamlOperation.get_locator('Modify','Submit'))  # 点击提交
        time.sleep(1)
        self.log.get_mes('点击提交', 'info')
        time.sleep(3)
   # 获取弹窗信息
    def add_alert_text(self):
        alert = Alert(self.lp.bo.driver)
        return alert.text
# if __name__ == '__main__':
#     cp=CustomerPage()
#     cp.customer_add(name='jack',Birthday='2020-10-14 16:32:02',customerAddMan='dawei',Email='1431714026@qq.com')
#     # cp.modify('15608414026')
#     a=cp.check_db_name('select * from customer_info')
#     print(a)

