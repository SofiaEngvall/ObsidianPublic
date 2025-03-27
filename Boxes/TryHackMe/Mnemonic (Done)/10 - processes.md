
```sh
james@mnemonic:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.1  0.8 159760  8920 ?        Ss   07:10   0:08 /sbin/init maybe-ubiquity
root         2  0.0  0.0      0     0 ?        S    07:10   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   07:10   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<   07:10   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    07:10   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    07:10   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    07:10   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    07:10   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    07:10   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    07:10   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    07:10   0:00 [kdevtmpfs]
root        14  0.0  0.0      0     0 ?        I<   07:10   0:00 [netns]
root        15  0.0  0.0      0     0 ?        S    07:10   0:00 [rcu_tasks_kthre]
root        16  0.0  0.0      0     0 ?        S    07:10   0:00 [kauditd]
root        17  0.0  0.0      0     0 ?        S    07:10   0:00 [xenbus]
root        18  0.0  0.0      0     0 ?        S    07:10   0:00 [xenwatch]
root        19  0.0  0.0      0     0 ?        I    07:10   0:00 [kworker/0:1]
root        20  0.0  0.0      0     0 ?        S    07:10   0:00 [khungtaskd]
root        21  0.0  0.0      0     0 ?        S    07:10   0:00 [oom_reaper]
root        22  0.0  0.0      0     0 ?        I<   07:10   0:00 [writeback]
root        23  0.0  0.0      0     0 ?        S    07:10   0:00 [kcompactd0]
root        24  0.0  0.0      0     0 ?        SN   07:10   0:00 [ksmd]
root        25  0.0  0.0      0     0 ?        SN   07:10   0:00 [khugepaged]
root        26  0.0  0.0      0     0 ?        I<   07:10   0:00 [crypto]
root        27  0.0  0.0      0     0 ?        I<   07:10   0:00 [kintegrityd]
root        28  0.0  0.0      0     0 ?        I<   07:10   0:00 [kblockd]
root        29  0.0  0.0      0     0 ?        I<   07:10   0:00 [ata_sff]
root        30  0.0  0.0      0     0 ?        I<   07:10   0:00 [md]
root        31  0.0  0.0      0     0 ?        I<   07:10   0:00 [edac-poller]
root        32  0.0  0.0      0     0 ?        I<   07:10   0:00 [devfreq_wq]
root        33  0.0  0.0      0     0 ?        I<   07:10   0:00 [watchdogd]
root        36  0.0  0.0      0     0 ?        S    07:10   0:00 [kswapd0]
root        37  0.0  0.0      0     0 ?        I<   07:10   0:00 [kworker/u31:0]
root        38  0.0  0.0      0     0 ?        S    07:10   0:00 [ecryptfs-kthrea]
root        80  0.0  0.0      0     0 ?        I<   07:10   0:00 [kthrotld]
root        81  0.0  0.0      0     0 ?        I<   07:10   0:00 [acpi_thermal_pm]
root        82  0.0  0.0      0     0 ?        S    07:10   0:00 [scsi_eh_0]
root        83  0.0  0.0      0     0 ?        I<   07:10   0:00 [scsi_tmf_0]
root        84  0.0  0.0      0     0 ?        S    07:10   0:00 [scsi_eh_1]
root        85  0.0  0.0      0     0 ?        I<   07:10   0:00 [scsi_tmf_1]
root        91  0.0  0.0      0     0 ?        I<   07:10   0:00 [ipv6_addrconf]
root       100  0.0  0.0      0     0 ?        I<   07:10   0:00 [kstrp]
root       117  0.0  0.0      0     0 ?        I<   07:10   0:00 [charger_manager]
root       181  0.0  0.0      0     0 ?        I<   07:10   0:00 [ttm_swap]
root       269  0.0  0.0      0     0 ?        I    07:11   0:00 [kworker/0:3]
root       277  0.0  0.0      0     0 ?        I<   07:11   0:00 [raid5wq]
root       330  0.0  0.0      0     0 ?        S    07:11   0:00 [jbd2/xvda2-8]
root       331  0.0  0.0      0     0 ?        I<   07:11   0:00 [ext4-rsv-conver]
root       365  0.0  0.0      0     0 ?        I<   07:11   0:00 [kworker/0:1H]
root       416  0.0  1.7 127660 17216 ?        S<s  07:11   0:01 /lib/systemd/systemd-journald
root       420  0.0  0.0      0     0 ?        I<   07:11   0:00 [iscsi_eh]
root       423  0.0  0.0      0     0 ?        I<   07:11   0:00 [ib-comp-wq]
root       424  0.0  0.0      0     0 ?        I<   07:11   0:00 [ib-comp-unb-wq]
root       425  0.0  0.0      0     0 ?        I<   07:11   0:00 [ib_mcast]
root       426  0.0  0.1  97708  1900 ?        Ss   07:11   0:00 /sbin/lvmetad -f
root       427  0.0  0.0      0     0 ?        I<   07:11   0:00 [ib_nl_sa_wq]
root       429  0.0  0.0      0     0 ?        I<   07:11   0:00 [rdma_cm]
root       430  0.0  0.5  46532  5496 ?        Ss   07:11   0:03 /lib/systemd/systemd-udevd
root       449  0.0  0.0      0     0 ?        S<   07:11   0:00 [loop0]
root       458  0.0  0.0      0     0 ?        S<   07:11   0:00 [loop1]
systemd+   680  0.0  0.5  80068  5352 ?        Ss   07:11   0:00 /lib/systemd/systemd-networkd
systemd+   694  0.0  0.5  70656  5152 ?        Ss   07:11   0:00 /lib/systemd/systemd-resolved
root       793  0.0  0.6 286332  6964 ?        Ssl  07:11   0:00 /usr/lib/accountsservice/accounts-daemon
root       795  0.0  1.6 169100 17080 ?        Ssl  07:11   0:01 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-
daemon     799  0.0  0.2  28332  2408 ?        Ss   07:11   0:00 /usr/sbin/atd -f
syslog     802  0.0  0.4 263040  4564 ?        Ssl  07:11   0:00 /usr/sbin/rsyslogd -n
message+   803  0.0  0.4  50100  4320 ?        Ss   07:11   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --
root       830  0.0  0.3  30028  3240 ?        Ss   07:11   0:00 /usr/sbin/cron -f
root       838  0.0  0.6  70592  6192 ?        Ss   07:11   0:00 /lib/systemd/systemd-logind
root       839  0.0  0.1  95540  1612 ?        Ssl  07:11   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       840  0.0  2.5 635612 26064 ?        Ssl  07:11   0:06 /usr/lib/snapd/snapd
root       841  0.0  0.2  29148  2944 ?        Ss   07:11   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root       852  0.0  0.2  14664  2412 ttyS0    Ss+  07:11   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0
root       853  0.0  0.7 291456  7328 ?        Ssl  07:11   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       855  0.0  0.3  57500  3260 ?        S    07:11   0:00 /usr/sbin/CRON -f
root       856  0.0  0.1  14888  1936 tty1     Ss+  07:11   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root       867  0.0  0.0   4628   832 ?        Ss   07:11   0:00 /bin/sh -c /usr/bin/sudo /usr/bin/python3 /bin/IPS.py
root       874  0.0  0.4  59924  4100 ?        S    07:11   0:00 /usr/bin/sudo /usr/bin/python3 /bin/IPS.py
root       875  0.0  0.5  72300  5620 ?        Ss   07:11   0:00 /usr/sbin/sshd -D
root       880  0.0  1.0  29464 10556 ?        S    07:11   0:00 /usr/bin/python3 /bin/IPS.py
root       896  0.0  2.0 185944 20192 ?        Ssl  07:11   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-u
root       905  0.0  0.4  73960  4604 ?        Ss   07:11   0:00 /usr/sbin/apache2 -k start
www-data   907  0.0  0.4 826256  4648 ?        Sl   07:11   0:00 /usr/sbin/apache2 -k start
www-data   908  0.0  0.4 826256  4648 ?        Sl   07:11   0:00 /usr/sbin/apache2 -k start
root      1985  0.0  0.0      0     0 ?        I    09:07   0:00 [kworker/u30:1]
root      2009  0.0  0.0      0     0 ?        I    09:12   0:00 [kworker/u30:2]
root      2033  0.0  0.0      0     0 ?        I    09:18   0:00 [kworker/u30:0]
root      2197  0.0  0.7 107988  7204 ?        Ss   09:23   0:00 sshd: james [priv]
root      2199  0.0  0.0      0     0 ?        Z    09:23   0:00 [sh] <defunct>
james     2201  0.1  0.7  76664  7624 ?        Ss   09:23   0:00 /lib/systemd/systemd --user
james     2202  0.0  0.2 193744  2420 ?        S    09:23   0:00 (sd-pam)
james     2278  0.0  0.3 107988  3536 ?        S    09:23   0:00 sshd: james@pts/0
james     2279  0.3  0.4  21460  4964 pts/0    Ss   09:23   0:00 -rbash
james     2293  0.0  0.3  36076  3264 pts/0    R+   09:23   0:00 ps aux
```

