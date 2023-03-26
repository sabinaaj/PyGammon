import pygame

R_BOARD = pygame.image.load("PyGammon/assets/board/1/R.png")
TR_R_BOTTOM = pygame.image.load("PyGammon/assets/board/1/R_BOT.png")
TR_R_TOP = pygame.image.load("PyGammon/assets/board/1/R_TOP.png")
L_BOARD = pygame.image.load("PyGammon/assets/board/1/L.png")
TR_L_BOTTOM = pygame.image.load("PyGammon/assets/board/1/L_BOT.png")
TR_L_TOP = pygame.image.load("PyGammon/assets/board/1/L_TOP.png")

image_width, image_height = L_BOARD.get_size()

scale_factor = min(WIDTH / (image_width * 2), HEIGHT / image_height)
scaled_image_width = int(image_width * scale_factor)
scaled_image_height = int(image_height * scale_factor)
scaled_L_BOARD = pygame.transform.scale(L_BOARD, (scaled_image_width, scaled_image_height))
scaled_R_BOARD = pygame.transform.scale(R_BOARD, (scaled_image_width, scaled_image_height))

background = pygame.Surface((scaled_image_width * 2, scaled_image_height))
background.blit(scaled_L_BOARD, (0, 0))
background.blit(scaled_R_BOARD, (scaled_image_width, 0))
#
class GameBoard:

    def __init__(self):
        #Jake ma plocha vlastnosti?
        pass

    def draw(self, win):
        #TODO zobrazi plochu a vsechny casti
        win.blit(background, (0, 0))
