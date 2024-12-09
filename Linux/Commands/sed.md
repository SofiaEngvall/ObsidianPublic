
stream editor

find and replace

sudo sed s/mysql/MySQL/g /etc/snort/snort.conf > snort2.conf

s source
g globally

pipe stuff into:
`sed -e 's/\x1b\[[0-9;]*m//g'`

you can make an alias like:
`alias uncolor="sed -e 's/\x1b\[[0-9;]*m//g'"`
and then
cat hard_to_read_stuff | uncolor

