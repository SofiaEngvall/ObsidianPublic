
A defer statement defers the execution of a function until the surrounding function returns.
The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

```go
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```

```go
package main

import "fmt"

func main() {
    var i int = 1
	defer fmt.Println("i is",i)
	i += 1
	fmt.Println("now, i is",i)
}
```

### Stacking 

Deferred function calls are pushed to a stack. When a function returns, its deferred calls are executed in last-in-first-out order.

```go
func main() {
	fmt.Println("counting")
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("done")
}
```

