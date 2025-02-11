# Read file
with open("Stego100-2.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Map zero-width characters to binary, ignoring others
binary_string = text.replace("\u200B", "1").replace("\u200C", "0")

# Remove any characters that aren't '1' or '0' (if any sneaked in)
binary_string = ''.join(filter(lambda x: x in '01', binary_string))

# Convert binary to ASCII, grouping into 8-bit chunks
try:
    hidden_message = "".join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    print("Hidden message:", hidden_message)
except ValueError as e:
    print("An error occurred during binary conversion:", e)

