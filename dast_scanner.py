import requests
from config import WEBAPP_URL

test_payloads = ["' OR '1'='1", "<script>alert('XSS')</script>"]

def test_vulnerabilities():
    print(f"Running DAST tests on {WEBAPP_URL}...\n")
    for payload in test_payloads:
        data = {
            "username": payload,
            "password": "password"
        }
        try:
            response = requests.post(WEBAPP_URL, data=data, timeout=5)
            if payload in response.text:
                print(f"[!] Potential vulnerability detected with payload: {payload}")
            else:
                print(f"[+] No vulnerability detected with payload: {payload}")
        except Exception as e:
            print(f"[ERROR] Could not connect to {WEBAPP_URL}: {e}")
