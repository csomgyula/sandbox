from conf import Conf
from primes import primes

def prime_scaled_remainders(n, conf = Conf()):
    """
    scaled remainders of a prime, $p$ up to N is

    $$
    ([p/p_1], p mod p_1), ([p/p_2], p mod p_2), ..., ([p/p_i], p mod p_i),... ): for all p_i < p
    $$

    union

    $$
    ((0, p), (0, p), ..., (0, p),...): for all p < p_i < N
    $$
    
    scaled remainders up to N is the scaled remainders of primes less N
    """
    if conf.debug:
        print(f"debug: started to compute scaled remainders < {n}, with {conf} @scaled_remainders()")
        print(f"debug: first determine primes up to {n}... @scaled_remainders()")

    primes_n = primes(n, conf)
    primes_len_n = len(primes_n)
    
    if conf.debug:
        print(f"debug: now compute scaled remainders... @scaled_remainders()")
    scaled_remainders_n = [[]] * primes_len_n
    for i, p in enumerate(primes_n):
        scaled_remainders_p_n = [(0,p)] * primes_len_n
        for j, q in enumerate(primes_n):
            if q < p:
                scaled_remainders_p_n[j] = (int(p/q), p % q)
            elif q == p:
                scaled_remainders_p_n[j] = (1, 0)
            else:
                break
        scaled_remainders_n[i] = scaled_remainders_p_n
        
    if conf.stdout:
        print(__scaled_remainders_n_to_str__(primes_n, scaled_remainders_n))
        #print(scaled_remainders_n)
        
    return scaled_remainders_n

def __scaled_remainders_n_to_str__(primes, scaled_remainders):
    """
    Convert scaled remainders matrix to csv for simplicity
    
    Problems to solve: make it a yield, to not exhaust memory
    """
    # first row
    primes_n_header_row = ""
    for p in primes:
        primes_n_header_row += f"; {p}"
        
    # next rows
    scrs_n_rows = ""
    for i_p, p in enumerate(primes):
        scrs_p_n_row = f"\n{p}"
        for scr in scaled_remainders[i_p]:
            scrs_p_n_row += f"; {scr}"
        scrs_n_rows += scrs_p_n_row
        
    return primes_n_header_row + scrs_n_rows
    
if __name__ == "__main__":    
    n = 100
    from sys import argv        
    if len(argv) > 1:
        n = int(argv[1])    
    prime_scaled_remainders(n, Conf(stdout = True, debug = False))
