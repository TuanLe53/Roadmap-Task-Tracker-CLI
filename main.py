import typer
import json
from utils import get_current_time_str
from task import create_new_task, update_task_file
from config import TASKS_FILE

app = typer.Typer()

@app.command()
def add(description: str):
    new_task = create_new_task(description)
    
    with open(TASKS_FILE, "r+") as file:
        file_data = json.load(file)
        file_data["task_list"].append(new_task)
        file.seek(0)
        json.dump(file_data, file, indent=4)

if __name__ == "__main__":
    app() 