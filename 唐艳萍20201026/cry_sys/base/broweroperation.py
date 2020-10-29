
from selenium.webdriver.common.alert import Alert


class BrowserOperation:
    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not found')
    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, 'url address error')
    #获取弹出文本
    def alert_text(self):
        alert = Alert(self.driver)
        return alert.text
    #切换框架
    def change_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)
    #清除
    def clear(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).clear()
        except Exception as e:
            print(e,'element not found')







# if __name__ == '__main__':
#     ub=UseBrowser()
#     bo=BrowserOperation(UseBrowser.driver)
#     bo.open_url('http://www.summermori.icu:8080/crm')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/input','admin')
#     bo.send_keys('/html/body/form/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/input','123456')
#     bo.click_element('//*[@id="in1"]')
#     time.sleep(3)
#     UseBrowser.quit()