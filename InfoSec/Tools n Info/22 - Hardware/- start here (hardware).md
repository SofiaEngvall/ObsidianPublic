
Guides:
https://www.rapid7.com/blog/post/2019/02/20/iot-security-introduction-to-embedded-hardware-hacking/

Find a way to connect a ttl to usb adapter

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



