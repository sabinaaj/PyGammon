from abc import ABC


class Player(ABC):
    def __init__(self):
        pass


class ConsolePlayer(Player):
    def __init__(self):
        super().__init__()


class AIPlayer(Player):
    def __init__(self):
        super().__init__()
