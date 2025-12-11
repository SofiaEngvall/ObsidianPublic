
```
┌──(fixit42㉿kali)-[~]
└─$ cd Downloads   
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ ls -la
total 85060
drwxr-xr-x  4 fixit42 fixit42     4096 Dec  5 23:24 .
drwx------ 43 fixit42 fixit42     4096 Dec  5 23:24 ..
-rw-r--r--  1 fixit42 fixit42   165712 Jul 23 20:40 ad_sampledata.zip
-rw-rw-r--  1 fixit42 fixit42      939 Jul 26 19:29 cacert.der
-rw-rw-r--  1 fixit42 fixit42      152 Nov 21 03:04 clean.py
drwxrwxr-x  3 fixit42 fixit42     4096 Aug  2 16:44 firensics
-rw-rw-r--  1 fixit42 fixit42      829 Nov 21 02:47 flag-parser.py
-rw-rw-r--  1 fixit42 fixit42   200571 Nov 21 00:04 FLAG.txt
-rw-rw-r--  1 fixit42 fixit42      178 Nov 21 02:57 hex-dump.py
-rw-rw-r--  1 fixit42 fixit42 51690104 Dec  5 23:24 Logs.7z
drwx------  6 fixit42 fixit42     4096 Oct 17 14:44 rev_spellbrewery
-rwxrwxr-x  1 fixit42 fixit42    38824 Nov 21 00:11 signal_signal_little_star
-rw-rw-r--  1 fixit42 fixit42      865 Nov 21 03:10 solver.py
-rw-rw-r--  1 fixit42 fixit42    66355 Oct 17 11:06 spellbrewery.zip
-rw-rw-r--  1 fixit42 fixit42 34886006 Nov 21 00:12 Stomaker.zip
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ unzip Logs.7z                    
Archive:  Logs.7z
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of Logs.7z or
        Logs.7z.zip, and cannot find Logs.7z.ZIP, period.
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ sudo apt install 7zip    
[sudo] password for fixit42: 
7zip is already the newest version (25.01+dfsg-4).
7zip set to manually installed.
The following packages were automatically installed and are no longer required:
  gir1.2-girepository-2.0  libgirepository-1.0-1  libobjc-14-dev       python3-click-plugins  python3-xlutils
  libarmadillo14           libgpgmepp6t64         libosmesa6           python3-multipart      ruby-childprocess
  libdisplay-info2         libgps30t64            libradare2-5.0.0t64  python3-py             soapysdr0.8-module-rfspace
  libgdal37                libinstpatch-1.0-2     libsqlcipher1        python3-pysmi          tini
  libgeos3.14.0            libnet1                libuhd4.8.0          python3-roman          yersinia
Use 'sudo apt autoremove' to remove them.

Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 48
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ 7zip                           
Command '7zip' not found, did you mean:
  command 'qzip' from deb qatzip
  command 'zip' from deb zip
  command 'p7zip' from deb p7zip
  command 'p7zip' from deb 7zip
  command 'rzip' from deb rzip
  command 'wzip' from deb wzip
  command 'mzip' from deb mtools
  command 'gzip' from deb gzip
Try: sudo apt install <deb name>
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ p7zip             
/usr/bin/p7zip: compressed data not written to a terminal.
For help, type: /usr/bin/p7zip -h
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ p7zip -h
Usage: /usr/bin/p7zip [options] [--] [ name ... ]

Options:
    -c --stdout --to-stdout      output data to stdout
    -d --decompress --uncompress decompress file
    -f --force                   do not ask questions
    -k --keep                    keep original file
    -h --help                    print this help
    --                           treat subsequent arguments as file
                                 names, even if they start with a dash

                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ ls -la
total 85060
drwxr-xr-x  4 fixit42 fixit42     4096 Dec  5 23:24 .
drwx------ 43 fixit42 fixit42     4096 Dec  5 23:24 ..
-rw-r--r--  1 fixit42 fixit42   165712 Jul 23 20:40 ad_sampledata.zip
-rw-rw-r--  1 fixit42 fixit42      939 Jul 26 19:29 cacert.der
-rw-rw-r--  1 fixit42 fixit42      152 Nov 21 03:04 clean.py
drwxrwxr-x  3 fixit42 fixit42     4096 Aug  2 16:44 firensics
-rw-rw-r--  1 fixit42 fixit42      829 Nov 21 02:47 flag-parser.py
-rw-rw-r--  1 fixit42 fixit42   200571 Nov 21 00:04 FLAG.txt
-rw-rw-r--  1 fixit42 fixit42      178 Nov 21 02:57 hex-dump.py
-rw-rw-r--  1 fixit42 fixit42 51690104 Dec  5 23:24 Logs.7z
drwx------  6 fixit42 fixit42     4096 Oct 17 14:44 rev_spellbrewery
-rwxrwxr-x  1 fixit42 fixit42    38824 Nov 21 00:11 signal_signal_little_star
-rw-rw-r--  1 fixit42 fixit42      865 Nov 21 03:10 solver.py
-rw-rw-r--  1 fixit42 fixit42    66355 Oct 17 11:06 spellbrewery.zip
-rw-rw-r--  1 fixit42 fixit42 34886006 Nov 21 00:12 Stomaker.zip
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ p7zip -d -k Logs.7z

7-Zip (a) 25.01 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
 64-bit locale=en_US.UTF-8 Threads:128 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 51690104 bytes (50 MiB)

Extracting archive: Logs.7z
--
Path = Logs.7z
Type = 7z
Physical Size = 51690104
Headers Size = 31639
Method = LZMA2:28 LZMA:20 BCJ2
Solid = +
Blocks = 2

Everything is Ok                                                                                                            

Folders: 413
Files: 1350
Size:       814801135
Compressed: 51690104
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ ls -la
total 85064
drwxr-xr-x  5 fixit42 fixit42     4096 Dec  5 23:42 .
drwx------ 43 fixit42 fixit42     4096 Dec  5 23:24 ..
-rw-r--r--  1 fixit42 fixit42   165712 Jul 23 20:40 ad_sampledata.zip
-rw-rw-r--  1 fixit42 fixit42      939 Jul 26 19:29 cacert.der
-rw-rw-r--  1 fixit42 fixit42      152 Nov 21 03:04 clean.py
drwxrwxr-x  3 fixit42 fixit42     4096 Aug  2 16:44 firensics
-rw-rw-r--  1 fixit42 fixit42      829 Nov 21 02:47 flag-parser.py
-rw-rw-r--  1 fixit42 fixit42   200571 Nov 21 00:04 FLAG.txt
-rw-rw-r--  1 fixit42 fixit42      178 Nov 21 02:57 hex-dump.py
drwxrwxr-x  7 fixit42 fixit42     4096 Nov 25 12:29 Logs
-rw-rw-r--  1 fixit42 fixit42 51690104 Dec  5 23:24 Logs.7z
drwx------  6 fixit42 fixit42     4096 Oct 17 14:44 rev_spellbrewery
-rwxrwxr-x  1 fixit42 fixit42    38824 Nov 21 00:11 signal_signal_little_star
-rw-rw-r--  1 fixit42 fixit42      865 Nov 21 03:10 solver.py
-rw-rw-r--  1 fixit42 fixit42    66355 Oct 17 11:06 spellbrewery.zip
-rw-rw-r--  1 fixit42 fixit42 34886006 Nov 21 00:12 Stomaker.zip
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads]
└─$ cd Logs                      
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -la
total 213720
drwxrwxr-x 7 fixit42 fixit42      4096 Nov 25 12:29  .
drwxr-xr-x 5 fixit42 fixit42      4096 Dec  5 23:42  ..
-rw-rw-r-- 1 fixit42 fixit42      8192 Nov 24 14:44 '$Boot'
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 '$Extend'
-rw-rw-r-- 1 fixit42 fixit42  57360384 Nov 24 14:42 '$LogFile'
-rw-rw-r-- 1 fixit42 fixit42 158859264 Mar 19  2019 '$MFT'
-rw-rw-r-- 1 fixit42 fixit42   2582676 Mar 19  2019 '$Secure_$SDS'
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28  ProgramData
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 'Program Files (x86)'
drwxrwxr-x 7 fixit42 fixit42      4096 Nov 25 12:29  Users
drwxrwxr-x 8 fixit42 fixit42      4096 Nov 25 12:29  Windows
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -la *   
-rw-rw-r-- 1 fixit42 fixit42      8192 Nov 24 14:44 '$Boot'
-rw-rw-r-- 1 fixit42 fixit42  57360384 Nov 24 14:42 '$LogFile'
-rw-rw-r-- 1 fixit42 fixit42 158859264 Mar 19  2019 '$MFT'
-rw-rw-r-- 1 fixit42 fixit42   2582676 Mar 19  2019 '$Secure_$SDS'

'$Extend':
total 39872
drwxrwxr-x 3 fixit42 fixit42     4096 Nov 25 12:28  .
drwxrwxr-x 7 fixit42 fixit42     4096 Nov 25 12:29  ..
-rw-rw-r-- 1 fixit42 fixit42 40811040 Mar 19  2019 '$J'
-rw-rw-r-- 1 fixit42 fixit42       32 Mar 19  2019 '$Max'
drwxrwxr-x 3 fixit42 fixit42     4096 Nov 25 12:28 '$RmMetadata'

ProgramData:
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 ..
drwxrwxr-x 6 fixit42 fixit42 4096 Nov 25 12:29 Microsoft

'Program Files (x86)':
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 Splashtop

Users:
total 28
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 .
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 Default
drwxrwxr-x 4 fixit42 fixit42 4096 Nov 25 12:29 IEUser
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 jowi
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 Public
drwxrwxr-x 4 fixit42 fixit42 4096 Nov 25 12:29 svc_patch.MSEDGEWIN10

Windows:
total 44
drwxrwxr-x  8 fixit42 fixit42  4096 Nov 25 12:29 .
drwxrwxr-x  7 fixit42 fixit42  4096 Nov 25 12:29 ..
drwxrwxr-x  3 fixit42 fixit42  4096 Nov 25 12:29 AppCompat
drwxrwxr-x  2 fixit42 fixit42  4096 Nov 25 12:29 inf
drwxrwxr-x  2 fixit42 fixit42 16384 Nov 25 12:29 prefetch
drwxrwxr-x  4 fixit42 fixit42  4096 Nov 25 12:29 ServiceProfiles
drwxrwxr-x 10 fixit42 fixit42  4096 Nov 25 12:29 System32
drwxrwxr-x  2 fixit42 fixit42  4096 Nov 25 12:29 Temp
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd program files
cd: string not in pwd: program
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd Program\ Files\ \(x86\) 
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)]
└─$ ls -la  
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 Splashtop
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)]
└─$ cd Splashtop              
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)/Splashtop]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28  .
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28  ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 'Splashtop Remote'
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)/Splashtop]
└─$ cd Splashtop\ Remote 
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Logs/Program Files (x86)/Splashtop/Splashtop Remote]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 Server
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Logs/Program Files (x86)/Splashtop/Splashtop Remote]
└─$ x Server 
x: command not found
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Logs/Program Files (x86)/Splashtop/Splashtop Remote]
└─$ cd Server           
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Program Files (x86)/Splashtop/Splashtop Remote/Server]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 ..
drwxrwxr-x 2 fixit42 fixit42 4096 Nov 25 12:28 log
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Program Files (x86)/Splashtop/Splashtop Remote/Server]
└─$ cd log                       
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ ls -la
total 44
drwxrwxr-x 2 fixit42 fixit42  4096 Nov 25 12:28 .
drwxrwxr-x 3 fixit42 fixit42  4096 Nov 25 12:28 ..
-rw-rw-r-- 1 fixit42 fixit42  9819 Nov 24 14:36 agent_log.txt
-rw-rw-r-- 1 fixit42 fixit42 12009 Nov 24 14:36 SPLog.txt
-rw-rw-r-- 1 fixit42 fixit42   351 Nov 24 14:36 svcinfo.txt
-rw-rw-r-- 1 fixit42 fixit42   709 Nov 24 14:36 sysinfo.txt
-rw-rw-r-- 1 fixit42 fixit42   271 Nov 24 14:37 vrdis_log.txt
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cat agent_log.txt 
<1>Nov24 05:36:55.072    12152[App] ==== 0 SRAgent v3.8.0.1 start 12152 (2) ====
<1>Nov24 05:36:55.076    12152[App] os version : 0x0A00 (workstation)
<1>Nov24 05:36:55.086    12152[App] lang : 1033, 1033, 1033, 1033, 1033, 1033
<6>Nov24 05:36:55.243    12152[App] Reg WTS 1 (0)
<1>Nov24 05:36:55.280    12152[App] tc start (13 - 7099265)
<1>Nov24 05:36:56.625    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:36:56
<0>Nov24 05:36:56.646    12152[AgentHelper] failed to convert time string, , -1--1--1 -1:-1:-1
<0>Nov24 05:36:56.648    12152[AgentHelper] failed to convert time string with scanf
<1>Nov24 05:36:56.672    12152[Handler] load emm update manual sync default table version - [1.0.5.12]
<1>Nov24 05:36:56.689    12152[Handler] TSS, 1-1020, 0x03638F40(0x00003448)
<1>Nov24 05:36:56.692    12152[Handler] TF1, 1-1020, 0x03638F40(0x00003448)
<1>Nov24 05:36:57.495    12152[SecuIPC] role 12 set role 1 encryption info
<1>Nov24 05:36:58.863    12152[SystemUpdateHelper] WUA Version : 10.0.17763.168
<1>Nov24 05:36:59.248    12152[Handler] update system update info
<1>Nov24 05:36:59.248    12152[Handler] TF2, 1-1020, 0x03638F40(0x00003448)
<0>Nov24 05:36:59.691    12152[PipeIPC] IPC WriteCommPipe time out
<0>Nov24 05:36:59.691    12152[SecuIPC] failed to send encryption info 1
<1>Nov24 05:36:59.692    12152[SecuIPC] role 12 replace role 1 encryption info
<0>Nov24 05:37:00.206    12152[PipeIPC] CreateFile for pipe \\.\pipe\PIPE_SRAGENTUI_0 fail error=2
<0>Nov24 05:37:00.350    12152[SecuIPC] failed to send encryption info 14
<1>Nov24 05:37:00.350    12152[Manager] TA1, 1-1013, 0, 2025/11/24 05:37:01
<1>Nov24 05:37:00.350    12152[Manager] TA1, 1-1022, 0, 2025/11/24 05:37:00
<1>Nov24 05:37:00.359    12152[Manager] TA1, 64-113, 0, 2025/11/24 05:37:00
<1>Nov24 05:37:00.360    12152[Manager] TA1, 32-200, 0, 2025/11/24 05:37:10
<1>Nov24 05:37:00.360    12152[Manager] TA1, 256-101, 0, 2025/11/24 05:37:30
<1>Nov24 05:37:00.398    12152[Handler] TSS, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:00.398    12152[Handler] TSS, 1-1022, 0x0368ED80(0x000019C0)
<1>Nov24 05:37:00.399    12152[Handler] TF1, 1-1022, 0x0368ED80(0x000019C0)
<0>Nov24 05:37:00.399    12152[AgentHelper] failed to convert time string, , -1--1--1 -1:-1:-1
<0>Nov24 05:37:00.399    12152[AgentHelper] failed to convert time string with scanf
<1>Nov24 05:37:00.424    12152[Handler] checking inventory, the last inventory scan time does not exist
<1>Nov24 05:37:00.424    12152[Handler] TF2, 1-1022, 0x0368ED80(0x000019C0)
<1>Nov24 05:37:00.942    12152[Handler] TF1, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:00.944    12152[Handler] TF2, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:01.561    12152[Handler] TSS, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:01.561    12152[Handler] TF1, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:01.611    12152[Handler] using the last reboot time from event log: 2025-11-24 03:38:31 -0800 -> 2025-11-24 14:38:38 -0800
<1>Nov24 05:37:02.626    12152[Handler] using the last reboot time from event log: 2025-11-24 03:38:31 -0800 -> 2025-11-24 14:38:38 -0800
<1>Nov24 05:37:02.679    12152[Handler] TF2, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:10.410    12152[Handler] TSS, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:11.732    12152[Handler] NBIPC - SetCloudRegion
<1>Nov24 05:37:11.732    12152[Handler] cloud region US
<1>Nov24 05:37:14.961    12152[Handler] TF1, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:16.099    12152[Handler] TF2, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:16.910    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:18.866    12152[Handler] NBIPC - SetCloudRegion
<1>Nov24 05:37:18.866    12152[Handler] cloud region US
<1>Nov24 05:37:18.946    12152[Handler] IPC - GetAlertSetting
<1>Nov24 05:37:19.077    12152[Handler] IPC - GetInventorySetting
<1>Nov24 05:37:19.149    12152[Handler] IPC - GetAvSetting
<1>Nov24 05:37:19.245    12152[Handler] IPC - GetSysUpdateSetting
<1>Nov24 05:37:19.314    12152[Handler] IPC - GetScheRebootSetting
<1>Nov24 05:37:19.408    12152[Handler] IPC - GetScheSysUpdateSetting
<1>Nov24 05:37:19.483    12152[Handler] IPC - GetScheCmdSetting
<1>Nov24 05:37:19.556    12152[Handler] IPC - GetScheExeSetting
<1>Nov24 05:37:19.625    12152[Handler] IPC - GetScheMsiSetting
<1>Nov24 05:37:19.701    12152[Handler] IPC - GetScheFileDispatchSetting
<1>Nov24 05:37:19.794    12152[Handler] IPC - GetScheSmartActionSetting
<1>Nov24 05:37:19.891    12152[Handler] IPC - GetSysInfo
<1>Nov24 05:37:19.891    12152[Handler] capability 0014038F8FD2FF787F7FF87FF7FFFFBF7FFFFFFB7FFFFFFF
<1>Nov24 05:37:19.891    12152[Handler] sys_info, start
<1>Nov24 05:37:20.263    12152[Handler] sys_info - basic : 343831
<1>Nov24 05:37:20.263    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:37:20
<1>Nov24 05:37:20.323    12152[Handler] TSS, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.323    12152[Handler] TF1, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.403    12152[Handler] sys_info - su : 127261
<1>Nov24 05:37:20.485    12152[Handler] update system update info
<1>Nov24 05:37:20.485    12152[Handler] TF2, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.486    12152[Handler] sys_info - av : 74884
<1>Nov24 05:37:20.526    12152[Handler] sys_info, len = 435
<1>Nov24 05:37:20.526    12152[Handler] sys_info, write reg
<1>Nov24 05:37:20.526    12152[Handler] sys_info, stop
<1>Nov24 05:37:20.541    12152[Handler] IPC - GetEmmAllPolicies
<1>Nov24 05:37:23.400    12152[Handler] NBIPC - 1083
<1>Nov24 05:37:23.419    12152[Handler] emm patch, start, no policy, reset emm patch
<1>Nov24 05:37:23.563    12152[Handler] NBIPC - SetInventorySetting
<1>Nov24 05:37:23.756    12152[Handler] NBIPC - SetSysUpdateSetting
<1>Nov24 05:37:23.800    12152[Handler] IPC - GetAlertSetting
<1>Nov24 05:37:23.988    12152[Handler] NBIPC - SetScheRebootSetting
<1>Nov24 05:37:24.222    12152[Handler] NBIPC - SetScheSysUpdateSetting
<1>Nov24 05:37:24.436    12152[Handler] NBIPC - SetScheCmdSetting
<1>Nov24 05:37:24.631    12152[Handler] IPC - GetInventorySetting
<1>Nov24 05:37:24.699    12152[Handler] IPC - GetAvSetting
<1>Nov24 05:37:24.796    12152[Handler] IPC - GetSysUpdateSetting
<1>Nov24 05:37:27.726    12152[Handler] IPC - GetScheRebootSetting
<1>Nov24 05:37:27.767    12152[Handler] NBIPC - SetScheExeSetting
<1>Nov24 05:37:27.807    12152[Handler] IPC - GetScheSysUpdateSetting
<1>Nov24 05:37:27.920    12152[Handler] NBIPC - SetScheMsiSetting
<1>Nov24 05:37:27.921    12152[Handler] IPC - GetScheCmdSetting
<1>Nov24 05:37:28.030    12152[Handler] IPC - GetScheExeSetting
<1>Nov24 05:37:28.035    12152[Handler] NBIPC - SetScheFileDispatchSetting
<1>Nov24 05:37:28.197    12152[Handler] IPC - GetScheMsiSetting
<1>Nov24 05:37:28.265    12152[Handler] NBIPC - SetScheSmartActionSetting
<1>Nov24 05:37:28.349    12152[Handler] IPC - GetScheFileDispatchSetting
<1>Nov24 05:37:28.409    12152[Handler] IPC - GetScheSmartActionSetting
<1>Nov24 05:37:28.512    12152[Handler] IPC - GetSysInfo
<1>Nov24 05:37:28.512    12152[Handler] capability 0014038F8FD2FF787F7FF87FF7FFFFBF7FFFFFFB7FFFFFFF
<1>Nov24 05:37:28.512    12152[Handler] sys_info, start
<1>Nov24 05:37:28.677    12152[Handler] sys_info - basic : 149744
<1>Nov24 05:37:28.677    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:37:28
<1>Nov24 05:37:28.677    12152[Handler] TSS, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.677    12152[Handler] TF1, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.739    12152[Handler] sys_info - su : 56780
<1>Nov24 05:37:28.788    12152[Handler] update system update info
<1>Nov24 05:37:28.789    12152[Handler] TF2, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.789    12152[Handler] sys_info - av : 45383
<1>Nov24 05:37:28.834    12152[Handler] sys_info, len = 435
<1>Nov24 05:37:28.834    12152[Handler] sys_info, write reg
<1>Nov24 05:37:28.834    12152[Handler] sys_info, stop
<1>Nov24 05:37:28.847    12152[Handler] IPC - GetEmmAllPolicies
<1>Nov24 05:37:30.378    12152[Handler] TSS, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:30.379    12152[SRAgent::CDevicePostureTask::Perform] device posture task: osquery status check
<1>Nov24 05:37:31.947    12152[Handler] TF1, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:31.948    12152[Handler] update system status to report osquery status
<1>Nov24 05:37:31.948    12152[Manager] TA1, 1-1026, 0, 2025/11/24 05:37:31
<1>Nov24 05:37:31.948    12152[Handler] TF2, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:31.950    12152[Handler] TSS, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:31.950    12152[Handler] TF1, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:31.950    12152[Handler] TF2, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:34.704    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.761    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.840    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.950    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.979    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.036    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.061    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.095    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.144    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.173    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.202    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.233    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.265    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.344    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.409    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.489    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:37.217    12152[Handler] NBIPC - SetServerId
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cat *            
<1>Nov24 05:36:55.072    12152[App] ==== 0 SRAgent v3.8.0.1 start 12152 (2) ====
<1>Nov24 05:36:55.076    12152[App] os version : 0x0A00 (workstation)
<1>Nov24 05:36:55.086    12152[App] lang : 1033, 1033, 1033, 1033, 1033, 1033
<6>Nov24 05:36:55.243    12152[App] Reg WTS 1 (0)
<1>Nov24 05:36:55.280    12152[App] tc start (13 - 7099265)
<1>Nov24 05:36:56.625    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:36:56
<0>Nov24 05:36:56.646    12152[AgentHelper] failed to convert time string, , -1--1--1 -1:-1:-1
<0>Nov24 05:36:56.648    12152[AgentHelper] failed to convert time string with scanf
<1>Nov24 05:36:56.672    12152[Handler] load emm update manual sync default table version - [1.0.5.12]
<1>Nov24 05:36:56.689    12152[Handler] TSS, 1-1020, 0x03638F40(0x00003448)
<1>Nov24 05:36:56.692    12152[Handler] TF1, 1-1020, 0x03638F40(0x00003448)
<1>Nov24 05:36:57.495    12152[SecuIPC] role 12 set role 1 encryption info
<1>Nov24 05:36:58.863    12152[SystemUpdateHelper] WUA Version : 10.0.17763.168
<1>Nov24 05:36:59.248    12152[Handler] update system update info
<1>Nov24 05:36:59.248    12152[Handler] TF2, 1-1020, 0x03638F40(0x00003448)
<0>Nov24 05:36:59.691    12152[PipeIPC] IPC WriteCommPipe time out
<0>Nov24 05:36:59.691    12152[SecuIPC] failed to send encryption info 1
<1>Nov24 05:36:59.692    12152[SecuIPC] role 12 replace role 1 encryption info
<0>Nov24 05:37:00.206    12152[PipeIPC] CreateFile for pipe \\.\pipe\PIPE_SRAGENTUI_0 fail error=2
<0>Nov24 05:37:00.350    12152[SecuIPC] failed to send encryption info 14
<1>Nov24 05:37:00.350    12152[Manager] TA1, 1-1013, 0, 2025/11/24 05:37:01
<1>Nov24 05:37:00.350    12152[Manager] TA1, 1-1022, 0, 2025/11/24 05:37:00
<1>Nov24 05:37:00.359    12152[Manager] TA1, 64-113, 0, 2025/11/24 05:37:00
<1>Nov24 05:37:00.360    12152[Manager] TA1, 32-200, 0, 2025/11/24 05:37:10
<1>Nov24 05:37:00.360    12152[Manager] TA1, 256-101, 0, 2025/11/24 05:37:30
<1>Nov24 05:37:00.398    12152[Handler] TSS, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:00.398    12152[Handler] TSS, 1-1022, 0x0368ED80(0x000019C0)
<1>Nov24 05:37:00.399    12152[Handler] TF1, 1-1022, 0x0368ED80(0x000019C0)
<0>Nov24 05:37:00.399    12152[AgentHelper] failed to convert time string, , -1--1--1 -1:-1:-1
<0>Nov24 05:37:00.399    12152[AgentHelper] failed to convert time string with scanf
<1>Nov24 05:37:00.424    12152[Handler] checking inventory, the last inventory scan time does not exist
<1>Nov24 05:37:00.424    12152[Handler] TF2, 1-1022, 0x0368ED80(0x000019C0)
<1>Nov24 05:37:00.942    12152[Handler] TF1, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:00.944    12152[Handler] TF2, 64-113, 0x002B0060(0x00002A10)
<1>Nov24 05:37:01.561    12152[Handler] TSS, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:01.561    12152[Handler] TF1, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:01.611    12152[Handler] using the last reboot time from event log: 2025-11-24 03:38:31 -0800 -> 2025-11-24 14:38:38 -0800
<1>Nov24 05:37:02.626    12152[Handler] using the last reboot time from event log: 2025-11-24 03:38:31 -0800 -> 2025-11-24 14:38:38 -0800
<1>Nov24 05:37:02.679    12152[Handler] TF2, 1-1013, 0x03638F40(0x00003448)
<1>Nov24 05:37:10.410    12152[Handler] TSS, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:11.732    12152[Handler] NBIPC - SetCloudRegion
<1>Nov24 05:37:11.732    12152[Handler] cloud region US
<1>Nov24 05:37:14.961    12152[Handler] TF1, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:16.099    12152[Handler] TF2, 32-200, 0x0365F4F0(0x000011CC)
<1>Nov24 05:37:16.910    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:18.866    12152[Handler] NBIPC - SetCloudRegion
<1>Nov24 05:37:18.866    12152[Handler] cloud region US
<1>Nov24 05:37:18.946    12152[Handler] IPC - GetAlertSetting
<1>Nov24 05:37:19.077    12152[Handler] IPC - GetInventorySetting
<1>Nov24 05:37:19.149    12152[Handler] IPC - GetAvSetting
<1>Nov24 05:37:19.245    12152[Handler] IPC - GetSysUpdateSetting
<1>Nov24 05:37:19.314    12152[Handler] IPC - GetScheRebootSetting
<1>Nov24 05:37:19.408    12152[Handler] IPC - GetScheSysUpdateSetting
<1>Nov24 05:37:19.483    12152[Handler] IPC - GetScheCmdSetting
<1>Nov24 05:37:19.556    12152[Handler] IPC - GetScheExeSetting
<1>Nov24 05:37:19.625    12152[Handler] IPC - GetScheMsiSetting
<1>Nov24 05:37:19.701    12152[Handler] IPC - GetScheFileDispatchSetting
<1>Nov24 05:37:19.794    12152[Handler] IPC - GetScheSmartActionSetting
<1>Nov24 05:37:19.891    12152[Handler] IPC - GetSysInfo
<1>Nov24 05:37:19.891    12152[Handler] capability 0014038F8FD2FF787F7FF87FF7FFFFBF7FFFFFFB7FFFFFFF
<1>Nov24 05:37:19.891    12152[Handler] sys_info, start
<1>Nov24 05:37:20.263    12152[Handler] sys_info - basic : 343831
<1>Nov24 05:37:20.263    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:37:20
<1>Nov24 05:37:20.323    12152[Handler] TSS, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.323    12152[Handler] TF1, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.403    12152[Handler] sys_info - su : 127261
<1>Nov24 05:37:20.485    12152[Handler] update system update info
<1>Nov24 05:37:20.485    12152[Handler] TF2, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:20.486    12152[Handler] sys_info - av : 74884
<1>Nov24 05:37:20.526    12152[Handler] sys_info, len = 435
<1>Nov24 05:37:20.526    12152[Handler] sys_info, write reg
<1>Nov24 05:37:20.526    12152[Handler] sys_info, stop
<1>Nov24 05:37:20.541    12152[Handler] IPC - GetEmmAllPolicies
<1>Nov24 05:37:23.400    12152[Handler] NBIPC - 1083
<1>Nov24 05:37:23.419    12152[Handler] emm patch, start, no policy, reset emm patch
<1>Nov24 05:37:23.563    12152[Handler] NBIPC - SetInventorySetting
<1>Nov24 05:37:23.756    12152[Handler] NBIPC - SetSysUpdateSetting
<1>Nov24 05:37:23.800    12152[Handler] IPC - GetAlertSetting
<1>Nov24 05:37:23.988    12152[Handler] NBIPC - SetScheRebootSetting
<1>Nov24 05:37:24.222    12152[Handler] NBIPC - SetScheSysUpdateSetting
<1>Nov24 05:37:24.436    12152[Handler] NBIPC - SetScheCmdSetting
<1>Nov24 05:37:24.631    12152[Handler] IPC - GetInventorySetting
<1>Nov24 05:37:24.699    12152[Handler] IPC - GetAvSetting
<1>Nov24 05:37:24.796    12152[Handler] IPC - GetSysUpdateSetting
<1>Nov24 05:37:27.726    12152[Handler] IPC - GetScheRebootSetting
<1>Nov24 05:37:27.767    12152[Handler] NBIPC - SetScheExeSetting
<1>Nov24 05:37:27.807    12152[Handler] IPC - GetScheSysUpdateSetting
<1>Nov24 05:37:27.920    12152[Handler] NBIPC - SetScheMsiSetting
<1>Nov24 05:37:27.921    12152[Handler] IPC - GetScheCmdSetting
<1>Nov24 05:37:28.030    12152[Handler] IPC - GetScheExeSetting
<1>Nov24 05:37:28.035    12152[Handler] NBIPC - SetScheFileDispatchSetting
<1>Nov24 05:37:28.197    12152[Handler] IPC - GetScheMsiSetting
<1>Nov24 05:37:28.265    12152[Handler] NBIPC - SetScheSmartActionSetting
<1>Nov24 05:37:28.349    12152[Handler] IPC - GetScheFileDispatchSetting
<1>Nov24 05:37:28.409    12152[Handler] IPC - GetScheSmartActionSetting
<1>Nov24 05:37:28.512    12152[Handler] IPC - GetSysInfo
<1>Nov24 05:37:28.512    12152[Handler] capability 0014038F8FD2FF787F7FF87FF7FFFFBF7FFFFFFB7FFFFFFF
<1>Nov24 05:37:28.512    12152[Handler] sys_info, start
<1>Nov24 05:37:28.677    12152[Handler] sys_info - basic : 149744
<1>Nov24 05:37:28.677    12152[Manager] TA1, 1-1020, 0, 2025/11/24 05:37:28
<1>Nov24 05:37:28.677    12152[Handler] TSS, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.677    12152[Handler] TF1, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.739    12152[Handler] sys_info - su : 56780
<1>Nov24 05:37:28.788    12152[Handler] update system update info
<1>Nov24 05:37:28.789    12152[Handler] TF2, 1-1020, 0x00299C50(0x00002D28)
<1>Nov24 05:37:28.789    12152[Handler] sys_info - av : 45383
<1>Nov24 05:37:28.834    12152[Handler] sys_info, len = 435
<1>Nov24 05:37:28.834    12152[Handler] sys_info, write reg
<1>Nov24 05:37:28.834    12152[Handler] sys_info, stop
<1>Nov24 05:37:28.847    12152[Handler] IPC - GetEmmAllPolicies
<1>Nov24 05:37:30.378    12152[Handler] TSS, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:30.379    12152[SRAgent::CDevicePostureTask::Perform] device posture task: osquery status check
<1>Nov24 05:37:31.947    12152[Handler] TF1, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:31.948    12152[Handler] update system status to report osquery status
<1>Nov24 05:37:31.948    12152[Manager] TA1, 1-1026, 0, 2025/11/24 05:37:31
<1>Nov24 05:37:31.948    12152[Handler] TF2, 256-101, 0x002969B0(0x0000277C)
<1>Nov24 05:37:31.950    12152[Handler] TSS, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:31.950    12152[Handler] TF1, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:31.950    12152[Handler] TF2, 1-1026, 0x0029A078(0x00003448)
<1>Nov24 05:37:34.704    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.761    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.840    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.950    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:34.979    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.036    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.061    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.095    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.144    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.173    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.202    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.233    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.265    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.344    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.409    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:35.489    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:37:37.217    12152[Handler] NBIPC - SetServerId
<1>Nov24 05:36:52.262 SM_11664[CUtility::IsV2CredentialProvider] SRCred ver:1.0.0.11
<1>Nov24 05:36:52.262 SM_11664[Manager] ==== SRManager start 11664 (0) ====  0
<1>Nov24 05:36:53.114 SM_11664[CtrlMgr] [P2P] prepare quic cert...
<1>Nov24 05:36:54.523 SM_11664[CtrlMgr] read SRS id from reg:0
<1>Nov24 05:36:54.541 SM_11664[CtrlMgr] Open SRS param: -h pid:10728 ret:1 (298)
<1>Nov24 05:36:54.815 SM_11664[CtrlMgr] Open SRA sid:2 pid:12152 ret:1 (18)
<1>Nov24 05:36:54.847 SM_11664[CtrlMgr] Close all SRVRDIS count succ:0, total:0
<1>Nov24 05:36:54.854 SM_11664[CtrlMgr] Close all SRAppPB count succ:0, total:0
<1>Nov24 05:36:55.030 SM_11664[CtrlMgr] Open SRAppPB sid:2 pid:9860 suc:1 err:0
<1>Nov24 05:36:55.377 SS_10728[ServGUI] ==== SRServer starting 10728 (0) ====
<1>Nov24 05:36:55.471 SM_11664[CtrlMgr] server version  : 3.8.0.1
<1>Nov24 05:36:55.472 SM_11664[CtrlMgr] OS 10.0(17763)  suite:00000100 type:00000001 x64:1
<1>Nov24 05:36:55.647 SM_11664[CtrlMgr] UserID is 
<0>Nov24 05:36:55.850 PB_09860[Banner] Get default path error:5
<1>Nov24 05:36:56.361 SM_11664[CtrlMgr] Open SRF sid:2 pid:8132 ret:1 (0)
<1>Nov24 05:36:56.361 SM_11664[CtrlMgr] SRM id:11664 SRF id:8132
<1>Nov24 05:36:57.259 SS_10728[SecuIPC] role 3 set role 1 encryption info
<1>Nov24 05:36:57.263 SM_11664[SecuIPC] role 1 set role 3 encryption info
<0>Nov24 05:36:57.278 SS_10728[ServGUI] Create Tray icon fail:cannot find taskbar
<1>Nov24 05:36:57.428 SF_08132[Feature] ==== SRFeature start 8132 (2) ====
<1>Nov24 05:36:57.533 SM_11664[SecuIPC] role 1 replace role 3 encryption info
<1>Nov24 05:36:57.533 SS_10728[SecuIPC] role 3 replace role 1 encryption info
<1>Nov24 05:36:57.557 SM_11664[SecuIPC] role 1 set role 12 encryption info
<1>Nov24 05:36:58.592 SM_11664[SecuIPC] role 1 set role 7 encryption info
<1>Nov24 05:36:58.831 SS_10728[ServGUI]  -- SRServer starting finished -- 
<1>Nov24 05:36:59.027 SS_10728[ServGUI] Query status...Loading(0)(0)
<1>Nov24 05:36:59.027 SM_11664[RMMmode] code [hZCDFPhK75mJ]
<1>Nov24 05:36:59.296 SS_10728[PUpdate] S-0 Rtn-0:0 Ops(0x40) Svr(0x00:1) BE(0x00) Relay(0x00) Proxy(0x00) Share(0x00)
<1>Nov24 05:36:59.720 SM_11664[Backend] server id:5e93022fa790faa8e81924a99124fe22
<1>Nov24 05:36:59.722 SM_11664[Network] set port to 6783, internal to 9527
<1>Nov24 05:36:59.725 SM_11664[CtrlMgr] FIPS:(X)
<1>Nov24 05:36:59.725 SM_11664[CtrlMgr] TLS:11(O) 12(O) 13(X)
<1>Nov24 05:36:59.725 SM_11664[CtrlMgr] WSS:(X) IPv6:(X)
<1>Nov24 05:36:59.735 SM_11664[Network] [SRF-S] FIPS-0, TLS11-1, TLS12-1, TLS13-0, IPv6-0
<1>Nov24 05:36:59.735 SM_11664[Network] [SRF-S][Server-0145EA60] create, v2.2.1.2, 11
<1>Nov24 05:36:59.785 SM_11664[CtrlMgr] socket datapool(T) is running...
<1>Nov24 05:36:59.798 SM_11664[Network] [Util-S] FIPS-0, TLS11-1, TLS12-1, TLS13-0, IPv6-0
<1>Nov24 05:36:59.798 SM_11664[Network] [Util-S][Server-027D8450] create, v2.2.1.2, 11
<1>Nov24 05:36:59.798 SM_11664[Network] wait Utility accept..
<1>Nov24 05:37:00.178 SM_11664[CtrlMgr] socket utility(T) is running on port:8763...
<1>Nov24 05:37:02.405 SS_10728[ServGUI] Abort to create tray icon due to the hide tray icon flag on.
<1>Nov24 05:37:05.923 SM_11664[Network] [LAN-S] FIPS-0, TLS11-1, TLS12-1, TLS13-0, IPv6-0
<1>Nov24 05:37:05.924 SM_11664[Network] [LAN-S][Server-027D1928] create, v2.2.1.2, 11
<1>Nov24 05:37:06.961 SM_11664[CtrlMgr] socket monitor(T) is running
<1>Nov24 05:37:07.029 SM_11664[Console] check UI IPC succ
<1>Nov24 05:37:07.036 SS_10728[ServGUI] Do nothing, just check IPC
<0>Nov24 05:37:07.149 SM_11664[Backend] Tcode read registry fail 18
<1>Nov24 05:37:07.155 SM_11664[Backend] Get streamer name:MSEDGEWIN10
<1>Nov24 05:37:07.170 SM_11664[Backend] version: 0x00030000 => v3
<1>Nov24 05:37:07.171 SM_11664[Backend] PROXY none status:-1 avail=0 auth=0 name=:0 site=st-lookup-v1-univ-srs-win-3801.api.splashtop.com:443,st-relay-v3-univ-srs-win-3801.api.splashtop.com
<1>Nov24 05:37:07.172 SM_11664[GLookup] infra gen 03020000 reprobe by win10 later
<1>Nov24 05:37:07.174 SM_11664[GLookup] infra gen 03020000 enforced 0 current 0
<1>Nov24 05:37:07.183 SM_11664[Backend] Get streamer name:MSEDGEWIN10
<1>Nov24 05:37:07.192 SM_11664[Backend] PROXY none status:-1 avail=0 auth=0 name=:0 site=st-lookup-v1-univ-srs-win-3801-g3.api.splashtop.com:443,st-relay-v3-univ-srs-win-3801.api.splashtop.com
<1>Nov24 05:37:07.192 SM_11664[Backend] PROXY none status:-1 avail=0 auth=0 name=:0 site=st-lookup-v1-univ-srs-win-3801-g3.api.splashtop.com:443,st-relay-v3-univ-srs-win-3801.api.splashtop.com
<1>Nov24 05:37:07.225 SS_10728[PUpdate] S-0 Rtn-0:0 Ops(0x00) Svr(0x81:1) BE(0x00) Relay(0x00) Proxy(0x00) Share(0x00)
<1>Nov24 05:37:09.172 SM_11664[Backend] CMD:1003 200(0):
<1>Nov24 05:37:09.172 SM_11664[Backend] CMD:1003 result:20200
<1>Nov24 05:37:11.546 SM_11664[Backend] CMD:1001 200(0):
<1>Nov24 05:37:11.546 SM_11664[Backend] CMD:1001 result:20200
<1>Nov24 05:37:11.670 SM_11664[GLookup] infra gen 03020003 enforced 0 current 3
<1>Nov24 05:37:11.712 SM_11664[Backend] Get streamer name:MSEDGEWIN10
<1>Nov24 05:37:11.747 SM_11664[Backend] PROXY none status:-1 avail=0 auth=0 name=:0 site=st-lookup-v1-univ-srs-win-3801-g3.api.splashtop.com:443,st-relay-v3-univ-srs-win-3801-g3.api.splashtop.com
<1>Nov24 05:37:11.747 SM_11664[Backend] channel is not running
<1>Nov24 05:37:13.529 SM_11664[Backend] CMD:02 200(0):
<1>Nov24 05:37:13.531 SM_11664[Backend] CMD:02 result:20200
<0>Nov24 05:37:13.639 SM_11664[SDEndec] failed to open file to read, 2
<1>Nov24 05:37:13.639 SM_11664[SDEndec] gen new key
<1>Nov24 05:37:14.448 SM_11664[Backend] srsinit bChange:1 nShare:-1 support:0 RMM:1
<1>Nov24 05:37:16.893 SM_11664[Backend] CMD:16 200(0)T2:
<1>Nov24 05:37:16.893 SM_11664[Backend] CMD:16 result:20200
<1>Nov24 05:37:16.897 SM_11664[Backend] RMM mode initialed.
<1>Nov24 05:37:18.724 SM_11664[Backend] CMD:606 200(0)T2:
<1>Nov24 05:37:18.726 SM_11664[Backend] CMD:606 result:40422
<1>Nov24 05:37:18.855 SM_11664[Console] update policy from login
<1>Nov24 05:37:18.855 SM_11664[Polices] ReadCurrentPolicy
<1>Nov24 05:37:18.945 SM_11664[Polices] GetAlertSetting
<1>Nov24 05:37:19.077 SM_11664[Polices] GetInventorySetting
<1>Nov24 05:37:19.149 SM_11664[Polices] GetAntivirusSetting
<1>Nov24 05:37:19.245 SM_11664[Polices] GetSystemUpdateSetting
<1>Nov24 05:37:19.313 SM_11664[Polices] GetScheduledRebootSetting
<1>Nov24 05:37:19.408 SM_11664[Polices] GetScheduledUpdateSetting
<1>Nov24 05:37:19.483 SM_11664[Polices] GetScheduledCmdSetting
<1>Nov24 05:37:19.556 SM_11664[Polices] GetScheduledExeSetting
<1>Nov24 05:37:19.624 SM_11664[Polices] GetScheduledMsiSetting
<1>Nov24 05:37:19.701 SM_11664[Polices] GetScheduledFileDisaptchSetting
<1>Nov24 05:37:19.789 SM_11664[Polices] GetScheduledSmartActinoSetting
<1>Nov24 05:37:19.881 SM_11664[Polices] ReadSystemInfo
<1>Nov24 05:37:20.536 SM_11664[Polices] ReadPreferencePolicy
<1>Nov24 05:37:20.538 SM_11664[Polices] ReadEmmPolicy
<1>Nov24 05:37:20.618 SM_11664[Polices] ReadDevicePostureCheck
<1>Nov24 05:37:21.078 SM_11664[Backend] CMD:08 200(0)T2:
<1>Nov24 05:37:21.080 SM_11664[Backend] CMD:08 result:20200 command
<1>Nov24 05:37:21.261 SM_11664[IdleChk] User Idle check method not idle2
<1>Nov24 05:37:21.354 SM_11664[RelayCh] setup start (OTM:0 LOCAL:0)
<1>Nov24 05:37:21.355 SM_11664[RelayCh] [command] FIPS-0, TLS11-1, TLS12-1, TLS13-0, IPv6-0
<1>Nov24 05:37:21.357 SS_10728[PUpdate] S-2 Rtn-200:0 Ops(0x00) Svr(0x00:1) BE(0x81) Relay(0x00) Proxy(0x00) Share(0x00)
<1>Nov24 05:37:22.466 SM_11664[RelayCh] [command][SC-0294D787][Client-0275E7B8] create, v2.2.1.2, 16
<1>Nov24 05:37:22.467 SM_11664[RelayCh] [command][SC-0294D787][Client-0275E7B8] timeout 15000/60000, buffer 65535, 99
<1>Nov24 05:37:22.655 SM_11664[RelayCh] [command][SC-0294D787][SSL] FIPS disabled, 251
<1>Nov24 05:37:22.657 SM_11664[RelayCh] [command][SC-0294D787][SSL] TLS 1.1 Y, 1.2 Y, 1.3 N, 269
<1>Nov24 05:37:22.661 SM_11664[RelayCh] [command][SC-0294D787][SSL] set ext host name 13-247-194-26.relay.splashtop.com, 307
<1>Nov24 05:37:22.858 SM_11664[RelayCh] [command][SC-0294D787][SSL] ssl version 0x0303, cipher ECDHE-RSA-AES256-GCM-SHA384, 350
<1>Nov24 05:37:22.858 SM_11664[RelayCh] [command][SC-0294D787] ssl connected, 960
<1>Nov24 05:37:22.859 SM_11664[RelayCh] [command][SC-0294D787] relay request "13-247-194-26.relay.splashtop.com?key=t2Fj-94ghqdoxVO--W022GG4Kb00ttmXe05Hi00t2Fj-94ghqdoxVOcp4dUXrQvpE8XoRcTGm6rs-Z HTTP/1.0\nSST: Ready\nNTY: Ready\nSTD: Ready\nRCT: command\nLST: zonal\nSON: yes\nBKD: US\nQUIC:Ready\n\n", 211
<1>Nov24 05:37:22.965 SM_11664[RelayCh] [command][SC-0294D787] relay reponse "HTTP/1.1 200 ok\nRCT: Ready\nNTY: Ready\nSTD: Ready\nSON: Ready\nQUIC: Ready\nContent-Type: application/json\nContent-Length: 378\n\n", 252
<1>Nov24 05:37:22.970 SM_11664[RelayCh] zone echo 3 times after 283sec
<1>Nov24 05:37:22.970 SM_11664[Backend] [P2P] recv quic server info from 'command' connection, 129-151-171-243.relay.splashtop.com 3479
<1>Nov24 05:37:22.971 SM_11664[RelayCh] [command][SC-0294D787] receiving relay data, 323
<1>Nov24 05:37:22.990 SM_11664[RelayCh] [command][SC-0294D787] start heartbeat thread, interval 50000, 1562
<1>Nov24 05:37:23.132 SM_11664[Backend] CMD:29 200(0)T2:
<1>Nov24 05:37:23.132 SM_11664[Backend] CMD:29 policy res:20200 parse:1
<1>Nov24 05:37:23.133 SM_11664[Backend] command policy interval 39048sec
<1>Nov24 05:37:23.671 SM_11664[Polices] ReadCurrentPolicy
<1>Nov24 05:37:23.800 SM_11664[Polices] GetAlertSetting
<1>Nov24 05:37:24.631 SM_11664[Polices] GetInventorySetting
<1>Nov24 05:37:24.699 SM_11664[Polices] GetAntivirusSetting
<1>Nov24 05:37:24.794 SM_11664[Polices] GetSystemUpdateSetting
<1>Nov24 05:37:27.725 SM_11664[Polices] GetScheduledRebootSetting
<1>Nov24 05:37:27.806 SM_11664[Polices] GetScheduledUpdateSetting
<1>Nov24 05:37:27.910 SM_11664[Polices] GetScheduledCmdSetting
<1>Nov24 05:37:28.013 SS_10728[PUpdate] S-2 Rtn-200:0 Ops(0x00) Svr(0x00:1) BE(0x00) Relay(0x81) Proxy(0x00) Share(0x00)
<1>Nov24 05:37:28.030 SM_11664[Polices] GetScheduledExeSetting
<1>Nov24 05:37:28.193 SM_11664[Polices] GetScheduledMsiSetting
<1>Nov24 05:37:28.342 SM_11664[Polices] GetScheduledFileDisaptchSetting
<1>Nov24 05:37:28.409 SM_11664[Polices] GetScheduledSmartActinoSetting
<1>Nov24 05:37:28.496 SM_11664[Polices] ReadSystemInfo
<1>Nov24 05:37:28.842 SM_11664[Polices] ReadPreferencePolicy
<1>Nov24 05:37:28.844 SM_11664[Polices] ReadEmmPolicy
<1>Nov24 05:37:28.914 SM_11664[Polices] ReadDevicePostureCheck
<1>Nov24 05:37:31.127 SM_11664[Backend] CMD:29 200(0)T2:
<1>Nov24 05:37:31.128 SM_11664[Backend] CMD:29 policy res:20200 parse:0
<1>Nov24 05:37:31.425 SS_10728[PPolicy] update policy ...
<1>Nov24 05:37:31.673 SM_11664[Backend] update policy end
<1>Nov24 05:37:33.465 SM_11664[Backend] CMD:03 200(0)T2:
<1>Nov24 05:37:33.468 SM_11664[Backend] CMD:03 hbtype:0 res:20200
<1>Nov24 05:37:33.468 SM_11664[RelayCh] [command][SC-0294D787] set heartbeat interval to 50000, 1124
<1>Nov24 05:37:34.075 SM_11664[RMMmode] clear spwd
<1>Nov24 05:37:34.075 SM_11664[Console] online helper remove by online
<1>Nov24 05:37:34.350 SM_11664[CtrlMgr] This SRS can handle 240:0
<1>Nov24 05:37:34.652 SM_11664[Console] update system status from SRA
<1>Nov24 05:37:34.706 SM_11664[RMMmode] Ignore the same code [hZCDFPhK75mJ]
<1>Nov24 05:37:34.710 SM_11664[RMMmode] assign spwd ttl 86400sec
<1>Nov24 05:37:34.720 SM_11664[RMMmode] assign spwd 9dcd97894ceede12bb134b9f4f1f1438ac87a1ee1a33af91b4e7f0cd167e6209
<1>Nov24 05:37:34.731 SM_11664[RMMmode] assign TTL (86400000)ms
<1>Nov24 05:37:34.734 SM_11664[Backend] update system status begin
<1>Nov24 05:37:35.076 SM_11664[Backend] srsinit bChange:1 nShare:-1 support:0 RMM:1
<1>Nov24 05:37:37.161 SM_11664[Backend] CMD:16 200(0)T2:
<1>Nov24 05:37:37.161 SM_11664[Backend] CMD:16 result:20200
<1>Nov24 05:37:37.172 SM_11664[Backend] RMM mode initialed.
<1>Nov24 05:37:44.209 SM_11664[CtrlMgr] Open SRVRDIS sid:2 pid:10916 ret:1 (0)
<1>Nov24 05:36:50.285  Service[Service] StartService Begin
<1>Nov24 05:36:50.297  Service[Service] ServiceMain Begin
<1>Nov24 05:36:50.301  Service[Service] Run Begin
<4>Nov 69245F72362 [ Service]:[SIT] SRManager() BEGIN
<1>Nov24 05:36:50.414  Service[Service] SRM=> create succ pid:11664 err:0
<4>Nov 69245F72414 [ Service]:[SIT] SRManager END
<6>Nov24 05:36:52.221 SM_11664[Manager] ==== SSUSvc is not exist ====
<6>Nov24 05:36:52.221 SM_11664[Manager] ==== STSLRSvc is not exist ====
<6>Nov24 05:36:52.221 SM_11664[Manager] ==== STWSSSvc is not exist ====
<6>Nov24 05:36:52.262 SM_11664[Manager] ==== SRManager start 11664 (0) ====  0
<6>Nov24 05:36:53.113 SM_11664[Manager] Reg SessionNotify succ (0)
<6>Nov24 05:36:55.472 SM_11664[CtrlMgr] server version  : 3.8.0.1
<6>Nov24 05:36:55.472 SM_11664[CtrlMgr] OS 10.0(17763)  suite:00000100 type:00000001 x64:1
<6>Nov24 05:36:57.428 SF_08132[Feature] ==== SRFeature start 8132 (2) ====
<6>Nov24 05:36:57.500 SM_11664[Console] CLOUD IS (0)
<6>Nov24 05:36:58.108 SF_08132[Feature] Reg WTS 1 (0)
<1>Nov24 05:37:44.748    10916[WmiInfo::IsVirtualMachine] Virtual Machine: V
<1>Nov24 05:37:44.762    10916[LciDriv] IsVirtualMachine
<1>Nov24 05:37:44.991    10916[App] Got SRM_NOTIFY_SRVRDIS_RESPONSE_TEAMID
<1>Nov24 05:37:44.991    10916[App] load vrdis setting {}
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cd ../../../..
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)]
└─$ cd ..         
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -la
total 213720
drwxrwxr-x 7 fixit42 fixit42      4096 Nov 25 12:29  .
drwxr-xr-x 5 fixit42 fixit42      4096 Dec  5 23:42  ..
-rw-rw-r-- 1 fixit42 fixit42      8192 Nov 24 14:44 '$Boot'
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 '$Extend'
-rw-rw-r-- 1 fixit42 fixit42  57360384 Nov 24 14:42 '$LogFile'
-rw-rw-r-- 1 fixit42 fixit42 158859264 Mar 19  2019 '$MFT'
-rw-rw-r-- 1 fixit42 fixit42   2582676 Mar 19  2019 '$Secure_$SDS'
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28  ProgramData
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 'Program Files (x86)'
drwxrwxr-x 7 fixit42 fixit42      4096 Nov 25 12:29  Users
drwxrwxr-x 8 fixit42 fixit42      4096 Nov 25 12:29  Windows
                                                                                                                             
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings '$MFT' | grep -i 'zip\|7z\|winzip\|winrar\|compressed'
7ZcG
7ZcG
7ZcG
microsoft.com/appx/2010/blockmap" HashMethod="http://www.w3.org/2001/04/xmlenc#sha256"><File Name="AppxMetadata\AppxBundleManifest.xml" Size="16568" LfhSize="65"><Block Hash="XmfqJH2mrAaiNlmF1B8VYP+Q02/ynags6U7ZobJXMVQ=" Size="2071"/></File></BlockMap>
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
<BlockMap xmlns="http://schemas.microsoft.com/appx/2010/blockmap" HashMethod="http://www.w3.org/2001/04/xmlenc#sha256"><File Name="AppxManifest.xml" Size="2549" LfhSize="46"><Block Hash="m+dnr1Kfm7z2YL7PXT6oysgh+bNVMxAnAXSEFvYOmQI=" Size="963"/></File></BlockMap>
7zC]
20181002202107Z0s0q0I0
20181002202107Z
20190331202107Z0
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
K7Zh
Q7Zy
R7Zm
R7Zl
H7z7
I       i:7zyJ
    <path d="M19,34V14h2V34Zm8-20h2V34H27Z" style="f
    <path d="M14.19,1.24,20,7.48,10,19.76,0,7.48,5.79,1.24ZM6,8.21H2.38l6.47,8ZM6.4,2.64,2.53,6.82H6.42L7.66,2.64Zm6.08,5.57h-5l2.49,7ZM10.57,2.64H9.11L7.87,6.82h3.94ZM14,8.21l-2.84,8,6.49-8Zm-.38-5.57H12l1.25,4.18h4.2Z" style="fill: #323130"/>
  <assemblyIdentity version="1.0.0.0" name="7z" processorArchitecture="*" type="win32" />
  <assemblyIdentity version="1.0.0.0" name="7z" processorArchitecture="*" type="win32" />
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
7z/E
  <path d="M20.33,13.67l-5.46,5.46-3.21-3.21.79-.79,2.42,2.42,4.67-4.67Z" style="fill: #666"/>
  <path d="M20.33,13.67l-5.46,5.46-3.21-3.21.79-.79,2.42,2.42,4.67-4.67Z" style="fill: #666"/>
t/BzIPKJG1.js 
20181002202107Z0s0q0I0
20181002202107Z
20190331202107Z0
    <path d="M19,34V14h2V34Zm8-20h2V34H27Z" style="f
    <path d="M14.19,1.24,20,7.48,10,19.76,0,7.48,5.79,1.24ZM6,8.21H2.38l6.47,8ZM6.4,2.64,2.53,6.82H6.42L7.66,2.64Zm6.08,5.57h-5l2.49,7ZM10.57,2.64H9.11L7.87,6.82h3.94ZM14,8.21l-2.84,8,6.49-8Zm-.38-5.57H12l1.25,4.18h4.2Z" style="fill: #323130"/>
#7zq
#7zq
#7zq
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
}U7zE
E
}U7zE
:Util::Execution.execute("gzip -dc #{Shellwords.shellescape(sourcefile)} | tar xof -")
    Puppet::Util::Execution.execute("tar cf - #{sourcedir} | gzip -c > #{File.basename(destfile)}")
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
7ZcG
7ZcG
<path d="M132.677 449.677L326.03 256.323L132.677 62.97L159.323 36.3233L379.323 256.323L159.323 476.323L132.677 449.677Z"/>
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
  <path d="M8 1a7 7 0 1 0 7 7 7 7 0 0 0-7-7zm1 10a1 1 0 0 1-2 0v-3a1 1 0 0 1 2 0zm-.293-5.293a1 1 0 1 1 .293-.707 1 1 0 0 1-.293.707z" fill="#767676"/>
t/BzIPKJG1.js 
Version":0,"HashOfHashes":"bLR+YkW147Gf10YSrQ6lgW3AC9E1aDesK3TaSr0DHJA=","ContentLength":244530,"PieceSize":1048576,"Pieces":["J/rmYNjGCeAgcDu0Y7ZgHmKBHcddsZl1vLfWjZWbUn0="]}
Version":0,"HashOfHashes":"aGZA/I8Lc2F+ZsPzrXhTrcZaVte+PexJ5cOai52WjpQ=","ContentLength":4642818,"PieceSize":1048576,"Pieces":["WXdd9JFACfSvd8pL4CzlApi6zSFcMZvaEco9C+Zcjgc=","7ZyMYuVE3K+gFOLr9YJstAno6vzOeLxh5fLQ8mHKt4g=","kEyeX2FsHicx3AN64BNqAbaPMG4N/4HoME4mYX4ahCk=","r1xSeMQBrq4Lp/VMMEtdGRCLr9DzJrjW+T/yj/IBMt4=","8rPNGdVaZxgYMQ9SkBnjIWZ9TbIHb9zfGnM7Ub8xtb0="]}
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
="0 0 16 16"><title>mdl-check-checked</title><path d="M16,0V16H0V0ZM15,1H1V15H15ZM6,12.71,2.65,9.35l.7-.7L6,11.29l6.65-6.64.7.7Z"/></svg>
.05 13.59"><title>Untitled-1</title><path d="M21.53,6.53,9,19.07,2.47,12.53l1.06-1.06L9,16.93,20.47,5.47Z" transform="translate(-2.47 -5.47)" style="fill:#4eae95"/></svg>
    <path d="M19,34V14h2V34Zm8-20h2V34H27Z" style="f
    <path d="M14.19,1.24,20,7.48,10,19.76,0,7.48,5.79,1.24ZM6,8.21H2.38l6.47,8ZM6.4,2.64,2.53,6.82H6.42L7.66,2.64Zm6.08,5.57h-5l2.49,7ZM10.57,2.64H9.11L7.87,6.82h3.94ZM14,8.21l-2.84,8,6.49-8Zm-.38-5.57H12l1.25,4.18h4.2Z" style="fill: #f3f2f1"/>
="0 0 16 16"><title>mdl-check-checked</title><path d="M16,0V16H0V0ZM15,1H1V15H15ZM6,12.71,2.65,9.35l.7-.7L6,11.29l6.65-6.64.7.7Z"/></svg>
.05 13.59"><title>light mode checkbox</title><path d="M21.53,6.53,9,19.07,2.47,12.53l1.06-1.06L9,16.93,20.47,5.47Z" transform="translate(-2.47 -5.47)" style="fill:#2c6b5b"/></svg>
    <path d="M19,34V14h2V34Zm8-20h2V34H27Z" style="f
    <path d="M14.19,1.24,20,7.48,10,19.76,0,7.48,5.79,1.24ZM6,8.21H2.38l6.47,8ZM6.4,2.64,2.53,6.82H6.42L7.66,2.64Zm6.08,5.57h-5l2.49,7ZM10.57,2.64H9.11L7.87,6.82h3.94ZM14,8.21l-2.84,8,6.49-8Zm-.38-5.57H12l1.25,4.18h4.2Z" style="fill: #323130"/>
37z>:]
37z>:]
]
20251123175007Z0s0q0I0
20251123175007Z
20251130175007Z0
    <path d="M19,34V14h2V34Zm8-20h2V34H27Z" style="f
    <path d="M14.19,1.24,20,7.48,10,19.76,0,7.48,5.79,1.24ZM6,8.21H2.38l6.47,8ZM6.4,2.64,2.53,6.82H6.42L7.66,2.64Zm6.08,5.57h-5l2.49,7ZM10.57,2.64H9.11L7.87,6.82h3.94ZM14,8.21l-2.84,8,6.49-8Zm-.38-5.57H12l1.25,4.18h4.2Z" style="fill: #323130"/>
1","UtcTime":"2025-11-24T13:22:15.6953697Z"}
  <path d="M20.33,13.67l-5.46,5.46-3.21-3.21.79-.79,2.42,2.42,4.67-4.67Z" style="fill: #666"/>
7-zip.chm 7-Zip Help
7-Zip.dll 7-Zip Plugin
7-Zip32.dll 7-Zip Plugin 32-bit
7z.dll 7-Zip Engine
7z.exe 7-Zip Console 
7z.sfx 7-Zip GUI SFX
7zCon.sfx 7-Zip Console SFX
7zFM.exe 7-Zip File Manager
7zg.exe 7-Z
descript.ion 7-Zip File Descriptions
history.txt 7-Zip History
Lang 7-Zip Translations
license.txt 7-Zip License
readme.txt 7-Zip Overview
bdf","txtMSource":"","txtMDest":"","cbMKey":"","cbMValue":"","cbTKey":"","cbTValue":"","txtSftpServer":"","seSftpPortNumber":"22","txtSftpUsername":"","txtSftpPassword":"","txtSftpDirectory":"","txtSftpComment":"","txtZipPassword":"","txtSasUri":"","txtSasComment":"","txtS3Region":"","txtS3Bucket":"","txtS3AccessKey":"","txtS3SecretKey":"","txtS3Comment":"","txtS3SessionToken":"","txtS3KeyPrefix":"","ckFlushWarning":"False","Skin":"Office 2016 Colorful"}
BinaryUrl: https://exiftool.org/exiftool-12.29.zip
BinaryUrl: https://github.com/wagga40/Zircolite/releases/download/2.9.7/zircolite_win10_x64_2.9.7.7z
BinaryUrl: https://www.nirsoft.net/utils/usbdeview-x64.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/EvtxExplorer.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/LECmd.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/MFTECmd.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/MFTECmd.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/PECmd.zip
BinaryUrl: https://download.sysinternals.com/files/Handle.zip
BinaryUrl: https://download.sysinternals.com/files/PSTools.zip
BinaryUrl: https://download.sysinternals.com/files/PSTools.zip
BinaryUrl: https://download.sysinternals.com/files/PSTools.zip
BinaryUrl: https://download.sysinternals.com/files/Sigcheck.zip
BinaryUrl: https://download.sysinternals.com/files/TCPView.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/RBCmd.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/WxTCmd.zip
BinaryUrl: https://s3.amazonaws.com/cyb-us-prd-kape/kape.zip
BinaryUrl: https://f001.backblazeb2.com/file/EricZimmermanTools/SQLECmd.zip

```

```
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings '$MFT' | grep -B2 -A2 '7z' | head -30
FILE0
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<BlockMap xmlns="http://schemas.microsoft.com/appx/2010/blockmap" HashMethod="http://www.w3.org/2001/04/xmlenc#sha256"><File Name="AppxManifest.xml" Size="2549" LfhSize="46"><Block Hash="m+dnr1Kfm7z2YL7PXT6oysgh+bNVMxAnAXSEFvYOmQI=" Size="963"/></File></BlockMap>
FILE0
5 W'
--
FILE0
FILE0
7zC]
FILE0
FILE0
--
6j^:T5@F
t*dB
H7z7
FILE0
PA30
--
6^w/ 
`30_
I       i:7zyJ
"u+RfV
SiT'_
--
<assembly xmlns="urn:schemas-microsoft-com:as
v1" manifestVersion="1.0">
  <assemblyIdentity version="1.0.0.0" name="7z" processorArchitecture="*" type="win32" />
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
--

```