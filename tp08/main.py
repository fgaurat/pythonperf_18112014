import csv
import sqlite3

def main():
    sql = """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) 
    VALUES(?,?,?,?,?)
    """
    con = sqlite3.connect('customers_db.db')

    with open('MOCK_DATA.csv') as f:
        data = csv.DictReader(f)
        for d in data:
            del d["id"]
            print(d)
            values = list(d.values())
            con.execute(sql,values)
    
    
    con.commit()
    con.close()
if __name__=='__main__':
    main()
