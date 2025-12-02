
```sh
┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ mkdir mount

┌──(fixit42㉿kali)-[~/boxes/htb/slonik]
└─$ ls -la mount                                 
total 16
drwxr-xr-x 19 root    root    4096 Sep 22 13:04 .
drwxrwxr-x  3 fixit42 fixit42 4096 Oct 19 23:17 ..
drwxr-xr-x  3 root    root    4096 Oct 24  2023 home
drwxr-xr-x 13 root    root    4096 Sep 19  2023 var
```


### home

home has a dir with user perms
```sh
┌──(fixit42㉿kali)-[~/…/htb/slonik/mount/home]
└─$ ls -la      
total 12
drwxr-xr-x  3 root root 4096 Oct 24  2023 .
drwxr-xr-x 19 root root 4096 Sep 22 13:04 ..
drwxr-x---  5 1337 1337 4096 Sep 22 14:46 service
```

add user to access
```sh
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
...
fixit42:x:1000:1000:fixit42,,,:/home/fixit42:/usr/bin/zsh
1337:x:1337:1001::/home/1337:/bin/sh
```

use user
```sh
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
```

```sh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .bash_history 
ls -lah /var/run/postgresql/
file /var/run/postgresql/.s.PGSQL.5432
psql -U postgres
exit
```

file /var/run/postgresql/.s.PGSQL.5432
file is run on a linux socket file, we might be able to connect to this using ssh

```sh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .psql_history 
CREATE DATABASE service;
\c service;
CREATE TABLE users ( id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, description TEXT);
INSERT INTO users (username, password, description)VALUES ('service', 'aaabf0d39951f3e6c3e8a7911df524c2'WHERE', network access account');
select * from users;
\q
```

service : aaabf0d39951f3e6c3e8a7911df524c2

crackstation:

| Hash                             | Type | Result  |
| -------------------------------- | ---- | ------- |
| aaabf0d39951f3e6c3e8a7911df524c2 | md5  | service |

```sh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.ssh$ ls -la
total 16
drwxrwxr-x 2 1337 1337 4096 Oct 24  2023 .
drwxr-x--- 5 1337 1337 4096 Sep 22 14:46 ..
-rw------- 1 1337 1337   96 Oct 24  2023 authorized_keys
-rw-r--r-- 1 1337 1337   96 Oct 24  2023 id_ed25519.pub
1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service/.ssh$ echo 1 > txt
bash: txt: Read-only file system
```

### var

```sh
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
```
backup files over here, interesting

copy out the latest file:
```sh
1337@kali:/home/fixit42/boxes/htb/slonik/mount/var/backups$ cp archive-2025-10-19T2153.zip /tmp/
```

```sh
┌──(fixit42㉿kali)-[/tmp]
└─$ cp archive-2025-10-19T2153.zip ~/boxes/htb/slonik
```

```sh
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
  inflating: opt/backups/current/base/13761/6176  
 extracting: opt/backups/current/base/13761/13587  
  inflating: opt/backups/current/base/13761/2618_vm  
  inflating: opt/backups/current/base/13761/2603  
...
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
```

```sh
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
```
