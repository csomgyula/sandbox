# cube

Heurisztikus algoritmus:

## Jelölések

- $C, C_1, C_2$: klauzúrák
- $var, var_1, var_2$: változók
- $lg, lg_1, lg_2$: logika unáris függvény változó ($identiy, \lnot$)
- $bool, bool_1, bool_2$: logikai értékek ($True, False$)
- $lg \circ bool$: operátor, ami logikai unáris függvényt és logikai értéket visz logikai függvénybe:

| $lg$     | $bool$    | $lg \circ bool$ |
|------------|---------|-----------------|
| $identity$ | $True$  | $identity$      |
| $identity$ | $False$ | $\lnot$         |
| $\lnot$    | $True$  | $\lnot$         |
| $\lnot$    | $False$ | $identity$      |


## Lazán függnek

Ha bármely clause max. 1 közös változóval rendelkezik, akkor megcsinálható

1. Nulladik lépés: Választok két clause-t: $C_1, C_2$ 
2. Első lépés:
	1. Választok két változót tetszőlegesen: $var_1 \in C_1, var_2 \in C_2$
	2. Beállítom $var_1, var_2$ értékét $C_1, C_2$-nek megfelelően
2. N. lépés: 
	1. Választok két már kiválasztott változót, ami párban még nem volt választva: $var_1', var_2'$
		1. feljegyzem a pár-választást
	2. Kiválasztom azt a clause-t, ami ezeket tartalmazza $lg_1 \ var_1' \lor lg_2 var_2' \lor \ lg_3 var_3$
	3. $var_3$-at $lg_3$-nak megfelelőre állítom

## Erős függés

Ha lehet több közös metszet is:

1. Első lépés: Választok két clause-t: $C_1, C_2$
2. Loop az összes lehetséges változóra $(var_1, var_2) \in C_1 \times C_2$-ben`
	1. Első lépés: Megfelelően beállítom $var_1, var_2$ értékét $C_1, C_2$-nek megfelelően
	2. N. lépés: 
		1. Választok két már kiválasztott (bound) változót, ami párban még nem volt választva:  
			$var_1' = bool_1 , var_2' = bool_2$
			1. feljegyzem a pár-választást
		2. Kiválasztom azt a clause-t, ami ezeket tartalmazza, negálva:  
		   $\lnot \circ bool_1 \ var_1 \lor \lnot \circ bool_2 var_2 \lor \ l_3 var_3$
		3. Ha nincs ilyen, akkor folytatom az N+1. lépéssel
		4. $var_3$-at $l_3$-nak megfelelőre állítom
3. Megnézem, hogy van-e olyan, amit senki nem ront el:
	1. Ha van, akkor az megoldás
	2. Ha nincs, akkor unsat
	