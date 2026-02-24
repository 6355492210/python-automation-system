## 🚀 Project Overview

This is a Python-based Automation System that organizes files, generates reports, and integrates with Gmail API to automate email-based workflows.

The project is designed to reduce manual effort by:
    1. Automatically organizing files (Documents, Downloads, Images)
    2. Generating structured reports
    3.Integrating with Gmail API for automated email operations
This project demonstrates real-world backend automation and API integration skills.

## 🎯 Core Features:
## 📂 File Automation
1.  Automatically sorts files into folders:
    1. Documents
    2. Downloads 
    3. Images
2.  Cleans and organizes directories
3.  Handles duplicate files safely

## 📊 Report Generation
1. Generates structured reports
2. Saves reports inside /reports directory
3. Tracks automation activity

## 📧 Gmail API Integration
1.  Secure Gmail authentication using OAuth
2.  Token-based authentication system
3.  Email service integration via Gmail API
4.  Automated email operations

## 🔐 Security
1.  Environment variables using .env
2.  OAuth credentials via client_secret.json
3.  Token storage (token_gmail_v1.pickle)

## 🛠️ Tech Stack
1.  Language: Python 3.x
2.  Libraries Used:
    1.  os
    2.  shutil
    3.  logging
    4.  datetime
    5.  dotenv
    6.  google-auth
    7.  google-api-python-client
    8.  pickle

## 📂Project Structure:

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

## ⚙️ How It Works
1. main.py acts as the entry point.
2. file_automation.py organizes files.
3. report_generator.py generates automation reports.
4. Gmail services inside /services handle authentication and email API communication.
5. Reports are saved in /reports.

## 💡 What This Project Demonstrates
1. Backend automation logic
2. Gmail API integration
3. Secure authentication handling
4. Modular project architecture
5. Clean folder structure
6. Real-world workflow automation
7. Error handling & logging

