
`traceroute <domainname>`

```sh
sofia@Main-i732:~$ traceroute -m 100 -q 10 fixitnow.se
traceroute to fixitnow.se (185.189.49.220), 100 hops max, 60 byte packets
1  Main-i732 (172.25.224.1)  1.222 ms  1.130 ms  1.102 ms  1.081 ms  1.057 ms  1.036 ms  1.015 ms  0.993 ms  1.091 ms  1.071 ms
2  192.168.0.1 (192.168.0.1)  0.940 ms  0.918 ms  0.898 ms  1.228 ms  1.204 ms  1.175 ms  1.108 ms  1.028 ms  1.094 ms  1.024 ms
3  * * * * * * * * * *
4  31-209-57-177.cust.bredband2.com (31.209.57.177)  3.246 ms  3.189 ms  3.518 ms  3.448 ms  3.186 ms  3.307 ms  1.880 ms  1.898 ms  1.993 ms1.820 ms
5  hu0000-sto-esb11-cr1.se.bredband2.net (82.209.171.222)  1.213 ms  1.192 ms  1.614 ms  1.692 ms  1.494 ms  1.422 ms  1.553 ms  1.514 ms  1.492 ms  1.326 ms
6  31-208-232-103.cust.bredband2.com (31.208.232.103)  0.824 ms  0.817 ms  0.833 ms  0.830 ms  0.896 ms  0.888 ms  0.737 ms  0.814 ms  0.889 ms  0.988 ms
7  netnod-ix-ge-a-sth-1500.he.net (194.68.123.187)
15.033 ms * * * * * * * * *
8  yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.381 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.284 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.369 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.337 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  12.358 ms  12.419 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.441 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.230)  2.716 ms yelles-ab.e0-3.switch1.sto2.he.net (184.104.204.246)  1.480 ms  1.424 ms
9  * * * * * * * * * *
10  * * * * * * * * * *
```
