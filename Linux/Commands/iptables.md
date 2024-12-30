
drop all tcp traffic from 10.10.10.10
`iptables -A INPUT -p tcp -s 10.10.10.10 -j DROP`

list rules
`iptables -L`

clear rules
`iptables -F`