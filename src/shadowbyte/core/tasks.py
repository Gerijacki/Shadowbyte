"""
Task management module using JSON.
"""
import json
import os
from typing import List, Dict
from shadowbyte.utils.display import print_error, print_success, console
from rich.table import Table

TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    """Loads tasks from file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_tasks(tasks: List[Dict]):
    """Saves tasks to file."""
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print_error(f"Error saving tasks: {e}")

def add_task(title: str, description: str = "", priority: int = 1):
    """Adds a new task."""
    tasks = load_tasks()
    tasks.append({
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending"
    })
    save_tasks(tasks)
    print_success(f"Task '{title}' added.")

def list_tasks(show_completed: bool = False):
    """Lists all tasks."""
    tasks = load_tasks()
    table = Table(title="Shadowbyte Task Manager")
    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")
    table.add_column("Priority", style="yellow")
    table.add_column("Status", style="green")

    for task in tasks:
        if not show_completed and task["status"] == "completed":
            continue
            
        status_color = "green" if task["status"] == "completed" else "red"
        table.add_row(
            str(task["id"]),
            task["title"],
            task["description"],
            str(task["priority"]),
            f"[{status_color}]{task['status']}[/{status_color}]"
        )
    console.print(table)

def complete_task(task_id: int):
    """Marks a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            save_tasks(tasks)
            print_success(f"Task {task_id} marked as completed.")
            return
    print_error(f"Task {task_id} not found.")

def remove_task(task_id: int):
    """Removes a task."""
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print_success(f"Task {task_id} removed.")
