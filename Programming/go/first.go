package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func main() {
	k := 3
	var MaxInt uint64 = 1<<64 - 1
	fmt.Println("Hello world!", k)
	fmt.Println("The time is", time.Now())
	fmt.Println("My favorite number is", rand.Intn(10000))
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
	fmt.Printf("Pi is %e\n", math.Pi)
	fmt.Println("Pi is", math.Pi)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)

}
