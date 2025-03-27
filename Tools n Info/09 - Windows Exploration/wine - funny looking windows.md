
If you realize Windows is looking odd, files are missing...

run "set" in windows to se the wine executable at the very top
try /bin/ps aux and see if you get a process listing :)


An example machine is `THM Brainpan 1`
In this machine I tried running a `/linux/x86/shell_reverse_tcp` instead of my original `windows/shell_reverse_tcp` one and got a nice stable linux shell instead of a quirky odd windows-like one. :)


In wine Linux executables with Linux path names can be run, like `/bin/ps aux`

