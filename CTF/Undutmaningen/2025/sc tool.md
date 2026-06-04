
https://github.com/CTFd/snicat

snicat - CTFd's tool

available for Windows, Linux and Mac

similar to nc

Use as proxy using the -bind switch

go version code
```go
package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"

	sclient "git.rootprojects.org/root/sclient.go"
)

var insecure = flag.Bool("insecure", false, "Disable verification of server SSL certificate")
var servername = flag.String("servername", "", "Server Name Indication (SNI) to provide to the server (e.g. ssl.example.com)")
var bind = flag.String("bind", "", "Tunnel connection to a local unencrypted port (e.g. localhost:3000, 3000)")
var (
	commit  = "unknown"
	version = "v0.0.2"
)

func init() {
	flag.BoolVar(insecure, "k", false, "Shorthand for -insecure")
	flag.StringVar(servername, "sni", "", "Shorthand for -servername")
	flag.StringVar(bind, "b", "", "Shorthand for -bind")
}

func Usage() {
	fmt.Println(os.Args[0], "<hostname>", "<port>")
	fmt.Println("version:", version)
	fmt.Println("commit:", commit)
	fmt.Println()
	flag.Usage()
}

func main() {
	flag.Parse()

	if flag.NArg() < 1 {
		Usage()
		os.Exit(1)
	}

	hostname := flag.Arg(0)
	var port int
	var err error
	if strings.Contains(hostname, ":") {
		split := strings.Split(hostname, ":")
		hostname = split[0]
		port, err = strconv.Atoi(split[1])
		if err != nil {
			fmt.Println(flag.Arg(1), "is not a valid remote port")
			os.Exit(1)
		}
	} else {
		portArg := flag.Arg(1)
		if len(portArg) != 0 {
			port, err = strconv.Atoi(portArg)
			if err != nil {
				fmt.Println(flag.Arg(1), "is not a valid remote port")
				os.Exit(1)
			}
		} else {
			port = 443
		}
	}

	localAddress := "-"
	var localPort int
	if len(*bind) > 0 {
		if strings.Contains(*bind, ":") {
			split := strings.Split(*bind, ":")
			localAddress = split[0]
			localPort, err = strconv.Atoi(split[1])
			if err != nil {
				fmt.Println(*bind, "is not a valid local port")
				os.Exit(1)
			}
		} else {
			localAddress = "localhost"
			localPort, err = strconv.Atoi(*bind)
			if err != nil {
				fmt.Println(*bind, "is not a valid local port")
				os.Exit(1)
			}
		}
	}

	if len(*servername) == 0 {
		servername = &hostname
	}
	sclient := &sclient.Tunnel{
		ServerName:         *servername,
		RemoteAddress:      hostname,
		RemotePort:         port,
		LocalAddress:       localAddress,
		LocalPort:          localPort,
		InsecureSkipVerify: *insecure,
	}
	sclient.DialAndListen()
}
```
https://github.com/therootcompany/sclient

python version code (doesn't have -bind)
```python
#!/usr/bin/env python3
from telnetlib import Telnet
import argparse
import ssl

parser = argparse.ArgumentParser(description="Connect to services behind an SNI proxy.")

parser.add_argument("hostname", type=str, help="hostname to connect to")
parser.add_argument(
    "port", type=int, default=443, nargs="?", help="port to connect to",
)
parser.add_argument(
    "--insecure",
    "-k",
    action="store_true",
    help="Disable verification of server SSL certificate",
)
parser.add_argument(
    "--servername",
    "-sni",
    type=str,
    default=None,
    nargs="?",
    help="Server Name Indication (SNI) to provide to the server (e.g. ssl.example.com)",
)

args = parser.parse_args()

context = ssl.create_default_context()
if args.insecure:
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

tn = Telnet(args.hostname, args.port)

servername = args.servername
if servername is None:
    servername = args.hostname

with context.wrap_socket(tn.sock, server_hostname=servername) as secure_sock:
    tn.sock = secure_sock
    tn.interact()
```