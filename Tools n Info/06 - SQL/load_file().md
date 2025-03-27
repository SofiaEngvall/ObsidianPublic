

```sql
SET @mytxtvar = LOAD_FILE('/var/lib/mysql-files/key.txt');
SELECT @mytxtvar;
```