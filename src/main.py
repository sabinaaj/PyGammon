from menu import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyGammon')


def main():
    menu = Menu(WIN)
    menu.menu_loop()
    # game = Game(WIN, False)
    # game.gameloop()


if __name__ == '__main__':
    main()
