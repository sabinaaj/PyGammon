from game_stone import *

GLOW_UP = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 'L_TOP_GLOW.png')),
                                 (FIELD_WIDTH, FIELD_HEIGHT))
GLOW_DOWN = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 'L_BOT_GLOW.png')),
                                   (FIELD_WIDTH, FIELD_HEIGHT))


class GameField:

    def __init__(self, number, x, y, up):
        self.number = number
        # True if field is in upper half
        self.up = up
        self.x = x
        self.y = y
        self.stones = []
        self.rect = pygame.Rect(self.x, self.y, FIELD_WIDTH, FIELD_HEIGHT)

    def add_stone(self, stone):
        self.stones.append(stone)

    def pop_stone(self):
        return self.stones.pop(-1)

    def is_empty(self):
        return len(self.stones) == 0

    def has_1_or_0_stones(self):
        return len(self.stones) <= 1

    def has_one_stone(self):
        return len(self.stones) == 1

    def draw_stones(self, win):
        for i, stone in enumerate(self.stones):
            if self.up:
                stone.draw(win, self.x, self.y + i * 42)
            else:
                stone.draw(win, self.x, self.y + FIELD_HEIGHT - STONE_SIZE - i * 42)

    def glow(self, win):
        if self.up:
            win.blit(GLOW_UP, (self.x, self.y))
        else:
            win.blit(GLOW_DOWN, (self.x, self.y))
