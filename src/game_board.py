import os

import pygame

from constants import *

R_BOARD = pygame.image.load("../assets/board/1/R.png")
TR_R_BOTTOM = pygame.image.load("../assets/board/1/R_BOT.png")
TR_R_TOP = pygame.image.load("../assets/board/1/R_TOP.png")
L_BOARD = pygame.image.load("../assets/board/1/L.png")
TR_L_BOTTOM = pygame.image.load("../assets/board/1/L_BOT.png")
TR_L_TOP = pygame.image.load("../assets/board/1/L_TOP.png")


def draw_text(_win, text, size, font, color, x, y, center=True):
    font = pygame.font.Font(f'../assets/fonts/Inter/{font}.ttf', size)
    text_on_display = font.render(text, True, color)
    text_rect = text_on_display.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)

    _win.blit(text_on_display, text_rect)
    return text_rect


class GameBoard:

    def __init__(self, _win):
        self._win = _win

    def draw(self, p1_name, p2_name):
        image_width, image_height = L_BOARD.get_size()

        scale_factor = min(WIDTH / (image_width * 2), HEIGHT / image_height)
        scaled_image_width = int(image_width * scale_factor)
        scaled_image_height = int(image_height * scale_factor)
        scaled_l_board = pygame.transform.scale(L_BOARD, (scaled_image_width, scaled_image_height))
        scaled_r_board = pygame.transform.scale(R_BOARD, (scaled_image_width, scaled_image_height))

        background = pygame.Surface((scaled_image_width * 2, scaled_image_height))
        background.blit(scaled_l_board, (0, 0))
        background.blit(scaled_r_board, (scaled_image_width, 0))

        self._win.blit(background, (0, HEIGHT / 13))

        self.draw_nums()
        self.draw_names(f"{p1_name}", f"{p2_name}", BONE_WHITE, BLACK)
        self.draw_window()

    def draw_nums(self):
        """Draws numbers around the game board."""
        for i in range(6):
            draw_text(self._win, f"{i + 13}", 20, "Inter-Regular", BLACK, 130 + i * 88, 20)
            draw_text(self._win, f"{12 - i}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 50)
            draw_text(self._win, f"{i + 19}", 20, "Inter-Regular", BLACK, 830 + i * 88, 20)
            draw_text(self._win, f"{6 - i}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 50)

            draw_text(self._win, f"{i + 13}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 800)
            draw_text(self._win, f"{12 - i}", 20, "Inter-Regular", BLACK, 130 + i * 88, 830)
            draw_text(self._win, f"{i + 19}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 800)
            draw_text(self._win, f"{6 - i}", 20, "Inter-Regular", BLACK, 830 + i * 88, 830)

    def draw_names(self, player1: str, player2: str, color_p1, color_p2):
        """Draws the player names."""
        draw_text(self._win, f"{player1}", 30, "Inter-Regular", color_p1, 10, HEIGHT - 125, center=False)
        draw_text(self._win, f"{player2}", 30, "Inter-Regular", color_p2, 10, HEIGHT - 75, center=False)

    def draw_window(self):
        pygame.draw.rect(self._win, TAN, (WIDTH / 2 - 300, HEIGHT - 125, 600, 90))

    def draw_button(self, image, coords, text, text_x, text_y):
        button = pygame.image.load(os.path.join('../assets/board/1', image))
        rect = button.get_rect(topleft=coords)
        self._win.blit(button, coords)
        draw_text(self._win, text, 45, "Inter-Regular", BONE_WHITE, text_x, text_y)
        return rect

    def draw_roll_button(self):
        return self.draw_button('button_backg.png', (WIDTH - 370, HEIGHT - 125), "Roll", WIDTH - 305, HEIGHT - 80)

#TODO nepise saved!
    def draw_save_button(self, saved):
        roll_button = pygame.image.load(os.path.join('../assets/board/1', 'button_backg.png'))
        roll_rect = roll_button.get_rect(topleft=(635, 285))
        self._win.blit(roll_button, (635, 285))
        if saved:
            draw_text(self._win, "Saved!", 45, "Inter-Regular", BONE_WHITE, 700, 328)
        else:
            draw_text(self._win, "Save", 45, "Inter-Regular", BONE_WHITE, 700, 328)
        return roll_rect

    def draw_exit_button(self):
        return self.draw_button('button_backg_red.png', (635, 485), "Quit", 700, 529)

    def draw_back_to_menu_button(self):
        return self.draw_button('button_backg_red.png', (635, 385), "Menu", 700, 429)
