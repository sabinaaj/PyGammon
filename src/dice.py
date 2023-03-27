import random
import pygame
import os


class Dice:
    def __init__(self):
        self.throw = []

    def draw_std(self, number: int, size_x, size_y):
        """
        Returns texture in chosen resolution for standard dice.
        """
        # for i in range(900):
        #     random_draw = pygame.transform.scale(pygame.image.load(os.path.join('../assets/dice/std', f'{random.randint(1,6)}.svg')), (size_x, size_y))
        dice = pygame.transform.scale(pygame.image.load(os.path.join('../assets/dice/std', f'{number}.svg')), (size_x, size_y))
        return dice

    def draw_spec(self,  number: int, size_x, size_y):
        """
        Returns texture in chosen resolution for special dice.
        """
        dice = pygame.transform.scale(pygame.image.load(os.path.join('../assets/dice/spec', f'{number}.svg')), (size_x, size_y))
        return dice

    def std_roll(self, num_throws: int):
        """
        Simulate rolling two standard six-sided dice.
        """
        self.throw = []
        for i in range(num_throws):
            self.throw.append(random.randint(1, 6))
        return self.throw

    def spec_roll(self):
        """
        Simulate rolling one user defined six-sided dice.
        """
        self.throw = []
        num_lst = [2, 4, 8, 16, 32, 64]
        self.throw.append(random.choice(num_lst))
        return self.throw
