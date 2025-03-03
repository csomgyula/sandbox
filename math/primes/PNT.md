$$
N \approx (\Pi(N)-\Pi(\sqrt N)) + (\Pi(N/2)-\Pi(\sqrt N)) + (\Pi(N/3)-\Pi(\sqrt N)) + ... + \Pi(1 + \sqrt N) - \Pi(\sqrt N)) + Q(\sqrt N)
$$

Or simplified:

$$
N \approx \Pi(N) + \Pi(N/2) + \Pi(N/3) + ... + \Pi(1 + \sqrt N) - \sqrt N * \Pi(\sqrt N)) + Q(\sqrt N)
$$

where 
* $Q(M)$ is counting each number which is not greater than $M^2$ but its every prime divider is less than $M$
* $\approx$ means kinda +- epsilon - the exact equoation depends on the integer part of $\sqrt N$

Proof: Let $Q\*$ be the opposite of Q then double count $Q\*$.
