
mona is plugin for [[Immunity Debugger]]

### Installing mona

https://github.com/corelan/mona

From github:
1. drop mona.py into the 'PyCommands' folder (inside the Immunity Debugger application folder).
2. install Python 2.7.14 (or a higher 2.7.xx version) into c:\python27, thus overwriting the version that was bundled with Immunity. This is needed to avoid TLS issues when trying to update mona. Make sure you are installing the 32bit version of python.

Configure working directory for mona:
```sh
!mona config -set workingfolder c:\mona\%p
```


### Analyze memory..

Analyze memory looking for cyclic pattern in memory (and registers)
```sh
!mona findmsp
```

#### Find Badchars

```sh
!mona bytearray -b "\x00"
```
Creates two files in a folder named after the executable, one txt file and one binary file.

Use the same bad chars in your python script to crash the program [[Code/badchars.py]].

When we have crashed the program, run:
```sh
!mona compare -f C:\mona\<executable name>\bytearray.bin -a <esp address>
```

Ex. `!mona compare -f C:\mona\gatekeeper\bytearray.bin -a 007A19E4`

This will give us a list of bad chars.
![[Images/Pasted image 20250117205510.png]]
The list might include characters that are not bad chars, especially the ones after a bad char, as they might have been corrupted too.

Add the ones you think are bad chars, like the first one of a pair, and then run an updated byte array creation:
`!mona bytearray -b "\x00\x0a"`

Then update your python script, restart the executable, crash it again and rerun `!mona compare` until you get a Hooray!
![[Images/Pasted image 20250117212414.png]]

### Finding return instructions

```sh
!mona jmp -r esp -cpb "\x00<more bad chars here>"
```

Ex `!mona jmp -r esp -cpb "\x00\x0a"`

