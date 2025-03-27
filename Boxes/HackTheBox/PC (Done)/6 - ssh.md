
```sh
┌──(kali㉿kali)-[~]
└─$ ssh sau@10.10.11.214
sau@10.10.11.214´s password: 
Last login: Thu Aug 31 17:03:43 2023 from 10.10.16.52
sau@pc:~$ ls -la
total 48
drwxr-xr-x 4 sau  sau  4096 Aug 31 10:41 .
drwxr-xr-x 3 root root 4096 Jan 11  2023 ..
-rw------- 1 sau  sau    48 Aug 31 06:44 .Xauthority
lrwxrwxrwx 1 root root    9 Jan 11  2023 .bash_history -> /dev/null
-rw-r--r-- 1 sau  sau   220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 sau  sau  3771 Feb 25  2020 .bashrc
drwx------ 2 sau  sau  4096 Jan 11  2023 .cache
drwxrwxr-x 3 sau  sau  4096 Aug 31 10:41 .local
-rw-r--r-- 1 sau  sau   807 Feb 25  2020 .profile
-rw------- 1 sau  sau  8930 Aug 31 08:47 .viminfo
-rw-r----- 1 root sau    33 Aug 31 04:50 user.txt
sau@pc:~$ cat user.txt
f794f938a1f93c9cc1d314c53a4b9a1a
```

```sh
sau@pc:~$ find / -perm -u=s -type f 2>/dev/null
/snap/snapd/17950/usr/lib/snapd/snap-confine
/snap/core20/1778/usr/bin/chfn
/snap/core20/1778/usr/bin/chsh
/snap/core20/1778/usr/bin/gpasswd
/snap/core20/1778/usr/bin/mount
/snap/core20/1778/usr/bin/newgrp
/snap/core20/1778/usr/bin/passwd
/snap/core20/1778/usr/bin/su
/snap/core20/1778/usr/bin/sudo
/snap/core20/1778/usr/bin/umount
/snap/core20/1778/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1778/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/at
/usr/bin/su
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/fusermount
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/umount
/usr/bin/gpasswd
```

```
sau@pc:~$ sudo -l
[sudo] password for sau: 
Sorry, user sau may not run sudo on localhost.
```

