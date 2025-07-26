
return
10.129.176.2

---

ad server

80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-title: HTB Printer Admin Panel
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE

389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: return.local0., Site: Default-First-Site-Name)

Service Info: Host: PRINTER; OS: Windows; CPE: cpe:/o:microsoft:windows

---

x64 (name:PRINTER) (domain:return.local) (signing:True) (SMBv1:False)

---

Server Address 	printer.return.local
Server Port 	389
Username 	svc-printer
Password 	`*******`

set password to password and clicked update

---

[LDAP] Cleartext Client   : 10.129.176.2
[LDAP] Cleartext Username : return\svc-printer
[LDAP] Cleartext Password : 1edFg43012!!

---

..

---

Mandatory Label\High Mandatory Level       Label            S-1-16-12288

SeBackupPrivilege             Back up files and directories       Enabled



