
#### help

```sh

```

#### usage

https://www.briskinfosec.com/tooloftheday/toolofthedaydetail/DIRSEARCH

General usage: root@kali:~#python3 dirsearch.py –u https://www.example.com/ -e php

Some examples how to use dirsearch - those are the most common arguments. If you need all, just use the "-h" argument.

- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --recursive -R 2
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --recursive -R 4 --scan-subdirs=/,/wp-content/,/wp-admin/
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --exclude-texts=This,AndThat
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt -H "User-Agent: IE"
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt -t 20
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --random-agents
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --json-report=reports/target.json
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --simple- root@kali:~#report=reports/target-paths.txt
    
- root@kali:~#python3 dirsearch.py -e php,txt,zip -u https://target -w db/dicc.txt --plain-text-report=reports/target-paths-and-status.json
