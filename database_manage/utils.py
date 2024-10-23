import os
import time as t
import sqlite3 
import json

DATA_BASE_QUERY = [
    '''CREATE TABLE USERS (
        Roll_no CHAR(11) PRIMARY KEY,
        FirstName VARCHAR(255),
        LasrName VARCHAR(255),
        Branch CHAR(4),
        Password VARCHAR(10),
        Data_path VARCHAR(50)
    );'''
]

def insert_data_in_user(RollNo, FirstName, LastName, branch, password):
    db = sqlite3.connect("./database_manage/data/database.db")
    db_cursor = db.cursor()
    path = f"./database_manage/data/users/{RollNo}/data.json"
    create_json_file(RollNo)
    query = f'''
        INSERT INTO USER (Roll_no, FirstName , LasrName, Branch, Password, Data_path)
        VALUES ({RollNo}, {FirstName}, { LastName}, {branch}, {password}, {path});
        '''
    db.execute("INSERT INTO USERS (Roll_no, FirstName , LasrName, Branch, Password, Data_path) VALUES (?, ?, ?, ?, ?, ?);", (RollNo, FirstName, LastName, branch, password, path))
    db.commit()
    db.close()

def fetch_user_data(RollNo):
    db = sqlite3.connect("./database_manage/data/database.db")
    db_cursor = db.cursor()
    db_cursor.execute("SELECT * FROM USERS WHERE Roll_no = ?", (RollNo,))
    data = db_cursor.fetchall()
    db.commit()
    db.close()
    return data

def basic_setup():
    for i in DATA_BASE_QUERY:
        run(i)

def run(query,):
    db = sqlite3.connect("./database_manage/data/database.db")
    db_cursor = db.cursor()
    db_cursor.execute(query)
    rows = db_cursor.fetchall()
    db.commit()
    db.close()
    return rows

def create_json_file(Roll_no):
    try:
        os.mkdir(f"./database_manage/data/users/{Roll_no}")
    except PermissionError:
        print("Access_Denied...")
    except FileExistsError:
        print("user_data_exists....")
    except Exception as e:
        print(e)

    with open(f"./database_manage/data/users/{Roll_no}/data.json", "w") as file:
        pass
    # print(f"Directory '{directory_name}' created successfully.")

"""
    task object 
    {
        "time_slot':"",
        "task":"someting"
        "priority":"some number"
    }
"""

def append_task(roll_no, time_slot, task, priority):
    data = {
        "time_slot":time_slot,
        "task":task,
        "priority":priority
    }
    user = fetch_user_data(roll_no)
    path = user[0][-1]
    with open(path, "w+") as file:
        d = json.load(file)
        pass