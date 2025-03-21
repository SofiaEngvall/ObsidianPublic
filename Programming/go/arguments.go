package main

import (
	"flag"
	"fmt"
	"os"
)

var (
	intFlag  int
	strFlag  string
	boolFlag bool
)

func main() {

	flag.IntVar(&intFlag, "int", 1234, "help message")
	flag.StringVar(&strFlag, "str", "default", "help message")
	flag.BoolVar(&boolFlag, "bool", false, "help message")
	flag.Parse()

	fmt.Println("All arguments:", os.Args)
	fmt.Println("Non-flag arguments:", flag.Args())
	fmt.Println("-----")
	fmt.Println("intFlag value is: ", intFlag)
	fmt.Println("strFlag value is: ", strFlag)
	fmt.Println("boolFlag value is: ", boolFlag)
}

// --help and -h are supported by default
