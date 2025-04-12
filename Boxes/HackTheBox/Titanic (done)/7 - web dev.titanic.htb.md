
gitea 1.22.1 site
found no vulns in this version
also http://dev.titanic.htb/api/swagger

Also found:
![[Images/Pasted image 20250319144819.png]]

http://dev.titanic.htb/administrator
![[Images/Pasted image 20250327145913.png]]

seems like a username, also developer

![[Images/Pasted image 20250327150343.png]]

![[Images/Pasted image 20250327150417.png]]
people have made users I assume :)

so much data, sigh
![[Images/Pasted image 20250327150628.png]]

![[Images/Pasted image 20250327150653.png]]


docker-config/gitea/docker-compose.yml
```yaml
version: '3'

services:
  gitea:
    image: gitea/gitea
    container_name: gitea
    ports:
      - "127.0.0.1:3000:3000"
      - "127.0.0.1:2222:22"  # Optional for SSH access
    volumes:
      - /home/developer/gitea/data:/data # Replace with your path
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
```

port 3000, not open

lfi scan data!



docker-config/mysql/docker-compose.yml
```yaml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    ports:
      - "127.0.0.1:3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 'MySQLP@$$w0rd!'
      MYSQL_DATABASE: tickets 
      MYSQL_USER: sql_svc
      MYSQL_PASSWORD: sql_password
    restart: always
```

oh, we got a password! reuse?

![[Images/Pasted image 20250327152948.png]]

```json
{"name": "Rose DeWitt Bukater", "email": "rose.bukater@titanic.htb", "phone": "643-999-021", "date": "2024-08-22", "cabin": "Suite"}
```

```json
{"name": "Jack Dawson", "email": "jack.dawson@titanic.htb", "phone": "555-123-4567", "date": "2024-08-23", "cabin": "Standard"}
```
