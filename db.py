import sqlite3
from pathlib import Path

DB_PATH = Path("tasks.db")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        """
        )
        conn.commit()


def add_task(description):
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        conn.commit()


def list_tasks():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM tasks").fetchall()


def delete_task(task_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()


def clear_tasks():
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks")
        conn.commit()

def mark_task_done(task_id):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
