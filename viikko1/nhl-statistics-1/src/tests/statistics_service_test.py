import unittest
from statistics_service import StatisticsService, SortBy
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

    def test_team_count(self):
        # testataan, että ohjelma osaa määritellä oikein joukkueen pelaajat
        # eli testataaan team()-metodin toimintaa
        team = self.stats.team("EDM") # joukkueen nimi on "EDM" ja sillä on kolme pelaajaa
        self.assertEqual(len(team), 3) # testataan, että joukkueen pelaajia on kolme

    def test_team_correct_players(self):
        # testataan, että joukkueen pelaajat ovat oikeat
        team = self.stats.team("PIT")
        self.assertEqual(team[0].name, "Lemieux")
    
    def test_top(self):
        # testataan top()-metodin toimintaa
        # eli testataan, että palauttaa oikean määrän pelaajia
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)
    
    def test_top_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")

    def test_top_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")

