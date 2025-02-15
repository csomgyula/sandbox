# Generic-Methods

## Problem split

## Eratosthenes sieve

Theorem: $Pi(N) \le RelativePrime(N,M)$

, where $RelativePrime(N, M)$ aka $EratosthenesSieve(N, M)$ is the number of numbers relative prime to all $m \le M$

Theorem: $\Pi(N) \le N \* (1-1/p_1) \* (1-1/p_2) \* ... \* (1 - 1/p_k) : p_1, p_2, ..., p_k <= M$

Theorem: $\Pi(N) \le ~ N \* e^{-(1/p_1 + 1/p_2 + ... + 1/p_k) : p_1, p_2, ..., p_k <= M}$

## Coding

## Interval split estimation

# Upper Bound (using [problem split](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm))

## Sub-Method: Sieve small-any primes (using Erathosthenes sieve)

Use Eratosthenes sieve for small primes. 

TODO: We need some formula for the reciprocals

## Sub-Method: Sieve large-only primes
The problem with the above is that the sieve can only use small numbers. Now we look into large primes as well. Outline:

* Since we already sieved small primes we just look into numbers which have only big prime dividers: $> p_k$.
* But not to big, because very big primes are again already sieved with small primes. Since: if a composite number $N$ has a prime divider $\ge N / p_k$ than it has a prime divider $\le p_k$

### Sub-Method: Large-any exponents (using Erathosthenes sieve)

Idea, large exponents cannot be frequent, for instance:

$$
N - (N / (x_1)^2 + N / (x_2)^2 +...+ N / (x_k)^2 : x_i > M) > N - (N/(M+1)^2 + N/(M+2)^2 + ... + N/(M+k)^2) 
$$

And the right side converges to zero...

### Sub-Method: Small-only exponents (using combinatorial coding)

Outline:

* We divide N into k intervals: $N_1 < N_2 < ... < N_k$
* Composite numbers have only dividers from these intervals. How much?
* Only exponents of 1 are interesting, hence:

$$
\Pi(N_2, N_1) * Binom(Pi(N_k, N_1) : N/log N_1) + \Pi(N_3, N_2) * Binom(N_k - N_2 : N / log N_2 + ... 
$$

where $\Pi(N, M)$ is the number of primes between N, M.

# Lower bound

## Using combinatorial, coding
