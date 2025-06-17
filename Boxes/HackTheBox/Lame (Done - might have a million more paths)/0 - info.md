
10.10.10.3

---

21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)

22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)

139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)

3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))

|   OS: Unix (Samba 3.0.20-Debian)

|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr

|_smb2-time: Protocol negotiation failed (SMB2)

---

there seem to be no files on the ftp

---

distccd = distributed C/C++ compiler
allows others to use your computer power to compile stuff
user distccd

---

| smb-enum-users: 

|   LAME\distccd (RID: 1222)
|     Flags:       Account disabled, Normal user account

|   LAME\msfadmin (RID: 3000)
|     Full name:   msfadmin,,,
|     Flags:       Normal user account

|   LAME\user (RID: 3002)
|     Full name:   just a user,111,,
|     Flags:       Normal user account

The account we found out should exist is disabled
But we have two other users:
user
msfadmin

---

| smb-enum-shares: 

|   account_used: `<blank>`

|   \\10.10.10.3\IPC$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Path: C:\tmp
|     Anonymous access: READ/WRITE

|   \\10.10.10.3\tmp: 
|     Type: STYPE_DISKTREE
|     Comment: oh noes!
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE

Let's check out `\\10.10.10.3\tmp`

---

id 
uid=1(daemon) gid=1(daemon) groups=1(daemon)
whoami
daemon



