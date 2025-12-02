

Set-ADAccountPassword Administrator -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose

Set users password & Force reset at logon
```powershell
Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
Set-ADUser -ChangePasswordAtLogon $true -Identity sophie -Verbose
```


