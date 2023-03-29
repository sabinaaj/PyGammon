from bar import *
from dice import *
from game_board import *
from game_field import *
from player import *
from enum import Enum

class GameState(Enum):
    ROLL_DICE = 0
    MOVE_STONE = 1
    END_TURN = 2

class Game:
    def __init__(self, win, multiplayer):
        self.win = win
        self.bar = Bar()

        # number of rolls before dice stop
        self.button_pressed = False
        self.roll = 0
        self.dice = Dice()

        self.game_board = GameBoard(self.win)

        self.game_fields = []

        self.game_state = GameState.ROLL_DICE
        self.multiplayer = multiplayer
        self.player1 = ConsolePlayer(False, "Player1")
        if self.multiplayer:
            self.player2 = AIPlayer(True, "Player2")
        else:
            self.player2 = ConsolePlayer(True, "Player2")
        self.player_turn = self.player1

    def init_fields(self):
        for i in range(6):
            self.game_fields.append(GameField(i, 113 + i * 87.3, 173, True))
        for i in range(6, 12):
            self.game_fields.append(GameField(i, 807.2 + (i-6) * 87.3, 173, True))
        for i in range(12, 18):
            self.game_fields.append(GameField(i, 113 + (i-12) * 87.3, 645, False))
        for i in range(18, 24):
            self.game_fields.append(GameField(i, 807.2 + (i-18) * 87.3, 645, False))

        # left_TOP
        for i in range(5):
            self.game_fields[0].add_stone(GameStone(0, self.player2))
        for i in range(3):
            self.game_fields[4].add_stone(GameStone(4, self.player1))

        # left_BOT
        for i in range(5):
            self.game_fields[12].add_stone(GameStone(12, self.player1))
        for i in range(3):
            self.game_fields[16].add_stone(GameStone(16, self.player2))

        # right_TOP
        for i in range(5):
            self.game_fields[6].add_stone(GameStone(6, self.player1))
        for i in range(2):
            self.game_fields[11].add_stone(GameStone(11, self.player2))

        # right_BOT
        for i in range(5):
            self.game_fields[18].add_stone(GameStone(18, self.player2))
        for i in range(2):
            self.game_fields[23].add_stone(GameStone(23, self.player1))

    def start_game(self):
        self.init_fields()

    def turn(self):
        if self.game_state == GameState.ROLL_DICE:
            self.roll_dice_state()

        if self.game_state == GameState.MOVE_STONE:
            self.move_stone_state()

        # text, kdo je na tahu
        # hod kostkou
        # text, kdo co hodil
        # pohyb kamenu
        # konec kola
        pass

    def roll_dice_state(self):
        draw_text(self.win, f"{self.player_turn.name}", 20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120, center=False)

        if self.button_pressed:
            if self.roll:
                self.dice.std_roll(2)
                self.roll -= 1
            else:
                self.button_pressed = False
                self.game_state = GameState.MOVE_STONE

    def move_stone_state(self):
        count = self.dice.throw[0] + self.dice.throw[1]
        if self.dice.throw[0] == self.dice.throw[1]:
            count_4 = self.dice.throw[0] * 4
            draw_text(self.win, f"Player {self.player_turn.name} rolled {self.dice.throw[0]}, {self.dice.throw[1]}, {self.dice.throw[0]}, {self.dice.throw[1]} or {count_4} in total.",20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120, center=False)
        else:
            draw_text(self.win, f"Player {self.player_turn.name} rolled {self.dice.throw[0]} and {self.dice.throw[1]} or {count} in total.", 20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120,center=False)

    def draw(self):
        self.game_board.draw()

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
            roll_rect = self.game_board.draw_roll_button()

            self.turn()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if roll_rect.collidepoint(mouse_pos) and self.game_state == GameState.ROLL_DICE:
                        self.roll = random.randint(4, 8)
                        self.button_pressed = True

    # TODO Dopsat az bude urceno, jak jsou ukladany polohy kamenu.
    # def save_game(self):
    #     file = open('/saves/save.json', 'w')
    #     file.write()
