import os

import pygame

from constants import *

B_STONE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 's_b.png')),
                                 (STONE_SIZE, STONE_SIZE))
W_STONE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 's_w.png')),
                                 (STONE_SIZE, STONE_SIZE))


class GameStone:
    def __init__(self, position, player):
        self.position = [position]
        self.player = player
        self.is_black = player.has_black_stones
        self.image = B_STONE if self.is_black else W_STONE

    def draw(self, win, x, y):
        win.blit(self.image, (x, y))
