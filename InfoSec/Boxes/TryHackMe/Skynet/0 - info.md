
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

mail2
From:   	serenakogan@skynet

01100010 01100001 01101100 01101100 01110011 00100000 01101000 01100001 01110110
01100101 00100000 01111010 01100101 01110010 01101111 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111 00100000 01101101 01100101 00100000 01110100 01101111
00100000 01101101 01100101 00100000 01110100 01101111 00100000 01101101 01100101
00100000 01110100 01101111

mail3

---

```sh
┌──(kali㉿kali)-[~/thm/skynet/notes]
└─$ cat important.txt

1. Add features to beta CMS /45kra24zxs28v3yd
2. Work on T-800 Model 101 blueprints
3. Spend more time with my wife
```