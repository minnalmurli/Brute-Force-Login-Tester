# Brute Force Login Tester

## Overview
This script performs a **brute force attack** on a login page using different username and password combinations. It supports:
- **Proxy Rotation** to avoid IP blocking.
- **Random User-Agents** for stealth.
- **Automated Proxy Checking** to ensure working proxies are used.
- **Customizable Delay** to mimic human behavior.

---

## Features
- ✅ **Proxy Support**: Uses HTTP/HTTPS proxies to hide your real IP.
- ✅ **User-Agent Rotation**: Mimics real browsers to evade detection.
- ✅ **Form Field Customization**: Update field names based on the target login page.
- ✅ **Error Handling**: Skips dead proxies automatically.
- ✅ **Randomized Delay**: Prevents rate-limiting detection.

---

## Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourrepo/bruteforce-tester.git
cd bruteforce-tester
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate    # For Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## Configuration

### 🔹 **Edit Login Details**
Update the `LOGIN_URL`, `usernames`, and `passwords` in `brute_force.py`:
```python
LOGIN_URL = "https://example.com/login"
usernames = ["admin", "user", "test"]
passwords = ["password123", "123456", "admin123"]
```

### 🔹 **Set Up Proxies**

---

## Running the Script
Run the script after setting up proxies and login details:
```bash
python brute_force.py
```

✅ If a **valid username-password pair** is found, it will be displayed.

---

## Example Output
```
[+] Working proxy: http://103.21.92.34:3128
[-] Failed: Username: admin, Password: password123
[-] Failed: Username: admin, Password: 123456
[+] Success! Username: admin, Password: welcome
```

---

## ⚠️ Legal Warning
This script is intended **ONLY for ethical hacking and security testing** on systems you have permission to test. Unauthorized access to systems is **illegal** and may result in **severe penalties**.



