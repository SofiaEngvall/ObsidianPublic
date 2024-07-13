
10.10.11.102

22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
3306/tcp open  mysql   MariaDB (unauthorized)

joomla 3.7.0

exploit 2017-8917



from john
user: jonah
pass: spiderman123



login found in /var/www/html/configuration.php:  public $password = 'nv5uz9r3ZEDzVjNu'; 
works with
user: jjameson
pass: nv5uz9r3ZEDzVjNu