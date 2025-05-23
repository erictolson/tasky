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
    parser_delete = subparsers.add_parser("delete", help="Delete a task by position")
    parser_delete.add_argument(
        "task_id", type=int, help="Position of the task to delete"
    )

    # Clear all tasks
    subparsers.add_parser("clear", help="Clear all tasks")

    # Mark task as done
    parser_done = subparsers.add_parser(
        "done", help="Mark a task as completed by position"
    )
    parser_done.add_argument(
        "task_id", type=int, help="Position of the task to mark as done"
    )

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
        else:
            for i, task in enumerate(tasks, 1):
                status = "✔" if task["completed"] else " "
                print(f"[{status}] {i}. {task['description']}")
            logger.log("list", f"{len(tasks)} task(s)")

    elif args.command == "delete":
        tasks = db.list_tasks()
        try:
            task = tasks[args.task_id - 1]
            db.delete_task(task["id"])
            logger.log("delete", f"Deleted task {task['id']}")
        except IndexError:
            print(f"No task at position {args.task_id}")

    elif args.command == "clear":
        db.clear_tasks()
        logger.log("clear", "All tasks cleared")

    elif args.command == "done":
        tasks = db.list_tasks()
        try:
            task = tasks[args.task_id - 1]
            db.mark_task_done(task["id"])
            logger.log("done", f"Marked task {task['id']} as completed")
        except IndexError:
            print(f"No task at position {args.task_id}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
