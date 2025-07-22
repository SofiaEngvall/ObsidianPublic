
10.10.106.240

|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local

svc-admin:management2005
backup@spookysec.local:backup2517860

##### all users
(nxc smb --users)
krbtgt
skidy
breakerofthings
james
optional
sherlocksec
darkstar
Ori
robin
paradox
Muirland
horshark
svc-admin
backup
a-spooks

(kerbrute userenum) I'm assuming the ones not in the wordlist are missing
james@spookysec.local
svc-admin@spookysec.local
robin@spookysec.local
darkstar@spookysec.local
administrator@spookysec.local
backup@spookysec.local
paradox@spookysec.local
ori@spookysec.local

Hashes:
Administrator:0e0363213e37b94221497260b0bcb4fc
spookysec.local\a-spooks:0e0363213e37b94221497260b0bcb4fc

