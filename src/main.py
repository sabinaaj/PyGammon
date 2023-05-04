from menu import *

#TODO: Add proerties to classes

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set icon
pygame_icon = pygame.image.load('../assets/icon.png')
pygame.display.set_icon(pygame_icon)

pygame.display.set_caption('PyGammon - An open-source Backgammon')


def main():
    menu = Menu(WIN)
    menu.menu_loop()


if __name__ == '__main__':
    main()
