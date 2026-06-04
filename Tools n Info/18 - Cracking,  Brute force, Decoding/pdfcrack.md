
```sh
ubuntu@tryhackme:~/Desktop$ pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
PDF version 1.7
Security Handler: Standard
V: 2
R: 3
P: -1060
Length: 128
Encrypted Metadata: True
FileID: 3792b9a3671ef54bbfef57c6fe61ce5d
U: c46529c06b0ee2bab7338e9448d37c3200000000000000000000000000000000
O: 95d0ad7c11b1e7b3804b18a082dda96b4670584d0044ded849950243a8a367ff
found user-password: 'naughtylist'
```


### Help

```sh
ubuntu@tryhackme:~/Desktop$ pdfcrack -h
pdfcrack: invalid option -- 'h'
Usage: pdfcrack -f filename [OPTIONS]
OPTIONS:
-b, --bench             perform benchmark and exit
-c, --charset=STRING    Use the characters in STRING as charset
-w, --wordlist=FILE     Use FILE as source of passwords to try
-n, --minpw=INTEGER     Skip trying passwords shorter than this
-m, --maxpw=INTEGER     Stop when reaching this passwordlength
-l, --loadState=FILE    Continue from the state saved in FILENAME
-o, --owner             Work with the ownerpassword
-u, --user              Work with the userpassword (default)
-p, --password=STRING   Give userpassword to speed up breaking
                        ownerpassword (implies -o)
-q, --quiet             Run quietly
-s, --permutate         Try permutating the passwords (currently only
                        supports switching first character to uppercase)
-v, --version           Print version and exit
```