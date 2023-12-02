"""Tennis game module."""
from player import Player
class TennisGame:
    """Represents a tennis game."""

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
        """Return the game's score."""
        if self.is_deuce():
            return "Deuce"
        elif self.is_advantage():
            return "Advantage " + self.get_leader().name
        elif self.is_winner():
            return "Win for " + self.get_leader().name
        else:
            return self.get_score_name(self.player1.get_score()) + "-" + self.get_score_name(self.player2.get_score())

    def is_deuce(self):
        """Return True if the game is in deuce."""
        return self.player1.get_score() >= 3 and self.player2.get_score() == self.player1.get_score()

    def is_advantage(self):
        """Return True if the game is in advantage."""
        return self.player1.get_score() >= 4 or self.player2.get_score() >= 4

    def is_winner(self):
        """Return True if the game is won."""
        return self.is_advantage() and abs(self.player1.get_score() - self.player2.get_score()) >= 2

    def get_leader(self):
        """Return the player with the higher score."""
        if self.player1.get_score() > self.player2.get_score():
            return self.player1
        else:
            return self.player2

    def get_score_name(self, score):
        """Return the name of the score."""
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
        else:
            return "Error"
