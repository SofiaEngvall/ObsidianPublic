
### Set file permissions

one command version
```powershell

get-acl | fl

Set-Acl "C:\users\Administrator\desktop" (Get-Acl "C:\users\Administrator\desktop" | %{$_.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule("Everyone","FullControl","ContainerInherit,ObjectInherit","None","Allow")));$_})

get-acl | fl

```

script version
```powershell
get-acl $path | fl

$user = "Everyone"
$path = "C:\users\Administrator\desktop"

$acl = get-acl $path
$acl.AddAccessRule((new-object System.Security.AccessControl.FileSystemAccessRule $user,'FullControl','ContainerInherit,ObjectInherit','None','Allow'))
set-acl $path -AclObject $acl

get-acl $path | fl
```


