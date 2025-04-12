exponent = # Den privata exponenten

# Dekryptera flaggan
enc_flag = open('sparsam/flagga.enc', 'rb').read()
modulus = 0x83398ec472e8b8716c244db4836bbd5c66895bfd1088e1bd97b64c7c162bfab57c99cac03e1b47a67b20de364d75330e2badb5727081cd254666d6eec782b41b
flag = pow(int.from_bytes(enc_flag), exponent, modulus).to_bytes(64, 'big').decode()
print(flag)
