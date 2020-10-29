import  logging
import time
class AutoLog:
    def __init__(self):
        self.logger=logging.getLogger('log')
    def get_mes(self,mess,level_p):
        try:
            now_data = time.strftime('%Y-%m-%d', time.localtime())  # 创建时间
            fh = logging.FileHandler('D:\\测试\\selenium\\唐艳萍20201026\\cry_sys\\log_info\\auto' + now_data + '.log')  # 创建文件handle
            ch = logging.StreamHandler()  # 创建控制台handle
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')  # 数据格式化
            fh.setFormatter(fm)  # 文件加入格式数据
            ch.setFormatter(fm)  # 控制台加入格式数据
            self.logger.addHandler(fh)  # 文件句柄加入logger
            self.logger.addHandler(ch)  # 控制台句柄加入Logger
            self.logger.setLevel(logging.DEBUG)  # 设置打印级别，debug以上的级别都会打印
            if level_p=='info':
                self.logger.info(mess)  # 输出info
            elif level_p=='error':
                self.logger.error(mess)# 输出error
            elif level_p=='debug':
                self.logger.debug(mess)#输出debug
            self.logger.removeHandler(fh)  # 移除文件句柄
            self.logger.removeHandler(ch)  # 移除控制台句柄
        except:
            print('file exception')
        finally:
            fh.close()  # 关闭文件
# if __name__ == '__main__':
#     auto_log=AutoLog()
#     url='www.baidu.com'
#     auto_log.get_mes('打开'+url,'info')