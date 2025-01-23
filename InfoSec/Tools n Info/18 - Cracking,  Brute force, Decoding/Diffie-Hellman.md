
https://tryhackme.com/r/room/publickeycrypto, task 4

![[Images/5f04259cf9bf5b57aed2c476-1728439878360.svg]]

Consider p = 29, g = 5, a = 12. What is A?
A = g<sup>a</sup> mod p = 5<sup>12</sup> mod 29 = 7

Consider p = 29, g = 5, b = 17. What is B?
B = g<sup>b</sup> mod p = 5<sup>17</sup> mod 29 = 9

p = 29, a = 12, B=9 What is the key calculated by Bob? (key = B<sup>a</sup> mod p)
key = B<sup>a</sup> mod p = 9<sup>12</sup> mod 29 = 24

p = 29, b = 17, A=7 What is the key calculated by Alice? (key = A<sup>b</sup> mod p)
key = A<sup>b</sup> mod p = 7<sup>17</sup> mod 29 = 24

