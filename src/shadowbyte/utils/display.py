"""
Display utilities for Shadowbyte using Rich.
"""
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_banner():
    """Prints the Shadowbyte banner."""
    banner_text = """
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗██████╗ ██╗   ██╗████████╗███████╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║██████╔╝ ╚████╔╝    ██║   █████╗
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║██╔══██╗  ╚██╔╝     ██║   ██╔══╝
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝██████╔╝   ██║      ██║   ███████╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝
    """
    panel = Panel(
        Text(banner_text, style="bold cyan"),
        subtitle="[bold red]Professional System & Network Toolkit[/bold red]",
        border_style="blue",
    )
    console.print(panel)

def print_error(message: str):
    """Prints an error message."""
    console.print(f"[bold red]Error:[/bold red] {message}")

def print_success(message: str):
    """Prints a success message."""
    console.print(f"[bold green]Success:[/bold green] {message}")

def print_warning(message: str):
    """Prints a warning message."""
    console.print(f"[bold yellow]Warning:[/bold yellow] {message}")

def print_info(message: str):
    """Prints an info message."""
    console.print(f"[bold blue]Info:[/bold blue] {message}")
