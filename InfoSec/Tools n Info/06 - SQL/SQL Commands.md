
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


### Clauses

###### FROM
```sql
SELECT name, description
    FROM books;
```
###### WHERE
```sql
DELETE FROM books
    WHERE id = 1;
```
###### DISTINCT - return only unique values
```sql
SELECT DISTINCT name
    FROM books;
```
###### GROUP BY
```sql
SELECT name, COUNT(*)
    FROM books
    GROUP BY name;
```
###### ORDER BY
```sql
SELECT *
    FROM books
    ORDER BY published_date ASC;
```
ASC    ascending
DESC  descending
###### HAVING
```sql
SELECT name, COUNT(*)
    FROM books
    GROUP BY name
    HAVING name LIKE '%Hack%';
```


### Operators

#### Logical operators

###### LIKE
```sql
SELECT *
    FROM books
    WHERE description LIKE "%guide%";
```
% is the *

###### AND
```sql
SELECT *
    FROM books
    WHERE category = "Offensive Security" AND name = "Bug Bounty Bootcamp";
```

###### OR
```sql
SELECT *
    FROM books
    WHERE name LIKE "%Android%" OR name LIKE "%iOS%"; 
```

###### NOT
```sql
SELECT *
    FROM books
    WHERE NOT description LIKE "%guide%";
```

###### BETWEEN
```sql
SELECT *
    FROM books
    WHERE id BETWEEN 2 AND 4;
```

#### Comparison operators

###### =
```sql
SELECT *
    FROM books
    WHERE name = "Designing Secure Software";
```

###### !=
```sql
SELECT *
    FROM books
    WHERE category != "Offensive Security";
```

###### <
```sql
SELECT *
    FROM books
    WHERE published_date < "2020-01-01";
```

###### >
```sql
SELECT *
    FROM books
    WHERE published_date > "2020-01-01";
```

###### <=
```sql
SELECT *
    FROM books
    WHERE published_date <= "2021-11-15";
```

###### >=
```sql
SELECT *
    FROM books
    WHERE published_date >= "2021-11-02";
```


### Functions

#### String functions

###### CONCAT()
```sql
SELECT CONCAT(name, " is a type of ", category, " book.") AS book_info FROM books;
```
###### GROUP_CONCAT()
```sql
SELECT category, GROUP_CONCAT(name SEPARATOR ", ") AS books
    FROM books
    GROUP BY category;
```

###### SUBSTRING()
```sql
SELECT SUBSTRING(published_date, 1, 4) AS published_year FROM books;
```

###### LENGTH()
```sql
SELECT LENGTH(name) AS name_length FROM books;
```

#### Aggregate functions

###### COUNT()
```sql
SELECT COUNT(*) AS total_books FROM books;
```

###### SUM()
```sql
SELECT SUM(price) AS total_price FROM books;
```

###### MAX()
```sql
SELECT MAX(published_date) AS latest_book FROM books;
```

###### MIN()
```sql
SELECT MIN(published_date) AS earliest_book FROM books;
```

###### MOD()
MOD(x, _y_)
_x_ MOD _y_
_x_ % y

###### CAST()
```sql
SELECT CAST("2017-08-29" AS DATE);
```

|Value|Description|
|---|---|
|DATE|Converts _value_ to DATE. Format: "YYYY-MM-DD"|
|DATETIME|Converts _value_ to DATETIME. Format: "YYYY-MM-DD HH:MM:SS"|
|DECIMAL|Converts _value_ to DECIMAL. Use the optional M and D parameters to specify the maximum number of digits (M) and the number of digits following the decimal point (D).|
|TIME|Converts _value_ to TIME. Format: "HH:MM:SS"|
|CHAR|Converts _value_ to CHAR (a fixed length string)|
|NCHAR|Converts _value_ to NCHAR (like CHAR, but produces a string with the national character set)|
|SIGNED|Converts _value_ to SIGNED (a signed 64-bit integer)|
|UNSIGNED|Converts _value_ to UNSIGNED (an unsigned 64-bit integer)|
|BINARY|Converts _value_ to BINARY (a binary string)|

