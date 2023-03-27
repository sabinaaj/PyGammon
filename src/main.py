from menu import *
import pygame
from constants import *
from game import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyGammon')

def draw_text(win, text, size, font, color, x, y, center = True):
    font = pygame.font.Font(f'../assets/fonts/Inter/{font}.ttf', size)
    text_on_display = font.render(text, True, color)
    text_rect = text_on_display.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.bottomleft = (x, y)

    win.blit(text_on_display, text_rect)
    return text_rect


def main():
    # menu = Menu(WIN)
    # menu.menu_loop()
    game = Game(WIN, False)
    game.gameloop()


if __name__ == '__main__':
    main()
