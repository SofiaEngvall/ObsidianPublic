
https://tryhackme.com/r/room/publickeycrypto
https://tryhackme.com/r/room/breakrsa

https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/

Tools for RSA challenges in CTFs
https://github.com/RsaCtfTool/RsaCtfTool
https://github.com/ius/rsatool


### What is RSA?

ESA is an encryption algorithm that uses a private and public key. The private key is kept secret while the public key is sent to the one who is sending a message. When the message arrives the private key is used to decrypt the message. The public key cannot decrypt the message.

Example: A sends a message to B:
1. A encrypts the clear text message with the public key
2. The encrypted cyphertext message is sent in possibly unsafe ways to B
3. B decrypts the cyphertext using the private key

### The mathematical base

Based on that while it is easy to multiply two large prime numbers it's very hard to factorize their product.

Example: 982451653031 × 169743212279 = 166764499494295486767649 is easy but having 166764499494295486767649 and trying to find the prime numbers used to achieve is is very hard.


### How the private and public keys are generated

##### Creating the keys

1. Two prime numbers are selected: `p = 157` and `q = 199`
	- In modern encryption these numbers are usually 256 to 512 bytes long, giving decimal numbers over 600 digits long
2. The `modulus` is calculated: `n = p × q = 157 × 199 = 31243`
	- `n` is part of both the private and public keys
	- `number mod n` ensures the result is always between `0` and `n−1`
	- this means `n` limits the range of possible results during encryption and decryption, securing them
3. The `totient function` is calculated: `ϕ(n) = n − p − q + 1 = 31243 − 157 − 199 + 1 = 30888`
	- or: `ϕ(n) = (p−1) × (q−1) = (157−1) × (199−1) = 156 × 198 = 30888`
	- The `totient function` counts the number of integers less than `n` that are relatively prime to `n`
	- This number is used in when creating the private and public keys
5. A `public exponent` is selected: `e = 163`
	- `e` has to be relatively prime to `ϕ(n)`, meaning their biggest common divisor is 1 - factorize both numbers to make sure
	- Low prime numbers are often used as this makes the check for the above easy, but `n` doesn't have to be a prime number
	- This number will be a part of the public key
6. The `private exponent` is calculated: 
	- `d` is the modular multiplicative inverse of e modulo ϕ(n):
	- e×d≡1(modϕ(n))e×d≡1(modϕ(n)).
	- In this case, d=379d=379, because:
	- e×d=163×379=61777e×d=163×379=61777, and 61777mod  30888=161777mod30888=1.
	- d = 379, where _e_ × _d_ = 1 mod _ϕ_(_n_), i.e., _e_ × _d_ = 163 × 379 = 61777 and 61777 mod 30888 = 1.
7. The `public key` is put together: (n, e) = (31243, 163)
	- This key is shared with everyone
8. The `private key` is put together: $(n,d), i.e., (31243,379)
	- This key is kept secret

##### Encrypting a messages

Let’s say that the value they want to encrypt is _x_ = 13, then Alice would calculate and send _y_ = _x__e_ mod _n_ = 13163 mod 31243 = 16341.

Alice wants to send a message x=13x = 13x=13 securely to Bob.
7. **Calculate the ciphertext yyy:**  
    y=xemod  n=13163mod  31243y = x^e \mod n = 13^{163} \mod 31243y=xemodn=13163mod31243.  
    Performing the modular exponentiation gives y=16341y = 16341y=16341.  
    Alice sends y=16341y = 16341y=16341 to Bob.
##### Decrypting a messages

Bob will decrypt the received value by calculating _x_ = _y__d_ mod _n_ = 16341379 mod 31243 = 13. This way, Bob recovers the value that Alice sent.

Bob receives y=16341y = 16341y=16341 and wants to recover xxx.
8. **Calculate the original message xxx:**  
    x=ydmod  n=16341379mod  31243x = y^d \mod n = 16341^{379} \mod 31243x=ydmodn=16341379mod31243.  
    Performing the modular exponentiation gives x=13x = 13x=13.  
    Bob successfully decrypts the message and recovers x=13x = 13x=13, the original value Alice sent.


