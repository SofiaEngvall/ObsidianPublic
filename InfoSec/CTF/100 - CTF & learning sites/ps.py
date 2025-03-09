import base64
import zlib

# Your base64 encoded string
base64_str = "hVRdb9owFH1H4j9YFAmiNab0Y6tou6mFrUXaOjTo+lBNrZtciLdge/ZNaNT1v+/GBAbbw4IEuZ/nnuNrTnfYWM+BGb0A6xJIUxbpGNjO23ptmqkIpVbsEhRYgRB+leSYDwfsuV5j9DQzB1YJqj9jTVB574bsa7JPqnhkss1wX89Nhtsp0lC0zR6WZvlcAobXgMNRX6upnGUEXU7xazPnNgEL4efH7xAhe2Z/Ar7nPR+O8sMBTEWW4iVNvhAFCxWwpsqI4cN2eihU/LePWtAI57EwNC4fo8DM+Q6NgXSRVopwIW5slr2sjMCjn8exBefovXqr1yrGCE9YKkLMX7FGs0Hfa6HWjpWyVc1FgeCo6G5cOIQ5n1AP/l7RWUk1+9br3ShZnhsn7Xxq26MEVbVPhHjige9I1hwsUtVEXwgHrw/HaKlNe4kSrAedx0cEqWAR6qXQ4aQwUB4eq8YYQ5RZiQXv28KgnllhkoJ/Ghwt7THYXEYwsjqXMdjV0uD0+D99Pb2byYfjFcWqNBEu2VDhQmJFBqynsyJCk/Nq2a6opO0xN8TZECQIgu3m/pdP9MfySrQDFlowqYiAtcLWLmu1Tlb6WMDMqmU+OV9K/y2pAeGVdkibohcq1aIcnxlRpELHjXqtmftLdC9jwvrnZlGfocr1Dwhv4fEL/MzAYbuVIJpep9PdO+T7B2/4Ae929ztZLvb3uscdh2IGB9y47rtlaxmftcoVWgMRwdMdNtNsqi0muwyexFzSLmMCTDzqHJiLrDRYxr1zmoqZ/wsoP78B"

# Step 1: Base64 decode
decoded_data = base64.b64decode(base64_str)

# Step 2: Decompress using raw deflate
decompressed_data = zlib.decompress(decoded_data, -15)  # -15 tells zlib to use raw deflate (no header)

# Step 3: Convert to a string (assuming it's ASCII/UTF-8 encoded)
try:
    decoded_text = decompressed_data.decode('utf-8')  # Or 'ascii' if necessary
    print(decoded_text)
except UnicodeDecodeError as e:
    print("Error decoding text:", e)
