from game_board import *
from game_field import *
from game import *
import menu

TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/menu', 'triangle.png')), (25, 25))

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

        white_bar_stones = 0
        black_bar_stones = 0

        for field in game_fields:
            for stone in field.stones:
                stone_lifespan = 0
                for position in stone.position:
                    if position != -1:
                        stone_lifespan += 1
                    else:
                        if stone.is_black:
                            black_bar_stones += 1
                            avg_black_stone_lifespan += stone_lifespan
                        else:
                            white_bar_stones += 1
                            avg_white_stone_lifespan += stone_lifespan
                        stone_lifespan = 0

                if stone.is_black:
                    avg_black_stone_lifespan += stone_lifespan
                else:
                    avg_white_stone_lifespan += stone_lifespan

        avg_white_stone_lifespan = avg_white_stone_lifespan / (white_bar_stones + NUM_OF_STONES)
        avg_black_stone_lifespan = avg_black_stone_lifespan / (black_bar_stones + NUM_OF_STONES)
        stones_discarded_white = len(game_fields[25].stones)
        stones_discarded_black = len(game_fields[0].stones)

        return avg_white_stone_lifespan, avg_black_stone_lifespan, white_bar_stones, black_bar_stones, stones_discarded_white, stones_discarded_black

    def end_screen(self, winner, game_fields, player1, player2):
        run = True
        self.get_win_type(game_fields)
        self.make_statistics(game_fields)
        avg_white_stone_lifespan, avg_black_stone_lifespan, white_bar_stones, black_bar_stones, stones_discarded_white, stones_discarded_black = self.make_statistics(game_fields)

        while run:

            mouse_pos = pygame.mouse.get_pos()

            self._win.fill(WHITE)

            exit_rect = draw_text(self._win, "EXIT", 30, "Inter-Bold", BLACK, 107, 700, center=False)

            menu_rect = draw_text(self._win, "MENU", 30, "Inter-Bold", BLACK, 300, 700, center=False)

            if exit_rect.collidepoint(mouse_pos):
                self._win.blit(TRIANGLE, (77, 705))
            if menu_rect.collidepoint(mouse_pos):
                self._win.blit(TRIANGLE, (270, 705))

            draw_text(self._win, f'{winner} won.', 85, 'Inter-Bold', BLACK, WIDTH / 2, 145,
                      center=True)

            draw_text(self._win, self._text, 35, 'Inter-Bold', BLACK, WIDTH / 2, 202.897,
                      center=True)

            draw_text(self._win, 'Statistics', 35, 'Inter-Regular', BLACK, WIDTH / 2, 250,
                      center=True)

            draw_text(self._win, 'Average stone lifespan', 25, 'Inter-Bold', BLACK, 250, 400, center=True)

            draw_text(self._win, 'Total on bar', 25, 'Inter-Bold', BLACK, 182, 475, center=True)

            draw_text(self._win, 'Total discarded', 25, 'Inter-Bold', BLACK, 204, 550, center=True)

            draw_text(self._win, f'{player1}', 25, 'Inter-Bold', BLACK, 500, 350,)

            draw_text(self._win, f'{player2}', 25, 'Inter-Bold', BLACK, 700, 350,)

            draw_text(self._win, f'{round(avg_white_stone_lifespan, 4)}', 25, 'Inter-Regular', BLACK, 500, 400,)

            draw_text(self._win, f'{round(avg_black_stone_lifespan,4)}', 25, 'Inter-Regular', BLACK, 700, 400,)

            draw_text(self._win, f'{white_bar_stones}', 25, 'Inter-Regular', BLACK, 500, 475,)

            draw_text(self._win, f'{black_bar_stones}', 25, 'Inter-Regular', BLACK, 700, 475,)

            draw_text(self._win, f'{stones_discarded_white}', 25, 'Inter-Regular', BLACK, 500, 550,)

            draw_text(self._win, f'{stones_discarded_black}', 25, 'Inter-Regular', BLACK, 700, 550,)

            pygame.display.update()

            for event in pygame.event.get():
                run = False
                m = menu.Menu(self._win)
                m.menu_loop()
