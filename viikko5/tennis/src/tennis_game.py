from player import Player
class TennisGame:
    """TennisGame class"""
    
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        """Initialize the game."""
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)


    def won_point(self, player_name):
        """Increment the player's score."""
        if player_name == self.player1.name:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def get_score(self):
        """Return the game score."""

        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() < 3:
                return self.SCORE_NAMES[self.player1.get_score()] + "-All"
            else:
                return "Deuce"
        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            score_difference = self.player1.get_score() - self.player2.get_score()
            if score_difference == 1:
                return "Advantage " + self.player1.name
            elif score_difference == -1:
                return "Advantage " + self.player2.name
            elif score_difference >= 2:
                return "Win for " + self.player1.name
            else:
                return "Win for " + self.player2.name
        else:
            return self.SCORE_NAMES[self.player1.get_score()] + "-" + self.SCORE_NAMES[self.player2.get_score()]

      

