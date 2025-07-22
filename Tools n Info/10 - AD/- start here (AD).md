

### finding the dc - in a network

##### from a windows client
 
 should be easy :D
 add something here

##### from a linux client on a windows network

If you're on a linux box in a ad network port scan for 88 to find the dc (not for red team)

### port scan

normal full nmap scan ([[../../Boxes/TryHackMe/Attacktive Directory/1 - nmap|nmap scan example]])
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

Examples from [[../../Boxes/TryHackMe/Attacktive Directory/1 - nmap|1 - nmap]]:
- NetBIOS name: `ATTACKTIVEDIREC`
- DNS name: `AttacktiveDirectory.spookysec.local`
- Domain name: `spookysec.local`

### dc time

in the nmap scan we see something like
`88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-07-02 21:05:34Z)`

for some things we need a similar time as the dc (within one minute)


### Listen with responder
- more: [[../29 - C2s, listening tools/responder|responder]] 
- examples to make people connect to responder:
	- send an e-mail with a smb link
	- get a smb link out some other way


### null session..
`nxc smb -u '' -p ''`



### user enumeration

`impacket-GetNPUsers spookysec.local/ -usersfile userlist.txt -no-pass -dc-ip 10.10.106.240`
- gives hashcat hash too!

`nxc smb 10.10.106.240 -u users.txt -p '' --kerberos` (req hosts file entries)
- finds vuln accounts



