
```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.10.95                                               
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-13 17:13 CEST
Nmap scan report for 10.10.10.95
Host is up (0.023s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
8080/tcp open  http    Apache Tomcat/Coyote JSP engine 1.1
|_http-title: Apache Tomcat/7.0.88
|_http-server-header: Apache-Coyote/1.1
|_http-favicon: Apache Tomcat

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 118.34 seconds
```

