```http
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Sun, 03 Mar 2024 19:34:04 GMT
Content-Type: application/javascript
Content-Length: 691
Connection: close
Last-Modified: Sun, 24 May 2020 21:27:26 GMT
ETag: "2b3-5a66b8758ab80-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Front-End-Https: on
```

```js
window.onload = function(){
	var upload = document.getElementById("fileSelect");
	var responseMsg = document.getElementsByClassName("responseMsg")[0];
	var errorMsg = document.getElementById("errorMsg");
	var uploadMsg = document.getElementById("uploadtext");
	upload.value="";
	upload.addEventListener("change",function(event){
		var file = this.files[0];
		responseMsg.style = "display:none;";
		if (file.type != "image/png"){
			upload.value = "";
			uploadMsg.style = "display:none;";
			error();
		} else{
			uploadMsg.innerHTML = "Chosen File: " + upload.value.split(/(\\|\/)/g).pop();
			responseMsg.style="display:none;";
			errorMsg.style="display:none;";
			success();
		}
	});
};
```