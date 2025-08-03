
```sh
┌──(fixit42㉿kali)-[~]
└─$ bloodyAD --host 10.129.176.2 -d return.local -u 'svc-printer' -p '1edFg43012!!' get dnsDump 

zoneName: return.local

AAAA: dead:beef::187; dead:beef::9869:11b6:2008:de54
SOA.PrimaryServer: printer.return.local
SOA.zoneAdminEmail: hostmaster@return.local
NS: printer.return.local
A: 10.129.176.2
recordName: return.local

recordName: _ldap._tcp.return.local
SRV: printer.return.local:389

recordName: _ldap._tcp.Default-First-Site-Name._sites.return.local
SRV: printer.return.local:389

recordName: _msdcs.return.local
NS: win-hqu2bcql89c.return.local

recordName: DomainDnsZones.return.local
AAAA: dead:beef::187; dead:beef::9869:11b6:2008:de54
A: 10.129.176.2

recordName: ForestDnsZones.return.local
AAAA: dead:beef::187; dead:beef::9869:11b6:2008:de54
A: 10.129.176.2

recordName: win-hqu2bcql89c.return.local
A: 10.10.10.233
AAAA: dead:beef::c877:5c09:dab7:af47

recordName: printer.return.local
AAAA: dead:beef::9869:11b6:2008:de54; dead:beef::187
A: 10.129.176.2

SOA.PrimaryServer: printer.return.local
SOA.zoneAdminEmail: hostmaster@return.local
NS: printer.return.local
recordName: _msdcs.return.local

recordName: _ldap._tcp.d3137589-2523-4e02-8c2e-98b4fa01e413.domains._msdcs.return.local
SRV: printer.return.local:389

recordName: _ldap._tcp.Default-First-Site-Name._sites.gc._msdcs.return.local
SRV: printer.return.local:3268

recordName: _ldap._tcp.gc._msdcs.return.local
SRV: printer.return.local:3268

recordName: _ldap._tcp.pdc._msdcs.return.local
SRV: printer.return.local:389

recordName: c2a9b7bb-a190-4065-b4d6-f373b72005f0._msdcs.return.local
CNAME: printer.return.local

recordName: gc._msdcs.return.local
AAAA: dead:beef::187; dead:beef::9869:11b6:2008:de54
A: 10.129.176.2

recordName: _gc._tcp.return.local

recordName: _gc._tcp.Default-First-Site-Name._sites.return.local

recordName: _kerberos._tcp.return.local

recordName: _kerberos._tcp.Default-First-Site-Name._sites.return.local

recordName: _kerberos._udp.return.local

recordName: _kpasswd._tcp.return.local

recordName: _kpasswd._udp.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.DomainDnsZones.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.ForestDnsZones.return.local

recordName: _ldap._tcp.DomainDnsZones.return.local

recordName: _ldap._tcp.ForestDnsZones.return.local

recordName: _kerberos._tcp.dc._msdcs.return.local

recordName: _kerberos._tcp.Default-First-Site-Name._sites.dc._msdcs.return.local

recordName: _ldap._tcp.dc._msdcs.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.return.local

recordName: _gc._tcp.return.local

recordName: _gc._tcp.Default-First-Site-Name._sites.return.local

recordName: _kerberos._tcp.return.local

recordName: _kerberos._tcp.Default-First-Site-Name._sites.return.local

recordName: _kerberos._udp.return.local

recordName: _kpasswd._tcp.return.local

recordName: _kpasswd._udp.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.DomainDnsZones.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.ForestDnsZones.return.local

recordName: _ldap._tcp.DomainDnsZones.return.local

recordName: _ldap._tcp.ForestDnsZones.return.local

recordName: _kerberos._tcp.dc._msdcs.return.local

recordName: _kerberos._tcp.Default-First-Site-Name._sites.dc._msdcs.return.local

recordName: _ldap._tcp.dc._msdcs.return.local

recordName: _ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.return.local
```


recordName: win-hqu2bcql89c.return.local
A: 10.10.10.233
AAAA: dead:beef::c877:5c09:dab7:af47

?

