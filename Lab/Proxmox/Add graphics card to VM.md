
setting up gfx card for kali vm

First we activate IOMMU by editing a line in /etc/default/grub:

```sh
root@pve:~# nano /etc/default/grub
```

edit:
```sh
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"
```

now run update -grub and than restart the server
```sh
root@pve:~# update-grub
Generating grub configuration file ...
Found linux image: /boot/vmlinuz-6.8.12-4-pve
Found initrd image: /boot/initrd.img-6.8.12-4-pve
Found memtest86+x64 image: /boot/memtest86+x64.bin
done
root@pve:~#
```

In the VMs Hardware settings: Add PCI Device → Select NVIDIA 970 with "All Functions" and "Primary GPU" enabled.

