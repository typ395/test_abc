import pymysql
class DbOperation():
    def __init__(self,host, user, password,database, port,charset):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.port=port
        self.chrset=charset
    #创建连接
    def get_conn(self):
        try:
            self.conn = pymysql.Connection(host=self.host, user=self.user, password=self.password,database=self.database, port=self.port, charset=self.chrset)
            return self.conn
        except Exception as e:
            print(e,'connect failed')
    #查询数据
    def search_all(self,sql):
        try:
            conn=self.get_conn()
            cur=self.conn.cursor()
            cur.execute(sql)
            conn.commit()
            res = cur.fetchall()
            return res
        except Exception as e:
            print(e,'cur exec error!')
            self.conn.rollback()
        finally:
            cur.close()



    #修改数据
    def update_data(self,sql):
        try:
            conn = self.get_conn()
            cur = conn.cursor()
            count=cur.execute(sql)
            conn.commit()

        except Exception as e:
            print(e,'cur exec error!')
            conn.rollback()
        finally:
            cur.close()
            conn.close()