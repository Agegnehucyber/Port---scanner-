 Port Scanner (Python)

A basic TCP port scanner written in Python using the `socket` module.  
This project is part of my cybersecurity learning journey, using Python to explore network security and ethical hacking tools.

Features

- Accepts target host (IP or domain) and custom ports
- Scans TCP ports and shows open/closed results
- Uses 'socket' for low-level networking
- Simple CLI interface – beginner friendly
- Easy to modify or extend

How to Run

```bash
python3 port_scanner.py

You'll be prompted to:
Enter a target IP or domain 
Enter a list of ports (e.g., 22, 80, 443)
The scanner will attempt to connect to each port and display whether it is open or closed.

Example Output

Target: 192.168.1.1
Scanning ports: 22, 80, 443...

[+] Port 22 is open
[-] Port 80 is closed
[+] Port 443 is open

Author:

Agegnehu Estifanos
Cybersecurity Analyst | Applied Mathematics Background
Focused on Python for Security • Linux Systems • Networking Fundamentals
GitHub: @AgegnehuCyber

NB:-

This tool is intended for educational and ethical use only.
Do not scan systems without permission.
It is part of my cybersecurity practice lab and portfolio building.

Future Improvements (Ideas):-

Add port range (e.g., 20–100)
Add timeout or threading for speed
Save results to a file (e.g., .txt or .json)
