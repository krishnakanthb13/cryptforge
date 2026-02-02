import json
import os
import datetime
from typing import List, Dict
from config import HISTORY_FILE

def load_history() -> List[Dict]:
    """Loads the operation history from the JSON file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_history_entry(operation: str, file_path: str, logic: str, status: str):
    """Saves a new entry to the history file."""
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "operation": operation,
        "file_path": file_path,
        "logic": logic,
        "status": status
    }
    
    history = load_history()
    history.append(entry)
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def get_recent_history(limit: int = 10) -> List[Dict]:
    """Returns the last N history entries."""
    history = load_history()
    return history[-limit:]
