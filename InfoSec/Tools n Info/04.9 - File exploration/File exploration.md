
file filename

head filename

strings filename

show where there are 10 or more printable characters
strings -10 filename

also just show the 10 first hits
strings -10 filename | head

binwalk filename
recognizes headers n stuff
[[binwalk]]

data duplicator - can get parts out of a binary data file, like a rom image
`dd if =[filename] skip=[number to start at] bs=[blocksize, probably 1] of=[output filename]`
