import pygame
import os

from constants import *

R_BOARD = pygame.image.load("../assets/board/1/R.png")
TR_R_BOTTOM = pygame.image.load("../assets/board/1/R_BOT.png")
TR_R_TOP = pygame.image.load("../assets/board/1/R_TOP.png")
L_BOARD = pygame.image.load("../assets/board/1/L.png")
TR_L_BOTTOM = pygame.image.load("../assets/board/1/L_BOT.png")
TR_L_TOP = pygame.image.load("../assets/board/1/L_TOP.png")


def draw_text(win, text, size, font, color, x, y, center=True):
    font = pygame.font.Font(f'../assets/fonts/Inter/{font}.ttf', size)
    text_on_display = font.render(text, True, color)
    text_rect = text_on_display.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)

    win.blit(text_on_display, text_rect)
    return text_rect


class GameBoard:

    def __init__(self, win):
        self.win = win

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

        self.win.blit(background, (0, HEIGHT / 13))

        self.draw_nums()
        self.draw_names(f"{p1_name}", f"{p2_name}", BONE_WHITE, BLACK)
        self.draw_window()

    def draw_nums(self):
        """Draws numbers around the game board."""
        for i in range(6):
            draw_text(self.win, f"{i + 13}", 20, "Inter-Regular", BLACK, 130 + i * 88, 20)
            draw_text(self.win, f"{12 - i}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 50)
            draw_text(self.win, f"{i + 19}", 20, "Inter-Regular", BLACK, 830 + i * 88, 20)
            draw_text(self.win, f"{6 - i}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 50)

            draw_text(self.win, f"{i + 13}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 800)
            draw_text(self.win, f"{12 - i}", 20, "Inter-Regular", BLACK, 130 + i * 88, 830)
            draw_text(self.win, f"{i + 19}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 800)
            draw_text(self.win, f"{6 - i}", 20, "Inter-Regular", BLACK, 830 + i * 88, 830)

    def draw_names(self, player1: str, player2: str, color_p1, color_p2):
        """Draws the player names."""
        draw_text(self.win, f"{player1}", 30, "Inter-Regular", color_p1, 10, HEIGHT - 125, center=False)
        draw_text(self.win, f"{player2}", 30, "Inter-Regular", color_p2, 10, HEIGHT - 75, center=False)

    def draw_window(self):
        pygame.draw.rect(self.win, TAN, (WIDTH/2 - 300, HEIGHT - 125, 600, 90))

    # TODO udelat z toho jednu funkci
    def draw_roll_button(self):
        roll_button = pygame.image.load(os.path.join('../assets/board/1', 'button_backg.png'))
        roll_rect = roll_button.get_rect(topleft=(WIDTH - 370, HEIGHT - 125))
        self.win.blit(roll_button, (WIDTH - 370, HEIGHT - 125))
        draw_text(self.win, "Roll", 45, "Inter-Regular", BONE_WHITE, WIDTH - 305, HEIGHT - 80)
        return roll_rect

    def draw_save_button(self):
        roll_button = pygame.image.load(os.path.join('../assets/board/1', 'button_backg.png'))
        roll_rect = roll_button.get_rect(topleft=(635, 325))
        self.win.blit(roll_button, (635, 325))
        draw_text(self.win, "Save", 45, "Inter-Regular", BONE_WHITE, 700, 367)
        return roll_rect

    def draw_exit_button(self):
        roll_button = pygame.image.load(os.path.join('../assets/board/1', 'button_backg_red.png'))
        roll_rect = roll_button.get_rect(topleft=(635, 425))
        self.win.blit(roll_button, (635, 425))
        draw_text(self.win, "Quit", 45, "Inter-Regular", BONE_WHITE, 700, 467)
        return roll_rect
