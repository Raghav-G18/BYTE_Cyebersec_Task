import base64

# Layer 1: The raw Base64 challenge string
raw_b64 = "QkFJTntiQTczX1E4Ul9BcmhIQ19YNHlHY0R9"

# Step 1: Decode Base64
decoded_bytes = base64.b64decode(raw_b64)
ciphertext_full = decoded_bytes.decode('utf-8')

print(f"Layer 1 (Base64 Decoded): {ciphertext_full}")
# This prints: BAIN{bA73_Q8R_ArhHC_X4yGcD}

# Extract the inner ciphertext inside the brackets
# ciphertext_full looks like "BAIN{bA73_Q8R_ArhHC_X4yGcD}"
inner_cipher = ciphertext_full.split("{")[1].rstrip("}")
key = "CYBR"

# Layer 2: Beaufort Decryption logic
decrypted = []
k_idx = 0
for c in inner_cipher:
    if c.isalpha():
        c_val = ord(c.lower()) - 97
        k_val = ord(key[k_idx % len(key)].lower()) - 97
        p_val = (k_val - c_val) % 26
        char = chr(p_val + 97)
        decrypted.append(char.upper() if c.isupper() else char)
        k_idx += 1
    else:
        decrypted.append(c)

# Final Flag assembly
final_flag = "BYTE{" + "".join(decrypted) + "}"
print(f"Final Flag: {final_flag}")

print("It looks like it is saying 'Byte Laa Chuka Badlav'. ")
