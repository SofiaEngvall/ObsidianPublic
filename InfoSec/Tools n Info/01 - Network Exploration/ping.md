
-c   count
-t   set ttl
-n   count on windows

ttl windows = 127...
ttl linux.. = 62...

```sh
for i in $(seq 254); do ping 192.168.0.${i} -c1 -W1 & done | grep from
```

```sh
local: tcpdump -i any "icmp"
payload: ping -c 3
```

### Help

```sh
┌──(kali㉿kali)-[~]
└─$ ping -h            

Usage
  ping [options] <destination>

Options:
  <destination>      DNS name or IP address
  -a                 use audible ping
  -A                 use adaptive ping
  -B                 sticky source address
  -c <count>         stop after <count> replies
  -C                 call connect() syscall on socket creation
  -D                 print timestamps
  -d                 use SO_DEBUG socket option
  -e <identifier>    define identifier for ping session, default is random for
                     SOCK_RAW and kernel defined for SOCK_DGRAM
                     Imply using SOCK_RAW (for IPv4 only for identifier 0)
  -f                 flood ping
  -h                 print help and exit
  -H                 force reverse DNS name resolution (useful for numeric
                     destinations or for -f), override -n
  -I <interface>     either interface name or address
  -i <interval>      seconds between sending each packet
  -L                 suppress loopback of multicast packets
  -l <preload>       send <preload> number of packages while waiting replies
  -m <mark>          tag the packets going out
  -M <pmtud opt>     define path MTU discovery, can be one of <do|dont|want|probe>
  -n                 no reverse DNS name resolution, override -H
  -O                 report outstanding replies
  -p <pattern>       contents of padding byte
  -q                 quiet output
  -Q <tclass>        use quality of service <tclass> bits
  -s <size>          use <size> as number of data bytes to be sent
  -S <size>          use <size> as SO_SNDBUF socket option value
  -t <ttl>           define time to live
  -U                 print user-to-user latency
  -v                 verbose output
  -V                 print version and exit
  -w <deadline>      reply wait <deadline> in seconds
  -W <timeout>       time to wait for response

IPv4 options:
  -4                 use IPv4
  -b                 allow pinging broadcast
  -R                 record route
  -T <timestamp>     define timestamp, can be one of <tsonly|tsandaddr|tsprespec>

IPv6 options:
  -6                 use IPv6
  -F <flowlabel>     define flow label, default is random
  -N <nodeinfo opt>  use IPv6 node info query, try <help> as argument

For more details see ping(8).
```
