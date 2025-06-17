
```sh
┌──(kali㉿proxli)-[~]
└─$ nc 10.10.10.152 5985         
hello
HTTP/1.1 400 Bad Request
Content-Type: text/html; charset=us-ascii
Server: Microsoft-HTTPAPI/2.0
Date: Fri, 16 May 2025 14:33:55 GMT
Connection: close
Content-Length: 326

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN""http://www.w3.org/TR/html4/strict.dtd">
<HTML><HEAD><TITLE>Bad Request</TITLE>
<META HTTP-EQUIV="Content-Type" Content="text/html; charset=us-ascii"></HEAD>
<BODY><h2>Bad Request - Invalid Verb</h2>
<hr><p>HTTP Error 400. The request verb is invalid.</p>
</BODY></HTML>

```

```sh
┌──(kali㉿proxli)-[~]
└─$ nc 10.10.10.152 5985
POST /wsman HTTP/1.1
Host: 10.10.10.152
User-Agent: curl/7.55.1
Content-Type: application/soap+xml;charset=UTF-8
Content-Length: 0

HTTP/1.1 401 
Server: Microsoft-HTTPAPI/2.0
WWW-Authenticate: Negotiate
Date: Fri, 16 May 2025 14:42:35 GMT
Connection: close
Content-Length: 0


```
