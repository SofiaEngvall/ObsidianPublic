
### Basic commands

`select * from users;`
`select username,password from users;`

`select * from users limit 1;`
`select * from users limit 3,1;`   skips 3 and then returns 1

`select * from users where username='admin';`
`select * from users where username != 'admin';`

`select * from users where username='admin' or username='jon';`
`select * from users where username='admin' and password='p4ssword';`

`select * from users where username like 'a%';`
`select * from users where username like '%n';`
`select * from users where username like '%mi%';`

### Union

Combining several select statements, results must have the same number of columns and the data needs to have a similar data type.

`SELECT name,address,city,postcode from customers UNION SELECT company,address,city,postcode from suppliers;`


### Insert

Insert a new row

`insert into users (username,password) values ('bob','password123');`


### Update

Update one or more rows

`update users SET username='root',password='pass123' where username='admin';`


### Delete

Delete one or more rows.

`delete from users where username='martin';`

`delete from users;` - Will delete the whole table, careful! LIMIT can be used for safety.


### Comments

`--` This is a comment (mysql req space after)
`#` (Mysql only)

### Statement end

`;`



