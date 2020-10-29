
import sys
sys.path.append('D:\\测试\\selenium')
from 唐艳萍20201026.cry_sys.base.broweroperation import BrowserOperation
from 唐艳萍20201026.cry_sys.base.usebrowser import UseBrowser
from 唐艳萍20201026.cry_sys.conifg.log_crm import AutoLog
from 唐艳萍20201026.cry_sys.util.yaml_operation import YamlOperation


class Login():
    def __init__(self,url):
        self.yamlOperation=YamlOperation('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\conifg\\test.yaml')
        self.log=AutoLog()#创建日志对象

        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url(url)

    def login(self,username='',password=''):
        self.log.get_mes('登录功能开始', 'info')
        self.bo.send_keys(self.yamlOperation.get_locator('LoginPage','username'), username)
        self.log.get_mes('输入用户名', 'info')
        self.bo.send_keys(self.yamlOperation.get_locator('LoginPage','password'),password)
        self.log.get_mes('输入密码', 'info')
        self.bo.click_element(self.yamlOperation.get_locator('LoginPage','submit'))
        self.log.get_mes('单击登录', 'info')


    def login_correct_text(self, frame_name, xpath):
        self.bo.change_frame(frame_name)
        success_image = self.bo.driver.find_element_by_xpath(xpath).text
        return success_image  # 当前用户：张三
# if __name__ == '__main__':
#     lo=Login('http://www.summermori.icu:8080/crm')
#     lo.login('admin','123456')
#     print(lo.login_correct_ext('topFrame','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/div'))
