
```sh
ssh -N -L /tmp/.s.PGSQL.5432:/var/run/postgresql/.s.PGSQL.5432 service@10.129.234.160
```

this can be done when we have a socket file

### How to find socket files

##### Databases

- **PostgreSQL** → `/var/run/postgresql/.s.PGSQL.5432`  
    _Pattern:_ `.s.PGSQL.<port>`
    
- **MySQL / MariaDB** → `/var/run/mysqld/mysqld.sock`  
    _Pattern:_ `*.sock` (sometimes `/tmp/mysql.sock`)
    
- **Redis** → `/var/run/redis/redis-server.sock`  
    _Pattern:_ `<service>.sock`
    

---

##### Web / Proxy servers

- **Nginx** → `/var/run/nginx.sock` or `/run/nginx/proxy.sock`  
    _Used for backend proxying to PHP-FPM or similar._
    
- **Apache (httpd + mod_proxy_fcgi)** → `/var/run/httpd/php-fpm.sock`
    
- **PHP-FPM** → `/var/run/php/php-fpm.sock`  
    _Pattern:_ `<app>-fpm.sock`
    

---

##### System & Daemons

- **systemd journal** → `/run/systemd/journal/socket`  
    _Used by logging services to send messages._
    
- **D-Bus** → `/run/dbus/system_bus_socket`  
    _IPC between desktop/system services._
    
- **cups (printing)** → `/run/cups/cups.sock`
    
- **udev (device manager)** → `/run/udev/control`
    

---

##### Security / Privilege-related

- **PolicyKit** → `/run/polkit-1/polkitd/polkitd.sock`
    
- **Sudo or SSH agent** → `/run/user/<uid>/ssh-agent.<pid>`  
    _Pattern:_ `ssh-*/agent.*` or `ssh-agent.<pid>`
    
- **Docker daemon** → `/var/run/docker.sock`  
    _(Very common; access to it = root access to host)_
    

---

##### General patterns

- Sockets often live in `/run/`, `/var/run/`, or `/tmp/`.
    
- Names end in `.sock` or start with `.s.`.
    
- They’re always associated with a **daemon or background service**, not a user file.


