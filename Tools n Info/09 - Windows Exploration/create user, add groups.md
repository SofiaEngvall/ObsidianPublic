
PowerShell:
```powershell
New-LocalUser -Name "pratchett"
```

Command line:
```sh
net user pratchett <password> /add /fullname:"Terry Pratchett" /comment:"Author"
```

Can be user in PowerShell by using `Invoke-Expression -Command "cmd.exe /c net user pratchett /add"`

Add to local admin group:
```sh
net localgroup administrators <username> /add
```

