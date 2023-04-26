from game_stone import *


class Bar:
    def __init__(self):
        self._number = None
        self._stones = []
        self._rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self._stones) * STONE_SIZE)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def stones(self):
        return self._stones

    @stones.setter
    def stones(self, value):
        self._stones = value

    @property
    def rect(self):
        return self._rect

    def add_stone(self, stone):
        self._stones.append(stone)
        self.make_rectangle()

    def pop_stone(self, has_black_stones):
        for stone in self._stones:
            # stone has same color as player on turn
            if stone.is_black == has_black_stones:
                self._stones.remove(stone)
                self.make_rectangle()
                return stone

    def is_empty(self, has_black_stones):
        for stone in self._stones:
            # stone has same color as player on turn
            if stone.is_black == has_black_stones:
                return False

        return True

    def make_rectangle(self):
        self._rect = pygame.Rect(WIDTH / 2 - STONE_SIZE / 2, 400, STONE_SIZE, len(self._stones) * STONE_SIZE)

    def draw_stones(self, win):
        for i, stone in enumerate(self._stones):
            stone.draw(win, WIDTH / 2 - STONE_SIZE / 2, 400 + i * 50)

