def rotate_char_combined(c, shift):
    """Rotates a-z and 0-9 as one continuous sequence (36 chars)"""
    if c == '_':
        return c
    sequence = "abcdefghijklmnopqrstuvwxyz0123456789"
    if c in sequence:
        idx = sequence.index(c)
        rotated_idx = (idx + shift) % len(sequence)
        return sequence[rotated_idx]
    return c

def rotate_char_separate(c, shift):
    """Rotates a-z (26) and 0-9 (10) as independent sequences"""
    if c == '_':
        return c
    if c.islower():
        rotated = chr(((ord(c) - ord('a') + shift) % 26 + ord('a')))
    elif c.isdigit():
        rotated = str((int(c) + shift) % 10)
    else:
        return c
    return rotated

def from_leet(text):
    """Converts leetspeak numbers to letters (e.g., 'a7mvh' → 'a_t_vh')"""
    leet_map = {'1':'i', '2':'z', '3':'e', '4':'a', '5':'s', '6':'g', '7':'t', '8':'b', '9':'p', '0':'o'}
    return ''.join(leet_map.get(c, c) for c in text)

def rotate_word(word, shift, mode="combined"):
    """Applies rotation based on selected mode (combined/separate)"""
    rotate_func = rotate_char_combined if mode == "combined" else rotate_char_separate
    return ''.join(rotate_func(c, shift) for c in word)

# Encoded flag and test case
encoded_flag = "b8nwi_h6um8m_o8so_wzo_"
test_case = ("see_yea", "tff_vbx")  # (original, rotated)

# Test both methods on the known pair
print("=== Validating Rotation Methods ===")
for mode in ["combined", "separate"]:
    for shift in range(1, 36):
        rotated = rotate_word(test_case[0], shift, mode)
        if rotated == test_case[1]:
            print(f"Match found: {mode} rotation, shift={shift}")

# Decode flag with all shifts using both methods
print("\n=== Decoding Flag (All Shifts) ===")
for mode in ["combined", "separate"]:
    print(f"\nMode: {mode}")
    for shift in range(1, 36):
        decoded = rotate_word(encoded_flag, -shift, mode)
        leet_decoded = from_leet(decoded)
        print(f"Shift -{shift}: {decoded}  →  Leet: {leet_decoded}")
        