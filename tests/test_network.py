import pytest
from unittest.mock import patch, MagicMock
from shadowbyte.core import network

def test_get_network_info():
    info = network.get_network_info()
    assert "Host Name" in info
    assert "Interfaces" in info

@patch("shadowbyte.core.network.requests.get")
def test_get_public_ip(mock_get):
    """Test public IP retrieval."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"ip": "1.2.3.4"}
    mock_get.return_value = mock_response
    
    ip = network.get_public_ip()
    assert ip == "1.2.3.4"

@patch("shadowbyte.core.network.speedtest.Speedtest")
def test_speedtest(mock_speedtest_cls):
    """Test speedtest run."""
    mock_st = MagicMock()
    mock_st.download.return_value = 10_000_000 # 10 Mbps
    mock_st.upload.return_value = 5_000_000    # 5 Mbps
    mock_st.results.ping = 20.0
    mock_speedtest_cls.return_value = mock_st
    
    res = network.run_speedtest()
    assert res is not None
    assert "10.00 Mbps" in res["Download"]
    assert "5.00 Mbps" in res["Upload"]

@patch("shadowbyte.core.network.socket.gethostbyname")
def test_dns_lookup(mock_gethost):
    """Test DNS lookup."""
    mock_gethost.return_value = "1.1.1.1"
    res = network.dns_lookup("example.com")
    assert res["IP"] == "1.1.1.1"

@patch("shadowbyte.core.network.socket.socket")
def test_scan_ports(mock_socket_cls):
    """Test port scanning."""
    mock_socket = MagicMock()
    mock_socket.__enter__.return_value = mock_socket
    mock_socket_cls.return_value = mock_socket
    
    # Simulate port 80 open (0), port 22 closed (1)
    mock_socket.connect_ex.side_effect = lambda addr: 0 if addr[1] == 80 else 1
    
    with patch("shadowbyte.core.network.socket.gethostbyname", return_value="127.0.0.1"):
        open_ports = network.scan_ports("localhost", [22, 80])
        assert 80 in open_ports
        assert 22 not in open_ports
