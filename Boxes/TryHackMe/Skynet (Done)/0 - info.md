
10.10.70.22
10.10.155.35

22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))

110/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: UIDL RESP-CODES TOP SASL PIPELINING CAPA AUTH-RESP-CODE
143/tcp open  imap        Dovecot imapd
|_imap-capabilities: ID have Pre-login ENABLE LITERAL+ IMAP4rev1 LOGIN-REFERRALS post-login listed capabilities IDLE OK SASL-IR LOGINDISABLEDA0001 more

139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)

nbstat: NetBIOS name: SKYNET

---

|   \\10.10.155.35\anonymous: 
|     Comment: Skynet Anonymous Share
|     Path: C:\srv\samba
|     Anonymous access: READ/WRITE

|   \\10.10.155.35\milesdyson: 
|     Comment: Miles Dyson Personal Share
|     Path: C:\home\milesdyson\share
|     Anonymous access: none

| smb-enum-users: 
|   `SKYNET\milesdyson (RID: 1000)`

---

```sh
┌──(kali㉿kali)-[~/thm/skynet]
└─$ cat attention.txt 
A recent system malfunction has caused various passwords to be changed. All skynet employees are required to change their password after seeing this.
-Miles Dyson
```

`[80][http-post-form] host: skynet.thm   login: milesdyson   password: cyborg007haloterminator`

---

logged into mail

mail1
Subject:   	Samba Password reset
From:   	skynet@skynet
We have changed your smb password after system malfunction.
Password: )s{A&2Z=F^n_E.B

---

```sh
┌──(kali㉿kali)-[~/thm/skynet/notes]
└─$ cat important.txt

1. Add features to beta CMS /45kra24zxs28v3yd
2. Work on T-800 Model 101 blueprints
3. Spend more time with my wife
```

---

```sh
cat ./backups/backup.sh
#!/bin/bash
cd /var/www/html
tar cf /home/milesdyson/backups/backup.tgz *
www-data@skynet:/home/milesdyson$ cat /etc/crontab
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
*/1 *   * * *   root    /home/milesdyson/backups/backup.sh
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

