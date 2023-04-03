from game_stone import *


class Bar:
    def __init__(self):
        self.number = None
        self.stones = []
        self.rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self.stones) * STONE_SIZE)

    def add_stone(self, stone):
        self.stones.append(stone)
        self.make_rectangle()

    def pop_stone(self):
        stone = self.stones.pop(-1)
        self.make_rectangle()
        return stone

    def is_empty(self):
        return len(self.stones) == 0

    def make_rectangle(self):
        self.rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self.stones) * STONE_SIZE)

    def draw_stones(self, win):
        for i, stone in enumerate(self.stones):
            stone.draw(win, WIDTH / 2 - STONE_SIZE / 2, 400 + i * 50)
