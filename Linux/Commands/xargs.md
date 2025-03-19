
```bash
cat text.txt | xargs -I {} ./Myscript.sh {}
```

`-I {}` (_placeholder_) splits the piped output (_reading that `text.txt` with `cat`_) - into as many arguments as there are lines in that file; so if there are 3 lines, then `Myscript.sh` will be executed 3 times: one for every line (_substituting `{}` argument placeholder_)

obs that  this removes  lines to, use tr for more control
```bash
$ echo "     welcome to   baeldung  " | xargs
welcome to baeldung
```

example that can handle spaces in filenames
```sh
fin . -type f -print0 | xargs -0 sha1sum
```