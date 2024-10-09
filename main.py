import typer
import json
from rich import print
from utils import get_current_time_str
from task import create_new_task, update_task_file, is_id_exists, get_tasks_by_status
from config import TASKS_FILE

app = typer.Typer()

@app.command()
def list(status: str = "all"):
    if status == "all":        
        with open(TASKS_FILE, "r") as f:
            file_data = json.load(f)
            if len(file_data["task_list"]) == 0:
                print("You have no tasks on your list.")
            else:
                print(file_data["task_list"])
    else:
        tasks = get_tasks_by_status(status)
        if len(tasks) == 0:
            print(f"You have no tasks marked as {status}.")
        else:
            print(tasks)

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
    
@app.command()
def update(task_id: int, new_description: str):
    if not is_id_exists(task_id):
        print(f"[bold red]Error:[/bold red] The task with ID {task_id} does not exist.")
        return
    
    with open(TASKS_FILE, "r") as f:
        file_data = json.load(f)
        tasks = file_data["task_list"]
        
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updated_at"] = get_current_time_str()
        
    file_data["task_list"] = tasks    
    update_task_file(file_data)
            
    print("[bold green]Success![/bold green] The task has been updated.")
    
@app.command()
def mark_in_progress(task_id:int):
    if not is_id_exists(task_id):
        print(f"[bold red]Error:[/bold red] The task with ID {task_id} does not exist.")
        return
    
    with open(TASKS_FILE, "r") as f:
        file_data = json.load(f)
        tasks = file_data["task_list"]
        
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updated_at"] = get_current_time_str()
        
    file_data["task_list"] = tasks    
    update_task_file(file_data)
            
    print("[bold green]Success![/bold green] The task has been updated.")
        
@app.command()
def mark_done(task_id:int):
    if not is_id_exists(task_id):
        print(f"[bold red]Error:[/bold red] The task with ID {task_id} does not exist.")
        return
    
    with open(TASKS_FILE, "r") as f:
        file_data = json.load(f)
        tasks = file_data["task_list"]
        
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updated_at"] = get_current_time_str()
        
    file_data["task_list"] = tasks    
    update_task_file(file_data)
            
    print("[bold green]Success![/bold green] The task has been updated.")
    
if __name__ == "__main__":
    app() 