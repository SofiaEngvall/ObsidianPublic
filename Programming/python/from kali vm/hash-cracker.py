#!/usr/bin/env python3

import hashlib

print("test")

#wordlist_location = "/usr/share/wordlists/rockyou.txt"
wordlist_location = "./wordlist.txt"

hash_input = str(input('Enter hash to be cracked: '))

#print(hashlib.algorithms_available)

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        #hash_ob = hashlib.md5(line.strip().encode())
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)
