```http
GET /api/ HTTP/1.1
Host: store-zeus.earth.ctfio.com
User-Agent: Fuzz Faster U Fool v2.1.0-dev
Accept-Encoding: gzip, deflate, br
Connection: close

```

```http
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 27 Feb 2024 00:35:31 GMT
Content-Type: application/json
Connection: close
Content-Length: 84

{"message":"Customer API Home","flag":"FLAG_FOUR{6fc5e770a9add1e15ee74eddb07425d1}"}
```