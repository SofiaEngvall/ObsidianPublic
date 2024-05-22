
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.171.184
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-16 15:11 CEST
Nmap scan report for 10.10.171.184
Host is up (0.044s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c2:84:2a:c1:22:5a:10:f1:66:16:dd:a0:f6:04:62:95 (RSA)
|   256 42:9e:2f:f6:3e:5a:db:51:99:62:71:c4:8c:22:3e:bb (ECDSA)
|_  256 2e:a0:a5:6c:d9:83:e0:01:6c:b9:8a:60:9b:63:86:72 (ED25519)
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Site doesn´t have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
37370/tcp open  ftp     vsftpd 3.0.3
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.32 seconds
```

22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
37370/tcp open  ftp     vsftpd 3.0.3

```sh
┌──(kali㉿kali)-[~]
└─$ sudo nmap -v -sS -n -p80 --script "http*" 10.10.171.184
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-16 17:47 CEST
NSE: Loaded 135 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 17:47
Completed NSE at 17:47, 0.00s elapsed
Initiating NSE at 17:47
Completed NSE at 17:47, 0.00s elapsed
Pre-scan script results:
|_http-robtex-shared-ns: *TEMPORARILY DISABLED* due to changes in Robtex´s API. See https://www.robtex.com/api/
Initiating Ping Scan at 17:47
Scanning 10.10.171.184 [4 ports]
Completed Ping Scan at 17:47, 0.06s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 17:47
Scanning 10.10.171.184 [1 port]
Discovered open port 80/tcp on 10.10.171.184
Completed SYN Stealth Scan at 17:47, 0.06s elapsed (1 total ports)
NSE: Script scanning 10.10.171.184.
Initiating NSE at 17:47
NSE Timing: About 3.16% done; ETC: 18:03 (0:15:49 remaining)
NSE Timing: About 3.16% done; ETC: 18:19 (0:31:07 remaining)
NSE Timing: About 3.16% done; ETC: 18:35 (0:46:25 remaining)
NSE Timing: About 4.81% done; ETC: 18:29 (0:39:52 remaining)
NSE Timing: About 4.96% done; ETC: 18:37 (0:48:11 remaining)
NSE Timing: About 4.96% done; ETC: 18:47 (0:57:45 remaining)
NSE Timing: About 6.60% done; ETC: 18:40 (0:49:44 remaining)
NSE Timing: About 6.90% done; ETC: 18:45 (0:54:11 remaining)
NSE Timing: About 6.90% done; ETC: 18:52 (1:00:55 remaining)
NSE Timing: About 6.90% done; ETC: 18:59 (1:07:40 remaining)
NSE Timing: About 8.73% done; ETC: 18:50 (0:57:41 remaining)
NSE Timing: About 8.73% done; ETC: 18:56 (1:02:54 remaining)
NSE Timing: About 8.73% done; ETC: 19:01 (1:08:08 remaining)
NSE Timing: About 10.06% done; ETC: 18:56 (1:02:43 remaining)
NSE Timing: About 10.20% done; ETC: 19:01 (1:06:37 remaining)
NSE Timing: About 10.20% done; ETC: 19:06 (1:11:01 remaining)
NSE Timing: About 11.52% done; ETC: 19:01 (1:05:48 remaining)
NSE Timing: About 11.72% done; ETC: 19:06 (1:09:46 remaining)
NSE Timing: About 11.72% done; ETC: 19:10 (1:13:55 remaining)
NSE Timing: About 13.00% done; ETC: 19:06 (1:09:01 remaining)
NSE Timing: About 13.14% done; ETC: 19:11 (1:13:11 remaining)
NSE Timing: About 13.14% done; ETC: 19:16 (1:17:29 remaining)
NSE Timing: About 14.77% done; ETC: 19:09 (1:10:30 remaining)
NSE Timing: About 14.77% done; ETC: 19:14 (1:14:49 remaining)
NSE Timing: About 16.13% done; ETC: 19:10 (1:10:02 remaining)
NSE Timing: About 16.52% done; ETC: 19:16 (1:14:23 remaining)
NSE Timing: About 20.95% done; ETC: 19:15 (1:09:51 remaining)
NSE Timing: About 39.50% done; ETC: 19:03 (0:46:03 remaining)
NSE Timing: About 97.26% done; ETC: 18:18 (0:00:52 remaining)
NSE Timing: About 97.95% done; ETC: 18:19 (0:00:40 remaining)
Completed NSE at 18:19, 1960.20s elapsed
Initiating NSE at 18:19
Completed NSE at 18:19, 0.41s elapsed
Nmap scan report for 10.10.171.184
Host is up (0.039s latency).

Bug in http-security-headers: no string output.
PORT   STATE SERVICE
80/tcp open  http
|_http-chrono: Request times for /; avg: 337.96ms; min: 271.20ms; max: 402.86ms
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; css: 1; html: 1
|     /gallery/
|       html: 1
|     /pricing/
|       html: 1
|     /static/
|       Other: 3
|   Longest directory structure:
|     Depth: 1
|     Dir: /gallery/
|   Total files found (by extension):
|_    Other: 4; css: 1; html: 3
|_http-feed: Couldn´t find any feeds.
|_http-malware-host: Host appears to be clean
| http-vhosts: 
| devel
| git
|_126 names had status 200
|_http-title: Site doesn´t have a title (text/html).
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-brute:   
|_  Path "/" does not require authentication
|_http-comments-displayer: Couldn´t find any comments.
|_http-slowloris: false
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn´t find wp-login.php
|_http-csrf: Couldn´t find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn´t find any DOM based XSS.
| http-php-version: Logo query returned unknown hash 4ae85e5628ee1085798fbc9978fada14
|_Credits query returned unknown hash 4ae85e5628ee1085798fbc9978fada14
|_http-jsonp-detection: Couldn´t find any JSONP endpoints.
|_http-xssed: No previously reported XSS vuln.
| http-grep: 
|   (1) http://10.10.171.184:80/js/art.js: 
|     (1) ip: 
|_      + 10.10.171.184
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-date: Thu, 16 May 2024 16:17:25 GMT; -1s from local time.
|_http-errors: ERROR: Script execution failed (use -d to debug)
|_http-referer-checker: Couldn´t find any cross-domain scripts.
|_http-mobileversion-checker: No mobile version detected.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-headers: 
|   Date: Thu, 16 May 2024 16:17:24 GMT
|   Server: Apache/2.4.41 (Ubuntu)
|   Last-Modified: Tue, 07 Mar 2023 23:11:16 GMT
|   ETag: "48b-5f6578751d51c"
|   Accept-Ranges: bytes
|   Content-Length: 1163
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-stored-xss: Couldn´t find any stored XSS vulnerabilities.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-devframework: Couldn´t determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.

NSE: Script Post-scanning.
Initiating NSE at 18:19
Completed NSE at 18:19, 0.00s elapsed
Initiating NSE at 18:19
Completed NSE at 18:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 1961.20 seconds
           Raw packets sent: 5 (196B) | Rcvd: 2 (84B)
```