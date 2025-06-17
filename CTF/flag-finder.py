import re

# File to check (change this to your filename)
filename = r"C:\Users\sofia\Desktop\free_flags.txt"  

# Regular expression pattern for flag{32-hex-chars}
pattern = re.compile(r'flag\{[0-9a-f]{32}\}', re.IGNORECASE)

try:
    with open(filename, 'r') as file:
        valid_flags = []
        
        for line in file:
            line = line.strip()  # Remove whitespace
            
            if pattern.fullmatch(line):
                valid_flags.append(line)
        
        # Print results
        print(f"Found {len(valid_flags)} valid flags:")
        for flag in valid_flags:
            print(flag)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
