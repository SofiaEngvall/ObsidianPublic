
clients
Adell Smith
Kyle Butler
Kyle Butler

there's a contact form

page with file upload
http://10.10.11.229/upload.php#


```html
<meta name="description" content="Start your development with Creative Design landing page.">
<meta name="author" content="Devcrud">

<!-- Submit File -->
<form id="zip-form" enctype="multipart/form-data" method="post" action="upload.php">
	<div class="mb-3">
		<input type="file" class="form-control" name="zipFile" accept=".zip">
	</div>
	<button type="submit" class="btn btn-primary" name="submit">Upload</button>
</form><!-- End submit file -->

<p>Made by <a href="https://github.com/xdann1">xDaNN1</p>
```


![[upload-page.png]]


Wants a zip file. I'll try php first

uploaded php rev shell php-reverse-shell.php
searching for php files with gobuster

dir called uploads found, access forbidden

http://10.10.11.229/uploads/php-reverse-shell.php, not found
http://10.10.11.229/assets/php-reverse-shell.php, not found

oh, noticed there's a small error uploading file on the page

tried renaming file tp zip. still failed

googling zip exploits

https://www.google.com/search?client=firefox-b-d&q=malicious+zip+file+upload

https://www.onsecurity.io/blog/file-upload-checklist/#zipslip



