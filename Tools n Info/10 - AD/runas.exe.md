
when you have creds but nowhere to log in!

`runas.exe /netonly /user:<domain>\<username> cmd.exe`
- netonly - will use these creds only for networking stuff

if possible, run the above as admin

test the creds validity by accessing SYSVOL on the DC

Example:
`runas.exe /netonly /user:za.tryhackme.com\phillip.reid cmd.exe`

