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

$$
\displaylines{ 
1 2 	4 		  8 			 			16													32\\
1  2 3	    5   7		   11    13	 			16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31\\
		  4   6     8 9 10    12  	14 15\\
					8 9       12				16    18    20 21       24 25    27 28    30\\
						10			14 15!						  22          26\\
}
$$						
nemcsak a kétszeresek jönnek be, hanem a 3x-orosok is, ami elrontja a 2-hatvány szimmetriát:				

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
