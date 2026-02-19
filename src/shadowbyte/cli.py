"""
Main CLI entry point for Shadowbyte.
"""
import os
from typing import Optional

import typer
from rich.panel import Panel
from rich.table import Table

from shadowbyte import config
from shadowbyte.core import files, media, network, security, system, tasks
from shadowbyte.utils.display import console, print_banner

app = typer.Typer(
    name="shadowbyte",
    help="Professional System & Network Toolkit",
    add_completion=False,
)

# Sub-commands
tasks_app = typer.Typer(help="Task management commands")
app.add_typer(tasks_app, name="tasks")

files_app = typer.Typer(help="File management and encryption")
app.add_typer(files_app, name="files")

network_app = typer.Typer(help="Network scanning and tools")
app.add_typer(network_app, name="network")

security_app = typer.Typer(help="Security tools")
app.add_typer(security_app, name="security")

media_app = typer.Typer(help="Media tools")
app.add_typer(media_app, name="media")


@tasks_app.command("list")
def tasks_list_cmd(
    show_completed: bool = typer.Option(False, "--completed", "-c", help="Show completed tasks")
) -> None:
    """List all tasks."""
    tasks.list_tasks(show_completed)

@tasks_app.command("add")
def tasks_add_cmd(
    title: str,
    desc: str = typer.Option("", help="Task description"),
    priority: int = typer.Option(1, help="Priority (1-5)")
) -> None:
    """Add a new task."""
    tasks.add_task(title, desc, priority)

@tasks_app.command("complete")
def tasks_complete_cmd(task_id: int) -> None:
    """Mark a task as completed."""
    tasks.complete_task(task_id)

@tasks_app.command("remove")
def tasks_remove_cmd(task_id: int) -> None:
    """Remove a task."""
    tasks.remove_task(task_id)


# Media Commands
@media_app.command("qr")
def media_qr_cmd(
    data: str,
    output: str = typer.Option("qrcode.png", help="Output filename")
) -> None:
    """Generate a QR code."""
    media.generate_qr_code(data, output)

@media_app.command("dl")
def media_yt_cmd(
    url: str,
    output: str = typer.Option(".", help="Output directory")
) -> None:
    """Download a video."""
    media.download_video(url, output)


# Security Commands
@security_app.command("gen-pass")
def security_password_cmd(
    length: int = typer.Option(12, help="Password length"),
    no_symbols: bool = typer.Option(False, help="Exclude symbols"),
    no_upper: bool = typer.Option(False, help="Exclude uppercase")
) -> None:
    """Generate a secure password."""
    password = security.generate_password(length, not no_upper, not no_symbols)
    console.print(f"[bold green]Generated Password:[/bold green] {password}")

@security_app.command("vt-scan")
def security_vt_cmd(file: str) -> None:
    """Scan a file with VirusTotal."""
    security.scan_file_virustotal(file)

@security_app.command("config")
def security_config_cmd(
    key: Optional[str] = typer.Option(None, help="Config key to set"),
    value: Optional[str] = typer.Option(None, help="Value to set")
) -> None:
    """View or update configuration."""
    current_config = config.load_config()

    if key and value:
        current_config[key] = value
        config.save_config(current_config)
        console.print(f"[green]Updated {key} to {value}[/green]")
    else:
        console.print(current_config)


# File Commands
@files_app.command("compare-dirs")
def files_compare_dirs_cmd(dir1: str, dir2: str) -> None:
    """Compare two directories."""
    result = files.compare_directories(dir1, dir2)
    if result:
        console.print(result)

@files_app.command("encrypt")
def files_encrypt_cmd(
    file: str,
    key_file: str = typer.Option("secret.key", help="Key file path"),
    generate: bool = typer.Option(False, help="Generate new key")
) -> None:
    """Encrypt a file."""
    if generate:
        key_bytes = files.generate_key()
        files.save_key(key_bytes, key_file)
    elif not os.path.exists(key_file):
        console.print("[red]Key file not found![/red]")
        return
    else:
        # Just to ensure key exists for typing, though logic above handles flow
        pass

    key_bytes = files.load_key(key_file)
    files.encrypt_file(file, key_bytes)

