import argparse
import db
import logger


def main():
    parser = argparse.ArgumentParser(description="Tasky CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # List tasks
    subparsers.add_parser("list", help="List all tasks")

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", type=int, help="ID of the task to delete")

    # Clear all tasks
    subparsers.add_parser("clear", help="Clear all tasks")

    args = parser.parse_args()

    # Initialize database
    db.init_db()

    if args.command == "add":
        db.add_task(args.description)
        logger.log("add", args.description)

    elif args.command == "list":
        tasks = db.list_tasks()
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(
                f"{task['id']}. {task['description']} {'[x]' if task['completed'] else ''}"
            )
        logger.log("list", f"{len(tasks)} task(s)")

    elif args.command == "delete":
        db.delete_task(args.task_id)
        logger.log("delete", f"Task {args.task_id}")

    elif args.command == "clear":
        db.clear_tasks()
        logger.log("clear", "All tasks cleared")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
