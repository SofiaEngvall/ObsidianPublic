
In VMWare Workstation Pro, Go to the VMs tab. Click `File`, `Export to OVF...`

Open a PowerShell prompt, select where on the proxmox server you want the files. I'll do `\tmp\`

```powershell
PS C:\Users\sofia> scp "C:\Virtual Machines\Kali.ovf" root@192.168.0.176:\tmp\
root@192.168.0.176's password:
Kali.ovf                                                                     100%   15KB   7.4MB/s   00:00

PS C:\Users\sofia> scp "C:\Virtual Machines\Kali-disk1.vmdk" root@192.168.0.176:\tmp\
root@192.168.0.176's password:
Kali-disk1.vmdk                                                              100%   20GB  67.4MB/s   05:06
```

#### Import the VM into Proxmox

```sh
root@pve:/tmp# qm importovf 102 Kali.ovf data
  Logical volume "vm-102-disk-0" created.
transferred 0.0 B of 50.0 GiB (0.00%)
transferred 512.0 MiB of 50.0 GiB (1.00%)
transferred 1.0 GiB of 50.0 GiB (2.00%)
...
transferred 49.5 GiB of 50.0 GiB (99.00%)
transferred 50.0 GiB of 50.0 GiB (100.00%)
transferred 50.0 GiB of 50.0 GiB (100.00%)
```

#### Grow the disk to 100GB

##### On the proxmox server:

```sh
root@pve:/tmp# qm resize 102 scsi0 +50G
  Size of logical volume data/vm-102-disk-0 changed from 50.00 GiB (12800 extents) to 100.00 GiB (25600 extents).
  Logical volume data/vm-102-disk-0 successfully resized.
```

##### On the Kali VM:

`df -h`
We have one Primary partition with `\` of about 50GB size
One logical partition with one Swap pertition of 1 GB size

`sudo gparted`
We turned of swap by right clicking it

`sudo cfdisk`
We changed the size of the logical partition to fill upp all the free space

`sudo gparted`
We moved the Swap to end of the logical partition and applied

We changed the size of the logical partition to only be the minimal size - This only worked when setting "align" to none

We increased the size of the Primary partition to fill the whole new area = the rest of the disk

(screenshots from stream? 2025-03-14)

