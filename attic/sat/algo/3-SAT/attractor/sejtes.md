x = bool

- megoldható, ha az implikációs gráfban
- a hozzá közvetve vagy közvetlenül kapcsolodó kikötésekben van Hamilton kör, ami átmegy rajta

$$
(subs \ x_1 = bool_1), (clause_1...) \ may \implies 
(subs \ x_2 = bool_2), (clause_2...) \ may \implies 
... 
$$

$$
(subs \ x_i = bool_i), (clause_i...) \ may \implies 
...
$$

$$
(subs \ x_n = bool_n), (clause_n...) \ may \implies 
(subs x_1 = bool_1)
$$

és nem vezet ki a fenti kör, nincs olyan klóz, ami 


- nem megoldható, ha befut egy attraktorba????
