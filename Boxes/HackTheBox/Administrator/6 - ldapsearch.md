
```sh
┌──(fixit42㉿kali)-[/usr/share/wordlists]
└─$ ldapsearch -x -H ldap://10.129.203.207 -D "Olivia@administrator.htb" -w 'ichliebedich' -b "dc=administrator,dc=htb" "(objectClass=user)" sAMAccountName description memberof
# extended LDIF
#
# LDAPv3
# base <dc=administrator,dc=htb> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName description memberof 
#

# Administrator, Users, administrator.htb
dn: CN=Administrator,CN=Users,DC=administrator,DC=htb
description: Built-in account for administering the computer/domain
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=administrator,DC=htb
memberOf: CN=Domain Admins,CN=Users,DC=administrator,DC=htb
memberOf: CN=Enterprise Admins,CN=Users,DC=administrator,DC=htb
memberOf: CN=Schema Admins,CN=Users,DC=administrator,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: Administrator

# Guest, Users, administrator.htb
dn: CN=Guest,CN=Users,DC=administrator,DC=htb
description: Built-in account for guest access to the computer/domain
memberOf: CN=Guests,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: Guest

# DC, Domain Controllers, administrator.htb
dn: CN=DC,OU=Domain Controllers,DC=administrator,DC=htb
sAMAccountName: DC$

# krbtgt, Users, administrator.htb
dn: CN=krbtgt,CN=Users,DC=administrator,DC=htb
description: Key Distribution Center Service Account
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=administrator,
 DC=htb
sAMAccountName: krbtgt

# Olivia Johnson, Users, administrator.htb
dn: CN=Olivia Johnson,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: olivia

# Michael Williams, Users, administrator.htb
dn: CN=Michael Williams,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: michael

# Benjamin Brown, Users, administrator.htb
dn: CN=Benjamin Brown,CN=Users,DC=administrator,DC=htb
memberOf: CN=Share Moderators,CN=Users,DC=administrator,DC=htb
sAMAccountName: benjamin

# Emily Rodriguez, Users, administrator.htb
dn: CN=Emily Rodriguez,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: emily

# Ethan Hunt, Users, administrator.htb
dn: CN=Ethan Hunt,CN=Users,DC=administrator,DC=htb
sAMAccountName: ethan

# Alexander Smith, Users, administrator.htb
dn: CN=Alexander Smith,CN=Users,DC=administrator,DC=htb
sAMAccountName: alexander

# Emma Johnson, Users, administrator.htb
dn: CN=Emma Johnson,CN=Users,DC=administrator,DC=htb
sAMAccountName: emma

# search reference
ref: ldap://ForestDnsZones.administrator.htb/DC=ForestDnsZones,DC=administrato
 r,DC=htb

# search reference
ref: ldap://DomainDnsZones.administrator.htb/DC=DomainDnsZones,DC=administrato
 r,DC=htb

# search reference
ref: ldap://administrator.htb/CN=Configuration,DC=administrator,DC=htb

# search result
search: 2
result: 0 Success

# numResponses: 15
# numEntries: 11
# numReferences: 3
```