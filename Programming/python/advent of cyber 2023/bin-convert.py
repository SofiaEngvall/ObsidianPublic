
# Decoded: https://tryhackme.com/jr/adv3nt0fdbopsjcap

# binary_data = '00101010 01101000 01110100 01110100 01110000 01110011 00111010 00101111' # *https:/
# binary_data = '00101111 01110100 01110010 01111001 01101000 01100001 01100011 01101011' # /tryhack
# binary_data = '01101101 01100101 00101110 01100011 01101111 01101101 00101111 01101010' # me.com/j
# binary_data = '01110010 00101111 01100001 01100100 01110110 00110011 01101110 01110100' # r/adv3nt
# binary_data = '00110000 01100110 01100100 01100010 01101111 01110000 01110011 01101010' # 0fdbopsj
binary_data = '01100011 01100001 01110000 00000101 10011010 01100000 11011101 01011000 0100010'  # cap♣

ascii_string = ''
binary_data = binary_data.strip()
for binary_segment in binary_data.split(' '):
    decimal_data = int(binary_segment, 2)
    ascii_char = chr(decimal_data)
    ascii_string += ascii_char
print(ascii_string)  # returns 'hello'
