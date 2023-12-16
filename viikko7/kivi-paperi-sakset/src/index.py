from peli import Peli
from KPS import KiviPaperiSakset


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in ["a", "b", "c"]:
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        if vastaus.endswith("a"):
            peli = Peli.pelaaja_vs_pelaaja()
            peli.pelaa()
        elif vastaus.endswith("b"):
            peli = Peli.pelaaja_vs_tekoaly()
            peli.pelaa()
        elif vastaus.endswith("c"):
            peli = Peli.pelaaja_vs_parempi_tekoaly()
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
