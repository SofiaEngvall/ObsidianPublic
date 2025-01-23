
List shares
```sh
net use \\<server>\IPC$ /USER:[domain\]<username> <password>
net view \\<server>
```

`net use \\10.21.31.111\IPC$ /USER:user password`
`net view \\10.21.31.111`

Map a drive letter to a share:
```sh
net use <driveletter>: \\<server>\<sharename> /USER:[domain\]<username> <password> /PERSISTENT:YES
```

`net use q: \\10.21.31.111\share /USER:user password /PERSISTENT:YES`

if problems:
`net use \\<server>\<sharename> /delete`


Copy files cmd
```sh
robocopy source destination /E
```

`robocopy . q:\gatekeeper /E`

Copy files ps
```powershell
Copy-Item -Path "C:\file1\*" -Destination "C:\file2\" -Recurse
```
