
We have the root of c:\ and we download some files of interest. Downloded files:
```sh
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ ls -la
total 2040
drwxrwxr-x  2 kali kali    4096 May 16 18:05  .
drwxr-xr-x 12 kali kali    4096 May 16 17:33  ..
-rw-rw-r--  1 kali kali      82 Dec 14  2017  auth0.htm
-rw-rw-r--  1 kali kali      34 Dec 14  2017  authzclientid.htm
-rw-rw-r--  1 kali kali      32 Dec 14  2017  authzdomain.htm
-rw-rw-r--  1 kali kali     669 Feb  3  2019  dh.log
-rw-rw-r--  1 kali kali     245 Feb  3  2019  dh.pem
-rw-rw-r--  1 kali kali   27066 Feb 26  2019  ex190226.log
-rw-rw-r--  1 kali kali      83 Dec 14  2017  generatedh.bat
-rw-rw-r--  1 kali kali     799 Feb  1  2018  mapdashboard.htm
-rw-rw-r--  1 kali kali   10835 Dec 14  2017  openssl.cnf
-rw-rw-r--  1 kali kali    1326 Dec 14  2017  prtg.crt
-rw-rw-r--  1 kali kali    1195 Feb  3  2019 'PRTG Enterprise Console.lnk'
-rw-rw-r--  1 kali kali    1675 Dec 14  2017  prtg.key
-rw-rw-r--  1 kali kali    1160 Feb  3  2019 'PRTG Network Monitor.lnk'
-rw-rw-r--  1 kali kali 1972066 Feb  3  2019 'PRTG Setup Log.log'
-rw-rw-r--  1 kali kali     916 Dec 14  2017  root.pem
-rw-rw-r--  1 kali kali     206 Jul 16  2016  system.ini
-rw-rw-r--  1 kali kali      15 Dec 14  2017  testlogin.htm
-rw-rw-r--  1 kali kali      33 May 16 14:16  user.txt
-rw-rw-r--  1 kali kali      85 Jul 16  2016  win.ini
```

```sh
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ cat PRTG\ Setup\ Log.log 
2019-02-02 23:15:27.661   Log opened. (Time zone: UTC-05:00)
2019-02-02 23:15:27.661   Setup version: Inno Setup version 5.5.9 (u)
2019-02-02 23:15:27.661   Original Setup EXE: C:\windows\temp\PRTG Network Monitor 18.1.37.13946 Setup (Stable).exe
2019-02-02 23:15:27.661   Setup command line: /SL5="$40022,186817002,417280,C:\windows\temp\PRTG Network Monitor 18.1.37.13946 Setup (Stable).exe" /silent /adminemail="na@na.com" /norestart  /licensekeyname="prtgtrial" /licensekey="000014-15UKFM-8FFP64-J5HKKP-TQ89F4-BJ8D9R-TC8ZNZ-DZR1W7-74BC9T-QJE1EK" 
2019-02-02 23:15:27.661   Windows version: 10.0.14393  (NT platform: Yes)
2019-02-02 23:15:27.661   64-bit Windows: Yes
2019-02-02 23:15:27.661   Processor architecture: x64
2019-02-02 23:15:27.661   User privileges: Administrative
2019-02-02 23:15:27.692   64-bit install mode: No
2019-02-02 23:15:27.692   Created temporary directory: C:\Users\ADMINI~1\AppData\Local\Temp\is-VM11G.tmp
2019-02-02 23:15:27.723   Extracting temporary file: C:\Users\ADMINI~1\AppData\Local\Temp\is-VM11G.tmp\IsLocalSystem.dll
2019-02-02 23:15:27.770   InitializeSetup
2019-02-02 23:15:27.770   CommonInit
2019-02-02 23:15:27.770   Running on 64bit.
2019-02-02 23:15:27.770   CommonInit A
2019-02-02 23:15:27.770   CommonInit B
2019-02-02 23:15:27.770   CommonInit C
2019-02-02 23:15:27.770   CommonInit D
2019-02-02 23:15:28.786   CommonInit E
2019-02-02 23:15:28.786   Kill Task PRTG Enterprise Console.exe
2019-02-02 23:15:28.926   Kill Task Result 259
2019-02-02 23:15:28.926   CommonInit F
2019-02-02 23:15:28.926   GetRegistryPath
2019-02-02 23:15:28.926   GetRegistryPath software\Paessler\PRTG Network Monitor
2019-02-02 23:15:28.926   No Admin Name set => Initial Install
```

