# Roadmap-Task-Tracker-CLI


## Description
A command-line interface (CLI) application for tracking tasks with ease. This tool allows users to manage tasks directly from the terminal, supporting common operations such as listing, adding, updating, and marking tasks by status. Ideal for those who prefer a lightweight and efficient approach to task management.

It is inspired by the [Task Tracker](https://roadmap.sh/projects/task-tracker) project from [roadmap.sh](https://roadmap.sh/).


## Installation
1. **Clone the Repository**:
   ``` python
   git clone https://github.com/TuanLe53/Roadmap-Task-Tracker-CLI.git
   cd task-tracker-cli
2. Create and Activate a Virtual Environment
   ```sh
   python -m venv env

   # On Windows:
   .\env\Scripts\activate

   # On macOS and Linux:
   source env/bin/activate
   ```
3. Install Dependencies
   ```sh
   pip install -r requirements.txt
   ```

## Usage

- Show help
```sh
python .\main.py --help
```

- `list`: List tasks
```sh
python .\main.py list #List all tasks
python .\main.py list done #Lists all completed tasks
python .\main.py list in-progress #Lists all tasks in progress
python .\main.py list todo #Lists all pending tasks
```

- `add`: Add a task
```sh
python .\main.py add 'Task description'
```

- `delete`: Delete a task
```sh
python .\main.py delete 1
```

- `update`: Update a task
```sh
python .\main.py update 1 'New task description'
```

- `mark-done`: Mark a task as completed
```sh
python .\main.py mark_done 1
```

- `mark-in-progress`: Mark a task as in-progress
```sh
python .\main.py mark_done 1
```