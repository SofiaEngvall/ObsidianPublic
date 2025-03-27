from base64 import b64decode
from Crypto.Cipher import AES

# Constants
key = bytes.fromhex("4e9906e8fcb66cc9faf49310620ffee8f496e834292cb01ca636aae947e04759")
iv = bytes.fromhex("00000000000000000000000000000000")

# Encrypted password (from the cpassword attribute)
cpassword = "9QHhFTUdm6rDgu30J7ShZfqt07T6vOUGkyAFG3G7M+5AotJjkOva7E9KSAcamdrruTgly0O/uVTB/UUdLNU4775b5381hyuUzkd4lJW+llcNNNrQlYu7zqH3/i+8jfjhUq9lqPn8VjCtb9iaEqWbKQ"
cpassword = cpassword + "=" * ((4 - len(cpassword) % 4) % 4)  # Add padding if needed

# Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = cipher.decrypt(b64decode(cpassword))

# Attempt to remove padding bytes from decrypted data
try:
    plaintext = decrypted_data.decode('utf-16-le').rstrip('\x0e')
except UnicodeDecodeError:
    plaintext = decrypted_data.decode('utf-8').rstrip('\x0e')

print("Decrypted password:")
print(plaintext)
