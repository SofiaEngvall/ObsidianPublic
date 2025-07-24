
DNS settings -> [[Kali  + Windows DNS settings]]

### Enumerating AD room

Got creds from http://distributor.za.tryhackme.com/creds

Username: graeme.williams
Password: hJnlKuLBa2

`xfreerdp /dynamic-resolution /scale-desktop:150 /scale:100 +clipboard /cert:ignore /tls-seclevel:0 /v:thmjmp1.za.tryhackme.com /u:'za.tryhackme.com\phillip.reid' /p:'Scooter1987'` 

`ssh za.tryhackme.com\\phillip.reid@thmjmp1.za.tryhackme.com`

### Lateral Movement and Pivoting room

Username: damien.horton
Password: pABqHYKsG8L7

`ssh za\\damien.horton@thmjmp2.za.tryhackme.com`

---

In this network, we covered several techniques that can be used to enumerate AD. This is by no means an exhaustive list. Here is a list of enumeration techniques that also deserve mention:

- **[LDAP enumeration](https://book.hacktricks.xyz/pentesting/pentesting-ldap)** - Any valid AD credential pair should be able to bind to a Domain Controller's LDAP interface. This will allow you to write LDAP search queries to enumerate information regarding the AD objects in the domain.
- **[PowerView](https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1)** - PowerView is a recon script part of the [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) project. Although this project is no longer receiving support, scripts such as PowerView can be incredibly useful to perform semi-manual enumeration of AD objects in a pinch.
- **[Windows Management Instrumentation (WMI)](https://0xinfection.github.io/posts/wmi-ad-enum/)** - WMI can be used to enumerate information from Windows hosts. It has a provider called "root\directory\ldap" that can be used to interact with AD. We can use this provider and WMI in PowerShell to perform AD enumeration.

TODO! Add ^ to notes
