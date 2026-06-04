
We went through the [[../../../Tools n Info/07 - Linux Exploration/- start here (linux)|- start here (linux)]] list (online htb meetup https://www.youtube.com/watch?v=lB8OouAvcJE)

```sh
christine@funnel:~$ ps aux|cat
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND                                                    
...
systemd+    1100  0.0  1.3 214124 26696 ?        Ss   16:47   0:00 postgres
systemd+    1186  0.0  0.3 214244  6868 ?        Ss   16:47   0:00 postgres: checkpointer 
systemd+    1187  0.0  0.2 214260  5556 ?        Ss   16:47   0:00 postgres: background writer 
systemd+    1189  0.0  0.4 214124  9964 ?        Ss   16:47   0:00 postgres: walwriter 
systemd+    1190  0.0  0.4 215708  8220 ?        Ss   16:47   0:00 postgres: autovacuum launcher 
systemd+    1191  0.0  0.3 215688  6424 ?        Ss   16:47   0:00 postgres: logical replication launcher 
...

```

```sh
christine@funnel:~$ ss -tulpn
Netid       State        Recv-Q       Send-Q             Local Address:Port              Peer Address:Port      Process       
udp         UNCONN       0            0                  127.0.0.53%lo:53                     0.0.0.0:*
udp         UNCONN       0            0                        0.0.0.0:68                     0.0.0.0:*
tcp         LISTEN       0            4096               127.0.0.53%lo:53                     0.0.0.0:*
tcp         LISTEN       0            128                      0.0.0.0:22                     0.0.0.0:*
tcp         LISTEN       0            4096                   127.0.0.1:5432                   0.0.0.0:*
tcp         LISTEN       0            4096                   127.0.0.1:40773                  0.0.0.0:*
tcp         LISTEN       0            32                             *:21                           *:*
tcp         LISTEN       0            128                         [::]:22                        [::]:*  
```

port 5432 and 40773 are open to localhost (127.0.0.1)

Port 5432 is PostgreSQL

psql, the postgres client is not installed on the machine so we'll do a port forward
