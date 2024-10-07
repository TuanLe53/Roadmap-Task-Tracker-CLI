import typer
import json
from rich import print
from utils import get_current_time_str
from task import create_new_task, update_task_file, is_id_exists
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
        
    print("[bold green]Success![/bold green] New task add to to do list")
    print(new_task)
        
@app.command()
def delete(task_id: int):
    if not is_id_exists(task_id):
        print(f"[bold red]Error:[/bold red] The task with ID {task_id} does not exist.")
        return
    
    with open(TASKS_FILE, "r") as file:
        file_data = json.load(file)
        tasks = file_data["task_list"]
        
        file_data["task_list"] = [task for task in tasks if task["id"] != task_id]

    update_task_file(file_data)
    print("[bold green]Success![/bold green] The task has been deleted.")

if __name__ == "__main__":
    app() 