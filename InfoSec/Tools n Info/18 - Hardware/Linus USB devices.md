
list usb devices by bus and device id
`lsusb`

list available usb devices
`ls /dev | grep USB`

using screen to talk to simple serial device (if you don't know the buad rate, test different ones until you get output)
`screen /dev/ttyUSB0 9600`
Ctrl+a+d to exit screen

