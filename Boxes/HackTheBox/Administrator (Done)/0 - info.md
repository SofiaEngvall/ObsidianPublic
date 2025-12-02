
administrator
10.129.203.207
10.129.229.8 (restarted box)
10.129.114.23 (restarted box)

Machine Information

As is common in real life Windows pentests, you will start the Administrator box with credentials for the following account: Username: Olivia Password: ichliebedich

user:
Olivia:ichliebedich

---
dc
ftp, smb, dns, winrm

clock-skew: 7h00m00s

Microsoft Windows Active Directory LDAP
Domain: administrator.htb

---

Windows Server 2022 Build 20348 x64

---

We got five users:
michael
benjamin
emily
olivia
ethan
administrator

---

dn: CN=Olivia Johnson,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb

---

The user OLIVIA@ADMINISTRATOR.HTB has GenericAll permissions to the user MICHAEL@ADMINISTRATOR.HTB.

The user MICHAEL@ADMINISTRATOR.HTB has the capability to change the user BENJAMIN@ADMINISTRATOR.HTB's password without knowing that user's current password.

---

michael:Password123!
benjamin:Password123!

---

benjamin had ftp access and we found a file containing more creds:

alexander:UrkIbagoxMyUGw0aPlj9B0AXSea4Sw
emma:WwANQWnmJnGV07WQN8bMS7FMAbjNur

emily:UXLCI5iETUsIBoFVTj8yQFKoHjXmb

dn: CN=Emily Rodriguez,CN=Users,DC=administrator,DC=htb
memberOf: CN=Remote Management Users,CN=Builtin,DC=administrator,DC=htb
sAMAccountName: emily

emily is a winrm user and we saw she has a user directory

we found user.txt on emilys desktop

there's also a link to edge - is this a hint?

---

ethan:limpbizkit

---

dcsync
administrator:3dc553ce4b9fd20bd016e098d2d2fd2e


