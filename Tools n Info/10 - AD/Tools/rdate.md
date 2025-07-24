
`sudo rdate -n <ipmachine>`

### Help

```sh
┌──(fixit42㉿kali)-[~]
└─$ rdate   
Usage: rdate [-46acnpsv] [ -b sec ] [-o port] [ -t msec ] host
  -4: use IPv4 only
  -6: use IPv6 only
  -a: use adjtime instead of instant change
  -b num: use instant change if difference is greater than
          num seconds, or else use adjtime
  -c: correct leap second count
  -n: use SNTP instead of RFC868 time protocol
  -o num: override time port with num
  -p: just print, don't set
  -s: just set, don't print
  -u: use UDP instead of TCP as transport
  -t msec: does not set clock if network delay greater than msec
  -v: verbose output

```
