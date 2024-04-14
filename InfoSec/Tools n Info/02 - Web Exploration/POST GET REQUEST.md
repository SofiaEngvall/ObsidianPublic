
What's the difference between `$_POST`, `$_GET`, and `$_REQUEST` in PHP?  (Generally for http GET and POST.)


`$_GET` and GET:
- Are intended for getting data = viewing, not changing
- It is assumed by browsers that repeating the request is ok without a warning
- Data is part of the URL = Visible in the URL string
- URL can be cached and logged by browsers, proxies and servers = Should not be used for sensitive data
- Can be  bookmarked, shared...
- Has a length limit (2083 characters is common in older browsers, now often more)
- Only ASCII characters allowed
- Limited to name and value pairs
- If a GET is used for sending data is might not be done since the page might have been cached

`$_POST` and POST:
- Are intended to update things on the server side = changing, not viewing
- You usually get a question by a browser if you want to resend data when reloading
- Retrieves variables from a POST method, usually forms
- Almost unlimited length
- Requires a content-length header
- Can handle more complex data structures like json and xml
- You can attach files through multipart mime encoding

`$_REQUEST`:
- Merges `$_GET` and `$_POST`
- At conflicts `$_POST` overrides `$_GET` as default

https://www.w3.org/2001/tag/doc/whenToUseGet.html

1) Both `$_GET` and `$_POST` create an array e.g. `array( key => value, key2 => value2, key3 => value3, ...)`. This array holds key/value pairs, where keys are the names of the form controls and values are the input data from the user.
 
2) Both `GET` and `POST` are treated as `$_GET` and `$_POST`. These are superglobals, which means that they are always accessible, regardless of scope - and you can access them from any function, class or file without having to do anything special.
 
3) `$_GET` is an array of variables passed to the current script via the URL parameters.
 
4) `$_POST` is an array of variables passed to the current script via the HTTP POST method.
 
---- whereas `$_REQUEST` contains `$_POST`, `$_GET` and `$_COOKIE` .



**$_POST** is an associative array of variables passed to the current script via the HTTP POST method when using application/x-www-form-urlencoded or multipart/form-data as the HTTP Content-Type in the request. You can use when you are sending large data to server or if you have sensitive information like passwords, credit card details etc

**$_GET** is an associative array of variables passed to the current script via the URL parameters. you can use when there is small amount of data, it is mostly used in pagination, page number is shown in the url and you can easily get the page number from URL using $_GET

**$_REQUEST** is a 'superglobal' or automatic global, variable. This simply means that it is available in all scopes throughout a script. It is an associative array that by default contains the contents of $_GET, $_POST and $_REQUEST (depending on [`request_order=`](http://php.net/manual/en/ini.core.php#ini.request-order))

`$_COOKIE`

they are all "superglobals". Full list: `$GLOBALS, $_SERVER, $_GET, $_POST, $_FILES, $_COOKIE, $_SESSION, $_REQUEST, $_ENV` as documented here: [php.net/manual/en/language.variables.superglobals.php](https://www.php.net/manual/en/language.variables.superglobals.php)

There are 2 methods to send HTML form data from 1 Page to another or HTML page to server side (In PHP).

1. `POST`

It is a method in which data gets sent using packet which is not visible to any user on web-browser. it is secured compared to GET method.

2. `GET`

It is a method in which data gets sent with URL which is visible to user in address-bar of any web-browser. So, it’s not secure as POST method.

Now, There are total three super global variables to catch this data in PHP.

1. `$_POST`: It can catch the data which is sent using POST method.
2. `$_GET`: It can catch the data which is sent using GET method.
3. `$_REQUEST`: It can catch the data which is sent using both POST & GET methods.

Also with `$_GET` superglobal variable can collect data sent in the URL from submit button.