

http://www.vmaxx.net/techinfo/ports.htm
https://wiki.wireshark.org/PortReference
### TCP
TCP - high reliability, website, SSH, FTP
TCP - Three way handshake “Syn” > “Syn Ack” > “Ack” - Can be used to collect data

20 ftp data
21 ftp                ftp     if ftp port open, try ftp 10.10.10.10 and login with anonymous
22 ssh               [[InfoSec/Tools n Info/01.5 - Connection/ssh|ssh]]
23 telnet
25 smtp
53 dns
80 http
110 pop3
143 imap
443 https
smb 139+445
imap 143
50051     gRPC            [[grpcui]]

### UDP 
UDP (connectionless) - streaming, DNS, VOIP

dns 53
dhcp 67, 68
tftp 69
snmp 161
