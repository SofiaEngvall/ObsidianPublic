Details at https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements

## Ports and protocols

The following table summarizes the information from the [System services ports](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements#system-services-ports) section. This table is sorted by port number instead of by service name.

| Port                                     | Protocol | Application protocol                     | System service name                                      |
| ---------------------------------------- | -------- | ---------------------------------------- | -------------------------------------------------------- |
| n/a                                      | GRE      | GRE (IP protocol 47)                     | Routing and Remote Access                                |
| n/a                                      | ESP      | IPsec ESP (IP protocol 50)               | Routing and Remote Access                                |
| n/a                                      | AH       | IPsec AH (IP protocol 51)                | Routing and Remote Access                                |
| 7                                        | TCP      | Echo                                     | Simple TCP/IP Services                                   |
| 7                                        | UDP      | Echo                                     | Simple TCP/IP Services                                   |
| 9                                        | TCP      | Discard                                  | Simple TCP/IP Services                                   |
| 9                                        | UDP      | Discard                                  | Simple TCP/IP Services                                   |
| 13                                       | TCP      | Daytime                                  | Simple TCP/IP Services                                   |
| 13                                       | UDP      | Daytime                                  | Simple TCP/IP Services                                   |
| 17                                       | TCP      | `Quotd`                                  | Simple TCP/IP Services                                   |
| 17                                       | UDP      | `Quotd`                                  | Simple TCP/IP Services                                   |
| 19                                       | TCP      | `Chargen`                                | Simple TCP/IP Services                                   |
| 19                                       | UDP      | `Chargen`                                | Simple TCP/IP Services                                   |
| 20                                       | TCP      | FTP default data                         | FTP Publishing Service                                   |
| 21                                       | TCP      | FTP control                              | FTP Publishing Service                                   |
| 21                                       | TCP      | FTP control                              | Application Layer Gateway Service                        |
| 23                                       | TCP      | Telnet                                   | Telnet                                                   |
| 25                                       | TCP      | SMTP                                     | Simple Mail Transfer Protocol                            |
| 25                                       | TCP      | SMTP                                     | Exchange Server                                          |
| 42                                       | TCP      | WINS Replication                         | Windows Internet Name Service                            |
| 42                                       | UDP      | WINS Replication                         | Windows Internet Name Service                            |
| 53                                       | TCP      | DNS                                      | DNS Server                                               |
| 53                                       | UDP      | DNS                                      | DNS Server                                               |
| 53                                       | TCP      | DNS                                      | Internet Connection Firewall/Internet Connection Sharing |
| 53                                       | UDP      | DNS                                      | Internet Connection Firewall/Internet Connection Sharing |
| 67                                       | UDP      | DHCP Server                              | DHCP Server                                              |
| 67                                       | UDP      | DHCP Server                              | Internet Connection Firewall/Internet Connection Sharing |
| 69                                       | UDP      | TFTP                                     | Trivial FTP Daemon Service                               |
| 80                                       | TCP      | HTTP                                     | Windows Media Services                                   |
| 80                                       | TCP      | HTTP                                     | WinRM 1.1 and earlier                                    |
| 80                                       | TCP      | HTTP                                     | World Wide Web Publishing Service                        |
| 80                                       | TCP      | HTTP                                     | SharePoint Portal Server                                 |
| 88                                       | TCP      | Kerberos                                 | Kerberos Key Distribution Center                         |
| 88                                       | UDP      | Kerberos                                 | Kerberos Key Distribution Center                         |
| 102                                      | TCP      | X.400                                    | Microsoft Exchange MTA Stacks                            |
| 110                                      | TCP      | POP3                                     | Microsoft POP3 Service                                   |
| 110                                      | TCP      | POP3                                     | Exchange Server                                          |
| 119                                      | TCP      | NNTP                                     | Network News Transfer Protocol                           |
| 123                                      | UDP      | NTP                                      | Windows Time                                             |
| 123                                      | UDP      | SNTP                                     | Windows Time                                             |
| 135                                      | TCP      | RPC                                      | Message Queuing                                          |
| 135                                      | TCP      | RPC                                      | Remote Procedure Call                                    |
| 135                                      | TCP      | RPC                                      | Exchange Server                                          |
| 135                                      | TCP      | RPC                                      | Certificate Services                                     |
| 135                                      | TCP      | RPC                                      | Cluster Service                                          |
| 135                                      | TCP      | RPC                                      | Distributed File System Namespaces                       |
| 135                                      | TCP      | RPC                                      | Distributed Link Tracking                                |
| 135                                      | TCP      | RPC                                      | Distributed Transaction Coordinator                      |
| 135                                      | TCP      | RPC                                      | Distributed File Replication Service                     |
| 135                                      | TCP      | RPC                                      | Fax Service                                              |
| 135                                      | TCP      | RPC                                      | Microsoft Exchange Server                                |
| 135                                      | TCP      | RPC                                      | File Replication Service                                 |
| 135                                      | TCP      | RPC                                      | Group Policy                                             |
| 135                                      | TCP      | RPC                                      | Local Security Authority                                 |
| 135                                      | TCP      | RPC                                      | Remote Storage Notification                              |
| 135                                      | TCP      | RPC                                      | Remote Storage                                           |
| 135                                      | TCP      | RPC                                      | Systems Management Server 2.0                            |
| 135                                      | TCP      | RPC                                      | RDSL                                                     |
| 135                                      | TCP      | RPC                                      | Remote Desktop Connection Broker                         |
| 137                                      | UDP      | NetBIOS Name Resolution                  | Computer Browser                                         |
| 137                                      | UDP      | NetBIOS Name Resolution                  | Server                                                   |
| 137                                      | UDP      | NetBIOS Name Resolution                  | Windows Internet Name Service                            |
| 137                                      | UDP      | NetBIOS Name Resolution                  | Net Logon                                                |
| 137                                      | UDP      | NetBIOS Name Resolution                  | Systems Management Server 2.0                            |
| 138                                      | UDP      | NetBIOS Datagram Service                 | Computer Browser                                         |
| 138                                      | UDP      | NetBIOS Datagram Service                 | Server                                                   |
| 138                                      | UDP      | NetBIOS Datagram Service                 | Net Logon                                                |
| 138                                      | UDP      | NetBIOS Datagram Service                 | Distributed File System                                  |
| 138                                      | UDP      | NetBIOS Datagram Service                 | Systems Management Server 2.0                            |
| 138                                      | UDP      | NetBIOS Datagram Service                 | License Logging Service                                  |
| 139                                      | TCP      | NetBIOS Session Service                  | Computer Browser                                         |
| 139                                      | TCP      | NetBIOS Session Service                  | Fax Service                                              |
| 139                                      | TCP      | NetBIOS Session Service                  | Performance Logs and Alerts                              |
| 139                                      | TCP      | NetBIOS Session Service                  | Print Spooler                                            |
| 139                                      | TCP      | NetBIOS Session Service                  | Server                                                   |
| 139                                      | TCP      | NetBIOS Session Service                  | Net Logon                                                |
| 139                                      | TCP      | NetBIOS Session Service                  | Remote Procedure Call Locator                            |
| 139                                      | TCP      | NetBIOS Session Service                  | Distributed File System Namespaces                       |
| 139                                      | TCP      | NetBIOS Session Service                  | Systems Management Server 2.0                            |
| 139                                      | TCP      | NetBIOS Session Service                  | License Logging Service                                  |
| 143                                      | TCP      | IMAP                                     | Exchange Server                                          |
| 161                                      | UDP      | SNMP                                     | SNMP Service                                             |
| 162                                      | UDP      | SNMP Traps Outgoing                      | SNMP Trap Service                                        |
| 389                                      | TCP      | LDAP Server                              | Local Security Authority                                 |
| 389                                      | UDP      | DC Locator                               | Local Security Authority                                 |
| 389                                      | TCP      | LDAP Server                              | Distributed File System Namespaces                       |
| 389                                      | UDP      | DC Locator                               | Distributed File System Namespaces                       |
| 389                                      | UDP      | DC Locator                               | `Netlogon`                                               |
| 389                                      | UDP      | DC Locator                               | Kerberos Key Distribution Center                         |
| 389                                      | TCP      | LDAP Server                              | Distributed File System Replication                      |
| 389                                      | UDP      | DC Locator                               | Distributed File System Replication                      |
| 443                                      | TCP      | HTTPS                                    | HTTP SSL                                                 |
| 443                                      | TCP      | HTTPS                                    | World Wide Web Publishing Service                        |
| 443                                      | TCP      | HTTPS                                    | SharePoint Portal Server                                 |
| 443                                      | TCP      | RPC over HTTPS                           | Exchange Server 2003                                     |
| 443                                      | TCP      | HTTPS                                    | WinRM 1.1 and earlier                                    |
| 445                                      | TCP      | SMB                                      | Fax Service                                              |
| 445                                      | TCP      | SMB                                      | Print Spooler                                            |
| 445                                      | TCP      | SMB                                      | Server                                                   |
| 445                                      | TCP      | SMB                                      | Remote Procedure Call Locator                            |
| 445                                      | TCP      | SMB                                      | Distributed File System Namespaces                       |
| 445                                      | TCP      | SMB                                      | Distributed File System Replication                      |
| 445                                      | TCP      | SMB                                      | License Logging Service                                  |
| 445                                      | TCP      | SMB                                      | Net Logon                                                |
| 464                                      | UDP      | Kerberos Password V5                     | Kerberos Key Distribution Center                         |
| 464                                      | TCP      | Kerberos Password V5                     | Kerberos Key Distribution Center                         |
| 500                                      | UDP      | IPsec ISAKMP                             | Local Security Authority                                 |
| 515                                      | TCP      | LPD                                      | TCP/IP Print Server                                      |
| 554                                      | TCP      | RTSP                                     | Windows Media Services                                   |
| 563                                      | TCP      | NNTP over SSL                            | Network News Transfer Protocol                           |
| 593                                      | TCP      | RPC over HTTPS endpoint mapper           | Remote Procedure Call                                    |
| 593                                      | TCP      | RPC over HTTPS                           | Exchange Server                                          |
| 636                                      | TCP      | LDAP SSL                                 | Local Security Authority                                 |
| 636                                      | UDP      | LDAP SSL                                 | Local Security Authority                                 |
| 647                                      | TCP      | DHCP Failover                            | DHCP Failover                                            |
| 9389                                     | TCP      | Active Directory Web Services (ADWS)     | Active Directory Web Services (ADWS)                     |
| 9389                                     | TCP      | Active Directory Web Services (ADWS)     | Active Directory Management Gateway Service              |
| 993                                      | TCP      | IMAP over SSL                            | Exchange Server                                          |
| 995                                      | TCP      | POP3 over SSL                            | Exchange Server                                          |
| 1067                                     | TCP      | Installation Bootstrap Service           | Installation Bootstrap protocol server                   |
| 1068                                     | TCP      | Installation Bootstrap Service           | Installation Bootstrap protocol client                   |
| 1270                                     | TCP      | MOM-Encrypted                            | Microsoft Operations Manager 2000                        |
| 1433                                     | TCP      | SQL over TCP                             | Microsoft SQL Server                                     |
| 1433                                     | TCP      | SQL over TCP                             | MSSQL$UDDI                                               |
| 1434                                     | UDP      | SQL Probe                                | Microsoft SQL Server                                     |
| 1434                                     | UDP      | SQL Probe                                | MSSQL$UDDI                                               |
| 1645                                     | UDP      | Legacy RADIUS                            | Internet Authentication Service                          |
| 1646                                     | UDP      | Legacy RADIUS                            | Internet Authentication Service                          |
| 1701                                     | UDP      | L2TP                                     | Routing and Remote Access                                |
| 1723                                     | TCP      | PPTP                                     | Routing and Remote Access                                |
| 1755                                     | TCP      | MMS                                      | Windows Media Services                                   |
| 1755                                     | UDP      | MMS                                      | Windows Media Services                                   |
| 1801                                     | TCP      | MSMQ                                     | Message Queuing                                          |
| 1801                                     | UDP      | MSMQ                                     | Message Queuing                                          |
| 1812                                     | UDP      | RADIUS Authentication                    | Internet Authentication Service                          |
| 1813                                     | UDP      | RADIUS Accounting                        | Internet Authentication Service                          |
| 1900                                     | UDP      | SSDP                                     | SSDP Discovery Service                                   |
| 2101                                     | TCP      | MSMQ-DCs                                 | Message Queuing                                          |
| 2103                                     | TCP      | MSMQ-RPC                                 | Message Queuing                                          |
| 2105                                     | TCP      | MSMQ-RPC                                 | Message Queuing                                          |
| 2107                                     | TCP      | MSMQ-Mgmt                                | Message Queuing                                          |
| 2393                                     | TCP      | OLAP Services 7.0                        | SQL Server: Downlevel OLAP Client Support                |
| 2394                                     | TCP      | OLAP Services 7.0                        | SQL Server: Downlevel OLAP Client Support                |
| 2460                                     | UDP      | MS Theater                               | Windows Media Services                                   |
| 2535                                     | UDP      | MADCAP                                   | DHCP Server                                              |
| 2701                                     | TCP      | SMS Remote Control (control)             | SMS Remote Control Agent                                 |
| 2701                                     | UDP      | SMS Remote Control (control)             | SMS Remote Control Agent                                 |
| 2702                                     | TCP      | SMS Remote Control (data)                | SMS Remote Control Agent                                 |
| 2702                                     | UDP      | SMS Remote Control (data)                | SMS Remote Control Agent                                 |
| 2703                                     | TCP      | SMS Remote Chat                          | SMS Remote Control Agent                                 |
| 2703                                     | UPD      | SMS Remote Chat                          | SMS Remote Control Agent                                 |
| 2704                                     | TCP      | SMS Remote File Transfer                 | SMS Remote Control Agent                                 |
| 2704                                     | UDP      | SMS Remote File Transfer                 | SMS Remote Control Agent                                 |
| 2725                                     | TCP      | SQL Analysis Services                    | SQL Server Analysis Services                             |
| 2869                                     | TCP      | UPNP                                     | UPnP Device Host                                         |
| 2869                                     | TCP      | SSDP event notification                  | SSDP Discovery Service                                   |
| 3268                                     | TCP      | Global Catalog                           | Local Security Authority                                 |
| 3269                                     | TCP      | Global Catalog                           | Local Security Authority                                 |
| 3343                                     | UDP      | Cluster Services                         | Cluster Service                                          |
| 3389                                     | TCP      | RDS                                      | RDS                                                      |
| 3389                                     | UDP      | RDS                                      | RDS                                                      |
| 3527                                     | UDP      | MSMQ-Ping                                | Message Queuing                                          |
| 4011                                     | UDP      | BINL                                     | Remote Installation                                      |
| 4500                                     | UDP      | NAT-T                                    | Local Security Authority                                 |
| 5000                                     | TCP      | SSDP legacy event notification           | SSDP Discovery Service                                   |
| 5004                                     | UDP      | RTP                                      | Windows Media Services                                   |
| 5005                                     | UDP      | RTCP                                     | Windows Media Services                                   |
| 5722                                     | TCP      | RPC                                      | Distributed File System Replication                      |
| 6001                                     | TCP      | Information Store                        | Exchange Server 2003                                     |
| 6002                                     | TCP      | Directory Referral                       | Exchange Server 2003                                     |
| 6004                                     | TCP      | DSProxy/NSPI                             | Exchange Server 2003                                     |
| 42424                                    | TCP      | ASP.NET Session State                    | ASP.NET State Service                                    |
| 51515                                    | TCP      | MOM-Clear                                | Microsoft Operations Manager 2000                        |
| 5985                                     | TCP      | HTTP                                     | WinRM 2.0                                                |
| 5986                                     | TCP      | HTTPS                                    | WinRM 2.0                                                |
| 1024-65535                               | TCP      | RPC                                      | Randomly allocated high TCP ports                        |
| 135                                      | TCP      | WMI                                      | Hyper-V service                                          |
| random port number between 49152 - 65535 | TCP      | Randomly allocated high TCP ports        | Hyper-V service                                          |
| 80                                       | TCP      | Kerberos Authentication (HTTP)           | Hyper-V service                                          |
| 443                                      | TCP      | Certificate-based Authentication (HTTPS) | Hyper-V service                                          |
| 6600                                     | TCP      | Live Migration                           | Hyper-V Live Migration                                   |
| 445                                      | TCP      | SMB                                      | Hyper-V Live Migration                                   |
| 3343                                     | UDP      | Cluster Service Traffic                  | Hyper-V Live Migration                                   |