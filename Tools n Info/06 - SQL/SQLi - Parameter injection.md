
### SQLi parameter

`https://website.thm/blog?id=1`
possibly running: `SELECT * from blog where id=1 and private=0 LIMIT 1;`

`https://website.thm/blog?id=2;--`
possibly running `SELECT * from blog where id=2;-- and private=0 LIMIT 1;`

