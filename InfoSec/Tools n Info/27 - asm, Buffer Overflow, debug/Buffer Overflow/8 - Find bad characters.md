
## Find bad characters - Are all bytes acceptable input?

To be able to send a payload we need to know which characters we can use. Some characters will have a special meaning to the program and these might stop the rest of the data to be read into memory. One common bad character is `NULL`, `\x00`, as this character often is used to mark the end of a string.

When we later create a payload we will make sure not to use these bad characters we find here.

##### Common bad characters
- `\x00` - Null byte
- `\x08` – Backspace
- `\x09` - Horizontal tab
- `\x0A` – Line Feed (LF) or Newline
- `\x0B` – Vertical Tab (VT)
- `\x0C` – Form Feed (FF)
- `\x0D` – Carriage Return (CR)
- `\x20` – Space
- `\x25` - Percent (%)
- `\x2E` - period, dot
- `\x2F` - Forward slash (/)
- `\x5C` - Backslash ()
- `\x5F` - Underscore
- `\xFF` - Often used as EOF (End of file)

ex. `\x00\x09\x0a\x20`

To save time we could also try running an exploit just removing some of these most common characters: `\x00\x0a\x0d\x5c\x5f\x2f\x2e`.

### Manually

Quick python script to generate all 256 numbers:
```python
allchars = "".join([chr(i) for i in range(256)])  # Generate all characters from \x00 to \xff
badchars = ""
usechars = "".join(c for c in allchars if c not in badchars) # Remove badchars from allchars
#print(''.join(f'\\x{ord(c):02x}' for c in usechars))
```
We prepare to later remove the characters we discover brakes the input.



<font color=red>Observe we have to break program execution with a breakpoint</font> The reason is that the buffer will not overflow if the string if cut short by a bad character.
We can use an AAAAA string to easier find where in memory to look for the badchars string. (And to find a good breakpoint.)

Then we look in memory if all characters are there:
`x/2000xb $esp+500`
`(gdb) x/2000xb $esp+2200`

```sh
0xffffd668:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd670:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd678:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd680:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd688:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd690:     0x55    0x55    0x55    0x55    0x55    0x55    0x55    0x55
0xffffd698:     0x55    0x55    0x55    0x55    0x55    0x01    0x02    0x03
0xffffd6a0:     0x04    0x05    0x06    0x07    0x08    0x00    0x0b    0x0c
0xffffd6a8:     0x0d    0x0e    0x0f    0x10    0x11    0x12    0x13    0x14
0xffffd6b0:     0x15    0x16    0x17    0x18    0x19    0x1a    0x1b    0x1c
0xffffd6b8:     0x1d    0x1e    0x1f    0x00    0x21    0x22    0x23    0x24
0xffffd6c0:     0x25    0x26    0x27    0x28    0x29    0x2a    0x2b    0x2c
0xffffd6c8:     0x2d    0x2e    0x2f    0x30    0x31    0x32    0x33    0x34
```
Instead of 0x09 we have 0x00. This means 0x09 is a bad character.

There will be characters missing in memory. Remove one at a time from the start and write them down. Then repeat until you have found all characters.

ex badchars in hex: `\x00\x09\x0A\x20`

### With Tools

##### [[../mona|Mona]]

