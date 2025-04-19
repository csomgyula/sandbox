# cube

Heurisztikus algoritmus:

## Lazán függnek

Ha bármely clause max. 1 közös változóval rendelkezik, akkor megcsinálható

1. Nulladik lépés: Választok két clause-t: $C_1, C_2$ 
2. Első lépés:
	1. Választok két változót tetszőlegesen: $var_1 \in C_1, var_2 \in C_2$
	2. Beállítom $var_1, var_2$ értékét $C_1, C_2$-nek megfelelően
2. N. lépés: 
	1. Választok két már kiválasztott változót $var_1', var_2'$ 
	2. Kiválasztom azt a clause-t, ami ezeket tartalmazza $l_1 \ var_1' \lor l_2 var_2' \ l_3 var_3$
	3. $var_3$-at $l_3$-nak megfelelőre állítom

## Erős függés

Ha lehet több közös metszet is:

1. Első lépés: Választok két clause-t: $C_1, C_2$
2. Loop az összes lehetséges változóra $(var_1, var_2) \in C_1 \times C_2$-ben`
	- Első lépés: Megfelelően beállítom $var_1, var_2$ értékét $C_1, C_2$-nek megfelelően
	- N. lépés: 
	  - Választok két már kiválasztott változót $var_1' = b_1 , var_2' = b_2$ 
	  - Kiválasztom azt a clause-t, ami ezeket tartalmazza, negálva:  
		$\lnot . b_1 \ var_1 \lor \lnot . b_2 var_2 \ l_3 var_3$
	  - $var_3$-at $l_3$-nak megfelelőre állítom
3. Megnézem, hogy van-e olyan, amit senki nem ront el:
	- Ha van, akkor az megoldás
	- Ha nincs, akkor unsat