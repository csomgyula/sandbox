# egyszam_jatekos.py

class EgyszamJatekos:
    def __init__(self, korok_szama):
        """
        Játékos alapértelmezett osztálya, amelyet minden robot kiterjeszt.
        :param korok_szama: A játék körök száma
        """
        self.korok_szama = korok_szama

    def get_szam(self, kor):
        """
        Absztrakt metódus, amit a robotoknak implementálniuk kell.
        :param kor: Az aktuális játék kör száma
        :return: A robot választása (szám)
        """
        raise NotImplementedError("A get_szam metódust implementálni kell a robotoknak.")
