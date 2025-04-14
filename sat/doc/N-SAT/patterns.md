## Példa

Példa 3 változóra: 

baloldalt a sat-2 kikötés, jobboldalt az esetek, amit kizár:

```
 a b *		~a~b *	~a~b c
					~a~b~c
~a * c		 a *~c	 a b~c
					 a~b~c
 *~b~c		 * b c   a b c
					~a b c
```
					
-> patternek, amik osztoznak változón, de nem osztoznak az "alakon", azok 3/4-edelnek

ha k változóra van ilyen p pattern, akkor az kivesz $p * 1/4 * 2^k$ kombinációt

## Sejtés

sejtés: ha $k > 2^k - p * 1/4 * 2^k$, akkor egy változó elhagyható v. üres, azaz, ha		
$p * 1/4 * 2^k > 2^k - k \implies p > 4 - 4k/2^k$

Vagyis már 4 ilyen patter elég?!


- példa 2 változóra: $2 >  4 - p * 1/4 *  4 =  4 - p     \implies p     > 2$
- példa 3 változóra: $3 >  8 - p * 1/4 *  8 =  8 - p * 2 \implies p * 2 > 5 \implies p> 2,5$
- példa 4 változóra: $4 > 16 - p * 1/4 * 16 = 16 - p * 4 \implies p * 4 > 12 \implies p>3$
- példa 5 változóra: $5 > 32 - p * 1/4 * 32 = 32 - p * 8 \implies p * 8 > 27  \implies p > 3,3$

## Példa

baloldalt a sat-2 kikötés, jobboldalt az esetek, amit kizár:

```
 a b 			~a~b * *	 
~a     d		 a * *~d
  ~b c           * b~c *
    ~c~d         * * c d
```
Ezt két kombináció elégíti ki:

```
 a~b~c d
~a b c~d
```

Hol a hiba az okoskodásban? A `*`-okban: `~a~b * *` és `* * c d` által kizárt esetek nem diszjunktak. 

Az okoskodás csak akkor érvényes, ha a kikötések (kizárások) diszjunktak, amihez az kell, hogy a változók 
száma k/2-nél nagyobb legyen. Viszont akkor a kizárások száma is kevesebb:

Például ha k páros, azaz $k = 2 * l$ akkor $l + 1$ változó kell, ami csak $2^l - 1$-et zár ki. Ez esetben
az egyenlőtlenség így alakul:

$k > 4^l - p * 2^l - 1 \implies p * 2^l > 4^l - k \implies p > 2^l - k/2^l$

azaz ekkor már exponenciálisan sok ilyen pattern kell.
