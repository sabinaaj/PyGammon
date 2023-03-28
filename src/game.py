from bar import *
from dice import *
from game_board import *
from game_field import *
from player import *


class Game:
    def __init__(self, win, multiplayer):
        self.win = win
        self.bar = Bar()

        self.dice = Dice()
        # number of rolls before dice stop
        self.roll = 0

        self.game_board = GameBoard()

        self.game_fields = []


        self.multiplayer = multiplayer
        self.player1 = ConsolePlayer(False)
        if self.multiplayer:
            self.player2 = AIPlayer(True)
        else:
            self.player2 = ConsolePlayer(True)

    def init_fields(self):
        for i in range(12):
            self.game_fields.append(GameField(i, 113 + i * 87.3, 173, True))
        # for i in range(12):
        #     self.game_fields.append(GameField(i, 220 + i * 87.3, 173, True))
        # for i in range(13, 25):
        #     self.game_fields.append(GameField(i, 50 + (i-13) * 50, 600, False))
        for i in range(13, 25):
            self.game_fields.append(GameField(i, 50 + (i-13) * 50, 600, False))

        #left_TOP
        for i in range(5):
            self.game_fields[0].add_stone(GameStone(0, self.player2))
        for i in range(3):
            self.game_fields[4].add_stone(GameStone(4, self.player1))

        #left_BOT
        for i in range(5):
            self.game_fields[12].add_stone(GameStone(12, self.player1))
        for i in range(3):
            self.game_fields[16].add_stone(GameStone(16, self.player2))

        #right_TOP
        for i in range(5):
            self.game_fields[6].add_stone(GameStone(6, self.player1))
        for i in range(2):
            self.game_fields[11].add_stone(GameStone(11, self.player2))

        #right_BOT
        for i in range(5):
            self.game_fields[18].add_stone(GameStone(18, self.player2))
        for i in range(2):
            self.game_fields[23].add_stone(GameStone(23, self.player1))

    def draw_roll_button(self, win):
        roll_rect = pygame.draw.rect(win, GRAY, (WIDTH - 370, HEIGHT - 125, 130, 90))
        draw_text(win, f"ROLL", 45, "Inter-Bold", BLACK, WIDTH - 305, HEIGHT - 80)
        return roll_rect

    def start_game(self):
        self.init_fields()

    def draw(self):
        self.game_board.draw(self.win)

        self.dice.draw_std(self.dice.throw[0], self.win, 90, 90, WIDTH - 220, HEIGHT - 125)
        self.dice.draw_std(self.dice.throw[1], self.win, 90, 90, WIDTH - 110, HEIGHT - 125)

        for field in self.game_fields:
            field.draw_stones(self.win)

    def gameloop(self):
        run = True

        self.start_game()

        roll_dice = pygame.USEREVENT
        pygame.time.set_timer(roll_dice, 100)

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill(SAGE)
            mouse_pos = pygame.mouse.get_pos()

            self.draw()
            roll_rect = self.draw_roll_button(self.win)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if roll_rect.collidepoint(mouse_pos):
                        self.roll = 5
                if event.type == roll_dice:
                    if self.roll:
                        self.dice.std_roll(2)
                        self.roll -= 1

    # TODO Dopsat az bude urceno, jak jsou ukladany polohy kamenu.
    # def save_game(self):
    #     file = open('/saves/save.json', 'w')
    #     file.write()
