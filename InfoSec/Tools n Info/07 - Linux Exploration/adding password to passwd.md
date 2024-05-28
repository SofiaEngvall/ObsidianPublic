
`openssl passwd newpasswordhere`

Edit the /etc/passwd file and copy the root user's row and append it to the bottom of the file, changing the first instance of the word "root" to "newroot" and placing the generated password hash between the first and second colon (replacing the "x").

`openssl passwd -1 -salt salt password`

`perl -e 'print crypt("password","\$1\$salt\$")."\n";'` is the same as just doing openssl passwd -1 -salt salt password

