
```go
var c, python, java bool
var i int
```

```go
var i, j int = 1, 2
var c, python, java = true, false, "no!"
```
if a value is given, it's allowed to omit the type - it'll guess the type from the value

uninitialized variables are given the types zero value, false for bool, "" for string..

```go
k := 3
```
can be used instead of var declaration
can ONLY be used within functions

```go
var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)
```
block variable declaration

### Conversion

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
```

### Constants

```go
const Pi = 3.14

func main() {
	const World = "世界"
}
```
constants use const instead of var


### Arrays

```go
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)
	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

	len(a)
	cap(a) #capasity
```

```
Hello World
[Hello World]
[2 3 5 7 11 13]
```

```go
	primes := [6]int{2, 3, 5, 7, 11, 13}
	var s []int = primes[1:4]
	fmt.Println(s)
```

```
[3 5 7]
```

### Types

bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128

`int`, `uint`, and `uintptr` will be sized after your system 32/64 bit


### Pointers

```go
var p *int
i := 42
p = &i

fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p
```


### Structs

```go
type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}
```

To access the field `X` of a struct when we have the struct pointer `p` we could write `(*p).X`. However, that notation is cumbersome, so the language permits us instead to write just `p.X`

```go
func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```

```
{1000000000 2}
```

