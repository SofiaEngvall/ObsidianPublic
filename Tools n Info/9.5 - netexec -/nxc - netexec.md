
available protocols: wmi, smb, mssql, ldap, rdp, ssh, ftp, vnc, winrm



### Help

```sh
┌──(fixit42㉿kali)-[~]
└─$ nxc -h
usage: nxc [-h] [--version] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL] [--verbose] [--debug] [--no-progress]
           [--log LOG] [-6] [--dns-server DNS_SERVER] [--dns-tcp] [--dns-timeout DNS_TIMEOUT]
           {smb,winrm,rdp,ftp,ssh,ldap,nfs,mssql,vnc,wmi} ...

     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /˙-˙\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ˙ \   / ˙
     ˙   ˙

    The network execution tool
    Maintained as an open source project by @NeffIsBack, @MJHallenbeck, @_zblurx
    
    For documentation and usage examples, visit: https://www.netexec.wiki/

    Version : 1.4.0
    Codename: SmoothOperator
    Commit  : Kali Linux
    

options:
  -h, --help            show this help message and exit

Generic:
  Generic options for nxc across protocols

  --version             Display nxc version
  -t, --threads THREADS
                        set how many concurrent threads to use
  --timeout TIMEOUT     max timeout in seconds of each thread
  --jitter INTERVAL     sets a random delay between each authentication

Output:
  Options to set verbosity levels and control output

  --verbose             enable verbose output
  --debug               enable debug level information
  --no-progress         do not displaying progress bar during scan
  --log LOG             export result into a custom file

DNS:
  -6                    Enable force IPv6
  --dns-server DNS_SERVER
                        Specify DNS server (default: Use hosts file & System DNS)
  --dns-tcp             Use TCP instead of UDP for DNS queries
  --dns-timeout DNS_TIMEOUT
                        DNS query timeout in seconds

Available Protocols:
  {smb,winrm,rdp,ftp,ssh,ldap,nfs,mssql,vnc,wmi}
    smb                 own stuff using SMB
    winrm               own stuff using WINRM
    rdp                 own stuff using RDP
    ftp                 own stuff using FTP
    ssh                 own stuff using SSH
    ldap                own stuff using LDAP
    nfs                 own stuff using NFS
    mssql               own stuff using MSSQL
    vnc                 own stuff using VNC
    wmi                 own stuff using WMI
```

