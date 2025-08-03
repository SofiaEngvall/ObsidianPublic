
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ bloodhound-python -u 'emily.oscars' -p 'Q!3@Lp#M6b*7t*Vt' -d cicada.htb -dc CICADA-DC.cicada.htb -ns 10.129.169.79 -c all
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: cicada.htb
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
INFO: Connecting to LDAP server: CICADA-DC.cicada.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: CICADA-DC.cicada.htb
INFO: Found 9 users
INFO: Found 54 groups
INFO: Found 3 gpos
INFO: Found 2 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: CICADA-DC.cicada.htb
INFO: Done in 00M 05S
```

![[Images/Pasted image 20250731203828.png]]

