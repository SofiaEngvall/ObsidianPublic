
```sh
james@mnemonic:~$ netstat -antplue
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       User       Inode      PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      101        18462      -                   
tcp        0      0 0.0.0.0:1337            0.0.0.0:*               LISTEN      0          21507      -                   
tcp        0    628 10.10.62.151:1337       10.18.21.236:37234      ESTABLISHED 0          32967      -                   
tcp6       0      0 :::21                   :::*                    LISTEN      0          21242      -                   
tcp6       0      0 :::1337                 :::*                    LISTEN      0          21518      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      0          21682      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           101        18461      -                   
udp        0      0 10.10.62.151:68         0.0.0.0:*                           100        30774      -                   
```

```sh
james@mnemonic:~$ ss -tlupn
Netid       State         Recv-Q        Send-Q                    Local Address:Port                Peer Address:Port        
udp         UNCONN        0             0                         127.0.0.53%lo:53                       0.0.0.0:*           
udp         UNCONN        0             0                     10.10.62.151%eth0:68                       0.0.0.0:*           
tcp         LISTEN        0             128                       127.0.0.53%lo:53                       0.0.0.0:*           
tcp         LISTEN        0             128                             0.0.0.0:1337                     0.0.0.0:*           
tcp         LISTEN        0             32                                    *:21                             *:*           
tcp         LISTEN        0             128                                [::]:1337                        [::]:*           
tcp         LISTEN        0             128                                   *:80                             *:*           
```

```sh
james@mnemonic:~$ netstat -ano
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       Timer
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0      0 0.0.0.0:1337            0.0.0.0:*               LISTEN      off (0.00/0/0)
tcp        0    324 10.10.62.151:1337       10.18.21.236:54398      ESTABLISHED on (0.09/0/0)
tcp6       0      0 :::21                   :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::1337                 :::*                    LISTEN      off (0.00/0/0)
tcp6       0      0 :::80                   :::*                    LISTEN      off (0.00/0/0)
udp        0      0 127.0.0.53:53           0.0.0.0:*                           off (0.00/0/0)
udp        0      0 10.10.62.151:68         0.0.0.0:*                           off (0.00/0/0)
raw6       0      0 :::58                   :::*                    7           off (0.00/0/0)
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     14885    /run/lvm/lvmpolld.socket
unix  2      [ ]         DGRAM                    34215    /run/user/1001/systemd/notify
unix  2      [ ACC ]     SEQPACKET  LISTENING     15367    /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     34218    /run/user/1001/systemd/private
unix  2      [ ]         DGRAM                    14887    /run/systemd/journal/syslog
unix  2      [ ACC ]     STREAM     LISTENING     34222    /run/user/1001/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     14899    /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     34223    /run/user/1001/gnupg/S.gpg-agent
unix  8      [ ]         DGRAM                    14901    /run/systemd/journal/socket
unix  2      [ ACC ]     STREAM     LISTENING     34224    /run/user/1001/snapd-session-agent.socket
unix  2      [ ACC ]     STREAM     LISTENING     34225    /run/user/1001/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     34226    /run/user/1001/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     18855    /var/lib/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     34227    /run/user/1001/gnupg/S.gpg-agent.browser
unix  8      [ ]         DGRAM                    15270    /run/systemd/journal/dev-log
unix  2      [ ACC ]     STREAM     LISTENING     18840    @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     18820    /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     18822    /run/acpid.socket
unix  2      [ ACC ]     STREAM     LISTENING     18828    /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     18841    /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     18843    /run/snapd-snap.socket
unix  3      [ ]         DGRAM                    14872    /run/systemd/notify
unix  2      [ ACC ]     STREAM     LISTENING     14875    /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     14880    /run/lvm/lvmetad.socket
unix  3      [ ]         STREAM     CONNECTED     21244    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21459    
unix  2      [ ]         DGRAM                    19598    
unix  3      [ ]         STREAM     CONNECTED     20453    
unix  3      [ ]         STREAM     CONNECTED     19131    
unix  3      [ ]         STREAM     CONNECTED     21484    /run/systemd/journal/stdout
unix  3      [ ]         DGRAM                    18203    
unix  2      [ ]         DGRAM                    34076    
unix  3      [ ]         STREAM     CONNECTED     19274    
unix  3      [ ]         STREAM     CONNECTED     19635    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     20012    
unix  3      [ ]         STREAM     CONNECTED     19569    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     18396    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     15941    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21198    
unix  3      [ ]         STREAM     CONNECTED     21266    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     20014    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     20531    
unix  3      [ ]         STREAM     CONNECTED     19636    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     19567    
unix  3      [ ]         DGRAM                    18205    
unix  2      [ ]         DGRAM                    21536    
unix  3      [ ]         STREAM     CONNECTED     19633    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    18204    
unix  2      [ ]         DGRAM                    21464    
unix  3      [ ]         STREAM     CONNECTED     21199    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     21543    
unix  2      [ ]         DGRAM                    18192    
unix  2      [ ]         DGRAM                    18443    
unix  3      [ ]         STREAM     CONNECTED     18152    
unix  3      [ ]         STREAM     CONNECTED     19276    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     20978    /run/systemd/journal/stdout
unix  2      [ ]         DGRAM                    19630    
unix  3      [ ]         STREAM     CONNECTED     18839    
unix  3      [ ]         STREAM     CONNECTED     18838    
unix  3      [ ]         STREAM     CONNECTED     19632    
unix  3      [ ]         STREAM     CONNECTED     19634    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    18202    
unix  3      [ ]         STREAM     CONNECTED     19133    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21544    /var/run/dbus/system_bus_socket
unix  2      [ ]         DGRAM                    15547    
unix  3      [ ]         STREAM     CONNECTED     20378    
unix  3      [ ]         STREAM     CONNECTED     19499    
unix  3      [ ]         STREAM     CONNECTED     19351    
unix  3      [ ]         STREAM     CONNECTED     15668    
unix  3      [ ]         STREAM     CONNECTED     21660    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     18153    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     18366    
unix  3      [ ]         STREAM     CONNECTED     15942    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     21983    
unix  3      [ ]         DGRAM                    16014    
unix  2      [ ]         DGRAM                    15947    
unix  3      [ ]         STREAM     CONNECTED     21978    
unix  3      [ ]         STREAM     CONNECTED     15728    
unix  3      [ ]         STREAM     CONNECTED     21287    /run/systemd/journal/stdout
unix  3      [ ]         STREAM     CONNECTED     19631    
unix  2      [ ]         DGRAM                    15899    
unix  3      [ ]         STREAM     CONNECTED     21659    
unix  3      [ ]         STREAM     CONNECTED     34404    
unix  3      [ ]         STREAM     CONNECTED     21979    /var/run/dbus/system_bus_socket
unix  3      [ ]         STREAM     CONNECTED     20624    
unix  2      [ ]         DGRAM                    34178    
unix  3      [ ]         STREAM     CONNECTED     34172    
unix  3      [ ]         DGRAM                    34217    
unix  3      [ ]         STREAM     CONNECTED     34403    
unix  2      [ ]         DGRAM                    34185    
unix  3      [ ]         STREAM     CONNECTED     21984    /var/run/dbus/system_bus_socket
unix  3      [ ]         DGRAM                    14873    
unix  3      [ ]         DGRAM                    34216    
unix  3      [ ]         DGRAM                    16013    
unix  3      [ ]         STREAM     CONNECTED     34193    /run/systemd/journal/stdout
unix  3      [ ]         DGRAM                    14874    
unix  2      [ ]         DGRAM                    21232    
```
