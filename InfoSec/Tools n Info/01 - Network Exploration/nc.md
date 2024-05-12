
| netcat as client | `nc 10.10.18.110 PORT_NUMBER` |
| ---------------- | ----------------------------- |
| netcat as server | `nc -lvnp PORT_NUMBER`        |

| option | meaning                                                    |
| ------ | ---------------------------------------------------------- |
| -l     | Listen mode                                                |
| -p     | Specify the Port number                                    |
| -n     | Numeric only; no resolution of hostnames via DNS           |
| -v     | Verbose output (optional, yet useful to discover any bugs) |
| -vv    | Very Verbose (optional)                                    |
| -k     | Keep listening after client disconnects                    |
- the option `-p` should appear just before the port number you want to listen on.
- the option `-n` will avoid DNS lookups and warnings.
- port numbers less than 1024 require root privileges to listen on.

can be used like telnet to grab the banner of a tcp service
you might need to use shift+enter sometimes, like after a GET http command

```sh
┌──(kali㉿kali)-[~]
└─$ nc 10.10.18.110 21
220 debra2.thm.local FTP server (Version 6.4/OpenBSD/Linux-ftpd-0.17) ready.
help
214- The following commands are recognized (* =>´s unimplemented).
   USER    PORT    MODE    MSND*   REST    XCWD    HELP    PWD     MDTM 
   PASS    PASV    RETR    MSOM*   RNFR    LIST    NOOP    XPWD 
   ACCT*   EPRT    STOR    MSAM*   RNTO    NLST    MKD     CDUP 
   SMNT*   EPSV    APPE    MRSQ*   ABOR    SITE    XMKD    XCUP 
   REIN*   TYPE    MLFL*   MRCP*   DELE    SYST    RMD     STOU 
   QUIT    STRU    MAIL*   ALLO    CWD     STAT    XRMD    SIZE 
214 Direct comments to ftp-bugs@debra2.thm.local.
list
530 Please login with USER and PASS.
quit
221 Goodbye.
```

```sh
┌──(kali㉿kali)-[~]
└─$ nc 10.10.18.110 80               
GET / HTTP/1.1
host: nc

HTTP/1.1 200 OK
Server: nginx/1.6.2
Date: Sat, 04 May 2024 15:24:11 GMT
Content-Type: text/html
Content-Length: 867
Last-Modified: Fri, 08 Oct 2021 04:30:27 GMT
Connection: keep-alive
ETag: "615fc963-363"
Accept-Ranges: bytes

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx on Debian!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx on Debian!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working on Debian. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a></p>

<p>
      Please use the <tt>reportbug</tt> tool to report bugs in the
      nginx package with Debian. However, check <a
      href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=nginx;repeatmerged=0">existing
      bug reports</a> before reporting a new bug.
</p>

<p><em>Thank you for using debian and nginx.</em></p>


</body>
</html>

```