from menu import *
# stale nevidim problem
# jsem ted zmaten
# co se stane po kliknuti na singleplayer?
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyGammon')


def main():
    menu = Menu(WIN)
    menu.menu_loop()


if __name__ == '__main__':
    main()
