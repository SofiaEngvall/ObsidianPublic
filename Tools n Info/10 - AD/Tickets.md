

### Silver ticket - 

SQL Example - User


### Golden ticket - use krbtgt hash to get any creds

Requirements:
domain:        domain.com
domain sid:  used sid minus the last bit
krbtgt hash:   (requires dc sync or similar permissions to get)

The krbtgt account is always disabled as it's not used for login.
Getting the krbtgt hash through mimikatz or impacket-secretsdump for example
