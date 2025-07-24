
```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ bloodhound-python -u svc-admin -p 'management2005' -d spookysec.local -dc AttacktiveDirectory.spookysec.local -ns 10.10.229.142 -c all
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: spookysec.local
INFO: Getting TGT for user
INFO: Connecting to LDAP server: AttacktiveDirectory.spookysec.local
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: AttacktiveDirectory.spookysec.local
INFO: Found 18 users
INFO: Found 54 groups
INFO: Found 2 gpos
INFO: Found 3 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: AttacktiveDirectory.spookysec.local
INFO: Done in 00M 17S
```

![[Images/Pasted image 20250705020504.png]]
