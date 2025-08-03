
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ldapsearch -x -H ldap://10.129.169.79 -s base namingContexts     
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: namingContexts 
#

#
dn:
namingContexts: DC=cicada,DC=htb
namingContexts: CN=Configuration,DC=cicada,DC=htb
namingContexts: CN=Schema,CN=Configuration,DC=cicada,DC=htb
namingContexts: DC=DomainDnsZones,DC=cicada,DC=htb
namingContexts: DC=ForestDnsZones,DC=cicada,DC=htb

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ldapsearch -x -H ldap://10.129.169.79 -b "dc=domain,dc=com" "(objectClass=user)" sAMAccountName description memberof
# extended LDIF
#
# LDAPv3
# base <dc=domain,dc=com> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName description memberof 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090C78, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4f7c

# numResponses: 1
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ldapsearch -x -H ldap://10.129.169.79 -D "emily.oscars@cicada.htb" -w 'Q!3@Lp#M6b*7t*Vt' -b "DC=cicada,DC=htb" "(objectClass=person)" sAMAccountName description memberof
# extended LDIF
#
# LDAPv3
# base <DC=cicada,DC=htb> with scope subtree
# filter: (objectClass=person)
# requesting: sAMAccountName description memberof 
#

# Administrator, Users, cicada.htb
dn: CN=Administrator,CN=Users,DC=cicada,DC=htb
description: Built-in account for administering the computer/domain
memberOf: CN=Group Policy Creator Owners,OU=Group,DC=cicada,DC=htb
memberOf: CN=Domain Admins,OU=Group,DC=cicada,DC=htb
memberOf: CN=Enterprise Admins,OU=Group,DC=cicada,DC=htb
memberOf: CN=Schema Admins,OU=Group,DC=cicada,DC=htb
memberOf: CN=Remote Desktop Users,CN=Builtin,DC=cicada,DC=htb
memberOf: CN=Administrators,CN=Builtin,DC=cicada,DC=htb
sAMAccountName: Administrator

# Guest, Users, cicada.htb
dn: CN=Guest,CN=Users,DC=cicada,DC=htb
description: Built-in account for guest access to the computer/domain
memberOf: CN=Guests,CN=Builtin,DC=cicada,DC=htb
sAMAccountName: Guest

# CICADA-DC, Domain Controllers, cicada.htb
dn: CN=CICADA-DC,OU=Domain Controllers,DC=cicada,DC=htb
sAMAccountName: CICADA-DC$

# krbtgt, Users, cicada.htb
dn: CN=krbtgt,CN=Users,DC=cicada,DC=htb
description: Key Distribution Center Service Account
memberOf: CN=Denied RODC Password Replication Group,OU=Group,DC=cicada,DC=htb
sAMAccountName: krbtgt

# John Smoulder, Users, cicada.htb
dn: CN=John Smoulder,CN=Users,DC=cicada,DC=htb
sAMAccountName: john.smoulder

# Sarah Dantelia, Users, cicada.htb
dn: CN=Sarah Dantelia,CN=Users,DC=cicada,DC=htb
sAMAccountName: sarah.dantelia

# Michael Wrightson, Users, cicada.htb
dn: CN=Michael Wrightson,CN=Users,DC=cicada,DC=htb
sAMAccountName: michael.wrightson

# David Orelious, Users, cicada.htb
dn: CN=David Orelious,CN=Users,DC=cicada,DC=htb
description: Just in case I forget my password is aRt$Lp#7t*VQ!3
sAMAccountName: david.orelious

# Emily Oscars, Users, cicada.htb
dn: CN=Emily Oscars,CN=Users,DC=cicada,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=cicada,DC=htb
memberOf: CN=Backup Operators,CN=Builtin,DC=cicada,DC=htb
sAMAccountName: emily.oscars

# search reference
ref: ldap://DomainDnsZones.cicada.htb/DC=DomainDnsZones,DC=cicada,DC=htb

# search reference
ref: ldap://ForestDnsZones.cicada.htb/DC=ForestDnsZones,DC=cicada,DC=htb

# search reference
ref: ldap://cicada.htb/CN=Configuration,DC=cicada,DC=htb

# search result
search: 2
result: 0 Success

# numResponses: 13
# numEntries: 9
# numReferences: 3
```

