
plaintext = "Lorem ipsum has et perpetua expetendis, explicari similique mnesarchum ei sed. Ius id tale persius assueverit. Sed vide autem erant te, justo fabellas an sit, et per sonet decore. Cum ad doctus placerat, sed at elit sensibus. Adhuc animal adversarium sed ei. Ea vel partem noluisse interpretaris, ei iudico oratio temporibus per. Commodo eloquentiam vis eu, ne fierent dissentiet pri. Idque dolorum efficiendi eum ad, ut wisi nemore urbanitas eos. Eu eam inermis vituperatoribus possim, in vis graeci invidunt apeirian."
ciphertext = "Nwglq zhslq muf gb elvgwtle jrcgbtuhzk, eotqcpczx zmdalzuzy zpmhhvtzud in mrf. Qjz mu laci uyeuqjz ejkuvzjlvv. Atk zzve ryyyz gzpux kw, jlwyi scjtsprk ae wnn, rv xty wffek hjwbtm. Rbq rv dfgyof rtpjiist, jii ug gtxa wvfszfzm. Nfpjj eeamrp fxigzhhvzmm jii yv. Gi klp gsrkir hbncxzwv ankiwjegbpymj, wi zyicpq wghxzg tvquiekjjz tvj. Cfqriqq mavulwnkmfg ika tb, rv xivvjhg fqhzielivx ulv. Klfbi uglfvzg rhnxjmvfdz izg nf, ci dmja nvqtlr wzqhrzlaj itm. Rw mpt mewrdmx pvvcelvrloimgof rwhzmd, an mmx aecmrp meniuysn nrmxymrf."

# Initialize a list to store the mappings
mappings = []

# Function to get the letter corresponding to the shift
def get_shift_letter(shift):
    return chr(ord('a') + shift)

# Iterate through both the plaintext and ciphertext
for p_char, c_char in zip(plaintext, ciphertext):
    if p_char.isalpha() and c_char.isalpha():  # Only consider alphabetic characters
        # Calculate the shift difference between corresponding letters
        p_index = ord(p_char.lower()) - ord('a')
        c_index = ord(c_char.lower()) - ord('a')
        shift = (c_index - p_index) % 26  # Calculate the shift and ensure it wraps around if negative
        shift_letter = get_shift_letter(shift)
        mappings.append(f"{p_char.lower()} {c_char.lower()} {shift} {shift_letter}")

# Output the mappings
for mapping in mappings:
    print(mapping)
