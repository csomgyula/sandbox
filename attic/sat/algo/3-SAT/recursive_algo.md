# Rekurzív algoritmus

Rekurzív algoritmus a 3-SAT problémára


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
3. N. lépés: 
	1. Választok két már kiválasztott (bound) változót, ami párban még nem volt választva:  
	   $var_1', var_2'$
		1. feljegyzem a párválasztást
	2. Kiválasztom azt a clause-t, ami ezeket tartalmazza: 
	   $lg_1 \ var_1' \lor lg_2 var_2' \lor \ lg_3 var_3$
	    1. Ha nincs ilyen, folytatom az N+1 lépéssel
		2. Ha van, akkor feljegyzem a klauzúrát a párhoz
	3. $var_3$-at $lg_3$-nak megfelelőre állítom és feljegyzem a bound változót
4.	A feljegyzett bound változók (sejtésem szerint): 
	1. megoldások a feljegyzett clause-okra és 
	2. nem mondanak ellent a többi nem feljegyzett clause-nak, azaz:
	3. az teljes megoldás ha minden clause-t feljegyeztem
	4. részleges megoldás, ha van fel nem jegyzett, ez esetben folytatom a többi clause-al 
	   (goto Nulladik lépés)

## Erős függés

Ha lehet több közös metszet is:

1. Nulladik lépés: Választok két clause-t: $C_1, C_2$
2. Loop az összes lehetséges változóra $(var_1, var_2) \in C_1 \times C_2$-ben`
	1. Első lépés: Megfelelően beállítom $var_1, var_2$ értékét $C_1, C_2$-nek megfelelően
	2. N. lépés: 
		1. Választok két már kiválasztott (bound) változót, ami párban még nem volt választva:  
			$var_1' = bool_1 , var_2' = bool_2$
			1. feljegyzem a párválasztást
		2. Kiválasztom azt a clause-t, ami ezeket tartalmazza, negálva:  
		   $\lnot \circ bool_1 \ var_1 \lor \lnot \circ bool_2 var_2 \lor \ l_3 var_3$
			1. Ha nincs ilyen, akkor folytatom az N+1. lépéssel
			2. Ha van, akkor feljegyzem a klauzúrát a párhoz
		3. $var_3$-at $l_3$-nak megfelelőre állítom
3. Megnézem, hogy van-e olyan, amit senki nem ront el:
	1. Ha nincs, akkor  (sejtésem szerint) unsat
	2. Ha van, akkor (sejtésem szerint)
		1. az teljes megoldás ha minden clause-t feljegyeztem
		2. részleges megoldás, ha van fel nem jegyzett, ez esetben folytatom a többi clause-al 
		   (goto Nulladik lépés)
	
## Diszkusszió

- A kát eset két okból van külön választva:
	- Az első sejtés az, hogy laza függés esetén mindig megoldható a 3-SAT
	- Az erre született sejtetten (nem bizonyítottan) megfelelő algoritmus lett kiterjesztve 
	  az általános esetree