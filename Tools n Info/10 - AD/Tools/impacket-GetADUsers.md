
`impacket-GetADUsers cicada.htb/emily.oscars:'Q!3@Lp#M6b*7t*Vt' -dc-ip 10.129.169.79 -all`

### Examples

```sh
┌──(fixit42㉿kali)-[~/tools]
└─$ impacket-GetADUsers cicada.htb/emily.oscars:'Q!3@Lp#M6b*7t*Vt' -dc-ip 10.129.169.79 -all                              
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Querying 10.129.169.79 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2024-08-26 22:08:03.186878  2025-08-01 01:07:43.686390 
Guest                                                 2024-08-28 19:26:56.662374  2025-08-01 01:38:09.405117 
krbtgt                                                2024-03-14 12:14:10.395299  <never>             
john.smoulder                                         2024-03-14 13:17:29.183818  <never>             
sarah.dantelia                                        2024-03-14 13:17:29.310232  <never>             
michael.wrightson                                     2024-03-14 13:17:29.373763  <never>             
david.orelious                                        2024-03-14 13:17:29.513848  2025-08-01 02:54:33.420772 
emily.oscars                                          2024-08-22 23:20:17.303714  <never>
```

### Help

```sh
┌──(fixit42㉿kali)-[~/tools]
└─$ impacket-GetADUsers -h
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

usage: GetADUsers.py [-h] [-user username] [-all] [-ts] [-debug] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                     [-dc-ip ip address] [-dc-host hostname]
                     target

Queries target domain for users data

positional arguments:
  target                domain[/username[:password]]

options:
  -h, --help            show this help message and exit
  -user username        Requests data for specific user
  -all                  Return all users, including those with no email addresses and disabled accounts. When used with
                        -user it will return user´s info even if the account is disabled
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don´t ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                        parameters. If valid credentials cannot be found, it will use the ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)

connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN) specified in the
                        target parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited, the domain part (FQDN) specified in the
                        account parameter will be used

```