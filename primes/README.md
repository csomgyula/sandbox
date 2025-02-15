# Generic-Methods

## Problem split

* https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm

## Eratosthenes sieve

* https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Theorem: $Pi(N) \le RelativePrime(N,M)$

, where $RelativePrime(N, M)$ aka $EratosthenesSieve(N, M)$ is the number of numbers relative prime to all $m \le M$

Theorem: $\Pi(N) \le N \* (1-1/p_1) \* (1-1/p_2) \* ... \* (1 - 1/p_k) : p_1, p_2, ..., p_k <= M$

Theorem: $\Pi(N) \le ~ N \* e^{-(1/p_1 + 1/p_2 + ... + 1/p_k) : p_1, p_2, ..., p_k <= M}$

## Coding

## Interval split estimation

* This is a heuristic typically usable for estimatating aggregations (such as e.g. count, sum). Lets say we want a quick elementary method to estimate the reciprocials:

$$
1/1 + 1/2 + 1/3 ... + 1/n
$$

We split the numbers into log N intervals 1, 2, 4, ..., 2^k where k = log n. We can quickly estimate reciprocials within interval with their bounds. Hence we get:

$$
1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + ... + 1/n \le 1/1 + (1/2 + 1/2) + (1/4 + 1/4 + 1/4 + 1/4)
$$

And that we can simplify:

$$
1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + ... + 1/n \le 1/1 + 2 * 1/2 + 4 * 1/4 + ... ~= log N
$$

Similarly for lower bound:

$$
1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + ... + 1/n \ge 1/1 + 1/2 + (1/4 + 1/4) + (1/8 + 1/8 + 1/8 + 1/8) ~= 1 + 1/2 * log N
$$

# Upper Bound (using problem split)

## Sub-Method: Sieve small-any primes (using Erathosthenes sieve)

Use Eratosthenes sieve for small primes. 

TODO: We need some formula for the reciprocals

## Sub-Method: Sieve large-only primes
The problem with the above is that the sieve can only use small numbers. Now we look into large primes as well. Outline:

* Since we already sieved small primes we just look into numbers which have only big prime dividers: $> p_k$.
* But not too  big, because very big primes are again already sieved with small primes. Since: if a composite number $N$ has a prime divider $\ge N / p_k$ than it has a prime divider $\le p_k$

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

# Idea

Instead of exponential we use faster

- $2, 2\*3, 2\*3\*5, 2\*3\*5\*7, 2\*3\*5\*7$
- goal: ow many primes between $[11, 2*3*5*7]$ in order to approximate primes not greater than $2*3*5*711$
  - same as primes in $(7, 2*3*5*7]$
- conjecture: it can bet that $7, 7 * 2, 7 * 2*3, 7 * 2*3*5$ behaves similarly as $2, 2*3, 2*3*5, 2*3*5*7$ ??? in what sense???

## Using combinatorial, coding
