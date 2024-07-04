
```sh
┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ ls -la
total 12
drwxrwxr-x 2 kali kali 4096 Jun 29 17:56 .
drwxrwxr-x 3 kali kali 4096 Jun 29 17:55 ..
-rw-rw-r-- 1 kali kali 1331 Jun 29 17:54 MyFriendJohn.zip

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip MyFriendJohn.zip              
Archive:  MyFriendJohn.zip
 extracting: use-rockyou.zip         

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ ls -la
total 16
drwxrwxr-x 2 kali kali 4096 Jun 29 17:56 .
drwxrwxr-x 3 kali kali 4096 Jun 29 17:55 ..
-rw-rw-r-- 1 kali kali 1331 Jun 29 17:54 MyFriendJohn.zip
-rw-r--r-- 1 kali kali 1151 Jun 15  2021 use-rockyou.zip

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip use-rockyou.zip 
Archive:  use-rockyou.zip
[use-rockyou.zip] custom-list.txt password: 
   skipping: custom-list.txt         incorrect password
   skipping: custom-list.zip         incorrect password

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ zip2john use-rockyou.zip > z2j-file
ver 2.0 efh 5455 efh 7875 use-rockyou.zip/custom-list.txt PKZIP Encr: TS_chk, cmplen=327, decmplen=536, crc=5DFDDFBE ts=8892 cs=8892 type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** use-rockyou.zip/custom-list.zip PKZIP Encr: TS_chk, cmplen=454, decmplen=442, crc=9DFA0523 ts=89D9 cs=89d9 type=0
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ john z2j-file --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
kdbs0429         (use-rockyou.zip)     
1g 0:00:00:00 DONE (2024-06-29 17:58) 1.666g/s 11120Kp/s 11120Kc/s 11120KC/s kdeandray0..kccooper
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip use-rockyou.zip                                 
Archive:  use-rockyou.zip
[use-rockyou.zip] custom-list.txt password: 
  inflating: custom-list.txt         
 extracting: custom-list.zip         

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ ls -la
total 28
drwxrwxr-x 2 kali kali 4096 Jun 29 17:58 .
drwxrwxr-x 3 kali kali 4096 Jun 29 17:55 ..
-rw-rw-r-- 1 kali kali 1331 Jun 29 17:54 MyFriendJohn.zip
-rw-r--r-- 1 kali kali  536 Jun 15  2021 custom-list.txt
-rw-r--r-- 1 kali kali  442 Jun 15  2021 custom-list.zip
-rw-r--r-- 1 kali kali 1151 Jun 15  2021 use-rockyou.zip
-rw-rw-r-- 1 kali kali  881 Jun 29 17:57 z2j-file

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip custom-list.zip 
Archive:  custom-list.zip
[custom-list.zip] brute-force-pin.zip password: 
   skipping: brute-force-pin.zip     incorrect password

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ zip2john custom-list.zip > z2j-file2
ver 1.0 efh 5455 efh 7875 custom-list.zip/brute-force-pin.zip PKZIP Encr: 2b chk, TS_chk, cmplen=238, decmplen=226, crc=445F3191 ts=8914 cs=8914 type=0

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ john z2j-file2 --wordlist=./custom-list.txt               
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
1N73rD3N0M1N4710N41 (custom-list.zip/brute-force-pin.zip)     
1g 0:00:00:00 DONE (2024-06-29 18:00) 100.0g/s 5100p/s 5100c/s 5100C/s P1351054Ur
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip custom-list.zip
Archive:  custom-list.zip
[custom-list.zip] brute-force-pin.zip password: 
 extracting: brute-force-pin.zip     

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ ls -la
total 36
drwxrwxr-x 2 kali kali 4096 Jun 29 18:00 .
drwxrwxr-x 3 kali kali 4096 Jun 29 17:55 ..
-rw-rw-r-- 1 kali kali 1331 Jun 29 17:54 MyFriendJohn.zip
-rw-r--r-- 1 kali kali  226 Jun 15  2021 brute-force-pin.zip
-rw-r--r-- 1 kali kali  536 Jun 15  2021 custom-list.txt
-rw-r--r-- 1 kali kali  442 Jun 15  2021 custom-list.zip
-rw-r--r-- 1 kali kali 1151 Jun 15  2021 use-rockyou.zip
-rw-rw-r-- 1 kali kali  881 Jun 29 17:57 z2j-file
-rw-rw-r-- 1 kali kali  620 Jun 29 17:59 z2j-file2

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ zip2john brute-force-pin.zip > z2j-file3 
ver 1.0 efh 5455 efh 7875 brute-force-pin.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=44, decmplen=32, crc=148DA515 ts=86D2 cs=86d2 type=0

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ john z2j-file3 --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
991337           (brute-force-pin.zip/flag.txt)     
1g 0:00:00:00 DONE (2024-06-29 18:11) 5.555g/s 12060Kp/s 12060Kc/s 12060KC/s ADRIANA16..989212518
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ unzip brute-force-pin.zip                                 
Archive:  brute-force-pin.zip
[brute-force-pin.zip] flag.txt password: 
 extracting: flag.txt                

┌──(kali㉿kali)-[~/ctflearn/myfriendjohn]
└─$ cat flag.txt            
CTFlearn{s0_n0W_y0uv3_M3t_J0hN}
```