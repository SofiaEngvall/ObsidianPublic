
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.32.52 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-11 22:50 CEST
Nmap scan report for 10.10.32.52
Host is up (0.039s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE            VERSION
21/tcp   open  ftp                Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can´t get directory listing: TIMEOUT
| ftp-syst: 
|_  SYST: Windows_NT
3389/tcp open  ssl/ms-wbt-server?
|_ssl-date: 2024-10-11T20:55:08+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=brainstorm
| Not valid before: 2024-10-10T20:46:44
|_Not valid after:  2025-04-11T20:46:44
| rdp-ntlm-info: 
|   Target_Name: BRAINSTORM
|   NetBIOS_Domain_Name: BRAINSTORM
|   NetBIOS_Computer_Name: BRAINSTORM
|   DNS_Domain_Name: brainstorm
|   DNS_Computer_Name: brainstorm
|   Product_Version: 6.1.7601
|_  System_Time: 2024-10-11T20:54:37+00:00
9999/tcp open  abyss?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, RPCCheck, RTSPRequest, SSLSessionReq, TerminalServerCookie: 
|     Welcome to Brainstorm chat (beta)
|     Please enter your username (max 20 characters): Write a message:
|   NULL: 
|     Welcome to Brainstorm chat (beta)
|_    Please enter your username (max 20 characters):
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.94SVN%I=7%D=10/11%Time=67098FF6%P=x86_64-pc-linux-gnu%
SF:r(NULL,52,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20e
SF:nter\x20your\x20username\x20\(max\x2020\x20characters\):\x20")%r(GetReq
SF:uest,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20ent
SF:er\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\x2
SF:0message:\x20")%r(HTTPOptions,63,"Welcome\x20to\x20Brainstorm\x20chat\x
SF:20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20chara
SF:cters\):\x20Write\x20a\x20message:\x20")%r(FourOhFourRequest,63,"Welcom
SF:e\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20u
SF:sername\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")
SF:%r(JavaRMI,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\
SF:x20enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x
SF:20a\x20message:\x20")%r(GenericLines,63,"Welcome\x20to\x20Brainstorm\x2
SF:0chat\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x
SF:20characters\):\x20Write\x20a\x20message:\x20")%r(RTSPRequest,63,"Welco
SF:me\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20
SF:username\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20"
SF:)%r(RPCCheck,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPleas
SF:e\x20enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write
SF:\x20a\x20message:\x20")%r(DNSVersionBindReqTCP,63,"Welcome\x20to\x20Bra
SF:instorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(m
SF:ax\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(DNSStatusRe
SF:questTCP,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x2
SF:0enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20
SF:a\x20message:\x20")%r(Help,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\
SF:(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20characte
SF:rs\):\x20Write\x20a\x20message:\x20")%r(SSLSessionReq,63,"Welcome\x20to
SF:\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20username
SF:\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(Term
SF:inalServerCookie,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nP
SF:lease\x20enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20W
SF:rite\x20a\x20message:\x20");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 295.97 seconds
```

OS: Windows

21/tcp   open  ftp                Microsoft ftpd
Anonymous FTP login allowed (FTP code 230)
Can´t get directory listing: TIMEOUT

3389/tcp open  ssl/ms-wbt-server?
|   Target_Name: BRAINSTORM
|   Product_Version: 6.1.7601

9999/tcp open  abyss?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, RPCCheck, RTSPRequest, SSLSessionReq, TerminalServerCookie: 
|     Welcome to Brainstorm chat (beta)
|     Please enter your username (max 20 characters): Write a message: