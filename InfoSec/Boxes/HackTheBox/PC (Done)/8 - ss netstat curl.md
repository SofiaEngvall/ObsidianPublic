
check what ports are listening

```sh
-bash-5.0$ ss -tlpn
State                 Recv-Q                Send-Q                     Local Address:Port                            Peer Address:Port                Process 
LISTEN                0                     4096                       127.0.0.53%lo:53                                   0.0.0.0:* 
LISTEN                0                     128                              0.0.0.0:22                                   0.0.0.0:* 
LISTEN                0                     5                              127.0.0.1:8000                                 0.0.0.0:*
LISTEN                0                     128                              0.0.0.0:9666                                 0.0.0.0:*   
LISTEN                0                     128                                 [::]:22                                      [::]:*   
LISTEN                0                     4096                                   *:50051                                      *:* 
```

```sh
-bash-5.0$ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 localhost:8000          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:9666            0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
tcp6       0      0 [::]:50051              [::]:*                  LISTEN     
udp        0      0 localhost:domain        0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     SEQPACKET  LISTENING     23707    /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     900367   /run/user/1001/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     900372   /run/user/1001/bus
unix  2      [ ACC ]     STREAM     LISTENING     900373   /run/user/1001/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     900374   /run/user/1001/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     900375   /run/user/1001/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     23689    @/org/kernel/linux/storage/multipathd
unix  2      [ ACC ]     STREAM     LISTENING     900376   /run/user/1001/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     900377   /run/user/1001/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     900378   /run/user/1001/pk-debconf-socket
unix  2      [ ACC ]     STREAM     LISTENING     28871    /var/snap/lxd/common/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     900379   /run/user/1001/snapd-session-agent.socket
unix  2      [ ACC ]     STREAM     LISTENING     23676    /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     23678    /run/systemd/userdb/io.systemd.DynamicUser
unix  2      [ ACC ]     STREAM     LISTENING     23687    /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     23692    /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     23702    /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     24126    /run/systemd/journal/io.systemd.journal
unix  2      [ ACC ]     STREAM     LISTENING     28868    /run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     28001    /var/run/vmware/guestServicePipe
unix  2      [ ACC ]     STREAM     LISTENING     28874    /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     28876    /run/snapd-snap.socket
unix  2      [ ACC ]     STREAM     LISTENING     28878    /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     29622    /run/irqbalance//irqbalance840.sock
unix  2      [ ACC ]     STREAM     LISTENING     28870    @ISCSIADM_ABSTRACT_NAMESPACE

```



```sh
sau@pc:/tmp$ curl localhost:8000
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/login?next=http%3A%2F%2Flocalhost%3A8000%2F">/login?next=http%3A%2F%2Flocalhost%3A8000%2F</a>. If not, click the link.
```

answer on 8000!

```sh
-bash-5.0$ curl -d login localhost:8000
<!DOCTYPE html>
<html lang="en">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
...
              <p><b>Error 500: 405 Method Not Allowed: The method is not allowed for the requested URL.</b></p>
              <p><b>Traceback (most recent call last):</b></p>
              <p><b>  File &#34;/usr/local/lib/python3.8/dist-packages/flask/app.py&#34;, line 1820, in full_dispatch_request</b></p>
```




