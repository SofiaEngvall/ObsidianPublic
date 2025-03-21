package main

import "fmt"

func main() {
	var i int = 1
	defer fmt.Println("i is", i)
	i += 1
	fmt.Println("now, i is", i)
}
