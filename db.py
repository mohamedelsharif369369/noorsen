import sqlite3

class DataBase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            title text,
            price Integer,
            mdfo3 Integer,
            tarekh text,
            baqi Integer,
            me3ad text,
            phone text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,name,title,price,mdfo3,tarekh,baqi,me3ad,phone):
        self.cur.execute(
            "insert into employees values (NULL,?,?,?,?,?,?,?,?)",
            (name,title,price,mdfo3,tarekh,baqi,me3ad,phone)
            )
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    
    def update(self,id,name,title,price,mdfo3,tarekh,baqi,me3ad,phone):
        self.cur.execute(
            "update employees set name=?,title=?,price=?,mdfo3=?,tarekh=?,baqi=?,me3ad=?,phone=? where id=?",
            (name,title,price,mdfo3,tarekh,baqi,me3ad,phone, id)
            )
        self.con.commit()
    