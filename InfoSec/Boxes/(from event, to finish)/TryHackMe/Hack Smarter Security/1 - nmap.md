
```sh
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -script vuln -Pn 10.10.14.26  
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-10 00:29 CEST
Nmap scan report for 10.10.14.26
Host is up (0.039s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           Microsoft ftpd
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
|_http-server-header: Microsoft-IIS/10.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.14.26
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://10.10.14.26:80/contact.html
|     Form id: 
|_    Form action: 
1311/tcp open  ssl/rxmon?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Tue, 09 Apr 2024 22:29:37 GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|     <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Tue, 09 Apr 2024 22:29:42 GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|_    <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
3389/tcp open  ms-wbt-server Microsoft Terminal Services
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1311-TCP:V=7.94SVN%T=SSL%I=7%D=4/10%Time=6615C151%P=x86_64-pc-linux
SF:-gnu%r(GetRequest,1089,"HTTP/1\.1\x20200\x20\r\nStrict-Transport-Securi
SF:ty:\x20max-age=0\r\nX-Frame-Options:\x20SAMEORIGIN\r\nX-Content-Type-Op
SF:tions:\x20nosniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nvary:\x20
SF:accept-encoding\r\nContent-Type:\x20text/html;charset=UTF-8\r\nDate:\x2
SF:0Tue,\x2009\x20Apr\x202024\x2022:29:37\x20GMT\r\nConnection:\x20close\r
SF:\n\r\n<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.0\x20
SF:Strict//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1-strict\.dtd\
SF:">\r\n<html>\r\n<head>\r\n<META\x20http-equiv=\"Content-Type\"\x20conte
SF:nt=\"text/html;\x20charset=UTF-8\">\r\n<title>OpenManage&trade;</title>
SF:\r\n<link\x20type=\"text/css\"\x20rel=\"stylesheet\"\x20href=\"/oma/css
SF:/loginmaster\.css\">\r\n<style\x20type=\"text/css\"></style>\r\n<script
SF:\x20type=\"text/javascript\"\x20src=\"/oma/js/prototype\.js\"\x20langua
SF:ge=\"javascript\"></script><script\x20type=\"text/javascript\"\x20src=\
SF:"/oma/js/gnavbar\.js\"\x20language=\"javascript\"></script><script\x20t
SF:ype=\"text/javascript\"\x20src=\"/oma/js/Clarity\.js\"\x20language=\"ja
SF:vascript\"></script><script\x20language=\"javascript\">\r\n\x20")%r(HTT
SF:POptions,1089,"HTTP/1\.1\x20200\x20\r\nStrict-Transport-Security:\x20ma
SF:x-age=0\r\nX-Frame-Options:\x20SAMEORIGIN\r\nX-Content-Type-Options:\x2
SF:0nosniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nvary:\x20accept-en
SF:coding\r\nContent-Type:\x20text/html;charset=UTF-8\r\nDate:\x20Tue,\x20
SF:09\x20Apr\x202024\x2022:29:42\x20GMT\r\nConnection:\x20close\r\n\r\n<!D
SF:OCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.0\x20Strict//E
SF:N\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1-strict\.dtd\">\r\n<ht
SF:ml>\r\n<head>\r\n<META\x20http-equiv=\"Content-Type\"\x20content=\"text
SF:/html;\x20charset=UTF-8\">\r\n<title>OpenManage&trade;</title>\r\n<link
SF:\x20type=\"text/css\"\x20rel=\"stylesheet\"\x20href=\"/oma/css/loginmas
SF:ter\.css\">\r\n<style\x20type=\"text/css\"></style>\r\n<script\x20type=
SF:\"text/javascript\"\x20src=\"/oma/js/prototype\.js\"\x20language=\"java
SF:script\"></script><script\x20type=\"text/javascript\"\x20src=\"/oma/js/
SF:gnavbar\.js\"\x20language=\"javascript\"></script><script\x20type=\"tex
SF:t/javascript\"\x20src=\"/oma/js/Clarity\.js\"\x20language=\"javascript\
SF:"></script><script\x20language=\"javascript\">\r\n\x20");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 201.17 seconds
```