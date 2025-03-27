number_str = "7710111697678470123108511161165111411595971145195115491091121081219597100118521109951100951101171099851114115125"

def convert_to_ascii_from_string(number_str):
    result = []

    while len(number_str) > 0:
        if int(number_str[:3]) < 256:
            chunk = number_str[:3]
            number_str = number_str[3:]
        else:
            chunk = number_str[:2]
            number_str = number_str[2:]
        
        char_code = int(chunk)
        if 0 <= char_code <= 255:  # Check if it's a valid ASCII code
            result.append(chr(char_code))
            print(chunk+" = "+chr(char_code))
        else:
            print("something went wrong")
    
    # Join the result into a final string
    print(result)
    return ''.join(result)

# Convert the string to ASCII
decoded_message = convert_to_ascii_from_string(number_str)

# Output the result
print(decoded_message)

