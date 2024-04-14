
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -Pn 10.10.51.95 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-21 19:18 CET
Nmap scan report for 10.10.51.95
Host is up (0.063s latency).
Not shown: 982 filtered tcp ports (no-response), 17 filtered tcp ports (host-unreach)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 09:23:62:a2:18:62:83:69:04:40:62:32:97:ff:3c:cd (RSA)
|   256 33:66:35:36:b0:68:06:32:c1:8a:f6:01:bc:43:38:ce (ECDSA)
|_  256 14:98:e3:84:70:55:e6:60:0c:c2:09:77:f8:b7:a6:1c (ED25519)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.90 seconds
```

Only 22 :O

```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.51.95
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-21 19:18 CET
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
...
```

Adding `-min-rate=5000`

```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -min-rate=5000 -sC -sV -Pn 10.10.51.95
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-21 19:28 CET
Nmap scan report for 10.10.51.95
Host is up (0.041s latency).
Not shown: 65501 filtered tcp ports (no-response), 32 filtered tcp ports (host-unreach)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 09:23:62:a2:18:62:83:69:04:40:62:32:97:ff:3c:cd (RSA)
|   256 33:66:35:36:b0:68:06:32:c1:8a:f6:01:bc:43:38:ce (ECDSA)
|_  256 14:98:e3:84:70:55:e6:60:0c:c2:09:77:f8:b7:a6:1c (ED25519)
12340/tcp open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: We&#39;ve got some trouble | 404 - Resource not found

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.57 seconds
```
