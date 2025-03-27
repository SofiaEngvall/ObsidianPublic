
```sh
┌──(kali㉿kali)-[~/thm/valley]
└─$ ftp 10.10.165.89 37370
Connected to 10.10.165.89.
220 (vsFTPd 3.0.3)
Name (10.10.165.89:kali): siemDev
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||18332|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000         7272 Mar 06  2023 siemFTP.pcapng
-rw-rw-r--    1 1000     1000      1978716 Mar 06  2023 siemHTTP1.pcapng
-rw-rw-r--    1 1000     1000      1972448 Mar 06  2023 siemHTTP2.pcapng
226 Directory send OK.
ftp> mget *
mget siemFTP.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||63381|)
150 Opening BINARY mode data connection for siemFTP.pcapng (7272 bytes).
100% |********************************************************************************|  7272       29.89 MiB/s    00:00 ETA
226 Transfer complete.
7272 bytes received in 00:00 (175.16 KiB/s)
mget siemHTTP1.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||6227|)
150 Opening BINARY mode data connection for siemHTTP1.pcapng (1978716 bytes).
100% |********************************************************************************|  1932 KiB    1.28 MiB/s    00:00 ETA
226 Transfer complete.
1978716 bytes received in 00:01 (1.24 MiB/s)
mget siemHTTP2.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||9370|)
150 Opening BINARY mode data connection for siemHTTP2.pcapng (1972448 bytes).
100% |********************************************************************************|  1926 KiB    1.19 MiB/s    00:00 ETA
226 Transfer complete.
1972448 bytes received in 00:01 (1.16 MiB/s)
ftp> exit
221 Goodbye.
```

