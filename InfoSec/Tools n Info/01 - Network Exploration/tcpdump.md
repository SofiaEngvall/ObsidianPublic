
command line wireshark

https://www.tcpdump.org/

https://www.tcpdump.org/manpages/tcpdump.1.html


### Basic options

`-i any` listen to all interfaces
`-i eth0` set interface to listen to

`-w FILE.pcap` file to write to

`-r FILE.pcap` file to read from

`-c COUNT` max amount of packets to capture
or just abort it with `Ctrl+C`

`-n` don't do DNS lookup
`-n` don't "translate" port numbers to common use (like 80 to http..)

`-v` `-vv` `-vvv` verbosity level

### Filtering

`host IP/HOSTNAME` capture only traffic to and from a specific host
`src host IP/HOSTNAME` capture only when the host is the source
`dst host IP/HOSTNAME` capture only when the host is the destination

`port PORT` capture only traffic to and from a specific port
`src port PORT` capture only when the port is the source
`dst port PORT` capture only when the port is the destination

`ip`, `ip6`, `udp`, `tcp`, `icmp`, `arp`, `ether` limit to a protocol
	`sudo tcpdump -i ens5 icmp -n`

Logical operators `and`, `or` and `not` can be used:
	`tcpdump host 1.1.1.1 and tcp`
	`tcpdump udp or icmp`
	`tcpdump not tcp`

### Advanced filtering

`greater LENGTH` filters packets that have a length greater than or equal to the specified length
`less LENGTH` filters packets that have a length less than or equal to the specified length

`man pcap-filter` for more filter info

Binary operators `&`, `|`, and `!` can be used in advanced filters

##### Looking at TCP flags

`protocol[offset:size]` offset starts at 0
	`ether[0] & 1 != 0` the first byte in the ethernet header will show multicast address
	`ip[0] & 0xf != 5` the first byte in the ip packet header will show if it has options
	
`tcp[tcpflags]` there are constants for the tcp flags field 
- `tcp-syn` TCP SYN (Synchronize)
- `tcp-ack` TCP ACK (Acknowledge)
- `tcp-fin` TCP FIN (Finish)
- `tcp-rst` TCP RST (Reset)
- `tcp-push` TCP Push

Capture TCP packets with **only** the SYN (Synchronize) flag set
`"tcp[tcpflags] == tcp-syn"`

Capture TCP packets with **at least** the SYN (Synchronize) flag set
`"tcp[tcpflags] & tcp-syn != 0"`

Capture TCP packets with **at least** the SYN (Synchronize) **or** ACK (Acknowledge) flags set
`"tcp[tcpflags] & (tcp-syn|tcp-ack) != 0"`

### Displaying packet data

`-q` Quick output; print brief packet information
`-e` Print the link-level header, mac address
`-A` Show packet data in ASCII
`-xx` Show packet data in hex format
`-X` Show packet headers and data in hex and ASCII



### Getting specific data from pcap-files

How many packets come from 192.168.124.1? (using wc to count the n umber of lines)
`tcpdump -r traffic.pcap src host 192.168.124.1 -n | wc`

How many packets use icmp?
`tcpdump -r traffic.pcap icmp -n | wc`

Which ip asked for the mac of 192.168.124.137?
`tcpdump -r traffic.pcap arp -n |grep 192.168.124.137`

Show DNS traffic
`tcpdump -r traffic.pcap port 53 -n`

How many packets have only the TCP Reset (RST) flag set?
`tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" -n | wc`

What is the IP address of the host that sent packets larger than 15000 bytes?
`tcpdump -r traffic.pcap greater 15000 -n`

