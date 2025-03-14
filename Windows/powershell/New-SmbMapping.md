

```powershell
PS C:\Users\graeme.williams\Documents> New-SmbMapping -LocalPath 'X:' -RemotePath '\\10.50.54.2\share' -UserName user -Passwor
d password

Status Local Path Remote Path
------ ---------- -----------
OK     X:         \\10.50.54.2\share
```

```powershell
Remove-SmbMapping X:
```

