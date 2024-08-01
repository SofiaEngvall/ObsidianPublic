```sh
┌──(kali㉿kali)-[~]
└─$ ping 10.10.11.249
PING 10.10.11.249 (10.10.11.249) 56(84) bytes of data.
64 bytes from 10.10.11.249: icmp_seq=1 ttl=127 time=33.2 ms
64 bytes from 10.10.11.249: icmp_seq=2 ttl=127 time=32.5 ms
64 bytes from 10.10.11.249: icmp_seq=3 ttl=127 time=35.2 ms
64 bytes from 10.10.11.249: icmp_seq=4 ttl=127 time=33.2 ms
64 bytes from 10.10.11.249: icmp_seq=5 ttl=127 time=32.4 ms
^C
--- 10.10.11.249 ping statistics ---
6 packets transmitted, 5 received, 16.6667% packet loss, time 5009ms
rtt min/avg/max/mdev = 32.430/33.288/35.166/0.995 ms
   
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.11.249
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-22 21:44 CET
Nmap scan report for 10.10.11.249
Host is up (0.036s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT      STATE SERVICE   VERSION
80/tcp    open  http      Microsoft IIS httpd 10.0
|_http-title: Did not follow redirect to http://crafty.htb
25565/tcp open  minecraft Minecraft 1.16.5 (Protocol: 127, Message: Crafty Server, Users: 1/100)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 151.60 seconds

┌──(kali㉿kali)-[~]
└─$ ls -la
total 1224
drwx------ 30 kali kali   4096 Feb 22 21:40  .
drwxr-xr-x  3 root root   4096 Sep 25 13:54  ..
drwx------  5 kali kali   4096 Sep 28 20:43  .BurpSuite
-rw-------  1 kali kali      0 Sep 25 13:57  .ICEauthority
-rw-------  1 kali kali     49 Feb 22 21:37  .Xauthority
-rw-r--r--  1 kali kali    220 Sep 25 13:54  .bash_logout
-rw-r--r--  1 kali kali   5551 Sep 25 13:54  .bashrc
-rw-r--r--  1 kali kali   3526 Sep 25 13:54  .bashrc.original
drwxr-xr-x 15 kali kali   4096 Feb  7 19:06  .cache
drwxr-xr-x  8 kali kali   4096 Nov 30 21:42  .cme
drwxr-xr-x 19 kali kali   4096 Feb 11 01:38  .config
-rw-r--r--  1 kali kali     35 Oct 23 20:48  .dmrc
-rw-r--r--  1 kali kali  11759 Sep 25 13:54  .face
lrwxrwxrwx  1 kali kali      5 Sep 25 13:54  .face.icon -> .face
drwx------  3 kali kali   4096 Sep 25 13:57  .gnupg
drwxr-xr-x  4 kali kali   4096 Sep 26 20:41  .java
drwx------  2 kali kali   4096 Dec  4 01:46  .john
-rw-------  1 kali kali     20 Dec  4 13:37  .lesshst
drwxr-xr-x  4 kali kali   4096 Sep 25 13:57  .local
drwx------  4 kali kali   4096 Sep 26 20:41  .mozilla
drwxr-xr-x 11 kali kali   4096 Dec 11 00:35  .msf4
drwx------  3 kali kali   4096 Sep 28 21:47  .pki
-rw-r--r--  1 kali kali    807 Sep 25 13:54  .profile
drwx------  2 kali kali   4096 Dec  6 18:59  .ssh
-rw-r--r--  1 kali kali      0 Sep 25 15:36  .sudo_as_admin_successful
-rw-------  1 kali kali    834 Feb 18 01:52  .viminfo
drwxr-xr-x  3 kali kali   4096 Sep 28 21:47  .vscode-oss
-rw-------  1 kali kali   4009 Feb 22 21:37  .xsession-errors
-rw-------  1 kali kali   4118 Feb 20 12:52  .xsession-errors.old
-rw-------  1 kali kali  45705 Feb 18 03:31  .zsh_history
-rw-r--r--  1 kali kali  10868 Sep 25 13:54  .zshrc
-rw-r--r--  1 kali kali  16384 Dec  3 18:26  3digits.txt
-rw-------  1 kali kali    800 Dec  3 01:33  840621_1701563612.hc22000
-rw-r--r--  1 kali kali   3505 Aug 16  2021  BastionHostingCreds.zip
drwxr-xr-x  2 kali kali   4096 Feb 11 01:42  Desktop
drwxr-xr-x  2 kali kali   4096 Sep 25 13:57  Documents
drwxr-xr-x 11 kali kali   4096 Dec 10 17:16  Downloads
-rw-------  1 kali kali   1056 Aug  6  2023  LIitdNxP.html
-rw-------  1 kali kali  22065 Aug  6  2023  MhckAmee.jpeg
drwxr-xr-x  2 kali kali   4096 Sep 25 13:57  Music
drwxr-xr-x  2 kali kali   4096 Dec  9 00:25  Pictures
drwxr-xr-x  2 kali kali   4096 Sep 25 13:57  Public
drwxr-xr-x  2 kali kali   4096 Sep 25 13:57  Templates
drwxr-xr-x  2 kali kali   4096 Sep 25 13:57  Videos
-rw-------  1 kali kali   2680 Aug  6  2023  beep.txt
-rw-r--r--  1 kali kali 557200 Dec  4 01:46  clinic-pass.lst
-rw-r--r--  1 kali kali   1078 Dec  4 01:04  clinic.lst
-rw-------  1 kali kali     39 Dec  9 04:04  cmd.php
-rw-r--r--  1 kali kali   3645 Aug 16  2021  combined.txt
-rw-------  1 kali kali   7188 Aug  6  2023  cronenum.py
-rw-r--r--  1 kali kali    243 Dec  3 23:33  crunch.txt
-rw-r--r--  1 kali kali    439 Dec  9 00:24  cthulu-rev.ps1
-rw-r--r--  1 kali kali    439 Dec  9 03:20  cthulu-rev444.ps1
-rw-r--r--  1 kali kali   2798 Aug 10  2021  emails.txt
-rw-r--r--  1 kali kali     38 Oct 12  2021  flag.txt
-rw-------  1 kali kali  21514 Aug  6  2023  git-dumper.py
drwxr-xr-x  5 kali kali   4096 Sep 25 15:59  gitdump
drwxr-xr-x  5 kali kali   4096 Sep 25 15:59  gitdump2
-rw-------  1 kali kali   4612 Aug  6  2023  hello
-rw-------  1 kali kali    460 Aug  6  2023  hello.asm
-rw-------  1 kali kali    656 Aug  6  2023  hello.o
drwxr-xr-x  5 kali kali   4096 Sep 28 21:40  htb
-rw-------  1 kali kali     30 Aug  6  2023  htb.sh
-rw-------  1 kali kali    873 Aug  6  2023  htb.txt
-rw-r--r--  1 kali kali  30358 Dec  5 18:06  hydra.restore
-rw-------  1 kali kali   1679 Aug  6  2023  id_rsa
-rw-------  1 kali kali   5446 Aug  6  2023  jp-free-08.protonvpn.net.udp.ovpn
-rw-r--r--  1 kali kali   2232 Dec  3 23:24  list.txt
-rw-------  1 kali kali  10406 Aug  6  2023  nictoscan.html
-rw-------  1 kali kali   5450 Aug  6  2023  nl-free-144.protonvpn.net.udp.ovpn
-rw-r--r--  1 kali kali   2629 Dec  5 03:13  output.txt
-rw-r--r--  1 kali kali    847 Aug 15  2021  passwords.txt
-rw-r--r--  1 kali kali   2196 Dec  4 20:51  passwords4.txt
-rw-r--r--  1 kali kali   5490 Feb 11 02:37  php-reverse-shell.php
-rw-r--r--  1 kali kali   5488 Feb 11 02:24  php-reverse-shell.png
-rw-------  1 kali kali  35204 Aug  6  2023 'ping 31.208.161'
drwxr-xr-x  3 kali kali   4096 Sep 25 15:59  py
-rw-------  1 kali kali   1798 Aug  6  2023  pyload050.py
-rw-------  1 kali kali    981 Aug  6  2023  red.txt
-rw-------  1 kali kali   1394 Aug  6  2023  request.txt
-rw-------  1 kali kali    809 Aug  6  2023  request2.txt
-rw-------  1 kali kali    810 Aug  6  2023  request3.txt
-rw-r--r--  1 kali kali   7168 Dec 11 00:45  reverse.exe
-rw-r--r--  1 kali kali    462 Jan 25 19:43  revsh-old.ps1
-rw-------  1 kali kali    442 Jan 25 19:45  revsh.ps1
drwxr-xr-x 18 kali kali   4096 Feb 18 01:38  s1
drwxrwxrwx  3 kali kali   4096 Dec 11 01:49  share
-rw-r--r--  1 kali kali     10 Dec  4 00:34  single-password-list.txt
-rw-------  1 kali kali   9315 Aug  6  2023  sofia75htb.ovpn
-rw-------  1 kali kali   8344 Aug  6  2023  sofia75thm.ovpn
-rw-r--r--  1 kali kali     20 Feb  7 19:07  test.py
drwxr-xr-x  9 kali kali   4096 Sep 25 15:59  thm
-rw-------  1 kali kali     30 Aug  6  2023  thm.sh
-rw-------  1 kali kali   1348 Aug  6  2023 'to obsidian'
-rw-------  1 kali kali   5443 Aug  6  2023  us-free-36.protonvpn.net.udp.ovpn
-rw-------  1 kali kali     58 Aug  6  2023  us.sh
-rw-------  1 kali kali     13 Aug  6  2023  useful.txt
-rw-r--r--  1 kali kali    307 Dec  4 20:52  usernames.txt
-rw-r--r--  1 kali kali     11 Dec  3 23:29  users.lst
-rw-r--r--  1 kali kali    752 Dec  9 02:54  vulnerable.ps1
-rw-r--r--  1 kali kali    752 Dec  9 03:17  vulnerable444.ps1
-rw-r--r--  1 root root  12818 Sep 25 20:29  wget-log
-rw-r--r--  1 kali kali   7168 Dec 11 00:35  win64_reverse.exe
-rw-r--r--  1 kali kali  27863 Dec 10 19:22  zsh_history_uniq_2023-12-10.txt

┌──(kali㉿kali)-[~]
└─$ cd htb        

┌──(kali㉿kali)-[~/htb]
└─$ mkdir crafty

┌──(kali㉿kali)-[~/htb]
└─$ git clone https://github.com/davidbombal/log4jminecraft.git                                              
Cloning into 'log4jminecraft'...
remote: Enumerating objects: 64, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 64 (delta 2), reused 2 (delta 2), pack-reused 60
Receiving objects: 100% (64/64), 16.51 KiB | 845.00 KiB/s, done.
Resolving deltas: 100% (20/20), done.

┌──(kali㉿kali)-[~/htb]
└─$ ls -la
total 28
drwxr-xr-x  7 kali kali 4096 Feb 22 22:14 .
drwx------ 30 kali kali 4096 Feb 22 21:40 ..
drwxr-xr-x  2 kali kali 4096 Sep 25 15:59 busqueda
drwxr-xr-x  3 kali kali 4096 Sep 28 21:42 clicker
drwxr-xr-x  2 kali kali 4096 Feb 22 22:14 crafty
drwxr-xr-x  4 kali kali 4096 Feb 22 22:14 log4jminecraft
drwxr-xr-x  2 kali kali 4096 Sep 25 15:59 sandworm

┌──(kali㉿kali)-[~/htb]
└─$ mv log4jminecraft crafty                      

┌──(kali㉿kali)-[~/htb]
└─$ ls -la
total 24
drwxr-xr-x  6 kali kali 4096 Feb 22 22:14 .
drwx------ 30 kali kali 4096 Feb 22 21:40 ..
drwxr-xr-x  2 kali kali 4096 Sep 25 15:59 busqueda
drwxr-xr-x  3 kali kali 4096 Sep 28 21:42 clicker
drwxr-xr-x  3 kali kali 4096 Feb 22 22:14 crafty
drwxr-xr-x  2 kali kali 4096 Sep 25 15:59 sandworm

┌──(kali㉿kali)-[~/htb]
└─$ cd crafty

┌──(kali㉿kali)-[~/htb/crafty]
└─$ ls -la
total 12
drwxr-xr-x 3 kali kali 4096 Feb 22 22:14 .
drwxr-xr-x 6 kali kali 4096 Feb 22 22:14 ..
drwxr-xr-x 4 kali kali 4096 Feb 22 22:14 log4jminecraft

┌──(kali㉿kali)-[~/htb/crafty]
└─$ cd log4jminecraft 

┌──(kali㉿kali)-[~/htb/crafty/log4jminecraft]
└─$ ls .la
ls: cannot access '.la': No such file or directory

┌──(kali㉿kali)-[~/htb/crafty/log4jminecraft]
└─$ ls -la           
total 28
drwxr-xr-x 4 kali kali 4096 Feb 22 22:14 .
drwxr-xr-x 3 kali kali 4096 Feb 22 22:14 ..
drwxr-xr-x 8 kali kali 4096 Feb 22 22:14 .git
-rw-r--r-- 1 kali kali 1167 Feb 22 22:14 README.md
-rw-r--r-- 1 kali kali  270 Feb 22 22:14 jcomp_pyserv.py
-rw-r--r-- 1 kali kali 3787 Feb 22 22:14 log4j.py
drwxr-xr-x 2 kali kali 4096 Feb 22 22:14 poc

┌──(kali㉿kali)-[~/htb/crafty/log4jminecraft]
└─$ nano README.md                   

```