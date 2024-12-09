from datetime import date
import os
import sqlite3
from state.datastate import DataState


cwd=os.getcwd()
parent_dir=os.path.dirname(cwd)
#print("PARENT PATH",parent_dir)
auditdb_path = os.path.join(parent_dir,"backend","core", "audit.db") 

class Audit:
    def __init__(self,auditdb_path) :
        self.auditdb_path=auditdb_path

    @staticmethod
    def create_audit():
        return Audit(auditdb_path) 

    def connect(self):
        return sqlite3.connect(self.auditdb_path)   
    
    def create_table(self):
        connection=self.connect()
        cursor=connection.cursor()
        create_table_query="""
                CREATE TABLE IF NOT EXISTS Audit(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Date date NOT NULL,
                App_Name TEXT NOT NULL,
                Model TEXT NOT NULL,
                Compliance Area DEFAULT "GDPR" NOT NULL,
                Status TEXT NOT NULL,
                Comments TEXT NOT NULL)"""
        cursor.execute(create_table_query)
        connection.commit()
        connection.close()

    def insert_values(self,dateval:str,appval:str,modelval:str,statusval:str, commentsval:str):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Audit (Date,App_Name,Model,Status,Comments) VALUES(?, ?, ?, ?, ?)",
                        (dateval,appval,modelval,statusval,commentsval ))
        connection.commit()
        connection.close()

    def get_records(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *
            FROM Audit 
            ORDER BY id DESC 
            LIMIT 10
        """)
        results= cursor.fetchall()
        connection.close()
        return results
    
audit_instance = Audit(auditdb_path)
audit_instance.create_table()
# res = audit_instance.get_records()
#print(res)