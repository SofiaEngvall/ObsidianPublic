
```sh
┌──(kali㉿kali)-[~/…/WIN10HDD/Windows/System32/Config]
└─$ ls -la
total 10548
drwxrwxr-x 2 kali kali     4096 Nov 14 12:31 .
drwxrwxr-x 3 kali kali     4096 Nov 14 12:31 ..
-rw-rw-r-- 1 kali kali    45056 Nov  1 13:48 SAM
-rw-rw-r-- 1 kali kali 10743808 Nov  1 13:48 SYSTEM

┌──(kali㉿kali)-[~/…/WIN10HDD/Windows/System32/Config]
└─$ impacket-secretsdump -sam SAM -system SYSTEM LOCAL
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0x0f8bba4a5a4a042ffaae1641c5cdce11
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administratör:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Gäst:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:365b962b7824e43785024320ba411ab8:::
KennethSpaceKingX:1001:aad3b435b51404eeaad3b435b51404ee:765e96743ddaab13c26db5c4291ad97b:::
[*] Cleaning up... 
```


crackstation:

| Hash                             | Type    | Result     |
| -------------------------------- | ------- | ---------- |
| 31d6cfe0d16ae931b73c59d7e0c089c0 | NTLM    |            |
| 31d6cfe0d16ae931b73c59d7e0c089c0 | NTLM    |            |
| 31d6cfe0d16ae931b73c59d7e0c089c0 | NTLM    |            |
| 365b962b7824e43785024320ba411ab8 | Unknown | Not found. |
| 765e96743ddaab13c26db5c4291ad97b | Unknown | Not found. |

so we have 
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:365b962b7824e43785024320ba411ab8:::
KennethSpaceKingX:1001:aad3b435b51404eeaad3b435b51404ee:765e96743ddaab13c26db5c4291ad97b:::
left

as we need the firefox password for kenneth..

