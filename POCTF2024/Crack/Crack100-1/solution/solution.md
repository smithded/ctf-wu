It's a Crack chall, for this challenge we have to find password for the zip file that contain the flag.txt

Since this is a 100 points level I tried a dictionary attack using rockyou.txt with this command

```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

password: lol12345

Opening up our archieve, we got the flag

**poctf{uwsp_7h3_hum4n_c0nd1710n}**

---
Pour ce challenge il faut trouver un mot de passe pour ouvrir l'archive

Du moment où ce challenge est de niveau 100, on a juste essayer une attacque par dictionnaire en utilisant le fameux rockyou.txt

Cette commande nous revele le mot de passe, après avoir récupérer le hash

```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

Et le mot de passe est _lol12345_

On découvre notre flag.txt qui est:

**poctf{uwsp_7h3_hum4n_c0nd1710n}**
