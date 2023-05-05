from game_stone import *

GLOW_UP = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 'L_TOP_GLOW.png')),
                                 (FIELD_WIDTH, FIELD_HEIGHT))
GLOW_DOWN = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 'L_BOT_GLOW.png')),
                                   (FIELD_WIDTH, FIELD_HEIGHT))


class GameField:

    def __init__(self, number, x, y, up):
        self._number = number
        # True if field is in upper half
        self._up = up
        self._x = x
        self._y = y
        self._stones = []
        self._rect = pygame.Rect(self._x, self._y, FIELD_WIDTH, FIELD_HEIGHT)

    @property
    def number(self):
        return self._number

    @property
    def rect(self):
        return self._rect

    @property
    def stones(self):
        return self._stones

    def add_stone(self, stone):
        self._stones.append(stone)

    def pop_stone(self):
        return self._stones.pop(-1)

    def is_empty(self):
        return len(self._stones) == 0

    def has_1_or_0_stones(self):
        return len(self._stones) <= 1

    def has_one_stone(self):
        return len(self._stones) == 1

    def draw_stones(self, win):
        if self._stones:
            spacing = FIELD_HEIGHT / len(self._stones)
            if spacing > 42:
                spacing = 42

            for i, stone in enumerate(self._stones):
                if self._up:
                    stone.draw(win, self._x, self._y + i * spacing)
                else:
                    stone.draw(win, self._x, self._y + FIELD_HEIGHT - STONE_SIZE - i * spacing)

    def glow(self, win):
        if self._up:
            win.blit(GLOW_UP, (self._x, self._y))
        else:
            win.blit(GLOW_DOWN, (self._x, self._y))
