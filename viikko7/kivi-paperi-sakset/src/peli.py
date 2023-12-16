from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

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
