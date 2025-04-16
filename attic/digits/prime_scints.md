$$
\displaylines{ 
Q(2n, n)  = S(n, range(2n, n)) \\
P(2n, n)  = n - S(n, range(2n, n))
}
$$


hence:

$$
\displaylines{ 
Q(4n, 2n) = S(n, range(4n, 2n)) + P(2n,n) = S(n, range(4n, 2n)) + n - S(n, range(2n, n)) \\
P(4n, 2n) = 2n - Q(4n, 2n) = 2n - S(n, range(4n, 2n)) + S(n, range(2n, n))
}
$$

hence:

$$
P(4n, 2n) = 3n - S(n, range(4n, 2n))
$$

hence:

$$
P(4n, n)  = 3 * (n - S(n, range(4n, 2n)) / 3)
$$

hence:

$$
\displaylines{ 
P(4n, n)  = 3 * (n - S(n, range(2n, n)) + S(n, range(2n, n)) - S(n, range(4n, 2n)) / 3))\\
P(4n, n)  = 3 * (P(2n, n) + S(n, range(2n, n)) - S(n, range(4n, 2n)) / 3))\\
P(4n, n)  = 3 * (P(2n, n) + S(n, range(2n, n)) * (1 - S(n, range(4n, 2n)) / 3 * S(n, range(2n, n))))\\
}
$$

node:

|1|2 |3 |4|5 |6|7 |8 |9 |10|11|12 |13|14|15|16 |17|18 |19|20 |21 |22|23|24 |25 |26|27 |28 |29|30 |31|32 |
|-|--|--|-|--|-|--|--|--|--|--|---|--|--|--|---|--|---|--|---|---|--|--|---|---|--|---|---|--|---|--|---|
|1|2 |  |4|  | |  |8 |  |  |  |   |  |  |  |16 |  |   |  |   |   |  |  |   |   |  |   |   |  |   |  |32 |
|1|2 |3 | |5 | |7 |  |  |  |11|   |13|  |  |   |17|   |19|   |   |  |23|   |   |  |   |   |29|   |31|32 |
| |g2|  |4|  | |  |*8|  |  |  |   |  |  |  |   |  |   |  |   |   |  |  |   |   |  |   |   |  |   |  |   |
| |g2|g3| |  |6|  |8 |*9|  |  |*12|  |  |  |*16|  |   |  |   |   |  |  |   |   |  |   |   |  |   |  |   |
| |g2|g3| |g5| |g7|  |9 |10|  |12 |  |14|15|16 |  |*18|  |*20|*21|  |  |*24|*25|  |*27|*28|  |*30|  |*32|
					
nemcsak a kétszeresek jönnek be, hanem a 3x-orosok is, ami elrontja a 2-hatvány szimmetriát:				

|1|10|11|100|101|110|111|1000|1001|1010|1011|1100|1101|1110|1111|10000|10001|10010|10011|10100|10101|10110|10111|11000|11001|11010|11011|11100|11101|11110|11111|100000|
|-|-|-|-|-|-|-|-|-|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|1|10| |100| | | |1000| |  |  |  |  |  |  |10000|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |100000|

$$
Q(4n, 2n) = S(n, range(4n, 2n)) + P(2n,n) + P(4/3n, n)
$$

Ugyanakkor az S-nek lehet valami szabályossága, mármint arányosan, olyan mintha a 2x skálázás 3/2-el növelne:

$$
S(n, range(4n, 2n)) ~= 3/2 * S(n, range(2n, n))
$$

Ha ez igaz lenne, akkor:

$$
\displaylines{ 
Q(4n, 2n) = 3/2 * S(n, range(2n, n)) + P(2n,n) + P(4/3n, n)\\
Q(4n, 2n) = 3/2 * Q(2n, n) + P(2n,n) + P(4/3n, n)
}
$$

Nézzük mi van 3/2n és n között:

$$
Q(3n, 2n) = S(n, range(3n, 2n)) + P(3/2n, n)
$$

Itt már a 3-asok nem jönnek be, mert azok n alatti prímmel oszthatók

node:

$$
P(3/2n, n) = 1/2n - Q(3/2n, n) = n/2 - S(n, range(3/2n, n)) 
$$

azaz:

$$
Q(3n, 2n) = S(n, range(3n, 2n)) + 1/2n - S(n, range(3/2n, n)) 
$$

azaz:

$$
\displaylines{ 
P(3n, 2n) = n - S(n, range(3n, 2n)) - 1/2n + S(n, range(3/2n, n))\\
P(3n, 2n) = n/2 - S(n, range(3n, 2n)) + S(n, range(3/2n, n))
}
$$

azaz:

$$
\displaylines{ 
P(3n, 2n) + P(3/2n, n) = n/2 - S(n, range(3n, 2n)) + S(n, range(3/2n, n)) + 1/2n - S(n, range(3/2n, n))\\
P(3n, 2n) + P(3/2n, n) = n - S(n, range(3n, 2n))
}
$$

ha igaz a sejtés, akkor:

$$
\displaylines{ 
P(3n, 2n) + P(3/2n, n) = n - 3/2 * S(n, range(3/2n, n))\\
P(3n, 2n) + P(3/2n, n) = n/4 + 3/4n - 3/2 * S(n, range(3/2n, n))\\
P(3n, 2n) + P(3/2n, n) = n/4 + 3/2 * P(3/2n, n)\\
P(3n, 2n)              = n/4 + 1/2 * P(3/2n, n)\\
}
$$

ami nem lehet, mivel azt jelentené (a rekurzív adódó mértani sort összegezve), hogy $3n$ és $2n$ között $n/3$ prím van, ami nem lehet mert itt kb. $n/logn$ prím van, azaz valszeg egyre jobban nő a hányad, ahogy... jönnek be új prímek?

Sejtés: Össszetett számok $n$-ig $Q(n)$ plusz a gyök n alatti prímek annyi, mint az összetett számok útjának, $path(i)$ összege $n/2$ és $n$ között. Egy összetett szám útja ahány féle kombinációja van a primtényezős felírásának, megszorítva arra, hogy két szomszédos prím eltérő kell legyen. Pl. 

$$
path(12) = |[ 4 * 3, 2 * 3 * 2, 3 * 4 ]| = 3
$$

Vázlatos bizonyítás: 

- először megszámolom az összetett számokat aszerint, hogy mi a legkisebb prímosztó: $prime(p_i, n) = | {p_i}^{k_i} * {p_{i+1}}^{k_{i+1}} * ... * {p_{i+j}}^{k_{i+j}} \leq n \land \forall j:\ p_{i+j} \leq \sqrt n |$
- sejtés: $prime(p_{i+1}, n) = prime(p_i, n / (p_{i+1} / p_i))$
- 2D Knapsack: az első dimenzió az n, a második, hogy mekkora a legkisebb prímosztója p, a Knapscak az, hogy hány olyan szám van n-ig, aminek a legkisebb primosztója legalább p
- sejtés: végigkövetem az utat a Knapsacken, amíg eljut 1-be, minden út egy összetett szám patha

A Csebiseb tételhez azt kell megbecsülni, hogy milyen gyakori olyan szám, aminek kicsi a path-a
