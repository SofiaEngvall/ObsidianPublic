
Guest has read permissions on:
\10.10.10.40\Share
\10.10.10.40\Users

get all files on a share recursively (might have problems with big files?)
`smbget --guest --recursive smb://10.10.10.40/Share`
`smbget --guest --recursive smb://10.10.10.40/Users`

```sh
┌──(kali㉿proxli)-[~/boxes/htb/blue]
└─$ smbget --guest --recursive smb://10.10.10.40/Share
Using guest user
Can´t open directory smb://10.10.10.40/Share: Permission denied

┌──(kali㉿proxli)-[~/boxes/htb/blue]
└─$ smbget --guest --recursive smb://10.10.10.40/Users
Using guest user
Can´t open directory smb://10.10.10.40/Users: Permission denied
```

ok, so let's try smbclient

`smbclient //10.10.10.40/Share -U Guest`
`smbclient //10.10.10.40/Users -U Guest`

