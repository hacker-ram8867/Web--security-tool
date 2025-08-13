# 🔐 Web Security Tool

A powerful and modular Python-based toolkit designed to automate web and network security assessments. This tool combines dynamic scanning, network analysis, and log auditing in a single, streamlined solution—ideal for penetration testers, DevSecOps teams, and cybersecurity professionals.

## 🚀 Features

- ✅ **DAST Scanner** (`dast_scanner.py`)  
  Identify common web application vulnerabilities using dynamic analysis techniques.

- 📡 **Network Scanner** (`network_scanner.py`)  
  Scan and analyze network configurations and open ports for potential security risks.

- 📊 **Log Analyzer** (`log_analyzer.py`)  
  Parse and audit web server logs to detect anomalies, brute-force attempts, or malicious access patterns.

- ⚙️ **Configurable Setup** (`config.py`)  
  Easily customizable configurations for scan depth, targets, and output preferences.

- 🔄 **Unified Execution Script** (`run_all.py`)  
  Automate and run all tools with a single command.

## 📁 File Structure

├── config.py # Configuration settings
├── dast_scanner.py # Dynamic web scanner module
├── log_analyzer.py # Log analysis module
├── network_scanner.py # Network scanning module
├── run_all.py # Master script to run all modules
├── Screenshot (615).png # Tool screenshot
├── Screenshot (616).png # Tool screenshot

bash
Copy
Edit

## 🧠 Usage

```bash
# Clone the repository
git clone https://github.com/hacker-ram8867/Web--security-tool.git
cd Web--security-tool

# Run the complete suite
python run_all.py
Customize scan targets and parameters in config.py before running.

📌 Requirements
Python 3.7+

Modules: requests, socket, re, os, etc.

Install dependencies:

pip install -r requirements.txt
(If requirements.txt is not present, manually install modules as needed.)

📷 Screenshots


🔒 Disclaimer
This tool is intended only for ethical hacking and educational purposes. Do not use it on systems or networks without proper authorization.

📫 Contact
Made with ❤️ by hacker-ram8867

⭐ Star this repository to support the project and get updates!
