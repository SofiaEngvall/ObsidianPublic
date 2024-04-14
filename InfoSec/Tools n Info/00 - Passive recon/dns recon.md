
`host <domainname>`

```sh
┌──(kali㉿kali)-[~]
└─$ host fixitnow.se
fixitnow.se has address 185.189.49.220
fixitnow.se has address 46.59.102.201
fixitnow.se has IPv6 address 2001:67c:750::8
fixitnow.se mail is handled by 10 mail.fixitnow.se.
```

`nslookup <domainname>`

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

`traceroute <domainname>`

```sh
sofia@Main-i732:~$ traceroute -m 100 -q 10 fixitnow.se
traceroute to fixitnow.se (185.189.49.220), 100 hops max, 60 byte packets
1  Main-i732 (172.25.224.1)  1.222 ms  1.130 ms  1.102 ms  1.081 ms  1.057 ms  1.036 ms  1.015 ms  0.993 ms  1.091 ms  1.071 ms
2  192.168.0.1 (192.168.0.1)  0.940 ms  0.918 ms  0.898 ms  1.228 ms  1.204 ms  1.175 ms  1.108 ms  1.028 ms  1.094 ms  1.024 ms
3  * * * * * * * * * *
4  31-209-57-177.cust.bredband2.com (31.209.57.177)  3.246 ms  3.189 ms  3.518 ms  3.448 ms  3.186 ms  3.307 ms  1.880 ms  1.898 ms  1.993 ms1.820 ms
5  hu0000-sto-esb11-cr1.se.bredband2.net (82.209.171.222)  1.213 ms  1.192 ms  1.614 ms  1.692 ms  1.494 ms  1.422 ms  1.553 ms  1.514 ms  1.492 ms  1.326 ms
6  31-208-232-103.cust.bredband2.com (31.208.232.103)  0.824 ms  0.817 ms  0.833 ms  0.830 ms  0.896 ms  0.888 ms  0.737 ms  0.814 ms  0.889 ms  0.988 ms
7  netnod-ix-ge-a-sth-1500.he.net (194.68.123.187)
15.033 ms * * * * * * * * *
8  yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.381 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.284 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.369 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.337 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.358 ms  12.419 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.441 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  2.716 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.480 ms  1.424 ms
9  * * * * * * * * * *
10  * * * * * * * * * *
```

`dnsrecon <domainname>`

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

`wafw00f fixitnow.se`

```sh
┌──(kali㉿kali)-[~]
└─$ wafw00f fixitnow.se
                ______
               /      \                                                                                                                                           (  W00f! )                                                                                                                                           \  ____/                                                                                                                                            ,,    __            404 Hack Not Found                                                                                                          |`-.__   / /                      __     __                                                                                                         /"  _/  /_/                       \ \   / /                                                                                                        *===*    /                          \ \_/ /  405 Not Allowed                                                                                       /     )__//                           \   /                                                                                                    /|  /     /---`                        403 Forbidden                                                                                                \\/`   \ |                                 / _ \                                                                                                    `\    /_\\_              502 Bad Gateway  / / \ \  500 Internal Error                                                                                 `_____``-`                             /_/   \_\                                                                                                                                      
                        ~ WAFW00F : v2.2.0 ~                                                                                                                The Web Application Firewall Fingerprinting Toolkit                                                                                                                                 
[*] Checking https://fixitnow.se
[+] Generic Detection results:
[-] No WAF detected by the generic detection
[~] Number of requests: 7
```

