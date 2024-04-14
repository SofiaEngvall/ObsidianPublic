
`binwalk filename`

can find headers in a file

for example in a rom update image:
boot loaders
kernel images
compressed data

![[Pasted image 20240215135632.png|800]]
https://youtu.be/GIU4yJn2-2A?si=Vw2bqia0nlqhjdW9


entropy = randomness of the file where 1 = totally random
`binwalk -E`
both compression and encryption makes a file be close to 1 in entropy

unzip internal compressed data
`binwalk -e`
this requires the right software installed for different formats

`-M -e` recursive uncompress

pretty print more info
`binwalk -t`

