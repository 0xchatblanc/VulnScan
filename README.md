# VulnScan

## Description
**VulnScan** is a powerful tool designed to scan a range of ports on a target, identify open ports, associated services, and search for known vulnerabilities linked to those services. This project combines performance and simplicity for cybersecurity professionals and enthusiasts.

---

## Features
- **Ultra-Fast Asynchronous Scanning**: Scans entire port ranges (1 to 65535) using the power of `asyncio`.
- **Service Detection**: Matches open ports with their known services.
- **Vulnerability Search**: Queries a public API (like Vulners) to fetch CVEs associated with the identified services.
- **Dynamic CLI Interface**: A user-friendly and colorful command-line interface.

---

## Installation

1. **Clone the GitHub Repository**:
   ```bash
   git clone https://github.com/0xtheghost/VulnScan.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd VulnScan
   ```

3. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. **Run the Main Script**:
   ```bash
   python vulnscan.py
   ```

2. **Provide Required Information**:
   - Target IP address or domain
   - Port range to scan (default: 1 to 65535)

3. **View Results**:
   - Open ports
   - Detected services
   - Known vulnerabilities (CVEs)

### Example Execution
```
Enter target IP address: 192.168.1.1
Enter start port (default 1): 1
Enter end port (default 65535): 1024

[+] Scanning in progress...

[+] Results:
+------+--------+---------+---------------------------+
| Port | Status | Service | Known Vulnerabilities    |
+------+--------+---------+---------------------------+
|  80  | Open   |  http   | CVE-2023-XXXXX, ...      |
| 443  | Open   |  https  | None                     |
+------+--------+---------+---------------------------+
```

---

## Project Structure
```
.
├── vulnscan.py              # Main program file
├── requirements.txt         # Python dependencies list
└── README.md                # Project documentation
```

---

## Dependencies
- **Python** >= 3.7
- Required Python Modules:
  - asyncio
  - colorama
  - prettytable
  - requests
  - aiohttp

Install the dependencies with the following command:
```bash
pip install -r requirements.txt
```

---

## Contribution
Contributions are welcome!

1. **Fork the project**
2. **Create a branch for your changes**:
   ```bash
   git checkout -b feature/my-feature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add a new feature"
   ```
4. **Push your changes**:
   ```bash
   git push origin feature/my-feature
   ```
5. **Open a pull request**

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
Special thanks to all open-source libraries and the Python community for their support and tools that make this project possible!