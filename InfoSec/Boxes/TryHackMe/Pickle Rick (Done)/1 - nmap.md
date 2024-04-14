
```sh
┌──(kali㉿kali)-[~/shells]
└─$ nmap -p- -min-rate=1000 -sC -sV -Pn 10.10.67.14
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-27 22:38 CET
Nmap scan report for 10.10.67.14
Host is up (0.049s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fc:43:70:35:fb:3c:f4:b1:bf:ad:f9:32:e8:59:89:cf (RSA)
|   256 f6:4d:65:98:81:4b:1a:d0:e1:78:d8:d7:9d:25:ec:ab (ECDSA)
|_  256 a1:38:9b:fa:5b:0b:c8:5f:65:d2:a3:23:bf:16:f5:4b (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Rick is sup4r cool
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.89 seconds
```

22 ssh
80 http
http-title: Rick is sup4r cool