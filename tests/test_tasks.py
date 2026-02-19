import pytest
from unittest.mock import patch
from shadowbyte.core import tasks
import os
import json

def test_task_lifecycle():
    """Test add, list, complete, remove tasks."""
    test_db = "test_tasks.json"
    
    with patch("shadowbyte.core.tasks.TASKS_FILE", test_db):
        # 1. Add
        tasks.add_task("Test Task", "Desc", 1)
        loaded = tasks.load_tasks()
        assert len(loaded) == 1
        assert loaded[0]["title"] == "Test Task"
        assert loaded[0]["status"] == "pending"
        
        # 2. Complete
        task_id = loaded[0]["id"]
        tasks.complete_task(task_id)
        loaded = tasks.load_tasks()
        assert loaded[0]["status"] == "completed"
        
        # 3. Remove
        tasks.remove_task(task_id)
        loaded = tasks.load_tasks()
        assert len(loaded) == 0
        
        # Cleanup
        if os.path.exists(test_db):
            os.remove(test_db)
