# The given number to convert
number_str = "661916610223539415142000000634030248871388513406397818523288057308"

# The base64 character set
custom_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Base we're converting to
base = len(custom_charset)  # 64
print(base)

# Convert the number from base 10 to base 64 using the custom character set
def base10_to_custom_base(number_str, base, charset):
    number = int(number_str)
    result = ""
    while number > 0:
        remainder = number % base
        result = charset[remainder] + result
        number //= base
    return result

# Convert and output the result
base64_conversion = base10_to_custom_base(number_str, base, custom_charset)
print(base64_conversion)
