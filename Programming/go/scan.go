package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
)

type scanned_port struct {
	port    int
	isOpen  bool
	problem error
}

const VERBOSE = false

func parse_arguments(arguments []string) (string, int, int) {
	//Default values
	host := "192.168.0.1"
	start_port := 0
	stop_port := 100

	args_count := len(arguments) - 1

	if args_count == 0 {
		fmt.Println("Use: scan [ip] [start_port] [stop_port]")
	}
	if args_count >= 1 {
		host = arguments[1]
	}
	if VERBOSE {
		fmt.Println("host =", host)
	}

	if args_count >= 2 {
		temp_int, err := strconv.Atoi(arguments[2])
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
	if VERBOSE {
		fmt.Println("start port =", start_port)
	}

	if args_count >= 3 {
		temp_int, err := strconv.Atoi(arguments[3])
		if err == nil {
			stop_port = temp_int
		} else {
			fmt.Println("Could not parse stop_port argument.")
			os.Exit(1)
		}
	}
	if VERBOSE {
		fmt.Println("start port =", stop_port)
	}

	return host, start_port, stop_port
}

func scanPort(host string, port int, message_channel chan scanned_port) {
	conn, err := net.Dial("tcp", fmt.Sprintf("%s:%d", host, port))
	if err == nil {
		conn.Close()
	}
	message_channel <- scanned_port{port, (err == nil), err}
}

func print_result(ports int) {
	switch ports {
	case 0:
		fmt.Println("Scan completed - No open ports were found.")
	case 1:
		fmt.Println("Scan completed - Found 1 open port.")
	default:
		fmt.Printf("Scan completed - Found %d open ports.\n", ports)
	}
}

func main() {

	host, start_port, stop_port := parse_arguments(os.Args)
	fmt.Printf("Starting port scan of %s (%d-%d):\n", host, start_port, stop_port)

	message_channel := make(chan scanned_port, 500) //(stop_port - start_port)) //change buffer size later

	for port := start_port; port <= stop_port; port++ {
		go scanPort(host, port, message_channel)
	}

	ports := 0
	for port := start_port; port <= stop_port; port++ {
		var new_message scanned_port = <-message_channel
		if new_message.isOpen {
			fmt.Printf("Port %d is open\n", new_message.port)
			ports++
		} else {
			if VERBOSE {
				fmt.Printf("Error: %s\n", new_message.problem)
			}
		}
	}

	close(message_channel)
	print_result(ports)
}
