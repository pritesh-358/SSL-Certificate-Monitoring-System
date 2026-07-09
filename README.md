# SSL Certificate Monitoring System

<p align="center">
  <img src="images/dashboard.png" width="900" alt="Dashboard">
</p>

<p align="center">

Python • SSL Monitoring • HTML Dashboard • Email Notification • CSV Report • Task Scheduler

</p>

---

Production-ready Python application for monitoring SSL certificate expiry across multiple websites.


---

# Features

- SSL Certificate Expiry Monitoring
- Scan Multiple Websites
- Remaining Days Calculation
- SAFE / WARNING / CRITICAL Status
- CSV Report Generation
- HTML Dashboard
- HTML Email Notification
- Multiple TO / CC / BCC Support
- Configuration using `config.yaml`
- Secure SMTP Credentials using `.env`
- Rotating Log Files
- Windows Task Scheduler Support
- Production Ready Project Structure

---

# Technologies Used

- Python 3
- SSL Module
- smtplib
- PyYAML
- python-dotenv
- HTML
- CSV
- Windows Task Scheduler
- Git

---

# Project Overview

The SSL Certificate Monitoring System automatically checks the SSL certificates of websites listed in `websites.txt`.

For each website it collects:

- Common Name
- Issuer Name
- Expiry Date
- Remaining Days
- Certificate Status

After scanning all websites, the system automatically:

- Generates a CSV report
- Generates an HTML dashboard
- Sends an email notification
- Creates detailed log files
- Displays a professional console summary

---

# Project Structure

```text
SSL-CERTIFICATE-MONITOR
│
├── app
│   ├── main.py
│   ├── config_reader.py
│   ├── logger.py
│   ├── email_sender.py
│   ├── ssl_checker.py
│   ├── ssl_certificate.py
│   └── report_generator.py
│
├── config
│   └── config.yaml
│
├── reports
│   ├── ssl_report.csv
│   └── ssl_dashboard.html
│
├── logs
│
├── tests
│
├── websites.txt
├── requirements.txt
├── run_ssl_monitor.bat
├── .env
├── .gitignore
└── README.md
```

---

# Folder Description

| Folder / File | Description |
|---------------|-------------|
| `app/` | Contains all Python source code |
| `config/` | Stores application configuration |
| `reports/` | Generated CSV and HTML reports |
| `logs/` | Daily log files |
| `tests/` | Future unit and integration tests |
| `websites.txt` | List of websites to monitor |
| `.env` | SMTP credentials and environment variables |
| `.gitignore` | Files ignored by Git |
| `requirements.txt` | Python dependencies |
| `run_ssl_monitor.bat` | Starts the monitoring system |
| `README.md` | Project documentation |

---

# System Workflow

```text
Start Project
      │
      ▼
Read config.yaml
      │
      ▼
Load websites.txt
      │
      ▼
For each Website
      │
      ▼
Fetch SSL Certificate
      │
      ▼
Extract Certificate Details
      │
      ▼
Calculate Remaining Days
      │
      ▼
Determine Status
(SAFE / WARNING / CRITICAL)
      │
      ▼
Save Results
      │
      ▼
Generate CSV Report
      │
      ▼
Generate HTML Dashboard
      │
      ▼
Send Email Notification
      │
      ▼
Write Log File
      │
      ▼
Project Completed
```

---

# Architecture

```text
                 +----------------------+
                 |     config.yaml      |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   config_reader.py   |
                 +----------+-----------+
                            |
                            v
+-------------------------------------------------------------+
|                         main.py                             |
+-------------------------------------------------------------+
     |         |           |           |           |
     |         |           |           |           |
     v         v           v           v           v
ssl_checker  ssl_certificate logger report_generator email_sender
     |                                               |
     |                                               |
     +---------------------------+-------------------+
                                 |
                                 v
                          Final Reports &
                      Email Notification
```

---

# Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/<your-github-username>/ssl-certificate-monitor.git
```

Example:

```bash
git clone https://github.com/pritesh-1904/ssl-certificate-monitor.git
```

---

## Step 2: Open Project

```bash
cd ssl-certificate-monitor
```

---

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv raj
```

Activate Virtual Environment

```bash
raj\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv raj

source raj/bin/activate
```

---

## Step 4: Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Step 5: Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

## Step 6: Configure Application

Open:

```text
config/config.yaml
```

Update the email section:

