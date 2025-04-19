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


- Nem elég a klóz, (klóz, változó) kell
- Nem Hamilton kör kell, hanem valszeg Euler-szerű kör, ami végigsétál az összes élen, nem feltétlen egyszer
- És nem is kell kör, elég hogy ne fusson bele olyan attraktorba, ami az ellentéte

Tartalmaznia kell 
- az összes klózát legalább egy ágon, 
- tranzitíve, azaz 
  - ha választott egy ágat, akkor
  - az azon az ágon lévő változó összes klózát is tartalmazni kell legalább egy ágon
  - amihez elég lehet valami körszerű képződmény...
  
Kell egy kör, ami tartalmazza

- a változót
- a kör összes változójának összes klózának legalább egy implikációs ágát

ez egy részmegoldás, ha n-változós, akkor teljes megoldás

Szóval, nem kör kell hanem 
- páros gráf, ami lefedi az összes változót és 
- az összes klózt.

Ez egy megoldás, de ez kevés, el kell rontani a többit:-)

Ezt kell levezetni azokra, ami nem megoldás: $x = bool \implies x = \lnot bool$ ha SAT.
Vagy ezt kell levezetni minden változóra: $x = bool \iff x = \lnot bool$ ha UNSAT.