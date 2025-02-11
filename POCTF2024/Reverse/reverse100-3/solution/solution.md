### Vue d'ensemble du code

Le code est conçu pour décoder un flag qui a été encodé en utilisant une série de modifications basées sur une "seed". Le processus de décodage implique d'inverser ces modifications. Voici les étapes principales :

1. **Affichage du flag encodé** : Le code commence par afficher le flag encodé en hexadécimal.
2. **Inversion des modifications** : Le code doit inverser les modifications appliquées au flag encodé en utilisant une fonction spécifique.
3. **Affichage du flag décodé** : Après avoir inversé les modifications, le code affiche le flag décodé en hexadécimal.

### Exemples pour illustrer les étapes

#### 1. Affichage du flag encodé

Le flag encodé est stocké dans un tableau de bytes :

```c
unsigned char encoded_flag[] = { 0x8e, 0x79, 0xa9, 0x9c, 0xac, 0xd5, 0xc5, 0xc7, 0x91, 0x7a, 0xa5, 0x8a, 0xb8, 0x8d, 0xc6, 0x81, 0x55, 0x83, 0xa5, 0x59, 0x7b, 0xb9, 0x87, 0xb8, 0x51, 0x69, 0x7b, 0x58, 0xbb, 0x8b, 0xcd};
```

Le code affiche ce flag encodé en hexadécimal :

```c
printf("Encoded flag: ");
print_flag_hex(encoded_flag, length, 0);
```

Cela produirait une sortie comme :

```
Encoded flag: 8e79a99cacd5c5c7917aa58ab88dc6815583a5597bb987b851697b58bb8bcd
```

#### 2. Inversion des modifications

La fonction `reverse_modify_flag` est utilisée pour inverser les modifications appliquées au flag encodé. Cette fonction prend chaque byte du flag et soustrait le dernier chiffre de la `seed` :

```c
void reverse_modify_flag(unsigned char *flag, unsigned int seed) {
    int length = strlen((char *)flag);

    for (int i = 0; i < length; i++) {
        flag[i] = (flag[i] - (seed % 10)) % 256;  // Reverse each byte modification
        seed = seed / 10;
        if (seed == 0) {
            seed = 88974713;  // Reset seed if it runs out
        }
    }
}
```

Par exemple, si le premier byte du flag est `0x8e` et la `seed` est `88974713`, le dernier chiffre de la `seed` est `3`. Donc, le byte modifié serait `0x8e - 3 = 0x8b`.

#### 3. Affichage du flag décodé

Après avoir inversé les modifications 10 fois, le code affiche le flag décodé en hexadécimal :

```c
printf("Decoded flag (plaintext in hex): ");
print_flag_hex(encoded_flag, length, 0);
```

### Modification nécessaire pour décoder le flag

Pour décoder le flag, nous devons appeler la fonction `reverse_modify_flag` 10 fois. Voici comment nous pouvons le faire :

```c
int main() {
    unsigned char encoded_flag[] = { 0x8e, 0x79, 0xa9, 0x9c, 0xac, 0xd5, 0xc5, 0xc7, 0x91, 0x7a, 0xa5, 0x8a, 0xb8, 0x8d, 0xc6, 0x81, 0x55, 0x83, 0xa5, 0x59, 0x7b, 0xb9, 0x87, 0xb8, 0x51, 0x69, 0x7b, 0x58, 0xbb, 0x8b, 0xcd};

    unsigned int seed = 88974713;
    int length = sizeof(encoded_flag);

    printf("Encoded flag: ");
    print_flag_hex(encoded_flag, length, 0);

    // Reverse the modifications 10 times
    for (int i = 0; i < 10; i++) {
        reverse_modify_flag(encoded_flag, seed);
        print_flag_hex(encoded_flag, length, i + 1);  // Print flag after each reverse step
    }

    printf("Decoded flag (plaintext in hex): ");
    print_flag_hex(encoded_flag, length, 0);  // Print final decoded flag in hex

    return 0;
}
```

### Flag

Après exécution de solution.c on obtient le flag.

**poctf{uwsp_br3v17y_15_7h3_50u1}**
