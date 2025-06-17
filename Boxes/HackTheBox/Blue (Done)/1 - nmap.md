
```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.10.40  
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-06 14:22 CEST
Nmap scan report for 10.10.10.40
Host is up (0.025s latency).
Not shown: 65526 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  msrpc        Microsoft Windows RPC
Service Info: Host: HARIS-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -19m56s, deviation: 34m37s, median: 1s
| smb2-time: 
|   date: 2025-05-06T12:23:59
|_  start_date: 2025-05-06T12:10:59
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2025-05-06T13:23:58+01:00
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 107.46 seconds
```

```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.10.40  
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-06 14:33 CEST
Nmap scan report for 10.10.10.40
Host is up (0.030s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.10.40\ADMIN$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Remote Admin
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.10.40\C$: 
|     Type: STYPE_DISKTREE_HIDDEN
|     Comment: Default share
|     Anonymous access: <none>
|     Current user access: <none>
|   \\10.10.10.40\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: Remote IPC
|     Anonymous access: READ
|     Current user access: READ/WRITE
|   \\10.10.10.40\Share: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|     Current user access: READ
|   \\10.10.10.40\Users: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Anonymous access: <none>
|_    Current user access: READ

Nmap done: 1 IP address (1 host up) scanned in 36.42 seconds
```

|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)

Probably just eternal blue

|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00

|   account_used: guest

|   \\10.10.10.40\Share: 
|     Anonymous access: <none>
|     Current user access: READ

|   \\10.10.10.40\Users: 
|     Anonymous access: <none>
|_    Current user access: READ
