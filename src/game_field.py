from game_stone import *

class GameField:

    def __init__(self, number, x, y, up):
        self.number = number
        # True if field is in upper half
        self.up = up
        self.x = x
        self.y = y
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def pop_stone(self):
        return self.stones.pop(-1)

    def draw_stones(self, win):
        for i, stone in enumerate(self.stones):
            stone.draw(win, self.x, self.y + i * 42 if self.up else self.y - i * 42)
