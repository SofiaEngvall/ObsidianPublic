
Messing with the cpus ability to read the bios

1. Connect uart so we can do input n output
2. connect data out from flash chip to ground (or clock..) at certain time during boot process - what it's loaded the base system, before it loads the linux image
3. we're hopefully in uboot/whatever it has, run help
4. if uboot, printend and modify bootargs
   setenv bootargs ...whatever was there but set init to /etc/sh
   run bootcmd
5. hopefully we end up at a root prompt instead of at a login prompt, now try running the command we removed from init
6. hopefully we not have a fully functioning device - if there's problems, dig into it
7. check for writeable storage... can we add a user or something else for persistence?


