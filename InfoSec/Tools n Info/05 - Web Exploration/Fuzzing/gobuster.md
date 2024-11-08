
#### common commands

`gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,jpg,zip`

`gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x php,htm,html,asp,shtm,shtml`

`gobuster dir -u http://shell.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,zip`
`-c "PHPSESSIONID=12123123"`


##### `dns` mode

will do a DNS lookup to the FQDN created by combining the configured domain name (-d flag) with an entry of a wordlist

`gobuster dns -d example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`

You can also make your own list using the website main page..


##### `vhost` mode

will navigate to the URL created by combining the configured HOSTNAME (-u flag) with an entry of a wordlist.

`gobuster vhost -u "http://example.thm" -w /path/to/wordlist`

`gobuster vhost -u "http://10.10.106.11" --domain example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`
(no actual dns example)

`gobuster vhost -u http://10.10.106.11 --domain offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain | grep "Status: 200"`


garr:
`gobuster dir -k -w ../../htb/iclean/raft-medium-directories-lowercase.txt -t 20 -u http://10.10.10.10`

| Gobuster flag       | Description                               |
| ------------------- | ----------------------------------------- |
| -e                  | Print the full URLs in your console       |
| -u                  | The target URL                            |
| -w                  | Path to your wordlist                     |
| -U and -P           | Username and Password for Basic Auth      |
| -p **<x>**          | Proxy to use for requests                 |
| -r                  | Follow redirects                          |
| `-c <http cookies>` | Specify a cookie for simulating your auth |

### dir

| Flag | Long Flag                  | Description                                                                                                                                                                                                                   |
| ---- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-c` | `--cookies`                | This flag configures a cookie to pass along each request, such as a session ID.                                                                                                                                               |
| `-x` | `--extensions`             | This flag specifies which file extensions you want to scan for. E.g., .php, .js                                                                                                                                               |
| `-H` | `--headers`                | This flag configures an entire header to pass along with each request.                                                                                                                                                        |
| `-k` | `--no-tls-validation`      | This flag  skips the process that checks the certificate when https is used. It often happens for CTF events or test rooms like the ones on THM a self-signed certificate is used. This causes an error during the TLS check. |
| `-n` | `--no-status`              | You can set this flag when you don’t want to see status codes of each response received. This helps keep the output on the screen clear.                                                                                      |
| `-P` | `password`                 | You can set this flag together with the --username flag to execute authenticated requests. This is handy when you have obtained credentials from a user.                                                                      |
| `-s` | `--status-codes`           | With this flag, you can configure which status codes of the received responses you want to display, such as 200, or a range like 300-400.                                                                                     |
| `-b` | `--status-codes-blacklist` | This flag allows you to configure which status codes of the received responses you don’t want to display. Configuring this flag overrides the -s flag.                                                                        |
| `-U` | `--username`               | You can set this flag together with the `--password` flag to execute authenticated requests. This is handy when you have obtained credentials from a user.                                                                    |
| `-r` | `--followredirect`         | This flags configures Gobuster to follow the redirect that it received as a response to the sent request. A HTTP redirect status code (e.g., 301 or 302) is used to redirect the client to a different URL.                   |

### dns subdomain

| Flag | Long Flag      | Description                                                                       |
| ---- | -------------- | --------------------------------------------------------------------------------- |
| `-c` | `--show-cname` | Show CNAME Records (cannot be used with the `-i` flag).                           |
| `-i` | `--show-ips`   | Including this flag shows IP addresses that the domain and subdomains resolve to. |
| `-r` | `--resolver`   | This flag configures a custom DNS server to use for resolving.                    |
| `-d` | `--domain`     | This flag configures the domain you want to enumerate.                            |

### vhost

| **Short Flag** | **Long Flag**       | **Description**                                                                                       |
| -------------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| `-u`           | `--url`             | Specifies the base URL (target domain) for brute-forcing virtual hostnames.                           |
|                | `--append-domain`   | Appends the base domain to each word in the wordlist (e.g., word.example.com).                        |
| `-m`           | `--method`          | Specifies the HTTP method to use for the requests (e.g., GET, POST).                                  |
|                | `--domain`          | Appends a domain to each wordlist entry to form a valid hostname (useful if not provided explicitly). |
|                | `--exclude-length`  | Excludes results based on the length of the response body (useful to filter out unwanted responses).  |
| `-r`           | `--follow-redirect` | Follows HTTP redirects (useful for cases where subdomains may redirect).                              |

#### help
 
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
      --no-error              Don´t display errors
  -z, --no-progress           Don´t display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don´t print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)

Use "gobuster [command] --help" for more information about a command.
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dir --help            
Uses directory/file enumeration mode

Usage:
  gobuster dir [flags]

Flags:
  -f, --add-slash                         Append / to each request
      --client-cert-p12 string            a p12 file to use for options TLS client certificates
      --client-cert-p12-password string   the password to the p12 file
      --client-cert-pem string            public key in PEM format for optional TLS client certificates
      --client-cert-pem-key string        private key in PEM format for optional TLS client certificates (this key needs to have no password)
  -c, --cookies string                    Cookies to use for the requests
  -d, --discover-backup                   Also search for backup files by appending multiple backup extensions
      --exclude-length string             exclude the following content lengths (completely ignores the status). You can separate multiple lengths by comma and it also supports ranges like 203-206
  -e, --expanded                          Expanded mode, print full URLs
  -x, --extensions string                 File extension(s) to search for
  -X, --extensions-file string            Read file extension(s) to search from the file
  -r, --follow-redirect                   Follow redirects
  -H, --headers stringArray               Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                              help for dir
      --hide-length                       Hide the length of the body in the output
  -m, --method string                     Use the following HTTP method (default "GET")
      --no-canonicalize-headers           Do not canonicalize HTTP header names. If set header names are sent as is.
  -n, --no-status                         Don´t print status codes
  -k, --no-tls-validation                 Skip TLS certificate verification
  -P, --password string                   Password for Basic Auth
      --proxy string                      Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
      --random-agent                      Use a random User-Agent string
      --retry                             Should retry on request timeout
      --retry-attempts int                Times to retry on request timeout (default 3)
  -s, --status-codes string               Positive status codes (will be overwritten with status-codes-blacklist if set). Can also handle ranges like 200,300-400,404.
  -b, --status-codes-blacklist string     Negative status codes (will override status-codes if set). Can also handle ranges like 200,300-400,404. (default "404")
      --timeout duration                  HTTP Timeout (default 10s)
  -u, --url string                        The target URL
  -a, --useragent string                  Set the User-Agent string (default "gobuster/3.6")
  -U, --username string                   Username for Basic Auth

Global Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
      --no-color              Disable color output
      --no-error              Don´t display errors
  -z, --no-progress           Don´t display progress
  -o, --output string         Output file to write results to (defaults to stdout)
  -p, --pattern string        File containing replacement patterns
  -q, --quiet                 Don´t print the banner and other noise
  -t, --threads int           Number of concurrent threads (default 10)
  -v, --verbose               Verbose output (errors)
  -w, --wordlist string       Path to the wordlist. Set to - to use STDIN.
      --wordlist-offset int   Resume from a given position in the wordlist (defaults to 0)
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster dns --help
Uses DNS subdomain enumeration mode

Usage:
  gobuster dns [flags]

Flags:
  -d, --domain string      The target domain
  -h, --help               help for dns
      --no-fqdn            Do not automatically add a trailing dot to the domain, so the resolver uses the DNS search domain
  -r, --resolver string    Use custom DNS server (format server.com or server.com:port)
  -c, --show-cname         Show CNAME records (cannot be used with '-i' option)
  -i, --show-ips           Show IP addresses
      --timeout duration   DNS resolver timeout (default 1s)
      --wildcard           Force continued operation when wildcard found

Global Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
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
```

