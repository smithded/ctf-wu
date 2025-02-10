Quand tu lis et analyse la description du challenge, tu te rends compte que tu dois utiliser un dictionnaire, mais lequel?

Ici l'accent est mis sur la langue française, ainsi il te faut un dictionnaire de mots français, le challenge ici est de comprendre que c'est un dictionnaire de verbe conjugués, en faisant une recherche sur github on trouve un tel dictionnaire.

On extrait le hash du fichier pdf puis on fait appel à john

password : surinvesti

Le pdf contient ceci :_cG9jdGZ7dXdzcF9XMW5kNV8wZl9DaDRuZzN9_

N'estce pas la forme d'un encodage base64, on tente de le décrypter

```
echo "cG9jdGZ7dXdzcF9XMW5kNV8wZl9DaDRuZzN9" | base64 -d
```

## Flag

**poctf{uwsp_W1nd5_0f_Ch4ng3}**
