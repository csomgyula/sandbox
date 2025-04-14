from math import sqrt 
from conf import Conf
    
class EulerSieveMethod:    
    def __init__(self, n, conf = Conf()):
        """
        Initialize computation
                
        Abbreviation:
        - sp = small prime <= srqrt(n) aka sieve prime
        - hp = high prime  > srqrt(n)        
        - nhp = next high prime
        
        TODO nhp, inv_nhp is kinda chained list over static array, should be moved to its own class with this
        method
        """
        self.conf = conf
        
        if self.conf.debug:
            print(f"debug: euler sieve is initializing with bound {n} and {conf} @EulerSieveMethod.__init__()")
        n = int(n)
        self.primes = []
        self.sieve_prime     = 1
        self.max_sieve_prime = int(sqrt(n))
        
        # abbreviation:
        # sp = small prime <= srqrt(n)
        # hp = high prime  > srqrt(n)        
        # nhp = next high prime
        self.bound = n
        self.prime_bitmap    = [0] * n # whether it is prime (1) or not (0)
        
        # index 0 is not used in computes, we only add so we don't have to do offset magic
        # a bit more memory for more visual and less computation
        # TODO nhp and inv_nph is kinda chained list over static array, should be moved to its own class
        self.nhp             = [n+1 for n in range(0, n+1)] # each points to next
        
        # index n+1 is used to avoid overflow
        # a bit more memory for less computation
        
        # TODO nhp and inv_nph is kinda chained list over static array, should be moved to its own class
        self.inv_nhp         = [n-1 for n in range(0, n+2)] # each points to prev
        
        self.sps             = []
        self.hps             = self.__nhp_to_hps__()
    
    def __remove_from_nhp__(self, k):
        """
        remove k from prime candidates
        
        used by: sieve for removing sieved composite numbers
        call rule: it shall be called in a backward manner
        
        TODO nhp, inv_nhp is kinda chained list over static array, should be moved to its own class with this
        method
        
        idea: API which can declare such call rules 
        """
        if self.conf.debug:
            print(f"debug: removing composite, divisible by {self.sieve_prime}, {k} @EulerSieveMethod.__remove_from_nhp__()")
        if k <= self.bound:
            # next high prime of k from previous round
            nhp_k = self.nhp[k]
            
            # previously pointing to k as next high prime
            inv_nhp_k = self.inv_nhp[k]
            
            # set previously pointing to k, to point where k pointed previously
            self.nhp[inv_nhp_k] = nhp_k
            self.inv_nhp[nhp_k] = inv_nhp_k
            self.nhp[k] = '_'
        
    def __nhp_to_hps__(self):
        """        
        rebuild high primes list from next high primes chained list, that is
        it is a list persistent-view of the chained list
        
        TODO nhp, inv_nhp is kinda chained list over static array, should be moved to its own class with this
        method. Why? 
        - Because this is slow. Instead an iterator (logical view) should be used
        - Bacause for engineers next and inverse_next is less visual terminology
        
        flow rule: shall be called:
            - when sieving after new sieve prime is determined
            - when return when last sieve prime is determined
            - previous sieve removed composites from high primes chained list
            
        idea: API which can declare such rules    
        """
        if self.conf.debug:
            print(f"debug: building list of high primes candidates > {self.sieve_prime} @EulerSieveMethod.__nhp_to_hps__()")

        hps = []
        inv_nhp = self.sieve_prime
        nhp = self.nhp
        
        bound = self.bound
        while inv_nhp < bound:
            hp = self.nhp[inv_nhp]
            if hp < bound:
                hps.append(hp)
            inv_nhp = hp
            
        self.hps = hps
        if self.conf.debug:
            print(f"debug: list of high primes candidates > {self.sieve_prime}: {hps} @EulerSieveMethod.__nhp_to_hps__()")
        
        
        return hps
        
    def __next_sieve_prime__(self):
        if self.conf.debug:
            print(f"debug: previous sieve prime: {self.sieve_prime} @EulerSieveMethod.__next_sieve_prime__()")
        sieve_prime = self.nhp[self.sieve_prime]        
        if self.conf.debug:
            print(f"debug: next sieve prime {sieve_prime} @EulerSieveMethod.__next_sieve_prime__()")
        self.sieve_prime = sieve_prime  
        if sieve_prime <= self.max_sieve_prime:
            self.sps.append(sieve_prime)
        return sieve_prime
        
    def __call__(self):
        """
        Euler's sieve, see spec at:
        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Euler's_sieve
        """        
        if self.conf.debug:
            print(f"debug: euler sieve is starting @EulerSieveMethod.__call__()")
        if self.bound < 2:
           return []
        elif self.bound == 2:
           return [2]
           
        max_sieve_prime = self.max_sieve_prime   
        while self.__next_sieve_prime__() <= max_sieve_prime:
            if self.conf.debug:
                print(f"debug: sieve with prime {self.sieve_prime} @EulerSieveMethod.__call__()")
                                
            if self.conf.stdout:
                print(f"{self.nhp}")
                
            # determine numbers divisible by the sieve prime
            non_primes = [candidate * self.sieve_prime for candidate in self.hps]
            if self.conf.debug:
                print(f"debug: composite, divisible by {self.sieve_prime} to be removed: {non_primes} @EulerSieveMethod.__call__()")

            # remove non prime from next high primes chained list
            for non_prime in non_primes[::-1]:
                self.__remove_from_nhp__(non_prime)
            
            # build high primes list from next high primes chained list
            self.__nhp_to_hps__()
                            
                    
        if self.conf.stdout:
            print(f"{self.nhp}")
        # return small primes
        hps = self.hps
        sps = self.sps
        primes =  sps + hps
        
        if self.conf.debug:
            print(f"debug: primes: {primes}, sps: {sps}, hps: {hps}")
        
        self.primes = primes
        return primes

if __name__ == "__main__":   
    n = 100
    from sys import argv        
    if len(argv) > 1:
        n = int(argv[1])
    EulerSieveMethod(n, Conf(stdout = True, debug = False))()        