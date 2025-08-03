
`smbmap -H 10.10.10.10`

with creds
`smbmap -H 10.129.170.211 -u "svc-printer" -p '1edFg43012!!'`

execute command (using wmi by default)
`smbmap -H 10.129.170.211 -u "svc-printer" -p '1edFg43012!!' -x 'net group "Domain Admins" /domain'`

`smbmap -H 10.129.170.211 -u "svc-printer" -p '1edFg43012!!' -x 'dir' --mode psexec`



### Examples

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ smbmap -H 10.129.170.211 -u "svc-printer" -p '1edFg43012!!'        

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[\] Checking for open ports...
[|] Checking for open ports...
[*] Detected 1 hosts serving SMB
[*] Established 1 SMB connections(s) and 1 authenticated session(s)

[+] IP: 10.129.170.211:445      Name: PRINTER                   Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  READ ONLY       Remote Admin
        C$                                                      READ ONLY       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections  
```
### Help

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ smbmap                                
usage: smbmap [-h] (-H HOST | --host-file FILE) [-u USERNAME] [-p PASSWORD | --prompt] [-k] [--no-pass] [--dc-ip IP or Host]
              [-s SHARE] [-d DOMAIN] [-P PORT] [-v] [--signing] [--admin] [--no-banner] [--no-color] [--no-update]
              [--timeout SCAN_TIMEOUT] [-x COMMAND] [--mode CMDMODE] [-L | -r [PATH]] [-g FILE | --csv FILE] [--dir-only]
              [--no-write-check] [-q] [--depth DEPTH] [--exclude SHARE [SHARE ...]] [-A PATTERN] [-F PATTERN]
              [--search-path PATH] [--search-timeout TIMEOUT] [--download PATH] [--upload SRC DST] [--delete PATH TO FILE]
              [--skip]

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

options:
  -h, --help            show this help message and exit

Main arguments:
  -H HOST               IP or FQDN
  --host-file FILE      File containing a list of hosts
  -u, --username USERNAME
                        Username, if omitted null session assumed
  -p, --password PASSWORD
                        Password or NTLM hash, format is LMHASH:NTHASH
  --prompt              Prompt for a password
  -s SHARE              Specify a share (default C$), ex 'C$'
  -d DOMAIN             Domain name (default WORKGROUP)
  -P PORT               SMB port (default 445)
  -v, --version         Return the OS version of the remote host
  --signing             Check if host has SMB signing disabled, enabled, or required
  --admin               Just report if the user is an admin
  --no-banner           Removes the banner from the top of the output
  --no-color            Removes the color from output
  --no-update           Removes the "Working on it" message
  --timeout SCAN_TIMEOUT
                        Set port scan socket timeout. Default is .5 seconds

Kerberos settings:
  -k, --kerberos        Use Kerberos authentication
  --no-pass             Use CCache file (export KRB5CCNAME='~/current.ccache')
  --dc-ip IP or Host    IP or FQDN of DC

Command Execution:
  Options for executing commands on the specified host

  -x COMMAND            Execute a command ex. 'ipconfig /all'
  --mode CMDMODE        Set the execution method, wmi or psexec, default wmi

Shard drive Search:
  Options for searching/enumerating the share of the specified host(s)

  -L                    List all drives on the specified host, requires ADMIN rights.
  -r [PATH]             Recursively list dirs and files (no share\path lists the root of ALL shares), ex. 'email/backup'
  -g FILE               Output to a file in a grep friendly format, used with -r (otherwise it outputs nothing), ex -g
                        grep_out.txt
  --csv FILE            Output to a CSV file, ex --csv shares.csv
  --dir-only            List only directories, ommit files.
  --no-write-check      Skip check to see if drive grants WRITE access.
  -q                    Quiet verbose output. Only shows shares you have READ or WRITE on, and suppresses file listing when
                        performing a search (-A).
  --depth DEPTH         Traverse a directory tree to a specific depth. Default is 1 (root node).
  --exclude SHARE [SHARE ...]
                        Exclude share(s) from searching and listing, ex. --exclude ADMIN$ C$
  -A PATTERN            Define a file name pattern (regex) that auto downloads a file on a match (requires -r), not case
                        sensitive, ex '(web|global).(asax|config)'

File Content Search:
  Options for searching the content of files (must run as root), kind of experimental

  -F PATTERN            File content search, -F '[Pp]assword' (requires admin access to execute commands, and PowerShell on
                        victim host)
  --search-path PATH    Specify drive/path to search (used with -F, default C:\Users), ex D:\HR\
  --search-timeout TIMEOUT
                        Specifcy a timeout (in seconds) before the file search job gets killed. Default is 300 seconds.

Filesystem interaction:
  Options for interacting with the specified host´s filesystem

  --download PATH       Download a file from the remote system, ex.'C$\temp\passwords.txt'
  --upload SRC DST      Upload a file to the remote system ex. '/tmp/payload.exe C$\temp\payload.exe'
  --delete PATH TO FILE
                        Delete a remote file, ex. 'C$\temp\msf.exe'
  --skip                Skip delete file confirmation prompt

Examples:

$ smbmap -u jsmith -p password1 -d workgroup -H 192.168.0.1
$ smbmap -u jsmith -p 'aad3b435b51404eeaad3b435b51404ee:da76f2c4c96028b7a6111aef4a50a94d' -H 172.16.0.20
$ smbmap -u 'apadmin' -p 'asdf1234!' -d ACME -Hh 10.1.3.30 -x 'net group "Domain Admins" /domain'
```

