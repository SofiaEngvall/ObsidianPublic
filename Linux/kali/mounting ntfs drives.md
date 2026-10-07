
If you have a dual boot with windows (which this is for) first disable fast start-up to make sure windows releases the drives fully and don't stay hibernated with memory dumped to the drives.

get info on your drives
```sh
┌──(fixit42㉿asus)-[/mnt]
└─$ lsblk -f
NAME        FSTYPE FSVER LABEL   UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sda                                                                                  
├─sda1                                                                               
├─sda2      ntfs         SYSTEM  40EC12F4EC12E446                                    
└─sda3      vfat   FAT32 WIN EFI 1A2F-D989                                           
sdb                                                                                  
├─sdb1                                                                               
└─sdb2      ntfs         BACKUP  5CFADA83FADA58BA                                    
sdc                                                                                  
├─sdc1                                                                               
└─sdc2      ntfs         DATA    222C076A2C0737F5                                    
nvme0n1                                                                              
├─nvme0n1p1 vfat   FAT32         8319-F83E                             973.8M     0% /boot/efi
├─nvme0n1p2                                                                          
├─nvme0n1p5 ext4   1.0           908eb0d3-1e4e-4e69-845a-3983d412431c  369.7G     9% /
└─nvme0n1p6 swap   1             fc533297-eaad-461b-8a52-068676fe4cec                [SWAP]
```

make directories where to mount the drives
```sh
┌──(fixit42㉿asus)-[/mnt]
└─$ ls -la           
total 20
drwxr-xr-x  5 root root 4096 Oct  4 00:39 .
drwxr-xr-x 19 root root 4096 Oct  4 00:20 ..
drwxr-xr-x  2 root root 4096 Oct  4 00:39 backup
drwxr-xr-x  2 root root 4096 Oct  4 00:39 data
drwxr-xr-x  2 root root 4096 Oct  4 00:39 system
```

add the drives to /etc/fstab
```sh
┌──(fixit42㉿asus)-[~]
└─$ sudo nano /etc/fstab       
[sudo] password for fixit42: 
```

```sh
  GNU nano 9.0                                         /etc/fstab *                                                
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# systemd generates mount units based on this file, see systemd.mount(5).
# Please run 'systemctl daemon-reload' after making changes here.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p5 during installation
UUID=908eb0d3-1e4e-4e69-845a-3983d412431c /               ext4    errors=remount-ro 0       1
# /boot/efi was on /dev/nvme0n1p1 during installation
UUID=8319-F83E  /boot/efi       vfat    umask=0077      0       1
# swap was on /dev/nvme0n1p6 during installation
UUID=fc533297-eaad-461b-8a52-068676fe4cec none            swap    sw              0       0

# Windows SYSTEM - sda2      ntfs         SYSTEM  40EC12F4EC12E446
UUID=40EC12F4EC12E446 /mnt/system ntfs defaults,uid=1000,gid=1000,dmask=000,111 0 0
# Windows DATA   - sdc2      ntfs         DATA    222C076A2C0737F5
UUID=222C076A2C0737F5 /mnt/data   ntfs defaults,uid=1000,gid=1000,dmask=000,111 0 0
# Windows BACKUP - sdb2      ntfs         BACKUP  5CFADA83FADA58BA
UUID=5CFADA83FADA58BA /mnt/backup ntfs defaults,uid=1000,gid=1000,dmask=000,111 0 0
```

get it up at once
```sh
┌──(fixit42㉿asus)-[~]
└─$ sudo systemctl daemon-reload

┌──(fixit42㉿asus)-[~]
└─$ sudo mount -a   
```
