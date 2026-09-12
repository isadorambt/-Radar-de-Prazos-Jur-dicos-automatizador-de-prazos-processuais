<div align="center">

# ⚖️ Legal Deadline Radar

**Automated Legal Deadline Calculator & Process Management System**

> *Bridging Law & Technology: Automating judicial deadlines with Python*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-3ddc84?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-informational?style=for-the-badge)

</div>

---

## 📌 Project Overview

A Python-based automated system that calculates legal deadline deadlines while accounting for business days, national holidays, and judicial recesses.

**The Challenge:** In Brazilian law, missing a procedural deadline can result in losing your case. Missing by even one day can be catastrophic.

**The Solution:** This project combines legal expertise with Python automation to ensure no deadline is missed. It intelligently calculates final dates by accounting for:
- ✅ Business days only (excluding weekends)
- ✅ National Brazilian holidays
- ✅ Judicial recess period (Dec 20 - Jan 20)
- ✅ Multiple cases tracked simultaneously
- ✅ Automatic email alerts for urgent cases
- ✅ Visual dashboard for case management

---

## ⚙️ What the System Does

1. **Calculates final deadline dates** from a starting date + number of business days
2. **Automatically skips** Saturdays, Sundays, and fixed national holidays
3. **Considers judicial recess** (December 20 - January 20)
4. **Displays countdown** showing days remaining until deadline
5. **Prioritizes cases** by urgency level
6. **Sends automatic alerts** when deadlines are within 3 days
7. **Provides visual dashboard** for easy case tracking

---

## 🚀 Quick Start

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)

### Installation

```bash
# Clone the repository
git clone https://github.com/isadorambt/-Radar-de-Prazos-Jur-dicos-automatizador-de-prazos-processuais.git
cd Radar-de-Prazos-Juridicos

# Install dependencies
pip install streamlit pandas
```

---

## 📊 Project Versions

### **V1: Single Deadline Calculator**
Command-line tool for calculating a single deadline.

```bash
python radar_prazos_v1.py
```

**Input Example:**
```
Starting date: 01/09/2026
Business days: 15
```

**Output:**
```
📅 Final deadline: 23/09/2026
⏳ Days remaining: 14 business days
```

---

### **V2: Batch Process Management**
Read and manage multiple cases from a spreadsheet, sorted by urgency.

**CSV Format (`processos.csv`):**
```csv
process_number,start_date,business_days
0001234-56.2025.8.25.0001,01/09/2026,5
0007891-23.2025.8.25.0002,03/09/2026,15
```

**Run:**
```bash
python radar_prazos_v2.py
```

**Priority Indicators:**
- 🔴 **Critical** (deadline today)
- 🟡 **Urgent** (1-3 days)
- 🟢 **Healthy** (4+ days)
- ❌ **Overdue** (missed deadline)

---

### **V3: Automatic Email Alerts**
Automatically sends email notifications when deadlines are within 3 days.

**Setup (One-time configuration):**

1. Enable 2FA on your Google account: [myaccount.google.com/security](https://myaccount.google.com/security)
2. Generate an app password: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Set environment variables:

**Mac/Linux:**
```bash
export EMAIL_SENDER="youremail@gmail.com"
export EMAIL_APP_PASSWORD="16-character password from Google"
```

**Windows (cmd):**
```cmd
set EMAIL_SENDER=youremail@gmail.com
set EMAIL_APP_PASSWORD=16-character password from Google
```

**Run:**
```bash
python radar_prazos_v3.py
```

> ⚠️ **Never hardcode credentials in your code.** Always use environment variables.

---

### **V4: Visual Dashboard (Streamlit)**
Interactive web interface for managing cases without touching the terminal.

**Run:**
```bash
streamlit run radar_prazos_v4.py
```

Opens automatically at `http://localhost:8501`

**Features:**
- 📊 Visual case list sorted by urgency
- ➕ Add new cases via web form
- 🔍 Quick deadline lookup
- 📈 Real-time countdown
- 🎯 Priority-based color coding

---

## 🔒 Security & Privacy

Since this project handles sensitive legal data:

**✅ Best Practices Implemented:**
- **No credentials in code** — Email credentials (V3) read from environment variables only
- **No sensitive data versioned** — `processos.csv` in `.gitignore` (never pushed to GitHub)
- **Client-side only** — Streamlit interface runs locally on `localhost`, not exposed to internet
- **Professional confidentiality** — Process numbers, party names, case details remain private
- **Secure installation** — Dependencies installed from official PyPI repository only

> ⚠️ If you accidentally pushed `processos.csv` before adding `.gitignore`, use `git filter-branch` or GitHub's security features to remove it from history.

---

## 🗺️ Version Roadmap

| Version | Feature | Status |
|---------|---------|--------|
| V1 | Single deadline calculator (CLI) | ✅ Complete |
| V2 | Batch processing via CSV | ✅ Complete |
| V3 | Email alerts for urgent cases | ✅ Complete |
| V4 | Visual dashboard (Streamlit) | ✅ Complete |
| V5 | Database integration (planned) | 🔄 In progress |
| V6 | API for external integrations (planned) | 📋 Planned |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Core language |
| **Streamlit** | Interactive web UI |
| **Pandas** | Data manipulation & CSV handling |
| **datetime** | Date calculations |
| **smtplib** | Email notifications |
| **os** | Environment variables |

---

## 📂 Project Structure

```
.
├── radar_prazos_v1.py          # Single deadline calculator
├── radar_prazos_v2.py          # Batch process manager
├── radar_prazos_v3.py          # Email alert system
├── radar_prazos_v4.py          # Streamlit dashboard
├── processos.exemplo.csv       # Example CSV template
├── .gitignore                  # Keeps processos.csv private
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🎯 Key Features That Stand Out

✨ **Legal Domain Expertise** — Built by a lawyer who understands the pain points  
🔐 **Security-First Design** — Credentials never exposed, sensitive data protected  
📈 **Scalable Architecture** — From single deadline to 100+ cases  
🤝 **User-Friendly** — No terminal skills required with Streamlit UI  
⚖️ **Brazil-Specific** — Includes Brazilian holidays & judicial recess  
🧪 **Production-Ready** — Tested and deployable  

---

## 💡 Use Cases

- **Law Firms:** Track deadlines for all active cases
- **Solo Practitioners:** Never miss a deadline again
- **In-house Counsel:** Manage corporate legal timelines
- **Paralegals:** Automated deadline management & alerts
- **Legal Tech:** Foundation for larger case management systems

---

## 📚 Learning Outcomes

This project demonstrates:

✅ **Python fundamentals:** datetime manipulation, file I/O, automation  
✅ **Data processing:** CSV handling, Pandas aggregation  
✅ **Web frameworks:** Streamlit for rapid UI development  
✅ **Email automation:** SMTP, environment-based configuration  
✅ **Security best practices:** Credential management, data privacy  
✅ **Real-world problem solving:** Law meets technology  

---

<div align="center">

## 👩‍💼 About the Creator

**Isadora Marques** — Lawyer transitioning into tech, automating the legal world one script at a time.

*"Combining legal expertise with Python automation to solve real problems in the law firm."*

---

**Have questions or want to contribute?** Feel free to open an issue or submit a pull request!

⭐ If this project helped you, please consider giving it a star!

</div>