
## Raspberry Pi OS


### Enabling ssh

`sudo raspi-config`

Select Interfacing Options


### Setting 1080p

*research more, only works when cable is unplugged at boot*

in `/boot/config.txt`
```sh
hdmi_force_hotplug=1
hdmi_group=1
hdmi_mode=16
disable_overscan=1
```

we also tried:
in /boot/firmware/cmdline.txt (added to start of kernel command line)
```sh
video=HDMI-A-1:1920x1080M@60D
```