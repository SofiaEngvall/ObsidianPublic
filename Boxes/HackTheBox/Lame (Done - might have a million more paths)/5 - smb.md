
```sh
┌──(kali㉿proxli)-[~/boxes/htb/lame]
└─$ smbclient //10.10.10.3/tmp                                     
Password for [WORKGROUP\kali]:
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Fri May  9 21:38:48 2025
  ..                                 DR        0  Sat Oct 31 07:33:58 2020
  .ICE-unix                          DH        0  Fri May  9 20:55:26 2025
  vmware-root                        DR        0  Fri May  9 20:56:04 2025
  .X11-unix                          DH        0  Fri May  9 20:55:52 2025
  .X0-lock                           HR       11  Fri May  9 20:55:52 2025
  5541.jsvc_up                        R        0  Fri May  9 20:56:28 2025
  vgauthsvclog.txt.0                  R     1600  Fri May  9 20:55:25 2025

                7282168 blocks of size 1024. 5386532 blocks available


smb: \> recurse on
smb: \> mget *

Get directory .ICE-unix? y
Get directory vmware-root? y
Get directory .X11-unix? y
Get file .X0-lock? y
getting file \.X0-lock of size 11 as .X0-lock (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
Get file 5541.jsvc_up? y
NT_STATUS_ACCESS_DENIED opening remote file \5541.jsvc_up
Get file vgauthsvclog.txt.0? y
getting file \vgauthsvclog.txt.0 of size 1600 as vgauthsvclog.txt.0 (17.0 KiloBytes/sec) (average 8.6 KiloBytes/sec)
NT_STATUS_ACCESS_DENIED listing \vmware-root\*
Get file X0? y
NT_STATUS_ACCESS_DENIED opening remote file \.X11-unix\X0

smb: \> exit
```

```sh
┌──(kali㉿proxli)-[~/boxes/htb/lame]
└─$ ls -la
total 16
drwxrwxr-x  2 kali kali 4096 May  9 21:51 .
drwxr-xr-x 11 kali kali 4096 May  9 21:35 ..
-rw-r--r--  1 kali kali 1600 May  9 21:41 vgauthsvclog.txt.0
-rw-r--r--  1 kali kali   11 May  9 21:41 .X0-lock
```

```sh
┌──(kali㉿proxli)-[~/boxes/htb/lame]
└─$ cat .X0-lock                                                
      5602

┌──(kali㉿proxli)-[~/boxes/htb/lame]
└─$ cat vgauthsvclog.txt.0 
[May 09 14:55:25.187] [ message] [VGAuthService] VGAuthService 'build-4448496' logging at level 'normal'
[May 09 14:55:25.188] [ message] [VGAuthService] Pref_LogAllEntries: 1 preference groups in file '/etc/vmware-tools/vgauth.conf'
[May 09 14:55:25.188] [ message] [VGAuthService] Group 'service'
[May 09 14:55:25.188] [ message] [VGAuthService]         samlSchemaDir=/usr/lib/vmware-vgauth/schemas
[May 09 14:55:25.188] [ message] [VGAuthService] Pref_LogAllEntries: End of preferences
[May 09 14:55:25.334] [ message] [VGAuthService] VGAuthService 'build-4448496' logging at level 'normal'
[May 09 14:55:25.334] [ message] [VGAuthService] Pref_LogAllEntries: 1 preference groups in file '/etc/vmware-tools/vgauth.conf'
[May 09 14:55:25.334] [ message] [VGAuthService] Group 'service'
[May 09 14:55:25.334] [ message] [VGAuthService]         samlSchemaDir=/usr/lib/vmware-vgauth/schemas
[May 09 14:55:25.334] [ message] [VGAuthService] Pref_LogAllEntries: End of preferences
[May 09 14:55:25.334] [ message] [VGAuthService] Cannot load message catalog for domain 'VGAuthService', language 'C', catalog dir '.'.
[May 09 14:55:25.334] [ message] [VGAuthService] INIT SERVICE
[May 09 14:55:25.334] [ message] [VGAuthService] Using '/var/lib/vmware/VGAuth/aliasStore' for alias store root directory
[May 09 14:55:25.379] [ message] [VGAuthService] SAMLCreateAndPopulateGrammarPool: Using '/usr/lib/vmware-vgauth/schemas' for SAML schemas
[May 09 14:55:25.440] [ message] [VGAuthService] SAML_Init: Allowing 300 of clock skew for SAML date validation
[May 09 14:55:25.440] [ message] [VGAuthService] BEGIN SERVICE
```
