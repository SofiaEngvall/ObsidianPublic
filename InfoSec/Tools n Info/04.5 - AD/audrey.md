**notes on enumerating active directory**




# SMB

get hostname
```shell
# one of these should work
nmblookup -A $target
nbtscan $target
nmap $target --script nbstat.nse,smb-os-discovery
nbtstat -A $target
ping -a $target
```

crackmapexec
```shell
# try both of these
crackmapexec smb $target --pass-pol
crackmapexec smb $target --pass-pol -u "" -p ""     # null auth only works on boomer systems
# if you know creds, try that too
```


rpcclient
```shell
# try both. it might do "access denied"
rpcclient $target -U ""
rpcclient $target -U "" -N

# if you get a shell, do
enumdomusers

# you can also hit tab twice to see the list of commands
# some useful commands below. note that `0x123` is a placeholder for some RID
queryuser 0x123
queryusergroups 0x123
querygroup 0x123

exit
```


polenum
```shell
# TODO idk how to get this to work lol
polenum $target -u "" -p ""
```


enum4linux. might work on boomer systems
```
enum4linux -a $target
enum4linux -a -u "" -p "" $target   # blank creds
enum4linux -a -u "victim-username" -p "password123" $target
```




try null session logons
```bash
shares=('C$' 'D$' 'ADMIN$' 'IPC$' 'PRINT$' 'FAX$' 'SYSVOL' 'NETLOGON')

for share in ${shares[*]}; do
    output=$(smbclient -U '%' -N \\\\$target\\$share -c '')

    # no output if command goes through, thus assuming that a session was created
    if [[ -z $output ]]; then
        echo "[+] creating a null session is possible for $share"
    else
        echo $output # error message (e.g. NT_STATUS_ACCESS_DENIED, NT_STATUS_BAD_NETWORK_NAME)
    fi
done
```




## enumerate file shares

metasploit scans
```
use /auxiliary/scanner/smb/smb_version
use /auxiliary/scanner/smb/smb_enumusers
use /auxiliary/scanner/smb/smb_enumshares
```




### worth a try

**nmap scans**
not always the best, but worth a shot
[[nmap notes#SMB]]


**easy way to access**
just type it into the filepath in the kali file explorer
e.g. `smb://10.10.10.10` where you'd normally type `/etc/path/to/file`
> this will not always work




### try to access without creds

list files
```shell
smbclient -L \\\\$target\\
smbclient -N -L \\\\$target\\
```

| flag      | description            |
| --------- | ---------------------- |
| `-h`      | help                   |
| `-L HOST` | list files on the host |
| `-N`      | no password            |




connect to a specific share (using `IPC$` as an example)
```shell
# dont put a space between the IP and share name!
# DONT ADD `-L`
smbclient \\\\$target\\IPC$
smbclient -N \\\\$target\\IPC$
```

if there's a space in the share name, append a slash before it

> `IPC$` is usually useless, but public
> but it's a good PoC that you can access the share. you usually wont be able to read anything


<u>side note about windows AD</u>
you normally cant get access without creds
logons are handled via the DC by default, so usually you cant just provide creds

you can try appending `-U %` or `-U guest%` or `-U ""`
if you know the creds, append `-U username%'password'`

`NT_STATUS_ACCESS_DENIED` and `NT_STATUS_ACCOUNT_DISABLED` should be self explanatory

also, the `$` at the end just means it's a hidden share. similar to adding `.` to the start of a file




navigating inside a share
```shell
help
ls
cd directoryName

mkdir dirToCreate

exit
```




### access with creds

enumerate shares
```shell
crackmapexec smb $target -u "victim-username" -p "password123" --shares
```
(if the perms column is blank, it probably means you cant access)




--------------------------------------------------------------------------------




# impacket

in general, check the stuff inside `/usr/share/doc/python3-impacket/examples`

find users that dont require kerberos preauthentication
```shell
# you need the IP of the DC, as well as the domain name
cd /usr/share/doc/python3-impacket/examples
python3 GetNPUsers.py -dc-ip $target -request "DOMAINNAME.local/" -format hashcat
```




--------------------------------------------------------------------------------




# LDAP

```shell
ldapsearch -H ldap://$target -x -s base namingcontexts
```

note that `-x` makes it do basic auth

> pay attention to where it says `namingContexts: DC=domainname,DC=local`

copypasta the stuff after the colon into
```shell
ldapsearch -H ldap://$target -x -b "DC=domainname,DC=local" > "ldap output.txt"
```

and then you can grep a bunch of info

you can also search for users specifically
```shell
ldapsearch -H ldap://$target -x -b "DC=domainname,DC=local" '(objectClass=Person)'
ldapsearch -H ldap://$target -x -b "DC=domainname,DC=local" '(objectClass=User)'

# get usernames
ldapsearch -H ldap://$target -x -b "DC=domainname,DC=local" '(objectClass=User)' sAMAccountName | grep sAMAccountName | cut -d " " -f 2
# the first line should be `requesting:`, which is just the remnants of a useless comment
# anything that ends with `$` is a service account, nand probably not worth spraying
# Guest and DefaultAccount are also probably not worth it
# you'll probably also have a bunch of useless accounts that come from MS exchange
```

for dates, you may need to use https://www.epochconverter.com/ldap
e.g. for `pwdLastSet`

