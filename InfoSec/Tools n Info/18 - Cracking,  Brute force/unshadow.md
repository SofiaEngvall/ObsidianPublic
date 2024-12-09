
used to combine /etc/passwd and /etc/shadow for use with john

### Help

```sh
┌──(kali㉿kali)-[~/thm/hashes]
└─$ unshadow --help
Usage: unshadow PASSWORD-FILE SHADOW-FILE
```

### Examples

```sh
┌──(kali㉿kali)-[~/thm/hashes]
└─$ unshadow etc-passwd etc-shadow 
root:$6$Ha.d5nGupBm29pYr$yugXSk24ZljLTAZZagtGwpSQhb3F2DOJtnHrvk7HI2ma4GsuioHp8sm3LJiRJpKfIf7lZQ29qgtH17Q/JDpYM/:0:0::/root:/bin/bash
                                                                                                                             
┌──(kali㉿kali)-[~/thm/hashes]
└─$ cat etc-shadow      
root:$6$Ha.d5nGupBm29pYr$yugXSk24ZljLTAZZagtGwpSQhb3F2DOJtnHrvk7HI2ma4GsuioHp8sm3LJiRJpKfIf7lZQ29qgtH17Q/JDpYM/:18576::::::

┌──(kali㉿kali)-[~/thm/hashes]
└─$ unshadow etc-passwd etc-shadow > etc-combined

┌──(kali㉿kali)-[~/thm/hashes]
└─$ john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt etc-combined
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
1234             (root)     
1g 0:00:00:00 DONE (2024-04-04 13:34) 2.380g/s 3047p/s 3047c/s 3047C/s kucing..poohbear1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

```sh
┌──(kali㉿kali)-[~/pentesterlab]
└─$echo "victim:$1$f4teV/4d$jL52CAMpqxNqjHhMf/jE2.:20065:0:99999:7:::" > unix16-shadow

┌──(kali㉿kali)-[~/pentesterlab]
└─$ john unix16-shadow --format=md5crypt                                           
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
victim4          (victim)     
1g 0:00:00:00 DONE 1/3 (2024-12-08 23:45) 100.0g/s 4800p/s 4800c/s 4800C/s victim..VictimVictim
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

### Common Commands

unshadow etc-passwd etc-shadow

