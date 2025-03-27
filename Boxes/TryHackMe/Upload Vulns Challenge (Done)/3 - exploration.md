
```js
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

```