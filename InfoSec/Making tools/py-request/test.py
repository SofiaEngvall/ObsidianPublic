import requests

url = "https://fixitnow.se"

session = requests.Session()

try:
    response = session.get(url, headers={"user-agent": "test"})
except (requests.exceptions.Timeout, requests.exceptions.TooManyRedirects, requests.exceptions.RequestException, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
    print("No internet connection")
    exit()

if response.status_code == 200:
    print(response.headers)
    print(response.text)
