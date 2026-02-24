🚀 Project Overview

This is a Python-based Automation System that organizes files, generates reports, and integrates with Gmail API to automate email-based workflows.
• The project is designed to reduce manual effort by:
    • Automatically organizing files (Documents, Downloads, Images)
    • Generating structured reports
    •Integrating with Gmail API for automated email operations
This project demonstrates real-world backend automation and API integration skills.

🎯 Core Features:
📂 File Automation
• Automatically sorts files into folders:
    • Documents
    • Downloads 
    • Images
• Cleans and organizes directories
• Handles duplicate files safely

📊 Report Generation
• Generates structured reports
• Saves reports inside /reports directory
• Tracks automation activity

📧 Gmail API Integration
• Secure Gmail authentication using OAuth
• Token-based authentication system
• Email service integration via Gmail API
• Automated email operations

🔐 Security
• Environment variables using .env
• OAuth credentials via client_secret.json
• Token storage (token_gmail_v1.pickle)

🛠️ Tech Stack
• Language: Python 3.x
• Libraries Used:
    • os
    • shutil
    • logging
    • datetime
    • dotenv
    • google-auth
    • google-api-python-client
    • pickle

📂Project Structure:

python-automation-system/
│
├── data/
├── Documents/
├── Downloads/
├── Images/
├── reports/
│
├── services/
│   ├── gmail_auth.py
│   ├── gmail_service.py
│
├── file_automation.py
├── report_generator.py
├── main.py
│
├── .env
├── client_secret.json
├── requirements.txt
└── README.md

⚙️ How It Works
1. main.py acts as the entry point.
2. file_automation.py organizes files.
3. report_generator.py generates automation reports.
4. Gmail services inside /services handle authentication and email API communication.
5. Reports are saved in /reports.

💡 What This Project Demonstrates
• Backend automation logic
• Gmail API integration
• Secure authentication handling
• Modular project architecture
• Clean folder structure
• Real-world workflow automation
• Error handling & logging

👨‍💻 Author
Vivek Vaghela
Python Developer | Backend & Automation Enthusiast
Skilled in Django, Flask, REST APIs, Automation, API Integration & Data Handling