## Introduction

Ce challenge de stéganographie, intitulé "Stego100-2: Reading Between the Lines", consistait à extraire un message caché dans un fichier texte apparemment ordinaire, mais contenant des caractères spéciaux de largeur nulle (zero-width characters). Ces caractères sont souvent utilisés dans les défis de stéganographie pour cacher des informations discrètement au sein d’un texte.

## Étapes de résolution

    ### Analyse du fichier et découverte initiale:
        En examinant le fichier texte avec la commande cat -A Stego100-2.txt, on a observé des symboles étranges (M-bM-^@M-^L et autres) indiquant que le fichier contenait des caractères non imprimables, souvent encodés en Unicode.
        En utilisant xxd pour examiner le contenu hexadécimal (xxd Stego100-2.txt), nous avons découvert des caractères de largeur nulle, tels que U+200B (Zero Width Space), U+200C (Zero Width Non-Joiner), et U+200D (Zero Width Joiner). Ces caractères sont souvent utilisés pour encoder des données cachées en binaire.

    Décodage des caractères de largeur nulle:
        Nous avons interprété les caractères de la façon suivante :
            U+200B (Zero Width Space) représente le bit 1.
            U+200C (Zero Width Non-Joiner) représente le bit 0.
            U+200D (Zero Width Joiner) peut être ignoré ou utilisé comme séparateur.

En utilisant decode.py, on a 

**poctf{uwsp_b3w4r3_7h3_j4bb3rw0ck}**
