
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.217.143
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-28 16:10 CEST
Nmap scan report for 10.10.217.143
Host is up (0.039s latency).
Not shown: 65395 filtered tcp ports (no-response), 138 filtered tcp ports (host-unreach)
PORT     STATE  SERVICE        VERSION
22/tcp   open   ssh            OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 95:09:13:a2:6e:3f:8d:21:10:5f:97:47:b1:67:a2:be (RSA)
|   256 04:72:4a:a8:98:77:8f:53:4e:96:98:71:a9:76:8e:45 (ECDSA)
|_  256 2c:74:b8:9f:c3:f2:36:80:4a:51:c4:35:f8:1f:7a:f9 (ED25519)
4241/tcp closed vrml-multi-use

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 143.69 seconds
```