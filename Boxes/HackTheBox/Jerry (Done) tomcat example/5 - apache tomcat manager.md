
http://10.10.10.95:8080/manager/html

googled for default creds:

admin : admin
ADMIN : ADMIN
admin : j5Brn9
admin : None
admin : tomcat
cxsdk : kdsxc
j2deployer : j2deployer
ovwebusr : OvW*busr1
QCC : QLogic66
role : changethis
role1 : role1
role1 : tomcat
root : root
tomcat : changethis
tomcat : s3cret
tomcat : tomcat
xampp : xampp

tomcat:s3cret worked to log in

![[Images/Pasted image 20250513201011.png]]

![[Images/Pasted image 20250513202248.png|1200]]

We can upload Web Application Resource (WAR) files

https://github.com/SecurityRiskAdvisors/cmd.jsp/blob/master/cmd.war
A webshell to upload

We now have cmd in out list of applications:
![[Images/Pasted image 20250513220404.png]]

To access the web shell we need to send post requests

We went to http://jerry.htb/cmd/cmd.jsp and then sent the request to repeater
![[Images/Pasted image 20250513220509.png]]

this one doesn't work with get though, so we uploaded a new one:
![[Images/Pasted image 20250513223956.png]]

