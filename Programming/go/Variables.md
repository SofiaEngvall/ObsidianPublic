
```go
var c, python, java bool
var i int
```

```go
var i, j int = 1, 2
var c, python, java = true, false, "no!"
```
if a value is given, it's allowed to omit the type - it'll get the type of the value

uninitialized variables are given the types zero value, false for bool, "" for string..

```go
k := 3
```
used instead of var declaration
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
