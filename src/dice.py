import os
import random

import pygame


class Dice:
    def __init__(self):
        self._throw = [3, 5]
        self._used = [False, False]

    @property
    def used(self):
        return self._used

    @used.setter
    def used(self, value):
        self._used = value

    @property
    def throw(self):
        return self._throw

    def draw(self, number: int, win, size_x, size_y, x, y):
        """
        Returns texture in chosen resolution for standard dice.
        """
        if self._used[number]:
            dice = pygame.transform.scale(pygame.image.load(os.path.join(f'../assets/dice/gray', f'{self._throw[number]}'
                                                                         f'.png')), (size_x, size_y))
        else:
            dice = pygame.transform.scale(
                pygame.image.load(os.path.join(f'../assets/dice/white', f'{self._throw[number]}'
                                               f'.png')), (size_x, size_y))
        win.blit(dice, (x, y))

    def std_roll(self, num_throws: int):
        """
        Simulate rolling two standard six-sided dice.
        """
        self._throw = []
        for i in range(num_throws):
            self._throw.append(random.randint(1, 6))

