package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"time"
)

type scanned_port struct {
	port    int
	isOpen  bool
	problem error
}

const VERBOSE = false

var (
	bad_context_count         int = 0
	refused_connection_count  int = 0
	timeout_count             int = 0
	insufficient_buffer_count int = 0
	invalid_port_count        int = 0
)

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

	var beginTime = time.Now()

	host, start_port, stop_port := parse_arguments(os.Args)
	fmt.Printf("Starting port scan of %s (%d-%d):\n", host, start_port, stop_port)

	message_channel := make(chan scanned_port, (stop_port - start_port)) //change buffer size later

	for port := start_port; port <= stop_port; port++ {
		go scanPort(host, port, message_channel)
		time.Sleep(time.Microsecond * 100) //remove later, for testing
	}

	ports := 0
	for port := start_port; port <= stop_port; port++ {
		var new_message scanned_port = <-message_channel
		if new_message.isOpen {
			fmt.Printf("Port %d is open\n", new_message.port)
			ports++
		} else {
			var tempStr string = fmt.Sprint(new_message.problem)
			if VERBOSE {
				fmt.Printf("Error: %s\n", tempStr)
			}

			if strings.Contains(tempStr, "connectex: The requested address is not valid in its context.") {
				bad_context_count++
			}
			if strings.Contains(tempStr, "connectex: No connection could be made because the target machine actively refused it.") {
				refused_connection_count++
			}
			if strings.Contains(tempStr, "connectex: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.") {
				timeout_count++
			}
			if strings.Contains(tempStr, "bind: An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.") {
				insufficient_buffer_count++
			}
			if strings.Contains(tempStr, "invalid port") {
				invalid_port_count++
			}
		}
	}

	close(message_channel)
	print_result(ports)
	fmt.Printf("-----------------------------------------------------------------------------------------------\n")
	fmt.Printf("refused_connection_count (closed): %d\n", refused_connection_count)
	fmt.Printf("timeout_count: %d\n", timeout_count)
	fmt.Printf("insufficient_buffer_count: %d\n", insufficient_buffer_count)
	fmt.Printf("invalid_port_count: %d\n", invalid_port_count)
	fmt.Printf("bad_context_count: %d\n", bad_context_count) //port 0
	fmt.Printf("-----------------------------------------------------------------------------------------------\n")

	t := time.Since(beginTime)
	fmt.Printf("Total time: %02f\n", t.Seconds())

}
