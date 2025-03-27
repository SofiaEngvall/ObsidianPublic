
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV 10.10.11.219  
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-24 17:40 CEST
Nmap scan report for pilgrimage.htb (10.10.11.219)
Host is up (0.037s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey:
|   3072 20:be:60:d2:95:f6:28:c1:b7:e9:e8:17:06:f1:68:f3 (RSA)
|   256 0e:b6:a6:a8:c9:9b:41:73:74:6e:70:18:0d:5f:e0:af (ECDSA)
|_  256 d1:4e:29:3c:70:86:69:b4:d7:2c:c8:0b:48:6e:98:04 (ED25519)
80/tcp open  http nginx 1.18.0
| http-cookie-flags:
|   /:
| PHPSESSID:
|_  httponly flag not set
|_http-title: Pilgrimage - Shrink Your Images
|_http-server-header: nginx/1.18.0
| http-git:
|   10.10.11.219:80/.git/
| Git repository found!
| Repository description: Unnamed repository; edit this file 'description' to name the...
|_ Last commit message: Pilgrimage image shrinking service initial commit. # Please ...
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
  
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.29 seconds
```

