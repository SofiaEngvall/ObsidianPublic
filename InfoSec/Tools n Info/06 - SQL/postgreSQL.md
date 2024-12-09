
`psql` to start postgres

`\list` to list the databases
`\c [DATABASE]` to select the database `[DATABASE]`
`\d` to list the tables
Use `SELECT` to find the data

### Examples

```sh
postgres@75dc5cab44d1:/home/pentesterlab$ psql
psql (9.4.15)
Type "help" for help.
postgres=# \list
                               List of databases
     Name     |  Owner   | Encoding  | Collate | Ctype |   Access privileges   
--------------+----------+-----------+---------+-------+-----------------------
 pentesterlab | postgres | SQL_ASCII | C       | C     | 
 postgres     | postgres | SQL_ASCII | C       | C     | 
 template0    | postgres | SQL_ASCII | C       | C     | =c/postgres          +
              |          |           |         |       | postgres=CTc/postgres
 template1    | postgres | SQL_ASCII | C       | C     | =c/postgres          +
              |          |           |         |       | postgres=CTc/postgres
(4 rows)
postgres=# \c pentesterlab
You are now connected to database "pentesterlab" as user "postgres".
pentesterlab=# \d
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | users | table | postgres
(1 row)
pentesterlab=# select * from users;
 login |               password               
-------+--------------------------------------
 admin | c3a2fb1c-c0d9-418b-9e36-ed098ff6ee4b
(1 row)
pentesterlab=# 
```

```sh
pentesterlab@68fff71b137f:/var/www$ psql photoblog photoblog
Password for user photoblog: 
psql (9.4.26)
Type "help" for help.
photoblog=# \d
                List of relations
 Schema |       Name        |   Type   |  Owner   
--------+-------------------+----------+----------
 public | categories        | table    | postgres
 public | categories_id_seq | sequence | postgres
 public | pictures          | table    | postgres
 public | pictures_id_seq   | sequence | postgres
 public | users             | table    | postgres
 public | users_id_seq      | sequence | postgres
(6 rows)
photoblog=# select * from users;
 id | login |             password             
----+-------+----------------------------------
  1 | admin | 8efe310f9ab3efeae8d410a8e0166eb2
(1 row)
photoblog=# create table demo(t text);
CREATE TABLE
photoblog=# copy demo from '/var/lib/postgresql/9.4/key.txt';
COPY 1
photoblog=# 
photoblog=# select * from demo;
                  t                   
--------------------------------------
 25eb9d43-416e-4d3e-9dd3-a7a707380bdb
(1 row)
photoblog=# drop table demo;
DROP TABLE
photoblog=# 
```

### Help

```sh
pentesterlab@68fff71b137f:/var/www$ psql --help
psql is the PostgreSQL interactive terminal.
Usage:
  psql [OPTION]... [DBNAME [USERNAME]]
General options:
  -c, --command=COMMAND    run only single command (SQL or internal) and exit
  -d, --dbname=DBNAME      database name to connect to (default: "pentesterlab")
  -f, --file=FILENAME      execute commands from file, then exit
  -l, --list               list available databases, then exit
  -v, --set=, --variable=NAME=VALUE
                           set psql variable NAME to VALUE
  -V, --version            output version information, then exit
  -X, --no-psqlrc          do not read startup file (~/.psqlrc)
  -1 ("one"), --single-transaction
                           execute as a single transaction (if non-interactive)
  -?, --help               show this help, then exit
Input and output options:
  -a, --echo-all           echo all input from script
  -e, --echo-queries       echo commands sent to server
  -E, --echo-hidden        display queries that internal commands generate
  -L, --log-file=FILENAME  send session log to file
  -n, --no-readline        disable enhanced command line editing (readline)
  -o, --output=FILENAME    send query results to file (or |pipe)
  -q, --quiet              run quietly (no messages, only query output)
  -s, --single-step        single-step mode (confirm each query)
  -S, --single-line        single-line mode (end of line terminates SQL command)
Output format options:
  -A, --no-align           unaligned table output mode
  -F, --field-separator=STRING
                           field separator for unaligned output (default: "|")
  -H, --html               HTML table output mode
  -P, --pset=VAR[=ARG]     set printing option VAR to ARG (see \pset command)
  -R, --record-separator=STRING
                           record separator for unaligned output (default: newline)
  -t, --tuples-only        print rows only
  -T, --table-attr=TEXT    set HTML table tag attributes (e.g., width, border)
  -x, --expanded           turn on expanded table output
  -z, --field-separator-zero
                           set field separator for unaligned output to zero byte
  -0, --record-separator-zero
                           set record separator for unaligned output to zero byte

Connection options:
  -h, --host=HOSTNAME      database server host or socket directory (default: "/var/run/postgresql")
  -p, --port=PORT          database server port (default: "5432")
  -U, --username=USERNAME  database user name (default: "pentesterlab")
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)

For more information, type "\?" (for internal commands) or "\help" (for SQL
commands) from within psql, or consult the psql section in the PostgreSQL
documentation.
Report bugs to <pgsql-bugs@postgresql.org>.
```