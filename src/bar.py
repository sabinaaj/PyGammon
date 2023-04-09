from game_stone import *


class Bar:
    def __init__(self):
        self.number = None
        self.stones = []
        self.rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self.stones) * STONE_SIZE)

    def add_stone(self, stone):
        self.stones.append(stone)
        self.make_rectangle()

    def pop_stone(self, has_black_stones):
        for stone in self.stones:
            # stone has same color as player on turn
            if stone.is_black == has_black_stones:
                self.stones.remove(stone)
                self.make_rectangle()
                return stone


    def is_empty(self, has_black_stones):
        for stone in self.stones:
            # stone has same color as player on turn
            if stone.is_black == has_black_stones:
                return False

        return True

    def make_rectangle(self):
        self.rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self.stones) * STONE_SIZE)

    def draw_stones(self, win):
        for i, stone in enumerate(self.stones):
            stone.draw(win, WIDTH / 2 - STONE_SIZE / 2, 400 + i * 50)
