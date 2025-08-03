
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ bloodhound-python -u 'olivia' -p 'ichliebedich' -d administrator.htb -dc DC.administrator.htb -ns 10.129.203.207 -c all
INFO: BloodHound.py for BloodHound LEGACY (BloodHound 4.2 and 4.3)
INFO: Found AD domain: administrator.htb
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
INFO: Connecting to LDAP server: DC.administrator.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: DC.administrator.htb
INFO: Found 11 users
INFO: Found 53 groups
INFO: Found 2 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: dc.administrator.htb
INFO: Done in 00M 06S
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ nxc ldap 10.129.203.207 --dns-server 10.129.203.207 -d administrator.htb -u olivia -p ichliebedich --bloodhound --collection All
LDAP        10.129.203.207  389    DC               [*] Windows Server 2022 Build 20348 (name:DC) (domain:administrator.htb)
LDAP        10.129.203.207  389    DC               [+] administrator.htb\olivia:ichliebedich 
LDAP        10.129.203.207  389    DC               Resolved collection methods: container, dcom, trusts, acl, psremote, localadmin, objectprops, session, group, rdp                                                                                       
LDAP        10.129.203.207  389    DC               Done in 00M 07S
LDAP        10.129.203.207  389    DC               Compressing output into /home/fixit42/.nxc/logs/DC_10.129.203.207_2025-08-02_040153_bloodhound.zip
```

![[Images/Pasted image 20250802041927.png]]
The user OLIVIA@ADMINISTRATOR.HTB has GenericAll permissions to the user MICHAEL@ADMINISTRATOR.HTB.

This is also known as full control. This permission allows the trustee to manipulate the target object however they wish.

![[Images/Pasted image 20250802042009.png]]
The user MICHAEL@ADMINISTRATOR.HTB has the capability to change the user BENJAMIN@ADMINISTRATOR.HTB's password without knowing that user's current password.

![[Images/Pasted image 20250802042649.png]]
