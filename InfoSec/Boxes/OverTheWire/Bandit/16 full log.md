
```sh
┌──(kali㉿kali)-[~/otw/bandit]
└─$ ssh bandit16@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit16@bandit.labs.overthewire.org's password: 

      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to the #wargames channel on
discord or IRC.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ is disabled and to /proc
  restricted so that users cannot snoop on eachother. Files and directories
  with easily guessable or short names will be periodically deleted! The /tmp
  directory is regularly wiped.
  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few useful tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /opt/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /opt/pwndbg/
    * peda (https://github.com/longld/peda.git) in /opt/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /opt/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us on discord or IRC.

  Enjoy your stay!

bandit16@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Jun 20 04:06 .
drwxr-xr-x 70 root     root     4096 Jun 20 04:08 ..
-rw-r-----  1 bandit16 bandit16   33 Jun 20 04:06 .bandit15.password
-rw-r--r--  1 root     root      220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root     3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root      807 Mar 31 08:41 .profile
bandit16@bandit:~$ ss -tlupn
Netid   State    Recv-Q   Send-Q        Local Address:Port        Peer Address:Port   Process                                
udp     UNCONN   0        0                   0.0.0.0:8000             0.0.0.0:*                                             
udp     UNCONN   0        0                127.0.0.54:53               0.0.0.0:*                                             
udp     UNCONN   0        0             127.0.0.53%lo:53               0.0.0.0:*                                             
udp     UNCONN   0        0           10.0.1.213%ens5:68               0.0.0.0:*                                             
udp     UNCONN   0        0                 127.0.0.1:323              0.0.0.0:*                                             
udp     UNCONN   0        0                 127.0.0.1:13482            0.0.0.0:*                                             
udp     UNCONN   0        0                     [::1]:323                 [::]:*                                             
tcp     LISTEN   0        5                 127.0.0.1:1840             0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:50001            0.0.0.0:*       users:(("sendonpass",pid=943,fd=3))   
tcp     LISTEN   0        4096                0.0.0.0:31518            0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:51790            0.0.0.0:*                                             
tcp     LISTEN   0        5                 127.0.0.1:60917            0.0.0.0:*                                             
tcp     LISTEN   0        4096          127.0.0.53%lo:53               0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:30000            0.0.0.0:*                                             
tcp     LISTEN   0        4096                0.0.0.0:30001            0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:30002            0.0.0.0:*                                             
tcp     LISTEN   0        4096             127.0.0.54:53               0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:1111             0.0.0.0:*                                             
tcp     LISTEN   0        4096                0.0.0.0:31790            0.0.0.0:*                                             
tcp     LISTEN   0        8                   0.0.0.0:8000             0.0.0.0:*                                             
tcp     LISTEN   0        5                 127.0.0.1:4321             0.0.0.0:*                                             
tcp     LISTEN   0        5                   0.0.0.0:4091             0.0.0.0:*                                             
tcp     LISTEN   0        64                        *:31046                  *:*                                             
tcp     LISTEN   0        4096                      *:22                     *:*                                             
tcp     LISTEN   0        4096                      *:2230                   *:*                                             
tcp     LISTEN   0        4096                      *:2231                   *:*                                             
tcp     LISTEN   0        4096                      *:2232                   *:*                                             
tcp     LISTEN   0        4096                      *:2220                   *:*                                             
tcp     LISTEN   0        64                        *:31691                  *:*                                             
tcp     LISTEN   0        64                        *:31960                  *:*                                             
bandit16@bandit:~$ netstat -antplue
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       User       Inode      PID/Program name    
netstat: no support for `AF INET (tcp)' on this system.
tcp6       0      0 :::31046                :::*                    LISTEN      0          6829       -                   
tcp6       0      0 :::22                   :::*                    LISTEN      0          4997       -                   
tcp6       0      0 :::2230                 :::*                    LISTEN      0          4993       -                   
tcp6       0      0 :::2231                 :::*                    LISTEN      0          4999       -                   
tcp6       0      0 :::2232                 :::*                    LISTEN      0          4995       -                   
tcp6       0      0 :::2220                 :::*                    LISTEN      0          4991       -                   
tcp6       0      0 :::31691                :::*                    LISTEN      0          6830       -                   
tcp6       0      0 :::31960                :::*                    LISTEN      0          6831       -                   
tcp6       0    144 10.0.1.213:2220         147.235.198.125:19693   ESTABLISHED 0          1864958    -                   
tcp6       0      0 10.0.1.213:2220         13.53.105.174:47376     ESTABLISHED 0          1843528    -                   
tcp6       0      0 127.0.0.1:2220          127.0.0.1:52674         ESTABLISHED 0          1821138    -                   
tcp6       0    268 10.0.1.213:2220         195.14.245.218:55564    ESTABLISHED 0          1552943    -                   
tcp6       0      0 10.0.1.213:2220         182.253.55.205:4263     ESTABLISHED 0          1871369    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:46748    ESTABLISHED 0          1825433    -                   
tcp6       0    108 10.0.1.213:2220         60.238.96.236:62300     ESTABLISHED 0          1871796    -                   
tcp6       0      0 10.0.1.213:2220         85.2.169.122:56844      ESTABLISHED 0          1843770    -                   
tcp6       0      0 10.0.1.213:2220         90.188.6.92:47786       ESTABLISHED 0          1827175    -                   
tcp6       0      0 10.0.1.213:2220         47.63.39.247:37688      ESTABLISHED 0          1852362    -                   
tcp6       0      0 10.0.1.213:2220         85.2.169.122:50558      ESTABLISHED 0          1843772    -                   
tcp6       0      0 10.0.1.213:2220         176.238.138.169:60110   ESTABLISHED 0          1750037    -                   
tcp6       0      0 10.0.1.213:2220         72.108.178.191:54789    ESTABLISHED 0          1499419    -                   
tcp6       0      0 10.0.1.213:2220         124.217.18.221:5171     ESTABLISHED 0          1863933    -                   
tcp6       0    240 10.0.1.213:2220         103.35.214.149:42279    ESTABLISHED 0          1610097    -                   
tcp6       0      0 10.0.1.213:2220         90.69.139.173:58552     ESTABLISHED 0          1869293    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:46856    ESTABLISHED 0          1792214    -                   
tcp6       0      0 10.0.1.213:2220         50.4.92.167:53026       ESTABLISHED 0          1730855    -                   
tcp6       0      0 10.0.1.213:2220         83.137.123.222:23090    ESTABLISHED 0          1491495    -                   
tcp6       0      0 10.0.1.213:2220         196.217.173.47:63641    ESTABLISHED 0          1872373    -                   
tcp6       0      0 10.0.1.213:2220         202.168.147.229:58633   ESTABLISHED 0          1779478    -                   
tcp6       0      0 10.0.1.213:2220         223.178.81.86:7167      ESTABLISHED 0          1871538    -                   
tcp6       0      0 10.0.1.213:2220         178.47.8.190:50203      ESTABLISHED 0          689037     -                   
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2946     ESTABLISHED 0          1480135    -                   
tcp6       0    304 10.0.1.213:2220         110.226.179.30:16878    ESTABLISHED 0          1613327    -                   
tcp6       0      0 127.0.0.1:2220          127.0.0.1:51878         ESTABLISHED 0          1868062    -                   
tcp6       0      0 10.0.1.213:2220         64.225.218.251:47782    ESTABLISHED 0          1817496    -                   
tcp6       0      0 10.0.1.213:2220         49.37.114.172:52088     ESTABLISHED 0          1809888    -                   
tcp6       0      0 10.0.1.213:2220         196.250.136.166:56871   ESTABLISHED 0          1873359    -                   
tcp6       0      0 10.0.1.213:2220         85.143.112.77:56888     ESTABLISHED 0          1870977    -                   
tcp6       0      0 10.0.1.213:2220         119.195.43.185:50794    ESTABLISHED 0          1793134    -                   
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2990     ESTABLISHED 0          1709385    -                   
tcp6       0      0 10.0.1.213:2220         109.252.59.3:3063       ESTABLISHED 0          1854827    -                   
tcp6       0      0 10.0.1.213:2220         90.165.4.164:51750      ESTABLISHED 0          1697942    -                   
tcp6       0      0 10.0.1.213:2220         86.106.136.106:55684    ESTABLISHED 0          1823758    -                   
tcp6       0      0 10.0.1.213:2220         72.108.178.191:65184    ESTABLISHED 0          1348471    -                   
tcp6       0    432 10.0.1.213:2220         174.229.182.11:4589     ESTABLISHED 0          1818066    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:55002    ESTABLISHED 0          1870145    -                   
tcp6       0      0 10.0.1.213:2220         78.171.155.169:51254    ESTABLISHED 0          1037484    -                   
tcp6       0      0 10.0.1.213:2220         37.155.231.34:17541     ESTABLISHED 0          1580631    -                   
tcp6       0      0 10.0.1.213:2220         45.18.65.73:56462       ESTABLISHED 0          1765036    -                   
tcp6       0      0 10.0.1.213:2220         149.108.159.41:60664    ESTABLISHED 0          1867991    -                   
tcp6       0      0 10.0.1.213:2220         31.52.159.1:49279       ESTABLISHED 0          1763959    -                   
tcp6       0      0 10.0.1.213:2220         1.171.212.146:50218     ESTABLISHED 0          1860086    -                   
tcp6       0    308 10.0.1.213:2220         122.170.162.241:50779   ESTABLISHED 0          1414758    -                   
tcp6       0      0 10.0.1.213:2220         89.163.130.100:56389    ESTABLISHED 0          1616201    -                   
tcp6       0    304 10.0.1.213:2220         49.37.114.172:51729     ESTABLISHED 0          1703912    -                   
tcp6       0      0 10.0.1.213:2220         137.83.244.161:27600    ESTABLISHED 0          1726642    -                   
tcp6       0      0 10.0.1.213:2220         42.62.176.66:60326      ESTABLISHED 0          1836946    -                   
tcp6       0      0 10.0.1.213:2220         89.176.167.81:59634     ESTABLISHED 0          1862078    -                   
tcp6       0      0 10.0.1.213:2220         43.246.202.201:50779    ESTABLISHED 0          1710134    -                   
tcp6       0      0 10.0.1.213:2220         49.43.233.202:59210     ESTABLISHED 0          1622256    -                   
tcp6       0      0 10.0.1.213:2220         125.167.48.126:3481     ESTABLISHED 0          1830080    -                   
tcp6       0      0 10.0.1.213:2220         24.114.55.253:61024     ESTABLISHED 0          1801127    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:50502    ESTABLISHED 0          1715001    -                   
tcp6       0      0 127.0.0.1:2220          127.0.0.1:38630         ESTABLISHED 0          1869308    -                   
tcp6       0      0 10.0.1.213:2220         171.78.155.184:63142    ESTABLISHED 0          1807826    -                   
tcp6       0      0 127.0.0.1:2220          127.0.0.1:38614         ESTABLISHED 0          1868155    -                   
tcp6       0      0 10.0.1.213:2220         36.82.208.132:58501     ESTABLISHED 0          1606377    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:47024    ESTABLISHED 0          1605572    -                   
tcp6       0      0 10.0.1.213:2220         178.47.8.190:53224      ESTABLISHED 0          661603     -                   
tcp6       0      0 10.0.1.213:2220         41.90.186.36:2316       ESTABLISHED 0          1822943    -                   
tcp6       0      0 10.0.1.213:2220         93.188.83.138:40826     ESTABLISHED 0          1706435    -                   
tcp6       0      0 10.0.1.213:2220         45.119.30.144:21342     ESTABLISHED 0          1867113    -                   
tcp6       0      0 10.0.1.213:2220         149.40.48.244:1356      ESTABLISHED 0          1855556    -                   
tcp6       0      0 10.0.1.213:2220         203.192.244.236:50550   ESTABLISHED 0          1852329    -                   
tcp6       0      0 10.0.1.213:2220         131.114.166.254:56880   ESTABLISHED 0          1824830    -                   
tcp6       0      0 10.0.1.213:2220         31.49.0.175:38714       ESTABLISHED 0          1872797    -                   
tcp6       0     44 10.0.1.213:2220         177.100.125.85:20672    ESTABLISHED 0          1810249    -                   
tcp6       0      0 10.0.1.213:2220         217.251.154.37:58184    ESTABLISHED 0          1872524    -                   
tcp6       0      0 10.0.1.213:2220         90.167.203.124:37086    ESTABLISHED 0          1828537    -                   
tcp6       0      0 10.0.1.213:2220         122.161.68.226:3007     ESTABLISHED 0          1847082    -                   
tcp6       0    268 10.0.1.213:2220         45.152.180.254:59222    ESTABLISHED 0          1697637    -                   
tcp6       0      0 10.0.1.213:2220         116.72.87.42:37468      ESTABLISHED 0          1657946    -                   
tcp6       0      0 10.0.1.213:2220         42.105.230.26:12734     ESTABLISHED 0          1800420    -                   
tcp6       0      0 10.0.1.213:2220         46.112.68.229:7868      ESTABLISHED 0          1861178    -                   
tcp6       0     36 127.0.0.1:2220          127.0.0.1:38642         ESTABLISHED 0          1868329    -                   
tcp6       0      0 10.0.1.213:2220         72.188.198.178:62707    ESTABLISHED 0          1835883    -                   
tcp6       0      0 10.0.1.213:2220         200.2.121.203:52010     ESTABLISHED 0          1823479    -                   
tcp6       0    296 10.0.1.213:2220         79.34.170.201:57271     ESTABLISHED 0          1603417    -                   
tcp6       0      0 10.0.1.213:2220         160.178.4.72:56378      ESTABLISHED 0          1859416    -                   
tcp6       0      0 10.0.1.213:2220         63.215.172.54:31389     ESTABLISHED 0          1827778    -                   
tcp6       0      0 10.0.1.213:2220         111.194.35.228:14513    ESTABLISHED 0          1866614    -                   
tcp6       0      0 10.0.1.213:2220         155.247.134.189:27970   ESTABLISHED 0          1788314    -                   
tcp6       0      0 10.0.1.213:2220         182.18.198.44:59942     ESTABLISHED 0          1752478    -                   
tcp6       0      0 10.0.1.213:2220         136.32.113.72:63842     ESTABLISHED 0          1752850    -                   
tcp6       0      0 10.0.1.213:2220         223.178.81.86:17720     ESTABLISHED 0          1873342    -                   
tcp6       0      0 10.0.1.213:2220         213.87.148.163:59500    ESTABLISHED 0          1834791    -                   
tcp6       0    268 10.0.1.213:2220         176.238.138.169:60050   ESTABLISHED 0          1525894    -                   
tcp6       0      0 10.0.1.213:2220         46.154.36.130:58801     ESTABLISHED 0          1574413    -                   
tcp6       0      0 10.0.1.213:2220         203.122.18.250:13850    ESTABLISHED 0          1148867    -                   
tcp6       0    268 10.0.1.213:2220         41.90.186.36:1552       ESTABLISHED 0          1635965    -                   
tcp6       0      0 10.0.1.213:2220         90.248.22.212:50898     ESTABLISHED 0          1785963    -                   
tcp6       0   3608 10.0.1.213:2220         63.215.172.54:24365     ESTABLISHED 0          1873371    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:36916    ESTABLISHED 0          1757998    -                   
tcp6       0      0 10.0.1.213:2220         213.57.86.146:55127     ESTABLISHED 0          1752870    -                   
tcp6       0      0 10.0.1.213:2220         49.37.114.172:52218     ESTABLISHED 0          1849115    -                   
tcp6       0      0 10.0.1.213:2220         24.114.55.253:27436     ESTABLISHED 0          1127565    -                   
tcp6       0    296 10.0.1.213:2220         47.132.113.201:61582    ESTABLISHED 0          1841941    -                   
tcp6       0      0 10.0.1.213:2220         181.36.17.92:40646      ESTABLISHED 0          1864314    -                   
tcp6       0      0 10.0.1.213:2220         174.229.182.169:5949    ESTABLISHED 0          1752110    -                   
tcp6       0      0 10.0.1.213:2220         45.18.65.73:58225       ESTABLISHED 0          1744747    -                   
tcp6       0      0 10.0.1.213:2220         187.55.77.18:51048      ESTABLISHED 0          1871970    -                   
tcp6       0      0 10.0.1.213:2220         82.158.5.53:43352       ESTABLISHED 0          1770956    -                   
tcp6       0      0 10.0.1.213:2220         171.78.155.184:63143    ESTABLISHED 0          1809499    -                   
tcp6       0      0 127.0.0.1:2220          127.0.0.1:52738         ESTABLISHED 0          1758645    -                   
tcp6       0      0 10.0.1.213:2220         37.156.155.126:50512    ESTABLISHED 0          1737263    -                   
tcp6       0    108 10.0.1.213:2220         188.190.71.107:54129    ESTABLISHED 0          1822947    -                   
tcp6       0      0 10.0.1.213:2220         94.54.56.140:46151      ESTABLISHED 0          1136843    -                   
tcp6       0      0 10.0.1.213:2220         213.87.148.163:43743    ESTABLISHED 0          1829993    -                   
tcp6       0      0 10.0.1.213:2220         3.253.234.86:34448      ESTABLISHED 0          1874288    -                   
tcp6       0      0 10.0.1.213:2220         197.46.94.151:49848     ESTABLISHED 0          1777788    -                   
tcp6       0    128 10.0.1.213:2220         49.161.12.171:54865     ESTABLISHED 0          1871431    -                   
tcp6       0      0 10.0.1.213:2220         105.78.28.20:55950      ESTABLISHED 0          1871287    -                   
tcp6       0      0 10.0.1.213:2220         223.238.110.198:41628   ESTABLISHED 0          1812510    -                   
tcp6       0    432 10.0.1.213:2220         143.44.165.139:9559     ESTABLISHED 0          1855101    -                   
tcp6       0      0 10.0.1.213:2220         152.59.133.158:46842    ESTABLISHED 0          1770806    -                   
tcp6       0      0 10.0.1.213:2220         152.58.163.196:64388    ESTABLISHED 0          1871580    -                   
tcp6       0    432 10.0.1.213:2220         106.222.176.231:47168   ESTABLISHED 0          1825418    -                   
tcp6       0      0 10.0.1.213:2220         82.163.115.98:33360     ESTABLISHED 0          1755622    -                   
tcp6       0      0 10.0.1.213:2220         122.173.26.211:31957    ESTABLISHED 0          1819623    -                   
tcp6       0      0 10.0.1.213:2220         45.18.65.73:63422       ESTABLISHED 0          1842295    -                   
tcp6       0      0 10.0.1.213:2220         217.96.44.106:49746     ESTABLISHED 0          1772089    -                   
tcp6       0      0 10.0.1.213:2220         76.141.51.7:44042       ESTABLISHED 0          1546690    -                   
tcp6       0      0 10.0.1.213:2220         80.215.149.124:3049     ESTABLISHED 0          1770469    -                   
tcp6       0    296 10.0.1.213:2220         152.59.134.215:4881     ESTABLISHED 0          1659686    -                   
tcp6       0    361 10.0.1.213:2220         223.238.120.28:35092    LAST_ACK    0          0          -                   
tcp6       0    304 10.0.1.213:2220         120.29.68.75:47591      ESTABLISHED 0          1661826    -                   
tcp6       0      0 10.0.1.213:2220         86.127.229.236:34348    ESTABLISHED 0          1735431    -                   
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2953     ESTABLISHED 0          1244313    -                   
tcp6       0    216 10.0.1.213:2220         91.117.235.176:3556     ESTABLISHED 0          1820656    -                   
tcp6       0      0 10.0.1.213:2220         223.72.66.99:13838      ESTABLISHED 0          1854829    -                   
tcp6       0     72 10.0.1.213:2220         89.1.215.188:35012      ESTABLISHED 0          1827177    -                   
tcp6       0     72 10.0.1.213:2220         78.62.34.159:60220      ESTABLISHED 0          1810517    -                   
tcp6       0      0 10.0.1.213:2220         41.65.103.16:58773      ESTABLISHED 0          1723265    -                   
tcp6       0      0 10.0.1.213:2220         186.15.204.84:7820      ESTABLISHED 0          1755718    -                   
tcp6       0   3544 10.0.1.213:2220         31.208.161.82:52130     ESTABLISHED 0          1744750    -                   
tcp6       0      0 10.0.1.213:2220         120.188.38.216:55498    ESTABLISHED 0          1870546    -                   
tcp6       0      0 10.0.1.213:2220         118.216.99.158:54356    ESTABLISHED 0          1710815    -                   
tcp6       0      0 10.0.1.213:2220         89.87.173.21:62368      ESTABLISHED 0          1869735    -                   
tcp6       0      0 10.0.1.213:2220         131.114.174.46:54838    ESTABLISHED 0          1872225    -                   
tcp6       0      0 10.0.1.213:2220         223.238.120.28:35098    ESTABLISHED 0          1874336    -                   
tcp6       0      0 10.0.1.213:2220         197.46.94.151:51756     ESTABLISHED 0          1834857    -                   
tcp6       0      0 10.0.1.213:2220         41.116.56.200:45945     ESTABLISHED 0          1822707    -                   
tcp6       0      0 10.0.1.213:2220         89.189.1.6:35295        ESTABLISHED 0          1400088    -                   
tcp6       0     36 10.0.1.213:2220         91.15.89.20:42090       ESTABLISHED 0          1758429    -                   
tcp6       0      0 10.0.1.213:2220         101.255.150.49:53832    ESTABLISHED 0          1841825    -                   
tcp6       0      0 10.0.1.213:2220         201.179.99.209:38896    ESTABLISHED 0          1720845    -                   
tcp6       0      0 10.0.1.213:2220         176.59.21.254:58890     ESTABLISHED 0          1638805    -                   
tcp6       0      0 10.0.1.213:2220         180.252.83.130:60042    ESTABLISHED 0          1780293    -                   
tcp6       0      0 10.0.1.213:2220         64.225.107.69:33376     ESTABLISHED 0          1722771    -                   
bandit16@bandit:~$ netstat -ano
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       Timer
tcp6       0      0 :::31046                :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::22                   :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::2230                 :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::2231                 :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::2232                 :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::2220                 :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::31691                :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::31960                :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 10.0.1.213:2220         147.235.198.125:19693   ESTABLISHED keepalive (6820.70/0/0)
tcp6       0      0 10.0.1.213:2220         43.246.202.200:51079    ESTABLISHED keepalive (7114.70/0/0)
tcp6       0      0 10.0.1.213:2220         63.215.172.54:44372     ESTABLISHED keepalive (7172.66/0/0)
tcp6       0      0 10.0.1.213:2220         89.163.130.100:54113    ESTABLISHED keepalive (7003.56/0/0)
tcp6       0      0 127.0.0.1:2220          127.0.0.1:52674         ESTABLISHED keepalive (6358.46/0/0)
tcp6       0      0 127.0.0.1:2220          127.0.0.1:52552         ESTABLISHED keepalive (7068.17/0/0)
tcp6       0    268 10.0.1.213:2220         195.14.245.218:55564    ESTABLISHED on (86.54/14/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:46748    ESTABLISHED keepalive (6475.05/0/0)
tcp6       0      0 10.0.1.213:2220         85.2.169.122:56844      ESTABLISHED keepalive (6639.13/0/0)
tcp6       0    144 10.0.1.213:2220         90.188.6.92:47786       ESTABLISHED on (0.16/0/0)
tcp6       0      0 10.0.1.213:2220         63.215.172.54:5352      ESTABLISHED keepalive (7135.23/0/0)
tcp6       0      0 10.0.1.213:2220         85.2.169.122:50558      ESTABLISHED keepalive (6639.61/0/0)
tcp6       0      0 10.0.1.213:2220         176.238.138.169:60110   ESTABLISHED keepalive (5626.54/0/0)
tcp6       0      0 10.0.1.213:2220         72.108.178.191:54789    ESTABLISHED keepalive (2971.19/0/0)
tcp6       0      0 10.0.1.213:2220         202.170.201.187:24042   ESTABLISHED keepalive (7111.88/0/0)
tcp6       0      0 10.0.1.213:2220         49.161.12.171:54949     ESTABLISHED keepalive (7072.69/0/0)
tcp6       0      0 10.0.1.213:2220         124.217.18.221:5171     ESTABLISHED keepalive (6819.51/0/0)
tcp6       0    240 10.0.1.213:2220         103.35.214.149:42279    ESTABLISHED on (12.81/12/0)
tcp6       0      0 10.0.1.213:2220         223.72.66.99:14273      ESTABLISHED keepalive (7135.21/0/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:46856    ESTABLISHED keepalive (6057.39/0/0)
tcp6       0      0 10.0.1.213:2220         50.4.92.167:53026       ESTABLISHED keepalive (5460.04/0/0)
tcp6       0      0 10.0.1.213:2220         83.137.123.222:23090    ESTABLISHED keepalive (2891.73/0/0)
tcp6       0      0 10.0.1.213:2220         217.96.44.106:49987     ESTABLISHED keepalive (7097.90/0/0)
tcp6       0      0 10.0.1.213:2220         196.217.173.47:63641    ESTABLISHED keepalive (6929.41/0/0)
tcp6       0      0 10.0.1.213:2220         143.44.165.139:38532    ESTABLISHED keepalive (7012.51/0/0)
tcp6       0      0 10.0.1.213:2220         202.168.147.229:58633   ESTABLISHED keepalive (5974.93/0/0)
tcp6       0      0 10.0.1.213:2220         223.178.81.86:7167      ESTABLISHED keepalive (6933.01/0/0)
tcp6       0      0 10.0.1.213:2220         178.47.8.190:50203      ESTABLISHED keepalive (149.23/0/0)
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2946     ESTABLISHED keepalive (2673.40/0/0)
tcp6       0    304 10.0.1.213:2220         110.226.179.30:16878    ESTABLISHED on (98.83/10/0)
tcp6       0     36 127.0.0.1:2220          127.0.0.1:51878         ESTABLISHED on (0.20/0/0)
tcp6       0      0 10.0.1.213:2220         49.37.114.172:52088     ESTABLISHED keepalive (6216.34/0/0)
tcp6       0      0 10.0.1.213:2220         196.250.136.166:56871   ESTABLISHED keepalive (6968.09/0/0)
tcp6       0      0 10.0.1.213:2220         3.253.234.86:54032      ESTABLISHED keepalive (7129.42/0/0)
tcp6       0      0 10.0.1.213:2220         119.195.43.185:50794    ESTABLISHED keepalive (6063.32/0/0)
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2990     ESTABLISHED keepalive (5111.55/0/0)
tcp6       0      0 10.0.1.213:2220         109.252.59.3:3063       ESTABLISHED keepalive (6738.47/0/0)
tcp6       0      0 10.0.1.213:2220         90.165.4.164:51750      ESTABLISHED keepalive (4991.73/0/0)
tcp6       0      0 10.0.1.213:2220         89.87.173.21:62395      ESTABLISHED keepalive (7151.04/0/0)
tcp6       0      0 10.0.1.213:2220         157.34.47.46:62959      ESTABLISHED keepalive (7169.33/0/0)
tcp6       0      0 10.0.1.213:2220         86.106.136.106:55684    ESTABLISHED keepalive (6417.76/0/0)
tcp6       0      0 10.0.1.213:2220         72.108.178.191:65184    ESTABLISHED keepalive (1241.21/0/0)
tcp6       0      0 10.0.1.213:2220         101.255.150.49:53936    ESTABLISHED keepalive (7134.59/0/0)
tcp6       0    432 10.0.1.213:2220         174.229.182.11:4589     ESTABLISHED on (21.00/11/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:55002    ESTABLISHED keepalive (6881.07/0/0)
tcp6       0      0 10.0.1.213:2220         78.171.155.169:51254    ESTABLISHED keepalive (3149.09/0/0)
tcp6       0      0 10.0.1.213:2220         37.155.231.34:17541     ESTABLISHED keepalive (3849.60/0/0)
tcp6       0      0 10.0.1.213:2220         45.18.65.73:56462       ESTABLISHED keepalive (5791.35/0/0)
tcp6       0      0 10.0.1.213:2220         31.52.159.1:49279       ESTABLISHED keepalive (5793.35/0/0)
tcp6       0      0 10.0.1.213:2220         1.171.212.146:50218     ESTABLISHED keepalive (6781.66/0/0)
tcp6       0      0 10.0.1.213:2220         90.69.139.173:59036     ESTABLISHED keepalive (7129.66/0/0)
tcp6       0      0 10.0.1.213:2220         89.163.130.100:56389    ESTABLISHED keepalive (4252.91/0/0)
tcp6       0    304 10.0.1.213:2220         49.37.114.172:51729     ESTABLISHED on (37.39/9/0)
tcp6       0    564 10.0.1.213:2220         137.83.244.161:27600    ESTABLISHED on (0.09/0/0)
tcp6       0      0 10.0.1.213:2220         42.62.176.66:60326      ESTABLISHED keepalive (6612.55/0/0)
tcp6       0      0 10.0.1.213:2220         49.43.233.202:59210     ESTABLISHED keepalive (4290.06/0/0)
tcp6       0      0 10.0.1.213:2220         85.143.112.77:49726     ESTABLISHED keepalive (7199.59/0/0)
tcp6       0      0 10.0.1.213:2220         24.114.55.253:61024     ESTABLISHED keepalive (6119.13/0/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:50502    ESTABLISHED keepalive (5176.82/0/0)
tcp6       0     36 127.0.0.1:2220          127.0.0.1:38630         ESTABLISHED on (0.20/0/0)
tcp6       0      0 10.0.1.213:2220         47.63.39.247:48418      ESTABLISHED keepalive (7064.44/0/0)
tcp6       0      0 10.0.1.213:2220         171.78.155.184:63142    ESTABLISHED keepalive (6195.97/0/0)
tcp6       0      0 127.0.0.1:2220          127.0.0.1:38614         ESTABLISHED keepalive (6869.01/0/0)
tcp6       0      0 10.0.1.213:2220         187.55.77.18:51054      ESTABLISHED keepalive (6983.95/0/0)
tcp6       0      0 10.0.1.213:2220         103.189.201.38:50210    ESTABLISHED keepalive (7125.73/0/0)
tcp6       0      0 10.0.1.213:2220         36.82.208.132:58501     ESTABLISHED keepalive (4119.10/0/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:47024    ESTABLISHED keepalive (4123.20/0/0)
tcp6       0      0 10.0.1.213:2220         197.46.94.151:53090     FIN_WAIT2   timewait (57.40/0/0)
tcp6       0      0 10.0.1.213:2220         178.47.8.190:53224      ESTABLISHED keepalive (0.00/0/0)
tcp6       0    612 10.0.1.213:2220         182.253.55.205:8683     ESTABLISHED on (0.20/0/0)
tcp6       0      0 10.0.1.213:2220         41.90.186.36:2316       ESTABLISHED keepalive (6396.52/0/0)
tcp6       0      0 10.0.1.213:2220         93.188.83.138:40826     ESTABLISHED keepalive (5078.73/0/0)
tcp6       0      0 10.0.1.213:2220         149.40.48.244:1356      ESTABLISHED keepalive (6730.55/0/0)
tcp6       0      0 10.0.1.213:2220         203.192.244.236:50550   ESTABLISHED keepalive (6705.13/0/0)
tcp6       0      0 10.0.1.213:2220         60.238.96.236:62314     ESTABLISHED keepalive (7124.22/0/0)
tcp6       0      0 10.0.1.213:2220         31.49.0.175:38714       ESTABLISHED keepalive (6949.88/0/0)
tcp6       0      0 10.0.1.213:2220         177.100.125.85:20672    ESTABLISHED keepalive (6219.87/0/0)
tcp6       0      0 10.0.1.213:2220         90.167.203.124:37086    ESTABLISHED keepalive (6510.49/0/0)
tcp6       0    252 10.0.1.213:2220         45.119.30.144:21307     ESTABLISHED on (0.21/0/0)
tcp6       0    268 10.0.1.213:2220         45.152.180.254:59222    ESTABLISHED on (61.96/9/0)
tcp6       0    288 10.0.1.213:2220         116.72.87.42:37468      ESTABLISHED on (0.21/0/0)
tcp6       0      0 10.0.1.213:2220         42.105.230.26:12734     ESTABLISHED keepalive (6112.79/0/0)
tcp6       0      0 10.0.1.213:2220         46.112.68.229:7868      ESTABLISHED keepalive (6794.19/0/0)
tcp6       0      0 127.0.0.1:2220          127.0.0.1:38642         ESTABLISHED keepalive (6872.86/0/0)
tcp6       0      0 10.0.1.213:2220         72.188.198.178:62707    ESTABLISHED keepalive (6571.66/0/0)
tcp6       0      0 10.0.1.213:2220         200.2.121.203:52010     ESTABLISHED keepalive (6424.63/0/0)
tcp6       0      0 10.0.1.213:2220         160.178.4.72:56378      ESTABLISHED keepalive (6762.07/0/0)
tcp6       0      0 10.0.1.213:2220         111.194.35.228:14513    ESTABLISHED keepalive (6838.42/0/0)
tcp6       0      0 10.0.1.213:2220         155.247.134.189:27970   ESTABLISHED keepalive (6039.70/0/0)
tcp6       0      0 10.0.1.213:2220         182.18.198.44:59942     ESTABLISHED keepalive (5642.81/0/0)
tcp6       0      0 10.0.1.213:2220         136.32.113.72:63842     ESTABLISHED keepalive (5653.07/0/0)
tcp6       0      0 10.0.1.213:2220         223.178.81.86:17720     ESTABLISHED keepalive (6963.95/0/0)
tcp6       0      0 10.0.1.213:2220         213.87.148.163:59500    ESTABLISHED keepalive (6560.54/0/0)
tcp6       0    268 10.0.1.213:2220         176.238.138.169:60050   ESTABLISHED on (25.10/15/0)
tcp6       0      0 10.0.1.213:2220         46.154.36.130:58801     ESTABLISHED keepalive (3787.05/0/0)
tcp6       0      0 10.0.1.213:2220         203.122.18.250:13850    ESTABLISHED keepalive (1198.16/0/0)
tcp6       0    268 10.0.1.213:2220         41.90.186.36:1552       ESTABLISHED on (21.00/11/0)
tcp6       0      0 10.0.1.213:2220         90.248.22.212:50898     ESTABLISHED keepalive (6031.95/0/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:36916    ESTABLISHED keepalive (5732.45/0/0)
tcp6       0      0 10.0.1.213:2220         213.57.86.146:55127     ESTABLISHED keepalive (5654.98/0/0)
tcp6       0      0 10.0.1.213:2220         24.114.55.253:27436     ESTABLISHED keepalive (5919.41/0/0)
tcp6       0      0 10.0.1.213:2220         47.132.113.201:61582    ESTABLISHED keepalive (6626.19/0/0)
tcp6       0      0 10.0.1.213:2220         49.37.114.172:52313     ESTABLISHED keepalive (7128.45/0/0)
tcp6       0      0 10.0.1.213:2220         122.161.68.226:13199    ESTABLISHED keepalive (7020.80/0/0)
tcp6       0      0 10.0.1.213:2220         174.229.182.169:5949    ESTABLISHED keepalive (5638.03/0/0)
tcp6       0      0 10.0.1.213:2220         45.18.65.73:58225       ESTABLISHED keepalive (5583.86/0/0)
tcp6       0      0 10.0.1.213:2220         82.158.5.53:43352       ESTABLISHED keepalive (5876.09/0/0)
tcp6       0      0 10.0.1.213:2231         49.47.192.14:62550      ESTABLISHED keepalive (7155.87/0/0)
tcp6       0      0 10.0.1.213:2220         171.78.155.184:63143    ESTABLISHED keepalive (6214.01/0/0)
tcp6       0      0 127.0.0.1:2220          127.0.0.1:52738         ESTABLISHED keepalive (5741.69/0/0)
tcp6       0      0 10.0.1.213:2220         37.156.155.126:50512    ESTABLISHED keepalive (5489.78/0/0)
tcp6       0      0 10.0.1.213:2220         188.190.71.107:54129    ESTABLISHED keepalive (6397.45/0/0)
tcp6       0     72 10.0.1.213:2220         89.176.167.81:52710     ESTABLISHED on (0.07/0/0)
tcp6       0      0 10.0.1.213:2220         94.54.56.140:46151      ESTABLISHED keepalive (66.11/0/8)
tcp6       0      0 10.0.1.213:2220         213.87.148.163:43743    ESTABLISHED keepalive (6540.63/0/0)
tcp6       0      0 10.0.1.213:2220         105.78.28.20:55950      ESTABLISHED keepalive (6921.97/0/0)
tcp6       0      0 10.0.1.213:2220         223.238.110.198:41628   ESTABLISHED keepalive (6226.22/0/0)
tcp6       0      0 10.0.1.213:2220         64.224.139.158:4610     ESTABLISHED keepalive (7067.48/0/0)
tcp6       0      0 10.0.1.213:2220         152.59.133.158:46842    ESTABLISHED keepalive (5868.92/0/0)
tcp6       0      0 10.0.1.213:2220         152.58.163.196:64388    ESTABLISHED keepalive (6933.74/0/0)
tcp6       0     36 10.0.1.213:2220         82.163.115.98:33360     ESTABLISHED on (0.23/0/0)
tcp6       0      0 10.0.1.213:2220         64.225.218.251:35284    ESTABLISHED keepalive (7180.38/0/0)
tcp6       0      0 10.0.1.213:2220         122.173.26.211:31957    ESTABLISHED keepalive (6332.78/0/0)
tcp6       0      0 10.0.1.213:2220         45.18.65.73:63422       ESTABLISHED keepalive (6617.49/0/0)
tcp6       0      0 10.0.1.213:2220         217.96.44.106:49746     ESTABLISHED keepalive (5882.96/0/0)
tcp6       0      0 10.0.1.213:2220         76.141.51.7:44042       ESTABLISHED keepalive (3502.69/0/0)
tcp6       0      0 10.0.1.213:2220         80.215.149.124:3049     ESTABLISHED keepalive (5871.32/0/0)
tcp6       0    296 10.0.1.213:2220         152.59.134.215:4881     ESTABLISHED on (57.86/9/0)
tcp6       0    304 10.0.1.213:2220         120.29.68.75:47591      ESTABLISHED on (49.67/11/0)
tcp6       0      0 10.0.1.213:2220         86.127.229.236:34348    ESTABLISHED keepalive (5479.90/0/0)
tcp6       0      0 10.0.1.213:2220         88.201.206.233:2953     ESTABLISHED keepalive (58.27/0/0)
tcp6       0      0 10.0.1.213:2220         91.117.235.176:3556     ESTABLISHED keepalive (6355.01/0/0)
tcp6       0      0 10.0.1.213:2220         89.1.215.188:35012      ESTABLISHED keepalive (6500.15/0/0)
tcp6       0     72 10.0.1.213:2220         78.62.34.159:60220      ESTABLISHED on (0.07/0/0)
tcp6       0      0 10.0.1.213:2220         41.65.103.16:58773      ESTABLISHED keepalive (5391.20/0/0)
tcp6       0      0 10.0.1.213:2220         186.15.204.84:7820      ESTABLISHED keepalive (5688.19/0/0)
tcp6       0    376 10.0.1.213:2220         31.208.161.82:52130     ESTABLISHED on (0.01/0/0)
tcp6       0      0 10.0.1.213:2220         120.188.38.216:55498    ESTABLISHED keepalive (6899.23/0/0)
tcp6       0      0 10.0.1.213:2220         181.36.17.92:36934      ESTABLISHED keepalive (7023.98/0/0)
tcp6       0      0 10.0.1.213:2220         118.216.99.158:54356    ESTABLISHED keepalive (5167.15/0/0)
tcp6       0    396 10.0.1.213:2220         106.222.176.231:47186   ESTABLISHED on (0.22/0/0)
tcp6       0      0 10.0.1.213:2220         131.114.174.46:54838    ESTABLISHED keepalive (6920.35/0/0)
tcp6       0   1368 10.0.1.213:2220         157.34.47.46:62884      ESTABLISHED on (20.29/1/0)
tcp6       0      0 10.0.1.213:2220         223.238.120.28:35098    ESTABLISHED keepalive (6972.96/0/0)
tcp6       0      0 10.0.1.213:2220         41.116.56.200:45945     ESTABLISHED keepalive (6415.27/0/0)
tcp6       0      0 10.0.1.213:2220         89.189.1.6:35295        ESTABLISHED keepalive (1814.59/0/0)
tcp6       0      0 10.0.1.213:2220         91.15.89.20:42090       ESTABLISHED keepalive (5733.58/0/0)
tcp6       0     52 10.0.1.213:2220         131.114.166.254:57012   ESTABLISHED on (0.20/0/0)
tcp6       0    304 10.0.1.213:2220         201.179.99.209:38896    ESTABLISHED on (52.55/7/0)
tcp6       0      0 10.0.1.213:2220         176.59.21.254:58890     ESTABLISHED keepalive (4462.70/0/0)
tcp6       0      0 10.0.1.213:2220         180.252.83.130:60042    ESTABLISHED keepalive (5981.75/0/0)
udp6       0      0 ::1:323                 :::*                                off (0.00/0/0)
raw6       0      0 :::58                   :::*                    7           off (0.00/0/0)
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
bandit16@bandit:~$ ss --help
Usage: ss [ OPTIONS ]
       ss [ OPTIONS ] [ FILTER ]
   -h, --help          this message
   -V, --version       output version information
   -n, --numeric       don't resolve service names
   -r, --resolve       resolve host names
   -a, --all           display all sockets
   -l, --listening     display listening sockets
   -o, --options       show timer information
   -e, --extended      show detailed socket information
   -m, --memory        show socket memory usage
   -p, --processes     show process using socket
   -T, --threads       show thread using socket
   -i, --info          show internal TCP information
       --tipcinfo      show internal tipc socket information
   -s, --summary       show socket usage summary
       --tos           show tos and priority information
       --cgroup        show cgroup information
   -b, --bpf           show bpf filter socket information
   -E, --events        continually display sockets as they are destroyed
   -Z, --context       display task SELinux security contexts
   -z, --contexts      display task and socket SELinux security contexts
   -N, --net           switch to the specified network namespace name

   -4, --ipv4          display only IP version 4 sockets
   -6, --ipv6          display only IP version 6 sockets
   -0, --packet        display PACKET sockets
   -t, --tcp           display only TCP sockets
   -M, --mptcp         display only MPTCP sockets
   -S, --sctp          display only SCTP sockets
   -u, --udp           display only UDP sockets
   -d, --dccp          display only DCCP sockets
   -w, --raw           display only RAW sockets
   -x, --unix          display only Unix domain sockets
       --tipc          display only TIPC sockets
       --vsock         display only vsock sockets
       --xdp           display only XDP sockets
   -f, --family=FAMILY display sockets of type FAMILY
       FAMILY := {inet|inet6|link|unix|netlink|vsock|tipc|xdp|help}

   -K, --kill          forcibly close sockets, display what was closed
   -H, --no-header     Suppress header line
   -O, --oneline       socket's data printed on a single line
       --inet-sockopt  show various inet socket options

   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|mptcp|udp|raw|unix|unix_dgram|unix_stream|unix_seqpacket|packet|packet_raw|packet_dgram|netlink|dccp|sctp|vsock_stream|vsock_dgram|tipc|xdp}[,QUERY]

   -D, --diag=FILE     Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state STATE-FILTER ] [ EXPRESSION ]
       STATE-FILTER := {all|connected|synchronized|bucket|big|TCP-STATES}
         TCP-STATES := {established|syn-sent|syn-recv|fin-wait-{1,2}|time-wait|closed|close-wait|last-ack|listening|closing}
          connected := {established|syn-sent|syn-recv|fin-wait-{1,2}|time-wait|close-wait|last-ack|closing}
       synchronized := {established|syn-recv|fin-wait-{1,2}|time-wait|close-wait|last-ack|closing}
             bucket := {syn-recv|time-wait}
                big := {established|syn-sent|fin-wait-{1,2}|closed|close-wait|last-ack|listening|closing}
bandit16@bandit:~$ netstat --help
usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -i | [-cnNe] -M | -s [-6tuw] }

        -r, --route              display routing table
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets

  <Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-S|--sctp} {-w|--raw}
           {-x|--unix} --ax25 --ipx --netrom
  <AF>=Use '-6|-4' or '-A <af>' or '--<af>'; default: inet
  List of possible address families (which support routing):
    inet (DARPA Internet) inet6 (IPv6) ax25 (AMPR AX.25) 
    netrom (AMPR NET/ROM) rose (AMPR ROSE) ipx (Novell IPX) 
    ddp (Appletalk DDP) x25 (CCITT X.25) 
bandit16@bandit:~$ netstat -lv
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
netstat: no support for `AF INET (tcp)' on this system.
tcp6       0      0 [::]:31046              [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
tcp6       0      0 [::]:2230               [::]:*                  LISTEN     
tcp6       0      0 [::]:2231               [::]:*                  LISTEN     
tcp6       0      0 [::]:2232               [::]:*                  LISTEN     
tcp6       0      0 [::]:2220               [::]:*                  LISTEN     
tcp6       0      0 [::]:31691              [::]:*                  LISTEN     
tcp6       0      0 [::]:31960              [::]:*                  LISTEN     
netstat: no support for `AF INET (sctp)' on this system.
netstat: no support for `AF INET (udp)' on this system.
udp6       0      0 ip6-localhost:323       [::]:*                             
netstat: no support for `AF INET (raw)' on this system.
raw6       0      0 [::]:ipv6-icmp          [::]:*                  7          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
netstat: no support for `AF UNIX' on this system.
netstat: no support for `AF IPX' on this system.
netstat: no support for `AF AX25' on this system.
netstat: no support for `AF X25' on this system.
netstat: no support for `AF NETROM' on this system.
netstat: no support for `AF ROSE' on this system.
bandit16@bandit:~$ ss --help
Usage: ss [ OPTIONS ]
       ss [ OPTIONS ] [ FILTER ]
   -h, --help          this message
   -V, --version       output version information
   -n, --numeric       don't resolve service names
   -r, --resolve       resolve host names
   -a, --all           display all sockets
   -l, --listening     display listening sockets
   -o, --options       show timer information
   -e, --extended      show detailed socket information
   -m, --memory        show socket memory usage
   -p, --processes     show process using socket
   -T, --threads       show thread using socket
   -i, --info          show internal TCP information
       --tipcinfo      show internal tipc socket information
   -s, --summary       show socket usage summary
       --tos           show tos and priority information
       --cgroup        show cgroup information
   -b, --bpf           show bpf filter socket information
   -E, --events        continually display sockets as they are destroyed
   -Z, --context       display task SELinux security contexts
   -z, --contexts      display task and socket SELinux security contexts
   -N, --net           switch to the specified network namespace name

   -4, --ipv4          display only IP version 4 sockets
   -6, --ipv6          display only IP version 6 sockets
   -0, --packet        display PACKET sockets
   -t, --tcp           display only TCP sockets
   -M, --mptcp         display only MPTCP sockets
   -S, --sctp          display only SCTP sockets
   -u, --udp           display only UDP sockets
   -d, --dccp          display only DCCP sockets
   -w, --raw           display only RAW sockets
   -x, --unix          display only Unix domain sockets
       --tipc          display only TIPC sockets
       --vsock         display only vsock sockets
       --xdp           display only XDP sockets
   -f, --family=FAMILY display sockets of type FAMILY
       FAMILY := {inet|inet6|link|unix|netlink|vsock|tipc|xdp|help}

   -K, --kill          forcibly close sockets, display what was closed
   -H, --no-header     Suppress header line
   -O, --oneline       socket's data printed on a single line
       --inet-sockopt  show various inet socket options

   -A, --query=QUERY, --socket=QUERY
       QUERY := {all|inet|tcp|mptcp|udp|raw|unix|unix_dgram|unix_stream|unix_seqpacket|packet|packet_raw|packet_dgram|netlink|dccp|sctp|vsock_stream|vsock_dgram|tipc|xdp}[,QUERY]

   -D, --diag=FILE     Dump raw information about TCP sockets to FILE
   -F, --filter=FILE   read filter information from FILE
       FILTER := [ state STATE-FILTER ] [ EXPRESSION ]
       STATE-FILTER := {all|connected|synchronized|bucket|big|TCP-STATES}
         TCP-STATES := {established|syn-sent|syn-recv|fin-wait-{1,2}|time-wait|closed|close-wait|last-ack|listening|closing}
          connected := {established|syn-sent|syn-recv|fin-wait-{1,2}|time-wait|close-wait|last-ack|closing}
       synchronized := {established|syn-recv|fin-wait-{1,2}|time-wait|close-wait|last-ack|closing}
             bucket := {syn-recv|time-wait}
                big := {established|syn-sent|fin-wait-{1,2}|closed|close-wait|last-ack|listening|closing}
bandit16@bandit:~$ openssl s_client localhost:31518
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: D4689855BDD4D61AC4C8EFEA70C5DDAD304E225E408C909BBD0B9E9B6554307A
    Session-ID-ctx: 
    Resumption PSK: 272C066F5D6F8722D53D5150DBA6090D2D6FDB430643658001EEE36DD1296A69E3A890941A8A20FE63CD05D480CA7EC0
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - b5 fb 85 f8 a5 d6 9d 31-2c df ae bd 17 e8 30 dd   .......1,.....0.
    0020 - ea bc 3f 2e 75 5a d9 c7-d6 cb 4c 8a e2 ff eb 0d   ..?.uZ....L.....
    0030 - 5b 96 56 3a b9 8e c5 50-16 65 ff ef ce ea 28 08   [.V:...P.e....(.
    0040 - 25 a5 33 fd e0 9c 31 6a-27 f3 00 5e 3b a8 bf aa   %.3...1j'..^;...
    0050 - fc 39 ec 6c 9b 08 dd b9-d0 50 f4 ea dd 95 b6 f4   .9.l.....P......
    0060 - 5c 87 05 64 da 36 bd 37-bf da 31 3b ac f0 98 51   \..d.6.7..1;...Q
    0070 - d4 47 e0 e3 ef 8e fe 6e-d9 1d 84 93 18 ad 2a ee   .G.....n......*.
    0080 - 46 6b fb 55 71 e5 e7 fb-f4 82 7e 29 44 5d 53 7e   Fk.Uq.....~)D]S~
    0090 - 1b 00 06 d5 08 db d3 09-be bf cd 90 2d 32 29 4e   ............-2)N
    00a0 - 1a 06 7c c2 ba 67 a8 b5-0f 72 09 01 40 a2 01 ac   ..|..g...r..@...
    00b0 - 0a 0d 1a e8 d5 5d b0 26-6e 9d 06 87 66 cd 9e 43   .....].&n...f..C
    00c0 - b5 d5 d5 88 1d 0c b5 59-24 c1 c1 2e 97 b7 5d ea   .......Y$.....].
    00d0 - 4c f2 57 78 75 ad d1 e2-f6 5a 3f 8f 08 2c 0a 13   L.Wxu....Z?..,..

    Start Time: 1719934999
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 067C9D1C06F0D7F6444C4B6DA3103F79187A191EA09BAD3462139153AE2AF455
    Session-ID-ctx: 
    Resumption PSK: CA22EC6CEF6358672D89003D668ED7215F22169BB051222C6CE4E5ED3159AA1A3AF0438D103E54908E71CD2104ADD476
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - 21 93 18 08 69 67 fc 07-ed 20 f3 68 97 73 0a 7d   !...ig... .h.s.}
    0020 - 51 d7 83 9b 90 b9 89 5f-89 c9 4e a2 56 2e 0b 5a   Q......_..N.V..Z
    0030 - 6d b1 4a 60 9c 35 4b b2-f8 ac 88 7f d7 7b 9e 7a   m.J`.5K......{.z
    0040 - 28 89 8c 20 bd 78 c9 84-de 9b 40 06 15 6c bc fb   (.. .x....@..l..
    0050 - a3 8b 7d d1 79 dc de 4c-bc 21 b7 94 40 c1 e1 c7   ..}.y..L.!..@...
    0060 - 04 69 72 23 84 23 b6 ca-5b 24 d0 e7 f4 6e a3 9d   .ir#.#..[$...n..
    0070 - aa 8f 44 fc 3d 56 3d 11-3a c6 e4 74 6a fd 3f 96   ..D.=V=.:..tj.?.
    0080 - a4 60 1f 67 4c c5 e3 31-8f 1f 84 e1 41 1f ca e3   .`.gL..1....A...
    0090 - 14 0a e5 c9 9a 21 13 ec-a5 e7 72 8c 58 f4 07 d9   .....!....r.X...
    00a0 - c1 9c 84 c0 ec 6c 80 84-4b 85 e1 6c c0 5b 17 45   .....l..K..l.[.E
    00b0 - 2f 0a 96 69 89 01 f0 76-85 79 37 52 3d 46 2f 86   /..i...v.y7R=F/.
    00c0 - d8 8f cb 90 bc be 6e f3-fe fa e5 26 52 f7 d7 0c   ......n....&R...
    00d0 - df 2a 08 9c 01 5b e5 98-ca 3f d0 dd f3 65 1a d2   .*...[...?...e..

    Start Time: 1719934999
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
closed
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: A26A618FDC9B470927911539D6A60428896416A923FFD407CB3A94AF96525C72
    Session-ID-ctx: 
    Resumption PSK: 372091E05710F3979A0FA225619639944A29A87637C58363B4FE5875C63F2B5449ED0185F9C6EA8A84B9D7A5523681B9
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - d3 7a fe 71 16 1f c1 72-76 04 a5 26 da f7 f3 85   .z.q...rv..&....
    0020 - 0e e5 ad 9a b6 6c 7a ed-f0 1a e7 e5 dd ff 91 6a   .....lz........j
    0030 - 06 51 eb 9b 0e ab 34 25-11 81 85 68 7b 47 d1 64   .Q....4%...h{G.d
    0040 - 00 c5 27 38 6f 28 e9 5c-46 ee b3 8c ab de 91 4c   ..'8o(.\F......L
    0050 - 69 ad c6 89 f5 f4 e9 7e-4f d2 ce 51 d2 46 81 08   i......~O..Q.F..
    0060 - 3f a5 33 62 8a fd 95 aa-8e 26 66 42 af 10 3c 9d   ?.3b.....&fB..<.
    0070 - 01 a6 6e 30 e7 33 cc 01-c3 70 e9 02 c7 5d 55 96   ..n0.3...p...]U.
    0080 - 2e d8 b2 e0 c5 fd d4 d6-ea 08 99 da c3 be dc 34   ...............4
    0090 - cf 42 30 b2 ca 62 b2 21-a9 98 a0 f7 39 77 c1 5c   .B0..b.!....9w.\
    00a0 - 5f 5d b6 00 95 d2 1d e2-37 32 ae ba 54 c9 7b f4   _]......72..T.{.
    00b0 - 7e 1e 8e 29 e3 d2 1f da-f1 d5 d2 bf a2 e6 2d cc   ~..)..........-.
    00c0 - a6 8a b0 dc a0 b1 ac 5d-e1 46 3e a7 e0 e7 fe 75   .......].F>....u
    00d0 - f1 7b 2f a0 f7 de 0d 31-96 39 78 ed 75 85 ca 44   .{/....1.9x.u..D

    Start Time: 1719935025
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 26873BA417FB0D3F7128FB3BDA609CEBA520B978CD909A70D5E0EC71CA2A3232
    Session-ID-ctx: 
    Resumption PSK: F76B7ADDF8C257862D9142405576305721E04DDF9555AC1B06F5911D6DA6BF80B43170956F663A28490AF53AC7251AC8
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 06 d4 b3 35 03 37 fa bc-7e 5c 0a bd a4 45 eb 54   ...5.7..~\...E.T
    0020 - 6d 60 6c ae 97 a4 12 8e-17 dc 9d 6e 4c 8f 02 39   m`l........nL..9
    0030 - 8b 11 91 a9 82 f2 28 02-38 87 8c c1 0c 0b b4 84   ......(.8.......
    0040 - 8c 91 36 e9 4f 9c 39 ca-e4 b0 48 fe 50 43 6a 9f   ..6.O.9...H.PCj.
    0050 - 1f 23 c0 ad 60 ca de db-0d 3d f8 58 3a 5b 35 32   .#..`....=.X:[52
    0060 - 0d 9b f7 a4 11 7f 31 62-f4 03 a8 a1 52 97 51 4c   ......1b....R.QL
    0070 - d0 20 b3 d4 c3 3f 71 27-f3 fc ee 8f 10 ba ed d3   . ...?q'........
    0080 - 6d 55 a8 17 66 5c d2 5b-d8 0b 1d 9a 4d 2f 0f 2f   mU..f\.[....M/./
    0090 - d8 04 4a 01 2f 91 f6 47-f8 43 d4 e0 e5 bb 1c c5   ..J./..G.C......
    00a0 - 26 72 53 6a 9a d7 2f 9a-ae 6e c5 b2 4b 37 bd 93   &rSj../..n..K7..
    00b0 - 6e 00 20 36 aa 4f 98 2e-b0 8a 6f 07 1a 27 92 bc   n. 6.O....o..'..
    00c0 - 1d af dc 30 1f ff c4 54-17 26 e8 ac 90 ae e8 00   ...0...T.&......
    00d0 - 0d ef 28 0e f2 39 36 f1-6f 15 25 ed 66 dd f6 b8   ..(..96.o.%.f...

    Start Time: 1719935025
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
^C
bandit16@bandit:~$ openssl s_client localhost:31046
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client localhost:31691
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client localhost:31960
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client localhost:31518
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E1B89AAA71E19C908DBCED2F67EB42986DFFDE1B398269F5E7CB65ACE65BE65E
    Session-ID-ctx: 
    Resumption PSK: 6F05139A769D60DD6DAED9A09DE421818AEB5180D768419FBC8ED8EFC8ECDD62020B512991A3C89B8B82AB6A50E4E270
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - 6c a2 c0 5a 92 12 da 2c-82 07 2d d9 d7 ff ba 75   l..Z...,..-....u
    0020 - 46 c2 15 5d 82 06 73 49-7e d7 ae 9d 43 a7 5c 28   F..]..sI~...C.\(
    0030 - 4a c5 b4 91 55 09 75 3e-dd e7 10 99 cf 5c d3 d9   J...U.u>.....\..
    0040 - 77 b6 89 03 9b fb 06 a8-b3 0d d9 9a a4 7b f1 c9   w............{..
    0050 - 33 a1 94 2a c0 1a f3 f4-03 71 a0 09 e6 03 d4 93   3..*.....q......
    0060 - 55 bf aa 6a 7b 4a ba 92-05 3d 05 8a 66 3e 60 cf   U..j{J...=..f>`.
    0070 - e7 10 c7 e7 53 74 de 27-00 15 0c fc 79 bc db 72   ....St.'....y..r
    0080 - 85 ba ad 8a 73 4c 7d 88-92 04 7e a6 78 4a 81 8c   ....sL}...~.xJ..
    0090 - 3c 14 96 61 96 41 84 c6-9d ab 7b 1e ad 48 c1 75   <..a.A....{..H.u
    00a0 - a0 04 5e db d1 c3 f0 e7-af ab f8 5d b2 f4 ed e4   ..^........]....
    00b0 - 80 8b 01 9c 20 4f 72 9b-ff c8 37 df 94 e9 80 0e   .... Or...7.....
    00c0 - 6b 7c 94 0e bc a5 16 c1-95 2c ed f4 e9 72 d6 42   k|.......,...r.B
    00d0 - d0 23 07 c3 38 5f 1b a7-40 1a c7 ab cf ff 9f d7   .#..8_..@.......

    Start Time: 1719935092
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B3700876C18CB5BD90200A675C61C4269464B9617069522F3D7141556DD99719
    Session-ID-ctx: 
    Resumption PSK: DAAFD0FE87A3DBF59E0F17533B4795CED907094D23320319612BF8A9161E1A00359E76D910A9F1E405401D7DC19EEFBF
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - 84 22 1b 4f 0f 6f 02 b7-88 25 69 90 b9 4c 69 fe   .".O.o...%i..Li.
    0020 - 3c ef 6c 9d f9 a0 79 6e-43 bd d9 d0 09 6c a0 56   <.l...ynC....l.V
    0030 - 6e 52 4a be 55 14 52 1b-ab f3 ea 54 97 02 f8 3d   nRJ.U.R....T...=
    0040 - af 28 1d 62 a9 e5 dc 87-7c a2 ad 15 2e ad 19 7a   .(.b....|......z
    0050 - df db ac 15 41 09 97 da-d8 6a 97 22 5e a9 f5 a3   ....A....j."^...
    0060 - f9 1c 80 56 e4 a5 7b e1-b1 83 6c 81 99 f5 a8 a7   ...V..{...l.....
    0070 - 20 1a d5 81 3c b4 01 37-71 f5 5d 68 96 af 87 21    ...<..7q.]h...!
    0080 - cc 17 25 c1 cf 6c ce 14-d7 0a c7 83 58 e9 63 5d   ..%..l......X.c]
    0090 - f5 53 8c 1b 93 6f 1e 95-f5 11 9c 0f 8f a5 3a dd   .S...o........:.
    00a0 - 73 d3 0f ab b5 f9 38 b8-a3 0f 32 4d d3 a8 d2 40   s.....8...2M...@
    00b0 - 40 30 4d 7e 6c 5d cf f5-4f d0 69 1e d1 20 b5 82   @0M~l]..O.i.. ..
    00c0 - 0f 5f 53 10 11 14 71 8c-65 0a 43 75 6c a4 78 14   ._S...q.e.Cul.x.
    00d0 - d6 1e e0 c6 23 94 55 d9-02 b7 a8 eb 62 f7 cf ac   ....#.U.....b...

    Start Time: 1719935092
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
closed
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E5A00B0885CA07A16D7E7E4C8951326898BF4DF13F6819000269A555224A7654
    Session-ID-ctx: 
    Resumption PSK: B76E2C93CB92DED7725EAC3F907520AEC83446E03C5C31047177AD9DDAEEA6530645E9531A5A620D3772B5D347E56C35
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - f1 46 97 d2 88 1b 26 38-c8 11 81 ae 4b 7d ac 1b   .F....&8....K}..
    0020 - fe 50 c7 dc f4 79 3d 3a-b6 b0 15 97 e1 17 00 26   .P...y=:.......&
    0030 - 38 fc f7 92 9b 65 ca 03-15 b7 fc 74 05 08 c6 ec   8....e.....t....
    0040 - 01 34 40 62 95 b7 eb 0f-53 2a 8d 55 15 fd 7b 07   .4@b....S*.U..{.
    0050 - d2 bd 42 d1 97 2a 97 8a-11 cf ed ee 4d 1c 61 0c   ..B..*......M.a.
    0060 - 26 75 f0 b3 34 f5 5c 2f-6c 0b 05 7e a4 96 11 31   &u..4.\/l..~...1
    0070 - 80 3b ad 88 49 a5 77 c8-3c 8c e4 6d d9 24 99 ee   .;..I.w.<..m.$..
    0080 - 97 2f 80 0f d1 d9 74 1e-93 db f9 09 46 d7 34 84   ./....t.....F.4.
    0090 - 32 ff 40 ba 09 a7 b1 74-21 e2 7c e2 53 62 ab ae   2.@....t!.|.Sb..
    00a0 - 6f 16 12 ab c3 52 f7 63-13 ee 5f 41 09 97 3b 2d   o....R.c.._A..;-
    00b0 - b4 15 43 71 eb 95 ac cf-79 f8 b6 bb be e3 be e4   ..Cq....y.......
    00c0 - e6 da 67 6a 40 f1 7a fc-d3 4f cb 6e 84 73 05 86   ..gj@.z..O.n.s..
    00d0 - 4d 7c d2 c8 4d 80 69 41-e7 0f a5 21 40 fa 62 da   M|..M.iA...!@.b.

    Start Time: 1719935213
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E6A627C0BA797E6A3CA17B3AAC26A47B65B03C534A06F8A647C9668412AF32CE
    Session-ID-ctx: 
    Resumption PSK: E3B07283B72C29B46D9E163E4E6D340AC9FFD56C8A8F91B84AB0EB94F7835CFA3A92EB4270C89E8E1389DE774437CC8D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 94 70 bf 95 c0 95 d3 aa-91 99 85 aa d9 9f 79 8c   .p............y.
    0020 - 82 03 a0 f3 72 b9 02 63-38 9b 6d c2 24 47 e5 be   ....r..c8.m.$G..
    0030 - 5e 43 75 cb 88 d3 e7 df-26 aa ba 32 1c 88 16 75   ^Cu.....&..2...u
    0040 - 09 a9 1f 55 e0 70 74 c2-ee 49 71 23 59 4d 8a 48   ...U.pt..Iq#YM.H
    0050 - 09 40 15 1e a9 a2 07 6e-ba e2 f2 32 a0 ae a9 5b   .@.....n...2...[
    0060 - dc 5f 49 c5 76 0e dd cc-1f 42 db b0 55 45 fc c7   ._I.v....B..UE..
    0070 - 70 10 6d a4 0e 9a 01 15-b8 c4 a3 d3 28 b4 a0 3a   p.m.........(..:
    0080 - 23 e5 37 e2 de aa a8 e3-cf 76 76 7f 74 06 dd a4   #.7......vv.t...
    0090 - 12 ae 9c 2a 7d 25 a6 78-31 10 ac b7 ad 8e d2 bb   ...*}%.x1.......
    00a0 - ba d5 11 1b 59 dd 18 94-12 ff f2 a6 22 f3 32 94   ....Y.......".2.
    00b0 - e6 86 46 88 23 e8 c3 b4-cc b2 55 86 9a df 38 32   ..F.#.....U...82
    00c0 - d6 56 9f 18 a5 29 79 ab-63 29 e7 39 82 e2 c8 96   .V...)y.c).9....
    00d0 - 51 4f eb 2c a5 76 e4 47-85 30 61 b9 70 a0 c8 2f   QO.,.v.G.0a.p../

    Start Time: 1719935213
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
^C
bandit16@bandit:~$ telnet localhost 31046
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
test
test
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31691
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
test
test
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
test
test
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31691
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
^[[AConnection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31691^C
bandit16@bandit:~$ telnet localhost 31518
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31790
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Connection closed by foreign host.
bandit16@bandit:~$ nmap -p3100-3200 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:07 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00017s latency).
All 101 scanned ports on localhost (127.0.0.1) are in ignored states.
Not shown: 101 closed tcp ports (conn-refused)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.59 seconds
bandit16@bandit:~$ nmap -p31000-32000 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:08 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
|_    Wrong! Please enter the correct current password.
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.94SVN%T=SSL%I=7%D=7/2%Time=66842601%P=x86_64-pc-linux
SF:-gnu%r(GenericLines,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\.\n")%r(GetRequest,32,"Wrong!\x20Please\x20enter\x2
SF:0the\x20correct\x20current\x20password\.\n")%r(HTTPOptions,32,"Wrong!\x
SF:20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%r(RTSP
SF:Request,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20p
SF:assword\.\n")%r(Help,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x2
SF:0current\x20password\.\n")%r(FourOhFourRequest,32,"Wrong!\x20Please\x20
SF:enter\x20the\x20correct\x20current\x20password\.\n")%r(LPDString,32,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%
SF:r(SIPOptions,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current
SF:\x20password\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.83 seconds
bandit16@bandit:~$ openssl s_client localhost:31960
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client --help
Usage: s_client [options] [host:port]

General options:
 -help                      Display this summary
 -engine val                Use engine, possibly a hardware device
 -ssl_client_engine val     Specify engine to be used for client certificate operations
 -ssl_config val            Use specified section for SSL_CTX configuration
 -ct                        Request and parse SCTs (also enables OCSP stapling)
 -noct                      Do not request or parse SCTs (default)
 -ctlogfile infile          CT log list CONF file

Network options:
 -host val                  Use -connect instead
 -port +int                 Use -connect instead
 -connect val               TCP/IP where to connect; default: 4433)
 -bind val                  bind local address for connection
 -proxy val                 Connect to via specified proxy to the real server
 -proxy_user val            UserID for proxy authentication
 -proxy_pass val            Proxy authentication password source
 -unix val                  Connect over the specified Unix-domain socket
 -4                         Use IPv4 only
 -6                         Use IPv6 only
 -maxfraglen +int           Enable Maximum Fragment Length Negotiation (len values: 512, 1024, 2048 and 4096)
 -max_send_frag +int        Maximum Size of send frames 
 -split_send_frag +int      Size used to split data for encrypt pipelines
 -max_pipelines +int        Maximum number of encrypt/decrypt pipelines to be used
 -read_buf +int             Default read buffer size to be used for connections
 -fallback_scsv             Send the fallback SCSV

Identity options:
 -cert infile               Client certificate file to use
 -certform PEM|DER          Client certificate file format (PEM/DER/P12); has no effect
 -cert_chain infile         Client certificate chain file (in PEM format)
 -build_chain               Build client certificate chain
 -key val                   Private key file to use; default: -cert file
 -keyform PEM|DER|ENGINE    Key format (ENGINE, other values ignored)
 -pass val                  Private key and cert file pass phrase source
 -verify +int               Turn on peer certificate verification
 -nameopt val               Certificate subject/issuer name printing options
 -CApath dir                PEM format directory of CA's
 -CAfile infile             PEM format file of CA's
 -CAstore uri               URI to store of CA's
 -no-CAfile                 Do not load the default certificates file
 -no-CApath                 Do not load certificates from the default certificates directory
 -no-CAstore                Do not load certificates from the default certificates store
 -requestCAfile infile      PEM format file of CA names to send to the server
 -dane_tlsa_domain val      DANE TLSA base domain
 -dane_tlsa_rrdata val      DANE TLSA rrdata presentation form
 -dane_ee_no_namechecks     Disable name checks when matching DANE-EE(3) TLSA records
 -psk_identity val          PSK identity
 -psk val                   PSK in hex (without 0x)
 -psk_session infile        File to read PSK SSL session from
 -name val                  Hostname to use for "-starttls lmtp", "-starttls smtp" or "-starttls xmpp[-server]"

Session options:
 -reconnect                 Drop and re-make the connection with the same Session-ID
 -sess_out outfile          File to write SSL session to
 -sess_in infile            File to read SSL session from

Input/Output options:
 -crlf                      Convert LF from terminal into CRLF
 -quiet                     No s_client output
 -ign_eof                   Ignore input eof (default when -quiet)
 -no_ign_eof                Don't ignore input eof
 -starttls val              Use the appropriate STARTTLS command before starting TLS
 -xmpphost val              Alias of -name option for "-starttls xmpp[-server]"
 -brief                     Restrict output to brief summary of connection parameters
 -prexit                    Print session information when the program exits

Debug options:
 -showcerts                 Show all certificates sent by the server
 -debug                     Extra output
 -msg                       Show protocol messages
 -msgfile outfile           File to send output of -msg or -trace, instead of stdout
 -nbio_test                 More ssl protocol testing
 -state                     Print the ssl states
 -keymatexport val          Export keying material using label
 -keymatexportlen +int      Export len bytes of keying material; default 20
 -security_debug            Enable security debug messages
 -security_debug_verbose    Output more security debug output
 -trace                     Show trace output of protocol messages
 -keylogfile outfile        Write TLS secrets to file
 -nocommands                Do not use interactive command letters
 -servername val            Set TLS extension servername (SNI) in ClientHello (default)
 -noservername              Do not send the server name (SNI) extension in the ClientHello
 -tlsextdebug               Hex dump of all TLS extensions received
 -ignore_unexpected_eof     Do not treat lack of close_notify from a peer as an error
 -status                    Request certificate status from server
 -serverinfo val            types  Send empty ClientHello extensions (comma-separated numbers)
 -alpn val                  Enable ALPN extension, considering named protocols supported (comma-separated list)
 -async                     Support asynchronous operation
 -nbio                      Use non-blocking IO

Protocol and version options:
 -tls1                      Just use TLSv1
 -tls1_1                    Just use TLSv1.1
 -tls1_2                    Just use TLSv1.2
 -tls1_3                    Just use TLSv1.3
 -dtls                      Use any version of DTLS
 -timeout                   Enable send/receive timeout on DTLS connections
 -mtu +int                  Set the link layer MTU
 -dtls1                     Just use DTLSv1
 -dtls1_2                   Just use DTLSv1.2
 -nextprotoneg val          Enable NPN extension, considering named protocols supported (comma-separated list)
 -early_data infile         File to send as early data
 -enable_pha                Enable post-handshake-authentication
 -use_srtp val              Offer SRTP key management with a colon-separated profile list
 -srpuser val               (deprecated) SRP authentication for 'user'
 -srppass val               (deprecated) Password for 'user'
 -srp_lateuser              (deprecated) SRP username into second ClientHello message
 -srp_moregroups            (deprecated) Tolerate other than the known g N values.
 -srp_strength +int         (deprecated) Minimal length in bits for N

Random state options:
 -rand val                  Load the given file(s) into the random number generator
 -writerand outfile         Write random data to the specified file

TLS/SSL options:
 -no_ssl3                   Just disable SSLv3
 -no_tls1                   Just disable TLSv1
 -no_tls1_1                 Just disable TLSv1.1
 -no_tls1_2                 Just disable TLSv1.2
 -no_tls1_3                 Just disable TLSv1.3
 -bugs                      Turn on SSL bug compatibility
 -no_comp                   Disable SSL/TLS compression (default)
 -comp                      Use SSL/TLS-level compression
 -no_ticket                 Disable use of TLS session tickets
 -serverpref                Use server's cipher preferences
 -legacy_renegotiation      Enable use of legacy renegotiation (dangerous)
 -client_renegotiation      Allow client-initiated renegotiation
 -no_renegotiation          Disable all renegotiation.
 -legacy_server_connect     Allow initial connection to servers that don't support RI
 -no_resumption_on_reneg    Disallow session resumption on renegotiation
 -no_legacy_server_connect  Disallow initial connection to servers that don't support RI
 -allow_no_dhe_kex          In TLSv1.3 allow non-(ec)dhe based key exchange on resumption
 -prioritize_chacha         Prioritize ChaCha ciphers when preferred by clients
 -strict                    Enforce strict certificate checks as per TLS standard
 -sigalgs val               Signature algorithms to support (colon-separated list)
 -client_sigalgs val        Signature algorithms to support for client certificate authentication (colon-separated list)
 -groups val                Groups to advertise (colon-separated list)
 -curves val                Groups to advertise (colon-separated list)
 -named_curve val           Elliptic curve used for ECDHE (server-side only)
 -cipher val                Specify TLSv1.2 and below cipher list to be used
 -ciphersuites val          Specify TLSv1.3 ciphersuites to be used
 -min_protocol val          Specify the minimum protocol version to be used
 -max_protocol val          Specify the maximum protocol version to be used
 -record_padding val        Block size to pad TLS 1.3 records to.
 -debug_broken_protocol     Perform all sorts of protocol violations for testing purposes
 -no_middlebox              Disable TLSv1.3 middlebox compat mode
 -no_etm                    Disable Encrypt-then-Mac extension

Validation options:
 -policy val                adds policy to the acceptable policy set
 -purpose val               certificate chain purpose
 -verify_name val           verification policy name
 -verify_depth int          chain depth limit
 -auth_level int            chain authentication security level
 -attime intmax             verification epoch time
 -verify_hostname val       expected peer hostname
 -verify_email val          expected peer email
 -verify_ip val             expected peer IP address
 -ignore_critical           permit unhandled critical extensions
 -issuer_checks             (deprecated)
 -crl_check                 check leaf certificate revocation
 -crl_check_all             check full chain revocation
 -policy_check              perform rfc5280 policy checks
 -explicit_policy           set policy variable require-explicit-policy
 -inhibit_any               set policy variable inhibit-any-policy
 -inhibit_map               set policy variable inhibit-policy-mapping
 -x509_strict               disable certificate compatibility work-arounds
 -extended_crl              enable extended CRL features
 -use_deltas                use delta CRLs
 -policy_print              print policy processing diagnostics
 -check_ss_sig              check root CA self-signatures
 -trusted_first             search trust store first (default)
 -suiteB_128_only           Suite B 128-bit-only mode
 -suiteB_128                Suite B 128-bit mode allowing 192-bit algorithms
 -suiteB_192                Suite B 192-bit-only mode
 -partial_chain             accept chains anchored by intermediate trust-store CAs
 -no_alt_chains             (deprecated)
 -no_check_time             ignore certificate validity time
 -allow_proxy_certs         allow the use of proxy certificates
 -CRL infile                CRL file to use
 -crl_download              Download CRL from distribution points
 -CRLform PEM|DER           CRL format (PEM or DER); default PEM
 -verify_return_error       Close connection on verification error
 -verify_quiet              Restrict verify output to errors
 -chainCAfile infile        CA file for certificate chain (PEM format)
 -chainCApath dir           Use dir as certificate store path to build CA certificate chain
 -chainCAstore uri          CA store URI for certificate chain
 -verifyCAfile infile       CA file for certificate verification (PEM format)
 -verifyCApath dir          Use dir as certificate store path to verify CA certificate
 -verifyCAstore uri         CA store URI for certificate verification

Extended certificate options:
 -xkey infile               key for Extended certificates
 -xcert infile              cert for Extended certificates
 -xchain infile             chain for Extended certificates
 -xchain_build              build certificate chain for the extended certificates
 -xcertform PEM|DER         format of Extended certificate (PEM/DER/P12); has no effect
 -xkeyform PEM|DER          format of Extended certificate's key (DER/PEM/P12); has no effect

Provider options:
 -provider-path val         Provider load path (must be before 'provider' argument if required)
 -provider val              Provider to load (can be specified multiple times)
 -propquery val             Property query used when fetching algorithms

Parameters:
 host:port                  Where to connect; same as -connect option
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
bandit16@bandit:~$ nmap -p31000-32000 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:08 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
|_    Wrong! Please enter the correct current password.
31960/tcp open  echo
1 service unrecognized despite returning data. If youbandit16@bandit:~$ nmap -p31000-32000 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:08 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
 know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
SF-Port31790-TCP:V=7.94SVN%T=SSL%I=7%D=7| ssl-cert: Subject: commonName=SnakeOil
/2%Time=66842601%P=x86_64-pc-linux
SF:-gnu%r(GenericLines,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\.\n")%r(GetR| Not valid before: 2024-06-10T03:59:50
equest,32,"Wrong!\x20Please\x20enter\x2
SF:0the\x20correct\x20current\x20password\.\n")%r(HTTPOptions,32,"Wrong!\x
SF:20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%r(RTSP
SF:Request,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20p
SF:assword\.\n")%r(Help,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x2
SF:0current\x20password\.\n")%r(FourOhFourRequest,32,"Wrong!\x20Please\x20
SF:enter\x20the\x20correct\x20current\x20password\.\n")%r(LPDString,32,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%
SF:r(SIPOptions,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current
SF:\x20password\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.83 seconds
|_Not valid after:  2034-06-08T03:59:50
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
|_    Wrong! Please enter the correct current password.
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.94SVN%T=SSL%I=7%D=7/2%Time=66842601%P=x86_64-pc-linux
SF:-gnu%r(GenericLines,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\.\n")%r(GetRequest,32,"Wrong!\x20Please\x20enter\x2
SF:0the\x20correct\x20current\x20password\.\n")%r(HTTPOptions,32,"Wrong!\x
SF:20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%r(RTSP
SF:Request,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20p
SF:assword\.\n")%r(Help,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x2
SF:0current\x20password\.\n")%r(FourOhFourRequest,32,"Wrong!\x20Please\x20
SF:enter\x20the\x20correct\x20current\x20password\.\n")%r(LPDString,32,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%
SF:r(SIPOptions,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current
SF:\x20password\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.83 seconds
bandit16@bandit:~$ nmap -p31000-32000 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:08 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
|_    Wrong! Please enter the correct current password.
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.94SVN%T=SSL%I=7%D=7/2%Time=66842601%P=x86_64-pc-linux
SF:-gnu%r(GenericLines,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\.\n")%r(GetRequest,32,"Wrong!\x20Please\x20enter\x2
SF:0the\x20correct\x20current\x20password\.\n")%r(HTTPOptions,32,"Wrong!\x
SF:20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%r(RTSP
SF:Request,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20p
SF:assword\.\n")%r(Help,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x2
SF:0current\x20password\.\n")%r(FourOhFourRequest,32,"Wrong!\x20Please\x20
SF:enter\x20the\x20correct\x20current\x20password\.\n")%r(LPDString,32,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%
SF:r(SIPOptions,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current
SF:\x20password\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.83 seconds
bandit16@bandit:~$ nmap -p31000-32000 -sC -sV localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 16:08 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
|_ssl-date: TLS randomness does not represent time
31691/tcp open  echo
31790/tcp open  ssl/unknown
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=SnakeOil
| Not valid before: 2024-06-10T03:59:50
|_Not valid after:  2034-06-08T03:59:50
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, LPDString, RTSPRequest, SIPOptions: 
|_    Wrong! Please enter the correct current password.
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.94SVN%T=SSL%I=7%D=7/2%Time=66842601%P=x86_64-pc-linux
SF:-gnu%r(GenericLines,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20
SF:current\x20password\.\n")%r(GetRequest,32,"Wrong!\x20Please\x20enter\x2
SF:0the\x20correct\x20current\x20password\.\n")%r(HTTPOptions,32,"Wrong!\x
SF:20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%r(RTSP
SF:Request,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20p
SF:assword\.\n")%r(Help,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x2
SF:0current\x20password\.\n")%r(FourOhFourRequest,32,"Wrong!\x20Please\x20
SF:enter\x20the\x20correct\x20current\x20password\.\n")%r(LPDString,32,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\.\n")%
SF:r(SIPOptions,32,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current
SF:\x20password\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 156.83 seconds
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Connection closed by foreign host.
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31960
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
bandit16@bandit:~$ 
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31518
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31518
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31790
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31960
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dxbandit16@bandit:~$ 
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31046
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dxbandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | nc localhost 31691
kSkvUpMQ7lBYyCM4GBP
bandit16@bandit:~$ 
bandit16@bandit:~$ 
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | opensll s_client localhost:31960
Command 'opensll' not found, did you mean:
  command 'openssl' from deb openssl (3.0.10-1ubuntu3)
Try: apt install <deb name>
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client localhost:31960
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client localhost:31518
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 377098A4A2FA3E30431B225144D25B64ED202E4AE165E32803292C05664963D9
    Session-ID-ctx: 
    Resumption PSK: 06D4EB99FCD59EED8B30AD2833CBE8FA949E6CA24BEC51DCF314F9F46FC49F98A78FDEF03EE168996A3E99DA2C33E6B2
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - 2d 02 90 50 58 3d 8b 53-82 60 b5 7c bf 00 75 5e   -..PX=.S.`.|..u^
    0020 - 60 06 8f 6a 0b 61 04 f9-8b 9c f3 ef 55 54 d9 da   `..j.a......UT..
    0030 - 9f 3a 3f f6 12 29 79 36-9d cb 63 96 38 95 aa 1a   .:?..)y6..c.8...
    0040 - 31 42 f7 37 fc f9 ed 3e-cb 80 b7 94 aa e0 90 21   1B.7...>.......!
    0050 - 66 82 b4 4d 3c b7 14 5a-7f 02 0c 1a e8 d1 35 ef   f..M<..Z......5.
    0060 - 95 7d bd d1 2a 09 74 19-5f 0b 2d 1c 20 7a 91 35   .}..*.t._.-. z.5
    0070 - 6f f9 69 ed 12 59 d0 4f-0d 55 e3 d2 c6 ab 08 96   o.i..Y.O.U......
    0080 - 34 45 f4 b3 3a c3 c6 c3-c8 ae 44 e5 97 65 e3 98   4E..:.....D..e..
    0090 - 58 cb 4c 16 9a 86 05 8e-84 d1 3e 53 28 45 7f b0   X.L.......>S(E..
    00a0 - 07 2d 59 ff ac db 98 c8-38 34 de 6e 52 75 d8 10   .-Y.....84.nRu..
    00b0 - f7 68 69 7b 79 f3 22 e7-f2 96 9d f3 1a 02 52 ca   .hi{y.".......R.
    00c0 - 3a 3a f4 f4 07 7a 70 59-01 b0 bb 40 e9 0f a6 09   ::...zpY...@....
    00d0 - ef bc 6a ed c5 2c 9b 41-c5 cd bf 94 51 a2 a1 9d   ..j..,.A....Q...

    Start Time: 1719937855
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 954F3C51A7F87AC03222CDC947DD72F4049B92B83CBA6914327522BDFAA9EB23
    Session-ID-ctx: 
    Resumption PSK: 5C353444F8EB48B733144559C80E76A99D4E7B0110A6B9B18B3AF08FBD640DAB73FACEDBBB160178A0F52AF5B4B33372
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - cf ff 8d 17 aa 92 c3 f3-55 9b 6c be eb 30 b6 1d   ........U.l..0..
    0010 - 84 c7 2d 91 0c 71 68 dc-65 e3 c4 f9 20 0e 94 e2   ..-..qh.e... ...
    0020 - 8b 19 53 d3 87 4b ff e3-28 ec 45 57 ca cb 33 ae   ..S..K..(.EW..3.
    0030 - ce 63 3a 86 53 0f 45 07-83 22 ee b2 4b 2b 1f 4f   .c:.S.E.."..K+.O
    0040 - 8b 06 d7 d4 51 9b 5c 88-29 c5 20 12 3b e0 73 23   ....Q.\.). .;.s#
    0050 - f7 0e 38 43 95 a3 44 cc-e9 bf 73 ef 1c a0 11 c6   ..8C..D...s.....
    0060 - b7 e7 60 7c ac 58 5e 04-0a 65 20 53 99 8d 56 4d   ..`|.X^..e S..VM
    0070 - 37 4e de 1f 4c be 6d 4e-4c 67 13 59 94 0a b0 4a   7N..L.mNLg.Y...J
    0080 - 9a 3d 78 79 f3 67 77 a3-80 f6 8e 4b 46 3e 42 c6   .=xy.gw....KF>B.
    0090 - a1 6f a8 f7 9c b1 ed 07-29 13 a5 bd 58 b9 fe f5   .o......)...X...
    00a0 - 13 25 03 76 b5 a7 84 50-a0 9c 16 c8 39 9a 0b 89   .%.v...P....9...
    00b0 - b0 a8 e7 7d 27 c3 8a c0-f0 d1 1d 2a 8d 45 3a 42   ...}'......*.E:B
    00c0 - 3c f0 f4 fc 98 20 0f 6c-5d 81 55 c3 32 6a 0c 14   <.... .l].U.2j..
    00d0 - 24 59 58 65 02 7b 31 bc-a7 31 4e 1b 86 44 ae 40   $YXe.{1..1N..D.@

    Start Time: 1719937855
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
KEYUPDATE
DONE
bandit16@bandit:~$ echo -n "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
KEYUPDATE
DONE
bandit16@bandit:~$ openssl s_client localhost:31960
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client -connect localhost:31960
CONNECTED(00000003)
4087F0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ telnet localhost:31960
Server lookup failure:  localhost:31960:telnet, Name or service not known
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
test
test
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
Connection closed by foreign host.
bandit16@bandit:~$ telnet localhost 31960
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
help
help
^C

Connection closed by foreign host.
bandit16@bandit:~$ ls -la
total 24
drwxr-xr-x  2 root     root     4096 Jun 20 04:06 .
drwxr-xr-x 70 root     root     4096 Jun 20 04:08 ..
-rw-r-----  1 bandit16 bandit16   33 Jun 20 04:06 .bandit15.password
-rw-r--r--  1 root     root      220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root     root     3771 Mar 31 08:41 .bashrc
-rw-r--r--  1 root     root      807 Mar 31 08:41 .profile
bandit16@bandit:~$ cat /etc/bandit_pass/bandit16
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E8EE17A8C9042A391AE86BC1FFEEB8CD2BA82E2361E0C1C04DF2F4B7BCD309E1
    Session-ID-ctx: 
    Resumption PSK: 40EBB00E4BE634CEF6AB94A99DD395FD43DA2C60AC0DC4BF26A2A77B5671721BC2D66488BA4A023808398D2DBF6408F1
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 03 d7 04 b5 8d 2b e4 d5-ae 1b bc 50 a5 28 f8 5d   .....+.....P.(.]
    0020 - b2 75 2c ac af a7 51 5e-5f a9 ee 91 f6 60 83 14   .u,...Q^_....`..
    0030 - 81 05 d5 82 ad f9 ec 43-16 ba 66 72 5c 95 f4 ed   .......C..fr\...
    0040 - 6a b6 90 2f 3d f8 fb 9d-d8 7f 70 c4 7d ca 07 42   j../=.....p.}..B
    0050 - d8 ae 54 c7 74 b3 67 60-4d cf ec f1 18 38 b4 01   ..T.t.g`M....8..
    0060 - 93 1f 39 12 26 39 05 3f-56 a7 12 b7 73 a2 97 e9   ..9.&9.?V...s...
    0070 - b5 f2 e0 ba 72 f6 73 65-1d 02 ad b5 7b 09 90 09   ....r.se....{...
    0080 - 08 eb 1d 4f fc bc 74 0d-a0 d8 78 15 6e 4d 31 8a   ...O..t...x.nM1.
    0090 - 68 ab 8c c1 c1 f1 1b b3-aa 0c 4b 8c b3 be 85 aa   h.........K.....
    00a0 - db f3 79 f6 06 6a 14 49-67 f4 8b 10 01 0b ff e9   ..y..j.Ig.......
    00b0 - e1 b8 d2 ca 19 cf c4 8d-2e f5 ca 1c e7 49 1f a2   .............I..
    00c0 - 8a 68 95 4c a9 21 55 46-fb 6d a6 90 33 f0 45 29   .h.L.!UF.m..3.E)
    00d0 - a0 8f 76 61 2f eb df ce-2e c2 fa 5c cc 1e 83 b5   ..va/......\....

    Start Time: 1719939549
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 82512E01E0D788145D463060CFD6839F40A5EE4BE4C4570EF7CC3CCF4A9C50E4
    Session-ID-ctx: 
    Resumption PSK: 7D07470D55080A718340E933D59FED1A447B1B2FCD226DF9BAEE089F05E97B097E92B3EB71C8D6523C567355E6796EA2
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 07 8e 61 87 c7 65 d5 50-92 f1 68 3b ac bf af ad   ..a..e.P..h;....
    0020 - 49 da 69 1e e6 02 8b 73-a6 67 57 9c 6b 27 d9 6b   I.i....s.gW.k'.k
    0030 - 4b 2d 16 0a 49 b7 bd ed-f7 69 f4 a6 16 34 da d6   K-..I....i...4..
    0040 - e6 6a 8e 4d c7 3a 40 04-88 f1 81 4a 22 e4 dd ce   .j.M.:@....J"...
    0050 - a1 d8 5f ac 2d a7 83 54-ca b7 91 8b ae 7b 3c 11   .._.-..T.....{<.
    0060 - 2b 3b 9f a9 14 c5 1a ef-1d 3a e2 7b f6 82 8e 5c   +;.......:.{...\
    0070 - 2d 5e 21 2c ba dc 1c 62-dd 15 dc 36 43 03 12 27   -^!,...b...6C..'
    0080 - d2 c7 6a 59 0a 70 28 6e-70 27 53 18 5e 1c 02 a2   ..jY.p(np'S.^...
    0090 - 45 69 11 17 2e 40 80 44-79 42 41 0f 49 49 8e 78   Ei...@.DyBA.II.x
    00a0 - 33 ab 90 db 18 98 9b ed-a1 2f 8a a1 d1 86 63 7f   3......../....c.
    00b0 - 51 71 d9 8d 02 91 e6 ca-b4 8c 96 48 c9 71 c5 57   Qq.........H.q.W
    00c0 - 89 1b 7f 2a 75 f4 7c 54-7f b3 da 32 5d a0 f3 c2   ...*u.|T...2]...
    00d0 - ea 06 47 36 0b 5c 15 7f-66 4d c8 16 9f 2d 05 9a   ..G6.\..fM...-..

    Start Time: 1719939549
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
^C
bandit16@bandit:~$ nmap -sC --script=ssl-enum-ciphers -p31000-32000 localhost
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 17:07 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00016s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
| ssl-enum-ciphers: 
|   TLSv1.2: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (secp256r1) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (rsa 4096) - A
|     compressors: 
|       NULL
|     cipher preference: client
|     warnings: 
|       Key exchange (secp256r1) of lower strength than certificate key
|   TLSv1.3: 
|     ciphers: 
|       TLS_AKE_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_AKE_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_AKE_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
|     cipher preference: client
|_  least strength: A
31691/tcp open  unknown
31790/tcp open  unknown
| ssl-enum-ciphers: 
|   TLSv1.2: 
|     ciphers: 
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (secp256r1) - A
|       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (secp256r1) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_CCM_8 (rsa 4096) - A
|       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_128_GCM_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_ARIA_256_GCM_SHA384 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (rsa 4096) - A
|       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (rsa 4096) - A
|     compressors: 
|       NULL
|     cipher preference: client
|     warnings: 
|       Key exchange (secp256r1) of lower strength than certificate key
|   TLSv1.3: 
|     ciphers: 
|       TLS_AKE_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
|       TLS_AKE_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
|       TLS_AKE_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
|     cipher preference: client
|_  least strength: A
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.60 seconds
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 03996C4D55AC7660B47C7F3C0AA9BDE4C277E291325824760E5004C0DF5461BC
    Session-ID-ctx: 
    Resumption PSK: 72245829C854A83E540DE85E1F0F8D3D49B0040A2112BAED83A4EE3F358C076B3AA4FF52B1CD098E8DC924EE27B44474
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - b9 cc 55 02 89 a3 82 a1-1a 8a b8 67 4f 31 09 29   ..U........gO1.)
    0020 - 3a 45 6e 0f 50 56 27 89-31 ac 7e 18 24 81 e0 11   :En.PV'.1.~.$...
    0030 - 67 7b 78 6a aa 7b ab 67-85 ce 19 43 0a 62 37 d2   g{xj.{.g...C.b7.
    0040 - 43 da 10 bd e2 eb ae ba-07 d8 5a be df 95 5f 41   C.........Z..._A
    0050 - 87 fa c0 a9 9e 57 d9 54-54 81 5a 51 74 2f fd 62   .....W.TT.ZQt/.b
    0060 - 5b 23 9a bb 40 3a 7f 93-72 92 e1 96 9b 35 27 bd   [#..@:..r....5'.
    0070 - 25 4e 4b bb fe 19 cb dd-6c 82 ec 41 33 ec 60 47   %NK.....l..A3.`G
    0080 - 94 75 b7 d8 5f d5 12 52-7e c4 57 de a5 dd e0 f9   .u.._..R~.W.....
    0090 - 89 93 7d ee 84 55 d5 95-08 cf f3 07 ad 68 d7 ed   ..}..U.......h..
    00a0 - 80 0f 71 f9 2b c7 04 88-b7 22 56 d3 b1 d3 52 4d   ..q.+...."V...RM
    00b0 - e2 77 26 29 8e 96 9b 4e-51 2f fd 95 ef fe 0f 0c   .w&)...NQ/......
    00c0 - d0 32 13 cc 26 6a 99 a8-47 a0 e6 d4 11 f9 0e 1d   .2..&j..G.......
    00d0 - 33 79 9c b4 bf 29 a9 90-16 62 b0 99 b6 3a c6 99   3y...)...b...:..

    Start Time: 1719940288
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B7A286046B859DD6450341020FE4F25186D3544127C9C973B3D24508F6EFA22B
    Session-ID-ctx: 
    Resumption PSK: B36222AEF162407FBE27E78E09238477244FAB02DDF36EF44080642B74217799F095ED6DF73FA7B55608186663674738
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - d4 62 af 09 14 98 af 15-fe 0f 66 d5 45 0d dc 3b   .b........f.E..;
    0020 - 1e dc df 7a 21 f0 8b 34-33 62 be 13 0d c4 f2 b5   ...z!..43b......
    0030 - 66 a0 76 af 93 e5 80 f0-35 a7 f6 42 83 bd c7 8a   f.v.....5..B....
    0040 - 94 c0 0c 3b 83 34 58 41-8b 9b 56 d9 7a 8a f4 8b   ...;.4XA..V.z...
    0050 - 88 33 67 c2 65 23 fb 5c-b3 c5 fd 19 10 b4 20 b7   .3g.e#.\...... .
    0060 - 10 06 5e 10 6e b1 3e d8-ff 62 29 59 f2 7d 15 34   ..^.n.>..b)Y.}.4
    0070 - 53 29 92 b0 1b e9 be 72-42 48 a1 0f 9a c5 d9 f0   S).....rBH......
    0080 - 71 c3 e8 66 48 97 c0 49-d9 38 0e 6b b4 5f 30 cd   q..fH..I.8.k._0.
    0090 - 98 90 0c 47 b8 f4 e0 1f-b8 8d 2c 0a 36 78 0b 68   ...G......,.6x.h
    00a0 - c2 1c 02 70 ba cb b9 b9-08 15 e0 1b 4a 9f b5 94   ...p........J...
    00b0 - 76 11 57 c7 0c ba 09 c5-58 86 85 41 76 1e 01 c7   v.W.....X..Av...
    00c0 - aa 15 cd cb fc f4 d3 97-fc 2c 10 a4 3f 1e db 24   .........,..?..$
    00d0 - 17 10 10 7a b6 f8 06 6a-6c 99 17 9e 27 9a 01 a9   ...z...jl...'...

    Start Time: 1719940288
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
read:errno=104
timed out waiting for input: auto-logout                                                                                      
Connection to bandit.labs.overthewire.org closed.                                                                             
                                                                                                                              
┌──(kali㉿kali)-[~/otw/bandit]
└─$ ssh bandit16@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit16@bandit.labs.overthewire.org's password: 

      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to the #wargames channel on
discord or IRC.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ is disabled and to /proc
  restricted so that users cannot snoop on eachother. Files and directories
  with easily guessable or short names will be periodically deleted! The /tmp
  directory is regularly wiped.
  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few useful tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /opt/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /opt/pwndbg/
    * peda (https://github.com/longld/peda.git) in /opt/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /opt/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us on discord or IRC.

  Enjoy your stay!

bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: DF0DA45DA8E0DBB56902A9BBC3EC6F00CBC39F574FFE299727D05F1EE61EC528
    Session-ID-ctx: 
    Resumption PSK: 3861CDAFD43ABBCE6FD774BD4F40AB6942553BE128923991E227714E98F2C4264713965A58BD57B0993EC98024A3E685
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - a4 b8 ca 1e 17 b5 77 02-1c 24 20 f3 25 91 57 45   ......w..$ .%.WE
    0020 - 0b a4 60 62 45 d4 ca 0c-f9 49 af 17 89 23 43 19   ..`bE....I...#C.
    0030 - d0 2f ae 68 f0 3a 78 6a-6d 15 83 bc 4d 98 ce 49   ./.h.:xjm...M..I
    0040 - 78 c6 69 5b 69 ac 62 db-07 32 7b 99 a2 75 f1 68   x.i[i.b..2{..u.h
    0050 - 68 34 64 32 be 1e 15 47-06 6a 6a fe 9f 57 3e b5   h4d2...G.jj..W>.
    0060 - 3d 19 9e 41 7f 50 0f d3-97 db fd 8f 2f f5 35 b0   =..A.P....../.5.
    0070 - e5 4c 1e e2 a5 45 18 d0-5d 15 3a 96 37 47 9b 26   .L...E..].:.7G.&
    0080 - 5f a4 20 2e f3 cf a8 fd-cc 20 8c 05 66 f0 96 31   _. ...... ..f..1
    0090 - 88 83 a5 30 28 e1 11 3e-b0 b8 0d b5 d6 24 09 9c   ...0(..>.....$..
    00a0 - d8 59 97 d6 43 53 8a f9-64 21 f4 01 c4 b1 06 98   .Y..CS..d!......
    00b0 - a5 ad 90 d7 95 f7 0a cd-82 3e c1 07 ad 48 e7 24   .........>...H.$
    00c0 - 1d b7 83 dd ea dc 59 14-d3 c2 28 0a 12 39 72 35   ......Y...(..9r5
    00d0 - 12 80 a9 75 df 91 7f a1-62 bd 79 d5 cf d0 2b b4   ...u....b.y...+.

    Start Time: 1719995221
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: CD9F9E78535C9161534CCBF9D60B8126A102CAAFC8426AE4329D8325C6A805A9
    Session-ID-ctx: 
    Resumption PSK: AF985D87459C01D6AB7AFBC6AA55DF152E59DF94AFA3823EE6904673692737191E0F69AFA5F8D218F47BE4439B77A596
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 9d ff 38 04 9a 68 86 6e-a8 3c 3f 5f 11 80 c3 9b   ..8..h.n.<?_....
    0020 - b5 b7 86 34 db f0 33 d8-6b de e1 14 c1 bd e1 94   ...4..3.k.......
    0030 - 4e 1c a0 bd 75 c8 41 41-22 e6 f3 51 77 b1 82 f4   N...u.AA"..Qw...
    0040 - 2d b7 a6 ac 90 ea c3 aa-9c 63 1d a4 cd 57 08 0e   -........c...W..
    0050 - 0c f5 c0 6d 1e 48 f1 61-5c 05 9f 64 a0 76 fc 5c   ...m.H.a\..d.v.\
    0060 - aa 1e 59 95 e6 13 72 67-f3 27 d9 37 49 e3 1d b3   ..Y...rg.'.7I...
    0070 - ca 61 7a e3 41 6d a9 f9-8b bf bc d6 64 4b 19 ec   .az.Am......dK..
    0080 - 46 1d ac d0 3d 2b fa 56-13 ac a8 70 55 9f dc 5e   F...=+.V...pU..^
    0090 - 71 f8 54 6c bc 2a 62 1b-cb ab 2e 10 f8 20 f0 f2   q.Tl.*b...... ..
    00a0 - 7d 14 1c b0 27 09 42 46-17 d4 77 e9 11 d3 d9 68   }...'.BF..w....h
    00b0 - 1b 52 6e 37 37 43 6c bd-2c 42 7a c6 6c 61 e7 68   .Rn77Cl.,Bz.la.h
    00c0 - 31 05 68 71 d1 5f 06 05-50 1c 2d 2b 81 c9 b4 1e   1.hq._..P.-+....
    00d0 - 38 09 72 33 40 a1 6a b0-c5 22 ab 05 55 02 9b d0   8.r3@.j.."..U...

    Start Time: 1719995221
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
KEYUPDATE
read:errno=104
timed out waiting for input: auto-logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                                              
┌──(kali㉿kali)-[~/otw/bandit]
└─$ ssh bandit16@bandit.labs.overthewire.org -p 2220
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit16@bandit.labs.overthewire.org's password: 

      ,----..            ,----,          .---.
     /   /   \         ,/   .`|         /. ./|
    /   .     :      ,`   .'  :     .--'.  ' ;
   .   /   ;.  \   ;    ;     /    /__./ \ : |
  .   ;   /  ` ; .'___,/    ,' .--'.  '   \' .
  ;   |  ; \ ; | |    :     | /___/ \ |    ' '
  |   :  | ; | ' ;    |.';  ; ;   \  \;      :
  .   |  ' ' ' : `----'  |  |  \   ;  `      |
  '   ;  \; /  |     '   :  ;   .   \    .\  ;
   \   \  ',  /      |   |  '    \   \   ' \ |
    ;   :    /       '   :  |     :   '  |--"
     \   \ .'        ;   |.'       \   \ ;
  www. `---` ver     '---' he       '---" ire.org


Welcome to OverTheWire!

If you find any problems, please report them to the #wargames channel on
discord or IRC.

--[ Playing the games ]--

  This machine might hold several wargames.
  If you are playing "somegame", then:

    * USERNAMES are somegame0, somegame1, ...
    * Most LEVELS are stored in /somegame/.
    * PASSWORDS for each level are stored in /etc/somegame_pass/.

  Write-access to homedirectories is disabled. It is advised to create a
  working directory with a hard-to-guess name in /tmp/.  You can use the
  command "mktemp -d" in order to generate a random and hard to guess
  directory in /tmp/.  Read-access to both /tmp/ is disabled and to /proc
  restricted so that users cannot snoop on eachother. Files and directories
  with easily guessable or short names will be periodically deleted! The /tmp
  directory is regularly wiped.
  Please play nice:

    * don't leave orphan processes running
    * don't leave exploit-files laying around
    * don't annoy other players
    * don't post passwords or spoilers
    * again, DONT POST SPOILERS!
      This includes writeups of your solution on your blog or website!

--[ Tips ]--

  This machine has a 64bit processor and many security-features enabled
  by default, although ASLR has been switched off.  The following
  compiler flags might be interesting:

    -m32                    compile for 32bit
    -fno-stack-protector    disable ProPolice
    -Wl,-z,norelro          disable relro

  In addition, the execstack tool can be used to flag the stack as
  executable on ELF binaries.

  Finally, network-access is limited for most levels by a local
  firewall.

--[ Tools ]--

 For your convenience we have installed a few useful tools which you can find
 in the following locations:

    * gef (https://github.com/hugsy/gef) in /opt/gef/
    * pwndbg (https://github.com/pwndbg/pwndbg) in /opt/pwndbg/
    * peda (https://github.com/longld/peda.git) in /opt/peda/
    * gdbinit (https://github.com/gdbinit/Gdbinit) in /opt/gdbinit/
    * pwntools (https://github.com/Gallopsled/pwntools)
    * radare2 (http://www.radare.org/)

--[ More information ]--

  For more information regarding individual wargames, visit
  http://www.overthewire.org/wargames/

  For support, questions or comments, contact us on discord or IRC.

  Enjoy your stay!

bandit16@bandit:~$ KsKVuPmq7LbyYcm4gbpVcVt1bFwrY0dX
KsKVuPmq7LbyYcm4gbpVcVt1bFwrY0dX: command not found
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 71D48AEBFD75FE41AFA2AEDB31617D0985E7E45E56CE6AC68A3AC9A2E0903BD9
    Session-ID-ctx: 
    Resumption PSK: E6D085C1D1894E0D599CC8EE8D3AF32778F166002C73FBE53C47CCAF5BC4E7D65C013DE482B578D61CEEE4163EAC2C84
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 44 35 0d f8 80 75 0c 01-93 0c 7a 35 d6 bf 17 09   D5...u....z5....
    0020 - b7 1c 0d 77 9e 97 66 aa-6a fe 3e 53 5f 41 12 6c   ...w..f.j.>S_A.l
    0030 - fd 24 1f 83 2f 81 c2 f9-44 57 2a 59 ad 04 5e 24   .$../...DW*Y..^$
    0040 - 8f 03 5e b2 e4 0b ef d3-88 9e b8 c5 91 d9 6b 29   ..^...........k)
    0050 - 9b 32 b1 bc df 48 b0 7d-4e 6e 4e 9f 4a 83 d8 54   .2...H.}NnN.J..T
    0060 - f0 13 06 a9 69 ad d8 8a-b4 13 e7 d3 5b 98 92 e7   ....i.......[...
    0070 - 0f c5 29 88 02 3d 65 77-e9 43 a1 5d d0 67 f7 52   ..)..=ew.C.].g.R
    0080 - 20 e1 9c 51 4c 48 c3 44-7d 12 b1 bc 6f d7 dc 11    ..QLH.D}...o...
    0090 - b3 88 27 c7 d4 85 d4 b5-bc d3 86 52 fe e1 59 c6   ..'........R..Y.
    00a0 - 83 cd b7 6a a5 1f c3 40-82 2e 06 c9 e5 86 80 05   ...j...@........
    00b0 - d7 17 88 29 62 48 93 11-ca d6 f2 02 3f 8a 05 52   ...)bH......?..R
    00c0 - d7 01 80 cb 6f d0 d9 e8-33 ab 6b a9 3c 5c 06 7d   ....o...3.k.<\.}
    00d0 - b3 86 45 c6 e2 5e d5 94-08 03 8e 3a 14 6b 9f 8b   ..E..^.....:.k..

    Start Time: 1720089480
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: EBEEC6A0306ECBC1316A9344B7C904FDD1B5CD0C354F3BD832E13BDC93C6D6C5
    Session-ID-ctx: 
    Resumption PSK: D5DA7F2F16B0FCEAEF50636208FC41BDA10FEDF7C9C2EFA4A0026E13318070BB52822AB53237CF6747672DF2888D50F5
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - a3 7d b6 7f 0a 23 37 5e-3e 26 60 51 d5 20 2b 82   .}...#7^>&`Q. +.
    0020 - b0 1e f9 c9 d7 26 bc e3-93 3a 1d f4 57 5f 3f 4e   .....&...:..W_?N
    0030 - 40 64 37 4d b6 1d d4 a9-1c 4b b3 86 d4 de 82 0e   @d7M.....K......
    0040 - 64 89 04 ca 8b 58 17 b6-60 cd 1e c8 d3 a5 05 16   d....X..`.......
    0050 - 8b 98 8d 19 a8 f9 83 e9-07 13 06 8e e8 45 61 7f   .............Ea.
    0060 - 99 24 ff ab 99 06 27 ba-b0 aa 57 31 4a 07 00 a9   .$....'...W1J...
    0070 - f3 ad cd 50 d1 3a 4e b7-24 6e 4e fb 2f dd f2 22   ...P.:N.$nN./.."
    0080 - 9b f9 2c 7c b0 eb d2 de-c9 f5 c3 bc 1a c9 ec d6   ..,|............
    0090 - b8 7a df 3f 5a 40 fc 43-be a0 d6 e4 38 f4 a3 1f   .z.?Z@.C....8...
    00a0 - de c4 6e 6a 89 36 f0 92-26 83 0e 32 59 36 a9 9a   ..nj.6..&..2Y6..
    00b0 - 1b ec 48 03 92 e7 8c d6-55 41 9e 6f ee aa dc e5   ..H.....UA.o....
    00c0 - 2a 82 b5 af 73 c8 63 4a-71 66 3b eb 8b 70 50 8a   *...s.cJqf;..pP.
    00d0 - 0c c6 94 6c db 71 1d 15-b5 d0 ea 37 ef 3e 93 0e   ...l.q.....7.>..

    Start Time: 1720089480
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
^C
bandit16@bandit:~$ openssl s_client localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = SnakeOil
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = SnakeOil
verify return:1
---
Certificate chain
 0 s:CN = SnakeOil
   i:CN = SnakeOil
   a:PKEY: rsaEncryption, 4096 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 10 03:59:50 2024 GMT; NotAfter: Jun  8 03:59:50 2034 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFBzCCAu+gAwIBAgIUBLz7DBxA0IfojaL/WaJzE6Sbz7cwDQYJKoZIhvcNAQEL
BQAwEzERMA8GA1UEAwwIU25ha2VPaWwwHhcNMjQwNjEwMDM1OTUwWhcNMzQwNjA4
MDM1OTUwWjATMREwDwYDVQQDDAhTbmFrZU9pbDCCAiIwDQYJKoZIhvcNAQEBBQAD
ggIPADCCAgoCggIBANI+P5QXm9Bj21FIPsQqbqZRb5XmSZZJYaam7EIJ16Fxedf+
jXAv4d/FVqiEM4BuSNsNMeBMx2Gq0lAfN33h+RMTjRoMb8yBsZsC063MLfXCk4p+
09gtGP7BS6Iy5XdmfY/fPHvA3JDEScdlDDmd6Lsbdwhv93Q8M6POVO9sv4HuS4t/
jEjr+NhE+Bjr/wDbyg7GL71BP1WPZpQnRE4OzoSrt5+bZVLvODWUFwinB0fLaGRk
GmI0r5EUOUd7HpYyoIQbiNlePGfPpHRKnmdXTTEZEoxeWWAaM1VhPGqfrB/Pnca+
vAJX7iBOb3kHinmfVOScsG/YAUR94wSELeY+UlEWJaELVUntrJ5HeRDiTChiVQ++
wnnjNbepaW6shopybUF3XXfhIb4NvwLWpvoKFXVtcVjlOujF0snVvpE+MRT0wacy
tHtjZs7Ao7GYxDz6H8AdBLKJW67uQon37a4MI260ADFMS+2vEAbNSFP+f6ii5mrB
18cY64ZaF6oU8bjGK7BArDx56bRc3WFyuBIGWAFHEuB948BcshXY7baf5jjzPmgz
mq1zdRthQB31MOM2ii6vuTkheAvKfFf+llH4M9SnES4NSF2hj9NnHga9V08wfhYc
x0W6qu+S8HUdVF+V23yTvUNgz4Q+UoGs4sHSDEsIBFqNvInnpUmtNgcR2L5PAgMB
AAGjUzBRMB0GA1UdDgQWBBTPo8kfze4P9EgxNuyk7+xDGFtAYzAfBgNVHSMEGDAW
gBTPo8kfze4P9EgxNuyk7+xDGFtAYzAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3
DQEBCwUAA4ICAQAKHomtmcGqyiLnhziLe97Mq2+Sul5QgYVwfx/KYOXxv2T8ZmcR
Ae9XFhZT4jsAOUDK1OXx9aZgDGJHJLNEVTe9zWv1ONFfNxEBxQgP7hhmDBWdtj6d
taqEW/Jp06X+08BtnYK9NZsvDg2YRcvOHConeMjwvEL7tQK0m+GVyQfLYg6jnrhx
egH+abucTKxabFcWSE+Vk0uJYMqcbXvB4WNKz9vj4V5Hn7/DN4xIjFko+nREw6Oa
/AUFjNnO/FPjap+d68H1LdzMH3PSs+yjGid+6Zx9FCnt9qZydW13Miqg3nDnODXw
+Z682mQFjVlGPCA5ZOQbyMKY4tNazG2n8qy2famQT3+jF8Lb6a4NGbnpeWnLMkIu
jWLWIkA9MlbdNXuajiPNVyYIK9gdoBzbfaKwoOfSsLxEqlf8rio1GGcEV5Hlz5S2
txwI0xdW9MWeGWoiLbZSbRJH4TIBFFtoBG0LoEJi0C+UPwS8CDngJB4TyrZqEld3
rH87W+Et1t/Nepoc/Eoaux9PFp5VPXP+qwQGmhir/hv7OsgBhrkYuhkjxZ8+1uk7
tUWC/XM0mpLoxsq6vVl3AJaJe1ivdA9xLytsuG4iv02Juc593HXYR8yOpow0Eq2T
U5EyeuFg5RXYwAPi7ykw1PW7zAPL4MlonEVz+QXOSx6eyhimp1VZC11SCg==
-----END CERTIFICATE-----
subject=CN = SnakeOil
issuer=CN = SnakeOil
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2103 bytes and written 373 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 4096 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: D8FC54C44B7C7D86F53DBBE9BF9352EB95BF8D6558534A24FFB9D55116EAF52C
    Session-ID-ctx: 
    Resumption PSK: CE5246835E5FF0E7538BDEEB46C0656E8869808DE012AD1B58229CDCA9A69BED4C5ACD22D53A2BE419A5A2B822DC800A
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - fc 55 27 74 5f b4 3e 34-ed 64 98 cf 1b 47 b4 c7   .U't_.>4.d...G..
    0020 - 1b 16 d8 e8 1e 53 45 8a-24 5e 52 43 87 b9 67 76   .....SE.$^RC..gv
    0030 - 8c ad bd df ce 65 1c 06-36 4e 50 3c f5 6e 52 9e   .....e..6NP<.nR.
    0040 - 53 34 37 14 7c 3e b9 43-17 08 4c 43 e1 09 c7 fc   S47.|>.C..LC....
    0050 - 9a b7 29 39 17 89 57 1e-98 12 e0 f4 fe 4f a0 15   ..)9..W......O..
    0060 - 44 4b a4 84 84 bf 02 3e-89 03 78 ae 1c 61 19 e9   DK.....>..x..a..
    0070 - f2 09 6f 9a 22 ef 1a d7-ee e0 d2 c0 43 6d ce be   ..o.".......Cm..
    0080 - 39 d8 b8 5f 10 4b a3 39-50 7a 34 53 46 0e 49 6f   9.._.K.9Pz4SF.Io
    0090 - 10 54 81 dd bb 81 a9 ba-a9 12 ee b0 59 d8 9e eb   .T..........Y...
    00a0 - ef 0d 53 98 1c b1 10 df-c9 af e7 5b 1e 5b 10 d4   ..S........[.[..
    00b0 - cc 1b 16 b5 cb 0b 99 9e-07 a8 fc 89 06 26 52 5b   .............&R[
    00c0 - d1 5b de 2a e3 96 91 ec-87 1f 2f 98 bf 96 90 ac   .[.*....../.....
    00d0 - fa 7f 43 6c 64 6f 08 c0-e7 99 f4 db 4d b7 ec d4   ..Cldo......M...

    Start Time: 1720089495
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B1928957A2C06EB3619579BBE08916360F07FC6E85E5184E127249E6ACAD0CFD
    Session-ID-ctx: 
    Resumption PSK: A2C402DBF0FC28BEA907282E84C94948C721AC72A28B0B1C60103FB625390C4F603E176AC38FB5593A40FBB949A75E08
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - e6 92 3f 4b ce a9 26 82-c0 99 c1 d0 08 d1 12 5c   ..?K..&........\
    0010 - 1a 5a 17 77 55 c7 7d e0-ae df cd a1 8b 5c 51 69   .Z.wU.}......\Qi
    0020 - 73 d9 f2 62 07 b2 50 e1-a2 9a a7 6e 84 28 8b a8   s..b..P....n.(..
    0030 - 9d 1d 94 67 45 bf 74 78-80 5b e5 e3 62 cf e7 53   ...gE.tx.[..b..S
    0040 - a4 7b 8f 7f fd ca bc 89-27 34 04 4a d9 8f f4 62   .{......'4.J...b
    0050 - 1b d4 52 ef ad 30 0b 89-40 9f 0f 26 70 a8 1c 5e   ..R..0..@..&p..^
    0060 - 15 dd 27 0e af 2d ab bc-8a 02 e5 76 5d dd 22 e4   ..'..-.....v].".
    0070 - b5 d4 f1 06 06 ca 8f a9-77 3b 64 6f e1 7f 40 b9   ........w;do..@.
    0080 - 2a 18 7c 01 b0 66 c4 0f-3c ef 42 61 fe 64 2b 5d   *.|..f..<.Ba.d+]
    0090 - 14 e7 91 4c b7 20 55 4e-80 b9 ce f6 0a 67 0d 0e   ...L. UN.....g..
    00a0 - e7 1e 3c 8e d6 95 b5 36-d5 f7 e5 1b e9 b3 7a 85   ..<....6......z.
    00b0 - 92 fb 20 43 40 c3 45 1a-a1 58 7d 59 13 96 04 5c   .. C@.E..X}Y...\
    00c0 - ea 4b 9c 0b a9 ea 92 ae-31 90 e8 e4 ae a7 2c 05   .K......1.....,.
    00d0 - c9 d4 cf 3a ac 36 6a ee-66 59 c8 55 3a 2f 71 0a   ...:.6j.fY.U:/q.

    Start Time: 1720089495
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
KsKVuPmq7LbyYcm4gbpVcVt1bFwrY0dX
KEYUPDATE

```