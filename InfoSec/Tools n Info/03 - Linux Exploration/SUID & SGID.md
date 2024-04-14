
### normal SUID

/bin/su
/usr/bin/sudo

/bin/ping
/bin/mount
/bin/umount
/bin/fusermount

/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/newuidmap
/usr/bin/newgidmap
/usr/bin/newgrp

/usr/lib/openssh/ssh-keysign

/usr/bin/at     # unless it's RTru64 linux, in which case CVE-2002-1614


### normal SGID

/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/expiry
/usr/bin/mlocate
/usr/bin/wall
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/at
/usr/lib/x86_64-linux-gnu/utempter/utempter
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd

