

from  selenium import webdriver

class UseBrowser:

    driver=None

    def __init__(self):
        self.driver=webdriver.Chrome('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\chromedriver.exe')#../../cry_sys/chromedriver.exe
        self.driver.maximize_window()
        # self.driver.implicitly_wait(30)
        UseBrowser.driver=self.driver

    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()

# if __name__ == '__main__':
#     ub=UseBrowser()
#     time.sleep(4)
#     UseBrowser.quit()

