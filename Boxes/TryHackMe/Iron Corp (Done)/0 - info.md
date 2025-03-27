
https://tryhackme.com/r/room/ironcorp

ip: 10.10.71.183
after restart: 10.10.112.197
10.10.205.123
scope: ironcorp.me

53/tcp    open  domain        Simple DNS Plus
135/tcp  open  msrpc         Microsoft Windows RPC
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815
8080/tcp open  http          Microsoft IIS httpd 10.0
|_  Potentially risky methods: TRACE
11025/tcp open  http          Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
|_  Potentially risky methods: TRACE
49667/tcp open  msrpc         Microsoft Windows RPC
49670/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

win-8vmbkf3g815.ironcorp.me ns

admin.ironcorp.me.      3600    IN      A       127.0.0.1
internal.ironcorp.me.   3600    IN      A       127.0.0.1

[11025][http-get] host: admin.ironcorp.me   login: admin   password: password123

