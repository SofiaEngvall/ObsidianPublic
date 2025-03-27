
`drwxrwxrwt  14 root root      4096 May 19 23:52 tmp`
t instead of x means sticky bit

A sticky bit is a permission bit that only permits the owner and root user of a file/directory to modify, rename or delete it. When it's not set, any user can.

sticky-bit directories (restricted deletion flag - other users can't overwrite/delete files in the dir) = If it's not set you can overwrite other users files

Find files:
`find / -perm -1000 -type d 2>/dev/null`

Example:
a "real-life scenario" for a missing _sticky_ bit on a directory:

If you use an old-style text mail program like `mutt` and start `compose mail`, the following happens (roughly):

1. mutt creates a temporary file in `/var/tmp`
2. mutt starts your text editor with the name of the temporary file
3. mutt pauses
4. you compose your text and save it
5. you quit the text editor
6. mutt reads the contents of the temporary file and sends it.
7. mutt deletes the temporary file

An attacker may replace the file containing the text of your mail between step 4 and step 6. The reason is that the directory for temporary files has to be world writeable to be usable for all users. This attack works even if the file itself has access mode 0600, because having the right to create, replace or delete a file depends on the write permission bits on the directory.

The sticky bit prevents an attacker from deleting (system call `unlink`) or replacing (`rename`) a file of another user even if the the attacker has write permission on the directory.

_Modifying_ a file depends on the write access bits (and the ownership) of the file itself.
(https://security.stackexchange.com/questions/9115/can-you-describe-a-real-life-scenario-of-exploiting-sticky-bits)

#### Example output

kali full
```sh
┌──(kali㉿kali)-[~]
└─$ find / -perm -1000 -type d 2>/dev/null
/dev/shm
/dev/mqueue
/var/log/postgresql
/var/spool/cron/crontabs
/var/lib/php/sessions
/var/lib/samba/usershares
/var/tmp
/run/lock
/run/screen
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/VMwareDnD
/tmp/.XIM-unix
/tmp/.X11-unix
/sys/fs/bpf
```
