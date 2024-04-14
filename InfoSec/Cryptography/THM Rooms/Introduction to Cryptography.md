![[2140d4d554b437c7fb2e7816c259b4fc.png|100]]
# Introduction to Cryptography
Learn about encryption algorithms such as AES, Diffie-Hellman key exchange, hashing, PKI, and TLS.

# Introduction

The purpose of this room is to introduce users to basic cryptography concepts such as:

- Symmetric encryption, such as AES
- Asymmetric encryption, such as RSA
- Diffie-Hellman Key Exchange
- Hashing
- PKI

Suppose you want to send a message that no one can understand except the intended recipient. How would you do that?

![[a31ad9ee6b4e321453508e8662fc4679.png|300]]  

One of the simplest ciphers is the Caesar cipher, used more than 2000 years ago. Caesar Cipher shifts the letter by a fixed number of places to the left or to the right. Consider the case of shifting by 3 to the right to encrypt, as shown in the figure below.

![[b4f1cbf444e5f19f855dadb7f272ab50.png|500]]

The recipient needs to know that the text was shifted by 3 to the right to recover the original message.

![[45b482f79ebcc2f202813a5d7de4df87.png|500]]

Using the same key to encrypt “TRY HACK ME”, we get “WUB KDFN PH”.

The Caesar Cipher that we have described above can use a key between 1 and 25. With a key of 1, each letter is shifted by one position, where A becomes B, and Z becomes A. With a key of 25, each letter is shifted by 25 positions, where A becomes Z, and B becomes A. A key of 0 means no change; moreover, a key of 26 will also lead to no change as it would lead to a full rotation. Consequently, we conclude that Caesar Cipher has a keyspace of 25; there are 25 different keys that the user can choose from.

Consider the case where you have intercepted a message encrypted using Caesar Cipher: “YMNX NX FQUMF GWFAT HTSYFHYNSL YFSLT MTYJQ RNPJ”. We are asked to decrypt it without knowledge of the key. We can attempt this by using brute force, i.e., we can try all the possible keys and see which one makes the most sense. In the following figure, we noticed that key being 5 makes the most sense, “THIS IS ALPHA BRAVO CONTACTING TANGO HOTEL MIKE.”

![[83c79636b07babb43ffe5402e2697772.png|800]]
Caesar cipher is considered a **substitution cipher** because each letter in the alphabet is substituted with another.

Another type of cipher is called **transposition cipher**, which encrypts the message by changing the order of the letters. Let’s consider a simple transposition cipher in the figure below. We start with the message, “THIS IS ALPHA BRAVO CONTACTING TANGO HOTEL MIKE”, and the key `42351`. After we write the letters of our message by filling one column after the other, we rearrange the columns based on the key and then read the rows. In other words, we write by columns and we read by rows. Also notice that we ignored all the space in the plaintext in this example.  The resulting ciphertext “NPCOTGHOTH…” is read one row after the other. In other words, a transposition cipher simply rearranges the order of the letters, unlike the substitution cipher, which substitutes the letters without changing their order.

![[Public/InfoSec/Cryptography/THM Rooms/Images/d1c99f9bf3e305eb4b50cb8c30be430d.png|600]]

This task introduced simple substitution and transposition ciphers and applied them to messages made of alphabetic characters. For an encryption algorithm to be considered **secure**, it should be infeasible to recover the original message, i.e., plaintext. (In mathematical terms, we need a **hard** problem, i.e., a problem that cannot be solved in polynomial time. A problem that we can solve in polynomial time is a problem that’s feasible to solve even for large input, although it might take the computer quite some time to finish.)

If the encrypted message can be broken in one week, the encryption used would be considered insecure. However, if the encrypted message can be broken in 1 million years, the encryption would be considered practically secure.

Consider the mono-alphabetic substitution cipher, where each letter is mapped to a new letter. For example, in English, you would map “a” to one of the 26 English letters, then you would map “b” to one of the remaining 25 English letters, and then map “c” to one of the remaining 24 English letters, and so on.

For example, we might choose the letters in the alphabet “abcdefghijklmnopqrstuvwxyz” to be mapped to “xpatvrzyjhecsdikbfwunqgmol” respectively. In other words, “a” becomes “x”, “b” becomes “p”, and so on. The recipient needs to know the key, “xpatvrzyjhecsdikbfwunqgmol”, to decrypt the encrypted messages successfully.

This algorithm might look very secure, especially since trying all the possible keys is not feasible. However, different techniques can be used to break a ciphertext using such an encryption algorithm. One weakness of such an algorithm is letter frequency. In English texts, the most common letters are ‘e’, ‘t’, and ‘a’, as they appear at a frequency of 13%, 9.1%, and 8.2%, respectively. Moreover, in English texts, the most common first letters are ‘t’, ‘a’, and ‘o’, as they appear at 16%, 11.7% and 7.6%, respectively. Add to this the fact that most of the message words are dictionary words, and you will be able to break an encrypted text with the alphabetic substitution cipher in no time.

We don’t really need to use the encryption key to decrypt the received ciphertext, “Uyv sxd gyi siqvw x sinduxjd pvzjdw po axffojdz xgxo wsxcc wuidvw.” As shown in the figure below, using a website such as [quipqiup](https://www.quipqiup.com/), it will take a moment to discover that the original text was “The man who moves a mountain begins by carrying away small stones.” This example clearly indicates that this algorithm is broken and should not be used for confidential communication.

![[0b4ac26e6f49c1156b6dc5c283b413a7.png|800]]

### Answer the questions below

You have received the following encrypted message:

_“Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy.” Zlwvzjxj Zpcvcol_

You can guess that it is a quote. Who said it?
>Miyamoto Musashi

