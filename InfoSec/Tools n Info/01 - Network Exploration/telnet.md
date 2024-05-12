
intended for remote admin but all clear text, not replaced with ssh

uses tcp and can be used to connect and grab the banner of any tcp service, and maybe even communicate a bit if it's not encrypted

test with web server:

`GET / HTTP/1.1`
`GET /page.html HTTP/1.1`
`host: example`
enter twice

```sh
┌──(kali㉿kali)-[~]
└─$ telnet 10.10.209.82 80
Trying 10.10.209.82...
Connected to 10.10.209.82.
Escape character is '^]'.
GET / HTTP/1.1
host: telnet

HTTP/1.1 200 OK
Date: Sat, 04 May 2024 15:19:19 GMT
Server: Apache/2.4.10 (Debian)
Last-Modified: Mon, 30 Aug 2021 12:09:24 GMT
ETag: "15-5cac5b436ddfa"
Accept-Ranges: bytes
Content-Length: 21
Content-Type: text/html

Telnet to port 80...
Connection closed by foreign host.
```

you could connect to a mail server and try smtp or pop3 commands

