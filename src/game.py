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
        # True - multiplayer, False - singleplayer
        self.multiplayer = False
        self.bar = Bar()
        self.dice = Dice()
        self.game_board = GameBoard()


    def gameloop(self, multiplayer):
        self.multiplayer = multiplayer
        run = True

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill(BLACK)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    # TODO Dopsat az bude urceno, jak jsou ukladany polohy kamenu.
    # def save_game(self):
    #     file = open('/saves/save.json', 'w')
    #     file.write()
