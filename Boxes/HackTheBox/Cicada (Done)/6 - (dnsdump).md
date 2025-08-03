
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/cicada]
└─$ bloodyAD --host 10.129.169.79 -d cicada.htb -u 'emily.oscars' -p 'Q!3@Lp#M6b*7t*Vt' get dnsDump

recordName: cicada.htb
AAAA: dead:beef::19c; dead:beef::15e:cea:ecd6:ab39
SOA.PrimaryServer: cicada-dc.cicada.htb
SOA.zoneAdminEmail: hostmaster@cicada.htb
NS: cicada-dc.cicada.htb
A: 10.129.169.79

recordName: _ldap._tcp.gc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:3268

recordName: _ldap._tcp.Default-First-Site-Name._sites.gc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:3268

recordName: _ldap._tcp.526effb7-04d9-4e71-8652-2afafc5fd8e0.domains._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: gc._msdcs.cicada.htb
AAAA: dead:beef::19c; dead:beef::15e:cea:ecd6:ab39
A: 10.129.169.79

recordName: 7ce436b6-8292-4500-a1a2-d580f7404157._msdcs.cicada.htb
CNAME: cicada-dc.cicada.htb

recordName: _kerberos._tcp.dc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:88

recordName: _kerberos._tcp.Default-First-Site-Name._sites.dc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:88

recordName: _ldap._tcp.dc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: _kerberos._tcp.cicada.htb
SRV: cicada-dc.cicada.htb:88

recordName: _kerberos._tcp.Default-First-Site-Name._sites.cicada.htb
SRV: cicada-dc.cicada.htb:88

recordName: _gc._tcp.cicada.htb
SRV: cicada-dc.cicada.htb:3268

recordName: _gc._tcp.Default-First-Site-Name._sites.cicada.htb
SRV: cicada-dc.cicada.htb:3268

recordName: _kerberos._udp.cicada.htb
SRV: cicada-dc.cicada.htb:88

recordName: _kpasswd._tcp.cicada.htb
SRV: cicada-dc.cicada.htb:464

recordName: _kpasswd._udp.cicada.htb
SRV: cicada-dc.cicada.htb:464

recordName: ForestDnsZones.cicada.htb
AAAA: dead:beef::19c; dead:beef::15e:cea:ecd6:ab39
A: 10.129.169.79

recordName: _ldap._tcp.ForestDnsZones.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: _ldap._tcp.Default-First-Site-Name._sites.ForestDnsZones.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: DomainDnsZones.cicada.htb
AAAA: dead:beef::19c; dead:beef::15e:cea:ecd6:ab39
A: 10.129.169.79

recordName: _ldap._tcp.DomainDnsZones.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: _ldap._tcp.Default-First-Site-Name._sites.DomainDnsZones.cicada.htb
SRV: cicada-dc.cicada.htb:389

recordName: cicada-dc.cicada.htb
AAAA: dead:beef::15e:cea:ecd6:ab39; dead:beef::19c
A: 10.129.169.79

zoneName: _msdcs.cicada.corp

SOA.PrimaryServer: cicada-dc.cicada.htb
SOA.zoneAdminEmail: hostmaster@cicada.corp
NS: cicada-dc.cicada.htb
recordName: _msdcs.cicada.corp

recordName: _ldap._tcp.cicada.htb

recordName: _ldap._tcp.Default-First-Site-Name._sites.cicada.htb

recordName: _ldap._tcp.pdc._msdcs.cicada.htb

recordName: _ldap._tcp.cicada.htb

recordName: _ldap._tcp.Default-First-Site-Name._sites.cicada.htb

recordName: _ldap._tcp.pdc._msdcs.cicada.htb
```

