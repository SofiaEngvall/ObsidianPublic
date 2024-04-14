
ttl windows = 127...
ttl linux.. = 62...

```sh
for i in $(seq 254); do ping 192.168.0.${i} -c1 -W1 & done | grep from
```

```sh
local: tcpdump -i any "icmp"
payload: ping -c 3
```



