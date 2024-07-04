[_tr_](https://man7.org/linux/man-pages/man1/tr.1p.html) is used for translating characters and can be leveraged for string manipulation. **We can also apply _tr_ when replacing or removing characters**.

Let’s use it for removing spaces:

```bash
$ echo " welcome to    baeldung " | tr -d '[:blank:]'
welcometobaeldung
```

We use the _-d_ flag to delete all occurrences of a character. **In this case, we’re deleting all blank characters.** This is represented by the [POSIX](https://www.baeldung.com/linux/posix) bracket expression _[:blank:]_, which groups the space and tab character.

Because of this, the [_tr_ command](https://www.baeldung.com/linux/tr-command) doesn’t maintain the spaces between characters.

If we use _[:space:]_ instead, we can remove all cases of whitespace, including newlines:

```bash
$ echo " welcome to    baeldung " | tr -d '[:space:]'
welcometobaeldung
```

**We can also trim extra whitespace between characters with the _-s_ flag**:

```bash
$ echo " welcome to    baeldung " | tr -s '[:blank:]'
 welcome to baeldung 
```

The _-s_ flag stands for squeeze, and we use it to remove sequential occurrences of a character.

---

You can rotate a string by 13 characters, ROT13

```bash
pax$ echo 'hello there' | tr 'a-z' 'n-za-m'
uryyb gurer

pax$ echo 'hello there' | tr 'a-z' 'n-za-m' | tr 'a-z' 'n-za-m'
hello there
```

For a more general solution where you want to provide an arbitrary rotation (0 through 26), you can use:

```bash
#!/usr/bin/bash
    
dual=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
phrase='hello there'
rotat=13
newphrase=$(echo $phrase | tr "${dual:0:26}" "${dual:${rotat}:26}")
echo ${newphrase}
```


### Help

```sh
┌──(kali㉿kali)-[~]
└─$ tr --help              
Usage: tr [OPTION]... STRING1 [STRING2]
Translate, squeeze, and/or delete characters from standard input,
writing to standard output.  STRING1 and STRING2 specify arrays of
characters ARRAY1 and ARRAY2 that control the action.

  -c, -C, --complement    use the complement of ARRAY1
  -d, --delete            delete characters in ARRAY1, do not translate
  -s, --squeeze-repeats   replace each sequence of a repeated character
                            that is listed in the last specified ARRAY,
                            with a single occurrence of that character
  -t, --truncate-set1     first truncate ARRAY1 to length of ARRAY2
      --help        display this help and exit
      --version     output version information and exit

ARRAYs are specified as strings of characters.  Most represent themselves.
Interpreted sequences are:

  \NNN            character with octal value NNN (1 to 3 octal digits)
  \\              backslash
  \a              audible BEL
  \b              backspace
  \f              form feed
  \n              new line
  \r              return
  \t              horizontal tab
  \v              vertical tab
  CHAR1-CHAR2     all characters from CHAR1 to CHAR2 in ascending order
  [CHAR*]         in ARRAY2, copies of CHAR until length of ARRAY1
  [CHAR*REPEAT]   REPEAT copies of CHAR, REPEAT octal if starting with 0
  [:alnum:]       all letters and digits
  [:alpha:]       all letters
  [:blank:]       all horizontal whitespace
  [:cntrl:]       all control characters
  [:digit:]       all digits
  [:graph:]       all printable characters, not including space
  [:lower:]       all lower case letters
  [:print:]       all printable characters, including space
  [:punct:]       all punctuation characters
  [:space:]       all horizontal or vertical whitespace
  [:upper:]       all upper case letters
  [:xdigit:]      all hexadecimal digits
  [=CHAR=]        all characters which are equivalent to CHAR

Translation occurs if -d is not given and both STRING1 and STRING2 appear.
-t is only significant when translating.  ARRAY2 is extended to length of
ARRAY1 by repeating its last character as necessary.  Excess characters
of ARRAY2 are ignored.  Character classes expand in unspecified order;
while translating, [:lower:] and [:upper:] may be used in pairs to
specify case conversion.  Squeezing occurs after translation or deletion.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/tr>
or available locally via: info '(coreutils) tr invocation'
```