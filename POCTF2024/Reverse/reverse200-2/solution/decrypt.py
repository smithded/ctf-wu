#!/usr/bin/python3

def reverse_transform(s):
    return ''.join([chr((ord(c) - 5) ^ 0x3f) for c in s])

hardcoded_string = "TUaP^IOMQTe\r\\\x11eV\x13\x0e\\\re\x13\x0fe`\x10RYG"
valid_input = reverse_transform(hardcoded_string)
print(valid_input)

#poctf{uwsp_7h3_n16h7_15_d4rk}
