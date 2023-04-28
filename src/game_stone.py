import os

import pygame

from constants import *

B_STONE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 's_b.png')),
                                 (STONE_SIZE, STONE_SIZE))
W_STONE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/board/1', 's_w.png')),
                                 (STONE_SIZE, STONE_SIZE))


class GameStone:
    def __init__(self, position, is_black):
        self._position = position
        self._is_black = is_black
        self._image = B_STONE if self._is_black else W_STONE

    @property
    def position(self):
        return self._position

    @property
    def is_black(self):
        return self._is_black

    def draw(self, win, x, y):
        win.blit(self._image, (x, y))
