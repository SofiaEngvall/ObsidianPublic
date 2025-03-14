
In VMWare Workstation Pro, Go to the VMs tab. Click `File`, `Export to OVF...`

Open a PowerShell prompt, select where on the proxmox server you want the. I'll do `\tmp\`

```powershell
PS C:\Users\sofia> scp C:\Virtual Machines\Kali.ovf root@192.168.0.176:\tmp\
C:\WINDOWS\System32\OpenSSH\scp.exe: stat local "C:/Virtual": No such file or directory
PS C:\Users\sofia> scp "C:\Virtual Machines\Kali.ovf" root@192.168.0.176:\tmp\
root@192.168.0.176's password:
Kali.ovf                                                                     100%   15KB   7.4MB/s   00:00
PS C:\Users\sofia> scp "C:\Virtual Machines\Kali-disk1.vmdk" root@192.168.0.176:\tmp\
root@192.168.0.176's password:
Kali-disk1.vmdk                                                              100%   20GB  67.4MB/s   05:06
PS C:\Users\sofia>
```

```sh
root@pve:/tmp# ls -la
total 21118528
drwxrwxrwt  8 root root        4096 Mar 11 20:07 .
drwxr-xr-x 18 root root        4096 Feb 25 17:05 ..
drwxrwxrwt  2 root root        4096 Mar 11 18:59 .font-unix
drwxrwxrwt  2 root root        4096 Mar 11 18:59 .ICE-unix
-rw-r--r--  1 root root 21625313792 Mar 11 20:12 Kali-disk1.vmdk
-rw-r--r--  1 root root       15527 Mar 11 20:06 Kali.ovf
drwx------  3 root root        4096 Mar 11 18:59 systemd-private-5a57ab9bb13340e897c862d496f265e1-chrony.service-cOLIIv
drwx------  3 root root        4096 Mar 11 18:59 systemd-private-5a57ab9bb13340e897c862d496f265e1-systemd-logind.service-BvEef8
drwxrwxrwt  2 root root        4096 Mar 11 18:59 .X11-unix
drwxrwxrwt  2 root root        4096 Mar 11 18:59 .XIM-unix
root@pve:/tmp#
```
We can see both of our files

#### Import the VM into Proxmox

`qm importovf 102 kali.ovf data`

```sh
root@pve:/tmp# qm importovf 102 Kali.ovf data
  Logical volume "vm-102-disk-0" created.
transferred 0.0 B of 50.0 GiB (0.00%)
transferred 512.0 MiB of 50.0 GiB (1.00%)
transferred 1.0 GiB of 50.0 GiB (2.00%)
transferred 1.5 GiB of 50.0 GiB (3.00%)
transferred 2.0 GiB of 50.0 GiB (4.00%)
transferred 2.5 GiB of 50.0 GiB (5.00%)
transferred 3.0 GiB of 50.0 GiB (6.00%)
transferred 3.5 GiB of 50.0 GiB (7.00%)
transferred 4.0 GiB of 50.0 GiB (8.00%)
transferred 4.5 GiB of 50.0 GiB (9.00%)
transferred 5.0 GiB of 50.0 GiB (10.00%)
transferred 5.5 GiB of 50.0 GiB (11.00%)
transferred 6.0 GiB of 50.0 GiB (12.00%)
transferred 6.5 GiB of 50.0 GiB (13.00%)
transferred 7.0 GiB of 50.0 GiB (14.00%)
transferred 7.5 GiB of 50.0 GiB (15.00%)
transferred 8.0 GiB of 50.0 GiB (16.00%)
transferred 8.5 GiB of 50.0 GiB (17.00%)
...
transferred 48.5 GiB of 50.0 GiB (97.00%)
transferred 49.0 GiB of 50.0 GiB (98.00%)
transferred 49.5 GiB of 50.0 GiB (99.00%)
transferred 50.0 GiB of 50.0 GiB (100.00%)
transferred 50.0 GiB of 50.0 GiB (100.00%)
root@pve:/tmp#
```

#### Grow the disk to 100GB

`qm resize 102 scsi0 +50G`

```sh
root@pve:/tmp# qm resize 102 scsi0 +50G
  Size of logical volume data/vm-102-disk-0 changed from 50.00 GiB (12800 extents) to 100.00 GiB (25600 extents).
  Logical volume data/vm-102-disk-0 successfully resized.
```

df -h
cfdisk
df -h
cfdisk

```sh

```