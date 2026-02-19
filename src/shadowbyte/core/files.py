"""
File management and encryption utilities.
"""
import hashlib
import os

from cryptography.fernet import Fernet

from shadowbyte.utils.display import print_error, print_success


def compare_directories(dir1: str, dir2: str):
    """Compares two directories."""
    if not os.path.exists(dir1) or not os.path.exists(dir2):
        print_error("One or both directories do not exist.")
        return None

    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))

    common = files1.intersection(files2)
    unique1 = files1 - files2
    unique2 = files2 - files1

    return {
        "common": list(common),
        "unique_to_dir1": list(unique1),
        "unique_to_dir2": list(unique2)
    }

def compare_file_content(file1: str, file2: str) -> bool:
    """Compares content of two files."""
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            return f1.read() == f2.read()
    except Exception as e:
        print_error(f"Error comparing files: {e}")
        return False

def generate_key():
    """Generates a key for encryption."""
    return Fernet.generate_key()

def save_key(key: bytes, filename: str = "secret.key"):
    """Saves the key to a file."""
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print_success(f"Key saved to {filename}")

def load_key(filename: str = "secret.key") -> bytes:
    """Loads the key from a file."""
    return open(filename, "rb").read()

def encrypt_file(filename: str, key: bytes):
    """Encrypts a file."""
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename + ".enc", "wb") as file:
            file.write(encrypted_data)
        print_success(f"File encrypted: {filename}.enc")
    except Exception as e:
        print_error(f"Encryption failed: {e}")

def decrypt_file(filename: str, key: bytes):
    """Decrypts a file."""
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)

        output_file = filename.replace(".enc", "")
        if output_file == filename:
            output_file += ".dec"

        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        print_success(f"File decrypted: {output_file}")
    except Exception as e:
        print_error(f"Decryption failed: {e}")

def calculate_hash(filename: str, algorithm: str = "sha256") -> str:
    """Calculates the hash of a file."""
    if not os.path.exists(filename):
        print_error(f"File not found: {filename}")
        return ""

    try:
        if algorithm.lower() == "sha256":
            hasher = hashlib.sha256()
        elif algorithm.lower() == "md5":
            hasher = hashlib.md5()
        elif algorithm.lower() == "sha1":
            hasher = hashlib.sha1()
        else:
            print_error(f"Unsupported algorithm: {algorithm}")
            return ""

        with open(filename, "rb") as f:
            # Read in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)

        return hasher.hexdigest()
    except Exception as e:
        print_error(f"Error calculating hash: {e}")
        return ""
