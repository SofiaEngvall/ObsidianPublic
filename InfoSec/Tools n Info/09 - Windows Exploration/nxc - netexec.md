



### Help

```sh
┌──(kali㉿kali)-[~]
└─$ nxc --help                                    
usage: nxc [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--no-progress] [--verbose] [--debug] [--version]
           {wmi,smb,mssql,ldap,rdp,ssh,ftp,vnc,winrm} ...

     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /ॱ-ॱ\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ॱ \   / ॱ
     ॱ   ॱ

    The network execution tool
    Maintained as an open source project by @NeffIsBack, @MJHallenbeck, @_zblurx
    
    For documentation and usage examples, visit: https://www.netexec.wiki/

    Version : 1.1.0
    Codename: nxc4u
    Commit  : f3fd612
    

options:
  -h, --help            show this help message and exit
  -t THREADS            set how many concurrent threads to use (default: 256)
  --timeout TIMEOUT     max timeout in seconds of each thread (default: None)
  --jitter INTERVAL     sets a random delay between each connection (default: None)
  --no-progress         Not displaying progress bar during scan
  --verbose             enable verbose output
  --debug               enable debug level information
  --version             Display nxc version

protocols:
  available protocols

  {wmi,smb,mssql,ldap,rdp,ssh,ftp,vnc,winrm}
    wmi                 own stuff using WMI
    smb                 own stuff using SMB
    mssql               own stuff using MSSQL
    ldap                own stuff using LDAP
    rdp                 own stuff using RDP
    ssh                 own stuff using SSH
    ftp                 own stuff using FTP
    vnc                 own stuff using VNC
    winrm               own stuff using WINRM

```


