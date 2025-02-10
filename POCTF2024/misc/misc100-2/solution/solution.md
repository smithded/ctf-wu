### Challenge : A Coward Dies Twice (Misc, 100 points)

**Analyser les indices :**
   - Le titre est un poème composé de quatre mots, avec des mots de 3 à 5 lettres chacun.
   - Aucun mot ne contient des lettres en double, et le premier mot est "The".

**Résoudre l’anagramme :**
   - Avec les lettres fournies : **A, D, E, N, K, R, O, T, T, O, N, H, A, T, E**, une possibilité de titre de poème correspondant est **“The Road Not Taken”** de Robert Frost.
   - Vérifions :
     - Cette phrase comporte bien quatre mots : **The Road Not Taken**.
     - Chaque mot respecte la limite de 3 à 5 lettres.
     - Aucun mot n’a de lettres en double.

**Convertir en Leetspeak :**
   - En utilisant le jeu de caractères fourni `4bcd3f6h1jklmn0pqr57uvwxyz`, on peut transcrire chaque mot en Leetspeak :
     - "The" → **7h3**
     - "Road" → **r04d**
     - "Not" → **n07**
     - "Taken" → **74k3n**

**Assembler le flag :**
   - En intégrant ces mots en Leetspeak dans le format donné `poctf{uwsp_7h3_ _ _ }`, on obtient :
     ```
     poctf{uwsp_7h3_r04d_n07_74k3n}
     ```

### Flag final :
```
poctf{uwsp_7h3_r04d_n07_74k3n}
```