```sh
sau@pc:/snap/bin$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.2 168144 11404 ?        Ss   04:50   0:02 /sbin/init
root           2  0.0  0.0      0     0 ?        S    04:50   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   04:50   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   04:50   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   04:50   0:00 [kworker/0:0H-kblockd]
root           8  0.0  0.0      0     0 ?        I<   04:50   0:00 [mm_percpu_wq]
root           9  0.0  0.0      0     0 ?        S    04:50   0:00 [ksoftirqd/0]
root          10  0.0  0.0      0     0 ?        I    04:50   0:20 [rcu_sched]
root          11  0.0  0.0      0     0 ?        S    04:50   0:00 [migration/0]
root          12  0.0  0.0      0     0 ?        S    04:50   0:00 [idle_inject/0]
root          14  0.0  0.0      0     0 ?        S    04:50   0:00 [cpuhp/0]
root          15  0.0  0.0      0     0 ?        S    04:50   0:00 [cpuhp/1]
root          16  0.0  0.0      0     0 ?        S    04:50   0:00 [idle_inject/1]
root          17  0.0  0.0      0     0 ?        S    04:50   0:00 [migration/1]
root          18  0.0  0.0      0     0 ?        S    04:50   0:00 [ksoftirqd/1]
root          20  0.0  0.0      0     0 ?        I<   04:50   0:00 [kworker/1:0H-kblockd]
root          21  0.0  0.0      0     0 ?        S    04:50   0:00 [kdevtmpfs]
root          22  0.0  0.0      0     0 ?        I<   04:50   0:00 [netns]
root          23  0.0  0.0      0     0 ?        S    04:50   0:00 [rcu_tasks_kthre]
root          24  0.0  0.0      0     0 ?        S    04:50   0:00 [kauditd]
root          26  0.0  0.0      0     0 ?        S    04:50   0:00 [khungtaskd]
root          27  0.0  0.0      0     0 ?        S    04:50   0:00 [oom_reaper]
root          28  0.0  0.0      0     0 ?        I<   04:50   0:00 [writeback]
root          29  0.0  0.0      0     0 ?        S    04:50   0:00 [kcompactd0]
root          30  0.0  0.0      0     0 ?        SN   04:50   0:00 [ksmd]
root          31  0.0  0.0      0     0 ?        SN   04:50   0:00 [khugepaged]
root          78  0.0  0.0      0     0 ?        I<   04:50   0:00 [kintegrityd]
root          79  0.0  0.0      0     0 ?        I<   04:50   0:00 [kblockd]
root          80  0.0  0.0      0     0 ?        I<   04:50   0:00 [blkcg_punt_bio]
root          81  0.0  0.0      0     0 ?        I<   04:50   0:00 [tpm_dev_wq]
root          82  0.0  0.0      0     0 ?        I<   04:50   0:00 [ata_sff]
root          83  0.0  0.0      0     0 ?        I<   04:50   0:00 [md]
root          84  0.0  0.0      0     0 ?        I<   04:50   0:00 [edac-poller]
root          85  0.0  0.0      0     0 ?        I<   04:50   0:00 [devfreq_wq]
root          86  0.0  0.0      0     0 ?        S    04:50   0:00 [watchdogd]
root          89  0.0  0.0      0     0 ?        S    04:50   0:00 [kswapd0]
root          90  0.0  0.0      0     0 ?        S    04:50   0:00 [ecryptfs-kthrea]
root          92  0.0  0.0      0     0 ?        I<   04:50   0:00 [kthrotld]
root          93  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/24-pciehp]
root          94  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/25-pciehp]
root          95  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/26-pciehp]
root          96  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/27-pciehp]
root          97  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/28-pciehp]
root          98  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/29-pciehp]
root          99  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/30-pciehp]
root         100  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/31-pciehp]
root         101  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/32-pciehp]
root         102  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/33-pciehp]
root         103  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/34-pciehp]
root         104  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/35-pciehp]
root         105  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/36-pciehp]
root         106  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/37-pciehp]
root         107  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/38-pciehp]
root         108  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/39-pciehp]
root         109  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/40-pciehp]
root         110  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/41-pciehp]
root         111  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/42-pciehp]
root         112  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/43-pciehp]
root         113  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/44-pciehp]
root         114  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/45-pciehp]
root         115  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/46-pciehp]
root         116  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/47-pciehp]
root         117  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/48-pciehp]
root         118  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/49-pciehp]
root         119  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/50-pciehp]
root         120  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/51-pciehp]
root         121  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/52-pciehp]
root         122  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/53-pciehp]
root         123  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/54-pciehp]
root         124  0.0  0.0      0     0 ?        S    04:50   0:00 [irq/55-pciehp]
root         125  0.0  0.0      0     0 ?        I<   04:50   0:00 [acpi_thermal_pm]
root         126  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_0]
root         127  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_0]
root         128  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_1]
root         129  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_1]
root         131  0.0  0.0      0     0 ?        I<   04:50   0:00 [vfio-irqfd-clea]
root         132  0.0  0.0      0     0 ?        I<   04:50   0:00 [ipv6_addrconf]
root         142  0.0  0.0      0     0 ?        I<   04:50   0:00 [kstrp]
root         145  0.0  0.0      0     0 ?        I<   04:50   0:00 [kworker/u257:0]
root         158  0.0  0.0      0     0 ?        I<   04:50   0:00 [charger_manager]
root         202  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_2]
root         203  0.0  0.0      0     0 ?        I<   04:50   0:00 [mpt_poll_0]
root         204  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_2]
root         205  0.0  0.0      0     0 ?        I<   04:50   0:00 [mpt/0]
root         206  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_3]
root         207  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_3]
root         208  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_4]
root         209  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_4]
root         210  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_5]
root         211  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_5]
root         212  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_6]
root         213  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_6]
root         214  0.0  0.0      0     0 ?        I<   04:50   0:00 [cryptd]
root         215  0.0  0.0      0     0 ?        S    04:50   0:06 [irq/16-vmwgfx]
root         216  0.0  0.0      0     0 ?        I<   04:50   0:00 [ttm_swap]
root         217  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_7]
root         218  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_7]
root         219  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_8]
root         221  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_8]
root         230  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_9]
root         232  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_9]
root         233  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_10]
root         234  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_10]
root         235  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_11]
root         236  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_11]
root         237  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_12]
root         238  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_12]
root         239  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_13]
root         240  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_13]
root         241  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_14]
root         242  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_14]
root         244  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_15]
root         262  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_15]
root         263  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_16]
root         264  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_16]
root         265  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_17]
root         266  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_17]
root         267  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_18]
root         271  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_18]
root         274  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_19]
root         275  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_19]
root         276  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_20]
root         277  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_20]
root         278  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_21]
root         279  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_21]
root         280  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_22]
root         281  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_22]
root         282  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_23]
root         283  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_23]
root         284  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_24]
root         285  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_24]
root         286  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_25]
root         287  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_25]
root         288  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_26]
root         289  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_26]
root         290  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_27]
root         291  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_27]
root         292  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_28]
root         293  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_28]
root         294  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_29]
root         295  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_29]
root         296  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_30]
root         297  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_30]
root         298  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_31]
root         299  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_31]
root         328  0.0  0.0      0     0 ?        S    04:50   0:00 [scsi_eh_32]
root         329  0.0  0.0      0     0 ?        I<   04:50   0:00 [scsi_tmf_32]
root         330  0.0  0.0      0     0 ?        I<   04:50   0:00 [kworker/0:1H-kblockd]
root         359  0.0  0.0      0     0 ?        I<   04:50   0:00 [raid5wq]
root         402  0.0  0.0      0     0 ?        I<   04:50   0:01 [kworker/1:1H-kblockd]
root         403  0.0  0.0      0     0 ?        S    04:50   0:01 [jbd2/sda2-8]
root         404  0.0  0.0      0     0 ?        I<   04:50   0:00 [ext4-rsv-conver]
root         463  0.0  2.9 192264 119432 ?       S<s  04:50   0:09 /lib/systemd/systemd-journald
root         489  0.0  0.0   2488   508 ?        S    04:50   0:00 bpfilter_umh
root         506  0.0  0.1  20576  6328 ?        Ss   04:50   0:00 /lib/systemd/systemd-udevd
systemd+     518  0.0  0.1  19080  7556 ?        Ss   04:50   0:00 /lib/systemd/systemd-networkd
root         677  0.0  0.0      0     0 ?        I<   04:50   0:00 [kaluad]
root         678  0.0  0.0      0     0 ?        I<   04:50   0:00 [kmpath_rdacd]
root         679  0.0  0.0      0     0 ?        I<   04:50   0:00 [kmpathd]
root         680  0.0  0.0      0     0 ?        I<   04:50   0:00 [kmpath_handlerd]
root         681  0.0  0.4 280136 17948 ?        SLsl 04:50   0:06 /sbin/multipathd -d -s
root         691  0.0  0.0      0     0 ?        S<   04:50   0:00 [loop0]
root         692  0.0  0.0      0     0 ?        S<   04:50   0:00 [loop1]
root         693  0.0  0.0      0     0 ?        S<   04:50   0:00 [loop2]
root         711  0.0  0.0  11356  1556 ?        S<sl 04:50   0:00 /sbin/auditd
root         731  0.0  0.2  49296 10860 ?        Ss   04:50   0:00 /usr/bin/VGAuthService
root         734  0.1  0.2 313228  8320 ?        Ssl  04:50   1:05 /usr/bin/vmtoolsd
root         760  0.0  0.1  99900  6016 ?        Ssl  04:50   0:00 /sbin/dhclient -1 -4 -v -i -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclien
root         779  0.0  0.0      0     0 ?        S    04:50   0:00 [audit_prune_tre]
root         823  0.0  0.2 241052  9220 ?        Ssl  04:50   0:03 /usr/lib/accountsservice/accounts-daemon
message+     824  0.0  0.1   7576  4736 ?        Ss   04:50   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         832  0.0  0.0  81956  3768 ?        Ssl  04:50   0:02 /usr/sbin/irqbalance --foreground
root         834  0.0  0.4  29876 18188 ?        Ss   04:50   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         835  0.0  0.2 236440  9084 ?        Ssl  04:50   0:00 /usr/lib/policykit-1/polkitd --no-debug
syslog       836  0.0  0.1 224344  5588 ?        Ssl  04:50   0:02 /usr/sbin/rsyslogd -n -iNONE
root         837  0.0  1.0 875264 42328 ?        Ssl  04:50   0:04 /usr/lib/snapd/snapd
root         838  0.0  0.1  17364  7732 ?        Ss   04:50   0:00 /lib/systemd/systemd-logind
root         840  0.0  0.3 395492 13700 ?        Ssl  04:50   0:00 /usr/lib/udisks2/udisksd
root         872  0.0  0.3 318820 13564 ?        Ssl  04:50   0:00 /usr/sbin/ModemManager
systemd+    1007  0.0  0.3  24448 13008 ?        Ss   04:50   0:00 /lib/systemd/systemd-resolved
root        1058  0.1  0.7 634884 31912 ?        Ssl  04:50   0:57 /usr/bin/python3 /opt/app/app.py
root        1063  0.0  1.6 1221140 65368 ?       Ssl  04:50   0:35 /usr/bin/python3 /usr/local/bin/pyload
root        1081  0.0  0.0   8540  3084 ?        Ss   04:50   0:00 /usr/sbin/cron -f
daemon      1083  0.0  0.0   3796  2268 ?        Ss   04:50   0:00 /usr/sbin/atd -f
root        1093  0.0  0.1  12180  7400 ?        Ss   04:50   0:01 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
root        1098  0.0  0.0   5828  1844 tty1     Ss+  04:50   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root        3888  0.0  0.0      0     0 ?        I    11:12   0:15 [kworker/1:1-events]
root        5344  0.0  0.0      0     0 ?        I    18:33   0:01 [kworker/0:3-cgroup_destroy]
root        5374  0.0  0.0      0     0 ?        I    19:14   0:01 [kworker/0:0-events]
root        5475  0.0  0.2  13956  9168 ?        Ss   20:02   0:00 sshd: sau [priv]
sau         5493  0.0  0.2  19100  9440 ?        Ss   20:03   0:00 /lib/systemd/systemd --user
sau         5495  0.0  0.0 169500  3460 ?        S    20:03   0:00 (sd-pam)
root        5503  0.0  0.0      0     0 ?        I    20:03   0:00 [kworker/1:2]
sau         5597  0.0  0.1  13956  5972 ?        S    20:03   0:00 sshd: sau@pts/0
sau         5598  0.0  0.1   9988  5024 pts/0    Ss   20:03   0:00 -bash
root        5650  0.0  0.0      0     0 ?        I    20:24   0:00 [kworker/u256:1-events_unbound]
root        5673  0.0  0.0      0     0 ?        I    20:30   0:00 [kworker/u256:2-events_unbound]
root        5696  0.0  0.0      0     0 ?        I    20:40   0:00 [kworker/u256:0-events_unbound]
sau         5699  0.0  0.0  10612  3348 pts/0    R+   20:41   0:00 ps aux
```

What are these:
root        1058  0.1  0.7 634884 31912 ?        Ssl  04:50   0:57 /usr/bin/python3 /opt/app/app.py
root        1063  0.0  1.6 1221140 65368 ?       Ssl  04:50   0:35 /usr/bin/python3 /usr/local/bin/pyload

```sh
sau@pc:/usr/local/bin$ pyload --version
pyLoad 0.5.0
```

googling "pyload exploit", found cve

