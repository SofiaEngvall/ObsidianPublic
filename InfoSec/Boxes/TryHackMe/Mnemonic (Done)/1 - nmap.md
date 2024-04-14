```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -Pn 10.10.183.107                                                                                         
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 08:56 CET
Nmap scan report for 10.10.183.107
Host is up (0.039s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/webmasters/*
|_http-title: Site doesn´t have a title (text/html).
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.21 seconds
```

```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.183.107
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-20 08:57 CET
Nmap scan report for 10.10.183.107
Host is up (0.043s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Site doesn´t have a title (text/html).
| http-robots.txt: 1 disallowed entry 
|_/webmasters/*
|_http-server-header: Apache/2.4.29 (Ubuntu)
1337/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e0:42:c0:a5:7d:42:6f:00:22:f8:c7:54:aa:35:b9:dc (RSA)
|   256 23:eb:a9:9b:45:26:9c:a2:13:ab:c1:ce:07:2b:98:e0 (ECDSA)
|_  256 35:8f:cb:e2:0d:11:2c:0b:63:f2:bc:a0:34:f3:dc:49 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 25.57 seconds
```

Ports 21, 80 and 1337 (ssh) are open.
Ubuntu machine. Apache 2.4.29.
robots.txt exists.
