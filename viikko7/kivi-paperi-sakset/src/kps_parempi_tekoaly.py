from tekoaly_parannettu import TekoalyParannettu
from KPS import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    """Kivi-paperi-sakset peliä tekoälyä vastaan"""
    def __init__(self):
        """Konstruktori, joka luo tekoälyn ja määrittää muistinkoon"""
        self.tekoaly = TekoalyParannettu(8)
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
