
```sh
┌──(fixit42㉿kali)-[~]
└─$ ldapsearch -x -H ldap://10.129.228.111 -D "SABatchJobs@megabank.local" -w 'SABatchJobs' -b "dc=megabank,dc=local" "(objectClass=user)" sAMAccountName description memberof
# extended LDIF
#
# LDAPv3
# base <dc=megabank,dc=local> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName description memberof 
#

# Administrator, Users, MEGABANK.LOCAL
dn: CN=Administrator,CN=Users,DC=MEGABANK,DC=LOCAL
description: Built-in account for administering the computer/domain
memberOf: CN=Azure Admins,OU=Groups,DC=MEGABANK,DC=LOCAL
memberOf: CN=ADSyncAdmins,CN=Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Domain Admins,CN=Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Enterprise Admins,CN=Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Schema Admins,CN=Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Administrators,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: Administrator

# Guest, Users, MEGABANK.LOCAL
dn: CN=Guest,CN=Users,DC=MEGABANK,DC=LOCAL
description: Built-in account for guest access to the computer/domain
memberOf: CN=Guests,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: Guest

# MONTEVERDE, Domain Controllers, MEGABANK.LOCAL
dn: CN=MONTEVERDE,OU=Domain Controllers,DC=MEGABANK,DC=LOCAL
sAMAccountName: MONTEVERDE$

# krbtgt, Users, MEGABANK.LOCAL
dn: CN=krbtgt,CN=Users,DC=MEGABANK,DC=LOCAL
description: Key Distribution Center Service Account
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=MEGABANK,DC=LO
 CAL
sAMAccountName: krbtgt

# AAD_987d7f2f57d2, Users, MEGABANK.LOCAL
dn: CN=AAD_987d7f2f57d2,CN=Users,DC=MEGABANK,DC=LOCAL
description: Service account for the Synchronization Service with installation
  identifier 05c97990-7587-4a3d-b312-309adfc172d9 running on computer MONTEVER
 DE.
memberOf: CN=Azure Admins,OU=Groups,DC=MEGABANK,DC=LOCAL
memberOf: CN=Users,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: AAD_987d7f2f57d2

# Mike Hope, London, MegaBank Users, MEGABANK.LOCAL
dn: CN=Mike Hope,OU=London,OU=MegaBank Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Azure Admins,OU=Groups,DC=MEGABANK,DC=LOCAL
memberOf: CN=Remote Management Users,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: mhope

# SABatchJobs, Service Accounts, MEGABANK.LOCAL
dn: CN=SABatchJobs,OU=Service Accounts,DC=MEGABANK,DC=LOCAL
sAMAccountName: SABatchJobs

# svc-ata, Service Accounts, MEGABANK.LOCAL
dn: CN=svc-ata,OU=Service Accounts,DC=MEGABANK,DC=LOCAL
sAMAccountName: svc-ata

# svc-bexec, Service Accounts, MEGABANK.LOCAL
dn: CN=svc-bexec,OU=Service Accounts,DC=MEGABANK,DC=LOCAL
sAMAccountName: svc-bexec

# svc-netapp, Service Accounts, MEGABANK.LOCAL
dn: CN=svc-netapp,OU=Service Accounts,DC=MEGABANK,DC=LOCAL
sAMAccountName: svc-netapp

# Dimitris Galanos, Athens, MegaBank Users, MEGABANK.LOCAL
dn: CN=Dimitris Galanos,OU=Athens,OU=MegaBank Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Trading,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: dgalanos

# Ray O'Leary, Toronto, MegaBank Users, MEGABANK.LOCAL
dn: CN=Ray O'Leary,OU=Toronto,OU=MegaBank Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=HelpDesk,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: roleary

# Sally Morgan, New York, MegaBank Users, MEGABANK.LOCAL
dn: CN=Sally Morgan,OU=New York,OU=MegaBank Users,DC=MEGABANK,DC=LOCAL
memberOf: CN=Operations,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: smorgan

# search reference
ref: ldap://ForestDnsZones.MEGABANK.LOCAL/DC=ForestDnsZones,DC=MEGABANK,DC=LOC
 AL

# search reference
ref: ldap://DomainDnsZones.MEGABANK.LOCAL/DC=DomainDnsZones,DC=MEGABANK,DC=LOC
 AL

# search reference
ref: ldap://MEGABANK.LOCAL/CN=Configuration,DC=MEGABANK,DC=LOCAL

# search result
search: 2
result: 0 Success

# numResponses: 17
# numEntries: 13
# numReferences: 3
```

AAD_987d7f2f57d2, Users, MEGABANK.LOCAL
dn: CN=AAD_987d7f2f57d2,CN=Users,DC=MEGABANK,DC=LOCAL
description: Service account for the Synchronization Service with installation
  identifier 05c97990-7587-4a3d-b312-309adfc172d9 running on computer MONTEVER
 DE.
memberOf: CN=Azure Admins,OU=Groups,DC=MEGABANK,DC=LOCAL
memberOf: CN=Users,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: AAD_987d7f2f57d2

SABatchJobs, Service Accounts, MEGABANK.LOCAL
sAMAccountName: SABatchJobs

svc-ata, Service Accounts, MEGABANK.LOCAL
sAMAccountName: svc-ata

svc-bexec, Service Accounts, MEGABANK.LOCAL
sAMAccountName: svc-bexec

svc-netapp, Service Accounts, MEGABANK.LOCAL
sAMAccountName: svc-netapp


Mike Hope, London, MegaBank Users, MEGABANK.LOCAL
memberOf: CN=Azure Admins,OU=Groups,DC=MEGABANK,DC=LOCAL
memberOf: CN=***Remote Management Users***,CN=Builtin,DC=MEGABANK,DC=LOCAL
sAMAccountName: mhope

Dimitris Galanos, Athens, MegaBank Users, MEGABANK.LOCAL
memberOf: CN=Trading,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: dgalanos

Ray O'Leary, Toronto, MegaBank Users, MEGABANK.LOCAL
memberOf: CN=HelpDesk,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: roleary

Sally Morgan, New York, MegaBank Users, MEGABANK.LOCAL
memberOf: CN=Operations,OU=Groups,DC=MEGABANK,DC=LOCAL
sAMAccountName: smorgan
