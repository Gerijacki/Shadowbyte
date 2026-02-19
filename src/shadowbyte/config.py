"""
Configuration management module.
"""
import json
import os
from typing import Any

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "virustotal_api_key": "",
    "logs_enabled": False,
    "logs_folder": "./logs",
    "theme": "default"
}

def load_config() -> dict:
    """Loads configuration from file."""
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            # Merge with default to ensure all keys exist
            return {**DEFAULT_CONFIG, **config}
    except Exception:
        return DEFAULT_CONFIG

def save_config(config: dict):
    """Saves configuration to file."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")

def get_setting(key: str) -> Any:
    """Gets a specific setting."""
    config = load_config()
    return config.get(key)
