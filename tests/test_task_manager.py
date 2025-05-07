import unittest
from task_manager import add_task, list_tasks, clear_tasks


class TaskManagerTest(unittest.TestCase):

    def setUp(self):
        clear_tasks()

    def test_add_task(self):
        add_task("Test Task")
        tasks = list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test Task")


if __name__ == "__main__":
    unittest.main()
