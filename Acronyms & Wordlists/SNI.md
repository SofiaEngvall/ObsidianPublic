
From https://knowledge.digicert.com/quovadis/ssl-certificates/ssl-general-topics/what-is-sni-server-name-indication

Server Name Indication (SNI) is an extension to the TLS protocol.  It allows a client or browser to indicate which hostname it is trying to connect to at the start of the TLS handshake. This allows the server to present multiple certificates on the same IP address and port number.

Before, for every SSL website you hosted, you needed a separate IP address on your server as port 443 (https) could not be shared.  If you attempted this on certain servers (such as IIS for example), one or both of your websites would not function.

With SNI enabled, you can cut down on the number of IP addresses, both internal and external, that are used to serve encrypted pages using https.