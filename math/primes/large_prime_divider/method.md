We can start to count when it is known that `p` is prime. It is known that `p` is prime if it is 
not sieved by primes less than `sqrt(p)`. So Euler method must finish before we can start counting.
We have to restart the Euler method unless we remember why a number was removed.

Originally we use this to remove composites

```
	non_primes = [candidate * self.sieve_prime for candidate in self.hps]
    for non_prime in non_primes[::-1]:
		self.__remove_from_nhp__(non_prime)
```

instead we can do something like this:

```
    for candidate in self.hps[::-1]:
		self.__remove_from_nhp__(candidate, self.sieve_prime)
```

Then we know, hence we can remember, during removal, that that the composite was `candidate * self.sieve_prime`. 
Then later when we find out that `candidate` was prime we can then count. 

This however is not enough because it only counts composites with primes on first power.

```
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
  2,  4,  6,  8,  10,   12,   14,   16,   18,   20,   22,   24
                  -                             -
```

here both 5x2 and `10x2` removed, but we do not see that `10 = 5x2`

We can change Euler method as follows:

sieve = 2

```
2 -> 2*2 -> 2*2*2 -> 2*2*2*2 -- times * 2, remove, times * 2
                             -- next non removed 
3 -> 3*2 -> 3*2*2 -> 3*2*2*2 -- times * 2, remove, times * 2
                             -- next non removed 
5 -> 5*2 -> 5*2*2 -> 5*2*2*2 -- times * 2, remove, times * 2
```

this will remove 2 powers, then odd times 2 powers. 

Count of removed numbers:

```
i. relative prime to 2 times log_2 n / i. relative prime to 2
```

sieve = 3

```
3 -> 3*3 -> 3*3*3 -> 3*3*2*3 -- times * 3, remove, times * 3
                             -- next non removed 
5 -> 5*3 -> 5*3*3 -> 5*3*3*3 -- times * 3, remove, times * 3
```

this will remove 3 powers, then relative prime to 2,3 times 3 powers

Count of removed numbers:

```
i. relative prime to 2,3 times log_3 n / i. relative prime to 2, 3
```

can we gain an upper bound for the longest gap between relative primes to p_1, p_2, ..., p_k (and some 
of them are primes) in recursive manner???

When removing during the next seed how many neighbours can you remove...???

Let the sieve prime be 5. Can two neighbours relative prime to 2,3 be divisible by 5?

```
_,1,_,_,_,5,_
```
Let the sieve prime be 7.  Can two neighbours relative prime to 2,3,5 be divisible by 7?

```
_, 1,_,_,_,_,_, 0,_,_,_,  4,_,  6,_,_,_,  3,_,  5,_,_,_,  2,_,_,_,_,_,  1
_, 1,_,_,_,_,_, 7,_,_,_,  0,_,  2,_,_,_,  6,_,  8,_,_,_, 12,_,_,_,_,_,  7
_, 1,_,_,_,_,_, 7,_,_,_, 11,_,  0,_,_,_,  4,_,  6,_,_,_, 10,_,_,_,_,_,  3
_, 1,_,_,_,_,_, 7,_,_,_, 11,_, 13,_,_,_,  0,_,  2,_,_,_,  6,_,_,_,_,_, 12
_, 1,_,_,_,_,_, 7,_,_,_, 11,_, 13,_,_,_, 17,_,  0,_,_,_,  4,_,_,_,_,_, 10
_, 1,_,_,_,_,_, 7,_,_,_, 11,_, 13,_,_,_, 17,_, 19,_,_,_,  0,_,_,_,_,_,  6
---------------------------------------------------------------------------
_, 1,_,_,_,_,_, 7,_,_,_, 11,_, 13,_,_,_, 17,_, 19,_,_,_, 23,_,_,_,_,_, 29,
_,31,_,_,_,_,_,37,_,_,_, 41,_, 43,_,_,_, 47,_, 49,_,_,_, 53,_,_,_,_,_, 59,
_,61,_,_,_,_,_,67,_,_,_, 71,_, 73,_,_,_, 77,_, 79,_,_,_, 83,_,_,_,_,_, 89,
_,91,_,_,_,_,_,97,_,_,_,101,_,103,_,_,_,107,_,109,_,_,_,113,_,_,_,_,_,119,
```
