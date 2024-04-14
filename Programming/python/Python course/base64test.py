import base64

# use ascii  to use  one byte per char
to_encode = "A test text 123456".encode("ascii")

encoded = base64.b64encode(to_encode)

print(to_encode)
print(encoded)


print("\nTest 2\n------")

# Encode a string to base64
original_string = "Hello, World!"
encoded_bytes = base64.b64encode(original_string.encode())
print("Encoded:", encoded_bytes)

# Testing that adding more = to the end does not affect the decoding
encoded_bytes += b'=='
print("Encoded:", encoded_bytes)

# Decode base64 back to a string
decoded_bytes = base64.b64decode(encoded_bytes)
decoded_string = decoded_bytes.decode()
print("Decoded:", decoded_string)
