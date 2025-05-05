# Tasky

Tasky is a simple command-line task manager for managing your tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/erictolson/tasky.git
    cd tasky
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install .
    ```

## Usage

Once installed, you can use the `tasky` command to interact with your tasks. Here are the available commands:

### Add a Task
```bash
tasky add "Your task description"
```

### List All Tasks
```bash
tasky list
```

### Mark a Task as Done
```bash
tasky done <task_id>
```

### Delete a Task
```bash
tasky delete <task_id>
```

### Clear All Tasks
```bash
tasky clear
```

## License
MIT License