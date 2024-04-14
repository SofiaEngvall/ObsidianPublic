
list info
`sudo ifconfig -a`

disable  network  adapter
`sudo ifconfig eth0 down`

enable network adapter
`sudo ifconfig eth0 up`

assign ip address
`$sudo ifconfig eth0 192.168.0.45`

set subnet mask
`sudo ifconfig eth0 192.168.0.45 netmask 255.255.255.0`

set default gateway
`sudo route add default gw 192.168.0.1`


