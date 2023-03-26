import pygame

from constants import *
from bar import *
from dice import *
from game_board import *
from game_stone import *
from player import *
from game_field import *


class Game:
    def __init__(self, win, multiplayer):
        self.win = win
        self.bar = Bar()
        self.dice = Dice()
        self.game_board = GameBoard()
        self.game_fields = []
        self.multiplayer = multiplayer
        self.console_player1 = ConsolePlayer(False)
        if self.multiplayer:
            self.AI_player = AIPlayer(True)
        else:
            self.console_player2 = ConsolePlayer(True)

    def init_fields(self):
        for i in range(24):
            self.game_fields.append(GameField(i))

    def start_game(self):
        self.init_fields()

    def draw(self):
        pass

    def gameloop(self):
        run = True

        self.start_game()

        while run:
            pygame.time.Clock().tick(FPS)
            # self.win.fill(BLACK)
            game_board.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

    # TODO Dopsat az bude urceno, jak jsou ukladany polohy kamenu.
    # def save_game(self):
    #     file = open('/saves/save.json', 'w')
    #     file.write()
