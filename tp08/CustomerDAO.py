from Customer import Customer
import sqlite3
class CustomerDAO:
    


    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)

    def find_all(self):
        print("find_all")
        
        sql = "SELECT * FROM customers_tbl"
        cur = self.__con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            c = Customer(*row)
            yield c
    

    def __del__(self):
        self.__con.close()

