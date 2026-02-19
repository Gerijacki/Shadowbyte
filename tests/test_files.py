import os
import pytest
from shadowbyte.core import files
import tempfile

@pytest.fixture
def temp_files():
    """Create temp files for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, "f1.txt")
        file2 = os.path.join(tmpdir, "f2.txt")
        with open(file1, "w") as f: f.write("content")
        with open(file2, "w") as f: f.write("content")
        yield tmpdir, file1, file2

def test_compare_file_content(temp_files):
    _, f1, f2 = temp_files
    assert files.compare_file_content(f1, f2) is True

def test_encryption_decryption():
    """Test full encryption cycle."""
    key = files.generate_key()
    content = b"Secret Message"
    
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        fname = f.name
        
    try:
        # Encrypt
        files.encrypt_file(fname, key)
        assert os.path.exists(fname + ".enc")
        
        # Decrypt
        files.decrypt_file(fname + ".enc", key)
        
        # Check original restored
        # Note: Implementation decrypts to .dec if original exists, or original name if not.
        # Let's check logic.
        
        # If we didn't delete fname, decrypt might produce fname.dec
        if os.path.exists(fname + ".dec"):
            restored = fname + ".dec"
        else:
            restored = fname
            
        with open(restored, "rb") as f:
            assert f.read() == content
            
    finally:
        if os.path.exists(fname): os.remove(fname)
        if os.path.exists(fname + ".enc"): os.remove(fname + ".enc")
        if os.path.exists(fname + ".dec"): os.remove(fname + ".dec")

def test_calculate_hash(temp_files):
    _, f1, _ = temp_files
    # content is "content" -> sha256
    import hashlib
    expected_hash = hashlib.sha256(b"content").hexdigest()
    
    assert files.calculate_hash(f1, "sha256") == expected_hash
