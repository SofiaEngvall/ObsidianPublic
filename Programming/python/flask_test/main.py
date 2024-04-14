import requests

login_url = "http://localhost:5000/Login"
login_data = {"username": "testo", "password": "test"}

response = requests.post(login_url, json=login_data)

if response.json().get("success"):
    print("Login successful!")
else:
    print("Login failed!")
