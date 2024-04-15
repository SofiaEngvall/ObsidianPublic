A sticky bit is a permission bit that only permits the owner and root user of a file/directory to modify, rename or delete it. When it's not set, any user can.

Find files:
`find / -perm -1000 -type d 2>/dev/null`

