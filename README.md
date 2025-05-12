# Tasky 📝

Tasky is a simple command-line task manager built in Python — great for learning CLI app development and DevOps basics.

## 🚀 Features

- Add, list, and manage tasks from your terminal
- Logging and simple metrics tracking
- Works in both virtual environments and Docker

---

## 🧪 Local Installation (Virtual Environment)

1. Clone the repository:
    ```bash
    git clone https://github.com/erictolson/tasky.git
    cd tasky
    ```

2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the app:
    ```bash
    pip install .
    ```

4. When you're done working:
    ```bash
    deactivate
    ```

### Example Usage
```bash
tasky add "Write better docs"
tasky list
tasky clear
```

---

## 🐳 Running in Docker (Recommended for DevOps Workflow)

1. Build the image:
    ```bash
    docker build -t tasky .
    ```

2. Run an interactive container:
    ```bash
    docker run -it --name tasky-dev tasky
    ```

3. Inside the container, use Tasky just like locally:
    ```bash
    tasky add "Dockerize the CLI"
    tasky list
    ```

4. Exit:
    ```bash
    exit
    ```

5. Restart the container later:
    ```bash
    docker start -ai tasky-dev
    ```

> You can also **persist your task data** by mounting a volume:
> ```bash
> docker run -it --name tasky-dev -v $PWD/tasks.db:/app/tasks.db tasky
> ```
> This ensures your task database is saved between container runs.

---

## 💠 Development

### Format the Code
```bash
make format
```

### Run Tests
```bash
make test
```

### Install Dev Dependencies
```bash
pip install .[dev]
```

---

## 📁 Project Structure

```
.
├── main.py              # Entry point
├── db.py                # SQLite logic
├── logger.py            # Logging/metrics
├── setup.py             # CLI setup
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📄 License

MIT License
