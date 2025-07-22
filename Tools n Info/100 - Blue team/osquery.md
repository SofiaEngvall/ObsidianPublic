
Find what to search for at: https://osquery.io/schema/5.5.1/


`osqueryi`  interactive mode
`.help`  help
`.tables`  list all tables
`.tables user`  list all tables containing `user`
`.schema users`  show schema for table `users`
`.mode `  set mode to csv, column, line, list or pretty


Examples:
`select gid, uid, description, username, directory from users;`
`select name, version, install_location, install_date from programs limit 1;`
`SELECT * FROM users WHERE username='James';`
`SELECT count(*) from programs;`

`select path, key, name from registry where key = 'HKEY_USERS';`
`select * from ie_extensions;`
`select name,install_location from programs where name LIKE '%wireshark%';`
`select count(*) from services;`

Interesting tables:
windows_eventlog


Operators:
- `=` [equal]
- `<>`  [not equal]
- `>` , `>=` [greater than, greater than, or equal to]
- `<` , `<=` [less than or less than or equal to] 
- `BETWEEN` [between a range]
- `LIKE` [pattern wildcard searches]
- `%` [wildcard, multiple characters]
- `_` [wildcard, one character]

Wildcards:
- `%` : Match all files and folders for one level.
- `%%` : Match all files and folders recursively.
- `%abc` : Match all within-level ending in "abc".
- `abc%` : Match all within-level starting with "abc".

Matching examples:
- `/Users/%/Library` : Monitor for changes to every user's Library folder, _but not the contents within_ .
- `/Users/%/Library/` : Monitor for changes to files _within_ each Library folder, but not the contents of their subdirectories.
- `/Users/%/Library/%` : Same, changes to files within each Library folder.
- `/Users/%/Library/%%` : Monitor changes recursively within each Library.
- `/bin/%sh` : Monitor the `bin` directory for changes ending in `sh` .

Joined query example:
**Query1:** `select uid, pid, name, path from processes;`
**Query2:** `select uid, username, description from users;`
**Joined Query:** `select p.pid, p.name, p.path, u.username from processes p JOIN users u on u.uid=p.uid LIMIT 10;`




