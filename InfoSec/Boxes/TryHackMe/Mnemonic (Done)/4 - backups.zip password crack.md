
```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ unzip backups.zip  
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password: 
password incorrect--reenter:
```

Googled "zip password crack kali"
https://medium.com/@rajendraprasanth/password-cracking-using-kali-67e0b89578df

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ zip2john backups.zip > ziphash.txt
ver 1.0 backups.zip/backups/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backups.zip/backups/note.txt PKZIP Encr: TS_chk, cmplen=67, decmplen=60, crc=AEE718A8 ts=24E2 cs=24e2 type=8
```

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cat ziphash.txt                                                               
backups.zip/backups/note.txt:$pkzip$1*1*2*0*43*3c*aee718a8*42*4a*8*43*24e2*2918f93964f9ffa39d4a5fc0d589cae4222fd228a12bc6459bf7b383bdc3cd74557af7a16783ba3217388d2db639162dcee0456f5264bb1839b0f63a28de19581bda79*$/pkzip$:backups/note.txt:backups.zip::backups.zip
```

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ john ziphash.txt --wordlist=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
00385007         (backups.zip/backups/note.txt)     
1g 0:00:00:02 DONE (2024-03-20 10:25) 0.4878g/s 6959Kp/s 6959Kc/s 6959KC/s 0066365..00377696192211
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ unzip backups.zip
Archive:  backups.zip
[backups.zip] backups/note.txt password: 
  inflating: backups/note.txt

┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cd backups

┌──(kali㉿kali)-[~/thm/mnemonic/backups]
└─$ ls -la
total 12
drwxrwxr-x 2 kali kali 4096 Mar 20 10:33 .
drwxr-xr-x 3 kali kali 4096 Mar 20 10:19 ..
-rw-r--r-- 1 kali kali   60 Jul 12  2020 note.txt

┌──(kali㉿kali)-[~/thm/mnemonic/backups]
└─$ cat note.txt   
@vill

James new ftp username: ftpuser
we have to work hard
```

We got the ftp username: ftpuser