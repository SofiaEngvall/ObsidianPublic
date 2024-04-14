
Got curious about gobusters error messages on port 53
```sh
┌──(kali㉿kali)-[~/hh/vhost-basics]
└─$ nmap -sC -sV -Pn 192.168.233.2 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-26 22:59 CET
Nmap scan report for 192.168.233.2
Host is up (0.00084s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE    VERSION
53/tcp open  tcpwrapped

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.54 seconds
```