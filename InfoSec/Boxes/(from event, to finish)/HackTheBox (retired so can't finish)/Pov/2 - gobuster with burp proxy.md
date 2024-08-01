
```sh
┌──(kali㉿kali)-[~]
└─$ gobuster --help                                         
Usage:
  gobuster [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  dir         Uses directory/file enumeration mode
  dns         Uses DNS subdomain enumeration mode
  fuzz        Uses fuzzing mode. Replaces the keyword FUZZ in the URL, Headers and the request body
  gcs         Uses gcs bucket enumeration mode
  help        Help about any command
  s3          Uses aws bucket enumeration mode
  tftp        Uses TFTP enumeration mode
  version     shows the current version
  vhost       Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)

Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
  -h, --help                  help for gobuster
      --no-color              Disable color output
      --no-error              Don't display errors
  -z, --no-progress           Don't display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don't print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)

Use "gobuster [command] --help" for more information about a command.
                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ gobuster --help | grep roxy
                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ gobuster dir --help | grep roxy
      --proxy string                      Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ gobuster dir --proxy http://127.0.0.1:8000 -u http://10.10.11.251 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.251
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Proxy:                   http://127.0.0.1:8000
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================

Error: error on running gobuster: unable to connect to http://10.10.11.251/: Get "http://10.10.11.251/": proxyconnect tcp: dial tcp 127.0.0.1:8000: connect: connection refused
                                                                                                                                                                                             
┌──(kali㉿kali)-[~]
└─$ gobuster dir --proxy http://127.0.0.1:8080 -u http://10.10.11.251 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,php 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.251
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Proxy:                   http://127.0.0.1:8080
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/img                  (Status: 301) [Size: 147] [--> http://10.10.11.251/img/]
/css                  (Status: 301) [Size: 147] [--> http://10.10.11.251/css/]
/js                   (Status: 301) [Size: 146] [--> http://10.10.11.251/js/]
Progress: 5909 / 661683 (0.89%)[ERROR] Get "http://10.10.11.251/sample.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 12341 / 661683 (1.87%)[ERROR] Get "http://10.10.11.251/m5.txt": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 12383 / 661683 (1.87%)[ERROR] Get "http://10.10.11.251/g2": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/IMG                  (Status: 301) [Size: 147] [--> http://10.10.11.251/IMG/]
/*checkout*           (Status: 400) [Size: 3420]
/CSS                  (Status: 301) [Size: 147] [--> http://10.10.11.251/CSS/]
/Img                  (Status: 301) [Size: 147] [--> http://10.10.11.251/Img/]
/JS                   (Status: 301) [Size: 146] [--> http://10.10.11.251/JS/]
/*docroot*            (Status: 400) [Size: 3420]
/*                    (Status: 400) [Size: 3420]
/http%3A%2F%2Fwww     (Status: 400) [Size: 3420]
/http%3A              (Status: 400) [Size: 3420]
/q%26a                (Status: 400) [Size: 3420]
/**http%3a            (Status: 400) [Size: 3420]
/*http%3A             (Status: 400) [Size: 3420]
/**http%3A            (Status: 400) [Size: 3420]
/http%3A%2F%2Fyoutube (Status: 400) [Size: 3420]
Progress: 178338 / 661683 (26.95%)[ERROR] Get "http://10.10.11.251/36665": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 203649 / 661683 (30.78%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 203649 / 661683 (30.78%)
===============================================================
Finished
===============================================================
```