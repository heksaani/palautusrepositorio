from KPS import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        toinen_siirto = input("Toisen pelaajan siirto: ")
        return toinen_siirto
        
