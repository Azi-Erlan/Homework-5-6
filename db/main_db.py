import sqlite3

import config
from db import queries



def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.tasks_table)

    conn.commit()
    conn.close()

def add_new_task(name):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.insert_tasks, (name,))

    conn.commit()
    conn.close()

    id = cursor.lastrowid

    return id

def edit_task(id, new_value):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.update_tasks, (new_value, id))

    conn.commit()
    conn.close()

    return id

def delete_task(id,):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_tasks, (id,))

    conn.commit()
    conn.close()

def delete_all_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.delete_all_tasks)
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()

    cursor.execute(queries.read_tasks)
    result = cursor.fetchall()

    conn.close()
    return result
    
