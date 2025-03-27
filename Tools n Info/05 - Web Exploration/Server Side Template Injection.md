
Template injection allows an attacker to include template code into an existing (or not) template. A template engine makes designing HTML pages easier by using static template files which at runtime replaces variables/placeholders with actual values in the HTML pages
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md

Server-side template injection is a vulnerability that occurs when an attacker can inject malicious code into a template that is executed on the server. This vulnerability can be found in various technologies, including Jinja.
https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection

Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.
Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. This allows attackers to inject arbitrary template directives in order to manipulate the template engine, often enabling them to take complete control of the server. As the name suggests, server-side template injection payloads are delivered and evaluated server-side, potentially making them much more dangerous than a typical client-side template injection.
https://portswigger.net/web-security/server-side-template-injection

SSTImap is a penetration testing software that can check websites for Code Injection and Server-Side Template Injection vulnerabilities and exploit them, giving access to the operating system itself.
This tool was developed to be used as an interactive penetration testing tool for SSTI detection and exploitation, which allows more advanced exploitation.
https://github.com/vladko312/SSTImap

