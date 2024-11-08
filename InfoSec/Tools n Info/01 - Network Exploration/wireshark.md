
Sample Captures:
https://wiki.wireshark.org/SampleCaptures


download file from ftp packets:
File -> Export Objects -> FTP-DATA, Save All



## Filters

`(tcp || udp) && (ip.src ==  8.8.8.8 || ip.dst == 8.8.8.8)`

`(tcp || udp) && (ip.src ==  10.0.0.3 || ip.dst == 10.0.0.3)`


To display packets with a specific source IP address:
`ip.src == 192.168.1.1`

To display packets with a specific destination IP address:
`ip.dst == 192.168.1.1`

To display packets with a specific source port:
`tcp.srcport == 80`

To display packets with a specific destination port:
`tcp.dstport == 443`
  
To display only HTTP (HyperText Transfer Protocol) traffic:
`http`
  
To display only DNS (Domain Name System) traffic:
`dns`
  
To display packets with a specific source MAC address:
`eth.src == 00:11:22:33:44:55`
  
To display packets with a specific destination MAC address:
`eth.dst == 00:11:22:33:44:55`

To combine filters using logical operators (AND, OR, NOT):
  
For example, to display only HTTP traffic from a specific IP address:
`ip.src == 192.168.1.1 && http`
  
To display all traffic except DNS:
`!(dns)`

[Wireshark Display Filter Reference](https://www.wireshark.org/docs/dfref/)