everything since I'm closing the tab
```sh
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||50361|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
11-10-23  10:20AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50364|)
125 Data connection already open; Transfer starting.
02-25-19  11:44PM       <DIR>          Administrator
01-15-24  11:03AM       <DIR>          Public
226 Transfer complete.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50372|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd desktop
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50373|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1195 PRTG Enterprise Console.lnk
02-03-19  12:18AM                 1160 PRTG Network Monitor.lnk
05-16-25  08:16AM                   34 user.txt
226 Transfer complete.
ftp> get user.txt
local: user.txt remote: user.txt
229 Entering Extended Passive Mode (|||50374|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|    34        1.43 KiB/s    00:00 ETA
226 Transfer complete.
34 bytes received in 00:00 (1.41 KiB/s)
ftp> cd..
?Invalid command.
ftp> cd ..
250 CWD command successful.
ftp> cd desktop
250 CWD command successful.
ftp> get user.txt
local: user.txt remote: user.txt
229 Entering Extended Passive Mode (|||50477|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    34        1.45 KiB/s    00:00 ETA
226 Transfer complete.
34 bytes received in 00:00 (1.40 KiB/s)
ftp> pwd
421 Service not available, remote server has closed connection.
Unable to determine remote directory
ftp> dir
Not connected.
ftp> 
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||50658|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
11-10-23  10:20AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users
250 CWD command successful.
ftp> cd administrator
550 Access is denied. 
ftp> cd ..
250 CWD command successful.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50753|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
11-10-23  10:20AM       <DIR>          Windows
226 Transfer complete.
ftp> cd windows
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||50755|)
125 Data connection already open; Transfer starting.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:20AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  08:45AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> cd config
421 Service not available, remote server has closed connection.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> cd windows
250 CWD command successful.
ftp> cd config
550 The system cannot find the file specified. 
ftp> dir
229 Entering Extended Passive Mode (|||50803|)
150 Opening ASCII mode data connection.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:22AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  09:20AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> get sam
local: sam remote: sam
229 Entering Extended Passive Mode (|||50814|)
550 The system cannot find the file specified. 
ftp> get SAM
local: SAM remote: SAM
421 Service not available, remote server has closed connection.
ftp> cd ..
Not connected.
ftp> dir
Not connected.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||51226|)
125 Data connection already open; Transfer starting.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd inetpup
550 The system cannot find the file specified. 
ftp> dir
229 Entering Extended Passive Mode (|||51236|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd inetpub
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51246|)
150 Opening ASCII mode data connection.
02-25-19  08:07AM       <DIR>          ftproot
02-25-19  10:15PM       <DIR>          logs
02-25-19  10:15PM       <DIR>          temp
02-25-19  10:15PM       <DIR>          wwwroot
226 Transfer complete.
ftp> cd wwroot
550 The system cannot find the file specified. 
ftp> cd wwwroot
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51247|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> cd ftproot
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51248|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> cd temp
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51251|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> dir
229 Entering Extended Passive Mode (|||51259|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51260|)
150 Opening ASCII mode data connection.
02-25-19  08:07AM       <DIR>          ftproot
02-25-19  10:15PM       <DIR>          logs
02-25-19  10:15PM       <DIR>          temp
02-25-19  10:15PM       <DIR>          wwwroot
226 Transfer complete.
ftp> cd logs
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51261|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          FailedReqLogFiles
02-25-19  09:52PM       <DIR>          LogFiles
02-25-19  10:15PM       <DIR>          wmsvc
226 Transfer complete.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous                                  
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||51418|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd windows
221 Goodbye.
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> cd windows/system32
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51421|)
150 Opening ASCII mode data connection.
11-20-16  09:53PM       <DIR>          0409
07-16-16  09:12AM                  404 @VpnToastIcon.png
11-20-16  09:59PM              5511680 aclui.dll
07-16-16  09:13AM               237408 ActionQueue.dll
07-16-16  09:13AM               264704 activeds.dll
07-16-16  09:13AM               112128 activeds.tlb
07-16-16  09:10AM              3541504 actxprxy.dll
07-16-16  09:12AM                23552 adhapi.dll
07-16-16  09:12AM                77312 adhsvc.dll
07-16-16  09:12AM               555520 AdmTmpl.dll
02-25-19  08:07AM                55296 admwprox.dll
07-16-16  09:13AM                59392 adprovider.dll
07-16-16  09:13AM               248320 adsldp.dll
07-16-16  09:13AM               249344 adsldpc.dll
11-20-16  09:59PM                99328 adsmsext.dll
07-16-16  09:13AM               338944 adsnt.dll
07-16-16  09:09AM               827392 adtschema.dll
07-16-16  09:18AM       <DIR>          AdvancedInstallers
07-16-16  09:12AM               652352 advapi32.dll
07-16-16  09:09AM               357448 advapi32legacy.dll
07-16-16  09:09AM                 2560 advapi32res.dll
07-16-16  09:13AM               135680 advpack.dll
02-25-19  08:07AM                53248 ahadmin.dll
07-16-16  09:09AM                49152 amsi.dll
07-16-16  09:09AM                14848 amsiproxy.dll
07-16-16  09:12AM               261120 apds.dll
07-16-16  09:12AM               100704 apisetschema.dll
07-16-16  09:13AM               481280 apphelp.dll
07-16-16  09:13AM                65648 appidapi.dll
07-16-16  09:13AM                19456 appidcertstorecheck.exe
07-16-16  09:13AM               160256 appidpolicyconverter.exe
07-16-16  09:12AM               410624 AppIdPolicyEngineApi.dll
07-16-16  09:13AM               124416 appidsvc.dll
07-16-16  09:13AM                27648 appidtel.exe
07-16-16  09:18AM       <DIR>          AppLocker
07-16-16  09:13AM               336384 AppLockerCSP.dll
07-16-16  09:12AM               197632 appmgmts.dll
07-16-16  09:12AM               453632 appmgr.dll
07-16-16  09:13AM               191840 AppxAllUserStore.dll
11-20-16  09:59PM               203776 AppXApplicabilityBlob.dll
11-20-16  09:59PM               406016 AppXDeploymentClient.dll
11-20-16  09:59PM               956416 AppXDeploymentExtensions.desktop.dll
11-20-16  09:59PM              1690112 AppXDeploymentExtensions.onecore.dll
11-20-16  09:59PM               395776 AppXDeploymentExtensions.server.dll
11-20-16  09:59PM              2273792 AppXDeploymentServer.dll
11-20-16  09:59PM              1112928 AppxPackaging.dll
07-16-16  09:13AM                 2711 AppxProvisioning.xml
07-16-16  09:10AM               178176 AppxSip.dll
07-16-16  09:10AM                12800 AppxStreamingDataSourcePS.dll
07-16-16  09:18AM       <DIR>          ar-SA
07-16-16  09:09AM                26112 ARP.EXE
07-16-16  09:14AM                30912 aspnet_counters.dll
11-20-16  09:59PM                89088 asycfilt.dll
07-16-16  09:13AM                29696 at.exe
07-16-16  09:12AM                97280 atl.dll
11-20-16  09:59PM               378720 atmfd.dll
11-20-16  09:59PM                45056 atmlib.dll
07-16-16  09:09AM                20480 attrib.exe
07-16-16  09:13AM               204288 auditcse.dll
07-16-16  09:12AM               223232 AuditNativeSnapIn.dll
07-16-16  09:09AM                35840 auditpol.exe
07-16-16  09:09AM                51200 auditpolcore.dll
07-16-16  09:12AM                73728 AuditPolicyGPInterop.dll
07-16-16  09:12AM                95744 auditpolmsg.dll
07-16-16  09:13AM               488960 authfwcfg.dll
11-20-16  09:59PM               881664 authui.dll
07-16-16  09:09AM               280064 authz.dll
07-16-16  09:09AM               968704 autochk.exe
07-16-16  09:13AM               953856 autoconv.exe
07-16-16  09:13AM               925184 autofmt.exe
07-16-16  09:13AM               906752 azroles.dll
07-16-16  09:13AM                31744 AzSqlExt.dll
07-16-16  09:13AM               201056 basecsp.dll
07-16-16  09:09AM                65536 basesrv.dll
07-16-16  09:09AM                97128 bcd.dll
07-16-16  09:13AM               173056 bcdboot.exe
11-20-16  09:59PM               425472 bcdedit.exe
07-16-16  09:10AM                78848 bcdprov.dll
07-16-16  09:10AM                89600 bcdsrv.dll
07-16-16  09:10AM               414744 BCP47Langs.dll
07-16-16  09:09AM               168424 bcrypt.dll
07-16-16  09:09AM               431296 bcryptprimitives.dll
07-16-16  09:18AM       <DIR>          BestPractices
07-16-16  09:13AM               795648 BFE.DLL
07-16-16  09:18AM       <DIR>          bg-BG
07-16-16  09:12AM                65024 bidispl.dll
07-16-16  09:12AM               301056 BingASDS.dll
07-16-16  09:09AM                25088 bitsperf.dll
07-16-16  09:09AM                56832 BitsProxy.dll
07-16-16  09:15AM                77824 BlbEvents.dll
11-20-16  09:59PM       <DIR>          Boot
07-16-16  09:13AM              3170304 boot.sdi
07-16-16  09:13AM                89088 bootcfg.exe
07-16-16  09:13AM                 3072 bootstr.dll
07-16-16  09:09AM                25952 BOOTVID.DLL
07-16-16  09:14AM                 7680 BPAInst.dll
07-16-16  09:09AM               254976 BrokerLib.dll
07-16-16  09:14AM                58368 browcli.dll
07-16-16  09:14AM               134656 browser.dll
11-20-16  09:59PM                97792 browserbroker.dll
07-16-16  09:14AM                26464 browser_broker.exe
07-16-16  09:10AM                51200 ByteCodeGenerator.exe
07-16-16  09:09AM                77312 cabapi.dll
07-16-16  09:09AM               145216 cabinet.dll
07-16-16  09:13AM                32768 cacls.exe
07-16-16  09:11AM                 4119 CallUxxProvider.vbs
07-16-16  09:13AM                62464 capiprovider.dll
07-16-16  09:13AM                23552 capisp.dll
07-16-16  09:18AM       <DIR>          CatRoot
02-25-19  11:58PM       <DIR>          catroot2
07-16-16  09:13AM               459264 catsrv.dll
07-16-16  09:13AM                49664 catsrvps.dll
07-16-16  09:13AM               493056 catsrvut.dll
07-16-16  09:12AM                34304 cbclient.dll
11-20-16  09:59PM               227328 cdd.dll
07-16-16  09:09AM               775168 certca.dll
07-16-16  09:09AM               451072 certcli.dll
07-16-16  09:13AM               440320 certCredProvider.dll
07-16-16  09:13AM                65536 certenc.dll
11-20-16  09:59PM              2914304 CertEnroll.dll
07-16-16  09:09AM                51712 CertEnrollCtrl.exe
07-16-16  09:13AM                61440 CertPKICmdlet.dll
07-16-16  09:13AM               116224 CertPolEng.dll
07-16-16  09:13AM               193536 certprop.dll
07-16-16  09:13AM               433152 certreq.exe
07-16-16  09:13AM              1417728 certutil.exe
07-16-16  09:12AM                78336 cfgbkend.dll
07-16-16  09:09AM               259848 cfgmgr32.dll
07-16-16  09:10AM                39776 cfmifs.dll
07-16-16  09:10AM                14848 cfmifsproxy.dll
07-16-16  09:12AM                17408 change.exe
11-20-16  09:59PM               130560 chartv.dll
07-16-16  09:13AM                14336 chcp.com
07-16-16  09:13AM                28672 CheckNetIsolation.exe
07-16-16  09:12AM                22528 chglogon.exe
07-16-16  09:12AM                25088 chgport.exe
07-16-16  09:12AM                22016 chgusr.exe
07-16-16  09:09AM                25600 chkdsk.exe
07-16-16  09:13AM                20480 chkntfs.exe
07-16-16  09:13AM                25600 chkwudrv.dll
07-16-16  09:13AM                33792 choice.exe
07-16-16  09:12AM                12800 CHxReadingStringIME.dll
11-20-16  09:59PM               634944 ci.dll
07-16-16  09:13AM                46592 cipher.exe
07-16-16  09:15AM                38912 CIWmi.dll
07-16-16  09:13AM                18432 clb.dll
07-16-16  09:13AM               631176 clbcatq.dll
07-16-16  09:09AM                76288 clfsw32.dll
07-16-16  09:12AM                86016 cliconfg.dll
07-16-16  09:12AM                30720 cliconfg.exe
07-16-16  09:12AM                37376 cliconfg.rll
07-16-16  09:13AM                30208 clip.exe
07-16-16  09:13AM               122984 Clipc.dll
07-16-16  09:13AM               729328 ClipSVC.dll
07-16-16  09:10AM                16384 clrhost.dll
11-20-16  09:59PM               715264 clusapi.dll
07-16-16  09:09AM               232960 cmd.exe
07-16-16  09:13AM                13824 cmdext.dll
07-16-16  09:13AM                19968 cmdkey.exe
11-20-16  09:59PM                93184 cmifw.dll
07-16-16  09:13AM               110080 cngcredui.dll
02-25-19  08:07AM                14336 cngkeyhelper.dll
07-16-16  09:13AM                66048 cngprovider.dll
07-16-16  09:13AM                39424 cnvfat.dll
07-16-16  09:18AM       <DIR>          CodeIntegrity
07-16-16  09:13AM                79872 colbact.dll
11-20-16  09:53PM       <DIR>          Com
11-20-16  09:59PM              2913104 combase.dll
07-16-16  09:13AM                10240 comcat.dll
07-16-16  09:12AM               684384 comctl32.dll
11-20-16  09:59PM               991232 comdlg32.dll
07-16-16  09:13AM               435552 coml2.dll
07-16-16  09:13AM                25088 comp.exe
07-16-16  09:13AM                44544 compact.exe
11-20-16  09:59PM                78688 CompatTelRunner.exe
07-16-16  09:12AM               309760 compstui.dll
07-16-16  09:13AM               111104 comrepl.dll
07-16-16  09:13AM              1295360 comres.dll
11-20-16  09:59PM              1639424 comsvcs.dll
12-15-21  10:49AM       <DIR>          config
07-16-16  09:18AM       <DIR>          Configuration
07-16-16  09:11AM                47104 Configure-SMRemoting.exe
07-16-16  09:13AM                47104 conhost.exe
07-16-16  09:13AM               325120 ConhostV1.dll
07-16-16  09:13AM               339456 ConhostV2.dll
07-16-16  09:12AM               102400 console.dll
11-20-16  09:59PM               266240 ConsoleLogon.dll
07-16-16  09:12AM               117760 control.exe
07-16-16  09:13AM                21504 convert.exe
11-20-16  09:59PM               764936 CoreMessaging.dll
07-16-16  09:12AM                88576 correngine.dll
07-16-16  09:12AM                69232 CredentialUIBroker.exe
11-20-16  09:59PM               461312 CredProvDataModel.dll
11-20-16  09:59PM               243712 credprovhost.dll
11-20-16  09:59PM               157696 credprovs.dll
11-20-16  09:59PM               166912 credprovslegacy.dll
07-16-16  09:09AM                23552 credssp.dll
07-16-16  09:13AM                47104 credui.dll
11-20-16  09:59PM              1851696 crypt32.dll
07-16-16  09:09AM                31080 cryptbase.dll
07-16-16  09:09AM               129024 cryptcatsvc.dll
07-16-16  09:09AM                71848 cryptdll.dll
07-16-16  09:09AM               170496 cryptnet.dll
11-20-16  09:59PM               376832 CryptoWinRT.dll
07-16-16  09:09AM                81176 cryptsp.dll
07-16-16  09:09AM                81920 cryptsvc.dll
07-16-16  09:13AM                57344 crypttpmeksvc.dll
07-16-16  09:13AM               600576 cryptui.dll
07-16-16  09:13AM               382464 cryptuiwizard.dll
07-16-16  09:10AM               127624 cryptxml.dll
07-16-16  09:18AM       <DIR>          cs-CZ
07-16-16  09:13AM                52736 cscapi.dll
07-16-16  09:13AM                29696 cscdll.dll
07-16-16  09:12AM               163328 cscript.exe
07-16-16  09:14AM                 6144 CSDeployRes.dll
11-20-16  09:59PM                58368 csrsrv.dll
07-16-16  09:09AM                18144 csrss.exe
07-16-16  09:09AM                26112 CSystemEventsBrokerClient.dll
07-16-16  09:12AM                10752 ctfmon.exe
07-16-16  09:13AM                66082 C_037.NLS
07-16-16  09:13AM                66082 C_10000.NLS
07-16-16  09:13AM               162850 C_10001.NLS
07-16-16  09:13AM               195618 C_10002.NLS
07-16-16  09:13AM               177698 C_10003.NLS
07-16-16  09:13AM                66082 C_10004.NLS
07-16-16  09:13AM                66082 C_10005.NLS
07-16-16  09:13AM                66082 C_10006.NLS
07-16-16  09:13AM                66082 C_10007.NLS
07-16-16  09:13AM               173602 C_10008.NLS
07-16-16  09:13AM                66082 C_10010.NLS
07-16-16  09:13AM                66082 C_10017.NLS
07-16-16  09:13AM                66082 C_10021.NLS
07-16-16  09:13AM                66082 C_10029.NLS
07-16-16  09:13AM                66082 C_10079.NLS
07-16-16  09:13AM                66082 C_10081.NLS
07-16-16  09:13AM                66082 C_10082.NLS
07-16-16  09:13AM                66082 C_1026.NLS
07-16-16  09:13AM                66082 C_1047.NLS
07-16-16  09:13AM                66082 C_1140.NLS
07-16-16  09:13AM                66082 C_1141.NLS
07-16-16  09:13AM                66082 C_1142.NLS
07-16-16  09:13AM                66082 C_1143.NLS
07-16-16  09:13AM                66082 C_1144.NLS
07-16-16  09:13AM                66082 C_1145.NLS
07-16-16  09:13AM                66082 C_1146.NLS
07-16-16  09:13AM                66082 C_1147.NLS
07-16-16  09:13AM                66082 C_1148.NLS
07-16-16  09:13AM                66082 C_1149.NLS
07-16-16  09:13AM                66082 C_1250.NLS
07-16-16  09:13AM                66082 C_1251.NLS
07-16-16  09:09AM                66082 C_1252.NLS
07-16-16  09:13AM                66082 C_1253.NLS
07-16-16  09:13AM                66082 C_1254.NLS
07-16-16  09:13AM                66082 C_1255.NLS
07-16-16  09:13AM                66082 C_1256.NLS
07-16-16  09:13AM                66082 C_1257.NLS
07-16-16  09:13AM                66082 C_1258.NLS
07-16-16  09:13AM               189986 C_1361.NLS
07-16-16  09:13AM               180258 C_20000.NLS
07-16-16  09:13AM               186402 C_20001.NLS
07-16-16  09:13AM               173602 C_20002.NLS
07-16-16  09:13AM               185378 C_20003.NLS
07-16-16  09:13AM               180258 C_20004.NLS
07-16-16  09:13AM               187938 C_20005.NLS
07-16-16  09:13AM                66082 C_20105.NLS
07-16-16  09:13AM                66082 C_20106.NLS
07-16-16  09:13AM                66082 C_20107.NLS
07-16-16  09:13AM                66082 C_20108.NLS
07-16-16  09:13AM                66082 C_20127.NLS
07-16-16  09:13AM               139810 C_20261.NLS
07-16-16  09:13AM                66082 C_20269.NLS
07-16-16  09:13AM                66082 C_20273.NLS
07-16-16  09:13AM                66082 C_20277.NLS
07-16-16  09:13AM                66082 C_20278.NLS
07-16-16  09:13AM                66082 C_20280.NLS
07-16-16  09:13AM                66082 C_20284.NLS
07-16-16  09:13AM                66082 C_20285.NLS
07-16-16  09:13AM                66082 C_20290.NLS
07-16-16  09:13AM                66082 C_20297.NLS
07-16-16  09:13AM                66082 C_20420.NLS
07-16-16  09:13AM                66082 C_20423.NLS
07-16-16  09:13AM                66082 C_20424.NLS
07-16-16  09:13AM                66082 C_20833.NLS
07-16-16  09:13AM                66082 C_20838.NLS
07-16-16  09:13AM                66082 C_20866.NLS
07-16-16  09:13AM                66082 C_20871.NLS
07-16-16  09:13AM                66082 C_20880.NLS
07-16-16  09:13AM                66082 C_20905.NLS
07-16-16  09:13AM                66082 C_20924.NLS
07-16-16  09:13AM               180770 C_20932.NLS
07-16-16  09:13AM               173602 C_20936.NLS
07-16-16  09:13AM               177698 C_20949.NLS
07-16-16  09:13AM                66082 C_21025.NLS
07-16-16  09:13AM                66082 C_21027.NLS
07-16-16  09:13AM                66082 C_21866.NLS
07-16-16  09:13AM                66082 C_28591.NLS
07-16-16  09:13AM                66082 C_28592.NLS
07-16-16  09:13AM                66082 C_28593.NLS
07-16-16  09:13AM                66082 C_28594.NLS
07-16-16  09:13AM                66082 C_28595.NLS
07-16-16  09:13AM                66082 C_28596.NLS
07-16-16  09:13AM                66082 C_28597.NLS
07-16-16  09:13AM                66082 C_28598.NLS
07-16-16  09:13AM                66082 C_28599.NLS
07-16-16  09:13AM                66082 c_28603.nls
07-16-16  09:13AM                66082 C_28605.NLS
07-16-16  09:09AM                66594 C_437.NLS
07-16-16  09:13AM                66082 C_500.NLS
07-16-16  09:13AM                66082 C_708.NLS
07-16-16  09:13AM                66594 C_720.NLS
07-16-16  09:13AM                66594 C_737.NLS
07-16-16  09:13AM                66594 C_775.NLS
07-16-16  09:13AM                66594 C_850.NLS
07-16-16  09:13AM                66594 C_852.NLS
07-16-16  09:13AM                66594 C_855.NLS
07-16-16  09:13AM                66594 C_857.NLS
07-16-16  09:13AM                66594 C_858.NLS
07-16-16  09:13AM                66594 C_860.NLS
07-16-16  09:13AM                66594 C_861.NLS
07-16-16  09:13AM                66594 C_862.NLS
07-16-16  09:13AM                66594 C_863.NLS
07-16-16  09:13AM                66594 C_864.NLS
07-16-16  09:13AM                66594 C_865.NLS
07-16-16  09:13AM                66594 C_866.NLS
07-16-16  09:13AM                66594 C_869.NLS
07-16-16  09:13AM                66082 C_870.NLS
07-16-16  09:13AM                66594 C_874.NLS
07-16-16  09:13AM                66082 C_875.NLS
11-20-16  09:59PM               162850 C_932.NLS
07-16-16  09:13AM               196642 C_936.NLS
07-16-16  09:13AM               196642 C_949.NLS
07-16-16  09:13AM               196642 C_950.NLS
11-20-16  09:59PM               227840 C_G18030.DLL
11-20-16  09:59PM                14848 c_GSM7.DLL
11-20-16  09:59PM                17408 C_IS2022.DLL
07-16-16  09:13AM                14336 C_ISCII.DLL
11-20-16  09:59PM              5611008 d2d1.dll
07-16-16  09:12AM               400304 d3d10level9.dll
11-20-16  09:59PM              2678056 d3d10warp.dll
11-20-16  09:59PM              2827864 d3d11.dll
11-20-16  09:59PM              1005568 D3D12.dll
07-16-16  09:12AM                13824 d3d8thk.dll
11-20-16  09:59PM              1609920 d3d9.dll
07-16-16  09:18AM       <DIR>          da-DK
11-20-16  09:59PM               109056 dab.dll
07-16-16  09:09AM                13824 dabapi.dll
07-16-16  09:12AM               120320 DafPrintProvider.dll
07-16-16  09:13AM                26624 davhlpr.dll
07-16-16  09:09AM               151552 dbgcore.dll
11-20-16  09:59PM              5384192 dbgeng.dll
07-16-16  09:09AM              1529344 dbghelp.dll
11-20-16  09:59PM               650240 DbgModel.dll
07-16-16  09:12AM               117760 dbnetlib.dll
07-16-16  09:12AM                23552 dbnmpntw.dll
07-16-16  09:11AM                67584 dcgpofix.exe
07-16-16  09:12AM                14336 dciman32.dll
07-16-16  09:12AM               218112 dcpromo.exe
07-16-16  09:12AM               479232 DDDS.dll
07-16-16  09:18AM       <DIR>          de-DE
07-16-16  09:16AM                  858 DefaultQuestions.json
07-16-16  09:13AM               186880 Defrag.exe
07-16-16  09:13AM                19968 defragproxy.dll
07-16-16  09:13AM                 4096 defragres.dll
07-16-16  09:13AM               511488 defragsvc.dll
11-20-16  09:59PM                26112 delegatorprovider.dll
11-20-16  09:59PM               283488 DeviceCensus.exe
07-16-16  09:13AM               101216 DeviceReactivation.dll
07-16-16  09:09AM               151904 devobj.dll
07-16-16  09:09AM                58880 devrtl.dll
07-16-16  09:09AM                64512 dfscli.dll
07-16-16  09:10AM              1560064 dfshim.dll
07-16-16  09:13AM                78848 dggpext.dll
07-16-16  09:12AM                14848 dhcpcmonitor.dll
07-16-16  09:09AM               360960 dhcpcore.dll
11-20-16  09:59PM               265728 dhcpcore6.dll
07-16-16  09:09AM                85504 dhcpcsvc.dll
07-16-16  09:09AM                67072 dhcpcsvc6.dll
07-16-16  09:12AM               216576 dhcpsapi.dll
11-20-16  09:59PM       <DIR>          DiagSvcs
11-20-16  09:59PM              1980416 diagtrack.dll
07-16-16  09:13AM                26112 DIMC.exe
07-16-16  09:13AM                43520 dimsjob.dll
07-16-16  09:13AM                46592 dimsroam.dll
07-16-16  09:12AM               547008 directmanipulation.dll
11-20-16  09:59PM               250368 discan.dll
07-16-16  09:13AM               157696 diskpart.exe
07-16-16  09:12AM                25600 diskperf.exe
07-16-16  09:13AM               336896 diskraid.exe
07-16-16  09:13AM               452608 diskshadow.exe
11-20-16  09:59PM       <DIR>          Dism
07-16-16  09:10AM               299872 Dism.exe
07-16-16  09:10AM               914272 DismApi.dll
07-16-16  09:12AM                58880 dispci.dll
07-16-16  09:12AM                29184 dispex.dll
07-16-16  09:13AM                73216 djoin.exe
07-16-16  09:09AM                21344 dllhost.exe
07-16-16  09:13AM                12288 dllhst3g.exe
07-16-16  09:12AM               119328 dmcmnutils.dll
07-16-16  09:12AM                14336 dmiso8601utils.dll
11-20-16  09:59PM               646136 dnsapi.dll
07-16-16  09:13AM                32768 dnscacheugc.exe
07-16-16  09:09AM               264192 dnsrslvr.dll
07-16-16  09:13AM                19456 doskey.exe
07-16-16  02:04AM       <DIR>          downlevel
07-16-16  09:09AM                15360 dpapi.dll
07-16-16  09:13AM                76288 dpapimig.exe
07-16-16  09:13AM                57344 dpapiprovider.dll
07-16-16  09:09AM               198144 dpapisrv.dll
07-16-16  09:13AM               172032 dps.dll
07-16-16  09:13AM               495104 dpx.dll
07-16-16  09:13AM                81920 driverquery.exe
11-10-23  10:39AM       <DIR>          drivers
02-25-19  10:56PM       <DIR>          DriverStore
07-16-16  09:12AM                25600 drprov.dll
07-16-16  09:13AM                70144 drvcfg.exe
07-16-16  09:13AM               133632 drvinst.exe
02-25-19  10:56PM       <DIR>          DRVSTORE
11-20-16  09:59PM               908640 drvstore.dll
07-16-16  09:12AM                39424 dsauth.dll
11-20-16  09:59PM       <DIR>          dsc
11-20-16  09:59PM               471552 DscCore.dll
11-20-16  09:59PM               204288 DscCoreConfProv.dll
07-16-16  09:15AM                19968 dscproxy.dll
07-16-16  09:15AM                25600 DscTimer.dll
07-16-16  09:14AM                 4096 DsDeployRes.dll
07-16-16  09:12AM               132608 dskquota.dll
07-16-16  09:09AM                31744 dsparse.dll
07-16-16  09:12AM               171008 dsprop.dll
07-16-16  09:09AM                28456 dsrole.dll
07-16-16  09:16AM               215943 dssec.dat
07-16-16  09:12AM                57856 dssec.dll
07-16-16  09:09AM               151352 dssenh.dll
07-16-16  09:12AM               684544 dsuiext.dll
07-16-16  09:13AM               101888 DuCsps.dll
07-16-16  09:12AM              1714688 dui70.dll
07-16-16  09:12AM               585216 duser.dll
11-20-16  09:59PM               128864 dwmapi.dll
11-20-16  09:59PM              2476544 DWrite.dll
07-16-16  09:12AM               637400 dxgi.dll
07-16-16  09:12AM                20992 dxgwdi.dll
07-16-16  09:12AM               131248 dxva2.dll
07-16-16  09:12AM                13312 Eap3Host.exe
07-16-16  09:12AM               215552 eapa3hst.dll
07-16-16  09:12AM               119296 eapacfg.dll
07-16-16  09:12AM               214528 eapahost.dll
11-20-16  09:59PM               327168 eapp3hst.dll
11-20-16  09:59PM               243200 eappcfg.dll
11-20-16  09:59PM               105984 eappgnui.dll
11-20-16  09:59PM               302592 eapphost.dll
11-20-16  09:59PM                71168 eappprxy.dll
07-16-16  09:13AM                30208 eapprovp.dll
07-16-16  09:12AM               112128 eapsvc.dll
11-20-16  09:59PM               161792 EditionUpgradeHelper.dll
11-20-16  09:59PM               882680 EditionUpgradeManagerObj.dll
07-16-16  09:12AM               833536 efscore.dll
11-20-16  09:59PM                40448 efsext.dll
07-16-16  09:12AM                80384 efslsaext.dll
07-16-16  09:12AM                55296 efssvc.dll
07-16-16  09:12AM                41984 efsutil.dll
07-16-16  09:18AM       <DIR>          el-GR
11-20-16  09:53PM       <DIR>          en
07-16-16  09:18AM       <DIR>          en-GB
02-25-19  08:07AM       <DIR>          en-US
07-16-16  09:09AM                98152 EncDump.dll
07-16-16  09:18AM       <DIR>          es-ES
07-16-16  09:18AM       <DIR>          es-MX
07-16-16  09:13AM               453632 es.dll
07-16-16  09:13AM                19968 EsdSip.dll
11-20-16  09:59PM              3054080 esent.dll
07-16-16  09:13AM                68608 esentprf.dll
11-20-16  09:59PM               339968 esentutl.exe
07-16-16  09:13AM                36864 esevss.dll
07-16-16  09:14AM               100352 eShims.dll
07-16-16  09:14AM                17408 EssentialsConfigPluginNative.dll
07-16-16  09:18AM       <DIR>          et-EE
07-16-16  09:09AM                51712 ETWESEProviderResources.dll
07-16-16  09:09AM                49152 EtwRundown.dll
07-16-16  09:09AM                84480 EventAggregation.dll
07-16-16  09:15AM                17920 eventcls.dll
07-16-16  09:13AM                41472 eventcreate.exe
07-16-16  09:13AM                67072 expand.exe
07-16-16  09:12AM                 8704 f3ahvoas.dll
07-16-16  09:09AM               383776 Faultrep.dll
07-16-16  09:12AM                31232 FaxPrinterInstaller.dll
07-16-16  09:13AM                25088 fc.exe
07-16-16  09:12AM                20992 fdPHost.dll
07-16-16  09:12AM               290816 fdprint.dll
07-16-16  09:12AM                64512 fdProxy.dll
07-16-16  09:12AM               149504 fdWSD.dll
07-16-16  09:12AM                73728 feclient.dll
07-16-16  09:18AM       <DIR>          fi-FI
07-16-16  09:10AM                23552 FileAppxStreamingDataSource.dll
07-16-16  09:12AM               157696 FilterDS.dll
07-16-16  09:13AM                17408 find.exe
07-16-16  09:12AM                65536 findnetprinters.dll
07-16-16  09:09AM                34816 findstr.exe
07-16-16  09:09AM                15872 finger.exe
07-16-16  09:10AM               525824 FirewallAPI.dll
11-20-16  09:59PM               635904 FlightSettings.dll
07-16-16  09:09AM                23040 fltLib.dll
07-16-16  09:09AM                30208 fltMC.exe
07-16-16  09:09AM                58720 fmifs.dll
07-16-16  09:12AM               189952 fms.dll
11-20-16  10:15PM               109400 FNTCACHE.DAT
11-20-16  09:59PM              1840640 FntCache.dll
07-16-16  09:12AM               111616 Fondue.exe
11-20-16  09:59PM               628552 fontdrvhost.exe
07-16-16  09:12AM               123392 fontsub.dll
07-16-16  09:13AM                49664 forfiles.exe
07-16-16  09:09AM                36864 format.com
07-16-16  09:18AM       <DIR>          forwarders
07-16-16  09:18AM       <DIR>          fr-CA
07-16-16  09:18AM       <DIR>          fr-FR
07-16-16  09:12AM               249856 framedyn.dll
07-16-16  09:10AM               292864 framedynos.dll
07-16-16  09:14AM                 4096 FSDeployRes.dll
07-16-16  09:15AM                10752 FssmInst.dll
11-20-16  09:59PM                 2560 fssmres.dll
07-16-16  09:12AM               372224 fssprov.dll
07-16-16  09:13AM               156672 fsutil.exe
07-16-16  09:13AM                32768 fsutilext.dll
07-16-16  09:13AM                55808 ftp.exe
07-16-16  09:12AM               152064 fundisc.dll
07-16-16  09:10AM               154112 fwbase.dll
07-16-16  09:13AM                56832 fwcfg.dll
07-16-16  09:10AM               201216 fwpolicyiomgr.dll
07-16-16  09:13AM               412160 FWPUCLNT.DLL
07-16-16  09:12AM                95744 FwRemoteSvr.dll
07-16-16  09:13AM                65376 gacinstall.dll
07-16-16  09:12AM                91132 gatherNetworkInfo.vbs
11-20-16  09:59PM               206096 gdi32.dll
11-20-16  09:59PM              1572768 gdi32full.dll
11-20-16  09:59PM              1656832 GdiPlus.dll
11-20-16  09:59PM               595296 generaltel.dll
11-20-16  09:59PM               665768 GenValObj.exe
07-16-16  09:10AM               169984 globinputhost.dll
07-16-16  09:09AM                38400 gmsaclient.dll
07-16-16  09:13AM               128648 gpapi.dll
07-16-16  09:13AM              1099264 gpedit.dll
07-16-16  09:12AM               147439 gpedit.msc
07-16-16  09:12AM               674816 gpprefcl.dll
07-16-16  09:12AM                39936 gpprnext.dll
07-16-16  09:13AM               218624 gpresult.exe
07-16-16  09:12AM                50688 gpscript.dll
07-16-16  09:12AM                45056 gpscript.exe
11-20-16  09:59PM              1227264 gpsvc.dll
07-16-16  09:13AM                25600 gptext.dll
07-16-16  09:13AM                29696 gpupdate.exe
07-16-16  09:18AM       <DIR>          GroupPolicy
07-16-16  09:18AM       <DIR>          GroupPolicyUsers
11-20-16  09:59PM               434528 hal.dll
07-16-16  09:09AM                20504 HalExtIntcLpioDMA.dll
07-16-16  09:09AM                17944 HalExtPL080.dll
07-16-16  09:09AM                81920 hbaapi.dll
07-16-16  09:18AM       <DIR>          he-IL
07-16-16  09:13AM                11264 help.exe
07-16-16  09:13AM                34816 hid.dll
07-16-16  09:12AM                36864 hidserv.dll
07-16-16  09:09AM                14336 HOSTNAME.EXE
07-16-16  09:18AM       <DIR>          hr-HR
07-16-16  09:09AM                30720 httpapi.dll
07-16-16  09:12AM                18944 httpprxc.dll
07-16-16  09:12AM               125952 httpprxm.dll
07-16-16  09:12AM                19456 httpprxp.dll
07-16-16  09:18AM       <DIR>          hu-HU
11-20-16  09:59PM               988512 hvax64.exe
07-16-16  09:11AM                67584 hvhostsvc.dll
11-20-16  09:59PM              1100128 hvix64.exe
11-20-16  09:59PM               947552 hvloader.efi
11-20-16  09:59PM               811872 hvloader.exe
07-16-16  09:11AM                45228 hypervisor.mof
07-16-16  09:09AM                37376 icacls.exe
07-16-16  09:10AM               116064 icfupgd.dll
07-16-16  09:12AM               247808 icm32.dll
07-16-16  09:09AM                 3072 icmp.dll
07-16-16  09:12AM                18432 icsunattend.exe
11-20-16  09:59PM               305152 icsvc.dll
11-20-16  09:59PM               349696 icsvcext.dll
07-16-16  09:18AM       <DIR>          icsxml
07-16-16  09:13AM                10240 idndl.dll
11-20-16  09:59PM              2750936 iertutil.dll
07-16-16  09:09AM                32256 ifmon.dll
07-16-16  09:09AM               227680 ifsutil.dll
07-16-16  09:13AM                15872 ifsutilx.dll
02-25-19  08:07AM                19456 iisreset.exe
02-25-19  08:07AM                13312 iisrstap.dll
02-25-19  08:07AM               203776 iisRtl.dll
07-16-16  09:13AM               932352 IKEEXT.DLL
07-16-16  09:09AM               104336 imagehlp.dll
07-16-16  09:12AM             26217472 imageres.dll
07-16-16  09:18AM       <DIR>          IME
07-16-16  09:12AM               175672 imm32.dll
07-16-16  09:13AM               127488 ImplatSetup.dll
07-16-16  09:09AM                66560 inetmib1.dll
02-25-19  10:15PM       <DIR>          inetsrv
11-20-16  09:59PM               322912 input.dll
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:12AM               352768 InputSwitch.dll
07-16-16  09:12AM               467968 intl.cpl
07-16-16  09:13AM                 2560 iologmsg.dll
07-16-16  09:14AM              2158592 ipamapi.dll
07-16-16  09:09AM                34816 ipconfig.exe
07-16-16  09:09AM               219040 IPHLPAPI.DLL
11-20-16  09:59PM               945664 iphlpsvc.dll
07-16-16  09:18AM       <DIR>          Ipmi
11-20-16  09:59PM               541696 ipnathlp.dll
07-16-16  09:12AM                11264 iprtprio.dll
07-16-16  09:12AM               556544 iprtrmgr.dll
07-16-16  09:12AM               391168 IPSECSVC.DLL
07-16-16  09:12AM               155136 iscsicli.exe
07-16-16  09:12AM               229376 iscsicpl.dll
07-16-16  09:12AM               122368 iscsicpl.exe
07-16-16  09:12AM                75264 iscsidsc.dll
07-16-16  09:12AM                12288 iscsied.dll
07-16-16  09:12AM               151552 iscsiexe.dll
07-16-16  09:09AM                16896 iscsilog.dll
07-16-16  09:12AM                35328 iscsium.dll
11-20-16  09:59PM                78336 iscsiwmi.dll
07-16-16  09:12AM               130048 iscsiwmiv2.dll
07-16-16  09:18AM       <DIR>          it-IT
07-16-16  09:11AM                22232 iumbase.dll
07-16-16  09:13AM                67168 iumcrypt.dll
07-16-16  09:11AM                15064 iumdll.dll
07-16-16  09:18AM       <DIR>          ja-JP
07-16-16  09:10AM                52736 joinproviderol.dll
07-16-16  09:10AM               102912 joinutil.dll
07-16-16  09:12AM               207872 JpnServiceDS.dll
07-16-16  09:12AM               799232 jscript.dll
11-20-16  09:59PM                52224 jsproxy.dll
07-16-16  09:13AM                 8192 kbd101.dll
07-16-16  09:13AM                 7680 kbd101a.dll
07-16-16  09:13AM                 7680 kbd101b.dll
07-16-16  09:13AM                 7680 kbd101c.dll
07-16-16  09:13AM                 7680 kbd103.dll
07-16-16  09:13AM                 8192 kbd106.dll
07-16-16  09:13AM                 8192 kbd106n.dll
07-16-16  09:13AM                 7680 KBDA1.DLL
07-16-16  09:13AM                 7680 KBDA2.DLL
07-16-16  09:13AM                 7680 KBDA3.DLL
07-16-16  09:13AM                 8704 KBDAL.DLL
07-16-16  09:13AM                 7168 KBDARME.DLL
07-16-16  09:13AM                 7680 kbdarmph.dll
07-16-16  09:13AM                 7680 kbdarmty.dll
07-16-16  09:13AM                 7168 KBDARMW.DLL
07-16-16  09:13AM                 8192 kbdax2.dll
07-16-16  09:13AM                 7680 KBDAZE.DLL
07-16-16  09:13AM                 7680 KBDAZEL.DLL
07-16-16  09:13AM                 7680 KBDAZST.DLL
07-16-16  09:13AM                 7680 KBDBASH.DLL
07-16-16  09:13AM                 8192 KBDBE.DLL
07-16-16  09:13AM                 8192 KBDBENE.DLL
07-16-16  09:13AM                 7680 KBDBGPH.DLL
07-16-16  09:13AM                 7680 KBDBGPH1.DLL
07-16-16  09:13AM                 7680 KBDBHC.DLL
07-16-16  09:13AM                 7680 KBDBLR.DLL
07-16-16  09:13AM                 8192 KBDBR.DLL
07-16-16  09:13AM                 7680 KBDBU.DLL
07-16-16  09:13AM                 7680 KBDBUG.DLL
07-16-16  09:13AM                 7680 KBDBULG.DLL
07-16-16  09:13AM                 8192 KBDCA.DLL
07-16-16  09:13AM                 9216 KBDCAN.DLL
07-16-16  09:13AM                 7680 KBDCHER.DLL
07-16-16  09:13AM                17408 KBDCHERP.DLL
07-16-16  09:13AM                 8704 KBDCR.DLL
07-16-16  09:13AM                 8704 KBDCZ.DLL
07-16-16  09:13AM                 8704 KBDCZ1.DLL
07-16-16  09:13AM                 8704 KBDCZ2.DLL
07-16-16  09:13AM                 8192 KBDDA.DLL
07-16-16  09:13AM                 7680 KBDDIV1.DLL
07-16-16  09:13AM                 7680 KBDDIV2.DLL
07-16-16  09:13AM                 7168 KBDDV.DLL
07-16-16  09:13AM                 8192 KBDES.DLL
07-16-16  09:13AM                 8192 KBDEST.DLL
07-16-16  09:13AM                 7680 KBDFA.DLL
07-16-16  09:13AM                 7680 kbdfar.dll
07-16-16  09:13AM                 8192 KBDFC.DLL
07-16-16  09:13AM                 8192 KBDFI.DLL
07-16-16  09:13AM                 8704 KBDFI1.DLL
07-16-16  09:13AM                 8192 KBDFO.DLL
07-16-16  09:13AM                 8192 KBDFR.DLL
07-16-16  09:13AM                 7680 KBDFTHRK.DLL
07-16-16  09:13AM                 7680 KBDGAE.DLL
07-16-16  09:13AM                 7168 KBDGEO.DLL
07-16-16  09:13AM                 7680 kbdgeoer.dll
07-16-16  09:13AM                 7680 kbdgeome.dll
07-16-16  09:13AM                 7680 kbdgeooa.dll
07-16-16  09:13AM                 7680 kbdgeoqw.dll
07-16-16  09:13AM                 8192 KBDGKL.DLL
07-16-16  09:13AM                 8704 KBDGN.DLL
07-16-16  09:13AM                 8192 KBDGR.DLL
07-16-16  09:13AM                 8192 KBDGR1.DLL
07-16-16  09:13AM                 8704 KBDGRLND.DLL
07-16-16  09:13AM                 7680 KBDGTHC.DLL
07-16-16  09:13AM                 7680 KBDHAU.DLL
07-16-16  09:13AM                 7680 KBDHAW.DLL
07-16-16  09:13AM                 7680 KBDHE.DLL
07-16-16  09:13AM                 8192 KBDHE220.DLL
07-16-16  09:13AM                 7680 KBDHE319.DLL
07-16-16  09:13AM                 7680 KBDHEB.DLL
07-16-16  09:13AM                 7680 kbdhebl3.dll
07-16-16  09:13AM                 8192 KBDHELA2.DLL
07-16-16  09:13AM                 8192 KBDHELA3.DLL
07-16-16  09:13AM                10240 KBDHEPT.DLL
07-16-16  09:13AM                 8704 KBDHU.DLL
07-16-16  09:13AM                 7680 KBDHU1.DLL
07-16-16  09:13AM                 8192 kbdibm02.dll
07-16-16  09:13AM                 8704 KBDIBO.DLL
07-16-16  09:13AM                 7680 KBDIC.DLL
07-16-16  09:13AM                 7680 KBDINASA.DLL
07-16-16  09:13AM                 7680 KBDINBE1.DLL
07-16-16  09:13AM                 7680 KBDINBE2.DLL
07-16-16  09:13AM                 8192 KBDINBEN.DLL
07-16-16  09:13AM                 7680 KBDINDEV.DLL
07-16-16  09:13AM                 9216 KBDINEN.DLL
07-16-16  09:13AM                 7680 KBDINGUJ.DLL
07-16-16  09:13AM                 7680 KBDINHIN.DLL
07-16-16  09:13AM                 7680 KBDINKAN.DLL
07-16-16  09:13AM                 8192 KBDINMAL.DLL
07-16-16  09:13AM                 7680 KBDINMAR.DLL
07-16-16  09:13AM                 8192 KBDINORI.DLL
07-16-16  09:13AM                 7680 KBDINPUN.DLL
07-16-16  09:13AM                 7680 KBDINTAM.DLL
07-16-16  09:13AM                 7680 KBDINTEL.DLL
07-16-16  09:13AM                 8704 KBDINUK2.DLL
07-16-16  09:13AM                 7168 KBDIR.DLL
07-16-16  09:13AM                 7680 KBDIT.DLL
07-16-16  09:13AM                 7680 KBDIT142.DLL
07-16-16  09:13AM                 8192 KBDIULAT.DLL
07-16-16  09:13AM                 7680 KBDJAV.DLL
07-16-16  09:13AM                16384 KBDJPN.DLL
07-16-16  09:13AM                 7680 KBDKAZ.DLL
07-16-16  09:13AM                 7680 KBDKHMR.DLL
07-16-16  09:13AM                 7680 KBDKNI.DLL
07-16-16  09:13AM                15872 KBDKOR.DLL
07-16-16  09:13AM                 7680 KBDKURD.DLL
07-16-16  09:13AM                 7680 KBDKYR.DLL
07-16-16  09:13AM                 8192 KBDLA.DLL
07-16-16  09:13AM                 7680 KBDLAO.DLL
07-16-16  09:13AM                 7680 kbdlisub.dll
07-16-16  09:13AM                 7680 kbdlisus.dll
07-16-16  09:13AM                 8704 kbdlk41a.dll
07-16-16  09:13AM                 7680 KBDLT.DLL
07-16-16  09:13AM                 7680 KBDLT1.DLL
07-16-16  09:13AM                 7680 KBDLT2.DLL
07-16-16  09:13AM                 8192 KBDLV.DLL
07-16-16  09:13AM                 8192 KBDLV1.DLL
07-16-16  09:13AM                 9216 KBDLVST.DLL
07-16-16  09:13AM                 7680 KBDMAC.DLL
07-16-16  09:13AM                 7680 KBDMACST.DLL
07-16-16  09:13AM                 7680 KBDMAORI.DLL
07-16-16  09:13AM                 7680 KBDMLT47.DLL
07-16-16  09:13AM                 7680 KBDMLT48.DLL
07-16-16  09:13AM                 7680 KBDMON.DLL
07-16-16  09:13AM                 7680 KBDMONMO.DLL
07-16-16  09:13AM                 7680 KBDMONST.DLL
07-16-16  09:13AM                 7680 KBDMYAN.DLL
07-16-16  09:13AM                 7680 KBDNE.DLL
07-16-16  09:13AM                 8704 kbdnec.dll
07-16-16  09:13AM                 8704 kbdnec95.dll
07-16-16  09:13AM                10752 kbdnecat.dll
07-16-16  09:13AM                 9216 kbdnecnt.dll
07-16-16  09:13AM                 8192 KBDNEPR.DLL
07-16-16  09:13AM                 7680 kbdnko.dll
07-16-16  09:13AM                 8192 KBDNO.DLL
07-16-16  09:13AM                 8704 KBDNO1.DLL
07-16-16  09:13AM                 8704 KBDNSO.DLL
07-16-16  09:13AM                 7680 KBDNTL.DLL
07-16-16  09:13AM                 7680 KBDOGHAM.DLL
07-16-16  09:13AM                 7680 KBDOLCH.DLL
07-16-16  09:13AM                 7680 KBDOLDIT.DLL
07-16-16  09:13AM                 7680 KBDOSM.DLL
07-16-16  09:13AM                 7680 KBDPASH.DLL
07-16-16  09:13AM                 7680 kbdphags.dll
07-16-16  09:13AM                 8704 KBDPL.DLL
07-16-16  09:13AM                 7680 KBDPL1.DLL
07-16-16  09:13AM                 8192 KBDPO.DLL
07-16-16  09:13AM                 8704 KBDRO.DLL
07-16-16  09:13AM                 9216 KBDROPR.DLL
07-16-16  09:13AM                 9216 KBDROST.DLL
07-16-16  09:13AM                 7680 KBDRU.DLL
07-16-16  09:13AM                 7680 KBDRU1.DLL
07-16-16  09:13AM                 9216 KBDRUM.DLL
07-16-16  09:13AM                 8192 KBDSF.DLL
07-16-16  09:13AM                 8704 KBDSG.DLL
07-16-16  09:13AM                 8704 KBDSL.DLL
07-16-16  09:13AM                 8704 KBDSL1.DLL
07-16-16  09:13AM                 9216 KBDSMSFI.DLL
07-16-16  09:13AM                 9216 KBDSMSNO.DLL
07-16-16  09:13AM                 7680 KBDSN1.DLL
07-16-16  09:13AM                 8192 KBDSORA.DLL
07-16-16  09:13AM                 8704 KBDSOREX.DLL
07-16-16  09:13AM                 8192 KBDSORS1.DLL
07-16-16  09:13AM                 8704 KBDSORST.DLL
07-16-16  09:13AM                 8192 KBDSP.DLL
07-16-16  09:13AM                 8192 KBDSW.DLL
07-16-16  09:13AM                 8192 KBDSW09.DLL
07-16-16  09:13AM                 7680 KBDSYR1.DLL
07-16-16  09:13AM                 7680 KBDSYR2.DLL
07-16-16  09:13AM                 7680 KBDTAILE.DLL
07-16-16  09:13AM                 7680 KBDTAJIK.DLL
07-16-16  09:13AM                 7680 KBDTAT.DLL
07-16-16  09:13AM                 7680 KBDTH0.DLL
07-16-16  09:13AM                 7680 KBDTH1.DLL
07-16-16  09:13AM                 7680 KBDTH2.DLL
07-16-16  09:13AM                 7680 KBDTH3.DLL
07-16-16  09:13AM                 7680 KBDTIFI.DLL
07-16-16  09:13AM                 7680 KBDTIFI2.DLL
07-16-16  09:13AM                 8192 KBDTIPRC.DLL
07-16-16  09:13AM                 8704 KBDTIPRD.DLL
07-16-16  09:13AM                 7680 KBDTT102.DLL
07-16-16  09:13AM                 8704 KBDTUF.DLL
07-16-16  09:13AM                 8192 KBDTUQ.DLL
07-16-16  09:13AM                 7680 KBDTURME.DLL
07-16-16  09:13AM                 8192 KBDTZM.DLL
07-16-16  09:13AM                 7680 KBDUGHR.DLL
07-16-16  09:13AM                 7680 KBDUGHR1.DLL
07-16-16  09:13AM                 7168 KBDUK.DLL
07-16-16  09:13AM                 8704 KBDUKX.DLL
07-16-16  09:13AM                 7680 KBDUR.DLL
07-16-16  09:13AM                 7680 KBDUR1.DLL
07-16-16  09:13AM                 7680 KBDURDU.DLL
07-16-16  09:09AM                 9216 KBDUS.DLL
07-16-16  09:13AM                 7680 KBDUSA.DLL
07-16-16  09:13AM                 7680 KBDUSL.DLL
07-16-16  09:13AM                 7680 KBDUSR.DLL
07-16-16  09:13AM                 8192 KBDUSX.DLL
07-16-16  09:13AM                 7680 KBDUZB.DLL
07-16-16  09:13AM                 7680 KBDVNTC.DLL
07-16-16  09:13AM                 8192 KBDWOL.DLL
07-16-16  09:13AM                 7680 KBDYAK.DLL
07-16-16  09:13AM                 8192 KBDYBA.DLL
07-16-16  09:13AM                 7680 KBDYCC.DLL
07-16-16  09:13AM                 9216 KBDYCL.DLL
07-16-16  09:09AM                15712 kd.dll
07-16-16  09:09AM                24920 kd1394.dll
07-16-16  09:09AM                31072 kdcom.dll
07-16-16  09:11AM                20320 kdhv1394.dll
11-20-16  09:59PM                20320 kdhvcom.dll
07-16-16  09:09AM               111968 kdnet.dll
07-16-16  09:09AM                16736 kdnet_uart16550.dll
07-16-16  09:09AM                82432 KdsCli.dll
07-16-16  09:09AM                22368 kdstub.dll
07-16-16  09:09AM                44896 kdusb.dll
07-16-16  09:09AM                29536 kd_02_10df.dll
07-16-16  09:09AM               325984 kd_02_10ec.dll
07-16-16  09:09AM                25440 kd_02_1137.dll
07-16-16  09:09AM               212312 kd_02_14e4.dll
07-16-16  09:09AM                42848 kd_02_15b3.dll
07-16-16  09:09AM                39264 kd_02_1969.dll
07-16-16  09:09AM                29536 kd_02_19a2.dll
07-16-16  09:09AM               228192 kd_02_8086.dll
07-16-16  09:09AM                17760 kd_07_1415.dll
07-16-16  09:09AM                37728 kd_0C_8086.dll
07-16-16  09:09AM               154488 KerbClientShared.dll
11-20-16  09:59PM               932864 kerberos.dll
07-16-16  09:10AM                48608 kernel.appcore.dll
07-16-16  09:13AM               699880 kernel32.dll
07-16-16  09:09AM               277880 kernel32legacy.dll
11-20-16  09:59PM              2213248 KernelBase.dll
07-16-16  09:09AM               235008 KernelTraceControl.dll
07-16-16  09:09AM                96768 keyiso.dll
07-16-16  09:13AM                37376 klist.exe
07-16-16  09:12AM                48128 kmddsp.tsp
07-16-16  09:18AM       <DIR>          ko-KR
11-20-16  10:10PM               183808 korwbrkr.dll
11-20-16  10:10PM             12023100 korwbrkr.lex
07-16-16  09:13AM               177152 kpssvc.dll
07-16-16  09:13AM                37888 ksetup.exe
07-16-16  09:13AM                17408 ktmutil.exe
07-16-16  09:09AM                24064 ktmw32.dll
07-16-16  09:13AM                47104 ktpass.exe
07-16-16  09:12AM                62976 l2nacp.dll
07-16-16  09:13AM                16896 label.exe
07-16-16  09:12AM                15872 LangCleanupSysprepAction.dll
07-16-16  09:13AM               184320 LaunchTM.exe
07-16-16  09:15AM               211938 lcphrase.tbl
07-16-16  09:15AM                24114 lcptr.tbl
02-03-19  08:05AM                50098 license.rtf
07-16-16  09:18AM       <DIR>          Licenses
07-16-16  09:13AM                70656 licensingdiag.exe
07-16-16  09:13AM               181760 LicensingDiagSpp.dll
07-16-16  09:13AM                44032 linkinfo.dll
07-16-16  09:13AM                48128 lltdapi.dll
07-16-16  09:13AM                 2560 lltdres.dll
07-16-16  09:13AM               275456 lltdsvc.dll
07-16-16  09:09AM                27136 lmhsvc.dll
07-16-16  09:10AM               122880 loadperf.dll
11-20-16  09:59PM               788624 locale.nls
11-20-16  09:59PM              1130496 localspl.dll
07-16-16  09:12AM                18944 localui.dll
07-16-16  09:10AM                51200 lodctr.exe
05-16-25  08:28AM       <DIR>          LogFiles
07-16-16  09:12AM               116224 logman.exe
07-16-16  09:12AM                23552 logoff.exe
07-16-16  09:09AM               246872 logoncli.dll
11-20-16  09:59PM               717824 LogonController.dll
07-16-16  09:13AM                13312 LogonUI.exe
07-16-16  09:12AM                 3072 lpk.dll
07-16-16  09:12AM               777216 lpksetup.exe
07-16-16  09:12AM                 9728 lpksetupproxyserv.dll
07-16-16  09:12AM                68096 lpremove.exe
11-20-16  09:59PM               218008 LsaIso.exe
11-20-16  09:59PM              1490944 lsasrv.dll
11-20-16  09:59PM                57400 lsass.exe
07-16-16  09:12AM                62464 LSCSHostPolicy.dll
11-20-16  09:59PM               691712 lsm.dll
07-16-16  09:12AM                44544 lsmproxy.dll
07-16-16  09:12AM                26624 lstelemetry.dll
07-16-16  09:18AM       <DIR>          lt-LT
07-16-16  09:13AM                51712 luainstall.dll
07-16-16  09:18AM       <DIR>          lv-LV
07-16-16  09:13AM                 3072 lz32.dll
07-16-16  09:09AM                 9926 l_intl.nls
02-25-19  10:56PM                    0 ma-log4cpp.log
02-25-19  10:56PM                    0 ma-log4cpp_rolling.log
07-16-16  09:12AM                75264 MaintenanceUI.dll
07-16-16  09:13AM                85504 makecab.exe
07-16-16  09:13AM               352256 mcbuilder.exe
07-16-16  09:13AM                80224 mcupdate_AuthenticAMD.dll
07-16-16  09:13AM               541024 mcupdate_GenuineIntel.dll
07-16-16  09:12AM                57344 mf3216.dll
07-16-16  09:12AM              1415168 mfc42.dll
07-16-16  09:12AM              1433088 mfc42u.dll
07-16-16  09:13AM                35840 mfcsubs.dll
07-16-16  09:12AM                23040 mgmtapi.dll
07-16-16  09:09AM               113664 mi.dll
07-16-16  09:10AM                90624 mibincodec.dll
11-20-16  10:16PM       <DIR>          Microsoft
07-16-16  09:10AM                12288 microsoft-windows-battery-events.dll
07-16-16  09:10AM                 6656 microsoft-windows-hal-events.dll
07-16-16  09:10AM                40448 microsoft-windows-kernel-pnp-events.dll
07-16-16  09:10AM               194048 microsoft-windows-kernel-power-events.dll
07-16-16  09:10AM                96256 microsoft-windows-kernel-processor-power-events.dll
07-16-16  09:10AM                62976 microsoft-windows-pdc.dll
07-16-16  09:10AM                 4096 microsoft-windows-processor-aggregator-events.dll
07-16-16  09:13AM                 6144 microsoft-windows-sleepstudy-events.dll
07-16-16  09:13AM                 6144 microsoft-windows-storage-tiering-events.dll
11-20-16  09:59PM               327168 microsoft-windows-system-events.dll
07-16-16  09:15AM                17920 Microsoft.Management.Infrastructure.Native.Unmanaged.dll
11-20-16  09:59PM                46592 Microsoft.NetworkController.SDNDiagnosticsTask.dll
07-16-16  09:14AM               279552 Microsoft.Windows.DeploymentServices.ServerManager.Plugin.dll
07-16-16  09:14AM               183296 Microsoft.Windows.ServerManager.DhcpServer.Plugin.dll
11-20-16  09:59PM                39936 Microsoft.Windows.ServerManager.NetworkController.Plugin.dll
07-16-16  09:14AM               336384 Microsoft.Windows.ServerManager.NPASRole.Plugin.dll
07-16-16  09:14AM              5537792 Microsoft.Windows.ServerManager.Plugins.Ipam.dll
07-16-16  09:13AM               142176 migisol.dll
02-25-19  08:07AM       <DIR>          migration
07-16-16  09:18AM       <DIR>          migwiz
07-16-16  09:12AM                38912 mimefilt.dll
07-16-16  09:10AM               157184 mimofcodec.dll
07-16-16  09:13AM                12288 MinstoreEvents.dll
07-16-16  09:09AM               321024 mintdh.dll
11-20-16  09:59PM              3287552 mispace.dll
07-16-16  09:18AM       <DIR>          mistreams
07-16-16  09:09AM               226816 miutils.dll
07-16-16  09:13AM               673088 mlang.dat
07-16-16  09:13AM               239616 mlang.dll
11-20-16  10:09PM              3054080 MLS1.dll
11-20-16  10:09PM              1915392 MLS2.dll
11-20-16  10:10PM              1747456 MLS3.dll
11-20-16  10:10PM              4435968 MLS6.dll
11-20-16  10:10PM              2295296 MLS7.dll
07-16-16  09:12AM               443744 MMDevAPI.dll
07-16-16  09:13AM                31744 mode.com
07-16-16  09:09AM                27648 more.com
07-16-16  09:09AM                17408 mountvol.exe
07-16-16  09:15AM               235008 mpeval.dll
07-16-16  09:13AM                19456 mpnotify.exe
07-16-16  09:09AM               101264 mpr.dll
11-20-16  09:59PM               512000 mprapi.dll
11-20-16  09:59PM               496128 mprdim.dll
07-16-16  09:12AM                13824 mprext.dll
07-16-16  09:12AM               115200 mprmsg.dll
12-10-18  06:04PM               592616 MpSigStub.exe
07-16-16  09:10AM               893952 MPSSVC.dll
07-16-16  09:15AM               489984 mpunits.dll
07-16-16  09:09AM                16384 MRINFO.EXE
07-16-16  09:10AM              1069208 MrmCoreR.dll
07-16-16  09:12AM                 3072 msafd.dll
07-16-16  09:09AM                59416 msasn1.dll
07-16-16  09:09AM               155136 msaudite.dll
07-16-16  09:12AM               300544 mscandui.dll
07-16-16  09:13AM                11776 mscat32.dll
07-16-16  09:12AM                82944 MSchedExe.exe
07-16-16  09:16AM               231424 msclmd.dll
07-16-16  09:12AM               576512 mscms.dll
07-16-16  09:10AM               387072 mscoree.dll
07-16-16  09:10AM                19968 mscorier.dll
07-16-16  09:10AM                73880 mscories.dll
11-20-16  09:59PM              1418312 msctf.dll
07-16-16  09:12AM                10240 msctfime.ime
07-16-16  09:12AM                32256 MsCtfMonitor.dll
07-16-16  09:12AM               217600 msctfp.dll
07-16-16  09:12AM               116224 msctfui.dll
07-16-16  09:12AM               882688 msctfuimanager.dll
07-16-16  09:12AM               134144 msdart.dll
07-16-16  09:12AM                 5120 msdatsrc.tlb
07-16-16  09:13AM               506368 msdelta.dll
07-16-16  09:18AM       <DIR>          MSDRM
07-16-16  09:13AM               565760 msdrm.dll
07-16-16  09:18AM       <DIR>          MsDtc
07-16-16  09:13AM               147456 msdtc.exe
07-16-16  09:13AM               376320 msdtckrm.dll
07-16-16  09:13AM               127488 msdtclog.dll
07-16-16  09:13AM               871424 msdtcprx.dll
11-20-16  09:59PM              1589248 msdtctm.dll
07-16-16  09:13AM               306176 msdtcuiu.dll
07-16-16  09:13AM                22528 msdtcVSp1res.dll
11-20-16  09:59PM              3202048 msftedit.dll
07-16-16  09:12AM                26624 msg.exe
11-20-16  09:59PM              3059200 msi.dll
07-16-16  09:12AM                65024 msiexec.exe
07-16-16  09:12AM               393216 msihnd.dll
07-16-16  09:12AM                20992 msiltcfg.dll
07-16-16  09:12AM                 8192 msimg32.dll
07-16-16  09:12AM                25600 msimsg.dll
07-16-16  09:12AM                46080 msimtf.dll
11-20-16  09:59PM               369664 msinfo32.exe
07-16-16  09:12AM                30208 msisip.dll
07-16-16  09:13AM                62976 mskeyprotect.dll
07-16-16  09:12AM               214016 msls31.dll
07-16-16  09:09AM                62976 msobjs.dll
07-16-16  09:13AM                45568 mspatcha.dll
07-16-16  09:13AM                83456 mspatchc.dll
07-16-16  09:12AM                54784 msports.dll
07-16-16  09:09AM                 2560 msprivs.dll
07-16-16  09:13AM                73728 mssign32.dll
07-16-16  09:13AM               245248 mstask.dll
07-16-16  09:12AM               464896 msutb.dll
11-20-16  09:59PM               405856 msv1_0.dll
07-16-16  09:09AM                83456 msvcirt.dll
07-16-16  09:09AM               588824 msvcp110_win.dll
07-16-16  09:14AM               690016 msvcp120_clr0400.dll
07-16-16  09:09AM               603648 msvcp60.dll
07-16-16  09:09AM               633216 msvcp_win.dll
07-16-16  09:14AM                18600 msvcr100_clr0400.dll
07-16-16  09:14AM               993632 msvcr120_clr0400.dll
07-16-16  09:09AM               634824 msvcrt.dll
11-20-16  10:10PM               717824 MSWB70011.dll
11-20-16  10:11PM               717824 MSWB7001E.dll
11-20-16  10:11PM               717824 MSWB70404.dll
11-20-16  10:11PM               717824 MSWB70804.dll
07-16-16  09:09AM               357216 mswsock.dll
07-16-16  09:12AM              1827840 msxml3.dll
07-16-16  09:12AM                 2560 msxml3r.dll
11-20-16  09:59PM              2446696 msxml6.dll
11-20-16  09:59PM                 2560 msxml6r.dll
07-16-16  09:12AM               233984 MTF.dll
07-16-16  09:12AM               265216 MTFServer.dll
07-16-16  09:13AM               403456 mtxclu.dll
07-16-16  09:13AM                30720 mtxdm.dll
07-16-16  09:13AM                 9728 mtxex.dll
07-16-16  09:13AM               147456 mtxoci.dll
07-16-16  09:18AM       <DIR>          MUI
07-16-16  09:12AM                18432 muifontsetup.dll
07-16-16  09:12AM                16384 MUILanguageCleanup.dll
07-16-16  09:09AM                76800 MuiUnattend.exe
07-16-16  09:13AM                52224 musdialoghandlers.dll
11-20-16  09:59PM               186880 MusNotification.exe
07-16-16  09:13AM                76288 MusNotificationUx.exe
11-20-16  09:59PM               523776 MusUpdateHandlers.dll
07-16-16  09:14AM                21504 MuxInst.dll
07-16-16  09:12AM                67584 NapiNSP.dll
07-16-16  09:18AM       <DIR>          nb-NO
07-16-16  09:12AM                21504 nbtstat.exe
07-16-16  09:12AM                25600 NcaApi.dll
07-16-16  09:12AM               167936 NcaSvc.dll
07-16-16  09:13AM                44032 nci.dll
07-16-16  09:09AM                69120 ncobjapi.dll
07-16-16  09:09AM               142616 ncrypt.dll
07-16-16  09:09AM               323072 ncryptprov.dll
07-16-16  09:09AM               118816 ncryptsslp.dll
11-20-16  09:59PM               396800 ncsi.dll
07-16-16  09:13AM                65536 ndadmin.exe
07-16-16  09:18AM       <DIR>          NDF
07-16-16  09:12AM               305664 ndfapi.dll
07-16-16  09:12AM                44544 ndfetw.dll
07-16-16  09:12AM                  565 NdfEventView.xml
07-16-16  09:12AM               115712 ndfhcdiscovery.dll
07-16-16  09:12AM                95232 ndishc.dll
07-16-16  09:12AM                32768 ndproxystub.dll
07-16-16  09:13AM               120832 negoexts.dll
07-16-16  09:09AM                55808 net.exe
07-16-16  09:09AM               175616 net1.exe
07-16-16  09:09AM                81184 netapi32.dll
07-16-16  09:13AM                18944 netbios.dll
07-16-16  09:12AM                25600 netbtugc.exe
07-16-16  09:13AM                33792 netcfg.exe
07-16-16  09:13AM                86016 NetCfgNotifyObjectHost.exe
07-16-16  09:12AM               432992 netcfgx.dll
07-16-16  09:12AM               302592 netdiagfx.dll
07-16-16  09:13AM                86016 netdom.exe
07-16-16  09:09AM                20480 netevent.dll
07-16-16  09:09AM                46592 NetEvtFwdr.exe
07-16-16  09:10AM                41472 netfxperf.dll
07-16-16  09:09AM                 2560 neth.dll
07-16-16  09:09AM               205312 netiohlp.dll
11-20-16  09:59PM                30208 netiougc.exe
07-16-16  09:13AM               163328 netjoin.dll
07-16-16  09:09AM               827392 netlogon.dll
07-16-16  09:09AM                 2560 netmsg.dll
07-16-16  09:13AM               203264 netprofm.dll
07-16-16  09:13AM               519168 netprofmsvc.dll
07-16-16  09:10AM                63488 netprovfw.dll
07-16-16  09:13AM                70656 netprovisionsp.dll
11-20-16  09:59PM               148832 NetSetupApi.dll
11-20-16  09:59PM               848736 NetSetupEngine.dll
07-16-16  09:13AM               489472 NetSetupShim.dll
11-20-16  09:59PM               265728 NetSetupSvc.dll
07-16-16  09:09AM                92672 netsh.exe
07-16-16  09:09AM                38400 NETSTAT.EXE
11-20-16  09:59PM              1037312 nettrace.dll
07-16-16  09:12AM                21656 NetTrace.PLA.Diagnostics.xml
07-16-16  09:09AM                43416 netutils.dll
11-20-16  09:59PM               336896 NetworkBindingEngineMigPlugin.dll
07-16-16  09:12AM              1195008 networkexplorer.dll
07-16-16  09:12AM                54272 networkitemfactory.dll
07-16-16  09:18AM       <DIR>          networklist
07-16-16  09:13AM               514048 newdev.dll
07-16-16  09:13AM                68096 newdev.exe
07-16-16  09:12AM               362496 ninput.dll
07-16-16  09:18AM       <DIR>          nl-NL
11-20-16  10:10PM              7417344 NL7Data0011.dll
11-20-16  10:11PM               861184 NL7Data001E.dll
11-20-16  10:11PM              2352640 NL7Data0404.dll
11-20-16  10:11PM              3430912 NL7Data0804.dll
11-20-16  10:10PM              2454528 NL7Lexicons0011.dll
11-20-16  10:11PM               201216 NL7Lexicons001E.dll
11-20-16  10:11PM               360960 NL7Lexicons0404.dll
11-20-16  10:11PM               409600 NL7Lexicons0804.dll
11-20-16  10:10PM              7702016 NL7Models0011.dll
11-20-16  10:11PM              1118208 NL7Models001E.dll
11-20-16  10:11PM              9720320 NL7Models0404.dll
11-20-16  10:11PM              2963968 NL7Models0804.dll
07-16-16  09:13AM                80896 nlaapi.dll
11-20-16  09:59PM               368640 nlasvc.dll
07-16-16  09:12AM               190464 nlhtml.dll
07-16-16  09:13AM                29184 nlmproxy.dll
07-16-16  09:13AM                17408 nlmsprep.dll
07-16-16  09:13AM                88928 nlsbres.dll
11-20-16  10:09PM               170496 NlsData0002.dll
11-20-16  10:09PM               170496 NlsData0003.dll
11-20-16  10:09PM              2083328 NlsData0007.dll
11-20-16  10:09PM              6354944 NlsData0009.dll
11-20-16  10:09PM              9681920 NlsData000a.dll
11-20-16  10:10PM              2359296 NlsData000c.dll
11-20-16  10:10PM               170496 NlsData000d.dll
11-20-16  10:10PM               170496 NlsData000f.dll
11-20-16  10:10PM               170496 NlsData0010.dll
11-20-16  10:11PM               170496 NlsData0018.dll
11-20-16  10:10PM               170496 NlsData001a.dll
11-20-16  10:11PM               170496 NlsData001b.dll
11-20-16  10:11PM               170496 NlsData001d.dll
11-20-16  10:11PM               169984 NlsData0020.dll
11-20-16  10:10PM               170496 NlsData0021.dll
11-20-16  10:11PM               170496 NlsData0022.dll
11-20-16  10:11PM               170496 NlsData0024.dll
11-20-16  10:10PM               170496 NlsData0026.dll
11-20-16  10:10PM               171520 NlsData0027.dll
11-20-16  10:11PM               170496 NlsData002a.dll
11-20-16  10:10PM               170496 NlsData0039.dll
11-20-16  10:10PM               170496 NlsData003e.dll
11-20-16  10:09PM               170496 NlsData0045.dll
11-20-16  10:11PM               170496 NlsData0046.dll
11-20-16  10:10PM               170496 NlsData0047.dll
11-20-16  10:11PM               170496 NlsData0049.dll
11-20-16  10:11PM               170496 NlsData004a.dll
11-20-16  10:10PM               170496 NlsData004b.dll
11-20-16  10:10PM               170496 NlsData004c.dll
11-20-16  10:10PM               170496 NlsData004e.dll
11-20-16  10:10PM               170496 NlsData0414.dll
11-20-16  10:11PM               170496 NlsData0416.dll
11-20-16  10:11PM               170496 NlsData0816.dll
11-20-16  10:11PM               170496 NlsData081a.dll
07-16-16  09:13AM                10240 Nlsdl.dll
11-20-16  10:09PM              4164608 NlsLexicons0002.dll
11-20-16  10:09PM              1453056 NlsLexicons0003.dll
11-20-16  10:09PM             12039168 NlsLexicons0007.dll
11-20-16  10:09PM              2629120 NlsLexicons0009.dll
11-20-16  10:09PM              9893376 NlsLexicons000a.dll
11-20-16  10:10PM              6238208 NlsLexicons000c.dll
11-20-16  10:10PM              1722880 NlsLexicons000d.dll
11-20-16  10:10PM              5655040 NlsLexicons000f.dll
11-20-16  10:10PM              4176384 NlsLexicons0010.dll
11-20-16  10:11PM              3331584 NlsLexicons0018.dll
11-20-16  10:10PM              6015488 NlsLexicons001a.dll
11-20-16  10:11PM              6586368 NlsLexicons001b.dll
11-20-16  10:11PM              6346752 NlsLexicons001d.dll
11-20-16  10:11PM              1237504 NlsLexicons0020.dll
11-20-16  10:10PM              2136576 NlsLexicons0021.dll
11-20-16  10:11PM              5500416 NlsLexicons0022.dll
11-20-16  10:11PM              7965184 NlsLexicons0024.dll
11-20-16  10:10PM              5791744 NlsLexicons0026.dll
11-20-16  10:10PM              6225408 NlsLexicons0027.dll
11-20-16  10:11PM                 4608 NlsLexicons002a.dll
11-20-16  10:10PM              1782784 NlsLexicons0039.dll
11-20-16  10:10PM              4046336 NlsLexicons003e.dll
11-20-16  10:09PM              1794048 NlsLexicons0045.dll
11-20-16  10:11PM              1809408 NlsLexicons0046.dll
11-20-16  10:10PM              1411584 NlsLexicons0047.dll
11-20-16  10:11PM              1558528 NlsLexicons0049.dll
11-20-16  10:11PM              3419648 NlsLexicons004a.dll
11-20-16  10:10PM              1703424 NlsLexicons004b.dll
11-20-16  10:10PM              4093952 NlsLexicons004c.dll
11-20-16  10:10PM              1973248 NlsLexicons004e.dll
11-20-16  10:10PM              4616704 NlsLexicons0414.dll
11-20-16  10:11PM              5091328 NlsLexicons0416.dll
11-20-16  10:11PM              5032448 NlsLexicons0816.dll
11-20-16  10:11PM              7043072 NlsLexicons081a.dll
11-20-16  09:59PM               492544 nltest.exe
11-20-16  10:11PM                 1696 NOISE.CHS
11-20-16  10:11PM                 1696 NOISE.CHT
11-20-16  10:10PM                 2060 noise.jpn
11-20-16  10:11PM                  697 NOISE.THA
07-16-16  09:09AM                 6144 normaliz.dll
07-16-16  09:09AM                72286 normidna.nls
07-16-16  09:09AM                50112 normnfc.nls
07-16-16  09:09AM                43566 normnfd.nls
07-16-16  09:09AM                71824 normnfkc.nls
07-16-16  09:09AM                65698 normnfkd.nls
07-16-16  09:12AM               243200 notepad.exe
07-16-16  09:13AM                38912 npmproxy.dll
07-16-16  09:09AM                19456 nrpsrv.dll
07-16-16  09:12AM                38912 nshhttp.dll
07-16-16  09:12AM               417280 nshipsec.dll
11-20-16  09:59PM               730112 nshwfp.dll
07-16-16  09:09AM                24312 nsi.dll
07-16-16  09:09AM                30720 nsisvc.dll
07-16-16  09:13AM                86528 nslookup.exe
07-16-16  09:09AM               237072 ntasn1.dll
11-20-16  09:59PM              1883784 ntdll.dll
07-16-16  09:09AM               148480 ntdsapi.dll
07-16-16  09:10AM                70656 ntlanman.dll
07-16-16  09:09AM                38792 NtlmShared.dll
07-16-16  09:09AM               189608 ntmarta.dll
11-20-16  09:59PM              7816544 ntoskrnl.exe
07-16-16  09:13AM               353792 ntprint.dll
07-16-16  09:13AM                63488 ntprint.exe
11-20-16  09:59PM               842240 ntshrui.dll
07-16-16  09:13AM                18432 ntvdm64.dll
07-16-16  09:12AM               677376 objsel.dll
07-16-16  09:13AM               165376 ocsetapi.dll
07-16-16  09:12AM               687104 odbc32.dll
07-16-16  09:12AM                74240 odbcad32.exe
07-16-16  09:12AM                46592 odbcbcp.dll
11-20-16  09:59PM                30208 odbcconf.dll
07-16-16  09:12AM                26112 odbcconf.exe
07-16-16  09:12AM                  263 odbcconf.rsp
07-16-16  09:12AM               124416 odbccp32.dll
07-16-16  09:12AM                87552 odbccr32.dll
07-16-16  09:12AM                89600 odbccu32.dll
07-16-16  09:12AM               225280 odbcint.dll
07-16-16  09:12AM               163328 odbctrac.dll
11-20-16  09:59PM                15425 OEMDefaultAssociations.xml
07-16-16  09:13AM               282112 oemlicense.dll
07-16-16  09:12AM               271360 offfilt.dll
11-20-16  09:59PM               114688 offlinelsa.dll
11-20-16  09:59PM               237056 offlinesam.dll
11-20-16  09:59PM              1274712 ole32.dll
07-16-16  09:12AM               391168 oleacc.dll
07-16-16  09:12AM                12800 oleacchooks.dll
07-16-16  09:12AM                 4608 oleaccrc.dll
11-20-16  09:59PM               773720 oleaut32.dll
07-16-16  09:12AM               142336 oleprn.dll
07-16-16  09:09AM               311296 OneCoreCommonProxyStub.dll
07-16-16  09:13AM                  843 onlinesetup.cmd
11-20-16  09:59PM       <DIR>          oobe
07-16-16  09:12AM              2216960 OpcServices.dll
07-16-16  09:13AM                72704 openfiles.exe
07-16-16  09:13AM                92488 OpenWith.exe
07-16-16  09:13AM                26112 osbaseln.dll
07-16-16  09:13AM                 9728 osuninst.dll
07-16-16  09:15AM                87552 PackageInspector.exe
08-18-14  11:07PM               107768 Packet.dll
07-16-16  09:09AM                19456 PATHPING.EXE
07-16-16  09:13AM                64000 pautoenr.dll
07-16-16  09:12AM                  150 pcl.sep
07-16-16  09:13AM               139264 PCPKsp.dll
07-16-16  09:13AM               623104 PCPTpm12.dll
07-16-16  09:13AM               385024 pcsvDevice.dll
07-16-16  09:09AM                26920 pcwum.dll
11-20-16  09:59PM               295936 pdh.dll
07-16-16  09:12AM               724992 PeerDistCacheProvider.dll
07-16-16  09:12AM               423424 PeerDistSh.dll
05-16-25  08:24AM               193546 perfc009.dat
07-16-16  09:10AM                45568 perfctrs.dll
07-16-16  09:16AM                33362 perfd009.dat
07-16-16  09:10AM                40960 perfdisk.dll
05-16-25  08:24AM               918648 perfh009.dat
07-16-16  09:16AM               296742 perfi009.dat
07-16-16  09:10AM                25600 perfnet.dll
07-16-16  09:10AM                40960 perfos.dll
07-16-16  09:10AM                40960 perfproc.dll
05-16-25  08:24AM              1104346 PerfStringBackup.INI
11-20-16  09:59PM              1066328 pidgenx.dll
07-16-16  09:09AM                21504 PING.EXE
07-16-16  02:04AM               206848 PkgMgr.exe
07-16-16  09:13AM               238592 pku2u.dll
07-16-16  09:18AM       <DIR>          pl-PL
07-16-16  09:13AM              1457152 pla.dll
07-16-16  09:13AM                10240 plasrv.exe
07-16-16  09:13AM                15360 pnpts.dll
07-16-16  09:13AM                34304 pnpui.dll
07-16-16  09:13AM                60928 PnPUnattend.exe
07-16-16  09:13AM               228352 pnputil.exe
07-16-16  09:12AM                92160 PNPXAssoc.dll
07-16-16  09:12AM                57344 PNPXAssocPrx.dll
07-16-16  09:12AM               330240 polstore.dll
07-16-16  02:04AM               142848 poqexec.exe
11-20-16  09:59PM                90112 powercfg.exe
07-16-16  09:13AM               302592 PowerWmiProvider.dll
07-16-16  09:09AM               301680 powrprof.dll
07-16-16  09:10AM               261120 PresentationHost.exe
07-16-16  09:10AM                65536 PresentationHostProxy.dll
07-16-16  09:12AM                14336 prflbmsg.dll
07-16-16  09:13AM                16896 print.exe
07-16-16  09:12AM                30504 PrintDialogHost.exe
07-16-16  09:12AM                21504 PrintDialogHost3D.exe
07-16-16  09:12AM               583680 PrintDialogs.dll
07-16-16  09:12AM               307200 PrintDialogs3D.dll
07-16-16  09:12AM                46080 printfilterpipelineprxy.dll
07-16-16  09:12AM               864256 printfilterpipelinesvc.exe
11-20-16  09:53PM       <DIR>          Printing_Admin_Scripts
07-16-16  09:13AM                76800 PrintIsolationHost.exe
07-16-16  09:13AM                59392 PrintIsolationProxy.dll
07-16-16  09:12AM                68096 PrintPlatformConfig.dll
07-16-16  09:12AM              1184256 printui.dll
07-16-16  09:12AM                64000 printui.exe
11-20-16  10:09PM             16735744 prm0001.dll
11-20-16  10:09PM              6472704 prm0005.dll
11-20-16  10:09PM              7046144 prm0006.dll
11-20-16  10:09PM             11602432 prm0007.dll
11-20-16  10:09PM              8229888 prm0008.dll
11-20-16  10:09PM              5739008 prm0009.dll
11-20-16  10:10PM              8071168 prm000b.dll
11-20-16  10:10PM             10402816 prm000e.dll
11-20-16  10:10PM              9481728 prm0013.dll
11-20-16  10:11PM              7850496 prm0015.dll
11-20-16  10:11PM              8628736 prm0019.dll
11-20-16  10:11PM             14329344 prm001f.dll
07-16-16  09:12AM               187392 prncache.dll
07-16-16  09:12AM               481792 prnfldr.dll
07-16-16  09:12AM               254976 prnntfy.dll
07-16-16  09:12AM               157184 prntvpt.dll
07-16-16  09:09AM                69264 profapi.dll
07-16-16  09:10AM                72704 profext.dll
07-16-16  09:13AM               112128 profprov.dll
11-20-16  09:59PM               358400 profsvc.dll
07-16-16  09:13AM               142848 profsvcext.dll
07-16-16  09:10AM              1599608 propsys.dll
02-25-19  10:56PM                    0 providerFx-log4cpp.log
02-25-19  10:56PM                    0 providerFx-log4cpp_rolling.log
07-16-16  09:09AM               306688 provthrd.dll
07-16-16  09:09AM                82944 prvdmofcomp.dll
07-16-16  09:13AM                18656 psapi.dll
07-16-16  09:12AM                   51 pscript.sep
07-16-16  09:09AM                65888 PSHED.DLL
07-16-16  09:10AM                49664 PSModuleDiscoveryProvider.dll
07-16-16  09:10AM                 4148 psmodulediscoveryprovider.mof
07-16-16  09:13AM                15360 pstask.dll
07-16-16  09:13AM                15872 pstorec.dll
07-16-16  09:18AM       <DIR>          pt-BR
07-16-16  09:18AM       <DIR>          pt-PT
07-16-16  09:12AM               200192 puiapi.dll
11-20-16  09:59PM               456192 puiobj.dll
11-20-16  09:59PM                90624 pwrshplugin.dll
07-16-16  09:12AM                24576 qappsrv.exe
11-20-16  09:59PM              1054208 qmgr.dll
07-16-16  09:12AM                28160 qprocess.exe
07-16-16  09:12AM                97792 Query.dll
07-16-16  09:12AM                16896 query.exe
07-16-16  09:12AM                25088 quser.exe
07-16-16  09:12AM                29184 qwinsta.exe
07-16-16  09:13AM                98816 radardt.dll
07-16-16  09:18AM       <DIR>          ras
07-16-16  09:12AM               632320 rasapi32.dll
07-16-16  09:13AM               137728 raschap.dll
07-16-16  09:12AM                 1820 rasctrnm.h
07-16-16  09:12AM                76800 rasdiag.dll
07-16-16  09:12AM               109568 rasman.dll
11-20-16  09:59PM               648192 rasmans.dll
07-16-16  09:15AM               304640 rasppp.dll
07-16-16  09:12AM               247296 rastapi.dll
07-16-16  09:13AM               502784 rastls.dll
07-16-16  09:14AM                21504 RdmsInst.dll
07-16-16  09:14AM                 2560 rdmsres.dll
07-16-16  09:12AM                11264 rdpcfgex.dll
07-16-16  09:12AM               394240 rdpclip.exe
11-20-16  09:59PM              4148736 rdpcorets.dll
11-20-16  09:59PM               299008 rdpinit.exe
07-16-16  09:12AM               179200 rdpinput.exe
07-16-16  09:12AM                43008 RdpSa.exe
07-16-16  09:12AM                26112 RdpSaProxy.exe
07-16-16  09:12AM                14848 RdpSaPs.dll
07-16-16  09:12AM                27136 RdpSaUacHelper.exe
11-20-16  09:59PM               415744 rdpshell.exe
07-16-16  09:12AM                88064 rdpsign.exe
11-20-16  09:59PM                92512 rdpudd.dll
07-16-16  09:09AM                46592 rdrleakdiag.exe
07-16-16  09:12AM                66048 rdsdwmdr.dll
07-16-16  09:12AM               108544 RDVGHelper.exe
07-16-16  09:12AM                81920 rdvvmtransport.dll
11-20-16  09:59PM              1117024 ReAgent.dll
07-16-16  09:13AM                34816 ReAgentc.exe
07-16-16  09:13AM                13824 recover.exe
02-03-19  08:05AM       <DIR>          Recovery
07-16-16  09:09AM                74240 reg.exe
07-16-16  09:12AM               104448 regapi.dll
07-16-16  09:13AM                11776 regedt32.exe
07-16-16  09:13AM                15360 regidle.dll
07-16-16  09:09AM                24576 Register-CimProvider.exe
07-16-16  09:09AM               155648 regsvc.dll
07-16-16  09:13AM                23552 regsvr32.exe
07-16-16  09:13AM               190976 ReInfo.dll
07-16-16  09:12AM                43520 relog.exe
07-16-16  09:11AM                  167 removehypervisor.mof
07-16-16  09:13AM                21504 replace.exe
07-16-16  09:12AM                17408 reset.exe
07-16-16  09:13AM                  714 RestartManager.mof
07-16-16  09:13AM                  176 RestartManagerUninstall.mof
11-20-16  09:59PM               374784 resutils.dll
07-16-16  09:12AM                37888 rfxvmt.dll
07-16-16  09:12AM               599040 riched20.dll
07-16-16  09:12AM                10240 riched32.dll
07-16-16  09:13AM               577536 RMActivate.exe
07-16-16  09:13AM               607744 RMActivate_isv.exe
07-16-16  09:13AM               501248 RMActivate_ssp.exe
07-16-16  09:13AM               501760 RMActivate_ssp_isv.exe
07-16-16  09:13AM                17920 RmClient.exe
07-16-16  09:18AM       <DIR>          ro-RO
07-16-16  09:13AM                44032 RoamingSecurity.dll
07-16-16  09:13AM               132608 Robocopy.exe
07-16-16  09:09AM                23552 ROUTE.EXE
07-16-16  09:09AM                79360 RpcEpMap.dll
07-16-16  09:13AM               198144 rpchttp.dll
07-16-16  09:13AM                 9728 RpcNs4.dll
07-16-16  09:13AM                32768 rpcnsh.dll
11-20-16  09:59PM              1176664 rpcrt4.dll
07-16-16  09:10AM                63048 RpcRtRemote.dll
07-16-16  09:09AM               888320 rpcss.dll
07-16-16  09:09AM               202992 rsaenh.dll
07-16-16  09:12AM                43566 rsop.msc
07-16-16  09:11AM                97280 rsopprov.exe
07-16-16  09:13AM               201728 RstrtMgr.dll
07-16-16  09:12AM                46080 rtffilt.dll
07-16-16  09:12AM               179712 rtm.dll
07-16-16  09:12AM                62464 rtutils.dll
07-16-16  09:18AM       <DIR>          ru-RU
07-16-16  09:13AM                19968 runas.exe
07-16-16  09:12AM                69632 rundll32.exe
07-16-16  09:12AM                58368 runonce.exe
07-16-16  09:12AM                23040 rwinsta.exe
07-16-16  09:13AM                41984 sacsess.exe
07-16-16  09:13AM                16896 sacsvr.dll
07-16-16  09:09AM                79360 samcli.dll
11-20-16  09:59PM               123904 samlib.dll
11-20-16  09:59PM               883712 samsrv.dll
07-16-16  09:09AM                69632 sc.exe
07-16-16  09:13AM                48640 SCardBi.dll
07-16-16  09:13AM                83456 SCardDlg.dll
07-16-16  09:13AM               250880 SCardSvr.dll
07-16-16  09:13AM               201728 ScDeviceEnum.dll
07-16-16  09:13AM               270336 scecli.dll
07-16-16  09:13AM               502272 scesrv.dll
11-20-16  09:59PM               476672 schannel.dll
07-16-16  09:09AM                24576 schedcli.dll
07-16-16  09:13AM               948224 schedsvc.dll
07-16-16  09:13AM               226816 schtasks.exe
07-16-16  09:13AM               249344 scksp.dll
07-16-16  09:13AM                  461 sconfig.cmd
07-16-16  09:13AM                42148 SCregEdit.wsf
07-16-16  09:12AM                37376 scrnsave.scr
07-16-16  09:12AM               243712 scrobj.dll
07-16-16  09:12AM               550912 scrptadm.dll
07-16-16  09:12AM               195072 scrrun.dll
07-16-16  09:13AM                25088 sdbinst.exe
07-16-16  09:12AM               249856 SDClient.dll
07-16-16  09:12AM               386560 SDDS.dll
02-08-21  12:54PM               459136 sdelete64.exe
07-16-16  09:13AM                35840 sdhcinst.dll
07-16-16  09:13AM                39936 SecEdit.exe
07-16-16  09:09AM               357984 sechost.dll
07-16-16  09:13AM                16896 secinit.exe
07-16-16  09:09AM                31232 seclogon.dll
07-16-16  09:12AM               120458 secpol.msc
07-16-16  09:13AM               398848 secproc.dll
07-16-16  09:13AM               397312 secproc_isv.dll
07-16-16  09:13AM               112640 secproc_ssp.dll
07-16-16  09:13AM               112640 secproc_ssp_isv.dll
07-16-16  09:09AM                28160 secur32.dll
07-16-16  09:18AM       <DIR>          SecureBootUpdates
11-20-16  09:59PM               455520 securekernel.exe
07-16-16  09:13AM                95232 SecureTimeAggregator.dll
07-16-16  09:13AM                 5120 security.dll
11-20-16  09:59PM                70656 Sens.dll
07-16-16  09:13AM                14848 SensApi.dll
02-25-19  08:07AM       <DIR>          ServerManager
07-16-16  09:18AM       <DIR>          ServerManagerInternal
07-16-16  09:09AM               454600 services.exe
11-20-16  09:59PM               387072 SessEnv.dll
07-16-16  09:13AM                69632 setbcdlocale.dll
07-16-16  09:13AM                13824 setres.exe
07-16-16  09:13AM                29184 setspn.exe
07-16-16  09:13AM                 8192 settings.dat
11-20-16  09:59PM       <DIR>          Setup
07-16-16  09:13AM              4387168 setupapi.dll
07-16-16  09:13AM                94720 setupcl.exe
07-16-16  09:13AM                18784 setupetw.dll
11-20-16  09:59PM               125952 setupugc.exe
07-16-16  09:09AM                55808 setx.exe
07-16-16  09:13AM                 3072 sfc.dll
07-16-16  09:13AM                41472 sfc.exe
07-16-16  09:13AM                49664 sfc_os.dll
07-16-16  09:12AM               140288 shacct.dll
07-16-16  09:12AM                69632 shacctprofile.dll
07-16-16  09:12AM               681312 SHCore.dll
11-20-16  09:59PM             22223968 shell32.dll
07-16-16  09:12AM                10752 shfolder.dll
07-16-16  09:13AM                 7168 shimeng.dll
07-16-16  09:12AM               333640 shlwapi.dll
07-16-16  09:13AM               134144 shsetup.dll
07-16-16  09:13AM                24064 shutdown.exe
11-20-16  09:59PM               231424 shutdownux.dll
07-16-16  09:13AM                53760 signdrv.dll
07-16-16  09:13AM                74752 sigverif.exe
07-16-16  09:09AM               221696 SIHClient.exe
07-16-16  09:11AM                 2282 silcollector.cmd
07-16-16  09:15AM               160768 SimAuth.dll
07-16-16  09:15AM               102912 SimCfg.dll
07-16-16  09:12AM                 8192 simpdata.tlb
07-16-16  09:18AM       <DIR>          sk-SK
11-20-16  09:59PM               169056 skci.dll
07-16-16  09:18AM       <DIR>          sl-SI
11-20-16  09:59PM               135168 slc.dll
11-20-16  09:59PM                22016 slcext.dll
11-20-16  09:53PM       <DIR>          slmgr
07-16-16  09:13AM               142904 slmgr.vbs
07-16-16  09:13AM               179200 slr100.dll
07-16-16  09:13AM               442368 slui.exe
07-16-16  09:13AM                74240 slwga.dll
07-16-16  09:13AM               927744 SmartcardCredentialProvider.dll
07-16-16  09:10AM               207872 smbwmiv2.dll
07-16-16  02:04AM       <DIR>          SMI
07-16-16  02:04AM               854528 SmiEngine.dll
11-20-16  09:59PM                23552 smphost.dll
07-16-16  09:09AM               142584 smss.exe
07-16-16  09:09AM                32768 snmpapi.dll
07-16-16  09:12AM                15872 snmptrap.exe
07-16-16  09:12AM               160256 softkbd.dll
07-16-16  09:09AM                24064 sort.exe
11-20-16  09:59PM               130560 SpaceAgent.exe
11-20-16  09:59PM                35328 spaceman.exe
07-16-16  09:13AM                84480 spbcd.dll
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
07-16-16  09:13AM               101888 spfileq.dll
07-16-16  09:13AM               103424 spinf.dll
07-16-16  09:13AM                10752 spmpm.dll
07-16-16  09:13AM                11776 spnet.dll
07-16-16  09:18AM       <DIR>          spool
07-16-16  09:13AM                91136 spoolss.dll
11-20-16  09:59PM               792064 spoolsv.exe
07-16-16  09:13AM                51712 spopk.dll
07-16-16  09:18AM       <DIR>          spp
11-20-16  09:59PM               138240 sppc.dll
11-20-16  09:59PM               538112 sppcext.dll
07-16-16  09:13AM               402432 sppcomapi.dll
07-16-16  09:13AM               656896 SppExtComObj.Exe
07-16-16  09:13AM                33792 sppinst.dll
07-16-16  09:13AM               178176 sppnp.dll
11-20-16  09:59PM              1600632 sppobjs.dll
11-20-16  09:59PM              5622088 sppsvc.exe
07-16-16  09:18AM       <DIR>          sppui
11-20-16  09:59PM               742704 sppwinob.dll
07-16-16  09:13AM               143360 sppwmi.dll
07-16-16  09:13AM               501088 spwizeng.dll
07-16-16  09:13AM              5865312 spwizimg.dll
07-16-16  09:13AM              5928448 spwizimg_svr.dll
07-16-16  09:13AM                16736 spwizres.dll
07-16-16  09:13AM               140800 sqlcecompact40.dll
07-16-16  09:13AM               204800 sqlceoledb40.dll
07-16-16  09:13AM               919552 sqlceqp40.dll
07-16-16  09:13AM               529408 sqlcese40.dll
07-16-16  09:12AM               735744 sqlsrv32.dll
07-16-16  09:12AM                94208 sqlsrv32.rll
07-16-16  09:12AM                37784 sqmapi.dll
11-20-16  09:59PM       <DIR>          sr-Latn-CS
07-16-16  09:18AM       <DIR>          sr-Latn-RS
07-16-16  09:13AM               136704 srpapi.dll
07-16-16  09:12AM               313344 SrpUxNativeSnapIn.dll
07-16-16  09:09AM               112632 srvcli.dll
07-16-16  09:14AM                62976 SrvMgrInst.dll
07-16-16  09:09AM               305152 srvsvc.dll
07-16-16  09:09AM                48128 sscore.dll
07-16-16  09:09AM                13312 sscoreext.dll
11-20-16  09:59PM               172528 sspicli.dll
07-16-16  09:09AM                28672 sspisrv.dll
07-16-16  02:04AM               133472 SSShim.dll
07-16-16  09:12AM               209920 sstpsvc.dll
07-16-16  09:10AM               642048 StateRepository.Core.dll
07-16-16  09:13AM                62464 stclient.dll
11-20-16  09:59PM                18432 stdole2.tlb
07-16-16  09:13AM                 7168 stdole32.tlb
11-20-16  09:59PM              2860032 storagewmi.dll
11-20-16  09:59PM                25600 storagewmi_passthru.dll
07-16-16  09:12AM                67584 Storprop.dll
11-20-16  09:59PM               634368 StructuredQuery.dll
07-16-16  09:13AM                16384 subst.exe
07-16-16  09:18AM       <DIR>          sv-SE
07-16-16  09:09AM                44496 svchost.exe
07-16-16  09:13AM                13824 svsvc.dll
07-16-16  09:13AM               467456 swprv.dll
07-16-16  09:13AM               616736 sxs.dll
07-16-16  09:13AM                45056 sxshared.dll
07-16-16  09:13AM                34304 sxssrv.dll
07-16-16  09:13AM                29696 sxsstore.dll
07-16-16  09:13AM                36864 sxstrace.exe
07-16-16  09:13AM               130048 sysclass.dll
07-16-16  09:13AM                31744 syskey.exe
07-16-16  09:13AM               944128 sysmain.dll
07-16-16  09:09AM                28160 sysntfy.dll
02-25-19  07:48AM       <DIR>          Sysprep
07-16-16  09:12AM                 3317 sysprint.sep
07-16-16  09:12AM                 3666 sysprtj.sep
07-16-16  09:13AM                18432 syssetup.dll
07-16-16  09:09AM               387072 SystemEventsBrokerServer.dll
07-16-16  09:12AM               101888 systeminfo.exe
07-16-16  09:12AM               166912 Tabbtn.dll
07-16-16  09:12AM                77824 TabbtnEx.dll
07-16-16  09:13AM                62464 takeown.exe
07-16-16  09:13AM               474624 taskcomp.dll
07-16-16  09:13AM                88392 taskhostw.exe
07-16-16  09:12AM                95744 taskkill.exe
07-16-16  09:12AM               100864 tasklist.exe
07-16-16  09:13AM              1259720 Taskmgr.exe
02-25-19  11:24PM       <DIR>          Tasks
07-16-16  09:13AM               808344 taskschd.dll
07-16-16  09:13AM                58880 TaskSchdPS.dll
07-16-16  09:13AM                44464 tbs.dll
07-16-16  09:12AM                 1673 tcpbidi.xml
11-20-16  09:59PM               234496 tcpipcfg.dll
07-16-16  09:12AM                37376 tcpmib.dll
07-16-16  09:12AM               219648 tcpmon.dll
07-16-16  09:12AM                60124 tcpmon.ini
07-16-16  09:12AM                71168 tcpmonui.dll
07-16-16  09:09AM                12288 TCPSVCS.EXE
11-20-16  09:59PM               680448 tdh.dll
07-16-16  09:12AM               987648 termsrv.dll
07-16-16  09:18AM       <DIR>          th-TH
07-16-16  09:13AM                18944 TieringEngineProxy.dll
07-16-16  09:13AM               287744 TieringEngineService.exe
07-16-16  09:09AM                36352 TimeBrokerClient.dll
07-16-16  09:09AM               177664 TimeBrokerServer.dll
11-20-16  09:59PM               545792 timedate.cpl
07-16-16  09:13AM                11776 TimeDateMUICallback.dll
07-16-16  09:13AM                30720 timeout.exe
07-16-16  09:12AM                48128 tlscsp.dll
07-16-16  09:09AM                39936 tokenbinding.dll
07-16-16  09:13AM                 3584 TpmCertResources.dll
11-20-16  09:59PM               531456 TpmCoreProvisioning.dll
11-20-16  09:59PM                43520 TpmTasks.dll
07-16-16  09:18AM       <DIR>          tr-TR
07-16-16  09:12AM               412160 tracerpt.exe
07-16-16  09:09AM                17920 TRACERT.EXE
07-16-16  09:12AM                42496 traffic.dll
07-16-16  09:13AM                19968 tree.com
07-16-16  09:12AM               220672 tscfgwmi.dll
07-16-16  09:12AM                23552 tscon.exe
07-16-16  09:12AM                15360 tsddd.dll
07-16-16  09:12AM                23552 tsdiscon.exe
07-16-16  09:12AM                12288 TSErrRedir.dll
07-16-16  09:12AM                24064 tskill.exe
11-20-16  09:59PM               115712 TSpkg.dll
07-16-16  09:14AM                91648 tsPubIconHelper.dll
11-20-16  09:59PM               221696 tspubwmi.dll
07-16-16  09:12AM               117248 tssdjet.dll
07-16-16  09:15AM                82432 TSSessionUX.dll
07-16-16  09:12AM               179712 tssrvlic.dll
07-16-16  09:12AM                54272 TSTheme.exe
07-16-16  09:15AM               246272 TtlsAuth.dll
07-16-16  09:15AM               224256 TtlsCfg.dll
11-20-16  09:59PM              1157000 twinapi.appcore.dll
11-20-16  09:59PM               483328 twinapi.dll
07-16-16  09:13AM               118272 txflog.dll
07-16-16  09:12AM                12800 txfw32.dll
07-16-16  09:12AM                47616 typeperf.exe
11-20-16  09:59PM                 2560 tzres.dll
07-16-16  09:13AM                60928 tzsync.exe
07-16-16  09:13AM                 4096 tzsyncres.dll
07-16-16  09:13AM                58368 tzutil.exe
07-16-16  09:12AM                81920 ualapi.dll
07-16-16  09:12AM               261120 ualsvc.dll
11-20-16  09:59PM               252928 ubpm.dll
07-16-16  09:09AM               998920 ucrtbase.dll
07-16-16  09:13AM                43520 ucsvc.exe
07-16-16  09:09AM               112640 uexfat.dll
07-16-16  09:09AM               152064 ufat.dll
11-20-16  09:59PM              1710080 UIAutomationCore.dll
07-16-16  09:18AM       <DIR>          uk-UA
07-16-16  09:09AM               181600 ulib.dll
07-16-16  09:12AM                70144 umb.dll
07-16-16  09:13AM               111104 umpnpmgr.dll
07-16-16  09:10AM                17408 umpo-overrides-base.dll
07-16-16  09:10AM                13312 umpo-overrides-xpc.dll
07-16-16  09:09AM               123904 umpo.dll
07-16-16  09:13AM                96256 umpoext.dll
07-16-16  09:13AM                55808 umpowmi.dll
07-16-16  09:12AM               273408 umrdp.dll
07-16-16  09:13AM               241504 unattend.dll
07-16-16  09:10AM                43008 unlodctr.exe
07-16-16  09:09AM               574976 untfs.dll
07-16-16  09:13AM                90112 updatecsp.dll
07-16-16  09:13AM               289792 updatehandlers.dll
11-20-16  09:59PM                90112 updatepolicy.dll
11-20-16  09:59PM               628736 uReFS.dll
07-16-16  09:13AM               516608 uReFSv1.dll
07-16-16  09:13AM                30208 ureg.dll
11-20-16  09:59PM              1779712 urlmon.dll
11-20-16  09:59PM               324608 usbmon.dll
07-16-16  09:12AM                14336 usbperf.dll
11-20-16  09:59PM              1461200 user32.dll
07-16-16  09:09AM               115744 userenv.dll
07-16-16  09:09AM                33280 userinit.exe
07-16-16  09:13AM                19968 userinitext.dll
07-16-16  09:10AM                79360 UserLanguageProfileCallback.dll
11-20-16  09:59PM              1020928 usermgr.dll
07-16-16  09:13AM                65536 usermgrcli.dll
11-20-16  09:59PM               268800 UserMgrProxy.dll
07-16-16  09:13AM                73728 usoapi.dll
07-16-16  09:13AM                32768 UsoClient.exe
11-20-16  09:59PM               539136 usocore.dll
07-16-16  09:12AM                79360 usp10.dll
07-16-16  09:12AM                45496 utildll.dll
07-16-16  09:13AM               167936 uudf.dll
07-16-16  09:12AM                92160 UXInit.dll
07-16-16  09:13AM               169312 uxlib.dll
07-16-16  09:13AM                11616 uxlibres.dll
07-16-16  09:10AM               587264 uxtheme.dll
07-16-16  09:10AM               267264 vaultcli.dll
07-16-16  09:13AM                26624 VaultCmd.exe
07-16-16  09:13AM               109056 VaultRoaming.dll
07-16-16  09:10AM               358912 vaultsvc.dll
11-20-16  09:59PM               590848 vbscript.dll
07-16-16  09:13AM               649216 vds.exe
07-16-16  09:13AM               239104 vdsbas.dll
07-16-16  09:13AM               591360 vdsdyn.dll
07-16-16  09:13AM                25600 vdsldr.exe
07-16-16  09:13AM               129536 vdsutil.dll
07-16-16  09:13AM                56832 vdsvd.dll
07-16-16  09:13AM               109056 vds_ps.dll
07-16-16  09:13AM               373936 verifier.dll
07-16-16  09:09AM               135168 verifier.exe
07-16-16  09:12AM                30504 version.dll
07-16-16  09:09AM                51712 virtdisk.dll
09-20-17  03:47AM               113080 vm3ddevapi64.dll
09-20-17  03:47AM             19044792 vm3dgl64.dll
09-20-17  03:47AM               362424 vm3dum64.dll
09-20-17  03:47AM               217528 vm3dum64_10.dll
07-16-16  09:11AM                16896 VmApplicationHealthMonitorProxy.dll
07-16-16  09:09AM                28456 vmbuspipe.dll
09-20-17  03:44AM               393192 vmGuestLib.dll
09-20-17  03:44AM                48616 vmGuestLibJava.dll
07-16-16  09:11AM                48128 vmictimeprovider.dll
11-20-16  09:59PM               427008 vmrdvcore.dll
09-20-17  03:30AM                22016 VMWSU_V1_0.DLL
07-16-16  09:12AM               587776 vpnike.dll
07-16-16  09:12AM                47104 vpnikeapi.dll
09-20-17  01:08AM                69104 vsocklib.dll
07-16-16  09:13AM               145408 vssadmin.exe
07-16-16  09:15AM              1562112 vssapi.dll
07-16-16  09:15AM                70144 vsstrace.dll
07-16-16  09:13AM              1443328 VSSVC.exe
07-16-16  09:13AM                61952 vss_ps.dll
11-20-16  09:59PM               520192 w32time.dll
07-16-16  09:13AM                81920 w32tm.exe
07-16-16  09:09AM                35328 w32topl.dll
07-16-16  09:13AM                39936 waitfor.exe
02-25-19  08:07AM                15360 wamregps.dll
02-25-19  10:56PM       <DIR>          wbem
07-16-16  09:10AM               470016 wbemcomn.dll
07-16-16  09:13AM               304128 wcl.dll
07-16-16  09:13AM                59904 wclEtw.dll
07-16-16  09:13AM               132096 wclPowrProf.dll
07-16-16  09:13AM                15360 wclSqm.dll
07-16-16  09:13AM               125952 wclUnicode.dll
07-16-16  09:13AM                 8704 wclWdi.dll
07-16-16  09:18AM       <DIR>          WDI
07-16-16  09:13AM                97792 wdi.dll
07-16-16  09:09AM               220672 wdigest.dll
07-16-16  02:04AM               267104 wdscore.dll
07-16-16  09:13AM                  614 WdsUnattendTemplate.xml
07-16-16  09:14AM                10240 WebCache.exe
11-20-16  09:59PM               560640 webio.dll
07-16-16  09:09AM              1376512 webservices.dll
07-16-16  09:09AM                46080 Websocket.dll
07-16-16  09:12AM                79872 wecapi.dll
07-16-16  09:12AM               206848 wecsvc.dll
07-16-16  09:12AM               106496 wecutil.exe
11-20-16  09:59PM               682816 wer.dll
07-16-16  09:09AM                38912 werdiagcontroller.dll
11-20-16  09:59PM               238056 weretw.dll
07-16-16  09:09AM               295264 WerFault.exe
07-16-16  09:09AM               124080 WerFaultSecure.exe
07-16-16  09:09AM               144736 wermgr.exe
07-16-16  09:09AM               156672 wersvc.dll
07-16-16  09:12AM               450048 werui.dll
11-20-16  09:59PM               389000 wevtapi.dll
07-16-16  09:12AM               103936 wevtfwd.dll
11-20-16  09:59PM              1709056 wevtsvc.dll
07-16-16  09:09AM               238592 wevtutil.exe
07-16-16  09:10AM                24576 wfapigp.dll
07-16-16  09:13AM                40960 where.exe
07-16-16  09:12AM                16384 whhelper.dll
07-16-16  09:13AM                70144 whoami.exe
07-16-16  09:13AM                 2307 WimBootCompress.ini
07-16-16  09:13AM               699744 wimgapi.dll
07-16-16  09:13AM               526176 wimserv.exe
11-20-16  09:59PM               206848 win32k.sys
11-20-16  09:59PM              1513472 win32kbase.sys
11-20-16  09:59PM              3616768 win32kfull.sys
11-20-16  09:59PM               833024 win32spl.dll
11-20-16  09:59PM               114192 win32u.dll
07-16-16  09:13AM                25600 Win32_DeviceGuard.dll
07-16-16  09:13AM               149504 winbio.dll
07-16-16  09:13AM                45056 winbioext.dll
07-16-16  09:13AM                69776 winbrand.dll
11-20-16  09:59PM               380928 wincorlib.dll
07-16-16  09:13AM                44544 wincredprovider.dll
07-16-16  09:13AM               174080 wincredui.dll
11-20-16  09:59PM               358912 Windows.ApplicationModel.dll
07-16-16  09:12AM                43008 Windows.Devices.Printers.Extensions.dll
11-20-16  09:59PM               437248 Windows.Devices.Usb.dll
07-16-16  09:12AM               339968 Windows.Graphics.dll
11-20-16  09:59PM               208896 Windows.Internal.UI.Logon.ProxyStub.dll
11-20-16  09:59PM              4136960 Windows.StateRepository.dll
11-20-16  09:59PM                73216 Windows.StateRepositoryBroker.dll
11-20-16  09:59PM               122880 Windows.StateRepositoryClient.dll
11-20-16  09:59PM              7219672 windows.storage.dll
07-16-16  09:13AM                23040 Windows.System.RemoteDesktop.dll
11-20-16  09:59PM              1726976 Windows.UI.Immersive.dll
11-20-16  09:59PM              1738040 WindowsCodecs.dll
07-16-16  09:12AM               277504 WindowsCodecsExt.dll
07-16-16  09:09AM              1041408 windowsperformancerecordercontrol.dll
07-16-16  09:18AM       <DIR>          WindowsPowerShell
07-16-16  09:13AM                33280 WindowsUpdateElevatedInstaller.exe
07-16-16  09:18AM       <DIR>          winevt
11-20-16  09:59PM               817664 winhttp.dll
07-16-16  09:09AM               100352 winhttpcom.dll
11-20-16  09:59PM              2669056 wininet.dll
07-16-16  09:09AM               304240 wininit.exe
07-16-16  09:13AM                33632 wininitext.dll
07-16-16  09:12AM               479744 winipcfile.dll
07-16-16  09:12AM               967680 winipcsecproc.dll
07-16-16  09:12AM               101376 winipsec.dll
07-16-16  09:10AM               429568 Winlangdb.dll
11-20-16  09:59PM              1354320 winload.efi
11-20-16  09:59PM              1173496 winload.exe
11-20-16  09:59PM               673792 winlogon.exe
07-16-16  09:13AM                76288 winlogonext.dll
07-16-16  09:18AM       <DIR>          WinMetadata
07-16-16  09:13AM               124552 winmm.dll
07-16-16  09:13AM               164264 winmmbase.dll
07-16-16  09:12AM              2054144 winmsipc.dll
07-16-16  09:12AM                87040 WinMsoIrmProtector.dll
07-16-16  09:09AM                19968 winnlsres.dll
07-16-16  09:09AM                32584 winnsi.dll
07-16-16  09:12AM                81408 WinOpcIrmProtector.dll
11-20-16  09:59PM              1051112 winresume.efi
11-20-16  09:59PM               894096 winresume.exe
11-20-16  09:53PM       <DIR>          winrm
07-16-16  09:10AM                  199 winrm.cmd
07-16-16  09:10AM               204105 winrm.vbs
07-16-16  09:10AM                48640 winrs.exe
07-16-16  09:10AM               107520 winrscmd.dll
07-16-16  09:10AM                28672 winrshost.exe
07-16-16  09:10AM                 2048 winrsmgr.dll
07-16-16  09:10AM                14336 winrssrv.dll
07-16-16  09:13AM               236544 WinSCard.dll
07-16-16  09:12AM                17920 winshfhc.dll
07-16-16  09:13AM               290816 winsku.dll
07-16-16  09:12AM                91648 winsockhc.dll
07-16-16  09:13AM               525312 winspool.drv
07-16-16  09:12AM                25600 WINSRPC.DLL
11-20-16  09:59PM               147456 winsrv.dll
07-16-16  09:12AM               332144 winsta.dll
07-16-16  09:14AM               820736 WinSync.dll
11-20-16  09:59PM               341936 wintrust.dll
11-20-16  09:59PM              1267504 WinTypes.dll
07-16-16  09:13AM                26624 winusb.dll
07-16-16  09:13AM                35328 witnesswmiv2provider.dll
07-16-16  09:09AM                80088 wkscli.dll
11-20-16  09:59PM               283648 wkssvc.dll
07-16-16  09:09AM               352256 Wldap32.dll
07-16-16  09:13AM                70288 wldp.dll
07-16-16  09:13AM                64584 wlrmdr.exe
07-16-16  09:09AM                 5632 wmi.dll
07-16-16  09:09AM                45568 wmiclnt.dll
07-16-16  09:13AM               386048 wmicmiplugin.dll
07-16-16  09:10AM               164864 wmidcom.dll
07-16-16  09:13AM                29696 wmiprop.dll
07-16-16  09:10AM               210944 wmitomi.dll
07-16-16  09:12AM               391168 WMPhoto.dll
07-16-16  09:09AM                18944 wmsgapi.dll
07-16-16  09:13AM                33792 WofUtil.dll
07-16-16  09:12AM                15360 workerdd.dll
07-16-16  09:13AM               318784 wow64.dll
07-16-16  09:13AM                22336 wow64cpu.dll
07-16-16  09:12AM               486040 wow64win.dll
07-16-16  09:13AM                17408 wowreg32.exe
08-18-14  11:07PM               370424 wpcap.dll
07-16-16  09:09AM                10752 WppRecorderUM.dll
07-16-16  09:09AM                  726 wpr.config.xml
07-16-16  09:09AM               275968 wpr.exe
07-16-16  09:12AM                 4608 ws2help.dll
11-20-16  09:59PM               424640 ws2_32.dll
07-16-16  09:15AM                25600 wsbonline.dll
07-16-16  09:12AM               164864 wscript.exe
07-16-16  09:12AM               675328 WSDApi.dll
07-16-16  09:12AM               590848 WSDMon.dll
07-16-16  09:14AM                 5120 WSEDeployRes.dll
07-16-16  09:12AM                23552 wshcon.dll
07-16-16  09:12AM                22528 wshelper.dll
07-16-16  09:11AM                 9728 wshhyperv.dll
07-16-16  09:09AM                12800 wship6.dll
07-16-16  09:12AM               142336 wshom.ocx
07-16-16  09:12AM                19456 wshqos.dll
07-16-16  09:09AM                12800 WSHTCPIP.DLL
07-16-16  09:10AM                31744 WsmAgent.dll
07-16-16  09:10AM                 4675 wsmanconfig_schema.xml
11-20-16  09:59PM                32256 WSManHTTPConfig.exe
07-16-16  09:10AM                73728 WSManMigrationPlugin.dll
07-16-16  09:10AM               158720 WsmAuto.dll
07-16-16  09:10AM                15360 wsmplpxy.dll
07-16-16  09:10AM                37376 wsmprovhost.exe
07-16-16  09:10AM                 1559 WsmPty.xsl
07-16-16  09:10AM                61440 WsmRes.dll
07-16-16  09:13AM               143872 Wsmselpl.dll
07-16-16  09:13AM                 2560 Wsmselrr.dll
11-20-16  09:59PM              2716672 WsmSvc.dll
07-16-16  09:10AM                 2426 WsmTxt.xsl
07-16-16  09:10AM               282112 WsmWmiPl.dll
07-16-16  09:12AM                64000 wsnmp32.dll
07-16-16  09:09AM                18432 wsock32.dll
11-20-16  09:59PM              1913344 wsp_fs.dll
11-20-16  09:59PM              1554944 wsp_health.dll
11-20-16  09:59PM               947200 wsp_sr.dll
07-16-16  09:12AM                78336 wsqmcons.exe
07-16-16  09:12AM                64112 wtsapi32.dll
11-20-16  09:59PM               869888 wuapi.dll
11-20-16  09:59PM                26408 wuauclt.exe
11-20-16  09:59PM              2315264 wuaueng.dll
07-16-16  09:12AM                48128 WUDFCoinstaller.dll
07-16-16  09:09AM               251392 WUDFHost.exe
07-16-16  09:09AM               196608 WUDFPlatform.dll
07-16-16  09:09AM                99840 WUDFSvc.dll
07-16-16  09:12AM               582656 WUDFx.dll
07-16-16  09:09AM               599552 WUDFx02000.dll
07-16-16  09:13AM                93696 wudriver.dll
11-20-16  09:59PM                48640 wups.dll
11-20-16  09:59PM                32768 wups2.dll
07-16-16  09:13AM               308736 wusa.exe
11-20-16  09:59PM               391168 wuuhext.dll
07-16-16  09:09AM                47616 xcopy.exe
07-16-16  09:12AM                67072 xmlfilter.dll
07-16-16  09:09AM               214360 xmllite.dll
07-16-16  09:13AM                62976 xolehlp.dll
07-16-16  09:12AM               532480 XpsGdiConverter.dll
07-16-16  09:12AM              1699840 XpsPrint.dll
07-16-16  09:18AM       <DIR>          zh-CN
07-16-16  09:18AM       <DIR>          zh-HK
07-16-16  09:18AM       <DIR>          zh-TW
226 Transfer complete.
ftp> cd inetsrv
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||51429|)
150 Opening ASCII mode data connection.
02-25-19  08:07AM               119808 appcmd.exe
07-16-16  09:14AM                 3810 appcmd.xml
02-25-19  08:07AM               184320 AppHostNavigators.dll
02-25-19  08:07AM               405504 appobj.dll
02-25-19  08:07AM               129536 aspnetca.exe
02-25-19  10:15PM                40960 authanon.dll
02-25-19  10:15PM                37888 authbas.dll
02-25-19  10:15PM                53248 authsspi.dll
02-25-19  08:07AM       <DIR>          config
02-25-19  10:15PM                39424 diprestr.dll
02-25-19  10:15PM       <DIR>          en-US
02-25-19  08:07AM                19456 ftpconfigext.dll
02-25-19  08:07AM                14336 ftpctrlps.dll
02-25-19  08:07AM                14336 ftpmib.dll
02-25-19  08:07AM                15360 ftpres.dll
02-25-19  08:07AM               382976 ftpsvc.dll
02-25-19  08:07AM                69990 ftpsvc.mof
02-25-19  10:15PM                17920 hwebcore.dll
02-25-19  10:15PM               322048 iiscore.dll
02-25-19  10:15PM               101888 iisetw.dll
02-25-19  10:15PM               167936 iisfreb.dll
02-25-19  08:07AM               109568 iisreg.dll
02-25-19  08:07AM               230912 iisres.dll
02-25-19  08:07AM                37888 iisrstas.exe
02-25-19  08:07AM               190464 iissetup.exe
02-25-19  08:07AM                72192 iissyspr.dll
02-25-19  08:07AM               290816 iisutil.dll
02-25-19  10:15PM               568832 iisw3adm.dll
02-25-19  10:15PM                29696 iprestr.dll
02-25-19  10:15PM                38400 loghttp.dll
02-25-19  10:15PM               143360 Microsoft.Web.Administration.dll
02-25-19  10:15PM              1052672 Microsoft.Web.Management.dll
02-25-19  10:15PM                41984 modrqflt.dll
02-25-19  08:07AM               492544 nativerd.dll
02-25-19  08:07AM                33792 rsca.dll
02-25-19  08:07AM                51200 rscaext.dll
02-25-19  08:07AM               193024 uihelper.dll
02-25-19  10:15PM                23552 urlauthz.dll
02-25-19  10:15PM               145480 w3core.mof
02-25-19  08:07AM                15872 w3ctrlps.dll
02-25-19  10:15PM               110592 w3dt.dll
02-25-19  10:15PM                 2560 w3isapi.mof
02-25-19  10:15PM                29696 w3tp.dll
02-25-19  10:15PM                72192 w3wphost.dll
02-25-19  10:15PM                31744 wbhstipm.dll
02-25-19  10:15PM                27648 wbhst_pm.dll
02-25-19  10:15PM                12288 WMSvc.exe
07-16-16  09:11AM                  165 wmsvc.exe.config
02-25-19  08:07AM               172032 XPath.dll
226 Transfer complete.
ftp> cd config
550 Access is denied. 
ftp> dir
229 Entering Extended Passive Mode (|||51430|)
125 Data connection already open; Transfer starting.
02-25-19  08:07AM               119808 appcmd.exe
07-16-16  09:14AM                 3810 appcmd.xml
02-25-19  08:07AM               184320 AppHostNavigators.dll
02-25-19  08:07AM               405504 appobj.dll
02-25-19  08:07AM               129536 aspnetca.exe
02-25-19  10:15PM                40960 authanon.dll
02-25-19  10:15PM                37888 authbas.dll
02-25-19  10:15PM                53248 authsspi.dll
02-25-19  08:07AM       <DIR>          config
02-25-19  10:15PM                39424 diprestr.dll
02-25-19  10:15PM       <DIR>          en-US
02-25-19  08:07AM                19456 ftpconfigext.dll
02-25-19  08:07AM                14336 ftpctrlps.dll
02-25-19  08:07AM                14336 ftpmib.dll
02-25-19  08:07AM                15360 ftpres.dll
02-25-19  08:07AM               382976 ftpsvc.dll
02-25-19  08:07AM                69990 ftpsvc.mof
02-25-19  10:15PM                17920 hwebcore.dll
02-25-19  10:15PM               322048 iiscore.dll
02-25-19  10:15PM               101888 iisetw.dll
02-25-19  10:15PM               167936 iisfreb.dll
02-25-19  08:07AM               109568 iisreg.dll
02-25-19  08:07AM               230912 iisres.dll
02-25-19  08:07AM                37888 iisrstas.exe
02-25-19  08:07AM               190464 iissetup.exe
02-25-19  08:07AM                72192 iissyspr.dll
02-25-19  08:07AM               290816 iisutil.dll
02-25-19  10:15PM               568832 iisw3adm.dll
02-25-19  10:15PM                29696 iprestr.dll
02-25-19  10:15PM                38400 loghttp.dll
02-25-19  10:15PM               143360 Microsoft.Web.Administration.dll
02-25-19  10:15PM              1052672 Microsoft.Web.Management.dll
02-25-19  10:15PM                41984 modrqflt.dll
02-25-19  08:07AM               492544 nativerd.dll
02-25-19  08:07AM                33792 rsca.dll
02-25-19  08:07AM                51200 rscaext.dll
02-25-19  08:07AM               193024 uihelper.dll
02-25-19  10:15PM                23552 urlauthz.dll
02-25-19  10:15PM               145480 w3core.mof
02-25-19  08:07AM                15872 w3ctrlps.dll
02-25-19  10:15PM               110592 w3dt.dll
02-25-19  10:15PM                 2560 w3isapi.mof
02-25-19  10:15PM                29696 w3tp.dll
02-25-19  10:15PM                72192 w3wphost.dll
02-25-19  10:15PM                31744 wbhstipm.dll
02-25-19  10:15PM                27648 wbhst_pm.dll
02-25-19  10:15PM                12288 WMSvc.exe
07-16-16  09:11AM                  165 wmsvc.exe.config
02-25-19  08:07AM               172032 XPath.dll
226 Transfer complete.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||52561|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52562|)
150 Opening ASCII mode data connection.
02-25-19  11:44PM       <DIR>          Administrator
01-15-24  11:03AM       <DIR>          Public
226 Transfer complete.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52563|)
150 Opening ASCII mode data connection.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd documents
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52564|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> help
Commands may be abbreviated.  Commands are:

!               edit            lpage           nlist           rcvbuf          struct
$               epsv            lpwd            nmap            recv            sunique
account         epsv4           ls              ntrans          reget           system
append          epsv6           macdef          open            remopts         tenex
ascii           exit            mdelete         page            rename          throttle
bell            features        mdir            passive         reset           trace
binary          fget            mget            pdir            restart         type
bye             form            mkdir           pls             rhelp           umask
case            ftp             mls             pmlsd           rmdir           unset
cd              gate            mlsd            preserve        rstatus         usage
cdup            get             mlst            progress        runique         user
chmod           glob            mode            prompt          send            verbose
close           hash            modtime         proxy           sendport        xferbuf
cr              help            more            put             set             ?
debug           idle            mput            pwd             site
delete          image           mreget          quit            size
dir             lcd             msend           quote           sndbuf
disconnect      less            newer           rate            status
ftp> ls -la
229 Entering Extended Passive Mode (|||52565|)
150 Opening ASCII mode data connection.
02-03-19  08:08AM       <DIR>          AccountPictures
01-15-24  11:03AM       <DIR>          Desktop
07-16-16  09:16AM                  174 desktop.ini
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Libraries
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> lcd boxes
Local directory now: /home/kali/boxes
ftp> lcd htb
Local directory now: /home/kali/boxes/htb
ftp> lcd netmon
Local directory now: /home/kali/boxes/htb/netmon
ftp> help
Commands may be abbreviated.  Commands are:

!               edit            lpage           nlist           rcvbuf          struct
$               epsv            lpwd            nmap            recv            sunique
account         epsv4           ls              ntrans          reget           system
append          epsv6           macdef          open            remopts         tenex
ascii           exit            mdelete         page            rename          throttle
bell            features        mdir            passive         reset           trace
binary          fget            mget            pdir            restart         type
bye             form            mkdir           pls             rhelp           umask
case            ftp             mls             pmlsd           rmdir           unset
cd              gate            mlsd            preserve        rstatus         usage
cdup            get             mlst            progress        runique         user
chmod           glob            mode            prompt          send            verbose
close           hash            modtime         proxy           sendport        xferbuf
cr              help            more            put             set             ?
debug           idle            mput            pwd             site
delete          image           mreget          quit            size
dir             lcd             msend           quote           sndbuf
disconnect      less            newer           rate            status
ftp> mget *
421 Service not available, remote server has closed connection.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ cd /home/kali/boxes/htb/netmon
                                                                                                               
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ ls -la
total 8
drwxrwxr-x  2 kali kali 4096 May 16 17:33 .
drwxr-xr-x 12 kali kali 4096 May 16 17:33 ..
                                                                                                               
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ ftp 10.10.10.152              
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||52679|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users
250 CWD command successful.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52687|)
150 Opening ASCII mode data connection.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> mget *
ftp> help
Commands may be abbreviated.  Commands are:

!               edit            lpage           nlist           rcvbuf          struct
$               epsv            lpwd            nmap            recv            sunique
account         epsv4           ls              ntrans          reget           system
append          epsv6           macdef          open            remopts         tenex
ascii           exit            mdelete         page            rename          throttle
bell            features        mdir            passive         reset           trace
binary          fget            mget            pdir            restart         type
bye             form            mkdir           pls             rhelp           umask
case            ftp             mls             pmlsd           rmdir           unset
cd              gate            mlsd            preserve        rstatus         usage
cdup            get             mlst            progress        runique         user
chmod           glob            mode            prompt          send            verbose
close           hash            modtime         proxy           sendport        xferbuf
cr              help            more            put             set             ?
debug           idle            mput            pwd             site
delete          image           mreget          quit            size
dir             lcd             msend           quote           sndbuf
disconnect      less            newer           rate            status
ftp> dir
229 Entering Extended Passive Mode (|||52691|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd desktop
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52699|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1195 PRTG Enterprise Console.lnk
02-03-19  12:18AM                 1160 PRTG Network Monitor.lnk
05-16-25  08:16AM                   34 user.txt
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52700|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd documents
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52701|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52702|)
150 Opening ASCII mode data connection.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> 
ftp> cd downloads
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52703|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> dir *
229 Entering Extended Passive Mode (|||52704|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> dir music
229 Entering Extended Passive Mode (|||52705|)
550 The system cannot find the file specified. 
ftp> dir ./music/
229 Entering Extended Passive Mode (|||52715|)
550 The system cannot find the file specified. 
ftp> cd music
550 The system cannot find the file specified. 
ftp> dir
229 Entering Extended Passive Mode (|||52716|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52717|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> dir music
229 Entering Extended Passive Mode (|||52718|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> dir pictures
229 Entering Extended Passive Mode (|||52719|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> dir desktop
229 Entering Extended Passive Mode (|||52720|)
125 Data connection already open; Transfer starting.
02-03-19  12:18AM                 1195 PRTG Enterprise Console.lnk
02-03-19  12:18AM                 1160 PRTG Network Monitor.lnk
05-16-25  08:16AM                   34 user.txt
226 Transfer complete.
ftp> dir videos
229 Entering Extended Passive Mode (|||52721|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> cd administratir
550 The system cannot find the file specified. 
ftp> cd administrator
550 Access is denied. 
ftp> dir
229 Entering Extended Passive Mode (|||52731|)
150 Opening ASCII mode data connection.
02-25-19  11:44PM       <DIR>          Administrator
01-15-24  11:03AM       <DIR>          Public
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52732|)
125 Data connection already open; Transfer starting.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd users/public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52733|)
125 Data connection already open; Transfer starting.
01-15-24  11:03AM       <DIR>          Desktop
02-03-19  08:05AM       <DIR>          Documents
07-16-16  09:18AM       <DIR>          Downloads
07-16-16  09:18AM       <DIR>          Music
07-16-16  09:18AM       <DIR>          Pictures
07-16-16  09:18AM       <DIR>          Videos
226 Transfer complete.
ftp> cd desktop
250 CWD command successful.
ftp> get *
local: * remote: *
229 Entering Extended Passive Mode (|||52734|)
550 The filename, directory name, or volume label syntax is incorrect. 
ftp> mget *
mget PRTG Enterprise Console.lnk [anpqy?]? a
Prompting off for duration of mget.
229 Entering Extended Passive Mode (|||52738|)
150 Opening ASCII mode data connection.
100% |******************************************************************|  1195       50.95 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 1 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
1195 bytes received in 00:00 (49.99 KiB/s)
229 Entering Extended Passive Mode (|||52739|)
150 Opening ASCII mode data connection.
100% |******************************************************************|  1160       49.63 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 1 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
1160 bytes received in 00:00 (48.41 KiB/s)
229 Entering Extended Passive Mode (|||52740|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    34        1.43 KiB/s    00:00 ETA
226 Transfer complete.
34 bytes received in 00:00 (1.42 KiB/s)
ftp> dir
421 Service not available, remote server has closed connection.
213 20250516121624
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> cd "Program Files (x86)\PRTG Network Monitor"
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52775|)
150 Opening ASCII mode data connection.
02-03-19  12:17AM       <DIR>          64 bit
02-03-19  12:15AM                 1888 activation.dat
02-03-19  12:18AM       <DIR>          cert
12-14-17  01:40PM              2461696 chartdir51.dll
12-14-17  01:40PM              9077248 ChilkatDelphiXE.dll
12-14-17  01:40PM              2138986 chrome.pak
02-03-19  12:17AM       <DIR>          Custom Sensors
12-14-17  01:40PM               382464 dbexpmda40.dll
12-14-17  01:40PM               519680 dbexpoda40.dll
12-14-17  01:40PM               377856 dbexpsda40.dll
12-14-17  01:40PM                 5681 defaultmaps.xml
12-14-17  01:40PM                12871 defaultmaps_iad.xml
02-13-18  03:08PM                 1224 deviceiconlist.txt
02-03-19  12:17AM       <DIR>          devicetemplates
05-16-25  08:15AM       <DIR>          dlltemp
02-03-19  12:18AM       <DIR>          download
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 6218 FlowRules.osr
02-03-19  12:18AM       <DIR>          helperlibs
12-14-17  01:40PM              9956864 icudt.dll
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-03-19  12:16AM       <DIR>          language
12-14-17  01:40PM              3707349 Lb2to3.exe
12-14-17  01:40PM             24978944 libcef.dll
12-14-17  01:40PM              1412096 libeay32.dll
02-03-19  12:17AM       <DIR>          locales
02-03-19  12:18AM       <DIR>          lookups
02-16-18  11:03AM               796566 macmanufacturerlist.txt
02-03-19  12:18AM       <DIR>          MIB
12-14-17  01:40PM                  522 Microsoft.VC80.CRT.manifest
12-14-17  01:40PM               421200 msvcp100.dll
12-14-17  01:40PM               770384 msvcr100.dll
12-14-17  01:40PM               630544 msvcr80.dll
12-14-17  01:40PM                12498 netsnmp-license.txt
02-03-19  12:17AM       <DIR>          Notifications
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM               487936 openssl.exe
01-18-18  11:03AM               177152 paelibssh.dll
12-14-17  01:40PM                35088 paesslerchart.dll
12-14-17  01:40PM              1083904 PaesslerSNMP.dll
02-15-18  05:24PM              1074688 PaesslerSNMPWrapper.dll
12-14-17  01:40PM               421160 PaesslerSQLEngine.dll
12-14-17  01:40PM               193832 PaesslerSQLEngineDBX.dll
12-14-17  01:40PM               331536 paesslerVMWareShell.exe
12-14-17  01:40PM               310032 paesslerVMWareShell.vshost.exe
12-14-17  01:40PM                 1429 phantomjs-license.bsd
12-14-17  01:40PM                 1428 protocol.txt
02-16-18  11:04AM              6379096 PRTG Administrator.exe
02-16-18  11:05AM             12923480 PRTG Enterprise Console.exe
02-16-18  11:04AM              5439576 PRTG GUI Starter.exe
02-03-19  12:17AM       <DIR>          PRTG Installer Archive
02-16-18  11:05AM             11647576 PRTG Probe.exe
02-16-18  11:05AM              7026776 PRTG Server.exe
02-03-19  12:18AM              2000256 PRTG Setup Log.log
02-03-19  12:17AM       <DIR>          prtg-installer-for-distribution
12-14-17  01:40PM               300318 prtg.ico
12-14-17  01:40PM               444640 PrtgDllWrapper.exe
02-16-18  11:04AM              2778200 PRTGProbeUpdate.exe
02-16-18  11:04AM              3227224 PrtgRemoteInstall.exe
02-16-18  11:04AM              2782808 PRTGServerUpdate.exe
02-16-18  11:04AM              2104408 PRTG_Chromium_Helper.exe
02-16-18  11:04AM              2264664 PRTG_IE_Helper.exe
02-03-19  12:17AM       <DIR>          Python34
02-16-18  11:04AM              1012224 RegWrapper.exe
02-03-19  12:17AM       <DIR>          Sensor System
02-03-19  12:17AM       <DIR>          snmplibs
02-03-19  12:18AM       <DIR>          snmptemp
01-18-18  11:03AM               461824 ssh.dll
12-14-17  01:40PM               384512 ssleay32.dll
02-03-19  12:18AM       <DIR>          themes
02-03-19  12:18AM              1275563 unins000.dat
02-03-19  12:15AM              1498815 unins000.exe
12-14-17  01:40PM              1163024 VimService2005.dll
12-14-17  01:40PM              4312848 VimService2005.XmlSerializers.dll
02-03-19  12:17AM       <DIR>          webroot
226 Transfer complete.
ftp> get "PRTG Setup Log.log"
local: PRTG Setup Log.log remote: PRTG Setup Log.log
229 Entering Extended Passive Mode (|||52786|)
150 Opening ASCII mode data connection.
100% |******************************************************************|  1953 KiB    3.68 MiB/s    00:00 ETA
226 Transfer complete.
2000256 bytes received in 00:00 (3.68 MiB/s)
ftp> cd webroot
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52805|)
125 Data connection already open; Transfer starting.
12-14-17  01:40PM                   68 acknowledgealarm.htm
12-14-17  01:40PM                 2614 activation.htm
12-14-17  01:40PM                 1723 addautodiscovery.htm
12-14-17  01:40PM                 4276 addautodiscovery0.htm
12-14-17  01:40PM                 1525 adddevice.htm
12-14-17  01:40PM                 5862 adddevice0.htm
12-14-17  01:40PM                  144 adddevice2.htm
12-14-17  01:40PM                 2009 addgroup.htm
12-14-17  01:40PM                 4087 addgroup0.htm
12-14-17  01:40PM                  143 addgroup2.htm
12-14-17  01:40PM                 2103 addlibrary.htm
12-14-17  01:40PM                 6126 addmap.htm
12-14-17  01:40PM                  115 addmap2.htm
12-14-17  01:40PM                 1549 addreport.htm
02-16-18  11:06AM                 7856 addsensor.htm
12-14-17  01:40PM                 6264 addsensor0.htm
12-14-17  01:40PM                 3186 addsensor4.htm
12-14-17  01:40PM                  169 addsensor5.htm
12-14-17  01:40PM                 8209 addsensorfailed.htm
12-14-17  01:40PM                 2166 addticket.htm
12-14-17  01:40PM                 4728 addticket0.htm
12-14-17  01:40PM                 2386 alarms.htm
12-14-17  01:40PM                 2424 alarmsgauges.htm
02-03-19  12:16AM       <DIR>          api
12-14-17  01:40PM                 5618 api.htm
12-14-17  01:40PM                 1232 apple-touch-icon.png
12-14-17  01:40PM                  739 autodiscoverytemplate.htm
12-14-17  01:40PM                 3203 autoupdate.htm
12-14-17  01:40PM                13368 colors.htm
12-14-17  01:40PM                 1296 compare.htm
12-14-17  01:40PM                 1696 compares.htm
12-14-17  01:40PM                  791 config_report_maps.htm
12-14-17  01:40PM                  811 config_report_object.htm
12-14-17  01:40PM                  892 config_report_reports.htm
12-14-17  01:40PM                  391 config_report_systemconfig.htm
12-14-17  01:40PM                 1189 config_report_users.htm
02-03-19  12:16AM       <DIR>          controls
01-11-18  06:05PM                 5451 createtemplate.htm
02-03-19  12:17AM       <DIR>          css
12-14-17  01:40PM                 2732 deleteobject.htm
12-14-17  01:40PM                 1492 deleteobjects.htm
12-14-17  01:40PM                   50 deletesub.htm
02-07-18  04:58PM                 1851 dependencies.htm
02-16-18  11:06AM                 5198 device.htm
12-14-17  01:40PM                 8902 deviceprobeinstall.htm
12-14-17  01:40PM                 1040 devices-qr.htm
12-14-17  01:40PM                 2375 devices.htm
12-14-17  01:40PM                  395 displayrights.htm
12-14-17  01:40PM                 2804 downloads.htm
12-14-17  01:40PM                 6173 duplicatedevice.htm
12-14-17  01:40PM                 4941 duplicategroup.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                 5399 duplicatesensor.htm
12-14-17  01:40PM                 3493 editnotification.htm
12-14-17  01:40PM                 3043 editrights.htm
12-14-17  01:40PM                 2834 editschedule.htm
12-14-17  01:40PM                 1648 editticket.htm
12-14-17  01:40PM                 3386 edituser.htm
12-14-17  01:40PM                 3247 editusergroup.htm
12-14-17  01:40PM                 2811 error.htm
12-14-17  01:40PM                 1032 errorreport.htm
12-14-17  01:40PM                 1150 favicon.ico
12-14-17  01:40PM                 1681 filter.htm
12-14-17  01:40PM                  873 generatehistoricdata.htm
12-14-17  01:40PM                  718 generatereport.htm
12-27-17  12:17PM                 3080 geomap.htm
12-14-17  01:40PM                  397 geomapdevices.htm
12-14-17  01:40PM                  768 geomap_static.htm
12-14-17  01:40PM                 1574 gotoserviceurl.htm
12-14-17  01:40PM                 1570 graphzoom.htm
12-14-17  01:40PM                 2022 graphzoomtoplist.htm
02-16-18  11:01AM                 5987 group.htm
12-22-17  09:32AM                 2248 healtherrors.htm
02-03-19  12:17AM       <DIR>          help
12-14-17  01:40PM                 9823 help.htm
01-11-18  03:21PM                14537 historicdata.htm
12-14-17  01:40PM                 2746 historicdata_html.htm
02-03-19  12:16AM       <DIR>          icons
02-03-19  12:16AM       <DIR>          images
02-03-19  12:17AM       <DIR>          includes
12-14-17  01:40PM                  153 index.htm
02-03-19  12:17AM       <DIR>          javascript
12-14-17  01:40PM                 1005 jstests.htm
12-14-17  01:40PM                 3131 libraries.htm
12-14-17  01:40PM                 3771 library.htm
12-14-17  01:40PM                 2955 libraryobject.htm
12-14-17  01:40PM                 1333 library_static.htm
12-14-17  01:40PM                 2234 licensing.htm
12-14-17  01:40PM                 1476 log.htm
02-03-19  12:16AM       <DIR>          mailtemplates
12-14-17  01:40PM                 4045 map.htm
02-01-18  02:04PM                  820 mapdashboard.htm
02-03-19  12:16AM       <DIR>          mapicons
02-03-19  12:17AM       <DIR>          mapobjects
02-16-18  11:06AM                 3293 maps.htm
12-14-17  01:40PM                 5997 mapshow.htm
12-14-17  01:40PM                 3725 mapshow_simple.htm
12-14-17  01:40PM                  439 mapshow_static.htm
12-14-17  01:40PM                 4860 moveobject.htm
12-14-17  01:40PM                   97 moveobjectnow.htm
12-14-17  01:40PM                 3195 multiedit.htm
12-14-17  01:40PM                 2480 multiinlineedit.htm
12-14-17  01:40PM                 3121 myaccount.htm
12-14-17  01:40PM                 2604 objecthistory.htm
12-14-17  01:40PM                 1661 objectusedby.htm
12-14-17  01:40PM                  899 openwindow.htm
12-14-17  01:40PM                79987 package-lock.json
12-14-17  01:40PM                   61 pause.htm
12-14-17  01:40PM                   64 pauseobjectfor.htm
02-16-18  11:06AM                 4798 probenode.htm
02-03-19  12:18AM                    0 prtg_trial_user_survey.txt
02-03-19  12:17AM       <DIR>          public
12-14-17  01:40PM                  262 remotedesktop.rdp
12-14-17  01:40PM                 4244 remoteprobeinstall.htm
12-14-17  01:40PM                 4266 report.htm
12-14-17  01:40PM                 2989 reports.htm
02-03-19  12:17AM       <DIR>          reporttemplates
12-14-17  01:40PM                 1634 salesbundle_send.htm
12-14-17  01:40PM                   63 scannow.htm
12-14-17  01:40PM                 2266 search.htm
12-14-17  01:40PM                 1742 searchdetailed.htm
12-14-17  01:40PM                  810 sendbdmfeedback.htm
12-14-17  01:40PM                  798 sendfeedback.htm
12-14-17  01:40PM                  812 sendsalesfeedback.htm
12-14-17  01:40PM                 5966 sensor.htm
12-14-17  01:40PM                 2593 sensors.htm
12-14-17  01:40PM                 2171 sensorxref.htm
12-14-17  01:40PM                 1772 setup.htm
02-16-18  11:06AM                 2172 similarsensors.htm
02-03-19  12:17AM       <DIR>          sounds
12-14-17  01:40PM                10602 speedtest.htm
01-22-18  11:55AM                10870 start.htm
12-14-17  01:40PM                 2021 status.htm
12-14-17  01:40PM                 1651 supportbundle_send.htm
12-14-17  01:40PM                 4759 systemsetup.htm
12-14-17  01:40PM                  587 tablewithstyles.htm
12-14-17  01:40PM                11780 tct-overview.htm
12-14-17  01:40PM                 6509 tct-toggle.htm
12-14-17  01:40PM                   28 testjson.htm
12-14-17  01:40PM                69758 testsuite.htm
12-14-17  01:40PM                 1883 ticket.htm
12-14-17  01:40PM                 3191 tickets.htm
02-03-19  12:16AM       <DIR>          tickettemplates
12-14-17  01:40PM                 1729 top10.htm
12-14-17  01:40PM                 4208 toplist.htm
12-14-17  01:40PM                 2886 toplistprint.htm
12-14-17  01:40PM                 2431 traceroute.htm
12-14-17  01:40PM                 1058 trialsurvey.htm
12-14-17  01:40PM                 5028 udc_ui_android.htm
12-14-17  01:40PM                 5028 udc_ui_mac.htm
12-14-17  01:40PM                 5028 udc_ui_win.htm
12-14-17  01:40PM                 5544 welcome.htm
12-14-17  01:40PM                 5181 wingui.htm
12-14-17  01:40PM                 1306 you_should_use_ssl.htm
226 Transfer complete.
ftp> get mapdashboard.htm
local: mapdashboard.htm remote: mapdashboard.htm
229 Entering Extended Passive Mode (|||52882|)
150 Opening ASCII mode data connection.
100% |******************************************************************|   820       34.79 KiB/s    00:00 ETA
226 Transfer complete.
820 bytes received in 00:00 (34.37 KiB/s)
ftp> mget *
421 Service not available, remote server has closed connection.
ftp> exit
                                                                                                               
┌──(kali㉿proxli)-[~/boxes/htb/netmon]
└─$ ftp 10.10.10.152
Connected to 10.10.10.152.
220 Microsoft FTP Service
Name (10.10.10.152:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> cd "Program Files (x86)\PRTG Network Monitor"
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52921|)
150 Opening ASCII mode data connection.
02-03-19  12:17AM       <DIR>          64 bit
02-03-19  12:15AM                 1888 activation.dat
02-03-19  12:18AM       <DIR>          cert
12-14-17  01:40PM              2461696 chartdir51.dll
12-14-17  01:40PM              9077248 ChilkatDelphiXE.dll
12-14-17  01:40PM              2138986 chrome.pak
02-03-19  12:17AM       <DIR>          Custom Sensors
12-14-17  01:40PM               382464 dbexpmda40.dll
12-14-17  01:40PM               519680 dbexpoda40.dll
12-14-17  01:40PM               377856 dbexpsda40.dll
12-14-17  01:40PM                 5681 defaultmaps.xml
12-14-17  01:40PM                12871 defaultmaps_iad.xml
02-13-18  03:08PM                 1224 deviceiconlist.txt
02-03-19  12:17AM       <DIR>          devicetemplates
05-16-25  08:15AM       <DIR>          dlltemp
02-03-19  12:18AM       <DIR>          download
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 6218 FlowRules.osr
02-03-19  12:18AM       <DIR>          helperlibs
12-14-17  01:40PM              9956864 icudt.dll
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-03-19  12:16AM       <DIR>          language
12-14-17  01:40PM              3707349 Lb2to3.exe
12-14-17  01:40PM             24978944 libcef.dll
12-14-17  01:40PM              1412096 libeay32.dll
02-03-19  12:17AM       <DIR>          locales
02-03-19  12:18AM       <DIR>          lookups
02-16-18  11:03AM               796566 macmanufacturerlist.txt
02-03-19  12:18AM       <DIR>          MIB
12-14-17  01:40PM                  522 Microsoft.VC80.CRT.manifest
12-14-17  01:40PM               421200 msvcp100.dll
12-14-17  01:40PM               770384 msvcr100.dll
12-14-17  01:40PM               630544 msvcr80.dll
12-14-17  01:40PM                12498 netsnmp-license.txt
02-03-19  12:17AM       <DIR>          Notifications
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM               487936 openssl.exe
01-18-18  11:03AM               177152 paelibssh.dll
12-14-17  01:40PM                35088 paesslerchart.dll
12-14-17  01:40PM              1083904 PaesslerSNMP.dll
02-15-18  05:24PM              1074688 PaesslerSNMPWrapper.dll
12-14-17  01:40PM               421160 PaesslerSQLEngine.dll
12-14-17  01:40PM               193832 PaesslerSQLEngineDBX.dll
12-14-17  01:40PM               331536 paesslerVMWareShell.exe
12-14-17  01:40PM               310032 paesslerVMWareShell.vshost.exe
12-14-17  01:40PM                 1429 phantomjs-license.bsd
12-14-17  01:40PM                 1428 protocol.txt
02-16-18  11:04AM              6379096 PRTG Administrator.exe
02-16-18  11:05AM             12923480 PRTG Enterprise Console.exe
02-16-18  11:04AM              5439576 PRTG GUI Starter.exe
02-03-19  12:17AM       <DIR>          PRTG Installer Archive
02-16-18  11:05AM             11647576 PRTG Probe.exe
02-16-18  11:05AM              7026776 PRTG Server.exe
02-03-19  12:18AM              2000256 PRTG Setup Log.log
02-03-19  12:17AM       <DIR>          prtg-installer-for-distribution
12-14-17  01:40PM               300318 prtg.ico
12-14-17  01:40PM               444640 PrtgDllWrapper.exe
02-16-18  11:04AM              2778200 PRTGProbeUpdate.exe
02-16-18  11:04AM              3227224 PrtgRemoteInstall.exe
02-16-18  11:04AM              2782808 PRTGServerUpdate.exe
02-16-18  11:04AM              2104408 PRTG_Chromium_Helper.exe
02-16-18  11:04AM              2264664 PRTG_IE_Helper.exe
02-03-19  12:17AM       <DIR>          Python34
02-16-18  11:04AM              1012224 RegWrapper.exe
02-03-19  12:17AM       <DIR>          Sensor System
02-03-19  12:17AM       <DIR>          snmplibs
02-03-19  12:18AM       <DIR>          snmptemp
01-18-18  11:03AM               461824 ssh.dll
12-14-17  01:40PM               384512 ssleay32.dll
02-03-19  12:18AM       <DIR>          themes
02-03-19  12:18AM              1275563 unins000.dat
02-03-19  12:15AM              1498815 unins000.exe
12-14-17  01:40PM              1163024 VimService2005.dll
12-14-17  01:40PM              4312848 VimService2005.XmlSerializers.dll
02-03-19  12:17AM       <DIR>          webroot
226 Transfer complete.
ftp> cd webroot
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52929|)
125 Data connection already open; Transfer starting.
12-14-17  01:40PM                   68 acknowledgealarm.htm
12-14-17  01:40PM                 2614 activation.htm
12-14-17  01:40PM                 1723 addautodiscovery.htm
12-14-17  01:40PM                 4276 addautodiscovery0.htm
12-14-17  01:40PM                 1525 adddevice.htm
12-14-17  01:40PM                 5862 adddevice0.htm
12-14-17  01:40PM                  144 adddevice2.htm
12-14-17  01:40PM                 2009 addgroup.htm
12-14-17  01:40PM                 4087 addgroup0.htm
12-14-17  01:40PM                  143 addgroup2.htm
12-14-17  01:40PM                 2103 addlibrary.htm
12-14-17  01:40PM                 6126 addmap.htm
12-14-17  01:40PM                  115 addmap2.htm
12-14-17  01:40PM                 1549 addreport.htm
02-16-18  11:06AM                 7856 addsensor.htm
12-14-17  01:40PM                 6264 addsensor0.htm
12-14-17  01:40PM                 3186 addsensor4.htm
12-14-17  01:40PM                  169 addsensor5.htm
12-14-17  01:40PM                 8209 addsensorfailed.htm
12-14-17  01:40PM                 2166 addticket.htm
12-14-17  01:40PM                 4728 addticket0.htm
12-14-17  01:40PM                 2386 alarms.htm
12-14-17  01:40PM                 2424 alarmsgauges.htm
02-03-19  12:16AM       <DIR>          api
12-14-17  01:40PM                 5618 api.htm
12-14-17  01:40PM                 1232 apple-touch-icon.png
12-14-17  01:40PM                  739 autodiscoverytemplate.htm
12-14-17  01:40PM                 3203 autoupdate.htm
12-14-17  01:40PM                13368 colors.htm
12-14-17  01:40PM                 1296 compare.htm
12-14-17  01:40PM                 1696 compares.htm
12-14-17  01:40PM                  791 config_report_maps.htm
12-14-17  01:40PM                  811 config_report_object.htm
12-14-17  01:40PM                  892 config_report_reports.htm
12-14-17  01:40PM                  391 config_report_systemconfig.htm
12-14-17  01:40PM                 1189 config_report_users.htm
02-03-19  12:16AM       <DIR>          controls
01-11-18  06:05PM                 5451 createtemplate.htm
02-03-19  12:17AM       <DIR>          css
12-14-17  01:40PM                 2732 deleteobject.htm
12-14-17  01:40PM                 1492 deleteobjects.htm
12-14-17  01:40PM                   50 deletesub.htm
02-07-18  04:58PM                 1851 dependencies.htm
02-16-18  11:06AM                 5198 device.htm
12-14-17  01:40PM                 8902 deviceprobeinstall.htm
12-14-17  01:40PM                 1040 devices-qr.htm
12-14-17  01:40PM                 2375 devices.htm
12-14-17  01:40PM                  395 displayrights.htm
12-14-17  01:40PM                 2804 downloads.htm
12-14-17  01:40PM                 6173 duplicatedevice.htm
12-14-17  01:40PM                 4941 duplicategroup.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                 5399 duplicatesensor.htm
12-14-17  01:40PM                 3493 editnotification.htm
12-14-17  01:40PM                 3043 editrights.htm
12-14-17  01:40PM                 2834 editschedule.htm
12-14-17  01:40PM                 1648 editticket.htm
12-14-17  01:40PM                 3386 edituser.htm
12-14-17  01:40PM                 3247 editusergroup.htm
12-14-17  01:40PM                 2811 error.htm
12-14-17  01:40PM                 1032 errorreport.htm
12-14-17  01:40PM                 1150 favicon.ico
12-14-17  01:40PM                 1681 filter.htm
12-14-17  01:40PM                  873 generatehistoricdata.htm
12-14-17  01:40PM                  718 generatereport.htm
12-27-17  12:17PM                 3080 geomap.htm
12-14-17  01:40PM                  397 geomapdevices.htm
12-14-17  01:40PM                  768 geomap_static.htm
12-14-17  01:40PM                 1574 gotoserviceurl.htm
12-14-17  01:40PM                 1570 graphzoom.htm
12-14-17  01:40PM                 2022 graphzoomtoplist.htm
02-16-18  11:01AM                 5987 group.htm
12-22-17  09:32AM                 2248 healtherrors.htm
02-03-19  12:17AM       <DIR>          help
12-14-17  01:40PM                 9823 help.htm
01-11-18  03:21PM                14537 historicdata.htm
12-14-17  01:40PM                 2746 historicdata_html.htm
02-03-19  12:16AM       <DIR>          icons
02-03-19  12:16AM       <DIR>          images
02-03-19  12:17AM       <DIR>          includes
12-14-17  01:40PM                  153 index.htm
02-03-19  12:17AM       <DIR>          javascript
12-14-17  01:40PM                 1005 jstests.htm
12-14-17  01:40PM                 3131 libraries.htm
12-14-17  01:40PM                 3771 library.htm
12-14-17  01:40PM                 2955 libraryobject.htm
12-14-17  01:40PM                 1333 library_static.htm
12-14-17  01:40PM                 2234 licensing.htm
12-14-17  01:40PM                 1476 log.htm
02-03-19  12:16AM       <DIR>          mailtemplates
12-14-17  01:40PM                 4045 map.htm
02-01-18  02:04PM                  820 mapdashboard.htm
02-03-19  12:16AM       <DIR>          mapicons
02-03-19  12:17AM       <DIR>          mapobjects
02-16-18  11:06AM                 3293 maps.htm
12-14-17  01:40PM                 5997 mapshow.htm
12-14-17  01:40PM                 3725 mapshow_simple.htm
12-14-17  01:40PM                  439 mapshow_static.htm
12-14-17  01:40PM                 4860 moveobject.htm
12-14-17  01:40PM                   97 moveobjectnow.htm
12-14-17  01:40PM                 3195 multiedit.htm
12-14-17  01:40PM                 2480 multiinlineedit.htm
12-14-17  01:40PM                 3121 myaccount.htm
12-14-17  01:40PM                 2604 objecthistory.htm
12-14-17  01:40PM                 1661 objectusedby.htm
12-14-17  01:40PM                  899 openwindow.htm
12-14-17  01:40PM                79987 package-lock.json
12-14-17  01:40PM                   61 pause.htm
12-14-17  01:40PM                   64 pauseobjectfor.htm
02-16-18  11:06AM                 4798 probenode.htm
02-03-19  12:18AM                    0 prtg_trial_user_survey.txt
02-03-19  12:17AM       <DIR>          public
12-14-17  01:40PM                  262 remotedesktop.rdp
12-14-17  01:40PM                 4244 remoteprobeinstall.htm
12-14-17  01:40PM                 4266 report.htm
12-14-17  01:40PM                 2989 reports.htm
02-03-19  12:17AM       <DIR>          reporttemplates
12-14-17  01:40PM                 1634 salesbundle_send.htm
12-14-17  01:40PM                   63 scannow.htm
12-14-17  01:40PM                 2266 search.htm
12-14-17  01:40PM                 1742 searchdetailed.htm
12-14-17  01:40PM                  810 sendbdmfeedback.htm
12-14-17  01:40PM                  798 sendfeedback.htm
12-14-17  01:40PM                  812 sendsalesfeedback.htm
12-14-17  01:40PM                 5966 sensor.htm
12-14-17  01:40PM                 2593 sensors.htm
12-14-17  01:40PM                 2171 sensorxref.htm
12-14-17  01:40PM                 1772 setup.htm
02-16-18  11:06AM                 2172 similarsensors.htm
02-03-19  12:17AM       <DIR>          sounds
12-14-17  01:40PM                10602 speedtest.htm
01-22-18  11:55AM                10870 start.htm
12-14-17  01:40PM                 2021 status.htm
12-14-17  01:40PM                 1651 supportbundle_send.htm
12-14-17  01:40PM                 4759 systemsetup.htm
12-14-17  01:40PM                  587 tablewithstyles.htm
12-14-17  01:40PM                11780 tct-overview.htm
12-14-17  01:40PM                 6509 tct-toggle.htm
12-14-17  01:40PM                   28 testjson.htm
12-14-17  01:40PM                69758 testsuite.htm
12-14-17  01:40PM                 1883 ticket.htm
12-14-17  01:40PM                 3191 tickets.htm
02-03-19  12:16AM       <DIR>          tickettemplates
12-14-17  01:40PM                 1729 top10.htm
12-14-17  01:40PM                 4208 toplist.htm
12-14-17  01:40PM                 2886 toplistprint.htm
12-14-17  01:40PM                 2431 traceroute.htm
12-14-17  01:40PM                 1058 trialsurvey.htm
12-14-17  01:40PM                 5028 udc_ui_android.htm
12-14-17  01:40PM                 5028 udc_ui_mac.htm
12-14-17  01:40PM                 5028 udc_ui_win.htm
12-14-17  01:40PM                 5544 welcome.htm
12-14-17  01:40PM                 5181 wingui.htm
12-14-17  01:40PM                 1306 you_should_use_ssl.htm
226 Transfer complete.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52930|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                  617 checklogin.htm
12-14-17  01:40PM                 2392 forgotpassword.htm
12-14-17  01:40PM                11785 local_login.htm
12-14-17  01:40PM                  151 login.htm
12-14-17  01:40PM                  296 manifest.json.htm
12-14-17  01:40PM                 6077 mapshow.htm
12-14-17  01:40PM                  759 mapshowstatic.htm
02-16-18  11:06AM                 8139 mapshow_simple.htm
12-14-17  01:40PM                  593 mapshow_static.htm
02-16-18  11:07AM             18879704 PRTG_Enterprise_Console_Installer.exe
02-16-18  11:08AM             59212432 PRTG_Remote_Probe_Installer.exe
12-14-17  01:40PM                 2083 sendpassword.htm
12-14-17  01:40PM                 4270 sso.login.htm
12-14-17  01:40PM                 3243 sso.login.v7.htm
12-14-17  01:40PM                  714 sso.silentCallback.htm
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52940|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                   68 acknowledgealarm.htm
12-14-17  01:40PM                 2614 activation.htm
12-14-17  01:40PM                 1723 addautodiscovery.htm
12-14-17  01:40PM                 4276 addautodiscovery0.htm
12-14-17  01:40PM                 1525 adddevice.htm
12-14-17  01:40PM                 5862 adddevice0.htm
12-14-17  01:40PM                  144 adddevice2.htm
12-14-17  01:40PM                 2009 addgroup.htm
12-14-17  01:40PM                 4087 addgroup0.htm
12-14-17  01:40PM                  143 addgroup2.htm
12-14-17  01:40PM                 2103 addlibrary.htm
12-14-17  01:40PM                 6126 addmap.htm
12-14-17  01:40PM                  115 addmap2.htm
12-14-17  01:40PM                 1549 addreport.htm
02-16-18  11:06AM                 7856 addsensor.htm
12-14-17  01:40PM                 6264 addsensor0.htm
12-14-17  01:40PM                 3186 addsensor4.htm
12-14-17  01:40PM                  169 addsensor5.htm
12-14-17  01:40PM                 8209 addsensorfailed.htm
12-14-17  01:40PM                 2166 addticket.htm
12-14-17  01:40PM                 4728 addticket0.htm
12-14-17  01:40PM                 2386 alarms.htm
12-14-17  01:40PM                 2424 alarmsgauges.htm
02-03-19  12:16AM       <DIR>          api
12-14-17  01:40PM                 5618 api.htm
12-14-17  01:40PM                 1232 apple-touch-icon.png
12-14-17  01:40PM                  739 autodiscoverytemplate.htm
12-14-17  01:40PM                 3203 autoupdate.htm
12-14-17  01:40PM                13368 colors.htm
12-14-17  01:40PM                 1296 compare.htm
12-14-17  01:40PM                 1696 compares.htm
12-14-17  01:40PM                  791 config_report_maps.htm
12-14-17  01:40PM                  811 config_report_object.htm
12-14-17  01:40PM                  892 config_report_reports.htm
12-14-17  01:40PM                  391 config_report_systemconfig.htm
12-14-17  01:40PM                 1189 config_report_users.htm
02-03-19  12:16AM       <DIR>          controls
01-11-18  06:05PM                 5451 createtemplate.htm
02-03-19  12:17AM       <DIR>          css
12-14-17  01:40PM                 2732 deleteobject.htm
12-14-17  01:40PM                 1492 deleteobjects.htm
12-14-17  01:40PM                   50 deletesub.htm
02-07-18  04:58PM                 1851 dependencies.htm
02-16-18  11:06AM                 5198 device.htm
12-14-17  01:40PM                 8902 deviceprobeinstall.htm
12-14-17  01:40PM                 1040 devices-qr.htm
12-14-17  01:40PM                 2375 devices.htm
12-14-17  01:40PM                  395 displayrights.htm
12-14-17  01:40PM                 2804 downloads.htm
12-14-17  01:40PM                 6173 duplicatedevice.htm
12-14-17  01:40PM                 4941 duplicategroup.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                 5399 duplicatesensor.htm
12-14-17  01:40PM                 3493 editnotification.htm
12-14-17  01:40PM                 3043 editrights.htm
12-14-17  01:40PM                 2834 editschedule.htm
12-14-17  01:40PM                 1648 editticket.htm
12-14-17  01:40PM                 3386 edituser.htm
12-14-17  01:40PM                 3247 editusergroup.htm
12-14-17  01:40PM                 2811 error.htm
12-14-17  01:40PM                 1032 errorreport.htm
12-14-17  01:40PM                 1150 favicon.ico
12-14-17  01:40PM                 1681 filter.htm
12-14-17  01:40PM                  873 generatehistoricdata.htm
12-14-17  01:40PM                  718 generatereport.htm
12-27-17  12:17PM                 3080 geomap.htm
12-14-17  01:40PM                  397 geomapdevices.htm
12-14-17  01:40PM                  768 geomap_static.htm
12-14-17  01:40PM                 1574 gotoserviceurl.htm
12-14-17  01:40PM                 1570 graphzoom.htm
12-14-17  01:40PM                 2022 graphzoomtoplist.htm
02-16-18  11:01AM                 5987 group.htm
12-22-17  09:32AM                 2248 healtherrors.htm
02-03-19  12:17AM       <DIR>          help
12-14-17  01:40PM                 9823 help.htm
01-11-18  03:21PM                14537 historicdata.htm
12-14-17  01:40PM                 2746 historicdata_html.htm
02-03-19  12:16AM       <DIR>          icons
02-03-19  12:16AM       <DIR>          images
02-03-19  12:17AM       <DIR>          includes
12-14-17  01:40PM                  153 index.htm
02-03-19  12:17AM       <DIR>          javascript
12-14-17  01:40PM                 1005 jstests.htm
12-14-17  01:40PM                 3131 libraries.htm
12-14-17  01:40PM                 3771 library.htm
12-14-17  01:40PM                 2955 libraryobject.htm
12-14-17  01:40PM                 1333 library_static.htm
12-14-17  01:40PM                 2234 licensing.htm
12-14-17  01:40PM                 1476 log.htm
02-03-19  12:16AM       <DIR>          mailtemplates
12-14-17  01:40PM                 4045 map.htm
02-01-18  02:04PM                  820 mapdashboard.htm
02-03-19  12:16AM       <DIR>          mapicons
02-03-19  12:17AM       <DIR>          mapobjects
02-16-18  11:06AM                 3293 maps.htm
12-14-17  01:40PM                 5997 mapshow.htm
12-14-17  01:40PM                 3725 mapshow_simple.htm
12-14-17  01:40PM                  439 mapshow_static.htm
12-14-17  01:40PM                 4860 moveobject.htm
12-14-17  01:40PM                   97 moveobjectnow.htm
12-14-17  01:40PM                 3195 multiedit.htm
12-14-17  01:40PM                 2480 multiinlineedit.htm
12-14-17  01:40PM                 3121 myaccount.htm
12-14-17  01:40PM                 2604 objecthistory.htm
12-14-17  01:40PM                 1661 objectusedby.htm
12-14-17  01:40PM                  899 openwindow.htm
12-14-17  01:40PM                79987 package-lock.json
12-14-17  01:40PM                   61 pause.htm
12-14-17  01:40PM                   64 pauseobjectfor.htm
02-16-18  11:06AM                 4798 probenode.htm
02-03-19  12:18AM                    0 prtg_trial_user_survey.txt
02-03-19  12:17AM       <DIR>          public
12-14-17  01:40PM                  262 remotedesktop.rdp
12-14-17  01:40PM                 4244 remoteprobeinstall.htm
12-14-17  01:40PM                 4266 report.htm
12-14-17  01:40PM                 2989 reports.htm
02-03-19  12:17AM       <DIR>          reporttemplates
12-14-17  01:40PM                 1634 salesbundle_send.htm
12-14-17  01:40PM                   63 scannow.htm
12-14-17  01:40PM                 2266 search.htm
12-14-17  01:40PM                 1742 searchdetailed.htm
12-14-17  01:40PM                  810 sendbdmfeedback.htm
12-14-17  01:40PM                  798 sendfeedback.htm
12-14-17  01:40PM                  812 sendsalesfeedback.htm
12-14-17  01:40PM                 5966 sensor.htm
12-14-17  01:40PM                 2593 sensors.htm
12-14-17  01:40PM                 2171 sensorxref.htm
12-14-17  01:40PM                 1772 setup.htm
02-16-18  11:06AM                 2172 similarsensors.htm
02-03-19  12:17AM       <DIR>          sounds
12-14-17  01:40PM                10602 speedtest.htm
01-22-18  11:55AM                10870 start.htm
12-14-17  01:40PM                 2021 status.htm
12-14-17  01:40PM                 1651 supportbundle_send.htm
12-14-17  01:40PM                 4759 systemsetup.htm
12-14-17  01:40PM                  587 tablewithstyles.htm
12-14-17  01:40PM                11780 tct-overview.htm
12-14-17  01:40PM                 6509 tct-toggle.htm
12-14-17  01:40PM                   28 testjson.htm
12-14-17  01:40PM                69758 testsuite.htm
12-14-17  01:40PM                 1883 ticket.htm
12-14-17  01:40PM                 3191 tickets.htm
02-03-19  12:16AM       <DIR>          tickettemplates
12-14-17  01:40PM                 1729 top10.htm
12-14-17  01:40PM                 4208 toplist.htm
12-14-17  01:40PM                 2886 toplistprint.htm
12-14-17  01:40PM                 2431 traceroute.htm
12-14-17  01:40PM                 1058 trialsurvey.htm
12-14-17  01:40PM                 5028 udc_ui_android.htm
12-14-17  01:40PM                 5028 udc_ui_mac.htm
12-14-17  01:40PM                 5028 udc_ui_win.htm
12-14-17  01:40PM                 5544 welcome.htm
12-14-17  01:40PM                 5181 wingui.htm
12-14-17  01:40PM                 1306 you_should_use_ssl.htm
226 Transfer complete.
ftp> cd api
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52941|)
125 Data connection already open; Transfer starting.
12-14-17  01:40PM                   67 acknowledgealarm.htm
12-14-17  01:40PM                   48 acktodo.htm
12-14-17  01:40PM                  146 adddevice.htm
12-14-17  01:40PM                  145 addgroup.htm
12-14-17  01:40PM                   61 addobjecttomap.htm
12-14-17  01:40PM                  156 addsensor.htm
12-14-17  01:40PM                   91 addticket.htm
12-14-17  01:40PM                   49 addusers.htm
12-14-17  01:40PM                   28 assignticket.htm
12-14-17  01:40PM                   35 authzclientid.htm
12-14-17  01:40PM                   33 authzdomain.htm
12-14-17  01:40PM                  487 autoupdatedownload.htm
12-14-17  01:40PM                   82 autoupdateinstall.htm
12-14-17  01:40PM                   32 chartlegend.json
12-14-17  01:40PM                   32 clearcache.htm
12-14-17  01:40PM                   27 closeticket.htm
12-14-17  01:40PM                   22 cluster.json
12-14-17  01:40PM                   33 createsupportbundle.htm
12-14-17  01:40PM                   80 createtemplate.htm
12-14-17  01:40PM                   32 debugtracker.htm
12-14-17  01:40PM                   64 defaultpw.htm
12-14-17  01:40PM                  104 deleteobject.htm
12-14-17  01:40PM                  101 deletesubobject.htm
12-14-17  01:40PM                   66 discovernow.htm
12-14-17  01:40PM                   80 dontshowhomenagscreen.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                   63 editmapobject.htm
12-14-17  01:40PM                   26 editticket.htm
12-14-17  01:40PM                   54 error.htm
12-14-17  01:40PM                   63 fave.htm
12-14-17  01:40PM                  601 findduplicates.htm
12-14-17  01:40PM                   20 flowmessagelist.json
12-14-17  01:40PM                   29 foldobject.htm
12-14-17  01:40PM                   40 genreport.htm
12-14-17  01:40PM                   11 geolocator.htm
12-14-17  01:40PM                   51 geomarkers.json
12-14-17  01:40PM                   63 geoprovider.json
12-14-17  01:40PM                  158 getaddsensorprogress.htm
12-14-17  01:40PM                  258 getobjectproperty.htm
12-14-17  01:40PM                  211 getobjectstatus.htm
12-14-17  01:40PM                   28 getpasshash.htm
12-14-17  01:40PM                 1901 getsensordetails.json
12-14-17  01:40PM                 2407 getsensordetails.xml
12-14-17  01:40PM                   31 getsensortypes.htm
12-14-17  01:40PM                   20 getserverurl.htm
12-14-17  01:40PM                   31 getserverurlwithdnsname.htm
12-14-17  01:40PM                 2576 getstatus.htm
12-14-17  01:40PM                 1473 getstatus.xml
12-14-17  01:40PM                   32 getticketmessage.htm
12-14-17  01:40PM                   31 getticketstatus.htm
12-14-17  01:40PM                   54 gettreeasjson.htm
12-14-17  01:40PM                 2005 gettreenodestats.xml
12-14-17  01:40PM                   64 hidechanneltabtip.htm
12-14-17  01:40PM                   59 hidesslnagscreen.htm
12-14-17  01:40PM                  263 historicdata.csv
12-14-17  01:40PM                  259 historicdata.json
12-14-17  01:40PM                  258 historicdata.xml
12-14-17  01:40PM                 2619 historicdata_totals.xml
12-14-17  01:40PM                   42 initialmailacknowledge.htm
12-14-17  01:40PM                   28 language.htm
12-14-17  01:40PM                   58 lastconfigsavetime.htm
12-14-17  01:40PM                  451 libraryname.json
12-14-17  01:40PM                  210 license.json
12-14-17  01:40PM                   35 LiveChatEnabled.htm
12-14-17  01:40PM                   38 loadlookups.htm
12-14-17  01:40PM                   29 logajax.htm
12-14-17  01:40PM                  109 maphistorydata.htm
12-14-17  01:40PM                   36 mapobject.json
12-14-17  01:40PM                   43 mapobjectli.htm
12-14-17  01:40PM                   78 mapobjects.htm
12-14-17  01:40PM                   52 mapsettings.htm
12-14-17  01:40PM                  183 mapsvg.htm
12-14-17  01:40PM                  142 maptree.json
12-14-17  01:40PM                   97 moveobject.htm
12-14-17  01:40PM                   53 moveobjectsimple.htm
12-14-17  01:40PM                   69 newpasshash.htm
12-14-17  01:40PM                   51 newtrigger.htm
12-14-17  01:40PM                   57 newtrigger.json
12-14-17  01:40PM                   25 nodechilds.json
12-14-17  01:40PM                   58 notificationtest.htm
12-14-17  01:40PM                   70 notificationtest.json
12-14-17  01:40PM                   31 objectlist.json
12-14-17  01:40PM                 2915 objectstatus.json
12-14-17  01:40PM                  103 ok.htm
12-14-17  01:40PM                   60 pause.htm
12-14-17  01:40PM                   63 pauseobjectfor.htm
12-14-17  01:40PM                  157 percentile.xml
12-14-17  01:40PM                   19 portassertion.htm
12-14-17  01:40PM                  130 preparesensor.htm
12-14-17  01:40PM                   88 preparesensorready.htm
12-14-17  01:40PM                   16 probestate.htm
02-03-19  12:16AM       <DIR>          public
12-14-17  01:40PM                  253 quicksearch.json
12-14-17  01:40PM                  101 recalccache.htm
12-14-17  01:40PM                   20 recommendedconvert.htm
12-14-17  01:40PM                   97 recommendedsensors.json
12-14-17  01:40PM                   67 recommendnow.htm
12-14-17  01:40PM                   45 rediscoverwithcredentials.htm
12-14-17  01:40PM                   38 refreshlicenseinfo.htm
12-14-17  01:40PM                   20 registerpush.htm
12-14-17  01:40PM                   55 reloadfilelists.htm
12-14-17  01:40PM                   72 remoteinstallprobe.htm
12-14-17  01:40PM                   29 rename.htm
12-14-17  01:40PM                   51 reportaddsensor.htm
12-14-17  01:40PM                   75 reportaddsensorchannel.htm
12-14-17  01:40PM                   78 reportdeletesensorchannel.htm
12-14-17  01:40PM                   25 requestudpmessagelist.htm
12-14-17  01:40PM                   40 resetafterpooling.htm
12-14-17  01:40PM                   48 resetnewmessagestimestamp.htm
12-14-17  01:40PM                   29 resolveticket.htm
12-14-17  01:40PM                  103 restartprobes.htm
12-14-17  01:40PM                   57 restartserver.htm
12-14-17  01:40PM                   47 savenow.htm
12-14-17  01:40PM                   62 scannow.htm
12-14-17  01:40PM                   14 search.htm
12-14-17  01:40PM                   38 search.xml
12-14-17  01:40PM                 2512 searchall.json
12-14-17  01:40PM                  849 searchtreeobject.json
12-14-17  01:40PM                  100 sensortest.htm
12-14-17  01:40PM                   52 sensortypes.json
12-14-17  01:40PM                   43 sensortypesinuse.json
12-14-17  01:40PM                   51 setclusterproperty.htm
12-14-17  01:40PM                   36 setcustomerip.htm
12-14-17  01:40PM                   64 setlonlat.htm
12-14-17  01:40PM                   52 setobjectproperty.htm
12-14-17  01:40PM                   65 setposition.htm
12-14-17  01:40PM                   66 setpriority.htm
12-14-17  01:40PM                   32 setshowhelpstatus.htm
12-14-17  01:40PM                   33 setticketpriority.htm
12-14-17  01:40PM                   71 setviewcontent.htm
12-14-17  01:40PM                   34 setviewsize.htm
12-14-17  01:40PM                   63 simulate.htm
12-14-17  01:40PM                   48 sortsubobjects.htm
12-14-17  01:40PM                 2718 status.json
12-14-17  01:40PM                   51 switchtossl.htm
12-14-17  01:40PM                   12 sysinfo.json
12-14-17  01:40PM                   56 sysinfochecknow.json
12-14-17  01:40PM                  149 table.csv
12-14-17  01:40PM                  147 table.json
12-14-17  01:40PM                  145 table.xml
12-14-17  01:40PM                   58 tctAction.htm
12-14-17  01:40PM                   11 tiles.htm
12-14-17  01:40PM                  235 toplist.json
12-14-17  01:40PM                   69 toplistdelete.htm
12-14-17  01:40PM                  105 tree.json
12-14-17  01:40PM                  140 treeobjects.json
12-14-17  01:40PM                   54 triggers.json
12-14-17  01:40PM                   49 typesstatus.json
12-14-17  01:40PM                   25 udpmessageliststatus.json
12-14-17  01:40PM                   22 unregisterpush.htm
12-14-17  01:40PM                   37 userlist.json
12-14-17  01:40PM                   26 usertags.json
12-14-17  01:40PM                  103 writecorestatus.htm
12-14-17  01:40PM                  107 writeprobestatus.htm
226 Transfer complete.
ftp> cd public
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52951|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                   82 auth0.htm
12-14-17  01:40PM                   35 authzclientid.htm
12-14-17  01:40PM                   33 authzdomain.htm
12-14-17  01:40PM                   15 testlogin.htm
226 Transfer complete.
ftp> gelp
?Invalid command.
ftp> help
Commands may be abbreviated.  Commands are:

!               edit            lpage           nlist           rcvbuf          struct
$               epsv            lpwd            nmap            recv            sunique
account         epsv4           ls              ntrans          reget           system
append          epsv6           macdef          open            remopts         tenex
ascii           exit            mdelete         page            rename          throttle
bell            features        mdir            passive         reset           trace
binary          fget            mget            pdir            restart         type
bye             form            mkdir           pls             rhelp           umask
case            ftp             mls             pmlsd           rmdir           unset
cd              gate            mlsd            preserve        rstatus         usage
cdup            get             mlst            progress        runique         user
chmod           glob            mode            prompt          send            verbose
close           hash            modtime         proxy           sendport        xferbuf
cr              help            more            put             set             ?
debug           idle            mput            pwd             site
delete          image           mreget          quit            size
dir             lcd             msend           quote           sndbuf
disconnect      less            newer           rate            status
ftp> type auth0.htm
auth0.htm: unknown mode.
ftp> mget *
mget auth0.htm [anpqy?]? a
Prompting off for duration of mget.
229 Entering Extended Passive Mode (|||52962|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    82        3.51 KiB/s    00:00 ETA
226 Transfer complete.
82 bytes received in 00:00 (3.46 KiB/s)
229 Entering Extended Passive Mode (|||52963|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    35        1.48 KiB/s    00:00 ETA
226 Transfer complete.
35 bytes received in 00:00 (1.47 KiB/s)
229 Entering Extended Passive Mode (|||52964|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    33        1.40 KiB/s    00:00 ETA
226 Transfer complete.
33 bytes received in 00:00 (1.35 KiB/s)
229 Entering Extended Passive Mode (|||52965|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    15        0.63 KiB/s    00:00 ETA
226 Transfer complete.
15 bytes received in 00:00 (0.62 KiB/s)
ftp> dir
229 Entering Extended Passive Mode (|||52966|)
125 Data connection already open; Transfer starting.
12-14-17  01:40PM                   82 auth0.htm
12-14-17  01:40PM                   35 authzclientid.htm
12-14-17  01:40PM                   33 authzdomain.htm
12-14-17  01:40PM                   15 testlogin.htm
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52967|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                   67 acknowledgealarm.htm
12-14-17  01:40PM                   48 acktodo.htm
12-14-17  01:40PM                  146 adddevice.htm
12-14-17  01:40PM                  145 addgroup.htm
12-14-17  01:40PM                   61 addobjecttomap.htm
12-14-17  01:40PM                  156 addsensor.htm
12-14-17  01:40PM                   91 addticket.htm
12-14-17  01:40PM                   49 addusers.htm
12-14-17  01:40PM                   28 assignticket.htm
12-14-17  01:40PM                   35 authzclientid.htm
12-14-17  01:40PM                   33 authzdomain.htm
12-14-17  01:40PM                  487 autoupdatedownload.htm
12-14-17  01:40PM                   82 autoupdateinstall.htm
12-14-17  01:40PM                   32 chartlegend.json
12-14-17  01:40PM                   32 clearcache.htm
12-14-17  01:40PM                   27 closeticket.htm
12-14-17  01:40PM                   22 cluster.json
12-14-17  01:40PM                   33 createsupportbundle.htm
12-14-17  01:40PM                   80 createtemplate.htm
12-14-17  01:40PM                   32 debugtracker.htm
12-14-17  01:40PM                   64 defaultpw.htm
12-14-17  01:40PM                  104 deleteobject.htm
12-14-17  01:40PM                  101 deletesubobject.htm
12-14-17  01:40PM                   66 discovernow.htm
12-14-17  01:40PM                   80 dontshowhomenagscreen.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                   63 editmapobject.htm
12-14-17  01:40PM                   26 editticket.htm
12-14-17  01:40PM                   54 error.htm
12-14-17  01:40PM                   63 fave.htm
12-14-17  01:40PM                  601 findduplicates.htm
12-14-17  01:40PM                   20 flowmessagelist.json
12-14-17  01:40PM                   29 foldobject.htm
12-14-17  01:40PM                   40 genreport.htm
12-14-17  01:40PM                   11 geolocator.htm
12-14-17  01:40PM                   51 geomarkers.json
12-14-17  01:40PM                   63 geoprovider.json
12-14-17  01:40PM                  158 getaddsensorprogress.htm
12-14-17  01:40PM                  258 getobjectproperty.htm
12-14-17  01:40PM                  211 getobjectstatus.htm
12-14-17  01:40PM                   28 getpasshash.htm
12-14-17  01:40PM                 1901 getsensordetails.json
12-14-17  01:40PM                 2407 getsensordetails.xml
12-14-17  01:40PM                   31 getsensortypes.htm
12-14-17  01:40PM                   20 getserverurl.htm
12-14-17  01:40PM                   31 getserverurlwithdnsname.htm
12-14-17  01:40PM                 2576 getstatus.htm
12-14-17  01:40PM                 1473 getstatus.xml
12-14-17  01:40PM                   32 getticketmessage.htm
12-14-17  01:40PM                   31 getticketstatus.htm
12-14-17  01:40PM                   54 gettreeasjson.htm
12-14-17  01:40PM                 2005 gettreenodestats.xml
12-14-17  01:40PM                   64 hidechanneltabtip.htm
12-14-17  01:40PM                   59 hidesslnagscreen.htm
12-14-17  01:40PM                  263 historicdata.csv
12-14-17  01:40PM                  259 historicdata.json
12-14-17  01:40PM                  258 historicdata.xml
12-14-17  01:40PM                 2619 historicdata_totals.xml
12-14-17  01:40PM                   42 initialmailacknowledge.htm
12-14-17  01:40PM                   28 language.htm
12-14-17  01:40PM                   58 lastconfigsavetime.htm
12-14-17  01:40PM                  451 libraryname.json
12-14-17  01:40PM                  210 license.json
12-14-17  01:40PM                   35 LiveChatEnabled.htm
12-14-17  01:40PM                   38 loadlookups.htm
12-14-17  01:40PM                   29 logajax.htm
12-14-17  01:40PM                  109 maphistorydata.htm
12-14-17  01:40PM                   36 mapobject.json
12-14-17  01:40PM                   43 mapobjectli.htm
12-14-17  01:40PM                   78 mapobjects.htm
12-14-17  01:40PM                   52 mapsettings.htm
12-14-17  01:40PM                  183 mapsvg.htm
12-14-17  01:40PM                  142 maptree.json
12-14-17  01:40PM                   97 moveobject.htm
12-14-17  01:40PM                   53 moveobjectsimple.htm
12-14-17  01:40PM                   69 newpasshash.htm
12-14-17  01:40PM                   51 newtrigger.htm
12-14-17  01:40PM                   57 newtrigger.json
12-14-17  01:40PM                   25 nodechilds.json
12-14-17  01:40PM                   58 notificationtest.htm
12-14-17  01:40PM                   70 notificationtest.json
12-14-17  01:40PM                   31 objectlist.json
12-14-17  01:40PM                 2915 objectstatus.json
12-14-17  01:40PM                  103 ok.htm
12-14-17  01:40PM                   60 pause.htm
12-14-17  01:40PM                   63 pauseobjectfor.htm
12-14-17  01:40PM                  157 percentile.xml
12-14-17  01:40PM                   19 portassertion.htm
12-14-17  01:40PM                  130 preparesensor.htm
12-14-17  01:40PM                   88 preparesensorready.htm
12-14-17  01:40PM                   16 probestate.htm
02-03-19  12:16AM       <DIR>          public
12-14-17  01:40PM                  253 quicksearch.json
12-14-17  01:40PM                  101 recalccache.htm
12-14-17  01:40PM                   20 recommendedconvert.htm
12-14-17  01:40PM                   97 recommendedsensors.json
12-14-17  01:40PM                   67 recommendnow.htm
12-14-17  01:40PM                   45 rediscoverwithcredentials.htm
12-14-17  01:40PM                   38 refreshlicenseinfo.htm
12-14-17  01:40PM                   20 registerpush.htm
12-14-17  01:40PM                   55 reloadfilelists.htm
12-14-17  01:40PM                   72 remoteinstallprobe.htm
12-14-17  01:40PM                   29 rename.htm
12-14-17  01:40PM                   51 reportaddsensor.htm
12-14-17  01:40PM                   75 reportaddsensorchannel.htm
12-14-17  01:40PM                   78 reportdeletesensorchannel.htm
12-14-17  01:40PM                   25 requestudpmessagelist.htm
12-14-17  01:40PM                   40 resetafterpooling.htm
12-14-17  01:40PM                   48 resetnewmessagestimestamp.htm
12-14-17  01:40PM                   29 resolveticket.htm
12-14-17  01:40PM                  103 restartprobes.htm
12-14-17  01:40PM                   57 restartserver.htm
12-14-17  01:40PM                   47 savenow.htm
12-14-17  01:40PM                   62 scannow.htm
12-14-17  01:40PM                   14 search.htm
12-14-17  01:40PM                   38 search.xml
12-14-17  01:40PM                 2512 searchall.json
12-14-17  01:40PM                  849 searchtreeobject.json
12-14-17  01:40PM                  100 sensortest.htm
12-14-17  01:40PM                   52 sensortypes.json
12-14-17  01:40PM                   43 sensortypesinuse.json
12-14-17  01:40PM                   51 setclusterproperty.htm
12-14-17  01:40PM                   36 setcustomerip.htm
12-14-17  01:40PM                   64 setlonlat.htm
12-14-17  01:40PM                   52 setobjectproperty.htm
12-14-17  01:40PM                   65 setposition.htm
12-14-17  01:40PM                   66 setpriority.htm
12-14-17  01:40PM                   32 setshowhelpstatus.htm
12-14-17  01:40PM                   33 setticketpriority.htm
12-14-17  01:40PM                   71 setviewcontent.htm
12-14-17  01:40PM                   34 setviewsize.htm
12-14-17  01:40PM                   63 simulate.htm
12-14-17  01:40PM                   48 sortsubobjects.htm
12-14-17  01:40PM                 2718 status.json
12-14-17  01:40PM                   51 switchtossl.htm
12-14-17  01:40PM                   12 sysinfo.json
12-14-17  01:40PM                   56 sysinfochecknow.json
12-14-17  01:40PM                  149 table.csv
12-14-17  01:40PM                  147 table.json
12-14-17  01:40PM                  145 table.xml
12-14-17  01:40PM                   58 tctAction.htm
12-14-17  01:40PM                   11 tiles.htm
12-14-17  01:40PM                  235 toplist.json
12-14-17  01:40PM                   69 toplistdelete.htm
12-14-17  01:40PM                  105 tree.json
12-14-17  01:40PM                  140 treeobjects.json
12-14-17  01:40PM                   54 triggers.json
12-14-17  01:40PM                   49 typesstatus.json
12-14-17  01:40PM                   25 udpmessageliststatus.json
12-14-17  01:40PM                   22 unregisterpush.htm
12-14-17  01:40PM                   37 userlist.json
12-14-17  01:40PM                   26 usertags.json
12-14-17  01:40PM                  103 writecorestatus.htm
12-14-17  01:40PM                  107 writeprobestatus.htm
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52968|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                   68 acknowledgealarm.htm
12-14-17  01:40PM                 2614 activation.htm
12-14-17  01:40PM                 1723 addautodiscovery.htm
12-14-17  01:40PM                 4276 addautodiscovery0.htm
12-14-17  01:40PM                 1525 adddevice.htm
12-14-17  01:40PM                 5862 adddevice0.htm
12-14-17  01:40PM                  144 adddevice2.htm
12-14-17  01:40PM                 2009 addgroup.htm
12-14-17  01:40PM                 4087 addgroup0.htm
12-14-17  01:40PM                  143 addgroup2.htm
12-14-17  01:40PM                 2103 addlibrary.htm
12-14-17  01:40PM                 6126 addmap.htm
12-14-17  01:40PM                  115 addmap2.htm
12-14-17  01:40PM                 1549 addreport.htm
02-16-18  11:06AM                 7856 addsensor.htm
12-14-17  01:40PM                 6264 addsensor0.htm
12-14-17  01:40PM                 3186 addsensor4.htm
12-14-17  01:40PM                  169 addsensor5.htm
12-14-17  01:40PM                 8209 addsensorfailed.htm
12-14-17  01:40PM                 2166 addticket.htm
12-14-17  01:40PM                 4728 addticket0.htm
12-14-17  01:40PM                 2386 alarms.htm
12-14-17  01:40PM                 2424 alarmsgauges.htm
02-03-19  12:16AM       <DIR>          api
12-14-17  01:40PM                 5618 api.htm
12-14-17  01:40PM                 1232 apple-touch-icon.png
12-14-17  01:40PM                  739 autodiscoverytemplate.htm
12-14-17  01:40PM                 3203 autoupdate.htm
12-14-17  01:40PM                13368 colors.htm
12-14-17  01:40PM                 1296 compare.htm
12-14-17  01:40PM                 1696 compares.htm
12-14-17  01:40PM                  791 config_report_maps.htm
12-14-17  01:40PM                  811 config_report_object.htm
12-14-17  01:40PM                  892 config_report_reports.htm
12-14-17  01:40PM                  391 config_report_systemconfig.htm
12-14-17  01:40PM                 1189 config_report_users.htm
02-03-19  12:16AM       <DIR>          controls
01-11-18  06:05PM                 5451 createtemplate.htm
02-03-19  12:17AM       <DIR>          css
12-14-17  01:40PM                 2732 deleteobject.htm
12-14-17  01:40PM                 1492 deleteobjects.htm
12-14-17  01:40PM                   50 deletesub.htm
02-07-18  04:58PM                 1851 dependencies.htm
02-16-18  11:06AM                 5198 device.htm
12-14-17  01:40PM                 8902 deviceprobeinstall.htm
12-14-17  01:40PM                 1040 devices-qr.htm
12-14-17  01:40PM                 2375 devices.htm
12-14-17  01:40PM                  395 displayrights.htm
12-14-17  01:40PM                 2804 downloads.htm
12-14-17  01:40PM                 6173 duplicatedevice.htm
12-14-17  01:40PM                 4941 duplicategroup.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                 5399 duplicatesensor.htm
12-14-17  01:40PM                 3493 editnotification.htm
12-14-17  01:40PM                 3043 editrights.htm
12-14-17  01:40PM                 2834 editschedule.htm
12-14-17  01:40PM                 1648 editticket.htm
12-14-17  01:40PM                 3386 edituser.htm
12-14-17  01:40PM                 3247 editusergroup.htm
12-14-17  01:40PM                 2811 error.htm
12-14-17  01:40PM                 1032 errorreport.htm
12-14-17  01:40PM                 1150 favicon.ico
12-14-17  01:40PM                 1681 filter.htm
12-14-17  01:40PM                  873 generatehistoricdata.htm
12-14-17  01:40PM                  718 generatereport.htm
12-27-17  12:17PM                 3080 geomap.htm
12-14-17  01:40PM                  397 geomapdevices.htm
12-14-17  01:40PM                  768 geomap_static.htm
12-14-17  01:40PM                 1574 gotoserviceurl.htm
12-14-17  01:40PM                 1570 graphzoom.htm
12-14-17  01:40PM                 2022 graphzoomtoplist.htm
02-16-18  11:01AM                 5987 group.htm
12-22-17  09:32AM                 2248 healtherrors.htm
02-03-19  12:17AM       <DIR>          help
12-14-17  01:40PM                 9823 help.htm
01-11-18  03:21PM                14537 historicdata.htm
12-14-17  01:40PM                 2746 historicdata_html.htm
02-03-19  12:16AM       <DIR>          icons
02-03-19  12:16AM       <DIR>          images
02-03-19  12:17AM       <DIR>          includes
12-14-17  01:40PM                  153 index.htm
02-03-19  12:17AM       <DIR>          javascript
12-14-17  01:40PM                 1005 jstests.htm
12-14-17  01:40PM                 3131 libraries.htm
12-14-17  01:40PM                 3771 library.htm
12-14-17  01:40PM                 2955 libraryobject.htm
12-14-17  01:40PM                 1333 library_static.htm
12-14-17  01:40PM                 2234 licensing.htm
12-14-17  01:40PM                 1476 log.htm
02-03-19  12:16AM       <DIR>          mailtemplates
12-14-17  01:40PM                 4045 map.htm
02-01-18  02:04PM                  820 mapdashboard.htm
02-03-19  12:16AM       <DIR>          mapicons
02-03-19  12:17AM       <DIR>          mapobjects
02-16-18  11:06AM                 3293 maps.htm
12-14-17  01:40PM                 5997 mapshow.htm
12-14-17  01:40PM                 3725 mapshow_simple.htm
12-14-17  01:40PM                  439 mapshow_static.htm
12-14-17  01:40PM                 4860 moveobject.htm
12-14-17  01:40PM                   97 moveobjectnow.htm
12-14-17  01:40PM                 3195 multiedit.htm
12-14-17  01:40PM                 2480 multiinlineedit.htm
12-14-17  01:40PM                 3121 myaccount.htm
12-14-17  01:40PM                 2604 objecthistory.htm
12-14-17  01:40PM                 1661 objectusedby.htm
12-14-17  01:40PM                  899 openwindow.htm
12-14-17  01:40PM                79987 package-lock.json
12-14-17  01:40PM                   61 pause.htm
12-14-17  01:40PM                   64 pauseobjectfor.htm
02-16-18  11:06AM                 4798 probenode.htm
02-03-19  12:18AM                    0 prtg_trial_user_survey.txt
02-03-19  12:17AM       <DIR>          public
12-14-17  01:40PM                  262 remotedesktop.rdp
12-14-17  01:40PM                 4244 remoteprobeinstall.htm
12-14-17  01:40PM                 4266 report.htm
12-14-17  01:40PM                 2989 reports.htm
02-03-19  12:17AM       <DIR>          reporttemplates
12-14-17  01:40PM                 1634 salesbundle_send.htm
12-14-17  01:40PM                   63 scannow.htm
12-14-17  01:40PM                 2266 search.htm
12-14-17  01:40PM                 1742 searchdetailed.htm
12-14-17  01:40PM                  810 sendbdmfeedback.htm
12-14-17  01:40PM                  798 sendfeedback.htm
12-14-17  01:40PM                  812 sendsalesfeedback.htm
12-14-17  01:40PM                 5966 sensor.htm
12-14-17  01:40PM                 2593 sensors.htm
12-14-17  01:40PM                 2171 sensorxref.htm
12-14-17  01:40PM                 1772 setup.htm
02-16-18  11:06AM                 2172 similarsensors.htm
02-03-19  12:17AM       <DIR>          sounds
12-14-17  01:40PM                10602 speedtest.htm
01-22-18  11:55AM                10870 start.htm
12-14-17  01:40PM                 2021 status.htm
12-14-17  01:40PM                 1651 supportbundle_send.htm
12-14-17  01:40PM                 4759 systemsetup.htm
12-14-17  01:40PM                  587 tablewithstyles.htm
12-14-17  01:40PM                11780 tct-overview.htm
12-14-17  01:40PM                 6509 tct-toggle.htm
12-14-17  01:40PM                   28 testjson.htm
12-14-17  01:40PM                69758 testsuite.htm
12-14-17  01:40PM                 1883 ticket.htm
12-14-17  01:40PM                 3191 tickets.htm
02-03-19  12:16AM       <DIR>          tickettemplates
12-14-17  01:40PM                 1729 top10.htm
12-14-17  01:40PM                 4208 toplist.htm
12-14-17  01:40PM                 2886 toplistprint.htm
12-14-17  01:40PM                 2431 traceroute.htm
12-14-17  01:40PM                 1058 trialsurvey.htm
12-14-17  01:40PM                 5028 udc_ui_android.htm
12-14-17  01:40PM                 5028 udc_ui_mac.htm
12-14-17  01:40PM                 5028 udc_ui_win.htm
12-14-17  01:40PM                 5544 welcome.htm
12-14-17  01:40PM                 5181 wingui.htm
12-14-17  01:40PM                 1306 you_should_use_ssl.htm
226 Transfer complete.
ftp> cd controls
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52969|)
125 Data connection already open; Transfer starting.
12-14-17  01:40PM                10820 accountoverview.htm
12-14-17  01:40PM                 1077 acknowledgealarm.htm
12-14-17  01:40PM                 1520 acknowledgealarmuntil.htm
12-14-17  01:40PM                  344 acknowledgealltodosdialog.htm
12-14-17  01:40PM                10901 activationrequired.htm
12-14-17  01:40PM                 2474 addautodiscovery.htm
12-14-17  01:40PM                  744 addautodiscovery_notallowed.htm
12-14-17  01:40PM                  846 addcontact.htm
12-14-17  01:40PM                 5347 adddevice.htm
12-14-17  01:40PM                  725 adddevice_notallowed.htm
12-14-17  01:40PM                 2305 addgroup.htm
12-14-17  01:40PM                  723 addgroup_notallowed.htm
12-14-17  01:40PM                  221 addsensor2.htm
12-14-17  01:40PM                  329 addsensor3.htm
12-14-17  01:40PM                 5312 apicustomnotifications.htm
02-16-18  11:06AM                36530 apicustomsensors.htm
12-14-17  01:40PM                 5527 apihistoricdata.htm
12-14-17  01:40PM                 7938 apihttp.htm
12-14-17  01:40PM                44663 apilivedata.htm
12-14-17  01:40PM                 6197 apilivegraphs.htm
12-14-17  01:40PM                44742 apiminiprobe.htm
12-14-17  01:40PM                11415 apiobjectmanipulation.htm
01-11-18  06:05PM                 1945 apioverview.htm
12-14-17  01:40PM                 5413 apiwebsitestyling.htm
02-16-18  11:06AM                  844 autodiscoverytemplatedevice.htm
02-16-18  11:06AM                  831 autodiscoverytemplategroup.htm
12-14-17  01:40PM                 8048 autoupdatedata.htm
12-14-17  01:40PM                 1160 autoupdatepage.htm
12-14-17  01:40PM                 6610 bdmticketform.htm
12-14-17  01:40PM                  591 channeledit.htm
12-14-17  01:40PM                 1129 channels.htm
12-14-17  01:40PM                   19 clusterdetail.htm
12-14-17  01:40PM                 1009 clusterselector.htm
12-14-17  01:40PM                 1445 clustersetup.htm
12-14-17  01:40PM                  269 clusterstateforpagetop.htm
12-14-17  01:40PM                  736 clusterstatus.htm
12-14-17  01:40PM                  521 clusterstatusdetail.htm
12-14-17  01:40PM                   31 clustervisuallist.htm
12-14-17  01:40PM                  912 comments.htm
12-14-17  01:40PM                  773 compareobject.htm
12-14-17  01:40PM                  419 compareobject.multi.htm
12-14-17  01:40PM                  948 compareobjectedit.htm
12-14-17  01:40PM                  327 compareobjecteditajax.htm
12-14-17  01:40PM                 1014 config_report_systemconfig.htm
12-14-17  01:40PM                 2693 contactlist.htm
12-14-17  01:40PM                 3915 dashboard1content.htm
12-14-17  01:40PM                 4267 datetimedialog.htm
12-14-17  01:40PM                 2217 dependenciesheader.htm
12-14-17  01:40PM                 3974 dependenciesoverview.htm
12-14-17  01:40PM                  398 dependenciestable.htm
12-14-17  01:40PM                 2264 devicedata.htm
12-14-17  01:40PM                 2010 deviceheader.htm
12-14-17  01:40PM                 9011 deviceoverview.htm
12-14-17  01:40PM                 3970 deviceoverview_statusinfo.htm
12-14-17  01:40PM                  397 devicestooltip.htm
12-14-17  01:40PM                 3172 devicetooltip.htm
12-14-17  01:40PM                 2608 downloads_enterpriseconsole.htm
12-14-17  01:40PM                 4456 downloads_mobile.htm
12-14-17  01:40PM                 2808 downloads_probe.htm
12-14-17  01:40PM                 1435 downloads_tools.htm
12-14-17  01:40PM                 1707 duplicatedevicedialog.htm
12-14-17  01:40PM                   71 duplicatesfounddialog.htm
12-14-17  01:40PM                 1675 editchannels.htm
12-14-17  01:40PM                  780 editcontact.htm
12-14-17  01:40PM                 1075 editnotification.htm
12-14-17  01:40PM                  711 editschedule.htm
12-14-17  01:40PM                 1207 editserviceurl.htm
12-14-17  01:40PM                 1696 edituser.htm
12-14-17  01:40PM                 2487 editusergroup.htm
12-14-17  01:40PM                  543 geomap.htm
12-14-17  01:40PM                 5866 googleaddons.htm
12-14-17  01:40PM                   26 graph.htm
12-14-17  01:40PM                 1961 groupdata.htm
12-14-17  01:40PM                 2217 groupheader.htm
12-14-17  01:40PM                 7154 groupoverview.htm
12-14-17  01:40PM                 2445 groupoverviewcolumnrigth.htm
02-16-18  11:06AM                 4029 groupoverviewsmalldata.htm
12-14-17  01:40PM                 2639 groupoverview_statusinfo.htm
02-16-18  11:06AM                 1685 groupoverview_treetoolbar.htm
12-14-17  01:40PM                 2951 grouptooltip.htm
01-11-18  03:21PM                13821 historicsensordata.htm
12-14-17  01:40PM                  727 history.htm
02-16-18  11:06AM                 2736 libmanage.htm
02-16-18  11:06AM                  972 liboverview.htm
01-24-18  06:04PM                 2031 liboverview_treetoolbar.htm
12-14-17  01:40PM                  360 libraryfiltertooltip.htm
12-14-17  01:40PM                 1091 libtree.htm
12-14-17  01:40PM                 2751 licensingpage.htm
12-14-17  01:40PM                  294 loadlog.htm
12-14-17  01:40PM                 1729 loginform_small.htm
12-14-17  01:40PM                 5496 lorem.htm
12-14-17  01:40PM                 1859 maintenance.htm
01-24-18  06:04PM                 5292 mapdesigner.htm
12-14-17  01:40PM                 2116 mapeditsettings.htm
12-14-17  01:40PM                 1872 maphtml.htm
12-14-17  01:40PM                   64 mapobjectonly.htm
12-14-17  01:40PM                  109 mapobjectpreview.htm
01-18-18  11:03AM                 8447 maponly.htm
12-14-17  01:40PM                  727 mapview.htm
12-14-17  01:40PM                  726 mapviewwingui.htm
12-14-17  01:40PM                 7765 menu.htm
12-14-17  01:40PM                 1112 multichannels.htm
12-14-17  01:40PM                 1856 multieditchannels.htm
12-14-17  01:40PM                 1099 multitab.htm
12-14-17  01:40PM                  288 myaccount.htm
12-14-17  01:40PM                 1573 noeditchannels.htm
12-14-17  01:40PM                 2987 notifications.htm
12-14-17  01:40PM                 9070 objectdata.htm
12-14-17  01:40PM                 1939 objectgraph.htm
12-14-17  01:40PM                   44 objectlink.htm
12-14-17  01:40PM                  789 objectlookupnew.htm
02-16-18  11:06AM                  387 objectlookupnewany.htm
12-14-17  01:40PM                  582 objectlookupnewempty.htm
12-14-17  01:40PM                 3497 objectselectorform.htm
12-14-17  01:40PM                 2021 objectselectorformnosensors.htm
12-14-17  01:40PM                 1593 pauseuntil.htm
12-14-17  01:40PM                 1083 pausewithcomment.htm
12-14-17  01:40PM                 1769 probedata.htm
12-14-17  01:40PM                 1910 probeheader.htm
12-14-17  01:40PM                28292 prtglicense_de.htm
12-14-17  01:40PM                29607 prtglicense_en.htm
12-14-17  01:40PM                  272 qr-object.htm
12-14-17  01:40PM                  803 qr-user.htm
12-14-17  01:40PM                  749 quickedit.htm
12-14-17  01:40PM                 1166 quickeditdevice.htm
12-14-17  01:40PM                   58 quickobjectpauser.htm
12-14-17  01:40PM                   83 recommendedsensors.htm
12-14-17  01:40PM                  295 reportchannellist.htm
02-16-18  11:06AM                 3255 reportchannels.htm
12-14-17  01:40PM                  171 reportchannelsearch.htm
12-14-17  01:40PM                  440 reportlister.htm
12-22-17  09:32AM                 9254 reportrunner.htm
12-14-17  01:40PM                  925 reportsensorsbytag.htm
12-14-17  01:40PM                 1682 rootandlibstree.htm
12-14-17  01:40PM                 1199 roottree.htm
12-14-17  01:40PM                   51 salesbundle.htm
12-14-17  01:40PM                 7020 salesticketform.htm
12-14-17  01:40PM                 1960 schedules.htm
12-14-17  01:40PM                   30 screenshot.htm
12-22-17  09:32AM                 4231 search.htm
01-22-18  11:55AM                 2400 searchdetailed.htm
02-16-18  11:06AM                 5996 searchform.htm
12-14-17  01:40PM                  106 searchhelp.htm
12-14-17  01:40PM                  387 searchid.htm
12-14-17  01:40PM                 6460 sensordata.htm
12-14-17  01:40PM                 2081 sensorgraph.htm
12-14-17  01:40PM                  492 sensorgraphs.htm
12-14-17  01:40PM                 2712 sensorheader.htm
12-14-17  01:40PM                 1657 sensormessages.htm
02-16-18  11:06AM                10115 sensoroverview.htm
12-14-17  01:40PM                 3596 sensoroverviewsmalldata.htm
12-14-17  01:40PM                   42 sensorstats.htm
12-14-17  01:40PM                 1327 sensorstatusdata.htm
12-14-17  01:40PM                 5363 sensortooltip.htm
12-14-17  01:40PM                  977 sensortree.htm
12-14-17  01:40PM                 4245 sensortreemanagetab.htm
12-14-17  01:40PM                  516 sensortypeselection.htm
12-14-17  01:40PM                 6813 statusadmintools.htm
12-14-17  01:40PM                  161 supportbundle.htm
12-14-17  01:40PM                  925 supportbundle_statusdata.htm
12-14-17  01:40PM                  596 supportbundle_table.htm
12-14-17  01:40PM                21632 supportticketform.htm
12-14-17  01:40PM                 1880 switchtossl.htm
12-14-17  01:40PM                11951 sysinfo.htm
12-14-17  01:40PM                  700 systemstatus.htm
12-14-17  01:40PM                   89 table.htm
12-14-17  01:40PM                  712 ticketheader.htm
12-14-17  01:40PM                 1561 tickethistory.htm
12-14-17  01:40PM                 2536 ticket_assign.htm
12-14-17  01:40PM                 2115 ticket_change.htm
12-14-17  01:40PM                13650 top10listcontent.htm
12-14-17  01:40PM                 1048 toplistadd.htm
12-14-17  01:40PM                  233 toplistdata.htm
12-14-17  01:40PM                 1041 toplistdelete.htm
12-14-17  01:40PM                  992 toplistedit.htm
12-14-17  01:40PM                  432 toplistgraph.htm
12-14-17  01:40PM                 1658 toplistperiods.htm
12-14-17  01:40PM                 1507 toplistpreview.htm
12-14-17  01:40PM                   59 toplists.htm
12-14-17  01:40PM                  627 toplistscontent.htm
12-14-17  01:40PM                   35 toplistselect.htm
12-14-17  01:40PM                  178 traceroute.htm
12-14-17  01:40PM                 4278 treesensorswitches.htm
12-14-17  01:40PM                 1431 treeswitches.htm
12-14-17  01:40PM                  844 triggers.htm
02-01-18  02:04PM                20993 triggersandnotifications.htm
12-14-17  01:40PM                 2369 usergroups.htm
12-14-17  01:40PM                 2421 userlist.htm
12-14-17  01:40PM                  937 welcome_autoupdate.htm
12-14-17  01:40PM                 2783 welcome_currentalarms.htm
12-14-17  01:40PM                  326 welcome_licenseinfo.htm
12-14-17  01:40PM                 2417 welcome_licenseinfo_c.htm
12-14-17  01:40PM                  472 welcome_licenseinfo_f.htm
12-14-17  01:40PM                  354 welcome_licenseinfo_p.htm
12-14-17  01:40PM                  337 welcome_licenseinfo_pt.htm
12-14-17  01:40PM                  970 welcome_licenseinfo_t.htm
12-14-17  01:40PM                  480 welcome_opentickets.htm
12-14-17  01:40PM                 3984 welcome_sensors.htm
12-14-17  01:40PM                 1580 welcome_sensors_available_donut.htm
12-14-17  01:40PM                 1769 welcome_yesterdayactivities.htm
12-10-18  12:36PM                44684 whatsnew.htm
12-14-17  01:40PM                  645 winguitctgroupoverview.htm
12-14-17  01:40PM                14297 winguitop10listcontent.htm
226 Transfer complete.
ftp> dir *txt
229 Entering Extended Passive Mode (|||52979|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> dir *.txt
229 Entering Extended Passive Mode (|||52980|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52981|)
150 Opening ASCII mode data connection.
12-14-17  01:40PM                   68 acknowledgealarm.htm
12-14-17  01:40PM                 2614 activation.htm
12-14-17  01:40PM                 1723 addautodiscovery.htm
12-14-17  01:40PM                 4276 addautodiscovery0.htm
12-14-17  01:40PM                 1525 adddevice.htm
12-14-17  01:40PM                 5862 adddevice0.htm
12-14-17  01:40PM                  144 adddevice2.htm
12-14-17  01:40PM                 2009 addgroup.htm
12-14-17  01:40PM                 4087 addgroup0.htm
12-14-17  01:40PM                  143 addgroup2.htm
12-14-17  01:40PM                 2103 addlibrary.htm
12-14-17  01:40PM                 6126 addmap.htm
12-14-17  01:40PM                  115 addmap2.htm
12-14-17  01:40PM                 1549 addreport.htm
02-16-18  11:06AM                 7856 addsensor.htm
12-14-17  01:40PM                 6264 addsensor0.htm
12-14-17  01:40PM                 3186 addsensor4.htm
12-14-17  01:40PM                  169 addsensor5.htm
12-14-17  01:40PM                 8209 addsensorfailed.htm
12-14-17  01:40PM                 2166 addticket.htm
12-14-17  01:40PM                 4728 addticket0.htm
12-14-17  01:40PM                 2386 alarms.htm
12-14-17  01:40PM                 2424 alarmsgauges.htm
02-03-19  12:16AM       <DIR>          api
12-14-17  01:40PM                 5618 api.htm
12-14-17  01:40PM                 1232 apple-touch-icon.png
12-14-17  01:40PM                  739 autodiscoverytemplate.htm
12-14-17  01:40PM                 3203 autoupdate.htm
12-14-17  01:40PM                13368 colors.htm
12-14-17  01:40PM                 1296 compare.htm
12-14-17  01:40PM                 1696 compares.htm
12-14-17  01:40PM                  791 config_report_maps.htm
12-14-17  01:40PM                  811 config_report_object.htm
12-14-17  01:40PM                  892 config_report_reports.htm
12-14-17  01:40PM                  391 config_report_systemconfig.htm
12-14-17  01:40PM                 1189 config_report_users.htm
02-03-19  12:16AM       <DIR>          controls
01-11-18  06:05PM                 5451 createtemplate.htm
02-03-19  12:17AM       <DIR>          css
12-14-17  01:40PM                 2732 deleteobject.htm
12-14-17  01:40PM                 1492 deleteobjects.htm
12-14-17  01:40PM                   50 deletesub.htm
02-07-18  04:58PM                 1851 dependencies.htm
02-16-18  11:06AM                 5198 device.htm
12-14-17  01:40PM                 8902 deviceprobeinstall.htm
12-14-17  01:40PM                 1040 devices-qr.htm
12-14-17  01:40PM                 2375 devices.htm
12-14-17  01:40PM                  395 displayrights.htm
12-14-17  01:40PM                 2804 downloads.htm
12-14-17  01:40PM                 6173 duplicatedevice.htm
12-14-17  01:40PM                 4941 duplicategroup.htm
12-14-17  01:40PM                   81 duplicateobject.htm
12-14-17  01:40PM                 5399 duplicatesensor.htm
12-14-17  01:40PM                 3493 editnotification.htm
12-14-17  01:40PM                 3043 editrights.htm
12-14-17  01:40PM                 2834 editschedule.htm
12-14-17  01:40PM                 1648 editticket.htm
12-14-17  01:40PM                 3386 edituser.htm
12-14-17  01:40PM                 3247 editusergroup.htm
12-14-17  01:40PM                 2811 error.htm
12-14-17  01:40PM                 1032 errorreport.htm
12-14-17  01:40PM                 1150 favicon.ico
12-14-17  01:40PM                 1681 filter.htm
12-14-17  01:40PM                  873 generatehistoricdata.htm
12-14-17  01:40PM                  718 generatereport.htm
12-27-17  12:17PM                 3080 geomap.htm
12-14-17  01:40PM                  397 geomapdevices.htm
12-14-17  01:40PM                  768 geomap_static.htm
12-14-17  01:40PM                 1574 gotoserviceurl.htm
12-14-17  01:40PM                 1570 graphzoom.htm
12-14-17  01:40PM                 2022 graphzoomtoplist.htm
02-16-18  11:01AM                 5987 group.htm
12-22-17  09:32AM                 2248 healtherrors.htm
02-03-19  12:17AM       <DIR>          help
12-14-17  01:40PM                 9823 help.htm
01-11-18  03:21PM                14537 historicdata.htm
12-14-17  01:40PM                 2746 historicdata_html.htm
02-03-19  12:16AM       <DIR>          icons
02-03-19  12:16AM       <DIR>          images
02-03-19  12:17AM       <DIR>          includes
12-14-17  01:40PM                  153 index.htm
02-03-19  12:17AM       <DIR>          javascript
12-14-17  01:40PM                 1005 jstests.htm
12-14-17  01:40PM                 3131 libraries.htm
12-14-17  01:40PM                 3771 library.htm
12-14-17  01:40PM                 2955 libraryobject.htm
12-14-17  01:40PM                 1333 library_static.htm
12-14-17  01:40PM                 2234 licensing.htm
12-14-17  01:40PM                 1476 log.htm
02-03-19  12:16AM       <DIR>          mailtemplates
12-14-17  01:40PM                 4045 map.htm
02-01-18  02:04PM                  820 mapdashboard.htm
02-03-19  12:16AM       <DIR>          mapicons
02-03-19  12:17AM       <DIR>          mapobjects
02-16-18  11:06AM                 3293 maps.htm
12-14-17  01:40PM                 5997 mapshow.htm
12-14-17  01:40PM                 3725 mapshow_simple.htm
12-14-17  01:40PM                  439 mapshow_static.htm
12-14-17  01:40PM                 4860 moveobject.htm
12-14-17  01:40PM                   97 moveobjectnow.htm
12-14-17  01:40PM                 3195 multiedit.htm
12-14-17  01:40PM                 2480 multiinlineedit.htm
12-14-17  01:40PM                 3121 myaccount.htm
12-14-17  01:40PM                 2604 objecthistory.htm
12-14-17  01:40PM                 1661 objectusedby.htm
12-14-17  01:40PM                  899 openwindow.htm
12-14-17  01:40PM                79987 package-lock.json
12-14-17  01:40PM                   61 pause.htm
12-14-17  01:40PM                   64 pauseobjectfor.htm
02-16-18  11:06AM                 4798 probenode.htm
02-03-19  12:18AM                    0 prtg_trial_user_survey.txt
02-03-19  12:17AM       <DIR>          public
12-14-17  01:40PM                  262 remotedesktop.rdp
12-14-17  01:40PM                 4244 remoteprobeinstall.htm
12-14-17  01:40PM                 4266 report.htm
12-14-17  01:40PM                 2989 reports.htm
02-03-19  12:17AM       <DIR>          reporttemplates
12-14-17  01:40PM                 1634 salesbundle_send.htm
12-14-17  01:40PM                   63 scannow.htm
12-14-17  01:40PM                 2266 search.htm
12-14-17  01:40PM                 1742 searchdetailed.htm
12-14-17  01:40PM                  810 sendbdmfeedback.htm
12-14-17  01:40PM                  798 sendfeedback.htm
12-14-17  01:40PM                  812 sendsalesfeedback.htm
12-14-17  01:40PM                 5966 sensor.htm
12-14-17  01:40PM                 2593 sensors.htm
12-14-17  01:40PM                 2171 sensorxref.htm
12-14-17  01:40PM                 1772 setup.htm
02-16-18  11:06AM                 2172 similarsensors.htm
02-03-19  12:17AM       <DIR>          sounds
12-14-17  01:40PM                10602 speedtest.htm
01-22-18  11:55AM                10870 start.htm
12-14-17  01:40PM                 2021 status.htm
12-14-17  01:40PM                 1651 supportbundle_send.htm
12-14-17  01:40PM                 4759 systemsetup.htm
12-14-17  01:40PM                  587 tablewithstyles.htm
12-14-17  01:40PM                11780 tct-overview.htm
12-14-17  01:40PM                 6509 tct-toggle.htm
12-14-17  01:40PM                   28 testjson.htm
12-14-17  01:40PM                69758 testsuite.htm
12-14-17  01:40PM                 1883 ticket.htm
12-14-17  01:40PM                 3191 tickets.htm
02-03-19  12:16AM       <DIR>          tickettemplates
12-14-17  01:40PM                 1729 top10.htm
12-14-17  01:40PM                 4208 toplist.htm
12-14-17  01:40PM                 2886 toplistprint.htm
12-14-17  01:40PM                 2431 traceroute.htm
12-14-17  01:40PM                 1058 trialsurvey.htm
12-14-17  01:40PM                 5028 udc_ui_android.htm
12-14-17  01:40PM                 5028 udc_ui_mac.htm
12-14-17  01:40PM                 5028 udc_ui_win.htm
12-14-17  01:40PM                 5544 welcome.htm
12-14-17  01:40PM                 5181 wingui.htm
12-14-17  01:40PM                 1306 you_should_use_ssl.htm
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52982|)
150 Opening ASCII mode data connection.
02-03-19  12:17AM       <DIR>          64 bit
02-03-19  12:15AM                 1888 activation.dat
02-03-19  12:18AM       <DIR>          cert
12-14-17  01:40PM              2461696 chartdir51.dll
12-14-17  01:40PM              9077248 ChilkatDelphiXE.dll
12-14-17  01:40PM              2138986 chrome.pak
02-03-19  12:17AM       <DIR>          Custom Sensors
12-14-17  01:40PM               382464 dbexpmda40.dll
12-14-17  01:40PM               519680 dbexpoda40.dll
12-14-17  01:40PM               377856 dbexpsda40.dll
12-14-17  01:40PM                 5681 defaultmaps.xml
12-14-17  01:40PM                12871 defaultmaps_iad.xml
02-13-18  03:08PM                 1224 deviceiconlist.txt
02-03-19  12:17AM       <DIR>          devicetemplates
05-16-25  08:15AM       <DIR>          dlltemp
02-03-19  12:18AM       <DIR>          download
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 6218 FlowRules.osr
02-03-19  12:18AM       <DIR>          helperlibs
12-14-17  01:40PM              9956864 icudt.dll
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-03-19  12:16AM       <DIR>          language
12-14-17  01:40PM              3707349 Lb2to3.exe
12-14-17  01:40PM             24978944 libcef.dll
12-14-17  01:40PM              1412096 libeay32.dll
02-03-19  12:17AM       <DIR>          locales
02-03-19  12:18AM       <DIR>          lookups
02-16-18  11:03AM               796566 macmanufacturerlist.txt
02-03-19  12:18AM       <DIR>          MIB
12-14-17  01:40PM                  522 Microsoft.VC80.CRT.manifest
12-14-17  01:40PM               421200 msvcp100.dll
12-14-17  01:40PM               770384 msvcr100.dll
12-14-17  01:40PM               630544 msvcr80.dll
12-14-17  01:40PM                12498 netsnmp-license.txt
02-03-19  12:17AM       <DIR>          Notifications
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM               487936 openssl.exe
01-18-18  11:03AM               177152 paelibssh.dll
12-14-17  01:40PM                35088 paesslerchart.dll
12-14-17  01:40PM              1083904 PaesslerSNMP.dll
02-15-18  05:24PM              1074688 PaesslerSNMPWrapper.dll
12-14-17  01:40PM               421160 PaesslerSQLEngine.dll
12-14-17  01:40PM               193832 PaesslerSQLEngineDBX.dll
12-14-17  01:40PM               331536 paesslerVMWareShell.exe
12-14-17  01:40PM               310032 paesslerVMWareShell.vshost.exe
12-14-17  01:40PM                 1429 phantomjs-license.bsd
12-14-17  01:40PM                 1428 protocol.txt
02-16-18  11:04AM              6379096 PRTG Administrator.exe
02-16-18  11:05AM             12923480 PRTG Enterprise Console.exe
02-16-18  11:04AM              5439576 PRTG GUI Starter.exe
02-03-19  12:17AM       <DIR>          PRTG Installer Archive
02-16-18  11:05AM             11647576 PRTG Probe.exe
02-16-18  11:05AM              7026776 PRTG Server.exe
02-03-19  12:18AM              2000256 PRTG Setup Log.log
02-03-19  12:17AM       <DIR>          prtg-installer-for-distribution
12-14-17  01:40PM               300318 prtg.ico
12-14-17  01:40PM               444640 PrtgDllWrapper.exe
02-16-18  11:04AM              2778200 PRTGProbeUpdate.exe
02-16-18  11:04AM              3227224 PrtgRemoteInstall.exe
02-16-18  11:04AM              2782808 PRTGServerUpdate.exe
02-16-18  11:04AM              2104408 PRTG_Chromium_Helper.exe
02-16-18  11:04AM              2264664 PRTG_IE_Helper.exe
02-03-19  12:17AM       <DIR>          Python34
02-16-18  11:04AM              1012224 RegWrapper.exe
02-03-19  12:17AM       <DIR>          Sensor System
02-03-19  12:17AM       <DIR>          snmplibs
02-03-19  12:18AM       <DIR>          snmptemp
01-18-18  11:03AM               461824 ssh.dll
12-14-17  01:40PM               384512 ssleay32.dll
02-03-19  12:18AM       <DIR>          themes
02-03-19  12:18AM              1275563 unins000.dat
02-03-19  12:15AM              1498815 unins000.exe
12-14-17  01:40PM              1163024 VimService2005.dll
12-14-17  01:40PM              4312848 VimService2005.XmlSerializers.dll
02-03-19  12:17AM       <DIR>          webroot
226 Transfer complete.
ftp> cd cert
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||52983|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                  673 dh.log
02-03-19  12:18AM                  245 dh.pem
12-14-17  01:40PM                   84 generatedh.bat
12-14-17  01:40PM                10835 openssl.cnf
12-14-17  01:40PM                 1326 prtg.crt
12-14-17  01:40PM                 1675 prtg.key
12-14-17  01:40PM                  916 root.pem
226 Transfer complete.
ftp> mget *
mget dh.log [anpqy?]? a
Prompting off for duration of mget.
229 Entering Extended Passive Mode (|||52994|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|   673       28.97 KiB/s    00:00 ETA
226 Transfer complete.
673 bytes received in 00:00 (28.45 KiB/s)
229 Entering Extended Passive Mode (|||52995|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|   245       10.41 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 5 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
245 bytes received in 00:00 (10.31 KiB/s)
229 Entering Extended Passive Mode (|||52996|)
150 Opening ASCII mode data connection.
100% |******************************************************************|    84        3.58 KiB/s    00:00 ETA
226 Transfer complete.
84 bytes received in 00:00 (3.49 KiB/s)
229 Entering Extended Passive Mode (|||52997|)
150 Opening ASCII mode data connection.
100% |******************************************************************| 10835      454.04 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 350 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
10835 bytes received in 00:00 (450.18 KiB/s)
229 Entering Extended Passive Mode (|||52998|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|  1326       56.23 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 22 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
1326 bytes received in 00:00 (55.40 KiB/s)
229 Entering Extended Passive Mode (|||52999|)
150 Opening ASCII mode data connection.
100% |******************************************************************|  1675       70.45 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 27 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
1675 bytes received in 00:00 (69.03 KiB/s)
229 Entering Extended Passive Mode (|||53000|)
150 Opening ASCII mode data connection.
100% |******************************************************************|   916       39.49 KiB/s    00:00 ETA
226 Transfer complete.
WARNING! 16 bare linefeeds received in ASCII mode.
File may not have transferred correctly.
916 bytes received in 00:00 (39.09 KiB/s)
ftp> dir
229 Entering Extended Passive Mode (|||53001|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                  673 dh.log
02-03-19  12:18AM                  245 dh.pem
12-14-17  01:40PM                   84 generatedh.bat
12-14-17  01:40PM                10835 openssl.cnf
12-14-17  01:40PM                 1326 prtg.crt
12-14-17  01:40PM                 1675 prtg.key
12-14-17  01:40PM                  916 root.pem
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53002|)
125 Data connection already open; Transfer starting.
02-03-19  12:17AM       <DIR>          64 bit
02-03-19  12:15AM                 1888 activation.dat
02-03-19  12:18AM       <DIR>          cert
12-14-17  01:40PM              2461696 chartdir51.dll
12-14-17  01:40PM              9077248 ChilkatDelphiXE.dll
12-14-17  01:40PM              2138986 chrome.pak
02-03-19  12:17AM       <DIR>          Custom Sensors
12-14-17  01:40PM               382464 dbexpmda40.dll
12-14-17  01:40PM               519680 dbexpoda40.dll
12-14-17  01:40PM               377856 dbexpsda40.dll
12-14-17  01:40PM                 5681 defaultmaps.xml
12-14-17  01:40PM                12871 defaultmaps_iad.xml
02-13-18  03:08PM                 1224 deviceiconlist.txt
02-03-19  12:17AM       <DIR>          devicetemplates
05-16-25  08:15AM       <DIR>          dlltemp
02-03-19  12:18AM       <DIR>          download
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 6218 FlowRules.osr
02-03-19  12:18AM       <DIR>          helperlibs
12-14-17  01:40PM              9956864 icudt.dll
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-03-19  12:16AM       <DIR>          language
12-14-17  01:40PM              3707349 Lb2to3.exe
12-14-17  01:40PM             24978944 libcef.dll
12-14-17  01:40PM              1412096 libeay32.dll
02-03-19  12:17AM       <DIR>          locales
02-03-19  12:18AM       <DIR>          lookups
02-16-18  11:03AM               796566 macmanufacturerlist.txt
02-03-19  12:18AM       <DIR>          MIB
12-14-17  01:40PM                  522 Microsoft.VC80.CRT.manifest
12-14-17  01:40PM               421200 msvcp100.dll
12-14-17  01:40PM               770384 msvcr100.dll
12-14-17  01:40PM               630544 msvcr80.dll
12-14-17  01:40PM                12498 netsnmp-license.txt
02-03-19  12:17AM       <DIR>          Notifications
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM               487936 openssl.exe
01-18-18  11:03AM               177152 paelibssh.dll
12-14-17  01:40PM                35088 paesslerchart.dll
12-14-17  01:40PM              1083904 PaesslerSNMP.dll
02-15-18  05:24PM              1074688 PaesslerSNMPWrapper.dll
12-14-17  01:40PM               421160 PaesslerSQLEngine.dll
12-14-17  01:40PM               193832 PaesslerSQLEngineDBX.dll
12-14-17  01:40PM               331536 paesslerVMWareShell.exe
12-14-17  01:40PM               310032 paesslerVMWareShell.vshost.exe
12-14-17  01:40PM                 1429 phantomjs-license.bsd
12-14-17  01:40PM                 1428 protocol.txt
02-16-18  11:04AM              6379096 PRTG Administrator.exe
02-16-18  11:05AM             12923480 PRTG Enterprise Console.exe
02-16-18  11:04AM              5439576 PRTG GUI Starter.exe
02-03-19  12:17AM       <DIR>          PRTG Installer Archive
02-16-18  11:05AM             11647576 PRTG Probe.exe
02-16-18  11:05AM              7026776 PRTG Server.exe
02-03-19  12:18AM              2000256 PRTG Setup Log.log
02-03-19  12:17AM       <DIR>          prtg-installer-for-distribution
12-14-17  01:40PM               300318 prtg.ico
12-14-17  01:40PM               444640 PrtgDllWrapper.exe
02-16-18  11:04AM              2778200 PRTGProbeUpdate.exe
02-16-18  11:04AM              3227224 PrtgRemoteInstall.exe
02-16-18  11:04AM              2782808 PRTGServerUpdate.exe
02-16-18  11:04AM              2104408 PRTG_Chromium_Helper.exe
02-16-18  11:04AM              2264664 PRTG_IE_Helper.exe
02-03-19  12:17AM       <DIR>          Python34
02-16-18  11:04AM              1012224 RegWrapper.exe
02-03-19  12:17AM       <DIR>          Sensor System
02-03-19  12:17AM       <DIR>          snmplibs
02-03-19  12:18AM       <DIR>          snmptemp
01-18-18  11:03AM               461824 ssh.dll
12-14-17  01:40PM               384512 ssleay32.dll
02-03-19  12:18AM       <DIR>          themes
02-03-19  12:18AM              1275563 unins000.dat
02-03-19  12:15AM              1498815 unins000.exe
12-14-17  01:40PM              1163024 VimService2005.dll
12-14-17  01:40PM              4312848 VimService2005.XmlSerializers.dll
02-03-19  12:17AM       <DIR>          webroot
226 Transfer complete.
ftp> cd download
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53012|)
150 Opening ASCII mode data connection.
12-10-18  02:58PM            195443176 PRTG Network Monitor 18.4.47.1962 Setup (Stable).exe
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53013|)
150 Opening ASCII mode data connection.
02-03-19  12:17AM       <DIR>          64 bit
02-03-19  12:15AM                 1888 activation.dat
02-03-19  12:18AM       <DIR>          cert
12-14-17  01:40PM              2461696 chartdir51.dll
12-14-17  01:40PM              9077248 ChilkatDelphiXE.dll
12-14-17  01:40PM              2138986 chrome.pak
02-03-19  12:17AM       <DIR>          Custom Sensors
12-14-17  01:40PM               382464 dbexpmda40.dll
12-14-17  01:40PM               519680 dbexpoda40.dll
12-14-17  01:40PM               377856 dbexpsda40.dll
12-14-17  01:40PM                 5681 defaultmaps.xml
12-14-17  01:40PM                12871 defaultmaps_iad.xml
02-13-18  03:08PM                 1224 deviceiconlist.txt
02-03-19  12:17AM       <DIR>          devicetemplates
05-16-25  08:15AM       <DIR>          dlltemp
02-03-19  12:18AM       <DIR>          download
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 6218 FlowRules.osr
02-03-19  12:18AM       <DIR>          helperlibs
12-14-17  01:40PM              9956864 icudt.dll
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-03-19  12:16AM       <DIR>          language
12-14-17  01:40PM              3707349 Lb2to3.exe
12-14-17  01:40PM             24978944 libcef.dll
12-14-17  01:40PM              1412096 libeay32.dll
02-03-19  12:17AM       <DIR>          locales
02-03-19  12:18AM       <DIR>          lookups
02-16-18  11:03AM               796566 macmanufacturerlist.txt
02-03-19  12:18AM       <DIR>          MIB
12-14-17  01:40PM                  522 Microsoft.VC80.CRT.manifest
12-14-17  01:40PM               421200 msvcp100.dll
12-14-17  01:40PM               770384 msvcr100.dll
12-14-17  01:40PM               630544 msvcr80.dll
12-14-17  01:40PM                12498 netsnmp-license.txt
02-03-19  12:17AM       <DIR>          Notifications
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM               487936 openssl.exe
01-18-18  11:03AM               177152 paelibssh.dll
12-14-17  01:40PM                35088 paesslerchart.dll
12-14-17  01:40PM              1083904 PaesslerSNMP.dll
02-15-18  05:24PM              1074688 PaesslerSNMPWrapper.dll
12-14-17  01:40PM               421160 PaesslerSQLEngine.dll
12-14-17  01:40PM               193832 PaesslerSQLEngineDBX.dll
12-14-17  01:40PM               331536 paesslerVMWareShell.exe
12-14-17  01:40PM               310032 paesslerVMWareShell.vshost.exe
12-14-17  01:40PM                 1429 phantomjs-license.bsd
12-14-17  01:40PM                 1428 protocol.txt
02-16-18  11:04AM              6379096 PRTG Administrator.exe
02-16-18  11:05AM             12923480 PRTG Enterprise Console.exe
02-16-18  11:04AM              5439576 PRTG GUI Starter.exe
02-03-19  12:17AM       <DIR>          PRTG Installer Archive
02-16-18  11:05AM             11647576 PRTG Probe.exe
02-16-18  11:05AM              7026776 PRTG Server.exe
02-03-19  12:18AM              2000256 PRTG Setup Log.log
02-03-19  12:17AM       <DIR>          prtg-installer-for-distribution
12-14-17  01:40PM               300318 prtg.ico
12-14-17  01:40PM               444640 PrtgDllWrapper.exe
02-16-18  11:04AM              2778200 PRTGProbeUpdate.exe
02-16-18  11:04AM              3227224 PrtgRemoteInstall.exe
02-16-18  11:04AM              2782808 PRTGServerUpdate.exe
02-16-18  11:04AM              2104408 PRTG_Chromium_Helper.exe
02-16-18  11:04AM              2264664 PRTG_IE_Helper.exe
02-03-19  12:17AM       <DIR>          Python34
02-16-18  11:04AM              1012224 RegWrapper.exe
02-03-19  12:17AM       <DIR>          Sensor System
02-03-19  12:17AM       <DIR>          snmplibs
02-03-19  12:18AM       <DIR>          snmptemp
01-18-18  11:03AM               461824 ssh.dll
12-14-17  01:40PM               384512 ssleay32.dll
02-03-19  12:18AM       <DIR>          themes
02-03-19  12:18AM              1275563 unins000.dat
02-03-19  12:15AM              1498815 unins000.exe
12-14-17  01:40PM              1163024 VimService2005.dll
12-14-17  01:40PM              4312848 VimService2005.XmlSerializers.dll
02-03-19  12:17AM       <DIR>          webroot
226 Transfer complete.
ftp> dir *.txt
229 Entering Extended Passive Mode (|||53014|)
150 Opening ASCII mode data connection.
02-13-18  03:08PM                 1224 deviceiconlist.txt
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-16-18  11:03AM               796566 macmanufacturerlist.txt
12-14-17  01:40PM                12498 netsnmp-license.txt
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM                 1428 protocol.txt
226 Transfer complete.
ftp> dir *txt
229 Entering Extended Passive Mode (|||53015|)
125 Data connection already open; Transfer starting.
02-13-18  03:08PM                 1224 deviceiconlist.txt
12-14-17  01:40PM                 6667 ethertype.txt
12-14-17  01:40PM                 1665 ipmi_bsd-2.0.txt
02-16-18  11:03AM               796566 macmanufacturerlist.txt
12-14-17  01:40PM                12498 netsnmp-license.txt
12-14-17  01:40PM                    0 Npgsql.txt
12-14-17  01:40PM                 1428 protocol.txt
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53016|)
125 Data connection already open; Transfer starting.
07-16-16  09:18AM       <DIR>          Common Files
07-16-16  09:18AM       <DIR>          internet explorer
07-16-16  09:18AM       <DIR>          Microsoft.NET
05-16-25  08:15AM       <DIR>          PRTG Network Monitor
11-20-16  09:53PM       <DIR>          Windows Defender
07-16-16  09:18AM       <DIR>          WindowsPowerShell
226 Transfer complete.
ftp> cd internet explorer
usage: cd remote-directory
ftp> cd "internet explorer
Common Files            PRTG Network Monitor    WindowsPowerShell
Microsoft.NET           Windows Defender        internet explorer
ftp> cd "internet explorer"
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53027|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53030|)
125 Data connection already open; Transfer starting.
07-16-16  09:18AM       <DIR>          Common Files
07-16-16  09:18AM       <DIR>          internet explorer
07-16-16  09:18AM       <DIR>          Microsoft.NET
05-16-25  08:15AM       <DIR>          PRTG Network Monitor
11-20-16  09:53PM       <DIR>          Windows Defender
07-16-16  09:18AM       <DIR>          WindowsPowerShell
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53038|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd "program files"
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53040|)
125 Data connection already open; Transfer starting.
02-25-19  10:56PM       <DIR>          Common Files
07-16-16  09:18AM       <DIR>          internet explorer
02-25-19  10:56PM       <DIR>          VMware
11-20-16  09:53PM       <DIR>          Windows Defender
07-16-16  09:18AM       <DIR>          WindowsPowerShell
02-03-19  12:18AM       <DIR>          WinPcap
226 Transfer complete.
ftp> cd winpcap
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53041|)
125 Data connection already open; Transfer starting.
08-18-14  11:07PM                13713 LICENSE
08-18-14  11:07PM               118520 rpcapd.exe
02-03-19  12:18AM                58127 uninstall.exe
226 Transfer complete.
ftp> cd ..cd ..
usage: cd remote-directory
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53051|)
125 Data connection already open; Transfer starting.
02-25-19  10:56PM       <DIR>          Common Files
07-16-16  09:18AM       <DIR>          internet explorer
02-25-19  10:56PM       <DIR>          VMware
11-20-16  09:53PM       <DIR>          Windows Defender
07-16-16  09:18AM       <DIR>          WindowsPowerShell
02-03-19  12:18AM       <DIR>          WinPcap
226 Transfer complete.
ftp> cd internet\ explorer
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53053|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53054|)
150 Opening ASCII mode data connection.
02-25-19  10:56PM       <DIR>          Common Files
07-16-16  09:18AM       <DIR>          internet explorer
02-25-19  10:56PM       <DIR>          VMware
11-20-16  09:53PM       <DIR>          Windows Defender
07-16-16  09:18AM       <DIR>          WindowsPowerShell
02-03-19  12:18AM       <DIR>          WinPcap
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53055|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd perflogs
550 Access is denied. 
ftp> cd inetpub
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53056|)
150 Opening ASCII mode data connection.
02-25-19  08:07AM       <DIR>          ftproot
02-25-19  10:15PM       <DIR>          logs
02-25-19  10:15PM       <DIR>          temp
02-25-19  10:15PM       <DIR>          wwwroot
226 Transfer complete.
ftp> dir ftproot
229 Entering Extended Passive Mode (|||53132|)
150 Opening ASCII mode data connection.
226 Transfer complete.
ftp> dir logs
229 Entering Extended Passive Mode (|||53133|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          FailedReqLogFiles
02-25-19  09:52PM       <DIR>          LogFiles
02-25-19  10:15PM       <DIR>          wmsvc
226 Transfer complete.
ftp> dir loags/fa
550 The system cannot find the file specified. 
ftp> dir loags/failerreqlogfiles
229 Entering Extended Passive Mode (|||53135|)
550 The system cannot find the path specified. 
ftp> dir temp
229 Entering Extended Passive Mode (|||53136|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> dir wwwroot
229 Entering Extended Passive Mode (|||53137|)
125 Data connection already open; Transfer starting.
226 Transfer complete.
ftp> dir
229 Entering Extended Passive Mode (|||53138|)
125 Data connection already open; Transfer starting.
02-25-19  08:07AM       <DIR>          ftproot
02-25-19  10:15PM       <DIR>          logs
02-25-19  10:15PM       <DIR>          temp
02-25-19  10:15PM       <DIR>          wwwroot
226 Transfer complete.
ftp> cd logs
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53141|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          FailedReqLogFiles
02-25-19  09:52PM       <DIR>          LogFiles
02-25-19  10:15PM       <DIR>          wmsvc
226 Transfer complete.
ftp> cd failerreqlogfiles
550 The system cannot find the file specified. 
ftp> cd failedreqlogfiles
550 Access is denied. 
ftp> cd logfiles
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53150|)
150 Opening ASCII mode data connection.
05-16-25  08:28AM       <DIR>          FTPSVC73478387
226 Transfer complete.
ftp> cd ftpsvc73478387
550 Access is denied. 
ftp> dir
229 Entering Extended Passive Mode (|||53161|)
150 Opening ASCII mode data connection.
05-16-25  08:28AM       <DIR>          FTPSVC73478387
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53162|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          FailedReqLogFiles
02-25-19  09:52PM       <DIR>          LogFiles
02-25-19  10:15PM       <DIR>          wmsvc
226 Transfer complete.
ftp> cd wmsvc
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53163|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          W3SVC1
226 Transfer complete.
ftp> cd w3svc1
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53164|)
150 Opening ASCII mode data connection.
02-25-19  10:48PM                27195 ex190226.log
226 Transfer complete.
ftp> get ex190226.log
local: ex190226.log remote: ex190226.log
229 Entering Extended Passive Mode (|||53166|)
150 Opening ASCII mode data connection.
100% |******************************************************************| 27195      535.53 KiB/s    00:00 ETA
226 Transfer complete.
27195 bytes received in 00:00 (533.69 KiB/s)
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53167|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          W3SVC1
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53168|)
150 Opening ASCII mode data connection.
02-25-19  10:15PM       <DIR>          FailedReqLogFiles
02-25-19  09:52PM       <DIR>          LogFiles
02-25-19  10:15PM       <DIR>          wmsvc
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53169|)
150 Opening ASCII mode data connection.
02-25-19  08:07AM       <DIR>          ftproot
02-25-19  10:15PM       <DIR>          logs
02-25-19  10:15PM       <DIR>          temp
02-25-19  10:15PM       <DIR>          wwwroot
226 Transfer complete.
ftp> cd ..
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53172|)
150 Opening ASCII mode data connection.
02-03-19  12:18AM                 1024 .rnd
02-25-19  10:15PM       <DIR>          inetpub
07-16-16  09:18AM       <DIR>          PerfLogs
02-25-19  10:56PM       <DIR>          Program Files
02-03-19  12:28AM       <DIR>          Program Files (x86)
02-03-19  08:08AM       <DIR>          Users
05-16-25  09:23AM       <DIR>          Windows
226 Transfer complete.
ftp> cd windows
250 CWD command successful.
ftp> dir
229 Entering Extended Passive Mode (|||53180|)
150 Opening ASCII mode data connection.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:22AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  09:20AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> get win.ini
local: win.ini remote: win.ini
229 Entering Extended Passive Mode (|||53181|)
125 Data connection already open; Transfer starting.
100% |******************************************************************|    92        3.90 KiB/s    00:00 ETA
226 Transfer complete.
92 bytes received in 00:00 (3.87 KiB/s)
ftp> dir
229 Entering Extended Passive Mode (|||53182|)
150 Opening ASCII mode data connection.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:22AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  09:20AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> dir *in
229 Entering Extended Passive Mode (|||53183|)
150 Opening ASCII mode data connection.
07-16-16  09:12AM                43131 mib.bin
226 Transfer complete.
ftp> dir *ini
229 Entering Extended Passive Mode (|||53184|)
125 Data connection already open; Transfer starting.
07-16-16  09:16AM                  219 system.ini
07-16-16  09:16AM                   92 win.ini
226 Transfer complete.
ftp> get system.ini
local: system.ini remote: system.ini
229 Entering Extended Passive Mode (|||53185|)
150 Opening ASCII mode data connection.
100% |******************************************************************|   219        9.34 KiB/s    00:00 ETA
226 Transfer complete.
219 bytes received in 00:00 (9.22 KiB/s)
ftp> dir *log
229 Entering Extended Passive Mode (|||53187|)
150 Opening ASCII mode data connection.
02-03-19  08:05AM                 4056 DtcInstall.log
02-25-19  10:15PM                12899 iis.log
11-20-16  10:15PM                 1344 lsasetup.log
11-10-23  10:20AM                  372 PFRO.log
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
05-16-25  09:20AM                  275 WindowsUpdate.log
226 Transfer complete.
ftp> get iis.log
local: iis.log remote: iis.log
229 Entering Extended Passive Mode (|||53197|)
550 Access is denied. 
ftp> dir
229 Entering Extended Passive Mode (|||53198|)
125 Data connection already open; Transfer starting.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:22AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  09:20AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> cd temp
550 Access is denied. 
ftp> dir
229 Entering Extended Passive Mode (|||53199|)
150 Opening ASCII mode data connection.
11-20-16  09:53PM       <DIR>          ADFS
07-16-16  09:18AM       <DIR>          AppCompat
11-20-16  09:59PM       <DIR>          AppPatch
02-25-19  08:07AM       <DIR>          assembly
07-16-16  09:13AM                61440 bfsvc.exe
07-16-16  09:18AM       <DIR>          Boot
05-16-25  08:17AM                67584 bootstat.dat
07-16-16  09:18AM       <DIR>          Branding
02-25-19  11:42PM       <DIR>          CbsTemp
02-03-19  08:05AM       <DIR>          debug
07-16-16  09:18AM       <DIR>          diagnostics
07-16-16  09:18AM       <DIR>          drivers
02-03-19  08:05AM                 4056 DtcInstall.log
11-20-16  09:53PM       <DIR>          en-US
11-20-16  09:59PM       <DIR>          Fonts
11-20-16  10:09PM       <DIR>          Globalization
11-20-16  09:53PM       <DIR>          Help
02-25-19  10:15PM                12899 iis.log
07-16-16  09:18AM       <DIR>          IME
02-25-19  10:56PM       <DIR>          INF
07-16-16  09:18AM       <DIR>          InfusedApps
07-16-16  09:18AM       <DIR>          InputMethod
07-16-16  09:18AM       <DIR>          L2Schemas
07-16-16  09:18AM       <DIR>          LiveKernelReports
11-20-16  10:15PM       <DIR>          Logs
11-20-16  10:15PM                 1344 lsasetup.log
07-16-16  09:12AM                43131 mib.bin
05-16-25  08:25AM       <DIR>          Microsoft.NET
07-16-16  09:18AM       <DIR>          Migration
11-20-16  10:12PM       <DIR>          OCR
02-03-19  08:05AM       <DIR>          Panther
11-10-23  10:20AM                  372 PFRO.log
07-16-16  09:18AM       <DIR>          PLA
11-20-16  10:36PM       <DIR>          PolicyDefinitions
07-16-16  09:18AM       <DIR>          Provisioning
02-25-19  10:54PM              1189697 PRTG Configuration.dat
07-16-16  09:13AM               320512 regedit.exe
05-16-25  08:15AM       <DIR>          Registration
07-16-16  09:18AM       <DIR>          RemotePackages
12-15-21  10:48AM       <DIR>          rescache
07-16-16  09:18AM       <DIR>          Resources
02-25-19  11:49PM                  140 restart.bat
07-16-16  09:18AM       <DIR>          SchCache
07-16-16  09:18AM       <DIR>          schemas
07-16-16  09:18AM       <DIR>          security
11-20-16  10:15PM       <DIR>          ServiceProfiles
11-20-16  09:53PM       <DIR>          servicing
07-16-16  09:19AM       <DIR>          Setup
02-03-19  08:05AM                 6894 setupact.log
11-20-16  10:15PM                    0 setuperr.log
11-20-16  10:09PM       <DIR>          SKB
02-03-19  12:13AM       <DIR>          SoftwareDistribution
11-20-16  10:12PM       <DIR>          Speech
11-20-16  10:12PM       <DIR>          Speech_OneCore
11-20-16  09:59PM               130560 splwow64.exe
07-16-16  09:18AM       <DIR>          System
07-16-16  09:16AM                  219 system.ini
05-16-25  08:24AM       <DIR>          System32
07-16-16  09:18AM       <DIR>          SystemResources
02-25-19  10:56PM       <DIR>          SysWOW64
11-20-16  10:15PM       <DIR>          Tasks
05-16-25  09:22AM       <DIR>          Temp
07-16-16  09:18AM       <DIR>          tracing
07-16-16  09:18AM       <DIR>          Vss
07-16-16  09:18AM       <DIR>          Web
07-16-16  09:16AM                   92 win.ini
05-16-25  09:20AM                  275 WindowsUpdate.log
12-15-21  10:47AM       <DIR>          WinSxS
226 Transfer complete.
ftp> exit

```