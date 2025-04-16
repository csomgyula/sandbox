# egyszam_jatek.py
import os
import importlib.util

class EgyszamJatek:
    def __init__(self, korok_szama, jatekos_konyvtar="uploads"):
        """
        A játék inicializálása.
        :param korok_szama: A játék körök száma.
        :param jatekos_konyvtar: A könyvtár, ahol a robotok találhatóak.
        """
        self.korok_szama = korok_szama
        self.jatekosok = self.load_jatekosok(jatekos_konyvtar)

    def load_jatekosok(self, jatekos_konyvtar):
        """
        Betölti a robotokat a megadott könyvtárból.
        :param jatekos_konyvtar: A könyvtár, ahol a robotok találhatóak.
        :return: A robotok listája.
        """
        jatekosok = []
        for file in os.listdir(jatekos_konyvtar):
            if file.endswith(".py"):
                # Robot importálása
                module_name = file[:-3]  # eltávolítjuk a ".py" kiterjesztést
                module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(jatekos_konyvtar, file))
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
                
                try:
                    # Robot példányosítása
                    jatekos = module.EgyszamJatekos(self.korok_szama)
                    jatekosok.append(jatekos)
                except AttributeError:
                    print(f"Hiba: A {file} modul nem tartalmazza az EgyszamJatekos osztályt.")
        
        return jatekosok

    def szamok_bekerese(self, kor):
        """
        Bekéri az összes játékostól az aktuális kör választásait.
        :param kor: Az aktuális játék kör száma.
        :return: A játékosok választásai (lista).
        """
        szamok = []
        for jatekos in self.jatekosok:
            szam = jatekos.get_szam(kor)
            szamok.append(szam)
        return szamok

    def kiertékelés(self, szamok):
        """
        Kiértékeli az adott kört a szabályok szerint.
        :param szamok: A játékosok választásai.
        :return: A nyertes játékos.
        """
        # Számok előkészítése: egyediek és azok előfordulásának száma
        szam_count = {}
        for szam in szamok:
            szam_count[szam] = szam_count.get(szam, 0) + 1
        
        # A legkisebb egyedi számot választja a nyertes
        nyertes = None
        for i, szam in enumerate(szamok):
            if szam_count[szam] == 1:  # Egyedülálló szám
                if nyertes is None or szam < szamok[nyertes]:
                    nyertes = i
        
        return nyertes

    def main(self):
        """
        A játék fő futtatója.
        """
        print(f"Körök száma: {self.korok_szama}")
        print("Játékosok:")
        for idx, jatekos in enumerate(self.jatekosok, start=1):
            print(f"    {idx}. {jatekos.__module__}")
            
        for kor in range(self.korok_szama):
            print(f"\n{kor + 1}. kör:")
            szamok = self.szamok_bekerese(kor)
            print(f"Játékosok választásai: {szamok}")
            
            nyertes = self.kiertékelés(szamok)
            if nyertes is not None:
                print(f"A {nyertes + 1}. játékos nyert ezen a körön!")
            else:
                print("Nincs nyertes ezen a körön.")

class ParhuzamosEgyszamJatek:
    def __init__(self, korok_szama, trng_robotok, jatekos_robotok):
        self.korok_szama = korok_szama
        self.trng_robotok = trng_robotok
        self.jatekos_robotok = jatekos_robotok
        self.eredmenyek = []  # Minden kör összes eredménye

    def run(self):
        for kor in range(1, self.korok_szama + 1):
            kor_eredmenyek = []

            # Minden TRNG generál egy számot
            trng_szamok = [trng.get_szam(kor) for trng in self.trng_robotok]

            # Minden játékos kapja a hozzá tartozó TRNG számot, ugyanabban a sorrendben
            for idx, jatekos in enumerate(self.jatekos_robotok):
                jatekos_szam = jatekos.get_szam(kor)
                trng_szam = trng_szamok[idx]
                kulonbseg = abs(jatekos_szam - trng_szam)

                kor_eredmenyek.append({
                    'kor': kor,
                    'jatekos': jatekos.__module__,
                    'jatekos_szam': jatekos_szam,
                    'trng_szam': trng_szam,
                    'kulonbseg': kulonbseg
                })

            self.eredmenyek.append(kor_eredmenyek)

    def vegso_eredmeny(self):
        osszesites = []
        for idx, jatekos in enumerate(self.jatekos_robotok):
            jatekos_nev = jatekos.__module__
            ossz_kulonbseg = sum(kor[idx]['kulonbseg'] for kor in self.eredmenyek)
            trng_ossz_kulonbseg = sum(
                abs(kor[idx]['trng_szam'] - kor[idx]['trng_szam'])  # always 0, can be updated if needed
                for kor in self.eredmenyek
            )
            gyoztes = "Játékos" if ossz_kulonbseg < trng_ossz_kulonbseg else "TRNG"
            osszesites.append({
                'jatekos': jatekos_nev,
                'jatekos_ossz': ossz_kulonbseg,
                'trng_ossz': trng_ossz_kulonbseg,
                'gyoztes': gyoztes
            })
        return osszesites
