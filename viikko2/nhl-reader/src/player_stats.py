class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def sort_by_points(self, players):
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_scorers_by_nationality(self, country):
        players_from_country = list(filter(lambda player: player.nationality == country, self.players))
        players_from_countr_sorted = self.sort_by_points(players_from_country)

        return players_from_countr_sorted