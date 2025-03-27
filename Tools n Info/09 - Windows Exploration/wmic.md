WMI command line utility

OS Arch
	`vmic OS get OSArchitecture`

Get user account SIDs
	`wmic useraccount get name,sid`

Installed/unpatched software
	`wmic product get name,version,vendor` enum programs - also check desktop shortcuts, start menu, available services...

HotFixes
	`wmic qfe get Caption,Description,HotFixID,InstalledOn`

List drive letters
	`(wmic logicaldisk get caption 2>nul | more) || (fsutil fsinfo drives 2>nul)`

---

## Using vmic on kali remotely



### Examples

```sh
┌──(kali㉿kali)-[~]
└─$ wmic -U 'Bob'%'!P@$$W0rD!123' //10.10.84.243 "select * from Win32_ComputerSystem"
[wmi/wmic.c:196:main()] ERROR: Login to remote object.
NTSTATUS: NT_STATUS_ACCESS_DENIED - Access denied
```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ wmic --help                                                                                                           
Usage: //host query

Example: wmic -U [domain/]adminuser%password //host "select * from Win32_ComputerSystem"
  --namespace=STRING                          WMI namespace, default to
                                              root\cimv2
  --delimiter=STRING                          delimiter to use when querying
                                              multiple values, default to '|'

Help options:
  -?, --help                                  Show this help message
  --usage                                     Display brief usage message

Common samba options:
  -d, --debuglevel=DEBUGLEVEL                 Set debug level
  --debug-stderr                              Send debug output to STDERR
  -s, --configfile=CONFIGFILE                 Use alternative configuration
                                              file
  --option=name=value                         Set smb.conf option from command
                                              line
  -l, --log-basename=LOGFILEBASE              Basename for log/debug files
  --leak-report                               enable talloc leak reporting on
                                              exit
  --leak-report-full                          enable full talloc leak
                                              reporting on exit

Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER       Use these name resolution
                                              services only
  -O, --socket-options=SOCKETOPTIONS          socket options to use
  -n, --netbiosname=NETBIOSNAME               Primary netbios name
  -W, --workgroup=WORKGROUP                   Set the workgroup name
  --realm=REALM                               Set the realm name
  -i, --scope=SCOPE                           Use this Netbios scope
  -m, --maxprotocol=MAXPROTOCOL               Set max protocol level

Authentication options:
  -U, --user=[DOMAIN\]USERNAME[%PASSWORD]     Set the network username
  -N, --no-pass                               Don´t ask for a password
  --password=STRING                           Password
  -A, --authentication-file=FILE              Get the credentials from a file
  -S, --signing=on|off|required               Set the client signing state
  -P, --machine-pass                          Use stored machine account
                                              password (implies -k)
  --simple-bind-dn=STRING                     DN to use for a simple bind
  -k, --kerberos=STRING                       Use Kerberos
  --use-security-mechanisms=STRING            Restricted list of
                                              authentication mechanisms
                                              available for use with this
                                              authentication

Common samba options:
  -V, --version                               Print version

```