def process_input(input_text):
    shifted_text = input_text[-1:] + input_text[:-1]  # Shift right by 1
    print(input_text, shifted_text)
    # XOR the shifted text against itself
    xor_result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(input_text, shifted_text))
    
    # Convert the result to hex
    hex_output = xor_result.encode('utf-8').hex()
    
    # Print to terminal
    print(hex_output)
    
    # Write to file
    with open('output.txt', 'w') as f:
        f.write(hex_output)

if __name__ == "__main__":
    plaintext = input("Enter your plaintext: ")
    process_input(plaintext)