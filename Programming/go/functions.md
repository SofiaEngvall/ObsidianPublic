
### Basic function

```go
func add(x int, y int) int {
	return x + y
}
```

```go
func swap(x, y string) (string, string) {
	return y, x
}
```

multiple named return values
```go
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```



### Imports

```go
import "time"
time.Now()
```

```go
import "math/rand"
rand.Intn(10)
```

```go
import "math"
math.Sqrt(7)
```

```go
package main

import (
	"fmt"
	"time"
	"math"
)

func main() {
	fmt.Println("Hello, 世界")
	fmt.Println("The time is", time.Now())
	fmt.Println("My favorite number is", math.rand.Intn(10))
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
	fmt.Println("",math.Pi)
}
```



