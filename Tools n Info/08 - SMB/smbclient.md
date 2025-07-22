

### Connect to smb share

`smbclient //10.10.138.39/Anonymous`

`smbclient //10.10.97.172/profiles -U Anonymous`
`smbclient //10.10.97.172/profiles -U krktgt`

`dir` to list files
`get <filename>` to get a file

download all files recursively
```sh
smbclient '\\server\share'
mask ""
recurse ON
prompt OFF
cd 'path\to\remote\dir'
lcd '~/path/to/download/to/'
mget *
```

oneliner:
```sh
smbclient '\\server\share' -N -c prompt OFF;recurse ON;cd "path";lcd "local path";mget *
```


### Upload a file

```sh
┌──(kali㉿kali)-[~]
└─$ cd shells

┌──(kali㉿kali)-[~/shells]
└─$ smbclient //relevant.thm/nt4wrksv -U 'Bob'%'!P@$$W0rD!123' -c 'put revsh.aspx' 
putting file revsh.aspx as \revsh.aspx (29.4 kb/s) (average 29.4 kb/s)

┌──(kali㉿kali)-[~/shells]
└─$ smbclient //relevant.thm/nt4wrksv -U 'Bob'%'!P@$$W0rD!123'                    
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Jul 25 18:14:16 2024
  ..                                  D        0  Thu Jul 25 18:14:16 2024
  passwords.txt                       A       98  Sat Jul 25 17:15:33 2020
  revsh.aspx                          A    15547  Thu Jul 25 18:14:16 2024

                7735807 blocks of size 4096. 4935823 blocks available
smb: \> 
```

### Commands

```sh
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!      
```
```sh
┌──(kali㉿kali)-[~]
└─$ smbclient //10.10.138.39/IPC$                                         

Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!              
smb: \> 

```
### Help

```sh
┌──(kali㉿kali)-[~]
└─$ smbclient --help         
Usage: smbclient [OPTIONS] service <password>
  -M, --message=HOST                           Send message
  -I, --ip-address=IP                          Use this IP to connect to
  -E, --stderr                                 Write messages to stderr instead of stdout
  -L, --list=HOST                              Get a list of shares available on a host
  -T, --tar=<c|x>IXFvgbNan                     Command line tar
  -D, --directory=DIR                          Start from directory
  -c, --command=STRING                         Execute semicolon separated commands
  -b, --send-buffer=BYTES                      Changes the transmit/send buffer
  -t, --timeout=SECONDS                        Changes the per-operation timeout
  -p, --port=PORT                              Port to connect to
  -g, --grepable                               Produce grepable output
  -q, --quiet                                  Suppress help message
  -B, --browse                                 Browse SMB servers using DNS

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