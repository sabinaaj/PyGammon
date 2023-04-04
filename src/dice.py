import os
import random

import pygame


class Dice:
    def __init__(self):
        self.throw = [3, 5]
        self.used = [False, False]

    def draw(self, number: int, win, size_x, size_y, x, y):
        """
        Returns texture in chosen resolution for standard dice.
        """
        if self.used[number]:
            dice = pygame.transform.scale(pygame.image.load(os.path.join(f'../assets/dice/gray', f'{self.throw[number]}'
                                                                         f'.png')), (size_x, size_y))
        else:
            dice = pygame.transform.scale(
                pygame.image.load(os.path.join(f'../assets/dice/white', f'{self.throw[number]}'
                                               f'.png')), (size_x, size_y))
        win.blit(dice, (x, y))

    def std_roll(self, num_throws: int):
        """
        Simulate rolling two standard six-sided dice.
        """
        self.throw = []
        for i in range(num_throws):
            self.throw.append(random.randint(1, 6))
