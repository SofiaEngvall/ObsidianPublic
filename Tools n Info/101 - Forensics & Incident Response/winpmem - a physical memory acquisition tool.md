
https://winpmem.velocidex.com/
https://github.com/Velocidex/WinPmem

to make raw image
`winpmem_mini_x64.exe physmem.raw`

1. PTE remapping mode - this is the default and is the most stable
2. MMMapIoSpace mode - uses the MMMapIoSpace kernel API
3. PhysicalMemory mode - passes a handle to the tradition `\\.\PhysicalMemory` device.

`winpmem.exe -1 myimage.raw` example specifying MMMapIoSpace method

has python usage examle

