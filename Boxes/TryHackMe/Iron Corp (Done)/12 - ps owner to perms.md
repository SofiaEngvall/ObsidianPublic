
`$acl = Get-Acl -Path "C:\Users\Admin"; $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("NT AUTHORITY\SYSTEM", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow"); $acl.AddAccessRule($rule); Set-Acl -Path "C:\Users\Admin" -AclObject $acl`




create user

`net user pratchett password /add`

`Invoke-Expression -Command "cmd.exe /c net user pratchett /add"`
`Invoke-Expression -Command "cmd.exe /c net user terry password /add"'

`Invoke-Expression -Command "cmd.exe /c net user"`

`Invoke-Expression -Command "cmd.exe /c net localgroup "Remote Desktop Users" terry /add"`
`Invoke-Expression -Command "cmd.exe /c net localgroup "Administrors" terry /add"`

`Invoke-Expression -Command "cmd.exe /c net localgroup pratchett"`


works
`New-LocalUser -Name "terry3" -Password (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -PasswordNeverExpires:$true`
`Add-LocalGroupMember -Group "Administrators" -Member "terry3"`
`Add-LocalGroupMember -Group "Remote Desktop Users" -Member "terry3"`

`net user terry3` to confirm
