
#### Variables

Setting a variable
`QWE="test"`

Make available to child processes
`export QWE`

Recalling the value
`echo $QWE`

Clearing
`unset QWE`

#### Functions

Create a function useable in bash
`function /usr/sbin/service { /bin/bash -p; }`

Export the function so it can be used from applications too (= "available to child processes")
`export -f /usr/sbin/service`

Remove all traces of the function
`unset -f /usr/sbin/service`
