# Két-változó módszere

## Implikációk[2->1]

1. Veszek 2 változót (x,y), annak 4 lehetséges behelyettesítési értékét
   Ezeket nézem 4 szálon (x,y), (~x, y), (x, ~y), (~x, ~y)
2. Minden szálon (lx, ly) megnézem az 1-eseket, 2-eseket - ha van - amiket nem elégít ki, azokat a kombinációkat eldobom
3. Minden szálon (lx, ly) megnézem azokat a 3-asokat, amikben ezek hamisak, azaz a harmadik változó (z) kell ezt kielégítse, ami tehát egy implikáció (lx, ly) -> z
   Példa: szál = (~x, y), ESAT-3 = (x, ~y, ~z), akkor: (~x, y) => ~z 
4. Így minden szálon előálltak implikációk, illetve azon a szálon, konkrét értékek egyéb változókra
   ha azon szálon több, mint két implikáció van, akkor goto 3. minden párossal
5. Ha végignéztem az összes szálat, akkor előálltat az adott szálon az összes közvetlen vagy közvetett implikáció,
   ha ezek diszjunktak a változókra, kész vagyok, divide and conquer

## Implikációk[2->1]-rekurzió

6. Ha az implikációk nem diszjunktak a változókra, annak több esete lehetséges
   1. mindegyik szálnak van közös metszete és
		1. legalább 2 elemű, akkor folytatom a 2-Implikációkkal
		2. TODO: Marad itt az eset, amikor egy közös metszetben csak egy elem van, az TODO
   2. a közös metszettel rendelkező szálak partíciót alkotnak (a fenti ennek speciális esete) akkor ugyanazt csinálom
7. TODO: Marad itt az eset, amikor a közös metszettel rendelkező szálak nem alkotnak partíciót egymásba metszenek

## TODO

8. Fentiek közül: 6.2, 7
9. Változó substitution módszere, amikor pár változóval ki tudok fejezni egy adott változót, akkor oda behelyettesíthetek, kérdés itt hány új szabály jön létre:

## Behelyettesítés[2->1]

Példa:

- (x, y) => ~z
- (x, ~y) => z
- (~x, ) => z

Ez tehát így írható le:

- (x and y and ~z) or (x and ~y and z) or (~x and z)
  
És akkor például az (u or v or z) (közvetlen) behelyettesítéssel átírható így:

- (u or v or z) <=> (u or v ~(x and y) or (x and ~y) or ~x) <=>  
- (u or v or z) <=> (u or v ~x or ~y   or (x and ~y) or ~x) <=>  
- (u or v or z) <=> (u or v ~x or ~y   or  x         or ~x) and  
                    (u or v ~x or ~y   or        ~y  or ~x)
- (u or v or z) <=> TAUTOLOGY and   
                    (u or v ~x or ~y)

Ötlet: a közös metszetben behelyettesítek a fenti szerint. Azaz az Implikációk[2->1]-rekurzió helyett a Behelyettesítés[2->1] heurisztikát alkalmazom.