
impacket-owneredit
impacket-dacledit


### Help impacket-owneredit

```
(fixit42㉿kali)-[~]
└─$ impacket-owneredit
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

usage: owneredit.py [-h] [-use-ldaps] [-ts] [-debug] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                    [-dc-ip ip address] [-new-owner NAME] [-new-owner-sid SID] [-new-owner-dn DN] [-target NAME]
                    [-target-sid SID] [-target-dn DN] [-action [{read,write}]]
                    identity

Python editor for a principal's DACL.

positional arguments:
  identity              domain.local/username[:password]

options:
  -h, --help            show this help message and exit
  -use-ldaps            Use LDAPS instead of LDAP
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON

authentication & connection:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                        parameters. If valid credentials cannot be found, it will use the ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)
  -dc-ip ip address     IP Address of the domain controller or KDC (Key Distribution Center) for Kerberos. If omitted it
                        will use the domain part (FQDN) specified in the identity parameter

owner:
  Object, controlled by the attacker, to set as owner of the target object

  -new-owner NAME       sAMAccountName
  -new-owner-sid SID    Security IDentifier
  -new-owner-dn DN      Distinguished Name

target:
  Target object to edit the owner of

  -target NAME          sAMAccountName
  -target-sid SID       Security IDentifier
  -target-dn DN         Distinguished Name

dacl editor:
  -action [{read,write}]
                        Action to operate on the owner attribute
```