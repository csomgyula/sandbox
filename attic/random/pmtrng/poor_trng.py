import random
import hashlib
import time
import sys

# PRNG alapú véletlenszám generálás
def get_random_input():
    return random.getrandbits(64)  # 64 bites véletlen szám

# Hash generálás
def hash_input(input_value):
    # Hasheljük a bemenetet SHA-256-tal
    return hashlib.sha256(str(input_value).encode()).hexdigest()

# Exponenciális mozgóátlag (EMA) alkalmazása
def exponential_moving_average(prev_ema, new_value, alpha=0.1):
    return alpha * new_value + (1 - alpha) * prev_ema

# A TRNG fő algoritmusának implementálása
def run_trng(rounds, warmup_rounds=1000, smoothing_alpha=0.1):
    # Inicializáljuk az EMA-t a kezdő értékkel
    ema = 0
    
    # Bemelegítés: gyűjtjük az időket, de nem generálunk véletlen számokat
    for _ in range(warmup_rounds):
        ema, _ = one_bit(ema, smoothing_alpha)
        
    # Tényleges generálás    
    for _ in range(rounds):
        ema, bit = one_bit(ema, smoothing_alpha)
        
        print(bit, end="")

# A TRNG core algoritmusának implementálása
def one_bit(ema, smoothing_alpha=0.1):
    # Véletlenszerű bemenet generálása
    input_value = get_random_input()
    
    # A futás idejének mérésére
    start_time = time.time()
    
    # A hash függvény végrehajtása
    hash_value = hash_input(input_value)
    
    # A futás idő mérésének maradéka (ms)
    residue_time = (time.time() - start_time)
    ema = exponential_moving_average(ema, residue_time, smoothing_alpha)
    residue_time = residue_time - ema # maradék
    hashed_residue = hash_input(residue_time)
    random_bit = int(hashed_residue, 16) % 2  # 0 vagy 1
    
    return ema, random_bit

if __name__ == "__main__":
    # Parancssori argumentumok kezelése
    if len(sys.argv) != 2:
        print("Használat: python poor_trng.py <rounds>")
        sys.exit(1)

    # Beállítjuk a kört, amit a felhasználó megadott
    rounds = int(sys.argv[1])
    
    # Futtatjuk a TRNG-t
    run_trng(rounds)
