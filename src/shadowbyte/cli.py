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
from shadowbyte.utils.display import console

app = typer.Typer(
    name="shadowbyte",
    help="Professional System & Network Toolkit",
    add_completion=False,
    no_args_is_help=True,
)

# Task Commands
tasks_app = typer.Typer(help="Simple task manager")
app.add_typer(tasks_app, name="tasks")

@tasks_app.command("list")
def tasks_list_cmd(all: bool = typer.Option(False, help="Show completed tasks")):
    """List tasks."""
    tasks.list_tasks(all)

@tasks_app.command("add")
def tasks_add_cmd(
    title: str,
    desc: str = typer.Option("", help="Task description"),
    priority: int = typer.Option(1, help="Priority (1-5)")
):
    """Add a new task."""
    tasks.add_task(title, desc, priority)

@tasks_app.command("complete")
def tasks_complete_cmd(id: int):
    """Mark a task as completed."""
    tasks.complete_task(id)

@tasks_app.command("remove")
def tasks_remove_cmd(id: int):
    """Remove a task."""
    tasks.remove_task(id)

# Media Commands
media_app = typer.Typer(help="Media tools (YouTube, QR)")
app.add_typer(media_app, name="media")

@media_app.command("qr")
def media_qr_cmd(data: str, output: str = "qrcode.png"):
    """Generate a QR code."""
    media.generate_qr_code(data, output)

@media_app.command("yt")
def media_yt_cmd(url: str, output: str = "."):
    """Download a video from YouTube."""
    media.download_video(url, output)

# Security Commands
security_app = typer.Typer(help="Security tools and configuration")
app.add_typer(security_app, name="security")

@security_app.command("password")
def security_password_cmd(
    length: int = typer.Option(16, help="Length of the password"),
    symbols: bool = typer.Option(True, help="Include symbols"),
    upper: bool = typer.Option(True, help="Include uppercase letters")
):
    """Generate a secure password."""
    pwd = security.generate_password(length, upper, symbols)
    console.print(f"[bold green]Generated Password:[/bold green] {pwd}")

@security_app.command("virustotal")
def security_vt_cmd(file: str):
    """Scan a file using VirusTotal."""
    security.scan_file_virustotal(file)

@security_app.command("config")
def security_config_cmd(
    key: str = typer.Option(None, help="Config key to set"),
    value: str = typer.Option(None, help="Value to set")
):
    """View or update configuration."""
    current_config = config.load_config()

    if key and value:
        current_config[key] = value
        config.save_config(current_config)
        console.print(f"[green]Updated {key} to {value}[/green]")
    else:
        console.print(Panel.fit(
            "\n".join([f"[bold]{k}:[/bold] {v}" for k, v in current_config.items()]),
            title="Current Configuration",
            border_style="yellow"
        ))

# File Commands
files_app = typer.Typer(help="File management and encryption")
app.add_typer(files_app, name="files")

@files_app.command("compare-dirs")
def files_compare_dirs_cmd(dir1: str, dir2: str):
    """Compare content of two directories."""
    result = files.compare_directories(dir1, dir2)
    if result:
        console.print(Panel.fit(
            f"[green]Common:[/green] {len(result['common'])}\n"
            f"[blue]Unique to Dir1:[/blue] {len(result['unique_to_dir1'])}\n"
            f"[magenta]Unique to Dir2:[/magenta] {len(result['unique_to_dir2'])}",
            title="Comparison Result"
        ))
        if result['unique_to_dir1']:
            console.print(f"[bold]Unique to {dir1}:[/bold] {', '.join(result['unique_to_dir1'])}")

@files_app.command("encrypt")
def files_encrypt_cmd(file: str, key_file: str = "secret.key"):
    """Encrypt a file."""
    if not os.path.exists(key_file):
        if typer.confirm("Key file not found. Generate new key?"):
            key = files.generate_key()
            files.save_key(key, key_file)
        else:
            return

    key = files.load_key(key_file)
    files.encrypt_file(file, key)

@files_app.command("decrypt")
def files_decrypt_cmd(file: str, key_file: str = "secret.key"):
    """Decrypt a file."""
    if not os.path.exists(key_file):
        console.print("[red]Key file not found![/red]")
        return

    key = files.load_key(key_file)
    files.decrypt_file(file, key)

