import random
from abc import ABC



class Player(ABC):
    def __init__(self, has_black_stones, name):
        self.has_black_stones = has_black_stones
        self.name = name
        self.fields = []


class ConsolePlayer(Player):
    def __init__(self, has_black_stones, name):
        super().__init__(has_black_stones, name)


class AIPlayer(Player):
    def __init__(self, has_black_stones, name):
        super().__init__(has_black_stones, name)

    def ai_choice(self, avail_fields: list):
        """
        Input is list, returns the field AI player chose.
        """
        choice = random.choice(range(len(avail_fields)))
        return avail_fields[choice], choice

