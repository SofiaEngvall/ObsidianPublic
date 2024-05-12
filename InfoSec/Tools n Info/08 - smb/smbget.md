get all files on a share recursively (might have problems with big files?)
`smbget --recursive smb://10.10.212.230/anonymous`

```sh
┌──(kali㉿kali)-[~]
└─$ smbget --recursive smb://10.10.110.17/anonymous
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
rlimit_max: increasing rlimit_max (1024) to minimum Windows limit (16384)
added interface eth0 ip=192.168.233.133 bcast=192.168.233.255 netmask=255.255.255.0
Using netbios name KALI.
Using workgroup WORKGROUP.
Password for [WORKGROUP\kali]:
Using domain: WORKGROUP, user: kali
Cannot do GSE to an IP address
Server connect ok: //10.10.110.17/anonymous: 0x563edf05b7b0
Can't open log.txt: File exists
Failed to download /log.txt: File exists
```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ smbget --help
Usage: smbget [OPTION...]
  -a, --guest                                  Work as user guest
  -e, --encrypt                                Encrypt SMB transport
  -r, --resume                                 Automatically resume aborted files
  -u, --update                                 Download only when remote file is newer than local file or local file is missing
      --recursive                              Recursively download files
  -b, --blocksize=INT                          Change number of bytes in a block
  -o, --outputfile=STRING                      Write downloaded data to specified file
      --stdout                                 Write data to stdout
  -D, --dots                                   Show dots as progress indication
  -q, --quiet                                  Be quiet
  -v, --verbose                                Be verbose
      --limit-rate=INT                         Limit download speed to this many KB/s

Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message

Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard output
  -s, --configfile=CONFIGFILE                  Use alternative configuration file
      --option=name=value                      Set smb.conf option from command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on exit
      --leak-report-full                       enable full talloc leak reporting on exit

Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution services only
  -O, --socket-options=SOCKETOPTIONS           socket options to use
  -m, --max-protocol=MAXPROTOCOL               Set max protocol level
  -n, --netbiosname=NETBIOSNAME                Primary netbios name
      --netbios-scope=SCOPE                    Use this Netbios scope
  -W, --workgroup=WORKGROUP                    Set the workgroup name
      --realm=REALM                            Set the realm name

Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don´t ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for Kerberos
      --use-winbind-ccache                     Use the winbind ccache for authentication
      --client-protection=sign|encrypt|off     Configure used protection for client connections

Deprecated legacy options:
  -k, --kerberos                               DEPRECATED: Migrate to --use-kerberos

Version options:
  -V, --version                                Print version

```