@files_app.command("hash")
def files_hash_cmd(file: str, algo: str = typer.Option("sha256", help="Algorithm (sha256, md5, sha1)")):
    """Calculate file hash."""
    result = files.calculate_hash(file, algo)
    if result:
        console.print(f"[bold cyan]{algo.upper()} Hash:[/bold cyan] {result}")

# Network Commands
network_app = typer.Typer(help="Network analysis and tools")
app.add_typer(network_app, name="network")

@network_app.command("info")
def network_info_cmd():
    """Show network interface information."""
    info = network.get_network_info()
    public_ip = network.get_public_ip()

    console.print(f"[bold]Host:[/bold] {info['Host Name']} ({info['Host IP']})")
    console.print(f"[bold]Public IP:[/bold] {public_ip}")

    for iface, details in info["Interfaces"].items():
        console.print(Panel.fit(
            f"IP: {details['IP']}\nNetmask: {details['Netmask']}\nBroadcast: {details['Broadcast']}",
            title=f"Interface: {iface}",
            border_style="green"
        ))

@network_app.command("speedtest")
def network_speedtest_cmd():
    """Run internet speed test."""
    results = network.run_speedtest()
    if results:
        console.print(Panel.fit(
            f"[bold green]Download:[/bold green] {results['Download']}\n"
            f"[bold blue]Upload:[/bold blue] {results['Upload']}\n"
            f"[bold yellow]Ping:[/bold yellow] {results['Ping']}",
            title="Speed Test Results",
            border_style="bold cyan"
        ))

@network_app.command("scan")
def network_scan_cmd(range: str = typer.Option("192.168.1.1/24", help="IP range to scan")):
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
):
    """Scan for open ports on a target."""
    port_list = [int(p.strip()) for p in ports.split(",")]
    open_ports = network.scan_ports(target, port_list)

    if open_ports:
        console.print(Panel.fit(
            "\n".join([f"[green]Port {p} OPEN[/green]" for p in open_ports]),
            title=f"Scan Results: {target}",
            border_style="green"
        ))
    else:
        console.print(f"[yellow]No open ports found on {target} (scanned {len(port_list)} ports)[/yellow]")

@network_app.command("dns")
def network_dns_cmd(domain: str):
    """Resolve a domain name."""
    result = network.dns_lookup(domain)
    if result:
        console.print(Panel.fit(
            f"[bold]IP:[/bold] {result['IP']}\n[bold]FQDN:[/bold] {result.get('FQDN', 'N/A')}",
            title=f"DNS Lookup: {domain}",
            border_style="blue"
        ))


# System Commands
system_app = typer.Typer(help="System information and maintenance")
app.add_typer(system_app, name="system")

@system_app.command("info")
def system_info_cmd():
    """Show system information."""
    info = system.get_system_info()
    disk = system.get_disk_info()

    console.print(Panel.fit(
        "\n".join([f"[bold]{k}:[/bold] {v}" for k, v in info.items()]),
        title="System Info",
        border_style="cyan"
    ))
    console.print(Panel.fit(
        "\n".join([f"[bold]{k}:[/bold] {v}" for k, v in disk.items()]),
        title="Disk Info",
        border_style="magenta"
    ))

@system_app.command("clean")
def system_clean_cmd():
    """Clean temporary files."""
    if typer.confirm("Are you sure you want to delete temporary files?"):
        system.clean_temp_files()

@system_app.command("update")
def system_update_cmd():
    """Update system packages."""
    if typer.confirm("Are you sure you want to update system packages?"):
        system.update_system()

@system_app.command("monitor")
def system_monitor_cmd():
    """Run real-time system monitor."""
    system.run_monitor()


@app.callback(invoke_without_command=True)
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", help="Show the application version and exit."
    ),
):
    """
    Shadowbyte: A professional toolkit for system administration, network analysis, and more.
    """
    if version:
        from shadowbyte import __version__
        console.print(f"[bold cyan]Shadowbyte[/bold cyan] version [bold green]{__version__}[/bold green]")
        raise typer.Exit()

    # If no command is provided, show banner and help
    # print_banner() # Clean but maybe too noisy for every command? Let's keep it for interactive if needed.

if __name__ == "__main__":
    app()
