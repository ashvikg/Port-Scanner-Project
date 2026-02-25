📌 Project Title

Simple Port Scanner using Python

🧠 Project Description

This project is a basic cybersecurity tool that scans a target system to identify open TCP ports.
It helps understand how network services work and demonstrates the fundamentals of ethical hacking and vulnerability assessment.

The scanner attempts to connect to multiple ports on a target IP or domain and displays which ports are open.

🎯 Features

Scan ports from 1 to 100

Accepts IP address or domain name

Detects open ports

Simple and beginner-friendly Python code

Useful for cybersecurity learning projects

🛠️ Technologies Used

Python 3

Socket Programming (Built-in Library)

📂 Project Structure
PortScannerProject/
│
├── scanner.py
└── README.md
▶️ How to Run
1️⃣ Install Python

Check Python installation:

python --version
2️⃣ Run the Program

Open terminal in project folder and run:

python scanner.py
3️⃣ Enter Target

Example:

Enter target (IP or domain): scanme.nmap.org
⚙️ How It Works

Converts domain name into IP address

Loops through ports 1–100

Uses TCP socket connection

If connection succeeds → port is OPEN

🔒 Ethical Use Warning

This tool is for educational purposes only.
Do NOT scan networks or systems without permission.

🚀 Future Improvements

Multithreading for faster scanning

Custom port ranges

Banner grabbing (service detection)

Save scan results to file

GUI or Web Interface

