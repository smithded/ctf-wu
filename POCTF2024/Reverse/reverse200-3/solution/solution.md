En inspectant le code avec `binninja`  on voit une sorte de flag dans la fonction `main`, ceci

optc{fwups1_4__mh7_3c043}n

Connaissant le format de notre flag, poctf{uwsp_, On comprend vite qu'il faut demeler le pseudo-flag en comptant 2 lettres à la fois puis en inversant i.e 

optc{f devient en 1ere étape (op => po) + (tc => ct) + ({f => f{)

Ainsi de suite jusqu'à obtenir le flag

**poctf{uwsp_1_4m_7h3_0c34n}**
