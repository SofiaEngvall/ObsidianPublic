
Reset user password:
```powershell
Set-ADAccountPassword <username> -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
```

Force password reset:
```powershell
Set-ADUser -ChangePasswordAtLogon $true -Identity sophie -Verbose
```
