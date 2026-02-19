"""
Network utilities and scanner module.
"""
import concurrent.futures
import socket

import psutil
import requests
import speedtest
from scapy.all import ARP, Ether, srp

from shadowbyte.utils.display import print_error, print_info


def get_network_info():
    """Returns network interface information."""
    info = {}
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    info["Host Name"] = host_name
    info["Host IP"] = host_ip

    interfaces = psutil.net_if_addrs()
    iface_details = {}
    for iface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                iface_details[iface] = {
                    "IP": addr.address,
                    "Netmask": addr.netmask,
                    "Broadcast": addr.broadcast
                }
    info["Interfaces"] = iface_details
    return info

def run_speedtest():
    """Runs a internet speed test."""
    print_info("Running speed test... (this may take a while)")
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print_info("Testing download speed...")
        download = st.download() / 1_000_000  # Convert to Mbps

        print_info("Testing upload speed...")
        upload = st.upload() / 1_000_000  # Convert to Mbps

        ping = st.results.ping

        return {
            "Download": f"{download:.2f} Mbps",
            "Upload": f"{upload:.2f} Mbps",
            "Ping": f"{ping:.2f} ms"
        }
    except Exception as e:
        print_error(f"Speed test failed: {e}")
        return None

def scan_network_arp(ip_range: str = "192.168.1.1/24"):
    """Scans the local network using ARP requests."""
    print_info(f"Scanning network range: {ip_range}...")

    try:
        # Create ARP request
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # Send packet and receive response
        result = srp(packet, timeout=3, verbose=0)[0]

        devices = []
        for sent, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})

        return devices
    except PermissionError:
        print_error("Permission denied. Network scanning requires root/admin privileges.")
        return []
    except Exception as e:
        print_error(f"Scan failed: {e}")
        return []

def get_public_ip():
    """Gets the public IP address."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception:
        return "Unknown"

def dns_lookup(domain: str):
    """Resolves a domain name to an IP address."""
    try:
        ip = socket.gethostbyname(domain)
        try:
            # Try to get more info like canonical name
            fqdn = socket.getfqdn(domain)
            return {"IP": ip, "FQDN": fqdn}
        except Exception:
            return {"IP": ip}
    except socket.gaierror:
        print_error(f"Could not resolve domain: {domain}")
        return None

def scan_port(ip, port):
    """Scans a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port
    except Exception:
        pass
    return None

def scan_ports(target: str, ports: list[int]):
    """Scans a list of ports on a target IP."""
    print_info(f"Scanning ports on {target}...")
    open_ports = []

    # Resolve domain if needed
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print_error(f"Could not resolve target: {target}")
        return []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    open_ports.append(port)
            except Exception:
                pass

    return sorted(open_ports)