```sh
┌──(kali㉿kali)-[~]
└─$ gobuster vhost --help
Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)

Usage:
  gobuster vhost [flags]

Flags:
      --append-domain                     Append main domain from URL to words from wordlist. Otherwise the fully qualified domains need to be specified in the wordlist.
      --client-cert-p12 string            a p12 file to use for options TLS client certificates
      --client-cert-p12-password string   the password to the p12 file
      --client-cert-pem string            public key in PEM format for optional TLS client certificates
      --client-cert-pem-key string        private key in PEM format for optional TLS client certificates (this key needs to have no password)
  -c, --cookies string                    Cookies to use for the requests
      --domain string                     the domain to append when using an IP address as URL. If left empty and you specify a domain based URL the hostname from the URL is extracted
      --exclude-length string             exclude the following content lengths (completely ignores the status). You can separate multiple lengths by comma and it also supports ranges like 203-206
  -r, --follow-redirect                   Follow redirects
  -H, --headers stringArray               Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                              help for vhost
  -m, --method string                     Use the following HTTP method (default "GET")
      --no-canonicalize-headers           Do not canonicalize HTTP header names. If set header names are sent as is.
  -k, --no-tls-validation                 Skip TLS certificate verification
  -P, --password string                   Password for Basic Auth
      --proxy string                      Proxy to use for requests [http(s)://host:port] or [socks5://host:port]
      --random-agent                      Use a random User-Agent string
      --retry                             Should retry on request timeout
      --retry-attempts int                Times to retry on request timeout (default 3)
      --timeout duration                  HTTP Timeout (default 10s)
  -u, --url string                        The target URL
  -a, --useragent string                  Set the User-Agent string (default "gobuster/3.6")
  -U, --username string                   Username for Basic Auth

Global Flags:
      --debug                 Enable debug output
      --delay duration        Time each thread waits between requests (e.g. 1500ms)
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
```

