
```st
'Enter the password: ' display.
s := ([ stdin nextLine ] on: Error do: ['']) asByteArray.
chars := 'abcdefghijklmnopqrstuvwxyz0123456789'.
ok := (s size) == 16 and: [
    (s allSatisfy: [ :c | chars includes: (c asCharacter)])
        & (((s at: 6)  -       (s at: 4))  <  -4)
        & (((s at: 12) -       (s at: 1))  == -5)
        & (((s at: 5)  bitXor: (s at: 13)) == 2)
        & (((s at: 14) bitXor: (s at: 2))  == 19)
        & (((s at: 11) bitOr:  (s at: 2))  == 126)
        & (((s at: 8)  bitOr:  (s at: 5))  == 108)
        & (((s at: 16) bitXor: (s at: 7))  == 16)
        & (((s at: 9)  bitXor: (s at: 10)) == 9)
        & (((s at: 3)  +       (s at: 12)) == 226)
        & (((s at: 15) -       (s at: 4))  == -5)
        & (((s at: 9)  bitOr:  (s at: 8))  == 125)
        & (((s at: 4)  +       (s at: 12)) <  226)
        & (((s at: 6)  bitXor: (s at: 10)) == 8)
        & (((s at: 12) bitOr:  (s at: 11)) == 111)
        & (((s at: 2)  bitXor: (s at: 4))  == 2)
        & (((s at: 13) bitXor: (s at: 3))  == 25)
        & (((s at: 10) bitXor: (s at: 16)) == 26)
].
'' displayNl.
ans := ok
    ifTrue:  [ ans := (FileStream open: 'flag.txt') nextLine ]
    ifFalse: ['Incorrect!'].
ans displayNl.
```