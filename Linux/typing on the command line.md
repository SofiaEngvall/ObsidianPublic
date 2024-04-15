
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
