
10.10.171.184
10.10.181.17
10.10.165.89
10.10.75.238
10.10.165.32

22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.41 ((Ubuntu))
37370/tcp open  ftp     vsftpd 3.0.3

`http://valley.thm/pricing/note.txt`
```sh
J,
Please stop leaving notes randomly on the website
-RP
```

http://valley.thm/static/00
```sh
dev notes from valleyDev:
-add wedding photo examples
-redo the editing on #4
-remove /dev1243224123123
-check for SIEM alerts
```

view-source:http://valley.thm/dev1243224123123/dev.js
```js
...
    if (username === "siemDev" && password === "california") {
        window.location.href = "/dev1243224123123/devNotes37370.txt";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
```
username === "siemDev"
password === "california"

http://valley.thm/dev1243224123123/devNotes37370.txt
```sh
dev notes for ftp server:
-stop reusing credentials
-check for any vulnerabilies
-stay up to date on patching
-change ftp port to normal port
```
ftp: logged in with ^
three pcapng files

siemHTTP2.pcapng
```http
HTML Form URL Encoded: application/x-www-form-urlencoded
    Form item: "uname" = "valleyDev"
    Form item: "psw" = "ph0t0s1234"
    Form item: "remember" = "on"
```
"uname" = "valleyDev"
"psw" = "ph0t0s1234"

/home/valleyAuthenticator
user: valley
pass: liberty123

