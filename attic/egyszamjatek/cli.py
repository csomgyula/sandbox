import sys
from egyszam_jatek import EgyszamJatek

def main():
    if len(sys.argv) < 2:
        print("Hiba: A körök számát meg kell adni!")
        sys.exit(1)

    korok_szama = int(sys.argv[1])
    jatekos_konyvtar = sys.argv[2] if len(sys.argv) > 2 else "uploads"

    jatek = EgyszamJatek(korok_szama, jatekos_konyvtar)
    jatek.main()

if __name__ == "__main__":
    main()
