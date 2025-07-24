
`ldapdomaindump ldap://10.10.10.10 -u domain.com\\myuser -p mypassword`

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ldapdomaindump ldap://10.10.106.240 -u spookysec.local\\svc-admin -p management2005
[*] Connecting to host...
[*] Binding to host
[+] Bind OK
[*] Starting domain dump
[+] Domain dump finished

┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ ls -la                                                                             
total 1352
drwxrwxr-x  2 kali kali   4096 Jul  3 01:03 .
drwxr-xr-x 45 kali kali   4096 Jul  3 00:03 ..
-rwxr-xr-x  1 kali kali     48 Jul  3 00:38 backup_credentials.txt
-rw-rw-r--  1 kali kali   1301 Jul  3 01:03 domain_computers_by_os.html
-rw-rw-r--  1 kali kali    398 Jul  3 01:03 domain_computers.grep
-rw-rw-r--  1 kali kali   1293 Jul  3 01:03 domain_computers.html
-rw-rw-r--  1 kali kali   4793 Jul  3 01:03 domain_computers.json
-rw-rw-r--  1 kali kali  10418 Jul  3 01:03 domain_groups.grep
-rw-rw-r--  1 kali kali  17694 Jul  3 01:03 domain_groups.html
-rw-rw-r--  1 kali kali  88504 Jul  3 01:03 domain_groups.json
-rw-rw-r--  1 kali kali    244 Jul  3 01:03 domain_policy.grep
-rw-rw-r--  1 kali kali   1140 Jul  3 01:03 domain_policy.html
-rw-rw-r--  1 kali kali   5492 Jul  3 01:03 domain_policy.json
-rw-rw-r--  1 kali kali     71 Jul  3 01:03 domain_trusts.grep
-rw-rw-r--  1 kali kali    828 Jul  3 01:03 domain_trusts.html
-rw-rw-r--  1 kali kali      2 Jul  3 01:03 domain_trusts.json
-rw-rw-r--  1 kali kali  21848 Jul  3 01:03 domain_users_by_group.html
-rw-rw-r--  1 kali kali   4048 Jul  3 01:03 domain_users.grep
-rw-rw-r--  1 kali kali  11724 Jul  3 01:03 domain_users.html
-rw-rw-r--  1 kali kali  42426 Jul  3 01:03 domain_users.json
-rw-r--r--  1 kali kali 569236 Jul  3 00:04 passwordlist.txt
-rw-rw-r--  1 kali kali    558 Jul  3 00:29 svc-admin.hash
-rw-r--r--  1 kali kali 540470 Jul  3 00:04 userlist.txt
```

![[../../Boxes/TryHackMe/Attacktive Directory (Done)/Images/Pasted image 20250703011149.png]]

