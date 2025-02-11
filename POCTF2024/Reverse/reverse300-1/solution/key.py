# Reconstruct the key by reversing the XOR operations done in the reconstruct_key function.

def reconstruct_key():
    # The array from the C code 'local_2e' mapped directly
    local_2e = [0x66, 0x1a, 0x6e, 0x65, 0x16, 0x4d, 0x73, 0x70, 0x6a, 0x18, 1, 0x50, 8, 0x1f, 0x3b, 0x3d, 0x2f, 0x74, 0x73, 0x78, 0x76, 0x67]
    
    # Initialize empty key array to hold the reconstructed key
    key = [''] * 22

    # First loop (XOR with 0x10, filling positions 0 to 4)
    for i in range(5):
        key[i] = chr(local_2e[i + 0x11] ^ 0x10)

    # Second loop (XOR with 0x5A, filling positions 5 to 9)
    for i in range(5):
        key[i + 5] = chr(local_2e[i + 0xc] ^ 0x5a)

    # Third loop (XOR with 0x20, filling positions 10 to 14)
    for i in range(5):
        key[i + 10] = chr(local_2e[i + 7] ^ 0x20)

    # Fourth loop (XOR with 0x30 or 0, filling positions 15 to 21)
    for i in range(7):
        if i < 5:
            key[i + 15] = chr(0x30 ^ local_2e[i])
        else:
            key[i + 15] = chr(0x00 ^ local_2e[i])
    
    return ''.join(key)

# Reconstruct the key
reconstructed_key = reconstruct_key()
print(reconstructed_key)

#the key
#dchfwREaguPJ8!pV*^U&Ms
#The flag
#poctf{uwsp_7h3_w0rld_15_4_57463}
