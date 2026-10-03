
- Install windows to a second hdd
- See what drive letter the drive you want to boot on has
- run `bcdboot E:\Windows` - this adds the partition to the windows boot menu
- reboot into your normal windows

Now we can see the drives - C: here has a partition on the same drive that we might be able to remove/use
![[Images/Pasted image 20261003212604.png]]

Disk 3 has the currently used System reserved partition we booted on

- run `diskpart`

```sh
C:\Windows\system32>diskpart

Microsoft DiskPart version 10.0.19041.3636

Copyright (C) Microsoft Corporation.
On computer: DESKTOP-3SPRNSH

DISKPART> list disk

  Disk ###  Status         Size     Free     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  Disk 0    Online           18 TB  1024 KB        *
  Disk 1    Online          931 GB  1024 KB        *
  Disk 2    Online         2794 GB      0 B        *
  Disk 3    Online          465 GB      0 B

DISKPART> select disk 1

Disk 1 is now the selected disk.

DISKPART> list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    Reserved            16 MB  1024 KB
  Partition 2    Primary            930 GB    17 MB
  Partition 3    Recovery           537 MB   930 GB

DISKPART> select partition 3

Partition 3 is now the selected partition.

DISKPART> set id=c12a7328-f81f-11d2-ba4b-00a0c93ec93b

DiskPart successfully set the partition ID.

DISKPART> format quick fs=fat32 label="Win EFI"

  100 percent completed

DiskPart successfully formatted the volume.

DISKPART> assign letter=S

DiskPart successfully assigned the drive letter or mount point.

DISKPART> exit

Leaving DiskPart...
```

```sh
C:\Windows\system32>bcdboot C:\Windows /s S: /f UEFI
Boot files successfully created.
```

```sh
C:\Windows\system32>diskpart

Microsoft DiskPart version 10.0.19041.3636

Copyright (C) Microsoft Corporation.
On computer: DESKTOP-3SPRNSH

DISKPART> select disk 1

Disk 1 is now the selected disk.

DISKPART> list partition

  Partition ###  Type              Size     Offset
  -------------  ----------------  -------  -------
  Partition 1    Reserved            16 MB  1024 KB
  Partition 2    Primary            930 GB    17 MB
  Partition 3    System             537 MB   930 GB

DISKPART> select partition 3

Partition 3 is now the selected partition.

DISKPART> remove letter=S

DiskPart successfully removed the drive letter or mount point.

DISKPART> exit

Leaving DiskPart...
```

![[Images/Pasted image 20261003215640.png]]

Booting into uefi bios and selecting to boot from the 1TB disk


Confirming system disk using diskpart
```sh
C:\Windows\system32>diskpart

Microsoft DiskPart version 10.0.19041.3636

Copyright (C) Microsoft Corporation.
On computer: DESKTOP-3SPRNSH

DISKPART> list volume

  Volume ###  Ltr  Label        Fs     Type        Size     Status     Info
  ----------  ---  -----------  -----  ----------  -------  ---------  --------
  Volume 0     D   DATA         NTFS   Partition     18 TB  Healthy
  Volume 1     C   SYSTEM       NTFS   Partition    930 GB  Healthy    Boot
  Volume 2         WIN EFI      FAT32  Partition    537 MB  Healthy    System
  Volume 3     E   BACKUP       NTFS   Partition   2794 GB  Healthy
  Volume 4     G   System Rese  NTFS   Partition    579 MB  Healthy
  Volume 5     F                NTFS   Partition    465 GB  Healthy
```

