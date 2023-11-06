import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )


    def test_playername_correct(self):
        # tällä testillä varmistetaan, että StatisticsService-luokan search-metodi palauttaa oikean pelaajan
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_playername_none(self):
        # tämän testin tarkoitus on testata tilannetta, jossa pelaajaa ei löydy
        player = self.stats.search("Selanne")
        self.assertEqual(player, None)

    def test_team(self):
        # testataan, että ohjelma osaa määritellä oikein joukkueen pelaajat
        # eli testataaan tema()-metodin toimintaa
        team = self.stats.team("EDM") # joukkueen nimi on "EDM" ja sillä on kolme pelaajaa
        self.assertEqual(len(team), 3) # testataan, että joukkueen pelaajia on kolme

    
    def test_top(self):
        # testataan top()-metodin toimintaa
        # eli testataan, että top()-metodi palauttaa oikean määrän pelaajia
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)



    
