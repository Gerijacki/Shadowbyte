"""
Security utilities module.
"""
import string
import random
import requests
import os
from shadowbyte.config import get_setting
from shadowbyte.utils.display import print_error, print_success, print_info

def generate_password(length: int = 12, use_upper: bool = True, use_symbols: bool = True) -> str:
    """Generates a secure password."""
    chars = string.ascii_lowercase + string.digits
    if use_upper:
        chars += string.ascii_uppercase
    if use_symbols:
        chars += string.punctuation
        
    return ''.join(random.choice(chars) for _ in range(length))

def scan_file_virustotal(filepath: str):
    """Scans a file using VirusTotal API."""
    api_key = get_setting("virustotal_api_key")
    if not api_key:
        print_error("VirusTotal API Key not configured. Please set it in config.")
        return

    if not os.path.exists(filepath):
        print_error(f"File not found: {filepath}")
        return

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}
    
    print_info(f"Uploading {filepath} to VirusTotal...")
    
    try:
        with open(filepath, 'rb') as file:
            files = {'file': (os.path.basename(filepath), file)}
            response = requests.post(url, files=files, params=params)
            
            if response.status_code == 200:
                result = response.json()
                print_success("File uploaded successfully.")
                print_info(f"Scan ID: {result.get('scan_id')}")
                print_info(f"Permalink: {result.get('permalink')}")
                print_info(f"Message: {result.get('verbose_msg')}")
            elif response.status_code == 204:
                print_error("Rate limit exceeded. Please try again later.")
            else:
                print_error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print_error(f"Request failed: {e}")
