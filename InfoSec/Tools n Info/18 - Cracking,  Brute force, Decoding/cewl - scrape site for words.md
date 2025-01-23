
```sh
┌──(kali㉿kali)-[~]
└─$ cewl -m 8 -w clinic.lst https://clinic.thmredteam.com/
CeWL 6.1 (Max Length) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
```

here used to generate password list with john
```sh
┌──(kali㉿kali)-[~]
└─$ john --wordlist=clinic.lst --rules=THM-Password-Attacks --stdout > clinic-pass.lst 
Using default input encoding: UTF-8
Press 'q' or Ctrl-C to abort, almost any other key for status
42000p 0:00:00:00 100.00% (2023-12-04 01:46) 381818p/s $ultricies99
```

```sh
cewl -d 2 -m 5 -w passwords.txt http://10.10.230.221 --with-numbers
```

```sh
cewl -d 0 -m 5 -w usernames.txt http://10.10.230.221/team.php --lowercase
```

```sh
┌──(kali㉿kali)-[~]
└─$ cewl -h                                   
CeWL 6.1 (Max Length) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
Usage: cewl [OPTIONS] ... <url>

    OPTIONS:
        -h, --help: Show help.
        -k, --keep: Keep the downloaded file.
        -d <x>,--depth <x>: Depth to spider to, default 2.
        -m, --min_word_length: Minimum word length, default 3.
        -x, --max_word_length: Maximum word length, default unset.
        -o, --offsite: Let the spider visit other sites.
        --exclude: A file containing a list of paths to exclude
        --allowed: A regex pattern that path must match to be followed
        -w, --write: Write the output to the file.
        -u, --ua <agent>: User agent to send.
        -n, --no-words: Don´t output the wordlist.
        -g <x>, --groups <x>: Return groups of words as well
        --lowercase: Lowercase all parsed words
        --with-numbers: Accept words with numbers in as well as just letters
        --convert-umlauts: Convert common ISO-8859-1 (Latin-1) umlauts (ä-ae, ö-oe, ü-ue, ß-ss)
        -a, --meta: include meta data.
        --meta_file file: Output file for meta data.
        -e, --email: Include email addresses.
        --email_file <file>: Output file for email addresses.
        --meta-temp-dir <dir>: The temporary directory used by exiftool when parsing files, default /tmp.
        -c, --count: Show the count for each word found.
        -v, --verbose: Verbose.
        --debug: Extra debug information.

        Authentication
        --auth_type: Digest or basic.
        --auth_user: Authentication username.
        --auth_pass: Authentication password.

        Proxy Support
        --proxy_host: Proxy host.
        --proxy_port: Proxy port, default 8080.
        --proxy_username: Username for proxy, if required.
        --proxy_password: Password for proxy, if required.

        Headers
        --header, -H: In format name:value - can pass multiple.

    <url>: The site to spider.
```

