import pygame

from constants import *
from bar import *
from dice import *
from game_board import *
from game_stone import *
from player import *


class Game:
    def __init__(self, win):
        self.win = win
        self.bar = Bar()
        self.dice = Dice()
        self.game_board = GameBoard()


    def gameloop(self):
        run = True

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill(BLACK)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
