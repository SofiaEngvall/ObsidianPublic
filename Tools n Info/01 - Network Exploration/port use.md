
https://www.speedguide.net/ports.php
https://wiki.wireshark.org/PortReference
### TCP
TCP - high reliability, website, SSH, FTP
TCP - Three way handshake “Syn” > “Syn Ack” > “Ack” - Can be used to collect data

20 ftp data
21 ftp                ftp     if ftp port open, try ftp 10.10.10.10 and login with anonymous
22 [[InfoSec/Tools n Info/01.5 - Connection/ssh|ssh]], sftp (ftp using ssh)
23 telnet
25 smtp
53 dns
80 http
110 pop3
143 imap
443 https, DoH dns over https
139+445 smb
465+587 smtps
853 DoT dns over tls
990 ftps (ftp using tls)
993 imaps
995 pop3s
50051     gRPC            [[../15 - APIs/grpcui]]

### UDP 
UDP (connectionless) - streaming, DNS, VOIP

dns 53
dhcp server listens on 67
dhcp client sends on 68
tftp 69
snmp 161
