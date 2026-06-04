
ubuntu@10.80.176.8
AOC2025Ubuntu!

```sh
ubuntu@tryhackme:~/Desktop$ ls -la
total 64
drwxr-xr-x  3 ubuntu ubuntu  4096 Oct 16 16:23 .
drwxr-xr-x 21 ubuntu ubuntu  4096 Dec 11 18:51 ..
-rw-r--r--  1 ubuntu ubuntu 42484 Oct  6 11:46 flag.pdf
-rw-r--r--  1 ubuntu ubuntu   245 Oct  6 11:46 flag.zip
drwxrwxr-x 10 ubuntu ubuntu  4096 Oct 16 15:25 john
-rwxrwxr-x  1 ubuntu ubuntu   166 Feb 27  2022 mate-terminal.desktop

ubuntu@tryhackme:~/Desktop$ file flag.pdf
flag.pdf: PDF document, version 1.7, 1 page(s)

ubuntu@tryhackme:~/Desktop$ file flag.zip
flag.zip: Zip archive data, at least v2.0 to extract, compression method=AES Encrypted
```

```sh
ubuntu@tryhackme:~/Desktop$ pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
PDF version 1.7
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 3792b9a3671ef54bbfef57c6fe61ce5d
U: c46529c06b0ee2bab7338e9448d37c3200000000000000000000000000000000
O: 95d0ad7c11b1e7b3804b18a082dda96b4670584d0044ded849950243a8a367ff
found user-password: 'naughtylist'
```

```sh
ubuntu@tryhackme:~/Desktop$ zip2john flag.zip
flag.zip/flag.txt:$zip2$*0*3*0*db58d2418c954f6d78aefc894faebf54*d89c*1d*b8370111f4d9eba3ca5ff6924f8c4ff8636055dce00daec2679f57bde1*57445596ac0bc2a29297*$/zip2$:flag.txt:flag.zip:flag.zip

ubuntu@tryhackme:~/Desktop$ zip2john flag.zip > ziphash

ubuntu@tryhackme:~/Desktop$ john --wordlist=/usr/share/wordlists/rockyou.txt ziphash
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Cost 1 (HMAC size [KiB]) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
winter4ever      (flag.zip/flag.txt)     
1g 0:00:00:00 DONE (2025-12-11 19:06) 3.571g/s 14628p/s 14628c/s 14628C/s friend..sahara
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day9]
└─$ scp ubuntu@10.80.176.8:Desktop/flag.zip .                              
ubuntu@10.80.176.8's password: 
flag.zip                                                                                    100%  245     3.3KB/s   00:00  ┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day9]
└─$ scp ubuntu@10.80.176.8:Desktop/flag.pdf .
ubuntu@10.80.176.8's password: 
flag.pdf 
```

![[Images/Pasted image 20251211203810.png]]

![[Images/Pasted image 20251211203949.png]]

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day9]
└─$ 7z x flag.zip

7-Zip 25.01 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
 64-bit locale=en_US.UTF-8 Threads:128 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 245 bytes (1 KiB)

Extracting archive: flag.zip
--
Path = flag.zip
Type = zip
Physical Size = 245

    
Enter password (will not be echoed):
Everything is Ok

Size:       29
Compressed: 245

┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day9]
└─$ cat flag.txt
THM{Cr4ck1n6_z1p$_1s_34$yyyy}
```

