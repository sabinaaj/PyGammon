from game import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Backgammon')


def main():
    game = Game(WIN)
    game.gameloop()


if __name__ == '__main__':
    main()
