import sys
from task_manager import add_task, list_tasks, mark_done, delete_task, clear_tasks

def print_usage():
    print("Usage:")
    print("  python main.py add <task description>")
    print("  python main.py list")
    print("  python main.py done <task_id>")
    print("  python main.py delete <task_id>")
    print("  python main.py clear")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: No task description provided.")
            return
        task_desc = " ".join(sys.argv[2:])
        task_id = add_task(task_desc)
        print(f"Added task #{task_id}: {task_desc}")

    elif command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✅" if task["done"] else "❌"
                print(f"{task['id']:>3}. {status} {task['title']}")

    elif command == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Error: Provide a task ID to mark as done.")
            return
        task_id = int(sys.argv[2])
        if mark_done(task_id):
            print(f"Task #{task_id} marked as done.")
        else:
            print(f"Task #{task_id} not found.")

    elif command == "delete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("Error: Provide a task ID to delete.")
            return
        task_id = int(sys.argv[2])
        if delete_task(task_id):
            print(f"Deleted task #{task_id}.")
        else:
            print(f"Task #{task_id} not found.")

    elif command == "clear":
        clear_tasks()
        print("All tasks cleared.")

    else:
        print(f"Unknown command: {command}")
        print_usage()

if __name__ == "__main__":
    main()
