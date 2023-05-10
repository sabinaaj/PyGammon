import copy
from enum import Enum
import json

import menu
from end_screen import *
from bar import *
from dice import *
from player import *

STONES_INIT = [(1, 2, True), (6, 5, False), (8, 3, False), (12, 5, True), (13, 5, False), (17, 3, True), (19, 5, True),
               (24, 2, False)]


class GameState(Enum):
    ROLL_DICE = 0
    MOVE_STONE = 1
    MOVE_STONE_FROM_BAR = 2

class GameMode(Enum):
    SINGLEPLAYER = 0
    MULTIPLAYER = 1
    AI_VS_AI = 2


class Game:
    """
    Start game
    """

    def __init__(self, win, game_mode, p1_name, p2_name):
        self._win = win

        self._bar = Bar()

        self._button_pressed = False
        # number of rolls before dice stop
        self._roll = 0
        # Moves which player can do computed from values on dice
        self._dice_move = []
        self._same_number = False
        self._dice = Dice()

        self._game_board = GameBoard(self._win)
        self._text = ''
        self._no_moves = False
        self._can_bear_off = False

        self._game_fields = []
        self._avail_moves = {}
        self._chosen_field = None

        self._game_state = GameState.ROLL_DICE
        self._game_mode = game_mode
        if self._game_mode == GameMode.AI_VS_AI:
            self._player1 = AIPlayer(has_black_stones=False, name='AI 1')
            self._AIturn = True
        else:
            self._player1 = ConsolePlayer(has_black_stones=False, name=f'{p1_name}')
            self._AIturn = False

        if self._game_mode != GameMode.MULTIPLAYER:
            self._player2 = AIPlayer(has_black_stones=True, name='AI')
        else:
            self._player2 = ConsolePlayer(has_black_stones=True, name=f'{p2_name}')

        self._player_turn = self._player1

    def init_game(self):
        for field in STONES_INIT:
            for i in range(field[1]):
                self._game_fields[field[0]].add_stone(GameStone([field[0]], field[2]))

                if field[2]:  # player has black stones
                    if self._game_fields[field[0]] not in self._player2.fields:
                        self._player2.fields.append(self._game_fields[field[0]])
                else:
                    if self._game_fields[field[0]] not in self._player1.fields:
                        self._player1.fields.append(self._game_fields[field[0]])

    def init_fields(self):
        # number of fields matches white numbering
        self._game_fields.append(GameField(0, 1327, 240, True))
        for i in range(1, 7):
            self._game_fields.append(GameField(i, 1243.7 - (i - 1) * 86.5, 167, True))
        for i in range(7, 13):
            self._game_fields.append(GameField(i, 549.5 - (i - 7) * 86.5, 167, True))
        for i in range(13, 19):
            self._game_fields.append(GameField(i, 113 + (i - 13) * 86.5, 480, False))
        for i in range(19, 25):
            self._game_fields.append(GameField(i, 807.2 + (i - 19) * 86.5, 480, False))
        self._game_fields.append(GameField(25, 1327, 570, False))

    def turn(self):
        if self._game_state == GameState.ROLL_DICE:
            self.roll_dice_state()

        if self._game_state == GameState.MOVE_STONE:
            self.move_stone_state()

        if self._game_state == GameState.MOVE_STONE_FROM_BAR:
            self.move_stone_state()
            self.move_stone_from_bar_state()

    def ai_turn(self):
        while self._game_state != GameState.ROLL_DICE:

            if self._game_state == GameState.MOVE_STONE_FROM_BAR:
                self.bar_clicked()

                if not self._avail_moves[self._chosen_field]:
                    self.end_turn()
                    break

                field = self._player_turn.ai_choice(self._avail_moves[self._chosen_field])
                self.move_stone(field)

            field = None

            if self._game_state == GameState.MOVE_STONE:
                self._chosen_field = self._player_turn.ai_choice(self._player_turn.fields)
                while not self._avail_moves[self._chosen_field]:
                    self._chosen_field = self._player_turn.ai_choice(self._player_turn.fields)
                field = self._player_turn.ai_choice(self._avail_moves[self._chosen_field])
                print(self._chosen_field.number)
                self.move_stone(field)

    """
    Roll dice
    """

    def roll_dice_state(self):
        if self._no_moves:
            self._text = f"You had no available moves. It's {self._player_turn.name}'s turn."
        else:
            self._text = f"It's {self._player_turn.name}'s turn."

        if self._button_pressed:
            if self._roll:
                self._dice.std_roll(2)
                self._roll -= 1
            else:
                self.stop_rolling()

    def stop_rolling(self):
        self._button_pressed = False

        if self._dice.throw[0] == self._dice.throw[1]:
            self._same_number = True
            self._dice_move = [self._dice.throw[0], 2 * self._dice.throw[0], 3 * self._dice.throw[0],
                               4 * self._dice.throw[0]]
        else:
            self._same_number = False
            self._dice_move = copy.deepcopy(self._dice.throw)
            self._dice_move.append(self._dice_move[0] + self._dice_move[1])

        if self._bar in self._player_turn.fields:
            self._game_state = GameState.MOVE_STONE_FROM_BAR
        else:
            self._game_state = GameState.MOVE_STONE

        self.get_avail_moves()

        if self._AIturn:
            self.ai_turn()

    def roll_button_clicked(self):
        self._roll = random.randint(4, 8)
        self._dice.used = [False, False]
        self._button_pressed = True

    """
    Move stone
    """

    def move_stone_state(self):
        if self._dice.throw[0] == self._dice.throw[1]:
            self._text = f'{self._player_turn.name} rolled 4x{self._dice.throw[0]} and may move stones {self._dice.throw[0]},' \
                        f' {2 * self._dice.throw[0]}, {3 * self._dice.throw[0]} or {4 * self._dice.throw[0]} spaces.'
        else:
            self._text = f'{self._player_turn.name} rolled {self._dice.throw[0]} and {self._dice.throw[1]} or' \
                        f' {self._dice.throw[0] + self._dice.throw[1]} in total.'

    def move_stone_from_bar_state(self):
        draw_text(self._win, 'Player has stones on bar.', 20, 'Inter-Regular', BLACK, WIDTH / 2 - 295, HEIGHT - 90,
                  center=False)

    def get_avail_moves(self):
        """
        Gets available moves for every field where player has stones.
        """
        self._no_moves = True

        for field in self._player_turn.fields:

            if not self._same_number:
                if len(self._dice_move) == 3:
                    current_avail_moves = self.get_current_avail_moves(field.number, self._dice_move[:2])
                    if current_avail_moves:
                        current_avail_moves += self.get_current_avail_moves(field.number, self._dice_move[2:])
                else:
                    current_avail_moves = self.get_current_avail_moves(field.number, self._dice_move[:1])

            else:
                current_avail_moves = self.get_current_avail_moves(field.number, self._dice_move)

                for index, move in enumerate(current_avail_moves):
                    if move[0] != self._dice_move[index]:

                        current_avail_moves = current_avail_moves[:index]
                        break

            if current_avail_moves:
                self._no_moves = False

            print(f"{field.number}: {current_avail_moves}")
            self._avail_moves[field] = current_avail_moves

        print(self._game_state)
        if self._bar in self._player_turn.fields and not self._avail_moves[self._bar]:
            self._no_moves = True

        print(self._dice_move)
        print(f"no_moves: {self._no_moves}")
        if self._no_moves:
            self.end_turn()

    def get_current_avail_moves(self, start_number, throw_list):
        """
        Gets available moves for one field.
        """
        current_avail_moves = []

        if start_number == 0 or start_number == 25:
            return current_avail_moves

        if start_number == -1:  # bar
            start_number = 25 if self._player_turn.has_black_stones else 0

        for throw in throw_list:
            field_num = self.get_valid_field_num(start_number, throw)

            if field_num is not None:
                avail_field = self._game_fields[field_num]
                if avail_field.has_1_or_0_stones() or avail_field in self._player_turn.fields:
                    current_avail_moves.append((throw, avail_field))

        return current_avail_moves

    def get_valid_field_num(self, start_number, throw):
        if self._player_turn.has_black_stones:
            field_num = start_number - throw
        else:
            field_num = start_number + throw

        if 0 < field_num < 25:
            return field_num

        if self._can_bear_off:
            if self._player_turn == self._player1 and field_num > 24:
                return 25
            if self._player_turn == self._player2 and field_num < 1:
                return 0

        return None

    def move_stone(self, end_field):
        """
        Moves stone from one field to another.
        """
        print("pred", end=": ")
        for i in range(len(self._player_turn.fields)):
            print(self._player_turn.fields[i].number, end=", ")
        print("")
        print(self._chosen_field.number)

        stone = None
        if self._chosen_field == self._bar:
            stone = self._chosen_field.pop_stone(self._player_turn.has_black_stones)
            if self._chosen_field.is_empty(self._player_turn.has_black_stones):
                self._player_turn.fields.remove(self._chosen_field)
        else:
            stone = self._chosen_field.pop_stone()
            if self._chosen_field.is_empty():
                self._player_turn.fields.remove(self._chosen_field)

        stone.position.append(end_field[1].number)
        if end_field[1] not in self._player_turn.fields:
            self._player_turn.fields.append(end_field[1])

            # opponent's stone got hit and moves to bar
            if end_field[1].has_one_stone():
                opponent_stone = end_field[1].pop_stone()
                self._bar.add_stone(opponent_stone)

                if self._player_turn == self._player1:
                    self._player2.fields.remove(end_field[1])
                    if self._bar not in self._player2.fields:
                        self._player2.fields.append(self._bar)
                else:
                    self._player1.fields.remove(end_field[1])
                    if self._bar not in self._player1.fields:
                        self._player1.fields.append(self._bar)

                opponent_stone.position.append(self._bar.number)

        stone.position.append(end_field[1].number)
        if end_field[1] not in self._player_turn.fields:
            self._player_turn.fields.append(end_field[1])

        end_field[1].add_stone(stone)

        print(
            f"Kamen se premistil z {self._chosen_field.number} na {end_field[1].number} a posunul se o {end_field[0]} poli.")
        for i in range(len(self._player_turn.fields)):
            print(self._player_turn.fields[i].number, end=", ")
        print("")

        self._chosen_field = None
        index = self._dice_move.index(end_field[0])

        if not self._same_number:
            print(f"{index} index")
            if index == 2:
                self.end_turn()
            else:
                num = self._dice_move.pop(index)
                print(f"{num} bylo pouzito.")
                self._dice.used[index] = True
                if self._dice_move:
                    num = self._dice_move.pop(-1)
                    print(f"{num} bylo pouzito.")
                    self.get_avail_moves()
                else:
                    self.end_turn()
        else:
            self._dice_move = self._dice_move[:((len(self._dice_move) - 1) - index)]
            if len(self._dice_move) == 0:
                self.end_turn()
            else:
                self.get_avail_moves()

    def game_fields_clicked(self, mouse_pos):
        if self._chosen_field:
            for field in self._avail_moves[self._chosen_field]:
                if field[1].rect.collidepoint(mouse_pos):
                    self.move_stone(field)
                    break

        for field in self._player_turn.fields:
            if field.rect.collidepoint(mouse_pos) and self._chosen_field != self._bar:
                if self._chosen_field == field:
                    self._chosen_field = None
                else:
                    if field.number != 0 or field.number != 25:
                        self._chosen_field = field

    def bar_clicked(self):
        self._chosen_field = self._bar
        self.get_avail_moves()
        self._game_state = GameState.MOVE_STONE

    def bear_off(self):
        for field in self._player_turn.fields:
            if self._player_turn.has_black_stones and field.number > 6:
                self._can_bear_off = False
                return
            if not self._player_turn.has_black_stones and field.number < 19:
                self._can_bear_off = False
                return

        self._can_bear_off = True
        draw_text(self._win, 'You can bear off.', 20, 'Inter-Regular', BLACK, WIDTH / 2 - 295, HEIGHT - 90,
                  center=False)

    """
    End turn
    """

    def end_turn(self):
        self._game_state = GameState.ROLL_DICE
        self._chosen_field = None
        self._dice.used = [True, True]

        if self._player_turn == self._player1:
            self._player_turn = self._player2
            if self._game_mode != GameMode.MULTIPLAYER:
                self._AIturn = True
                self.roll_button_clicked()
            else:
                self._AIturn = False

        else:
            self._player_turn = self._player1
            if self._game_mode == GameMode.AI_VS_AI:
                self._AIturn = True
                self.roll_button_clicked()
            else:
                self._AIturn = False

        print("------")
        print(f"{self._player_turn.name} je na tahu")

    def draw(self):
        self._game_board.draw(self._player1.name, self._player2.name)

        self._dice.draw(0, self._win, 90, 90, WIDTH - 220, HEIGHT - 125)
        self._dice.draw(1, self._win, 90, 90, WIDTH - 110, HEIGHT - 125)

        if self._chosen_field and self._game_state != GameState.ROLL_DICE:
            for field in self._avail_moves[self._chosen_field]:
                if field:
                    field[1].glow(self._win)

        for field in self._game_fields:
            field.draw_stones(self._win)
        self._bar.draw_stones(self._win)

        draw_text(self._win, self._text, 20, 'Inter-Regular', BLACK, WIDTH / 2 - 295, HEIGHT - 120,
                  center=False)


    def gameloop(self, load=''):
        run = True
        show_menu = False
        self.init_fields()

        if load:
            self.load_game(load)
        else:
            self.init_game()

        if self._game_mode == GameMode.AI_VS_AI:
            self.roll_button_clicked()

        while run:
            pygame.time.Clock().tick(FPS)
            self._win.fill(FAWN)
            mouse_pos = pygame.mouse.get_pos()

            self.draw()
            roll_rect = self._game_board.draw_roll_button()

            self.turn()

            self.bear_off()

            if show_menu:
                pygame.draw.rect(self._win, FAWN, [550, 200, 300, 450], 0)
                save_rect = self._game_board.draw_save_button()
                quit_rect = self._game_board.draw_exit_button()
                back_to_menu_rect = self._game_board.draw_back_to_menu_button()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        show_menu = not show_menu

                if event.type == pygame.MOUSEBUTTONDOWN and not self._AIturn:

                    if roll_rect.collidepoint(mouse_pos) and self._game_state == GameState.ROLL_DICE:
                        self.roll_button_clicked()

                    if self._game_state == GameState.MOVE_STONE:
                        self.game_fields_clicked(mouse_pos)

                    if self._bar.rect.collidepoint(mouse_pos) and self._game_state == GameState.MOVE_STONE_FROM_BAR:
                        self.bar_clicked()


                    if show_menu:
                        if save_rect.collidepoint(mouse_pos):
                            self.save_game()

                        if quit_rect.collidepoint(mouse_pos):
                            run = False
                            pygame.quit()

                        if back_to_menu_rect.collidepoint(mouse_pos):
                            run = False
                            m = menu.Menu(self._win)
                            m.menu_loop()

            run = self.endgame(run)


    def format_for_save(self):
        data = {}
        data["game_fields"] = []
        data["player_names"] = []
        data["dice"] = []
        data["player_turn"] = self._player_turn.name
        data["bar"] = []
        data["game_state"] = self._game_state.name
        data["same_number"] = self._same_number
        data["game_mode"] = self._game_mode.name

        avail_moves_dict = {}
        for key, value in self._avail_moves.items():
            avail_moves_dict[key.number] = [[field[0], field[1].number] if field else None for field in value]
        data["avail_moves_dict"] = avail_moves_dict
        data["dice_move"] = self._dice_move
        data["dice_used"] = self._dice.used
        data["player_names"].append({
            "player1": str(self._player1.name),
            "player2": str(self._player2.name),
        })

        for field in self._game_fields:
            stones = []
            for stone in field.stones:
                if stone.is_black:
                    color = "Black"
                else:
                    color = "White"
                stones.append({
                    "position": stone.position,
                    "color": color,
                })

            data["game_fields"].append({
                "number": field.number,
                "stones": stones,
            })

        for stone in self._bar.stones:
            if stone.is_black:
                color = "Black"
            else:
                color = "White"
            data["bar"].append({
                "position": stone.position,
                "color": color,
            })

        return data

    def save_game(self):
        data = self.format_for_save()
        with open("../save.json", "w") as outfile:
            json.dump(data, outfile)

    def load_game(self, file: json):
        with open(file) as json_file:
            data = json.load(json_file)

            self._player1.name = data["player_names"][0]["player1"]
            self._player2.name = data["player_names"][0]["player2"]
            self._same_number = data["same_number"]
            self._game_state = GameState[data["game_state"]]
            self._dice_move = data["dice_move"]
            self._dice.used = data["dice_used"]
            self._game_mode = GameMode[data["game_mode"]]

            for field_key in data["avail_moves_dict"]:
                self._avail_moves[self._game_fields[int(field_key)]] = []
                for field in data["avail_moves_dict"][field_key]:
                    self._avail_moves[self._game_fields[int(field_key)]].append((int(field[0]), self._game_fields[int(field[1])]))

        if data["player_turn"] == self._player1.name:
            self._player_turn = self._player1
        else:
            self._player_turn = self._player2

        for field in data["game_fields"]:
            is_black = None
            for stone in field["stones"]:
                if stone["color"] == "Black":
                    is_black = True
                else:
                    is_black = False
                self._game_fields[field["number"]].add_stone(GameStone(stone["position"], is_black))
            if is_black:
                self._player2.fields.append(self._game_fields[field["number"]])
            elif is_black == False: # not is_black don't work
                self._player1.fields.append(self._game_fields[field["number"]])

        for stone in data["bar"]:
            if stone["color"] == "Black":
                is_black = True
                if self._bar not in self._player2.fields:
                    self._player2.fields.append(self._bar)
            else:
                is_black = False
                if self._bar not in self._player1.fields:
                    self._player1.fields.append(self._bar)
            self._bar.add_stone(GameStone(stone["position"], is_black))

    def endgame(self, run):
        '''
        function for determining the win type and the winner of the game
        '''
        if len(self._game_fields[0].stones) >= 15:
            winner = self._player2.name
            run = False
            end_screen = EndScreen(self._win)
            end_screen.end_screen(winner, self._game_fields)

        elif len(self._game_fields[25].stones) >= 15:
            winner = self._player1.name
            run = False
            end_screen = EndScreen(self._win)
            end_screen.end_screen(winner, self._game_fields, self._player1.name, self._player2.name)

        return run


