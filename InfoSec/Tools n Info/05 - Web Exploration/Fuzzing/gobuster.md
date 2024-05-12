
|                     |                                           |
| ------------------- | ----------------------------------------- |
| **Gobuster flag**   | **Description**                           |
| -e                  | Print the full URLs in your console       |
| -u                  | The target URL                            |
| -w                  | Path to your wordlist                     |
| -U and -P           | Username and Password for Basic Auth      |
| -p **<x>**          | Proxy to use for requests                 |
| `-c <http cookies>` | Specify a cookie for simulating your auth |
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
  -n, --no-status                         Don't print status codes
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

#### common commands

`gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,jpg,zip`

`gobuster dir -u http://10.10.183.107/webmasters/backups -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x php,htm,html,asp,shtm,shtml`

`gobuster dir -u http://shell.uploadvulns.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -x txt,zip`
`-c "PHPSESSIONID=12123123"`

