import sys
sys.path.append('D:\\测试\\selenium')
from 唐艳萍20201026.cry_sys.db.handlesql import DbOperation
class CustomerOperationDb:
    def __init__(self):
        self.dbop=DbOperation(host='106.15.34.49', user='root', password='123456',database='crm', port=3306,charset='utf8')
    def dele_customer(self,sql):
        self.dbop.update_data(sql)
    def search_customer(self,sql):
        data=self.dbop.search_all(sql)
        return data

    def add_customer_db_data(self,sql):
        lst_id_name=[]
        data=self.search_customer(sql)
        lst_id_name.append(data[0][5])
        return lst_id_name
# if __name__ == '__main__':
#     db=CustomerOperationDb()
#     db.dbop.get_conn()
#     # db.dele_customer()
#     print(db.search_customer('select * from customer_info'))