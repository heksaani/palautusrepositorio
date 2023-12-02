"""Player class for the tennis game."""
class Player:

    def __init__(self, name):
        """Initialize the player."""
        self.name = name
        self.score = 0

    def won_point(self):
        """Increment the player's score."""
        self.score += 1

    def get_score(self):
        """Return the player's score."""
        return self.score
