
10.129.231.244

22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://cypher.htb/

/login                (Status: 200) [Size: 3671]
/api                  (Status: 307) [Size: 0] [--> /api/docs]
/about                (Status: 200) [Size: 4986]
/demo                 (Status: 307) [Size: 0] [--> /login]
/index                (Status: 200) [Size: 4562]
/testing              (Status: 301) [Size: 178] [--> http://cypher.htb/testing/]

no vhosts found



