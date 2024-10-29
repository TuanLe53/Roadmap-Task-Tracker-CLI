# Roadmap-Task-Tracker-CLI

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
```