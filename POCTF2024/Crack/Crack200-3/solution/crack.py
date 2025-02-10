from itertools import product
from Crypto.Cipher import ARC4
import string

# Ciphertext (hex-encoded from the challenge)
ciphertext_hex = "718113f7f7b287bdc677686725aefd99006e2e53e6605050aea80f9b0a"
ciphertext = bytes.fromhex(ciphertext_hex)

# Character set for brute force (A-Z only based on challenge hint)
charset = string.ascii_uppercase

# Key length (8 characters)
key_length = 8

# Brute force all possible keys
for key_tuple in product(charset, repeat=key_length):
    key = ''.join(key_tuple)  # Generate key as string

    # Decrypt using RC4
    cipher = ARC4.new(key.encode())
    decrypted = cipher.decrypt(ciphertext)

    # Check if the decrypted text makes sense (e.g., ASCII-readable or contains known plaintext)
    try:
        decrypted_text = decrypted.decode()
        if all(c in string.printable for c in decrypted_text):  # Ensure it's printable
            print(f"[+] Key Found: {key}")
            print(f"[+] Decrypted Text: {decrypted_text}")
            break
    except UnicodeDecodeError:
        # Skip non-decodable results
        continue

