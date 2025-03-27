
https://delinea.com/blog/windows-privilege-escalation

There's a Security Account Manager database, a SAM file, on every Windows system. It stores User accounts and security descriptors.

Each user has an access a token that contains privileges - When they perform an action, it's checked if they have the right permissions.
If they don't have the right perms they are usually prompted to log in with another account. (Makes it possible not to be admin.)

Security Identifiers, SIDs, are used instead of names for accounts, groups and processes.
#### Local_Users ex
![[Images/Pasted image 20240103141015.png]]

#### Local Groups ex
![[Images/Pasted image 20240103140925.png]]



#### Priv esc examples

- service running with system perms + user perms to change service (path, executable..)
- unquoted service path + user perms to parent dir
- weak registry perms, for example service config
- passwords in text files, browsers, config files...
	- cmd search of registry:  `reg query HKLM /f password /t REG_SZ /s`