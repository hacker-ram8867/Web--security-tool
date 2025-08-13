from dast_scanner import test_vulnerabilities
from log_analyzer import analyze_logs
from network_scanner import scan_ports
from config import LOG_FILE_PATH, NETWORK_TARGET_IP, PORTS_TO_SCAN

def main():
    print("=== Starting Security Testing Framework ===\n")
    
    # Run web app DAST tests
    test_vulnerabilities()
    
    # Analyze logs
    analyze_logs(LOG_FILE_PATH)
    
    # Run network scan
    open_ports = scan_ports(NETWORK_TARGET_IP, PORTS_TO_SCAN)
    
    print("\n=== Summary Report ===")
    if open_ports:
        print(f"Open ports on {NETWORK_TARGET_IP}: {open_ports}")
    else:
        print(f"No open ports detected on {NETWORK_TARGET_IP}.")

if __name__ == "__main__":
    main()
