import argparse
import csv

def pseudo_primes(p: int, N: int, numbers_file=None, pseudo_primes_file=None):
    result = [0] * N  # Alapértelmezés szerint minden szám nem pszeudó prím
    numbers = list(range(1, N + 1))
    
    for n in range(1, N + 1):
        divisors = [i for i in range(2, n + 1) if n % i == 0]  # Osztók keresése, 1 kihagyása
        
        if all(d >= p for d in divisors):  # Ha minden osztó legalább p
            result[n-1] = 1

    if numbers_file:
        with open(numbers_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(numbers)
    
    if pseudo_primes_file:
        with open(pseudo_primes_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(result)
    
    return result

def grouped_pseudo_primes(p: int, N: int, numbers_file=None, pseudo_primes_file=None):
    M = (N + p - 1) // p * p  # Felkerekítés a legközelebbi p többszörösére
    pseudo_prime_list = pseudo_primes(p, M)  # Psz. prímek kiszámítása a módosított N-re
    matrix = [[0] * (M // p) for _ in range(p)]  # p sor és M//p oszlopos mátrix
    numbers_matrix = [[0] * (M // p) for _ in range(p)]
    
    for n in range(1, M + 1):
        row = (n % p) - 1  # Modulo p szerinti sor
        if row < 0:
            row += p            
        col = (n-1) // p  # Oszlop index
        matrix[row][col] = pseudo_prime_list[n-1]  # Érték beállítása
        numbers_matrix[row][col] = n
    
    if numbers_file:
        with open(numbers_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(numbers_matrix)
    
    if pseudo_primes_file:
        with open(pseudo_primes_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)
    
    return matrix

def main():
    parser = argparse.ArgumentParser(description="Pszeudó prímek számítása.")
    parser.add_argument("p", type=int, help="A minimális prímosztó.")
    parser.add_argument("N", type=int, help="A keresési tartomány felső határa.")
    parser.add_argument("--grouped", action="store_true", help="Csoportosított eredményt ad vissza.")
    parser.add_argument("--numbers_file", type=str, default=None, help="CSV fájl az összes szám mentéséhez.")
    parser.add_argument("--pseudo_primes_file", type=str, default=None, help="CSV fájl a pszeudó prímek mentéséhez.")
    
    args = parser.parse_args()
    
    if args.grouped:
        result = grouped_pseudo_primes(args.p, args.N, args.numbers_file, args.pseudo_primes_file)
    else:
        result = pseudo_primes(args.p, args.N, args.numbers_file, args.pseudo_primes_file)
    
    if not args.pseudo_primes_file:
        print(result)

if __name__ == "__main__":
    main()
