Utilisez string *.jpeg à la fin on trouve qu'il y a un fichier *flag.txt et en bas *probably_improbable* qui sera le pass à Utilisez dans le zip que va extraire binwalk (binary walk) 
Utilisez binwalk -e img.jpeg
Utilisez unzip -P probably_improbable *.zip 
et une fois encore erreur et resolution de l'erreur, il faut utiliser 
7z x *.zip puis boom mon fichier est extrait avec le pass

**poctf{uwsp_w3_4r3_such_57uff}**
