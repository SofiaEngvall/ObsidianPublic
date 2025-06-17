
```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.10.4 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-06 18:18 CEST
Nmap scan report for 10.10.10.4
Host is up (0.023s latency).
Not shown: 65532 closed tcp ports (reset)
PORT    STATE SERVICE      VERSION
135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows XP microsoft-ds
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:94:d8:a2 (VMware)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00
|_  System time: 2025-05-11T21:16:53+03:00
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: mean: 5d00h27m38s, deviation: 2h07m16s, median: 4d22h57m38s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.03 seconds
```

135/tcp open  msrpc        Microsoft Windows RPC
139/tcp open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds Windows XP microsoft-ds

|   OS: Windows XP (Windows 2000 LAN Manager)
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00

```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.10.4 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-06 18:22 CEST
Nmap scan report for 10.10.10.4
Host is up (0.024s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (NT_STATUS_ACCESS_DENIED)
|   account_used: <blank>
|   \\10.10.10.4\ADMIN$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\10.10.10.4\C$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\10.10.10.4\IPC$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|_    Anonymous access: READ

Nmap done: 1 IP address (1 host up) scanned in 19.66 seconds
```

nothing?

let's try all nmap smb scripts

```sh
┌──(kali㉿proxli)-[~]
└─$ nmap -p 445 --script=smb* 10.10.10.4
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-06 18:24 CEST
NSE: [smb-brute] usernames: Time limit 10m00s exceeded.
NSE: [smb-brute] usernames: Time limit 10m00s exceeded.
NSE: [smb-brute] passwords: Time limit 10m00s exceeded.
Nmap scan report for 10.10.10.4
Host is up (0.023s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb-vuln-ms08-067: 
|   VULNERABLE:
|   Microsoft Windows system vulnerable to remote code execution (MS08-067)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2008-4250
|           The Server service in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2,
|           Vista Gold and SP1, Server 2008, and 7 Pre-Beta allows remote attackers to execute arbitrary
|           code via a crafted RPC request that triggers the overflow during path canonicalization.
|           
|     Disclosure date: 2008-10-23
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms08-067.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb-vuln-ms10-054: false
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_smb2-time: Protocol negotiation failed (SMB2)
|_smb-flood: ERROR: Script execution failed (use -d to debug)
|_smb-vuln-ms10-061: ERROR: Script execution failed (use -d to debug)
| smb-brute: 
|_  No accounts found
| smb-mbenum: 
|   Master Browser
|     LEGACY  5.1  
|   Potential Browser
|     LEGACY  5.1  
|   Server service
|     LEGACY  5.1  
|   Windows NT/2000/XP/2003 server
|     LEGACY  5.1  
|   Workstation
|_    LEGACY  5.1  
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (NT_STATUS_ACCESS_DENIED)
|   account_used: <blank>
|   \\10.10.10.4\ADMIN$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\10.10.10.4\C$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\10.10.10.4\IPC$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|_    Anonymous access: READ
|_smb-print-text: false
| smb-protocols: 
|   dialects: 
|_    NT LM 0.12 (SMBv1) [dangerous, but default]
|_smb2-capabilities: SMB 2+ not supported

Nmap done: 1 IP address (1 host up) scanned in 628.94 seconds

```