
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.235.155
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-08 21:05 CET
Nmap scan report for 10.10.235.155
Host is up (0.042s latency).
Not shown: 65520 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: HOSTEVASION
|   NetBIOS_Domain_Name: HOSTEVASION
|   NetBIOS_Computer_Name: HOSTEVASION
|   DNS_Domain_Name: HostEvasion
|   DNS_Computer_Name: HostEvasion
|   Product_Version: 10.0.17763
|_  System_Time: 2023-12-08T20:07:58+00:00
| ssl-cert: Subject: commonName=HostEvasion
| Not valid before: 2023-07-28T19:06:15
|_Not valid after:  2024-01-27T19:06:15
|_ssl-date: 2023-12-08T20:08:40+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
8000/tcp  open  http          PHP cli server 5.5 or later
|_http-title: 404 Not Found
8080/tcp  open  http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: PowerShell Script Analyser
8443/tcp  open  ssl/http      Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
|_http-title: PowerShell Script Analyser
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-12-08T20:08:03
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 204.30 seconds
```