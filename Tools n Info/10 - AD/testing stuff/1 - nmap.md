
```sh
┌──(fixit42㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.200.78.101
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-24 17:22 CEST
Nmap scan report for 10.200.78.101
Host is up (0.039s latency).
Not shown: 65514 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
22/tcp    open  ssh           OpenSSH for_Windows_8.1 (protocol 2.0)
| ssh-hostkey: 
|   3072 87:4c:ef:4c:bf:9b:eb:32:89:e0:c4:ba:8b:23:84:c5 (RSA)
|   256 b7:ad:cc:81:7a:7f:72:69:09:3d:98:99:4c:ea:8d:2d (ECDSA)
|_  256 73:e4:2e:a5:8e:0f:5a:a7:57:27:2f:f3:d2:6c:e4:78 (ED25519)
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-24 15:23:57Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: za.tryhackme.com0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: za.tryhackme.com0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=THMDC.za.tryhackme.com
| Not valid before: 2025-07-23T06:08:19
|_Not valid after:  2026-01-22T06:08:19
|_ssl-date: 2025-07-24T15:25:26+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: ZA
|   NetBIOS_Domain_Name: ZA
|   NetBIOS_Computer_Name: THMDC
|   DNS_Domain_Name: za.tryhackme.com
|   DNS_Computer_Name: THMDC.za.tryhackme.com
|   Product_Version: 10.0.17763
|_  System_Time: 2025-07-24T15:24:46+00:00
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49671/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49704/tcp open  msrpc         Microsoft Windows RPC
49937/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: THMDC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-07-24T15:24:47
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 207.76 seconds
```