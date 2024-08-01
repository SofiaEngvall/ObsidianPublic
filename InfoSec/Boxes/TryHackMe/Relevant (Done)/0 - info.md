
Find and report ALL vulnerabilities (yes, there is more than one path to root)

I encourage you to approach this challenge as an actual penetration test. Consider writing a report, to include an executive summary, vulnerability and exploitation assessment, and remediation suggestions

10.10.182.105

80/tcp    open  http          Microsoft IIS httpd 10.0
49663/tcp open  http          Microsoft IIS httpd 10.0

135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC

|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant

---

```
SMB         10.10.182.105   445    RELEVANT         nt4wrksv        READ,WRITE   
```
READ/WRITE even for guest

Found file:
```
Bob - !P@$$W0rD!123 
Bill - Juw4nnaM4n420696969!$$$ 
```

```
SMB         10.10.182.105   445    RELEVANT         [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:RELEVANT) (domain:Relevant) (signing:False) (SMBv1:True)

SMB         10.10.182.105   445    RELEVANT         500: RELEVANT\Administrator (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         501: RELEVANT\Guest (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         503: RELEVANT\DefaultAccount (SidTypeUser)
SMB         10.10.182.105   445    RELEVANT         513: RELEVANT\None (SidTypeGroup)
SMB         10.10.182.105   445    RELEVANT         1002: RELEVANT\Bob (SidTypeUser)
```


---

Confirmed user: Bob
Password: `!P@$$W0rD!123`

dirsearch:
found a directory with the same name as the smb share we have write access to

