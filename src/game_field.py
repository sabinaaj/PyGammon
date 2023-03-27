class GameField:
    def __init__(self, number):
        self.number = number
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def pop_stone(self):
        return self.stones.pop(-1)
