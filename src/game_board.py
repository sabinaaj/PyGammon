import pygame
from main import draw_text
from constants import *
from dice import *

R_BOARD = pygame.image.load("../assets/board/1/R.png")
TR_R_BOTTOM = pygame.image.load("../assets/board/1/R_BOT.png")
TR_R_TOP = pygame.image.load("../assets/board/1/R_TOP.png")
L_BOARD = pygame.image.load("../assets/board/1/L.png")
TR_L_BOTTOM = pygame.image.load("../assets/board/1/L_BOT.png")
TR_L_TOP = pygame.image.load("../assets/board/1/L_TOP.png")


class GameBoard:

    def __init__(self):
        #Jake ma plocha vlastnosti?
        pass

    def draw(self, win):
        #TODO zobrazi plochu a vsechny casti
        image_width, image_height = L_BOARD.get_size()

        scale_factor = min(WIDTH / (image_width * 2), HEIGHT / image_height)
        scaled_image_width = int(image_width * scale_factor)
        scaled_image_height = int(image_height * scale_factor)
        scaled_L_BOARD = pygame.transform.scale(L_BOARD, (scaled_image_width, scaled_image_height))
        scaled_R_BOARD = pygame.transform.scale(R_BOARD, (scaled_image_width, scaled_image_height))

        background = pygame.Surface((scaled_image_width * 2, scaled_image_height))
        background.blit(scaled_L_BOARD, (0, 0))
        background.blit(scaled_R_BOARD, (scaled_image_width, 0))

        win.blit(background, (0, HEIGHT / 13))

        self.draw_nums(win)
        self.draw_names(win, "Player 1", "Player 2", BLACK, BONE_WHITE)

    def draw_nums(self, win):
        """Draws numbers around the game board."""
        for i in range(6):
            draw_text(win, f"{i + 13}", 20, "Inter-Regular", BLACK, 130 + i * 88, 20)
            draw_text(win, f"{12 - i}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 50)
            draw_text(win, f"{i + 19}", 20, "Inter-Regular", BLACK, 830 + i * 88, 20)
            draw_text(win, f"{6 - i}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 50)

            draw_text(win, f"{i + 13}", 20, "Inter-Regular", BONE_WHITE, 130 + i * 88, 800)
            draw_text(win, f"{12 - i}", 20, "Inter-Regular", BLACK, 130 + i * 88, 830)
            draw_text(win, f"{i + 19}", 20, "Inter-Regular", BONE_WHITE, 830 + i * 88, 800)
            draw_text(win, f"{6 - i}", 20, "Inter-Regular", BLACK, 830 + i * 88, 830)
    def draw_names(self, win, player1:str, player2:str, color_p1, color_p2):
        """Draws the player names."""
        draw_text(win, f"{player1}", 20, "Inter-Regular", color_p1, 70, 870)
