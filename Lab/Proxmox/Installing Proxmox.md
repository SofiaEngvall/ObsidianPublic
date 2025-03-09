
### Basic installation

1. Download Proxmox VE latest ISO Installer from https://www.proxmox.com/en/downloads
2. Flash the ISO to a USB drive with for example https://etcher.balena.io/
3. Boot on the USB
4. Follow the guide for installation
5. Go to ip:8006 for web UI, the username is root, the password your selected one

### Uploading an ISO

1. Expand the server you want to upload to
2. Click the "local" storage, `ISO Images` and click Upload

### Resizing partitions

1. Check partition info (right click Server name and click Shell)
```
root@pve:~# lsblk
NAME               MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda                  8:0    0 465.8G  0 disk 
├─sda1               8:1    0  1007K  0 part 
├─sda2               8:2    0     1G  0 part 
└─sda3               8:3    0 464.8G  0 part 
  ├─pve-swap       252:0    0     8G  0 lvm  [SWAP]
  ├─pve-root       252:1    0    96G  0 lvm  /
  ├─pve-data_tmeta 252:2    0   3.4G  0 lvm  
  │ └─pve-data     252:4    0 337.9G  0 lvm  
  └─pve-data_tdata 252:3    0 337.9G  0 lvm  
    └─pve-data     252:4    0 337.9G  0 lvm  
sdb                  8:16   0   1.8T  0 disk 
└─sdb1               8:17   0 232.9G  0 part 
sr0                 11:0    1  1024M  0 rom  
```

![[Images/Pasted image 20250225163633.png]]
- Go to **Datacenter > Node (your server name) > Disks**.
- Select **sdb** (your 2TB drive).
- Click **Initialize Disk with GPT** (this prepares the disk for use).
- After initialization, go to LVM-Thin and click **Create: Thinpool**:
    - **Name:** `data-vg` (or any preferred name).
    - **Device:** `/dev/sdb`.
- Click **Create** to finish.

```sh
root@pve:~# vgs
  VG  #PV #LV #SN Attr   VSize    VFree 
  pve   1   3   0 wz--n- <464.76g 16.00g
root@pve:~# lvremove pve/data
Do you really want to remove active logical volume pve/data? [y/n]: y
  Logical volume "data" successfully removed.
```

```sh
root@pve:~# lvdisplay
  --- Logical volume ---
  LV Path                /dev/pve/swap
  LV Name                swap
  VG Name                pve
  LV UUID                51C9MW-wejo-7cq8-mcxd-Ugfd-B6SK-3oANqK
  LV Write Access        read/write
  LV Creation host, time proxmox, 2025-02-22 01:16:22 +0100
  LV Status              available
  # open                 2
  LV Size                8.00 GiB
  Current LE             2048
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           252:0
   
  --- Logical volume ---
  LV Path                /dev/pve/root
  LV Name                root
  VG Name                pve
  LV UUID                PMhEpM-7Ucl-yMvj-7HBa-Kjsb-cwUf-OFBM7C
  LV Write Access        read/write
  LV Creation host, time proxmox, 2025-02-22 01:16:22 +0100
  LV Status              available
  # open                 1
  LV Size                96.00 GiB
  Current LE             24576
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     256
  Block device           252:1
   
root@pve:~# lvextend -l +100%FREE /dev/pve/root
  Size of logical volume pve/root changed from 96.00 GiB (24576 extents) to <456.76 GiB (116930 extents).
  Logical volume pve/root successfully resized.

root@pve:~# resize2fs /dev/pve/root
resize2fs 1.47.0 (5-Feb-2023)
Filesystem at /dev/pve/root is mounted on /; on-line resizing required
old_desc_blocks = 12, new_desc_blocks = 58
The filesystem on /dev/pve/root is now 119736320 (4k) blocks long.
```


### Updating Proxmox

1. First fix the repo sources:
	- Remove the ones called enterprise
	- Add `pve-no-subscription`
	  ![[Images/Pasted image 20250225212951.png]]

2. Go to the Shell
   ![[Images/Pasted image 20250227201354.png]]
3. Run `apt update`
4. Run `apt upgrade`


### TODO!

install ad on server
install win11
workarounds for gfx card sharing to kali

