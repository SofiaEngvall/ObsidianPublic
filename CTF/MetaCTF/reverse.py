# The given hex output
hex_output = "686950021716160b1a54541b4f59161a590c41414d0c0f1759541b4f4f010b490c4f010b455716185946131b0d171d06014f016969530607174548071f1545541c0915544e014f4f010b45460f0e12071716534f1a0154414157161859541b4f421017040a4b491d580c4207060214061645541c09155457181a1908444207454b02070a444f094641161c1c1613164a0e743c0d45460a0d064749074e4302121645531c02080a010b4543020f4e491a536d2811152217123d0f03476f28434d2639131b0d1745015e31325d42416c335d5a586c365e4a510c42170154490f4659161a52551745521704050d070947541c011a5f0c696947121016005359161a55410d1e1704051d5942101d040e45491d5a00000e7732091c5c0c696e4b004c4a1f0607544b0e001550420709050c131f07094759161a55480917130b495355"

# Convert hex to bytes
xor_bytes = bytes.fromhex(hex_output)

# Convert bytes to string (original XOR result)
xor_result = xor_bytes.decode('utf-8')

# Initialize lists for reconstruction
original_chars = [None] * len(xor_result)
shifted_chars = [None] * len(xor_result)

# First, handle all characters except the first
for i in range(1, len(xor_result)):
    # shifted[i] = original[i-1]
    if original_chars[i-1] is not None:
        shifted_chars[i] = original_chars[i-1]
        original_chars[i] = chr(ord(xor_result[i]) ^ ord(shifted_chars[i]))

# Now handle the first character
# shifted[0] = original[-1]
if original_chars[-1] is not None:
    shifted_chars[0] = original_chars[-1]
    original_chars[0] = chr(ord(xor_result[0]) ^ ord(shifted_chars[0]))

    # Now that we have original[0], we can verify/fix other characters
    for i in range(1, len(xor_result)):
        shifted_chars[i] = original_chars[i-1]
        original_chars[i] = chr(ord(xor_result[i]) ^ ord(shifted_chars[i]))

# Reconstruct the original string
original_text = ''.join(original_chars)

print("Recovered plaintext:", original_text)