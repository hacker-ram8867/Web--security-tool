import socket
from config import NETWORK_TARGET_IP, PORTS_TO_SCAN

def scan_ports(target_ip=NETWORK_TARGET_IP, ports=PORTS_TO_SCAN):
    open_ports = []
    print(f"\nScanning ports on {target_ip}...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open.")
            open_ports.append(port)
        else:
            print(f"[CLOSED] Port {port} is closed.")
        sock.close()
    return open_ports
