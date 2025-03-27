
port 53 dns open

Testing normal dns checkup:

```sh
┌──(kali㉿kali)-[~]
└─$ host -t ns ironcorp.me
ironcorp.me name server ns1.abovedomains.com.
ironcorp.me name server ns2.abovedomains.com.

┌──(kali㉿kali)-[~]
└─$ host -l ironcorp.me ns1.abovedomain.com
;; Connection to 103.224.212.246#53(103.224.212.246) for ironcorp.me failed: connection refused.
;; no servers could be reached

;; Connection to 103.224.212.246#53(103.224.212.246) for ironcorp.me failed: connection refused.
;; no servers could be reached

```

```sh
┌──(kali㉿kali)-[~]
└─$ dig ironcorp.me -t ns

; <<>> DiG 9.19.21-1-Debian <<>> ironcorp.me -t ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58929
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0x0005, udp: 512
;; QUESTION SECTION:
;ironcorp.me.                   IN      NS

;; ANSWER SECTION:
ironcorp.me.            5       IN      NS      ns2.abovedomains.com.
ironcorp.me.            5       IN      NS      ns1.abovedomains.com.

;; Query time: 191 msec
;; SERVER: 192.168.233.2#53(192.168.233.2) (UDP)
;; WHEN: Fri Mar 29 15:09:59 CET 2024
;; MSG SIZE  rcvd: 92
```

```sh
┌──(kali㉿kali)-[~]
└─$ dig axfr ironcorp.me @ns1.abovedomins.com
dig: couldn´t get address for 'ns1.abovedomins.com': not found
```

Commands not really working. Lab environment!

Going for the machine ip instead:

```sh
┌──(kali㉿kali)-[~]
└─$ dig axfr ironcorp.me @10.10.112.197      

; <<>> DiG 9.19.21-1-Debian <<>> axfr ironcorp.me @10.10.112.197
;; global options: +cmd
ironcorp.me.            3600    IN      SOA     win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
ironcorp.me.            3600    IN      NS      win-8vmbkf3g815.
admin.ironcorp.me.      3600    IN      A       127.0.0.1
internal.ironcorp.me.   3600    IN      A       127.0.0.1
ironcorp.me.            3600    IN      SOA     win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
;; Query time: 479 msec
;; SERVER: 10.10.112.197#53(10.10.112.197) (TCP)
;; WHEN: Fri Mar 29 16:33:47 CET 2024
;; XFR size: 5 records (messages 1, bytes 238)

```

SOA   start of authority record
	important information about a domain or zone such as the email address of the administrator, when the domain was last updated, and how long the server should wait between refreshes
        3  ;Serial
        900        ;Refresh
        600        ;Retry
        86400     ;Expire
        3600        ;Negative response caching TTL


There if is! We have three subdomains/addresses to test:

admin.ironcorp.me.      3600    IN      A       127.0.0.1
internal.ironcorp.me.   3600    IN      A       127.0.0.1

win-8vmbkf3g815.ironcorp.me ns

added to .hosts



Also tried nslookup for learning but the ls command is not implemented. Might go back and try more here later to learn. Why not just do domain.com as with the type ns?

```sh
┌──(kali㉿kali)-[~]
└─$ nslookup                                 
> set type=ns
> ironcorp.me
Server:         192.168.233.2
Address:        192.168.233.2#53

Non-authoritative answer:
ironcorp.me     nameserver = ns1.abovedomains.com.
ironcorp.me     nameserver = ns2.abovedomains.com.

Authoritative answers can be found from:
> server 10.10.112.197
Default server: 10.10.112.197
Address: 10.10.112.197#53
> set type=any
> ls -d ironcorp.me
The 'ls' command is not implemented.
> help
The 'help' command is not yet implemented.
> 
```