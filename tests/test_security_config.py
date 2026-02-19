import pytest
from unittest.mock import patch
from shadowbyte.core import security
from shadowbyte import config
import json
import os

def test_generate_password():
    pwd = security.generate_password(length=20, use_upper=True, use_symbols=True)
    assert len(pwd) == 20
    assert any(c.isupper() for c in pwd)
    assert any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in pwd)

def test_config_crud():
    """Test load and save config."""
    test_conf = "test_config.json"
    with patch("shadowbyte.config.CONFIG_FILE", test_conf):
        # Save
        data = {"theme": "dark"}
        config.save_config(data)
        
        # Load
        loaded = config.load_config()
        assert loaded["theme"] == "dark"
        
        # Cleanup
        if os.path.exists(test_conf):
            os.remove(test_conf)
