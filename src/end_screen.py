from game_board import *
from game_field import *
class EndScreen:
    def __init__(self, win):
        self._win = win
        self._text = ''

    def get_win_type(self, game_fields):

        if len(game_fields[0].stones) == 15 and len(game_fields[25].stones) >= 1:
            self._text = ''
            return

        elif len(game_fields[25].stones) == 15 and len(game_fields[0].stones) >= 1:
            self._text = ''
            return

        count = 0
        for i in range(1,7):
            count += len(game_fields[i].stones)

        if len(game_fields[0].stones) == 15 and count >= 1 and len(game_fields[25].stones) == 0:
            self._text = 'Backgammon'
            return

        elif len(game_fields[0].stones) == 15 and count == 0 and len(game_fields[25].stones) == 0:
            self._text = 'Gammon'
            return

        count = 0
        for i in range(19, 25):
            count += len(game_fields[i].stones)

        if len(game_fields[25].stones) == 15 and count >= 1 and len(game_fields[0].stones) == 0:
            self._text = 'Backgammon'
            return

        elif len(game_fields[25].stones) == 15 and count == 0 and len(game_fields[0].stones) == 0:
            self._text = 'Gammon'
            return

    def make_statistics(self, game_fields):

        avg_white_stone_lifespan = 0
        avg_black_stone_lifespan = 0

        white_discarded_stones = 0
        black_discarded_stones = 0

        for field in game_fields:
            for stone in field.stones:
                stone_lifespan = 0
                for position in stone.position:
                    if position != -1:
                        stone_lifespan += 1
                    else:
                        if stone.is_black:
                            black_discarded_stones += 1
                            avg_black_stone_lifespan += stone_lifespan
                        else:
                            white_discarded_stones += 1
                            avg_white_stone_lifespan += stone_lifespan
                        stone_lifespan = 0

                if stone.is_black:
                    avg_black_stone_lifespan += stone_lifespan
                else:
                    avg_white_stone_lifespan += stone_lifespan

        avg_white_stone_lifespan = avg_white_stone_lifespan / (white_discarded_stones + NUM_OF_STONES)
        avg_black_stone_lifespan = avg_black_stone_lifespan / (black_discarded_stones + NUM_OF_STONES)
        print(f'avg_black_stone_lifespan: {avg_black_stone_lifespan}')
        print(f'avg_white_stone_lifespan: {avg_white_stone_lifespan}')
        print(f'black_discarded_stones: {black_discarded_stones}')
        print(f'white_discarded_stones: {white_discarded_stones}')

        #TODO: Udělej počet vyvedených kamenů

    def end_screen(self, winner, game_fields):
        run = True
        self.get_win_type(game_fields)
        self.make_statistics(game_fields)

        while run:

            self._win.fill(WHITE)

            draw_text(self._win, f'{winner} won.', 85, 'Inter-Bold', BLACK, WIDTH / 2, 145,
                      center=True)
            draw_text(self._win, self._text, 35, 'Inter-Bold', BLACK, WIDTH / 2, 200,
                      center=True)
            draw_text(self._win, 'Statistics', 35, 'Inter-Regular', BLACK, WIDTH / 2, 700,
                      center=True)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
