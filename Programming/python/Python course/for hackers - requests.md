

`import requests`

`response = requests.get("http://our.web.page")`

add parameters and headers:
`response = requests.get("http://our.web.page",parmas ={"param_name":value},headers="header_name":"value")`
also auth, timeout, files, data..

we can also use requests.post(), requests.delete() and so on

look at headers:
```python
print(response.headers)
print(response.headers["Server"])
print(response.status_code) #200, 404 and other codes
```

test for 200 ok:
```python
if response.status_code == 200:
	print("Success - write your code here")
elif response.status_code == 301 or response.status_code == 302: #requests will auto redirect but we can set allow_redirects=False in the request
	print("redirect")
else
	print("And here for failure")
```

check time:
`response.elapsed` int

time based can also use:
TODO! add from natas scripts

Cookies:
`response.cookies` returns dictionary

Text:
`response.text` there's also `response.content` with returns the byte string instead on unicode string

Content:
if we get a data file, like an image, we can use .content to save the data to a file:
```python
with open("my_new_file","wb") as file: #remember w=write b=binary
  file.write(responce.content)
```
### Sessions

works the same as a simple request but data is kept between requests

```python
session = requests.Session()
session.cookies.update({"my_cookie":"value"})
session.get(url)
```

