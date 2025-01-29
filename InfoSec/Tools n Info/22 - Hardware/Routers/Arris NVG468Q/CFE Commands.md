
```sh
CFE> help
Available commands:

erase_misc_parti    Erase misc partition
x                   Change extra partitions size
find                Find string in NAND
comp                Compare NAND blocks
fb                  Find NAND bad blocks
dn                  Dump NAND contents along with spare area
phy                 Set memory or registers.
meminfo             Display CFE System Memory
kernp               Updates extra bootloader parameter for kernel. To end input enter // consecutively at any time then pres>
sm                  Set memory or registers.
db                  Dump bytes.
dh                  Dump half-words.
dw                  Dump words.
w                   Write the whole image start from beginning of the flash
e                   Erase NAND flash
wp                  Write pmc (previously loaded through JTAG to flash block 0.
ws                  Write whole image (priviously loaded by kermit or JTAG) to flash .
ldt                 load device tree blob from tftp server.
go                  goto and execute from specefic address.
loadb               load binary via network or kermit protocol.
r                   Run program from flash image or from host depending on [f/h/c] flags
p                   Print boot line and board parameter info
c                   Change booline parameters
i                   Erase persistent storage data
i2c                 i2c command to exercise temp75
ddr                 Change board DDR config
a                   Change board AFE ID
b                   Change board parameters
reset               Reset the board
pmdio               Pseudo MDIO access for external switches.
spi                 Legacy SPI access of external switch.
pmclog              pmclog
pmc                 pmc cmd
closeavs            pmc close avs cmd
cpufreq             set CPU frequency
force               override chipid check for images.
help                Obtain help for CFE commands

For more information about a command, enter 'help command-name'
*** command status = 0
CFE>
```

```sh
*** command status = 1
CFE> dw
dw address_in_hex length_in_decimal
*** command status = 0
CFE> 
```


dw 0x02f80000 1024
dw 0x02f80000 20480
dw 0x6100000 20480

dw 0x7ffff42f 1024