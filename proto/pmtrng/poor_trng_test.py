import random
import hashlib
import time
import math
import sys
import argparse

MILLION = 1000 * 1000

def get_random_input():
    """Véletlenszerű bemenet generálása."""
    return random.getrandbits(64)

def hash_input(input_value):
    """Hash függvény alkalmazása a bemenetre."""
    return hashlib.sha256(str(input_value).encode()).hexdigest()

def exponential_moving_average(prev_ema, new_value, alpha=0.1):
    """Exponenciális mozgóátlag számítása."""
    return alpha * new_value + (1 - alpha) * prev_ema

def one_bit(ema, bit_pos = 2, smoothing_alpha=0.1):
    """Egyetlen véletlenszám generálása."""
    # Véletlenszerű bemenet generálása
    input_value = get_random_input()
    
    # Futás idő mérésének kezdete
    start_time = time.time()
    
    # A hash függvény végrehajtása
    hash_value = hash_input(input_value)
    
    # Futás idő maradékának kiszámítása
    residue_time = (time.time() - start_time)
    
    # EMA alkalmazása
    ema = exponential_moving_average(ema, residue_time, smoothing_alpha)
    residue_time -= ema  # Maradék számítása
    
    # Maradék hash-elése és véletlenszám generálása
    hashed_residue = hash_input(residue_time)
    random_bit = int(hashed_residue, 16) % 2  # 0 vagy 1
    #residue_time = int(MILLION * residue_time) % MILLION
    #random_bit = (residue_time >> int(bit_pos)) & 1
    return ema, random_bit

def run_trng(rounds, warmup_rounds=1000, smoothing_alpha=0.1):
    """A TRNG algoritmus futtatása."""
    ema = 0  # EMA kezdeti érték
    bits = []
    for _ in range(warmup_rounds):
        ema, _ = one_bit(ema, smoothing_alpha)  # Bemelegítés

    # Véletlenszám generálás a megadott számú körben
    for _ in range(rounds):
        ema, bit = one_bit(ema, smoothing_alpha)
        bits.append(bit)
    
    return bits

def frequency_test(bits, verbose):
    """Frequency test: Ellenőrzi, hogy a 0 és 1 arányban egyenletes-e az eloszlás."""
    count_0 = bits.count(0)
    count_1 = bits.count(1)
    
    if verbose:
        print(f"Frequency Test: 0 count = {count_0}, 1 count = {count_1}")
    return abs(count_0 - count_1) < len(bits) * 0.05  # Arányban 5%-os eltérés lehet megengedett

def runs_test(bits, verbose):
    """Runs test: Ellenőrzi, hogy túl sok egymás utáni 0 vagy 1 van-e."""
    runs = 1  # Minimum 1 futás van mindig
    for i in range(1, len(bits)):
        if bits[i] != bits[i-1]:
            runs += 1
    
    # Az optimális futás számának a következő az elvárt intervalluma:
    expected_runs = len(bits) / 2
    if verbose:
        print(f"Runs Test: {runs} runs - expected: {expected_runs} runs +- {expected_runs * 0.05}")
    
    # Ha a futások száma túllépi az elvárt értéket, akkor hibás a generált adat
    return abs(runs - expected_runs) < expected_runs * 0.05  # A túllépés mértéke max 5%-kal lehet eltérő

def chi_square_test(bits, verbose):
    """Chi-Square test: Ellenőrzi, hogy a 0 és 1 eloszlás mennyire tér el a várttól."""
    expected_count = len(bits) / 2
    count_0 = bits.count(0)
    count_1 = bits.count(1)
    
    chi_square = ((count_0 - expected_count) ** 2) / expected_count + ((count_1 - expected_count) ** 2) / expected_count
    
    if verbose:
        print(f"Chi-Square Test: χ² = {chi_square} - expected <= 3.84")
    return chi_square <= 3.84  # Optimális eredmény esetén χ² < 1.5

def test_experiment(test_round, gen_rounds, verbose):
    bits = run_trng(gen_rounds)

    # Tesztelés
    if verbose:
        print(f"\n{test_round+1}. kísérlet kezdődik...\n")
    
    # Teszteljük az egyes statisztikai teszteket
    pass_freq = frequency_test(bits, verbose)
    pass_runs = runs_test(bits, verbose)
    pass_chi_square = chi_square_test(bits, verbose)
    
    # Teszt eredmények
    if pass_freq and pass_runs and pass_chi_square:
        if verbose:
            print("A generált véletlenszámok megfelelő minőségűek:")
        return {"pass_freq": 1, "pass_runs": 1, "pass_chi_square": 1}
    else:
        if verbose:
            print("A generált véletlenszámok nem megfelelő minőségűek.")
            print(f"\tfreq test passed:       {pass_freq}")
            print(f"\truns_test passed:       {pass_runs}")
            print(f"\tchi square test passed: {pass_chi_square}")
        return {"pass_freq": pass_freq, "pass_runs": pass_runs, "pass_chi_square": pass_chi_square}
        
def main():
    # Argumentumok kezelése
    parser = argparse.ArgumentParser(description="TRNG (True Random Number Generator) teszt és éles futtatás.")
    parser.add_argument('test_rounds', type=int, help="A kísérletek száma")
    parser.add_argument('gen_rounds', type=int, help="A generált véletlenszámok száma egy kísérletben")
    parser.add_argument('-v', '--verbose', action='store_true', help="A kísérleteket részletesen kiírja (lassú)")

    parsed = parser.parse_args()
    test_rounds = parsed.test_rounds
    gen_rounds  = parsed.gen_rounds
    verbose = parsed.verbose
    
    print(f"\nTesztelés kezdődik...")
    print(f"\tteszt kísérletek száma:        {test_rounds}")
    print(f"\tgen. bitek száma per kísérlet: {gen_rounds}")
    print(f"\tverbose: {verbose}")
    
    pass_freq = 0
    pass_runs = 0
    pass_chi_square = 0
    
    for i in range(0, test_rounds):
        test_round_result = test_experiment(i, gen_rounds, verbose)
        pass_freq += test_round_result["pass_freq"]
        pass_runs += test_round_result["pass_runs"]
        pass_chi_square += test_round_result["pass_chi_square"]
    
    print(f"\nTeszt eredmény:")
    print(f"\tfreq test passed:       {pass_freq} / {test_rounds}")
    print(f"\truns_test passed:       {pass_runs} / {test_rounds}")
    print(f"\tchi square test passed: {pass_chi_square} / {test_rounds} (p-value=0.05)")
    
if __name__ == "__main__":
    main()
