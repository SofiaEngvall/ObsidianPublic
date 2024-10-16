
Testing but we don't have login info
```sh
┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ xfreerdp /dynamic-resolution /scale-desktop:300 /scale:100 +clipboard /cert:ignore /tls-seclevel:0 /v:10.10.32.52 /u:Administrator /p:'password' 
[23:18:30:877] [260267:260268] [ERROR][com.freerdp.core.transport] - transport_ssl_cb: ACCESS DENIED
[23:18:30:877] [260267:260268] [ERROR][com.freerdp.core] - transport_ssl_cb:freerdp_set_last_error_ex ERRCONNECT_AUTHENTICATION_FAILED [0x00020009]
[23:18:30:877] [260267:260268] [ERROR][com.freerdp.core.transport] - BIO_read returned an error: error:0A000419:SSL routines::tlsv1 alert access denied
```

```sh
┌──(kali㉿kali)-[~/thm/brainstorm/ftp]
└─$ xfreerdp /dynamic-resolution /scale-desktop:300 /scale:100 +clipboard /cert:ignore /tls-seclevel:0 /v:10.10.32.52
[23:17:37:033] [259828:259829] [INFO][com.freerdp.client.x11] - No user name set. - Using login name: kali
Domain:   brainstorm
Password: 
[23:17:56:352] [259828:259829] [ERROR][com.freerdp.core.transport] - transport_ssl_cb: ACCESS DENIED
[23:17:56:353] [259828:259829] [ERROR][com.freerdp.core] - transport_ssl_cb:freerdp_set_last_error_ex ERRCONNECT_AUTHENTICATION_FAILED [0x00020009]
[23:17:56:353] [259828:259829] [ERROR][com.freerdp.core.transport] - BIO_read returned an error: error:0A000419:SSL routines::tlsv1 alert access denied
```

