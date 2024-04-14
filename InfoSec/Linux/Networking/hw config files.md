
Interface / Adapter settings - DHCP settings
`nano /etc/network/interfaces`

```
auto eth0
iface eth0 inet static
address [ip address]
netmask [netmask]
gateway [default gateway]
```
Take down and then up the reconfigured interfaces for updates to apply.

DNS settings
`nano /etc/resolv.conf`

