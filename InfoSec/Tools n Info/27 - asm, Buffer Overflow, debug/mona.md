
Configure working directory for mona:
```sh
!mona config -set workingfolder c:\mona\%p
```

Analyze memory looking for cyclic pattern in memory (and registers)
```sh
!mona findmsp
```
find EIP

```sh
!mona bytearray -b "\x00"
```

```sh
!mona compare -f C:\mona\oscp\bytearray.bin -a <esp address>
```
try without path is the file is not found