```yaml
email:

  enabled: true

  sender_name: "SSL Certificate Monitoring"

  subject_prefix: "SSL Certificate Monitoring Report"

  to:

    - your_email@gmail.com

  cc:

    - manager@example.com

  bcc:

    - security@example.com
```

---

## Step 7: Add Websites

Open:

```text
websites.txt
```

Example:

```text
motoshare.in
cotocus.org
PILOTTRAININGUS.COM
```

---

## Step 8: Run the Project

```bash
python app/main.py
```

Or simply double-click:

```text
run_ssl_monitor.bat
```

---

## Step 9: Verify Output

After successful execution, the project will automatically:

- Scan all websites
- Check SSL certificates
- Calculate remaining days
- Generate CSV Report
- Generate HTML Dashboard
- Send Email Notification
- Save Logs

---

## Generated Files

```text
reports/
│
├── ssl_report.csv
└── ssl_dashboard.html
```

```text
logs/
│
└── ssl_monitor_YYYY-MM-DD.log
```

---

# Configuration Guide

The application is fully configurable using the `config/config.yaml` file.

---

## Project Configuration

```yaml
project:
  name: "SSL Certificate Monitoring System"
  version: "3.0"
  author: "Pritesh Thamke"
```

---

## SSL Scan Configuration

```yaml
scan:
  warning_days: 30
  critical_days: 7
  timeout: 10
  retry_count: 3
```

| Option | Description |
|---------|-------------|
| `warning_days` | Days before expiry when the certificate is marked as WARNING |
| `critical_days` | Days before expiry when the certificate is marked as CRITICAL |
| `timeout` | SSL connection timeout (seconds) |
| `retry_count` | Number of retry attempts for failed SSL connections |

---

## Report Configuration

```yaml
reports:
  csv: "reports/ssl_report.csv"
  html: "reports/ssl_dashboard.html"
```

This section defines where the generated reports will be saved.

---

## Email Configuration

```yaml
email:

  enabled: true

  sender_name: "SSL Certificate Monitoring"

  subject_prefix: "SSL Certificate Monitoring Report"

  to:
    - admin@example.com

  cc:
    - manager@example.com

  bcc:
    - security@example.com
```

### Email Fields

| Field | Description |
|--------|-------------|
| `to` | Primary recipients |
| `cc` | Carbon Copy recipients |
| `bcc` | Blind Carbon Copy recipients |
| `subject_prefix` | Prefix added to the email subject |

---

## Logging Configuration

```yaml
logging:
  enabled: true
  level: "INFO"
  file: "logs/ssl_monitor.log"
  console: true
```

Available log levels:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# Environment Variables

Sensitive information should never be stored in the source code.

Store SMTP credentials inside the `.env` file.

Example:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

# Windows Task Scheduler

This project supports automatic execution using Windows Task Scheduler.

## Steps

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Enter the task name (for example, `SSL Certificate Monitoring`)
4. Select the execution schedule (Daily, Weekly, etc.)
5. Choose **Start a Program**
6. Browse and select:

```text
run_ssl_monitor.bat
```

7. Save the task.
8. Test it using the **Run** option in Task Scheduler.

---

# Automation Workflow

```text
Windows Task Scheduler
          │
          ▼
run_ssl_monitor.bat
          │
          ▼
Virtual Environment
          │
          ▼
main.py
          │
          ▼
SSL Scan
          │
          ▼
Reports + Email + Logs
```

---

# Customization

You can easily customize:

- SSL warning days
- SSL critical days
- Email recipients
- Report locations
- Logging level
- SMTP settings
- Dashboard title
- Project information

without modifying the Python source code.

# Screenshots

You can add screenshots of your project here after running the application.

## Console Output

Example:

```text
======================================================================
SSL Certificate Monitoring System
======================================================================

Total Websites Found : 92

Checking Website : motoshare.in
Status           : SAFE

Checking Website : cotocus.org
Status           : SAFE

Checking Website : jetexe.com
Status           : WARNING

Checking Website : learnflying.com
Status           : SAFE

======================================================================
SSL Monitoring Completed Successfully
======================================================================
```

---

## CSV Report

Example:

| Website | Common Name | Expiry Date | Remaining Days | Status |
|----------|-------------|-------------|---------------:|--------|
| devopsschool.jp | devopsschool.jp | 12-09-2026 | 64 | SAFE |
| devopsschool.org | devopsschool.org | 16-08-2026 | 37 | SAFE |
| devopsschool.xyz | devopsschool.xyz | 07-08-2026 | 28 | WARNING |

