import random

class EgyszamJatekos:
    def __init__(self, korok_szama):
        self.korok_szama = korok_szama

    def get_szam(self, kor):
        # Véletlenszerű 0 vagy 1
        return 1 + random.choice([0, 1])
