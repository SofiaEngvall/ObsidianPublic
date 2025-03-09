
```sh
Hello GET / HTTP/1.1
!!!
Hello Host: 10.10.224.11:31337
!!!
Hello User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
!!!
Hello Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
!!!
Hello Accept-Language: en-US,en;q=0.5
!!!
Hello Accept-Encoding: gzip, deflate, br
!!!
Hello Connection: keep-alive
!!!
Hello Upgrade-Insecure-Requests: 1
!!!
Hello DNT: 1
!!!
Hello Sec-GPC: 1
!!!
Hello 
!!!
```

Burp confirms it just adds Hello to the start of all the lines we send:
![[Images/Pasted image 20241016100548.png]]