@files_app.command("decrypt")
def files_decrypt_cmd(
    file: str,
    key_file: str = typer.Option("secret.key", help="Key file path")
) -> None:
    """Decrypt a file."""
    if not os.path.exists(key_file):
        console.print("[red]Key file not found![/red]")
        return

    key_bytes = files.load_key(key_file)
    files.decrypt_file(file, key_bytes)

@files_app.command("hash")
def files_hash_cmd(file: str, algo: str = "sha256") -> None:
    """Calculate file hash."""
    result = files.calculate_hash(file, algo)
    console.print(f"[bold]{algo.upper()}:[/bold] {result}")


# Network Commands
@network_app.command("info")
def network_info_cmd() -> None:
    """Show network information."""
    info = network.get_network_info()
    public_ip = network.get_public_ip()

    console.print(f"[bold]Host:[/bold] {info['Host Name']} ({info['Host IP']})")
    console.print(f"[bold]Public IP:[/bold] {public_ip}")

    # Helper for generic dict access
    interfaces = info.get("Interfaces", {})
    if isinstance(interfaces, dict):
        for iface, details in interfaces.items():
            console.print(Panel.fit(
                str(details),
                title=f"Interface: {iface}",
                border_style="green"
            ))

@network_app.command("speedtest")
def network_speedtest_cmd() -> None:
    """Run internet speed test."""
    result = network.run_speedtest()
    if result:
        console.print(Panel.fit(
            f"Download: {result['Download']}\nUpload: {result['Upload']}\nPing: {result['Ping']}",
            title="Speedtest Results",
            border_style="blue"
        ))

@network_app.command("scan")
def network_scan_cmd(range: str = typer.Argument("192.168.1.1/24")) -> None:
    """Scan local network for devices (Requires Root)."""
    devices = network.scan_network_arp(range)

    if devices:
        table = Table(title=f"Network Scan: {range}")
        table.add_column("IP Address", style="green")
        table.add_column("MAC Address", style="magenta")

        for device in devices:
            table.add_row(device['ip'], device['mac'])

        console.print(table)
    else:
        console.print("[yellow]No devices found or permission denied.[/yellow]")

@network_app.command("port-scan")
def network_portscan_cmd(
    target: str,
    ports: str = typer.Option("21,22,80,443,3306,8080", help="Comma-separated list of ports")
) -> None:
    """Scan open ports on target."""
    port_list = [int(p.strip()) for p in ports.split(",")]
    open_ports = network.scan_ports(target, port_list)

    if open_ports:
        console.print(Panel.fit(
            f"Open Ports on {target}: {', '.join(map(str, open_ports))}",
            title="Port Scan Results",
            border_style="green"
        ))
    else:
        console.print(f"[yellow]No open ports found on {target} (checked {len(port_list)} ports).[/yellow]")

@network_app.command("dns")
def network_dns_cmd(domain: str) -> None:
    """DNS Lookup."""
    result = network.dns_lookup(domain)
    if result:
        console.print(Panel.fit(
            str(result),
            title=f"DNS Lookup: {domain}",
            border_style="cyan"
        ))


# System Commands (now top-level)
@app.command()
def info() -> None:
    """Show system information."""
    info = system.get_system_info()
    disk = system.get_disk_info()

    console.print(Panel.fit(
        "\n".join([f"[bold]{k}:[/bold] {v}" for k, v in info.items()]),
        title="System Info",
        border_style="blue"
    ))
    console.print(Panel.fit(
        "\n".join([f"[bold]{k}:[/bold] {v}" for k, v in disk.items()]),
        title="Disk Info",
        border_style="magenta"
    ))

@app.command("clean")
def clean_cmd() -> None:
    """Clean temporary files."""
    system.clean_temp_files()

@app.command("update")
def update_cmd() -> None:
    """Update system packages."""
    system.update_system()

@app.command("monitor")
def monitor_cmd() -> None:
    """Run real-time system monitor."""
    system.run_monitor()

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """
    Shadowbyte - Professional System & Network Toolkit
    """
    if ctx.invoked_subcommand is None:
        print_banner()
        console.print("[bold yellow]Use --help to see available commands.[/bold yellow]")
        # raise typer.Exit()


if __name__ == "__main__":
    app()
