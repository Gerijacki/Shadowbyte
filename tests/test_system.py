import pytest
from unittest.mock import patch, MagicMock
from shadowbyte.core import system

def test_get_system_info():
    """Test that system info returns essential keys."""
    info = system.get_system_info()
    assert "OS" in info
    assert "Python" in info
    assert "CPU Cores" in info

def test_get_disk_info():
    """Test disk info returns valid data."""
    # We mock psutil to avoid actual disk reads if needed, 
    # but for now we just check struct since it's read-only
    disk = system.get_disk_info()
    assert "Total" in disk
    assert "Free" in disk

@patch("shadowbyte.core.system.shutil.which")
@patch("shadowbyte.core.system.subprocess.run")
def test_update_system_linux(mock_run, mock_which):
    """Test update system command structure on Linux."""
    with patch("platform.system", return_value="Linux"):
        mock_which.return_value = "/usr/bin/apt"
        system.update_system()
        assert mock_run.called

@patch("shadowbyte.core.system.print_error")
def test_clean_temp_files(mock_print_error):
    """Test clean temp files doesn't crash."""
    # This is risky to test for real deletions, so we just verify it runs
    # We could mock tempfile.gettempdir to a safe temp dir
    with patch("tempfile.gettempdir", return_value="/tmp/shadowbyte_test"):
        with patch("os.listdir", return_value=[]):
             system.clean_temp_files()
