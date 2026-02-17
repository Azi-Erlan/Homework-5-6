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

# update - обновление данных

update_tasks ="""
    UPDATE tasks SET task = ? WHERE id = ?
"""

delete_tasks = """
    DELETE FROM tasks WHERE id = ?
"""

insert_tasks ="""
    INSERT INTO tasks (task) VALUES (?)
"""