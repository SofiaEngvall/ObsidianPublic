
```sh
hacker@talking-web-level-2:~$ /challenge/run
Make an HTTP request to 127.0.0.1 on port 80 to get the flag
You must make this request using the nc command

The following output is from the server, might be useful in helping you debug:
------------------------------------------------
 * Serving Flask app 'run'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:80
Press CTRL+C to quit

hacker@talking-web-level-2:~$ nc localhost 80
GET / HTTP/1.1

HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Fri, 01 Sep 2023 00:08:19 GMT
Content-Length: 58
Server: pwn.college
Connection: close

pwn.college{AonXg6a4uvvz7Wid_Prs_wFoBIc.dljNyMDLxITM1MzW}

```
