
#### host

`host -t ns domain.com`

-t specifies the query type

`host -l domain.com ns.domain.com`

-l lists all hosts in a domain, using AXFR

## dig

`dig domain.com -t ns`

`dig axfr domain.com @ns.domain.com`


### nslookup

<u>works on windows too</u>

`nslookup`
\>`set type=ns`
\>`domain.com`

\>`server ns.domain.com`
\>`set type=any`
\>`ls -d domain.com`

### dnsrecon

`dnsrecon -d domain.com -t axfr`


### DNS in Linux

saved in the file `/etc/resolv.conf`
`nameserver     192.168.1.100`


