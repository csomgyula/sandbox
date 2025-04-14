from conf import Conf
from primes import primes

def prime_scaled_remainders(n, conf = Conf()):
    """
    scaled remainders of a number, $k$ up to N is

    $$
    ([k/p_1], k mod p_1), ([k/p_2], k mod p_2), ..., ([k/p_i], k mod p_i),... ): for all p_i < k
    $$
    
    scaled remainders up to N is the scaled remainders of numbers less N
    """
    if conf.debug:
        print(f"debug: started to compute scaled remainders < {n}, with {conf} @scaled_remainders()")
        print(f"debug: first determine primes up to {n}... @scaled_remainders()")

    primes_n = primes(n, conf)
    primes_len_n = len(primes_n)
    
    if conf.debug:
        print(f"debug: now compute scaled remainders... @scaled_remainders()")
    scaled_remainders_n = [[]] * (n-1)
    for k in range(1, n):
        scaled_remainders_k_n = [""] * primes_len_n
        for primes_index_q, q in enumerate(primes_n):
            if q < k:
                scaled_remainders_k_n[primes_index_q] = (int(k/q), k % q)
            elif q == k:
                scaled_remainders_k_n[primes_index_q] = (1, 0)
            else:
                break
        scaled_remainders_n[__scrs_index__(k)] = scaled_remainders_k_n
        
    if conf.stdout:
        print(__scaled_remainders_n_to_str__(n, primes_n, scaled_remainders_n))
        #print(scaled_remainders_n)
        
    return scaled_remainders_n

def __scaled_remainders_n_to_str__(n, primes, scaled_remainders):
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
    for k in range(n):
        scrs_k_n_row = f"\n{k}"
        for scr in scaled_remainders[__scrs_index__(k)]:
            scrs_k_n_row += f"; {scr}"
        scrs_n_rows += scrs_k_n_row
        
    return primes_n_header_row + scrs_n_rows
    
def __scrs_index__(k):
    return k-1
    
if __name__ == "__main__":    
    n = 100
    from sys import argv        
    if len(argv) > 1:
        n = int(argv[1])    
    prime_scaled_remainders(n, Conf(stdout = True, debug = False))
