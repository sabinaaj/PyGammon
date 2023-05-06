from game import *
from game_stone import *


class MenuPages(Enum):
    MAIN_MENU = 0
    GAMEMODE_MENU = 1
    SINGLEP_MENU = 2
    MULTIP_MENU = 3
    DEV_WARNING = 4
    DEV_MENU = 5


class DevMenu:
    def __init__(self, win):
        self._win = win

    def dev_warning(self, mouse_pos):
        run = True
        menu_page = MenuPages.DEV_WARNING
        self._win.fill(WHITE)
        draw_text(self._win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)
        draw_text(self._win, "PyGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
        draw_text(self._win, "Development mode", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)

        draw_text(self._win, "WARNING!", 40, "Inter-Medium", EXTREME_RED, WIDTH / 2, HEIGHT / 2 - 150, center=True)
        draw_text(self._win, "Things might break. ", 25, "Inter-Medium", EXTREME_RED, WIDTH / 2, HEIGHT / 2 - 115,
                  center=True)
        draw_text(self._win, "We are not liable for any damage caused to you or your loved ones.", 15, "Inter-Medium",
                  BLACK, WIDTH / 2, HEIGHT / 2 - 70, center=True)

        crybaby_rect = draw_text(self._win, ":'(", 30, "Inter-Bold", SABINY_OCI, WIDTH / 2 + 200, HEIGHT / 2,
                                 center=True)
        chad_rect = draw_text(self._win, "YES DADDY", 30, "Inter-Bold", SABINY_OCI, WIDTH / 2 - 200, HEIGHT / 2,
                              center=True)

        if crybaby_rect.collidepoint(mouse_pos):
            crybaby_rect = draw_text(self._win, ":'(", 30, "Inter-Bold", FAWN, WIDTH / 2 + 200, HEIGHT / 2,
                                     center=True)
        elif chad_rect.collidepoint(mouse_pos):
            chad_rect = draw_text(self._win, "YES DADDY", 30, "Inter-Bold", FAWN, WIDTH / 2 - 200, HEIGHT / 2,
                                  center=True)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # Actions after clicking on menu buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crybaby_rect.collidepoint(mouse_pos):
                    menu_page = MenuPages.MAIN_MENU
                elif chad_rect.collidepoint(mouse_pos):
                    menu_page = MenuPages.DEV_MENU

        return run, menu_page

    def dev_menu(self, mouse_pos):
        run = True
        menu_page = MenuPages.DEV_MENU
        self._win.fill(WHITE)
        draw_text(self._win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)
        draw_text(self._win, "DevGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
        draw_text(self._win, "An open-source developer menu.", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)

        back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", SABINY_OCI, 35, 820, center=False)
        gammon_rect = draw_text(self._win, "GAMMON WIN", 30, "Inter-Bold", SABINY_OCI, 200, HEIGHT / 2 - 100,
                                center=True)
        backg_rect = draw_text(self._win, "BACKGAMMON WIN", 30, "Inter-Bold", SABINY_OCI, 600, HEIGHT / 2 - 100,
                               center=True)
        norm_rect = draw_text(self._win, "NORMAL WIN", 30, "Inter-Bold", SABINY_OCI, 1100, HEIGHT / 2 - 100,
                              center=True)
        daddy_rect = draw_text(self._win, "BREAK ME DADDY", 30, "Inter-Bold", SABINY_OCI, 1100, HEIGHT / 2,
                              center=True)
        ai_rect = draw_text(self._win, "AI vs. AI", 30, "Inter-Bold", SABINY_OCI, 200, HEIGHT / 2,
                               center=True)

        if back_rect.collidepoint(mouse_pos):
            back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", FAWN, 35, 820, center=False)
        elif gammon_rect.collidepoint(mouse_pos):
            gammon_rect = draw_text(self._win, "GAMMON WIN", 30, "Inter-Bold", FAWN, 200, HEIGHT / 2 - 100,
                                    center=True)
        elif backg_rect.collidepoint(mouse_pos):
            backg_rect = draw_text(self._win, "BACKGAMMON WIN", 30, "Inter-Bold", FAWN, 600, HEIGHT / 2 - 100,
                                   center=True)
        elif norm_rect.collidepoint(mouse_pos):
            norm_rect = draw_text(self._win, "NORMAL WIN", 30, "Inter-Bold", FAWN, 1100, HEIGHT / 2 - 100,
                                  center=True)
        elif daddy_rect.collidepoint(mouse_pos):
            daddy_rect = draw_text(self._win, "BREAK ME DADDY", 30, "Inter-Bold", FAWN, 1100, HEIGHT / 2,
                                  center=True)
        elif ai_rect.collidepoint(mouse_pos):
            ai_rect = draw_text(self._win, "AI vs. AI", 30, "Inter-Bold", FAWN, 200, HEIGHT / 2,
                                center=True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    menu_page = MenuPages.MAIN_MENU
                if gammon_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop('../dev_saves/gammon.json')
                    run = False
                if backg_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop('../dev_saves/backgammon.json')
                    run = False
                if norm_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop('../dev_saves/win.json')
                    run = False
                if daddy_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop('../dev_saves/daddy.json')
                    run = False
                if ai_rect.collidepoint(mouse_pos):
                    game = Game(self._win, GameMode.AI_VS_AI, 'Player1', 'Player2')
                    game.gameloop()
                    run = False

        return run, menu_page
