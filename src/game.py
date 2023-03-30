from enum import Enum

from bar import *
from dice import *
from game_board import *
from game_field import *
from player import *


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
        self.avail_moves = []

        self.game_state = GameState.ROLL_DICE
        self.multiplayer = multiplayer
        self.player1 = ConsolePlayer(has_black_stones=False, name="Player1")
        if self.multiplayer:
            self.player2 = AIPlayer(has_black_stones=True, name="Player2")
        else:
            self.player2 = ConsolePlayer(has_black_stones=True, name="Player2")
        self.player_turn = self.player1

    def init_game(self):
        # number of fields matches white numbering - 1
        for i in range(6):
            self.game_fields.append(GameField(i, 1243.7 - i * 86.5, 167, True))
        for i in range(6, 12):
            self.game_fields.append(GameField(i, 549.5 - (i - 6) * 86.5, 167, True))
        for i in range(12, 18):
            self.game_fields.append(GameField(i, 113 + (i - 12) * 86.5, 480, False))
        for i in range(18, 24):
            self.game_fields.append(GameField(i, 807.2 + (i - 18) * 86.5, 480, False))

        # left_TOP
        for i in range(5):
            self.game_fields[11].add_stone(GameStone(11, self.player2.has_black_stones))
        for i in range(3):
            self.game_fields[7].add_stone(GameStone(7, self.player1.has_black_stones))

        # left_BOT
        for i in range(5):
            self.game_fields[12].add_stone(GameStone(12, self.player1.has_black_stones))
        for i in range(3):
            self.game_fields[16].add_stone(GameStone(16, self.player2.has_black_stones))

        # right_TOP
        for i in range(5):
            self.game_fields[5].add_stone(GameStone(5, self.player1.has_black_stones))
        for i in range(2):
            self.game_fields[0].add_stone(GameStone(0, self.player2.has_black_stones))

        # right_BOT
        for i in range(5):
            self.game_fields[18].add_stone(GameStone(18, self.player2.has_black_stones))
        for i in range(2):
            self.game_fields[23].add_stone(GameStone(23, self.player1.has_black_stones))

        self.player1.fields = [self.game_fields[5], self.game_fields[7], self.game_fields[12], self.game_fields[23]]
        self.player2.fields = [self.game_fields[0], self.game_fields[11], self.game_fields[16], self.game_fields[18]]

    def turn(self):
        if self.game_state == GameState.ROLL_DICE:
            self.roll_dice_state()

        if self.game_state == GameState.MOVE_STONE:
            self.move_stone_state()

    def roll_dice_state(self):
        draw_text(self.win, f"{self.player_turn.name}", 20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120,
                  center=False)

        if self.button_pressed:
            if self.roll:
                self.dice.std_roll(2)
                self.roll -= 1
            else:
                self.button_pressed = False
                self.game_state = GameState.MOVE_STONE

    def move_stone_state(self):
        count = self.dice.throw[0] + self.dice.throw[1]
        self.dice.throw.append(count)
        if self.dice.throw[0] == self.dice.throw[1]:
            count = self.dice.throw[0] * 4
            draw_text(self.win,
                      f"{self.player_turn.name} rolled {self.dice.throw[0]}, {self.dice.throw[1]}, {self.dice.throw[0]}, {self.dice.throw[1]} or {count} in total.",
                      20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120, center=False)
        else:
            draw_text(self.win,
                      f"{self.player_turn.name} rolled {self.dice.throw[0]} and {self.dice.throw[1]} or {count} in total.",
                      20, "Inter-Regular", BLACK, WIDTH / 2 - 295, HEIGHT - 120, center=False)


    def get_avail_moves(self, field):
        self.avail_moves = []
        for throw in self.dice.throw:
            field_num = self.get_valid_field_num(field.number, throw)
            if field_num:
                avail_field = self.game_fields[field_num]
                if avail_field.is_empty() or avail_field in self.player_turn.fields:
                    self.avail_moves.append(avail_field)

    def get_valid_field_num(self, start_number, throw):
        field_num = -1
        if self.player_turn.has_black_stones:
            field_num = start_number - throw
        else:
            field_num = start_number + throw

        if 0 <= field_num < 24:
            return field_num

        return None


    def draw(self):
        self.game_board.draw()

        self.dice.draw_std(self.dice.throw[0], self.win, 90, 90, WIDTH - 220, HEIGHT - 125)
        self.dice.draw_std(self.dice.throw[1], self.win, 90, 90, WIDTH - 110, HEIGHT - 125)

        for field in self.avail_moves:
            field.glow(self.win)

        for field in self.game_fields:
            field.draw_stones(self.win)

    def gameloop(self):
        run = True

        self.init_game()

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill((138, 161, 177))
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
                    if self.game_state == GameState.MOVE_STONE:
                        for field in self.player_turn.fields:
                            if field.rect.collidepoint(mouse_pos):
                                self.get_avail_moves(field)
                                self.game_state = GameState.ROLL_DICE

    # TODO Dopsat az bude urceno, jak jsou ukladany polohy kamenu.
    # def save_game(self):
    #     file = open('/saves/save.json', 'w')
    #     file.write()
