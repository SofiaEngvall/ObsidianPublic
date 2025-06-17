
```sh
for ip in {1..254} ;do (ping -c 1 10.10.10.$ip | grep "bytes from") done     
64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=0.418 ms
64 bytes from 10.10.10.3: icmp_seq=1 ttl=64 time=0.011 ms
64 bytes from 10.10.10.228: icmp_seq=1 ttl=128 time=10.6 ms
```

nmap?

