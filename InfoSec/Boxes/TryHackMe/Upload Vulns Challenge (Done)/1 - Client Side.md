
Made a copy of pentest monkeys revsh.php and:
- renamed it shell.jpg.php
- added the magic number for jpg to the start of the file (added 1234 in nano and then hexedited the file to set the numbers)


Changing script to confirm that the client side script does not catch out revsh
Adding console.log("...");

upload.js
```js
$(document).ready(function () {
  let errorTimeout;
  const fadeSpeed = 1000;
  function setResponseMsg(responseTxt, colour) {
    $("#responseMsg").text(responseTxt);
    if (!$("#responseMsg").is(":visible")) {
      $("#responseMsg").css({ color: colour }).fadeIn(fadeSpeed);
    } else {
      $("#responseMsg").animate({ color: colour }, fadeSpeed);
    }
    clearTimeout(errorTimeout);
    errorTimeout = setTimeout(() => {
      $("#responseMsg").fadeOut(fadeSpeed);
    }, 5000);
  }
  $("#uploadBtn").click(function () {
    $("#fileSelect").click();
  });
  $("#fileSelect").change(function () {
    const fileBox = document.getElementById("fileSelect").files[0];
    const reader = new FileReader();
    reader.readAsDataURL(fileBox);
    reader.onload = function (event) {

	  console.log("In function!");

	  //Check File Size
      if (event.target.result.length > 50 * 8 * 1024) {
        setResponseMsg("File too big", "red");
        return;
      }
      //Check Magic Number
      if (atob(event.target.result.split(",")[1]).slice(0, 3) != "ÿØÿ") {
        setResponseMsg("Invalid file format", "red");
        console.log("Check Magic Number");
        return;
      }
      //Check File Extension
      const extension = fileBox.name.split(".")[1].toLowerCase();
      if (extension != "jpg" && extension != "jpeg") {
        setResponseMsg("Invalid file format", "red");
        console.log("Check File Extension");
        return;
      }

      const text = {
        success: "File successfully uploaded",
        failure: "No file selected",
        invalid: "Invalid file type",
      };
      $.ajax("/", {
        data: JSON.stringify({
          name: fileBox.name,
          type: fileBox.type,
          file: event.target.result,
        }),
        contentType: "application/json",
        type: "POST",
        success: function (data) {
          let colour = "";
          switch (data) {
            case "success":
              colour = "green";
              break;
            case "failure":
            case "invalid":
              colour = "red";
              break;
          }
          setResponseMsg(text[data], colour);
        },
      });
    };
  });
});

```

Confirmed server side catch. If statements not true:

![[Images/Pasted image 20240401092725.png|900]]

reply from server for actual jpg:

```http
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Mon, 01 Apr 2024 06:10:15 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 7
Connection: close
X-Powered-By: Express
Access-Control-Allow-Origin: *
ETag: W/"7-U6VofLJtxB8qtAM+l+E63v03QNY"
Front-End-Https: on

success
```

reply for shell.jpg.php

```http
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Mon, 01 Apr 2024 06:10:19 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 7
Connection: close
X-Powered-By: Express
Access-Control-Allow-Origin: *
ETag: W/"7-gfNEp2hqgLTFKT6P3AsBYMgsBqg"
Front-End-Https: on

invalid
```

#### Alternative client side

just sending straight from burp, no js messing about

Real image: (Obs the X-Powered-By: Express. This means node js. We're still using out php revsh to test with.)
![[Images/Pasted image 20240401195749.png]]

shell with .jpg extension
![[Images/Pasted image 20240401200125.png]]

shell with .jpg.php extension
![[Images/Pasted image 20240401195854.png]]

