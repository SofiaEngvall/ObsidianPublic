
10.129.234.160

ports ssh, 111 rpc, nfs ...

| nfs-showmount: 
|   /var/backups *
|_  /home *

---

1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .bash_history 
ls -lah /var/run/postgresql/
file /var/run/postgresql/.s.PGSQL.5432
psql -U postgres
exit

file /var/run/postgresql/.s.PGSQL.5432
file is run on a linux socket file, we might be able to connect to this using ssh

---

1337@kali:/home/fixit42/boxes/htb/slonik/mount/home/service$ cat .psql_history 
CREATE DATABASE service;
\c service;
CREATE TABLE users ( id SERIAL PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, description TEXT);
INSERT INTO users (username, password, description)VALUES ('service', 'aaabf0d39951f3e6c3e8a7911df524c2'WHERE', network access account');
select * from users;
\q


service : aaabf0d39951f3e6c3e8a7911df524c2

crackstation:

| Hash                             | Type | Result  |
| -------------------------------- | ---- | ------- |
| aaabf0d39951f3e6c3e8a7911df524c2 | md5  | service |

---

normal ssh disconnects



