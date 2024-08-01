
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -p- -sC -sV -Pn 10.10.11.12
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-11 23:04 CEST
Nmap scan report for capiclean.htb (10.10.11.12)
Host is up (0.040s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 2c:f9:07:77:e3:f1:3a:36:db:f2:3b:94:e3:b7:cf:b2 (ECDSA)
|_  256 4a:91:9f:f2:74:c0:41:81:52:4d:f1:ff:2d:01:78:6b (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
| http-server-header: 
|   Apache/2.4.52 (Ubuntu)
|_  Werkzeug/2.3.7 Python/3.10.12
|_http-title: Capiclean
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.82 seconds
```

```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -script vuln -Pn 10.10.11.12 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-11 21:00 CEST
Nmap scan report for 10.10.11.12
Host is up (0.029s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| vulners: 
|   cpe:/a:openbsd:openssh:8.9p1: 
|       CVE-2012-1577   7.5     https://vulners.com/cve/CVE-2012-1577
|       CVE-2010-4816   5.0     https://vulners.com/cve/CVE-2010-4816
|_      CVE-2023-51767  3.5     https://vulners.com/cve/CVE-2023-51767
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-stored-xss: Couldn´t find any stored XSS vulnerabilities.
|_http-csrf: Couldn´t find any CSRF vulnerabilities.
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-dombased-xss: Couldn´t find any DOM based XSS.
| vulners: 
|   cpe:/a:apache:http_server:2.4.52: 
|       PACKETSTORM:176334      7.5     https://vulners.com/packetstorm/PACKETSTORM:176334      *EXPLOIT*
|       OSV:BIT-APACHE-2023-25690       7.5     https://vulners.com/osv/OSV:BIT-APACHE-2023-25690
|       OSV:BIT-APACHE-2022-31813       7.5     https://vulners.com/osv/OSV:BIT-APACHE-2022-31813
|       CVE-2023-25690  7.5     https://vulners.com/cve/CVE-2023-25690
|       CVE-2022-31813  7.5     https://vulners.com/cve/CVE-2022-31813
|       CVE-2022-23943  7.5     https://vulners.com/cve/CVE-2022-23943
|       CVE-2022-22720  7.5     https://vulners.com/cve/CVE-2022-22720
|       CNVD-2022-73123 7.5     https://vulners.com/cnvd/CNVD-2022-73123
|       5C1BB960-90C1-5EBF-9BEF-F58BFFDFEED9    7.5     https://vulners.com/githubexploit/5C1BB960-90C1-5EBF-9BEF-F58BFFDFEED9*EXPLOIT*
|       3F17CA20-788F-5C45-88B3-E12DB2979B7B    7.5     https://vulners.com/githubexploit/3F17CA20-788F-5C45-88B3-E12DB2979B7B*EXPLOIT*
|       1337DAY-ID-39214        7.5     https://vulners.com/zdt/1337DAY-ID-39214        *EXPLOIT*
|       OSV:BIT-APACHE-2022-28615       6.4     https://vulners.com/osv/OSV:BIT-APACHE-2022-28615
|       OSV:BIT-2023-31122      6.4     https://vulners.com/osv/OSV:BIT-2023-31122
|       CVE-2022-28615  6.4     https://vulners.com/cve/CVE-2022-28615
|       CVE-2021-44224  6.4     https://vulners.com/cve/CVE-2021-44224
|       CVE-2022-22721  5.8     https://vulners.com/cve/CVE-2022-22721
|       OSV:BIT-APACHE-2022-36760       5.1     https://vulners.com/osv/OSV:BIT-APACHE-2022-36760
|       CVE-2022-36760  5.1     https://vulners.com/cve/CVE-2022-36760
|       OSV:BIT-APACHE-2023-45802       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2023-45802
|       OSV:BIT-APACHE-2023-43622       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2023-43622
|       OSV:BIT-APACHE-2023-31122       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2023-31122
|       OSV:BIT-APACHE-2023-27522       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2023-27522
|       OSV:BIT-APACHE-2022-37436       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-37436
|       OSV:BIT-APACHE-2022-30556       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-30556
|       OSV:BIT-APACHE-2022-30522       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-30522
|       OSV:BIT-APACHE-2022-29404       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-29404
|       OSV:BIT-APACHE-2022-28614       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-28614
|       OSV:BIT-APACHE-2022-28330       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-28330
|       OSV:BIT-APACHE-2022-26377       5.0     https://vulners.com/osv/OSV:BIT-APACHE-2022-26377
|       OSV:BIT-2023-45802      5.0     https://vulners.com/osv/OSV:BIT-2023-45802
|       OSV:BIT-2023-43622      5.0     https://vulners.com/osv/OSV:BIT-2023-43622
|       F7F6E599-CEF4-5E03-8E10-FE18C4101E38    5.0     https://vulners.com/githubexploit/F7F6E599-CEF4-5E03-8E10-FE18C4101E38*EXPLOIT*
|       E5C174E5-D6E8-56E0-8403-D287DE52EB3F    5.0     https://vulners.com/githubexploit/E5C174E5-D6E8-56E0-8403-D287DE52EB3F*EXPLOIT*
|       DB6E1BBD-08B1-574D-A351-7D6BB9898A4A    5.0     https://vulners.com/githubexploit/DB6E1BBD-08B1-574D-A351-7D6BB9898A4A*EXPLOIT*
|       CVE-2023-31122  5.0     https://vulners.com/cve/CVE-2023-31122
|       CVE-2023-27522  5.0     https://vulners.com/cve/CVE-2023-27522
|       CVE-2022-37436  5.0     https://vulners.com/cve/CVE-2022-37436
|       CVE-2022-30556  5.0     https://vulners.com/cve/CVE-2022-30556
|       CVE-2022-29404  5.0     https://vulners.com/cve/CVE-2022-29404
|       CVE-2022-28614  5.0     https://vulners.com/cve/CVE-2022-28614
|       CVE-2022-26377  5.0     https://vulners.com/cve/CVE-2022-26377
|       CVE-2022-22719  5.0     https://vulners.com/cve/CVE-2022-22719
|       CVE-2006-20001  5.0     https://vulners.com/cve/CVE-2006-20001
|       CNVD-2023-93320 5.0     https://vulners.com/cnvd/CNVD-2023-93320
|       CNVD-2023-80558 5.0     https://vulners.com/cnvd/CNVD-2023-80558
|       CNVD-2022-73122 5.0     https://vulners.com/cnvd/CNVD-2022-73122
|       CNVD-2022-53584 5.0     https://vulners.com/cnvd/CNVD-2022-53584
|       CNVD-2022-53582 5.0     https://vulners.com/cnvd/CNVD-2022-53582
|       B0208442-6E17-5772-B12D-B5BE30FA5540    5.0     https://vulners.com/githubexploit/B0208442-6E17-5772-B12D-B5BE30FA5540*EXPLOIT*
|       A820A056-9F91-5059-B0BC-8D92C7A31A52    5.0     https://vulners.com/githubexploit/A820A056-9F91-5059-B0BC-8D92C7A31A52*EXPLOIT*
|       9814661A-35A4-5DB7-BB25-A1040F365C81    5.0     https://vulners.com/githubexploit/9814661A-35A4-5DB7-BB25-A1040F365C81*EXPLOIT*
|       5A864BCC-B490-5532-83AB-2E4109BB3C31    5.0     https://vulners.com/githubexploit/5A864BCC-B490-5532-83AB-2E4109BB3C31*EXPLOIT*
|       CVE-2016-8612   3.3     https://vulners.com/cve/CVE-2016-8612
|       CVE-2023-45802  2.6     https://vulners.com/cve/CVE-2023-45802
|       OSV:BIT-APACHE-2024-27316       0.0     https://vulners.com/osv/OSV:BIT-APACHE-2024-27316
|       OSV:BIT-APACHE-2024-24795       0.0     https://vulners.com/osv/OSV:BIT-APACHE-2024-24795
|       OSV:BIT-APACHE-2023-38709       0.0     https://vulners.com/osv/OSV:BIT-APACHE-2023-38709
|_      B0A9E5E8-7CCC-5984-9922-A89F11D6BF38    0.0     https://vulners.com/githubexploit/B0A9E5E8-7CCC-5984-9922-A89F11D6BF38*EXPLOIT*
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.18 seconds
```
