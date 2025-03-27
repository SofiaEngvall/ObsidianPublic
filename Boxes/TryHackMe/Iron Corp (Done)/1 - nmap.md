
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.71.183
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-29 13:20 CET
Nmap scan report for 10.10.71.183
Host is up (0.075s latency).
Not shown: 65528 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
135/tcp   open  msrpc         Microsoft Windows RPC
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-03-29T12:26:59+00:00; +1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-8VMBKF3G815
|   NetBIOS_Domain_Name: WIN-8VMBKF3G815
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815
|   DNS_Domain_Name: WIN-8VMBKF3G815
|   DNS_Computer_Name: WIN-8VMBKF3G815
|   Product_Version: 10.0.14393
|_  System_Time: 2024-03-29T12:26:51+00:00
| ssl-cert: Subject: commonName=WIN-8VMBKF3G815
| Not valid before: 2024-03-28T12:10:09
|_Not valid after:  2024-09-27T12:10:09
8080/tcp  open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-open-proxy: Proxy might be redirecting requests
11025/tcp open  http          Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.4.4
|_http-title: Coming Soon - Start Bootstrap Theme
| http-methods: 
|_  Potentially risky methods: TRACE
49667/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 400.19 seconds
```

53/tcp    open  domain        Simple DNS Plus

135/tcp  open  msrpc         Microsoft Windows RPC

3389/tcp open  ms-wbt-server Microsoft Terminal Services
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815

8080/tcp open  http          Microsoft IIS httpd 10.0
|_  Potentially risky methods: TRACE
11025/tcp open  http          Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
|_  Potentially risky methods: TRACE

49667/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

