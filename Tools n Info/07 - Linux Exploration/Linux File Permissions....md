
`ls -l`
`getfacl`
`stat <dirname>`
`chmod`
#### Permissions types/modes

- **Read (r)**: The file can be opened, and its content viewed. For a directory, the read permission allows you to list the contents of the directory.
- **Write (w)**: The file can be modified; for a directory, the write permission allows you to create, delete, and rename files within the directory.
- **Execute (x)**: The file can be executed as a program. For a directory, the execute permission allows you to access, or traverse into, the directory, and access any of its contents.

##### Octal representation

Full permissions (read, write, execute) would be `7` in octal (since 4+2+1=7), which also stands for `rwx`. No permissions would be `0` (`---`), read-only would be `4` (`r--)`, write-only would be `2` (`-w-`), execute-only would be `1` (`--x`), etc.
#### Permission classes

- **User (u)**: The owner of the file.
- **Group (g)**: Users who are members of the file's group.
- **Others (o)**: Users who are not the owners of the file and do not belong to the group.
- **All (a)**: Represents all three types of access classes.


#### File Types

The first character indicates the type of the file: a dash (**`-`**) means it's a regular file, **`d`** stands for a directory, and there are other types as well (**`l`** for link, **`b`** for block device, **`c`** for character device, **`s`** for socket, and **`p`** for named pipe).


#### Special permissions

Special permissions are available for files and directories and provide additional privileges over the standard permission sets that have been covered.

- SUID is the special permission for the user access level and always executes as the user who owns the file, no matter who is passing the command.
- SGID allows a file to be executed as the group owner of the file; a file created in the directory has its group ownership set to the directory owner. This is helpful for directories used collaboratively among different members of a group because all members can access and execute new files.

The "sticky bit" is a directory-level special permission that restricts file deletion, meaning only the file owner can remove a file within the directory.

#### chmod - change mode

- **Who** - represents identities: u,g,o,a (user, group, other, all)
- **What** - represents actions: +, -, = (add, remove, set exact)
- **Which** - represents access levels: r, w, x (read, write, execute)

- Start at 0
- If the _read_ permission should be set, add **4**
- If the _write_ permission should be set, add **2**
- If the _execute_ permission should be set, add **1**

#### user + s (pecial)

Commonly noted as **SUID**, the special permission for the user access level has a single function: A file with **SUID** always executes as the user who owns the file, regardless of the user passing the command. If the file owner doesn't have execute permissions, then use an uppercase **S** here.

#### group + s (pecial)

Commonly noted as **SGID**, this special permission has a couple of functions:

- If set on a file, it allows the file to be executed as the **group** that owns the file (similar to SUID)
- If set on a directory, any files created in the directory will have their **group** ownership set to that of the directory owner

This permission set is noted by a lowercase **s** where the **x** would normally indicate **execute** privileges for the **group**. It is also especially useful for directories that are often used in collaborative efforts between members of a group. Any member of the group can access any new file. This applies to the execution of files, as well. **SGID** is very powerful when utilized properly.

As noted previously for **SUID**, if the owning group does not have execute permissions, then an uppercase **S** is used.

#### other + t (sticky)

The last special permission has been dubbed the "sticky bit." This permission does not affect individual files. However, at the directory level, it restricts file deletion. Only the **owner** (and **root**) of a file can remove the file within that directory. A common example of this is the `/tmp` directory:

```sh
┌──(kali㉿kali)-[~]
└─$ ls -la /tmp
drwxrwxrwt  24 root root 12288 Apr 21 18:12 tmp
```

The permission set is noted by the lowercase **t**, where the **x** would normally indicate the execute privilege.


#### Setting special perms

- Start at 0
- SUID = 4
- SGID = 2
- Sticky = 1

`chmod X###

meaning 4000 is suid and 2000 guid
1000 is sticky
