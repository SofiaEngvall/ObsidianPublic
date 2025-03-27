
https://requests.readthedocs.io/en/latest/

```python
import requests

URL = "https://www.google.com"
resp = requests.get(URL)

print(resp)
```

```python
import requests

URL = "https://www.google.com/blah"
resp = requests.get(URL)

if resp.status_code == 200:
  print("Okay, all good!")
elif resp.status_code == 301:
  print("Ops, the resource has been moved!")
elif resp.status_code == 404:
  print("Oh no, the resource wasn't found!")
else:
  print(resp.status_code)
```

if json data, like:
```
> curl https://api.agify.io?name=michael

{
	name: "michael",
	age: 64,
	count: 298219
}
```

```python
import requests
import json

URL = "https://api.agify.io/?name=Marcus"
resp = requests.get(URL)

if resp.status_code == 200:
  encoded = resp.json()
  print(encoded['age'])
else:
  print(resp.status_code)
```

```python
import requests

URL = "https://www.google.com"
custom_headers = {'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'}
resp = requests.get(URL, headers=custom_headers)

if resp.status_code == 200:
  # handle the response
  print(resp.content[:100])  
else:
  print(resp.status_code)
```

POST
```python
import requests
print(requests.post(f'http://127.0.0.1:80/',data={'a': '36dafb9f1aa753e9213caf9d62b1009f'}).text)
```

~> nc 127.0.0.1 80
POST / HTTP/1.1
Host: qwerty
Content-Type: application/x-www-form-urlencoded
Content-Length: 34

a=145c6c71b5fa08c50a19733fd98f1dd9

`a` as value 36dafb9f1aa753e9213caf9d62b1009f
