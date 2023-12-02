class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset_arvot = []

    def miinus(self, operandi):
        self.tallenna_arvo()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.tallenna_arvo()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.tallenna_arvo()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
    
    def tallenna_arvo(self):
        self._edelliset_arvot.append(self._arvo)

    def kumoa(self):
        """Kumoaa edellisen operaation."""
        edellinen_arvo = self._edelliset_arvot.pop()
        self.aseta_arvo(edellinen_arvo)

