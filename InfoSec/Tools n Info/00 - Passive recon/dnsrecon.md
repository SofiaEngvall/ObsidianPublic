
`dnsrecon <domainname>`

`dnsrecon -d domain.com -t axfr`

```sh
┌──(kali㉿kali)-[~]
└─$ dnsrecon -d fixitnow.se
[*] std: Performing General Enumeration against: fixitnow.se...
[*] DNSSEC is configured for fixitnow.se
[*] DNSKEYs:
[*]     NSEC ZSK ECDSAP256SHA256 b9bd652ef99c4908a0d2382ed7bb72b1 2dc139dbc7771b38517b9e142818d3fb 97c87811b3bfd4a4125ce46df6622645 c9788698919f320dbc8435567abaa79e
[*]     NSEC KSk ECDSAP256SHA256 ecb8b3ef3fb3f257fcc03edaa004da19 33939bd80b474bc8dfe010739bc9bec2 8261d2babd519342ff813844ea9941e2 a236951241a9bacd3167c9480243577c
[*]      SOA ns1.inleed.net 185.189.49.214
[*]      SOA ns1.inleed.net 2001:67c:750::2
[*]      NS ns6.inleed.net 185.189.49.219
[*]      Bind Version for 185.189.49.219 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns6.inleed.net 2001:67c:750::7
[*]      NS ns1.inleed.net 185.189.49.214
[*]      Bind Version for 185.189.49.214 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns1.inleed.net 2001:67c:750::2
[*]      NS ns2.inleed.net 185.189.49.215
[*]      Bind Version for 185.189.49.215 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns2.inleed.net 2001:67c:750::3
[*]      NS ns5.inleed.net 185.189.49.218
[*]      Bind Version for 185.189.49.218 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns5.inleed.net 2001:67c:750::6
[*]      NS ns4.inleed.net 194.68.59.6
[*]      Bind Version for 194.68.59.6 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns4.inleed.net 2001:67c:750::5
[*]      NS ns3.inleed.net 185.189.49.216
[*]      Bind Version for 185.189.49.216 "9.11.4-P2-RedHat-9.11.4-26.P2.el7_9.14"
[*]      NS ns3.inleed.net 2001:67c:750::4
[*]      MX mail.fixitnow.se 46.59.102.201
[*]      MX mail.fixitnow.se 185.189.49.220
[*]      MX mail.fixitnow.se 2001:67c:750::8
[*]      A fixitnow.se 46.59.102.201
[*]      A fixitnow.se 185.189.49.220
[*]      AAAA fixitnow.se 2001:67c:750::8
[*]      TXT fixitnow.se v=spf1 a mx include:spf.inleed.se ip4:185.189.49.220 -all
[*]      TXT _dmarc.fixitnow.se v=DMARC1; p=none; sp=none;
[*] Enumerating SRV Records
[+]      SRV _autodiscover._tcp.fixitnow.se autodiscover.inleed.se 194.14.207.121 443
[+]      SRV _autodiscover._tcp.fixitnow.se autodiscover.inleed.se 2001:67c:750::2 443
[+] 2 Records Found
```
