import re
from collections import defaultdict
from config import LOG_FILE_PATH

log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] ".*" (\d{3}) \d+')

def analyze_logs(logfile_path=LOG_FILE_PATH):
    error_counts = defaultdict(lambda: defaultdict(int))

    try:
        with open(logfile_path, 'r') as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    ip, timestamp, status_code = match.groups()
                    if status_code.startswith('4') or status_code.startswith('5'):
                        error_counts[ip][status_code] += 1
    except FileNotFoundError:
        print(f"[ERROR] Log file not found at {logfile_path}")
        return

    print(f"\nLog Analysis Report (from {logfile_path}):")
    if not error_counts:
        print("No 4xx or 5xx errors found.")
        return

    for ip, errors in error_counts.items():
        print(f"IP: {ip}")
        for status, count in errors.items():
            print(f"  HTTP {status} errors: {count}")
