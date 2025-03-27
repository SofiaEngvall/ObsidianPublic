
```sh
pentesterlab@0ac07fec12ea:/tmp$ ls -la
total 20
drwxrwxrwt 1 root root 4096 Dec  8 22:24 .
drwxr-xr-x 1 root root 4096 Dec  8 22:24 ..
-rwxr-xr-x 1 root root 2048 Dec  8 22:24 database.db
drwxr-xr-x 3 root root 4096 Jun 17  2015 npm-15-Z7kY83XR
drwxr-xr-x 3 root root 4096 Apr  6  2018 npm-6-ea199a7a

pentesterlab@0ac07fec12ea:/tmp$ file database.db 
database.db: SQLite 3.x database

pentesterlab@0ac07fec12ea:/tmp$ sqlite3 database.db 
SQLite version 3.8.7.1 2014-10-29 13:59:56
Enter ".help" for usage hints.

sqlite> .tables
users

sqlite> select * from users;
admin|3af54a55-f26d-409a-a7b3-aa14a4b3303c

sqlite> 
```