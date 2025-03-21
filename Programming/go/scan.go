package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
)

const VERBOSE = true

func scanPort(host string, port int) bool {
	address := fmt.Sprintf("%s:%d", host, port)
	conn, err := net.Dial("tcp", address)
	if err != nil {
		if VERBOSE {
			fmt.Printf("Error: %s\n", err.Error())
		}
		return false
	}
	conn.Close()
	return true
}

func main() {
	host := "192.168.0.1"
	start_port := 0
	stop_port := 100
	ports := 0

	arguments := len(os.Args) - 1

	if arguments == 0 {
		fmt.Println("Use: scan [ip] [start_port] [stop_port]")
	}
	if arguments >= 1 {
		host = os.Args[1]
	}
	fmt.Println("host =", host)

	if arguments >= 2 {
		temp_int, err := strconv.Atoi(os.Args[2])
		if err == nil {
			start_port = temp_int
			stop_port = start_port + stop_port
			if start_port >= 65535 {
				start_port = 65535
			}
		} else {
			fmt.Println("Could not parse start_port argument.")
			os.Exit(1)
		}
	}
	fmt.Println("start port =", start_port)

	if arguments >= 3 {
		temp_int, err := strconv.Atoi(os.Args[3])
		if err == nil {
			stop_port = temp_int
		} else {
			fmt.Println("Could not parse stop_port argument.")
			os.Exit(1)
		}
	}
	fmt.Println("start port =", stop_port)

	fmt.Println("Starting port scan:")
	for port := start_port; port <= stop_port; port++ {
		if scanPort(host, port) {
			fmt.Printf("Port %d is open\n", port)
			ports++
		}
	}

	switch ports {
	case 0:
		fmt.Printf("Scan completed - No open ports were found.")
	case 1:
		fmt.Printf("Scan completed - Found 1 open port.")
	default:
		fmt.Printf("Scan completed - Found %d open ports.", ports)
	}
}
