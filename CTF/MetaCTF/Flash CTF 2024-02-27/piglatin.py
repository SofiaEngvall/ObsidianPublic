#!/usr/local/bin/python
import signal

# In-memory storage for user asheshay and asswordspay
user_data = {}

def ashhay(message):
    # Initial ashhay values
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Pad the message to 64 bytes
    message = message.ljust(64, b'\x00')

    # Process each 64-byte block
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        M = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        for m in M:
            A = (A + m + (B ^ C ^ D)) & 0xFFFFFFFF
            A = ((A << 3) | (A >> (32 - 3))) & 0xFFFFFFFF
            A, B, C, D = D, A, B, C

    # Concatenate the final ashhay values
    return f"{A:08x}{B:08x}{C:08x}{D:08x}"

def egisterray():
    print("\n--- Egistrationray ---")
    usernameyay = input("Enter usernameyay: ").strip()
    if usernameyay == 'admin':
        print("Registration failed: Usernameyay cannot be 'admin'.")
        return False
    for c in usernameyay:
        if ord(c) < 33 or ord(c) > 126:
            print("Registration failed: Unsupported character in usernameyay.")
            return False

    asswordpay = input("Enter asswordpay: ").strip()
    usernameyay_ashhay = ashhay(usernameyay.encode().ljust(64, b'\x00'))
    asswordpay_ashhay = ashhay(asswordpay.encode().ljust(64, b'\x00'))

    if usernameyay_ashhay in user_data:
        print("Registration failed: Usernameyay already exists.")
        return False

    user_data[usernameyay_ashhay] = asswordpay_ashhay
    print("Registration successful!")
    return True

def oginlay():
    print("\n--- oginlay ---")
    usernameyay = input("Enter usernameyay: ").strip()
    asswordpay = input("Enter asswordpay: ").strip()
    usernameyay_ashhay = ashhay(usernameyay.encode().ljust(64, b'\x00'))
    asswordpay_ashhay = ashhay(asswordpay.encode().ljust(64, b'\x00'))

    if usernameyay_ashhay in user_data and user_data[usernameyay_ashhay] == asswordpay_ashhay:
        if usernameyay == 'admin':
            print("oginlay successful! Admin session granted.")
            return usernameyay, True
        else:
            print("oginlay successful! User session granted.")
            return usernameyay, False
    else:
        print("oginlay failed: Invalid usernameyay or asswordpay.")
        return None, False

def iewvay_agflay():
    print("\n--- Iewvay Agflay ---")
    print(open('flag.txt','r').read())

def pig_latinify():
    print("\n--- Pig Latin-ify ---")
    text = input("Enter a string to convert to Pig Latin: ").strip()
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word[0].lower() in 'aeiou':
            pig_latin_word = word + 'way'
        else:
            pig_latin_word = word[1:] + word[0] + 'ay'
        pig_latin_words.append(pig_latin_word)

    pig_latin_text = ' '.join(pig_latin_words)
    print(f"Pig Latin: {pig_latin_text}")

def handle_client():
    print("=====================================")
    print(" Welcome to the Pig Latin Translator!")
    print("=====================================")
    print("You can egisterray and oginlay with your usernameyay and asswordpay.")

    usernameyay = None
    is_admin = False

    while True:
        if not usernameyay:
            print("\nOptions:\n1. egisterray\n2. oginlay\n3. Exit")
        else:
            if is_admin:
                print("\nOptions:\n1. Iewvay Agflay\n2. Logout\n3. Exit")
            else:
                print("\nOptions:\n1. Pig Latin-ify\n2. Logout\n3. Exit")
        choice = input("Choose an option: ").strip().lower()

        if choice in ["1", "egisterray"] and not usernameyay:
            egisterray()
        elif choice in ["2", "oginlay"] and not usernameyay:
            usernameyay, is_admin = oginlay()
        elif choice in ["1", "iewvay_agflay", "iewvay agflay"] and is_admin:
            iewvay_agflay()
        elif choice in ["1", "pig_latinify", "pig latin-ify", "pig_latinify", "pig latin-ify"] and not is_admin:
            pig_latinify()
        elif choice in ["2", "logout"] and usernameyay:
            print("Logged out successfully.")
            usernameyay = None
            is_admin = False
        elif choice in ["3", "exit"]:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    # Set a timeout for the session
    signal.alarm(300)
    handle_client()

if __name__ == "__main__":
    main()