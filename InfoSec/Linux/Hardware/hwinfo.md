
sudo apt install hwinfo

```sh
hwinfo -h
Usage: hwinfo [OPTIONS]
Probe for hardware.
Options:
    --<HARDWARE_ITEM>
        This option can be given more than once. Probe for a particular
        HARDWARE_ITEM. Available hardware items are:
        all, arch, bios, block, bluetooth, braille, bridge, camera,
        cdrom, chipcard, cpu, disk, dsl, dvb, fingerprint, floppy,
        framebuffer, gfxcard, hub, ide, isapnp, isdn, joystick, keyboard,
        memory, mmc-ctrl, modem, monitor, mouse, netcard, network, partition,
        pci, pcmcia, pcmcia-ctrl, pppoe, printer, redasd,
        reallyall, scanner, scsi, smp, sound, storage-ctrl, sys, tape,
        tv, uml, usb, usb-ctrl, vbe, wlan, xen, zip
    --short
        Show only a summary. Use this option in addition to a hardware
        probing option.
    --listmd
        Normally hwinfo does not report RAID devices. Add this option to
        see them.
    --only DEVNAME
        This option can be given more than once. If you add this option
        only entries in the device list matching DEVNAME will be shown.
        Note that you also have to specify --<HARDWARE_ITEM> to trigger
        any device probing.
    --save-config SPEC
        Store config  for a particular device below /var/lib/hardware.
        SPEC can be a device name, an UDI, or 'all'. This option must be
        given in addition to a hardware probing option.
    --show-config UDI
        Show saved config data for a particular device.
    --map
        If disk names have  changed (e.g. after a kernel update) this
        prints a list of disk name mappings. Note  that  you must have
        used --save-config at some point before for this can work.
    --debug N
        Set debug level to N. The debug info is shown only in the log
        file. If you specify a log file, the debug level is implicitly
        set to a reasonable value (N is a bitmask of individual flags).
    --verbose
        Increase verbosity. Only together with --map.
    --log FILE
        Write log info to FILE.
        Don´t forget to also specify --<HARDWARE_ITEM> to trigger any
        device probing.
    --dump-db N
        Dump hardware data base. N is either 0 for the external data
        base in /var/lib/hardware, or 1 for the internal data base.
    --version
        Print libhd version.
    --help
        Print usage.
```

