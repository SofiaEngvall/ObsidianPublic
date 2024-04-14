
### URI – Syntax

```html
<scheme>:<authority>/<path>?<query>#<fragment>
```

- scheme
	The protocol to use to request the resource
- authority
	The entity that controls the interpretation of the rest of the URI
	Usually a server name
		``<username>@<host>:<port>``
- path
	Usually a hierarchical pathname composed of “/” separated strings
- query
	Used to pass non-hierarchical data
- fragment
	Used to identify a subsection or subresource of the resource

URI can contain –../../people.html

## Requests

An HTTP request consists of:
- method
- resource (derived from the URI)
- protocol version
- client information
- body (optional)
- empty line

## Request Methods

- GET – Request transfer of the entity referred to by the URI
- POST – Ask the server to process the included body as “data” associated with the resource identified by the URI
- PUT – Request that the enclosed entity be stored under the supplied URI
- HEAD – Identical to GET except server must not return a body
- OPTIONS – Request information about the communication options available on the request/response chain identified by the URL
- DELETE – Request that the server delete the resource identified by the URI
- TRACE – used to invoke a remote, application-layer loop-back of the request message and the server should reflect the message received back to the client as the body of the response
- CONNECT – used with proxies
- … A webserver can define arbitrary extension methods!

Example:

GET / HTTP/1.1
User-Agent: curl/7.37.1
Host: www.google.com
Accept: */*

Modern request:

GET / HTTP/1.1
Host: www.google.com
Accept-Encoding: deflate, gzip
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36

## Responses

An HTTP response consists of:
- protocol version
- status code
- short reason
- headers
- body

### Responses – Status Codes

1XX – Informational: request received, continuing to process
2XX – Successful: request received, understood, and accepted
3XX – Redirection: user agent needs to take further action to fulfill the request
4XX – Client error: request cannot be fulfilled or error in request
5XX – Server error: the server is aware that it has erred or is incapable of performing the request

"200"   ; OK
"201"   ; Created
"202"   ; Accepted
"204"   ; No Content
“301"   ; Moved Permanently
"307"   ; Temporary Redirect
"400"   ; Bad Request
"401"   ; Unauthorized
"403"   ; Forbidden
"404"   ; Not Found
"500"   ; Internal Server Error
"501"   ; Not Implemented
"502"   ; Bad Gateway
"503"   ; Service Unavailable


Example:

HTTP/1.1 200 OK
Date: Tue, 13 Jan 2015 03:57:26 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Set-Cookie: …
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic,p=0.02
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

```html
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Go …
```


## Sessions

http is stateless, no memory of previous requests
but we need to make sessions
Three ways this can be achieved
- Embedding information in URLs
- Using hidden fields in forms
- Using cookies

### Cockies

Cookies are name-value pairs (seperated by "=")
The "Set-Cookie" header field is in the HTTP response
- Set-Cookie: USER=sofia;
The browser then sends the cookie back using the "Cookie" header
- Cookie: USER=sofia;

There can be multible cookies
- Set-Cookie: lang=en-us;
Other examples are Path, Domain, Expires/Max-Age, HttpOnly and Secure.
The client removes expired cookies so they can be removed by setting a past date.






