"""Tämä moduuli sisältää käyttöliittymän toteuttavan luokan Kayttoliittyma."""
from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    """Komento-luokka määrittelee laskimen toiminnot."""
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    """Summa-luokka määrittelee summaamisen toiminnallisuuden."""
    def __init__(self, sovelluslogiikka, lue_komento):
        """Konstruktori, joka luo summaamisen toiminnallisuuden."""
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_komento = lue_komento

    def suorita(self):
        """Suorittaa summaamisen."""
        arvo = int(self._lue_komento())
        self._sovelluslogiikka.plus(arvo)

class Erotus:
    """Erotus-luokka määrittelee erotuksen toiminnallisuuden."""
    def __init__(self, sovelluslogiikka, lue_komento):
        """Konstruktori, joka luo erotuksen toiminnallisuuden."""
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_komento = lue_komento


    def suorita(self):
        """Suorittaa erotuksen."""
        arvo = int(self._lue_komento())
        self._sovelluslogiikka.miinus(arvo)

class Nollaus:
    """Nollaus-luokka määrittelee nollaamisen toiminnallisuuden."""
    def __init__(self, sovelluslogiikka):
        """Konstruktori, joka luo nollaamisen toiminnallisuuden."""
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        """Suorittaa nollaamisen."""
        self._sovelluslogiikka.nollaa()

class Kumoa:
    """Kumoa-luokka määrittelee kumoamisen toiminnallisuuden."""
    def __init__(self, sovelluslogiikka):
        """Konstruktori, joka luo kumoamisen toiminnallisuuden."""
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        """Suorittaa kumoamisen."""
        self._sovelluslogiikka.kumoa()
        

class Kayttoliittyma:
    """Kayttoliittyma-luokka luo käyttöliittymän ja määrittelee sen toiminnallisuuden."""
    def __init__(self, sovelluslogiikka, root):
        """Konstruktori, joka luo käyttöliittymän."""
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_komento),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_komento),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: Kumoa(sovelluslogiikka)
        }

    def _lue_komento(self):
        """Palauttaa komennon syötteenä."""
        return self._syote_kentta.get()


    def kaynnista(self):
        """Käynnistää käyttöliittymän."""
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)


    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
