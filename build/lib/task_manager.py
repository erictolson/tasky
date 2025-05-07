import json
import os
from logger import logger

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r") as f:
            logger.info(f"Loading tasks from {TASKS_FILE}")
            return json.load(f)
    except json.JSONDecodeError:
        logger.error(f"Error reading {TASKS_FILE}: File is empty or corrupted.")
        return []  # fallback if file is empty or corrupted


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title):
    tasks = load_tasks()
    task_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": task_id, "title": title, "done": False})
    save_tasks(tasks)
    logger.info(f"Added task #{task_id}: {title}")
    return task_id


def list_tasks():
    tasks = load_tasks()
    return tasks


def mark_done(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            found = True
            break
    save_tasks(tasks)
    if found:
        logger.info(f"Marked task #{task_id} as done")
    else:
        logger.warning(f"Task #{task_id} not found")
    return found


def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(new_tasks)
    if len(new_tasks) < len(tasks):
        logger.info(f"Deleted task #{task_id}")
    else:
        logger.warning(f"Task #{task_id} not found")
    return len(new_tasks) < len(tasks)


def clear_tasks():
    logger.info("Clearing all tasks")
    save_tasks([])
