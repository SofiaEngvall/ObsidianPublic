
```sh
──(kali㉿kali)-[~/.ssh]
└─$ ssh-keygen          
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kali/.ssh/id_rsa
Your public key has been saved in /home/kali/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:6fhyZaEaCGTnNxYKlyOmZgI8uUQ8plXzvLXnZDDGZ8M kali@kali
The key´s randomart image is:
+---[RSA 3072]----+
|+...o.           |
|.OB =+.. .       |
|=*+* oo.* E      |
|++. o ++ B..     |
|+  . +..S.+.     |
|    . .o.=o      |
|      .o.o.      |
|      o..        |
|       o.        |
+----[SHA256]-----+
```

- **DSA (Digital Signature Algorithm)** is a public-key cryptography algorithm specifically designed for digital signatures.
- **ECDSA (Elliptic Curve Digital Signature Algorithm)** is a variant of DSA that uses elliptic curve cryptography to provide smaller key sizes for equivalent security.
- **ECDSA-SK (ECDSA with Security Key)** is an extension of ECDSA. It incorporates hardware-based security keys for enhanced private key protection.
- **Ed25519** is a public-key signature system using EdDSA (Edwards-curve Digital Signature Algorithm) with Curve25519.
- **Ed25519-SK (Ed25519 with Security Key)** is a variant of Ed25519. Similar to ECDSA-SK, it uses a hardware-based security key for improved private key protection.

