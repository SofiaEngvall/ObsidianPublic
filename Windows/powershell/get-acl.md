
`get-acl|fl`

example:

```powershell
*Evil-WinRM* PS C:\users\Administrator\desktop> get-acl|fl


Path   : Microsoft.PowerShell.Core\FileSystem::C:\users\Administrator\desktop
Owner  : BUILTIN\Administrators
Group  : RETURN\Domain Users
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         RETURN\Administrator Allow  FullControl
Audit  :
Sddl   : O:BAG:DUD:(A;OICIID;FA;;;SY)(A;OICIID;FA;;;BA)(A;OICIID;FA;;;LA)
```

