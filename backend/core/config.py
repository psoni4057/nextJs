from pathlib import Path
import os
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
cwd = os.getcwd()
parent_dir = os.path.dirname(cwd)
db_path = Path(parent_dir+"/backend/core/gdbr_Validator.db")

class ConfigRules:
    def __init__(self, db_path):
        self.db_paths = db_path
        
    def create_config():
        return ConfigRules(db_path)   

    def _connect(self):
        return sqlite3.connect(db_path)

    def create_table(self):
        connection = self._connect()
        cursor = connection.cursor()
        table_creation_query = """
            CREATE TABLE IF NOT EXISTS gdbr_rules(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rules TEXT NOT NULL,
                example TEXT NOT NULL
            );
        """
        cursor.execute(table_creation_query)
        connection.commit()
        connection.close()

    def insert_rule(self, rule_value, example_value):
        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM gdbr_rules WHERE rules = ?", (rule_value,))
        existing_rule = cursor.fetchone()

        if existing_rule:
            print(f"Rule '{rule_value}' already exists.")
            connection.close()
            return

        cursor.execute("INSERT INTO gdbr_rules (rules, example) VALUES (?, ?)", 
                       (rule_value, example_value))
        connection.commit()
        connection.close()

    def get_all_rules(self):
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM gdbr_rules")
        rows = cursor.fetchall()
        connection.close()
        return rows

    def get_rule_by_name(self, rule):
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM gdbr_rules WHERE rules = ?", (rule,))
        rows = cursor.fetchall()
        connection.close()
        return rows

    def update_rule(self, rule_value: str, new_example: str):
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        update_query = "UPDATE gdbr_rules SET example = ? WHERE rules = ?"
        
        try:
            cursor.execute(update_query, (new_example, rule_value))
            connection.commit()  
            
            if cursor.rowcount > 0:
                return True 
            else:
                return False  
        except sqlite3.Error as e:
            raise HTTPException(status_code=500, detail=f"Error while updating: {e}")
        finally:
            connection.close()

    def delete_rule(self, rule):
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM gdbr_rules WHERE rules = ?", (rule,))
        connection.commit()
        connection.close()

    def reset(self):
        connection = self._connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM gdbr_rules;")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='gdbr_rules';")
        connection.commit()


