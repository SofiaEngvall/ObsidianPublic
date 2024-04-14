
```
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ls -la 
total 28
drwxr-xr-x  3 kali kali 4096 Mar 20 11:13 .
drwxr-xr-x 11 kali kali 4096 Mar 20 10:03 ..
drwxrwxr-x  2 kali kali 4096 Mar 20 10:33 backups
-rw-r--r--  1 kali kali  409 Mar 20 10:00 backups.zip
-rw-r--r--  1 kali kali 1766 Jul 13  2020 id_rsa
-rw-r--r--  1 kali kali   31 Jul 13  2020 not.txt
-rw-r--r--  1 kali kali  261 Mar 20 10:19 ziphash.txt
                                                                                                                              
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cat not.txt                                        
james change ftp user password
                                                                                                                              
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ cat id_rsa                                                       
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,01762A15A5B935E96A1CF34704C79AC3

pSxCqzRmFf4dcfdkVay0+fN88/GXwl3LXOS1WQrRV26wqXTE1+EaL5LrRtET8mPM
dkScGB/cHICB0cPvn3WU8ptdYCk78w9X9wHpPBa6VLk1eRi7MANLcfRWxQ4GFwXp
CP8KSSZBCduabfcx6eLBBM8fMC+P2kgtIOhnlpt/sAU2zDQa8kZHw8V76pzcBLka
trq4ik4tpsgHqEU4BDw24bNjtJxgEy4sddtpXyy0i3KZ9gm6Uop6/jFG8uuoAQPn
AcwIZSCpjEfiMLzerVNNotZU9I11jRtbdQsxAjLPYY30PyO2cFlgpohvpyMD6lfO
33v8DOV8U69zlyUtUgArfZ9IORPKLOW5VLfuqX8yLsylVrmmuGdlfN+zO5enukjV
cg/mpJL/kePgViEqnTJf5Y8vYJ9tEGko8YBvorrsS0QXN7GJtW8h7IYrsLpXYzeu
FPD5cgEdixE4UlGo7G6nmlkikLsDwjjVIDX9C3eHljAhiktKAu19wbwdaJ8F4WWW
txZv/fsKBSI/JexzOY2lKSFq52Dod6G1eCVf0WgsQrXBOxgKn/iQ0dg4aCVNttni
kKKW3hEQP3gK6B20dnIItFzQpaqapuNJKnAWEj6YG+7QpCjncMEMUDGpCSqnMuYB
PVM3GU4sq5OO14gXtjOgTfBXP07cqkuW6L8XQl+sWobgVuIGmK69wfCZSjy29Hqo
8SmeUAdiv37UenHGLxwjelnNcblLm/BYyW6P6m6pc+zgUSK/MVysGj9B8ryLVcIc
P8O/HKResEUC/MZJGYWIZeu7UK/Ifs5IN/uTYmBM9/44tRJApvY+3rrdUUA3khjY
ZTzeX1/xS5rqprEYcr19ExboGVqNCUMHPwmufZZbB1uUagaR2Cv44j9rU19BVF1s
czMMNJGJSoeA4UKNIuXFVIMbMcZD2fCKaKYWT6C0RDS0TrAf7AUurgHReAqsQhTE
xxaGq7DLLflzVHC7EY2VhdAWmbNbGQi/k7+4wC6HTRbnLMh2kTFYMbGA64hDHxFP
DYJh4ZCEDiyWe1JkmaeAAyc2n0TCVsgEzxgGPGe3tZynVML/rFWDMA0B5kZ9VLS7
j5NOaTeWFwVy55ONPzGgCICsj+izaOuCvsbdJQ7FdQ0LPNzZ/RUFvh4k7E1ZjBos
y9GNQW8WMAWH7SFK91KdX4c+fsAPnHN/v7uF/dRWlzkusrVLznURsVtG0k2BxUwx
PYn3OG7SwGS+DyiFvvV0NspX2oIXEqA6VioqQxc+0dcEGxcyNY5uDut3BENGPD+X
Ut/fe6bIfVse+ovAb6F36SBquuDjJWCHaHyVMASlmmzA6A6XhlSnrxhVP2/cmtdo
zUicXz715Li1enhR6p68AzGhBzYZsF/F9MSbrBgust0zDeNllL/4slZ9zfrg+zUY
weJKZAn1ib9/mG+PcdcPLFTcWIbXvigSx22svaiuG9WbVzU7GolkStYnrTPdDJ8M
Nw6TzknzJ6s79cg6cKPefrQVFXYXYxSZOvK/TElYrirHqBacVwIyMxCbOgoUbsF2
ipwD46fpPTKgP6qwDirNcKtULMtEud/rbqVvnP+fqm5UC+oqoX+lb1g2fvytTXSe
-----END RSA PRIVATE KEY-----

```


Proc-Type: 4,ENCRYPTED

we need to use john

```sh
┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ ssh2john id_rsa > sshhash

┌──(kali㉿kali)-[~/thm/mnemonic]
└─$ john sshhash                                                                      
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
Proceeding with incremental:ASCII
bluelove         (id_rsa)     
1g 0:00:00:08 DONE 3/3 (2024-03-20 11:25) 0.1204g/s 1404Kp/s 1404Kc/s 1404KC/s bluelich..blueloc1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

bluelove
