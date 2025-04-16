# uploads/robot1.py
import egyszam_jatekos

class EgyszamJatekos(egyszam_jatekos.EgyszamJatekos):
    def __init__(self, korok_szama):
        super().__init__(korok_szama)

    def get_szam(self, kor):
        # Itt az aktuális kör száma alapján választunk egy számot
        return 1  # Egyszerű választás: 1
