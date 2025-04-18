## Bolyongás

Analógia: Google Page Rank

Minden érték, $x$ (lánc, $xyz...$) bolyong az implikációs gráfon a következő szabályok szerint

- Mozgás 
  - Minden implikációt "linket" bejár 
  - Amikor a $chain$ választhat változót egy klauzurára (csoportra), akkor 
    - megjegyzi a választását a klauzúrával egyetemben: (choice var x (list clauses))
	- ha belefut mégegyszer ebbe a klauzúrába, akkor körbeért megáll
  - Amikor változót választ, akkor osztódik (source választás)
  - Amikor a választása után több clause-ra ugorhat, szintén osztódik (target választás)
 
- Súlyozás:
  - Osztódás (split)
	- Amikor $chain$ választhat új változót, akkor a súlyát felezi (source választás)
	- Amikor egy választott változó mellett, több ágra ($id$|$neg$$part$) is mehet, akkor osztódik, súlyokat megőrzi 
    (target választás), amikor joinolás van vigyázni kell, hogy ezeket nem szabad direktben összeadni
  - Csatlakozás (join)
	- Amikor olyan klauzurára ér, amivel körbeér, akkor kivonja a saját súlyát a kört megelőző részről
	- Amikor olyan klauzurára ér, ami nem körbeérés, de már járt ott akkor csatlakozik ahhoz, ami 
	  először ott járt (elkéri tőle az infókat), de nem olvad össze vele, mivel a két lánc az eredetében
	  eltér, emiatt a körképzésben eltérőek lehetnek

## Implikációs gráf

Implikációs gráf leegyszerűsítve klauzurák és közötti implikációk:

$3-SAT \implies 2-SAT$ implikációk:

$$
(cl \ x \lor idpart_x) \land (cl \ \lnot x \lor negpart_x) \implies 
(
	(var \ x \land negpart_x) 
	\lor 
	(var \ \lnot x \land cl \ idpart_x)
)
$$

$2-SAT \implies 2-SAT$ implikációk:

$$
(cl \ x \lor y) \implies 
(
	(var \ \lnot x \implies (idpart_x \land (y \implies negpart_y))) 
	\land
	(var \ \lnot y \implies (idpart_y \land (x \implies negpart_x)))
)
$$

## TODO

A Node-ok nemcsak klauzúrák lehetnek? hanem SAT problémák is?