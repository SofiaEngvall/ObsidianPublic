
https://www.flashrom.org/

`sudo flashrom -V -r [filename] -p`

-V verbose
-r read

old shikara example: `flashrom -p ft2232_spi:type=232H -r spidump.bin`

for ch314a:
`sudo flashrom --programmer ch341a_spi -r [filename] --progress`


