from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
# Sopivan peliolion (kaksinpeli, helppo yksinpeli, vaikea yksinpeli) 
# luominen tulee toteuttaa staattisen tehdasmetodin avulla.
# staattinen tehdasmetodi on metodi, joka ei vaadi olion luomista, sitä käytetään luokan nimellä
# esim. Peli.pelaaja_vs_pelaaja(). Staattisia tehdsametodeja käytetään usein luokkien välisen riippuvuuden
# vähentämiseen. 
class Peli:

    @staticmethod
    def pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def pelaaja_vs_tekoaly():
        return KPSTekoaly()

    @staticmethod
    def pelaaja_vs_parempi_tekoaly():
        return KPSParempiTekoaly()
