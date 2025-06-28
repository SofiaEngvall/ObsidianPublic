
usual ports

53 dns
88 kerberos

139+445 smb

389 ldap
636 ldap ssl
3268 global ldap
3269 global ldap ssl

5985 rdp


If you're on a linux box in a ad network

port scan for 88 to find the dc (not for red team)
responder

normal full nmap scan
`nmap -sC -sV -Pn 10.10.10.10`


