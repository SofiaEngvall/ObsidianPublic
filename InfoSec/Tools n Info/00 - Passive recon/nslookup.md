
`nslookup [options] <domainname>`

`nslookup -type=MX tryhackme.com 1.1.1.1`
`nslookup -type=TXT tryhackme.com`
###### Options
`-type=A` ...
`A` IPv4
`AAAA` IPv6
`CNAME` Canonical Name
`MX`	Mail Servers
`SOA` Start of Authority
`TXT` TXT Records


<u>works on windows too</u>

`nslookup`
\>`set type=ns`
\>`domain.com`

\>`server ns.domain.com`
\>`set type=any`
\>`ls -d domain.com`

```sh
┌──(kali㉿kali)-[~]
└─$ nslookup fixitnow.se             
Server:         192.168.233.2
Address:        192.168.233.2#53

Non-authoritative answer:
Name:   fixitnow.se
Address: 46.59.102.201
Name:   fixitnow.se
Address: 185.189.49.220
Name:   fixitnow.se
Address: 2001:67c:750::8
```
