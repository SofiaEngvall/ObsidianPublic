
The {} are required

for
```go
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
```

while is also for ;)
```go
	sum := 1
	for sum < 1000 {
		sum += sum
	}
```

infinite loop
```go
	for {
		fmt.Println("here we GO...")
	}
```

for each loop
```go
	stuff := []string{
		"something",
		"something else",
		"whatever",
	}

	for url := range stuff {
		fmt.Printf("Look: %s\n",url)
	}
```
or
```go
	for index, url := range stuff {
		fmt.Printf("Look: %s\n",url)
	}
```

if
```go
	if x < 0 {
		 fmt.Println("x is less than zero")
	} else {
		//whatever
	}
```

can contain start statement like a for - declarations here are scoped within the if
```go
	if v := math.Pow(x, n); v < lim {
		return v
	}
```

switch
- go only runs one so no break statements are required
- when a match is found the rest are not checked = only one is run!
```go
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
```

A switch with no condition will work like an if else chain
```go
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
```


