
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -Pn monitorsthree.htb
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-26 20:46 CEST
Nmap scan report for monitorsthree.htb (10.10.11.30)
Host is up (0.026s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 86:f8:7d:6f:42:91:bb:89:72:91:af:72:f3:01:ff:5b (ECDSA)
|_  256 50:f9:ed:8e:73:64:9e:aa:f6:08:95:14:f0:a6:0d:57 (ED25519)
80/tcp   open     http        nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: MonitorsThree - Networking Solutions
8084/tcp filtered websnp
9090/tcp open     zeus-admin?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 140.92 seconds
```

