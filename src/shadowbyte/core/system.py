"""
System information and monitoring module.
"""
import os
import platform
import shutil
import subprocess
import tempfile
import time

import cpuinfo
import psutil
from rich.live import Live
from rich.table import Table

from shadowbyte.utils.display import console, print_error, print_info, print_success


def get_system_info():
    """Returns a dictionary with system information."""
    info = {
        "OS": f"{platform.system()} {platform.release()}",
        "OS Version": platform.version(), # Renamed to OS Version for clarity
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "Python": platform.python_version(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
    }
    try:
        cpu_details = cpuinfo.get_cpu_info()
        info["CPU Model"] = cpu_details.get('brand_raw', 'Unknown')
    except Exception:
        info["CPU Model"] = "Unknown"
    return info

def get_disk_info():
    """Returns disk usage information."""
    try:
        usage = psutil.disk_usage('/')
        return {
            "Total": f"{usage.total / (1024**3):.2f} GB",
            "Used": f"{usage.used / (1024**3):.2f} GB",
            "Free": f"{usage.free / (1024**3):.2f} GB",
            "Percent": f"{usage.percent}%"
        }
    except Exception as e:
        print_error(f"Error getting disk info: {e}")
        return {}

def clean_temp_files():
    """Cleans temporary files."""
    temp_dir = tempfile.gettempdir()

    print_info(f"Cleaning temporary files in {temp_dir}...")
    file_count = 0
    error_count = 0

    # In strict mode, we might want to be careful.
    # For now, let's just delete files inside temp, avoiding subdirectories for safety unless specified
    try:
        if os.path.exists(temp_dir):
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        file_count += 1
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        file_count += 1
                except Exception:
                    error_count += 1
        print_success(f"Cleaned {file_count} items. ({error_count} failed)")
    except Exception as e:
        print_error(f"Failed to clean temp files: {e}")

def update_system():
    """Updates the system packages."""
    system = platform.system().lower()
    commands = []

    if system == "linux":
        # Check for apt
        if shutil.which("apt"):
            commands = [
                "sudo apt update",
                "sudo apt upgrade -y"
            ]
        elif shutil.which("dnf"):
            commands = ["sudo dnf update -y"]
        elif shutil.which("pacman"):
            commands = ["sudo pacman -Syu --noconfirm"]
    elif system == "windows":
        commands = ["winget upgrade --all"]
    elif system == "darwin": # MacOS
        if shutil.which("brew"):
            commands = ["brew update", "brew upgrade"]

    if not commands:
        print_error("Unsupported package manager or OS.")
        return

    print_info("Starting system update...")
    for cmd in commands:
        console.print(f"[dim]Running: {cmd}[/dim]")
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError:
            print_error(f"Command failed: {cmd}")
            return
    print_success("System update update completed.")

def generate_dashboard_table() -> Table:
    """Generates the realtime system monitor table."""
    table = Table(title="System Monitor", expand=True)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    # CPU
    cpu_percent = psutil.cpu_percent()
    table.add_row("CPU Usage", f"{cpu_percent}%")

    # RAM
    ram = psutil.virtual_memory()
    table.add_row("RAM Usage", f"{ram.percent}% ({ram.used / (1024**3):.1f}/{ram.total / (1024**3):.1f} GB)")

    # Disk
    disk = psutil.disk_usage('/')
    table.add_row("Disk Usage", f"{disk.percent}% ({disk.free / (1024**3):.1f} GB Free)")

    # Network
    net = psutil.net_io_counters()
    table.add_row("Net Sent", f"{net.bytes_sent / (1024**2):.1f} MB")
    table.add_row("Net Recv", f"{net.bytes_recv / (1024**2):.1f} MB")

    return table

def run_monitor():
    """Runs the real-time system monitor."""
    print_info("Starting System Monitor (Press Ctrl+C to stop)...")
    try:
        with Live(generate_dashboard_table(), refresh_per_second=1) as live:
            while True:
                time.sleep(1)
                live.update(generate_dashboard_table())
    except KeyboardInterrupt:
        print_info("Monitor stopped.")
