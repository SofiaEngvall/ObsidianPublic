
space in file name
`"with space"`
`'with space'`
`with\ space`


"string" will resolve variables
'string' will not

`echo $((1+2))`
`myvar=$((1+2))`

`argidx=$((argidx+1))`

`${IFS%??}` = space as in `which${IFS%??}bash`
`{;IFS=];whatever]command]requireing]spaces;}` ? do I remember right


### Command substitution
Backticks (`` ` ``) command substitution, allowing the output of a command to replace the command itself
`$(...)` is the preferred, newer alternative, especially in scripts or when nested
``current_date=`date` ``
`echo $current_dates`