---

## HTML Dashboard

The application automatically generates:

```text
reports/
└── ssl_dashboard.html
```

The dashboard contains:

- SSL Certificate Summary
- Website Status Table
- Remaining Days
- Color-coded Status
- Professional HTML Layout

---

## Email Notification

The application automatically sends:

- HTML Email
- CSV Attachment
- SSL Summary
- Scan Date
- Website Statistics

---

# Troubleshooting

## ModuleNotFoundError

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

## YAML Configuration Error

Check:

```text
config/config.yaml
```

Ensure the YAML indentation is correct.

---

## SMTP Authentication Failed

Verify:

- Gmail App Password
- EMAIL_ADDRESS
- EMAIL_PASSWORD
- SMTP Server
- SMTP Port

inside:

```text
.env
```

---

## SSL Connection Failed

Possible reasons:

- Website is down
- Firewall blocking connection
- Invalid domain name
- Network connectivity issue

---

## CSV Report Not Generated

Verify:

```text
reports/
```

folder exists and the application has write permission.

---

## Email Not Received

Check:

- Spam Folder
- SMTP Configuration
- Internet Connection
- Gmail App Password
- Recipient Email Address

---

# Frequently Asked Questions (FAQ)

## Can I monitor multiple websites?

Yes.

Simply add one website per line inside:

```text
websites.txt
```

---

## Can I schedule automatic monitoring?

Yes.

Use:

- Windows Task Scheduler
- Cron (Linux)

---

## Can I monitor 100+ websites?

Yes.

The project is designed to monitor multiple websites.

---

## Can I change warning days?

Yes.

Update:

```yaml
scan:
  warning_days: 30
```

inside:

```text
config/config.yaml
```

---

## Where are reports stored?

```text
reports/
```

---

## Where are logs stored?

```text
logs/
```

---

## Where are email settings stored?

SMTP credentials:

```text
.env
```

Recipients and email configuration:

```text
config/config.yaml
```

---

## Is this project production ready?

Yes.

It includes:

- Configuration Management
- Logging
- HTML Reports
- Email Notifications
- CSV Reports
- Task Scheduler Automation
- Environment Variable Support
- Modular Architecture

# Future Roadmap

The following features are planned for future releases:

## Version 3.1

- Email Template Improvements
- Better HTML Dashboard
- Performance Optimization
- Enhanced Error Handling

---

## Version 3.2

- Docker Support
- Docker Compose
- Automatic Backup
- SSL Trend Reports

---

## Version 4.0

- REST API
- Web Dashboard
- User Authentication
- Multi-User Support
- Database Integration
- SMS Notifications
- Microsoft Teams Notifications
- Slack Notifications

---

# Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

Please ensure that your code is properly tested before submitting.

---

# Coding Standards

This project follows:

- PEP 8 Coding Style
- Modular Architecture
- Production-ready Folder Structure
- Configuration-based Development
- Secure Environment Variable Management

---

# License

This project is released under the **MIT License**.

You are free to use, modify and distribute this project according to the terms of the MIT License.

---

# Author

**Pritesh Thamke**

DevOps Engineer 

GitHub:

https://github.com/pritesh-1904

---

# Project Highlights

✔ SSL Certificate Monitoring

✔ Multiple Website Support

✔ CSV Report Generation

✔ HTML Dashboard

✔ HTML Email Notification

✔ Multiple Email Recipients (TO / CC / BCC)

✔ YAML Configuration

✔ Environment Variables (.env)

✔ Rotating Log Files

✔ Windows Task Scheduler Automation

✔ Professional Logging

✔ Production-ready Architecture

---

# Version History

| Version | Description |
|----------|-------------|
| 1.0 | Initial SSL Monitoring |
| 2.0 | Reports and Email Support |
| 3.0 | Configuration System and Logging |
| 4.0 | Multi-Recipient Email Support |

---

# Support

If you find this project useful:

- Star the repository
- Fork the repository
- Share feedback
- Report issues
- Suggest improvements

---

# Acknowledgements

Special thanks to the Python open-source community and all contributors whose libraries made this project possible.

---

# Thank You

Thank you for using the **SSL Certificate Monitoring System**.

Happy Learning!
Happy Coding!
