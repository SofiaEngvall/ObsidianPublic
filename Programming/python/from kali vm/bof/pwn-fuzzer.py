#!/usr/bin/env python3

import socket, time, sys
from pwn import cyclic

ip = "localhost"
port = 9999
use_pattern = True


timeout = 5

steps = 0 #0 at start
step_size = 100

def get_string(total_size):
  if not use_pattern:
    return b'A'*total_size
  else:
    return cyclic(total_size)
  
try:

  while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))

      steps += 1
      total_size = steps * step_size

      string = get_string(total_size)

      print("Fuzzing with {} bytes.".format(len(string) - len(prefix)))
      print("Send: "+str(string))
      s.send(string+b'\n') #add \r\n if can't recv data

      print("Recv: "+str(s.recv(1024)))

      time.sleep(1)

except Exception as e:
  print("Fuzzing crashed: "+str(e))
  sys.exit(0)
