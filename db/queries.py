# C-R-U-D


tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
    )
"""

# read - чтение

read_tasks = """
    SELECT id, task FROM tasks
"""

insert_tasks = """
    INSERT INTO tasks (task) VALUES (?)
"""

# update - обновление данных

update_tasks ="""
    UPDATE tasks SET task = ? WHERE id = ?
"""

delete_tasks = """
    DELETE FROM tasks WHERE id = ?
"""

delete_all_tasks ="""
    DELETE FROM tasks
"""