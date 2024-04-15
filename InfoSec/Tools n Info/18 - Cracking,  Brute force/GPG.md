
### Help

```sh
┌──(kali㉿kali)-[~/thm/hashes]
└─$ gpg --help                                                                                                              
gpg (GnuPG) 2.2.40
libgcrypt 1.10.3
Copyright (C) 2022 g10 Code GmbH
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/kali/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2

Syntax: gpg [options] [files]
Sign, check, encrypt or decrypt
Default operation depends on the input data

Commands:
 
 -s, --sign                         make a signature
     --clear-sign                   make a clear text signature
 -b, --detach-sign                  make a detached signature
 -e, --encrypt                      encrypt data
 -c, --symmetric                    encryption only with symmetric cipher
 -d, --decrypt                      decrypt data (default)
     --verify                       verify a signature
 -k, --list-keys                    list keys
     --list-signatures              list keys and signatures
     --check-signatures             list and check key signatures
     --fingerprint                  list keys and fingerprints
 -K, --list-secret-keys             list secret keys
     --generate-key                 generate a new key pair
     --quick-generate-key           quickly generate a new key pair
     --quick-add-uid                quickly add a new user-id
     --quick-revoke-uid             quickly revoke a user-id
     --quick-set-expire             quickly set a new expiration date
     --full-generate-key            full featured key pair generation
     --generate-revocation          generate a revocation certificate
     --delete-keys                  remove keys from the public keyring
     --delete-secret-keys           remove keys from the secret keyring
     --quick-sign-key               quickly sign a key
     --quick-lsign-key              quickly sign a key locally
     --quick-revoke-sig             quickly revoke a key signature
     --sign-key                     sign a key
     --lsign-key                    sign a key locally
     --edit-key                     sign or edit a key
     --change-passphrase            change a passphrase
     --export                       export keys
     --send-keys                    export keys to a keyserver
     --receive-keys                 import keys from a keyserver
     --search-keys                  search for keys on a keyserver
     --refresh-keys                 update all keys from a keyserver
     --import                       import/merge keys
     --card-status                  print the card status
     --edit-card                    change data on a card
     --change-pin                   change a card´s PIN
     --update-trustdb               update the trust database
     --print-md                     print message digests
     --server                       run in server mode
     --tofu-policy VALUE            set the TOFU policy for a key

Options controlling the diagnostic output:
 -v, --verbose                      verbose
 -q, --quiet                        be somewhat more quiet
     --options FILE                 read options from FILE
     --log-file FILE                write server mode logs to FILE

Options controlling the configuration:
     --default-key NAME             use NAME as default secret key
     --encrypt-to NAME              encrypt to user ID NAME as well
     --group SPEC                   set up email aliases
     --openpgp                      use strict OpenPGP behavior
 -n, --dry-run                      do not make any changes
 -i, --interactive                  prompt before overwriting

Options controlling the output:
 -a, --armor                        create ascii armored output
 -o, --output FILE                  write output to FILE
     --textmode                     use canonical text mode
 -z N                               set compress level to N (0 disables)

Options controlling key import and export:
     --auto-key-locate MECHANISMS   use MECHANISMS to locate keys by mail address
     --auto-key-import              import missing key from a signature
     --include-key-block            include the public key in signatures
     --disable-dirmngr              disable all access to the dirmngr

Options to specify keys:
 -r, --recipient USER-ID            encrypt for USER-ID
 -u, --local-user USER-ID           use USER-ID to sign or decrypt

(See the man page for a complete listing of all commands and options)

Examples:

 -se -r Bob [file]          sign and encrypt for user Bob
 --clear-sign [file]        make a clear text signature
 --detach-sign [file]       make a detached signature
 --list-keys [names]        show keys
 --fingerprint [names]      show fingerprints

Please report bugs to <https://bugs.gnupg.org>.
```


### Info

GPG is an Open Source implementation of PGP

https://www.gnupg.org/gph/de/manual/r1023.html

