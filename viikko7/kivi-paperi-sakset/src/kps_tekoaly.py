from tekoaly import Tekoaly
from KPS import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset): # peritään luokka KiviPaperiSakset
    """Kivi-paperi-sakset peliä tekoälyä vastaan"""
    def __init__(self):
        """Konstruktori, joka luo tekoälyn"""
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        """Metodi palauttaa toisen pelaajan siirron
        parametrina annetun ensimmäisen pelaajan siirron perusteella"""
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
