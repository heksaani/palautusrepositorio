from tuomari import Tuomari
# koska Pääohjelmalla ei saa olla riippuvuuksia konkreettisiin pelin toteuttaviin luokkiin
# on ne toeutettava rajapinnan kautta ( eli luokkan Peli avulla) 
class KiviPaperiSakset:
    """Kivi-paperi-sakset peliin liittyvä luokka
    joka pitää kirjaa pelin kierroksista ja tuloksista"""
    def pelaa(self):
        """Metodi pelaa kierroksen peliä
        ja tulostaa lopuksi pelin tuloksen"""
        #pelaa-metodi tulee toteuttaa template-metodina
        # template metodi kutsuu abstrakteja metodeja _ensimmaisen_siirto ja _toisen_siirto 
        # ja tarkastaa niiden palauttamat siirrot
        # sekä kutsuu metodia kirjaa_siirto tuomarin olion avulla
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
