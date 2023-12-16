from tuomari import Tuomari
class KiviPaperiSakset:
    """Kivi-paperi-sakset peliin liittyvä luokka
    joka pitää kirjaa pelin kierroksista ja tuloksista"""
    def pelaa(self):
        """Metodi pelaa kierroksen peliä
        ja tulostaa lopuksi pelin tuloksen"""
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        """Metodi palauttaa toisen pelaajan siirron
        parametrina annetun ensimmäisen pelaajan siirron perusteella
        olettuksena vastustaja antaa aina k:n"""
        return "k"

    def _onko_ok_siirto(self, siirto):
        """Metodi tarkastaa onko parametrina annettu siirto"""
        return siirto in ["k", "p", "s"]
