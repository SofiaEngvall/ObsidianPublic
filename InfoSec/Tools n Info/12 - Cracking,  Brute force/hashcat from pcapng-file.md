
webpage: https://hashcat.net/cap2hashcat/
uses: https://github.com/ZerBea/hcxtools

---
## Handshake extraction successful: [Download](https://hashcat.net/cap2hashcat/out/840621_1701563612.hc22000)

---
```
hcxpcapngtool 6.3.1 reading from 840621_1701563612.cap...

summary capture file
--------------------
file name................................: 840621_1701563612.cap
version (pcapng).........................: 1.0
operating system.........................: Linux 6.5.0-kali3-amd64
application..............................: Dumpcap (Wireshark) 4.0.10 (Git v4.0.10 packaged as 4.0.10-1)
interface name...........................: hwsim0
interface vendor.........................: 000000
openSSL version..........................: 1.0
weak candidate...........................: N/A
MAC ACCESS POINT.........................: 000000000000 (incremented on every new client)
MAC CLIENT...............................: 000000000000
REPLAYCOUNT..............................: 0
ANONCE...................................: 0000000000000000000000000000000000000000000000000000000000000000
SNONCE...................................: 0000000000000000000000000000000000000000000000000000000000000000
timestamp minimum (GMT)..................: 25.11.2023 15:50:28
timestamp maximum (GMT)..................: 25.11.2023 15:57:07
used capture interfaces..................: 1
link layer header type...................: DLT_IEEE802_11_RADIO (127)
endianness (capture system)..............: little endian
packets inside...........................: 45243
packets received on 2.4 GHz..............: 45233
packets received on 5 GHz................: 10
ESSID (total unique).....................: 1
BEACON (total)...........................: 3903
BEACON on 2.4 GHz channel (from IE_TAG)..: 6 
PROBEREQUEST (undirected)................: 34
PROBERESPONSE (total)....................: 2
AUTHENTICATION (total)...................: 4
AUTHENTICATION (OPEN SYSTEM).............: 4
ASSOCIATIONREQUEST (total)...............: 2
ASSOCIATIONREQUEST (PSK).................: 2
WPA encrypted............................: 20635
EAPOL messages (total)...................: 8
EAPOL RSN messages.......................: 8
EAPOLTIME gap (measured maximum msec)....: 0
EAPOL ANONCE error corrections (NC)......: not detected
EAPOL M1 messages (total)................: 2
EAPOL M2 messages (total)................: 2
EAPOL M3 messages (total)................: 2
EAPOL M4 messages (total)................: 2
EAPOL M4 messages (zeroed NONCE).........: 2
EAPOL pairs (total)......................: 4
EAPOL pairs (best).......................: 2
EAPOL pairs written to 22000 hash file...: 2 (RC checked)
EAPOL M32E2 (authorized).................: 2

frequency statistics from radiotap header (frequency: received packets)
-----------------------------------------------------------------------
 2412: 2	 2417: 2	 2422: 2	 2427: 2	
 2432: 2	 2437: 45211	 2442: 2	 2447: 2	
 2452: 2	 2457: 2	 2462: 2	 2472: 2	
 5180: 2	 5200: 2	 5240: 2	 5745: 2	
 5785: 2	

Warning: out of sequence timestamps!
This dump file contains frames with out of sequence timestamps.
That is a bug of the capturing/cleaning tool.


session summary
---------------
processed pcapng files................: 1
```

run hashcat in kali:

```sh
┌──(kali㉿kali)-[~]
└─$ hashcat --attack-mode 0 --hash-type 22000 840621_1701563612.hc22000 /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 4.0+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.7, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: cpu-haswell-Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz, 2895/5854 MB (1024 MB allocatable), 2MCU

Minimum password length supported by kernel: 8
Maximum password length supported by kernel: 63

Hashes: 2 digests; 2 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Salt
* Slow-Hash-SIMD-LOOP

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

af804935ab322d4b0bbd84a711c36f01:22c712c7e235:d267d13f36ec:FreeWifiBFC:Christmas
c10a70d965945b57f2988ae0fcfd2b22:22c712c7e235:2a8449acf9d8:FreeWifiBFC:Christmas
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 22000 (WPA-PBKDF2-PMKID+EAPOL)
Hash.Target......: 840621_1701563612.hc22000
Time.Started.....: Sun Dec  3 01:55:26 2023 (3 secs)
Time.Estimated...: Sun Dec  3 01:55:29 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     4733 H/s (9.44ms) @ Accel:128 Loops:1024 Thr:1 Vec:8
Recovered........: 2/2 (100.00%) Digests (total), 2/2 (100.00%) Digests (new)
Progress.........: 34758/14344385 (0.24%)
Rejected.........: 23238/34758 (66.86%)
Restore.Point....: 33956/14344385 (0.24%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1-3
Candidate.Engine.: Device Generator
Candidates.#1....: iloveu69 -> brandon69
Hardware.Mon.#1..: Util: 95%

Started: Sun Dec  3 01:54:30 2023
Stopped: Sun Dec  3 01:55:30 2023

```
