from datetime import datetime
import json
from config import TASKS_FILE




def generate_new_task_id() -> int:
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
    
    if len(data["task_list"]) == 0:
        return 1
    
    last_task = data["task_list"][-1]

    return last_task["id"] + 1

def get_current_time_str() -> str:
    current_time = datetime.now()
    
    return current_time.strftime("%m/%d/%Y, %H:%M:%S")