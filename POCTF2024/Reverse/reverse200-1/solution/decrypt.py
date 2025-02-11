# La chaîne hexadécimale extraite
hex_string = "2d383c313f2432302c2d08710870356e376f086d3f083b6c713270262a"

# Convertir la chaîne hexadécimale en bytes
obfuscated_bytes = bytes.fromhex(hex_string)

# Fonction de déobfuscation (soustraction de 3, puis XOR avec 90)
def reverse_obfuscate(obfuscated_bytes):
    return bytes((byte - 3) ^ 90 for byte in obfuscated_bytes)

# Appliquer la déobfuscation
deobfuscation = reverse_obfuscate(obfuscated_bytes)

# Convertir le résultat final en chaîne ASCII pour voir le flag
flag = deobfuscation.decode('utf-8', errors='ignore')
print(flag)

