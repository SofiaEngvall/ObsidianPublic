
Sets full control if you're the owner:
```powershell
$acl = Get-Acl -Path "C:\Users\Admin"; $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("NT AUTHORITY\SYSTEM", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow"); $acl.AddAccessRule($rule); Set-Acl -Path "C:\Users\Admin" -AclObject $acl
```
*^ here logged in as NT AUTHORITY\\SYSTEM*
