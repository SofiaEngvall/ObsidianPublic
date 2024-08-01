
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.11.251
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-29 19:29 CET
Nmap scan report for 10.10.11.251
Host is up (0.041s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 10.0
|_http-title: pov.htb
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 161.42 seconds

┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.11.251
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-29 19:29 CET
Nmap scan report for 10.10.11.251
Host is up (0.041s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Microsoft IIS httpd 10.0
|_http-title: pov.htb
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 161.42 seconds

┌──(kali㉿kali)-[~]
└─$ sudo nmap -p- -sU 10.10.11.251
[sudo] password for kali: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-29 20:15 CET
Stats: 0:00:03 elapsed; 0 hosts completed (1 up), 1 undergoing UDP Scan
UDP Scan Timing: About 0.08% done
Nmap scan report for 10.10.11.251
Host is up (0.040s latency).
All 65535 scanned ports on 10.10.11.251 are in ignored states.
Not shown: 65535 open|filtered udp ports (no-response)

Nmap done: 1 IP address (1 host up) scanned in 2617.67 seconds
```