import os
from enum import Enum

from game import *
from main import draw_text


class MenuPages(Enum):
    MAIN_MENU = 0
    GAMEMODE_MENU = 1
    OPTIONS_MENU = 2


class Menu:
    def __init__(self, win):
        self.win = win
        self.triangle = pygame.transform.scale(pygame.image.load(os.path.join('../assets/menu', 'triangle.png')),(25, 25))
        self.menu_page = MenuPages.MAIN_MENU
        self.game = Game(win)

    def menu_loop(self):
        run = True

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill(WHITE)
            draw_text(self.win, "PyGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, HEIGHT / 5 + 10, center=False)
            draw_text(self.win, "An open-source Backgammon", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, HEIGHT / 5 + 10)

            mouse_pos = pygame.mouse.get_pos()

            if self.menu_page == MenuPages.MAIN_MENU:
                run = self.main_menu(mouse_pos)
            elif self.menu_page == MenuPages.GAMEMODE_MENU:
                run = self.gamemode_menu(mouse_pos)
            elif self.menu_page == MenuPages.OPTIONS_MENU:
                run = self.options_menu(mouse_pos)

    def main_menu(self, mouse_pos):
        run = True

        play_rect = draw_text(self.win, "PLAY", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 5, center=False)
        if play_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 5 - 30))

        load_rect = draw_text(self.win, "LOAD GAME", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 6, center=False)
        if load_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 6 - 30))

        options_rect = draw_text(self.win, "OPTIONS", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 7, center=False)
        if options_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 7 - 30))

        exit_rect = draw_text(self.win, "EXIT", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 8, center=False)
        if exit_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 8 - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.GAMEMODE_MENU
                if load_rect.collidepoint(mouse_pos):
                    pass
                if options_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.OPTIONS_MENU
                if exit_rect.collidepoint(mouse_pos):
                    run = False
                    pygame.quit()

        return run

    def gamemode_menu(self, mouse_pos):
        run = True

        singleplayer_rect = draw_text(self.win, "SINGLEPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 5,center=False)
        if singleplayer_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 5 - 30))

        multiplayer_rect = draw_text(self.win, "MULTIPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 6,center=False)
        if multiplayer_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 6 - 30))

        back_rect = draw_text(self.win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 7, center=False)
        if back_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 7 - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_rect.collidepoint(mouse_pos):
                    run = False
                    self.game.gameloop(multiplayer=False)
                if multiplayer_rect.collidepoint(mouse_pos):
                    run = False
                    self.game.gameloop(multiplayer=True)
                if back_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.MAIN_MENU

        return run

    def options_menu(self, mouse_pos):
        run = True

        back_rect = draw_text(self.win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, HEIGHT / 12 * 5, center=False)
        if back_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, HEIGHT / 12 * 5 - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.MAIN_MENU

        return run
