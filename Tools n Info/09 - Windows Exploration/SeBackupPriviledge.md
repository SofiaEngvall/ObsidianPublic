
```powershell

get-acl | fl

set-acl -AclObject get-acl.AddAccessRule((new-object System.Security.AccessControl.FileSystemAccessRule 'Administrator','FullControl','ContainerInherit,ObjectInherit','None','Allow'))




Set-Acl "C:\users\Administrator\desktop" (Get-Acl "C:\users\Administrator\desktop" | %{$_.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone","FullControl","ContainerInherit,ObjectInherit","None","Allow")));$_})


get-acl | fl

```

```powershell
get-acl $path | fl

$user = "Everyone"
$path = "C:\users\Administrator\desktop"

$acl = get-acl $path
$acl.AddAccessRule((new-object System.Security.AccessControl.FileSystemAccessRule $user,'FullControl','ContainerInherit,ObjectInherit','None','Allow'))
set-acl $path -AclObject $acl

get-acl $path | fl
```