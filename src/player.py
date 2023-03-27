import random
from abc import ABC


class Player(ABC):
    def __init__(self, color):
        # black - True, white - False
        self.color = color


class ConsolePlayer(Player):
    def __init__(self, color):
        super().__init__(color)


class AIPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def ai_choice(self, avail_fields: list):
        """
        Input is list, returns the field AI player chose.
        """
        choice = random.choice(avail_fields)
        return choice
