import json
from utils import generate_new_task_id, get_current_time_str
from config import TASKS_FILE

def create_new_task(description: str):
    id = generate_new_task_id()
    current_time_str = get_current_time_str()
    
    new_task = {
        "id": id,
        "description": description,
        "status": "todo",
        "created_at": current_time_str,
        "updated_at": current_time_str
    }

    return new_task

def update_task_file(new_file_data):
    with open(TASKS_FILE, "w") as f:
        json.dump(new_file_data, f, indent=4)