import pygame.time
import pygame_gui

from game import *


class MenuPages(Enum):
    MAIN_MENU = 0
    GAMEMODE_MENU = 1
    SINGLEP_MENU = 2
    MULTIP_MENU = 3
    DEV_WARNING = 4
    DEV_MENU = 5


TRIANGLE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/menu', 'triangle.png')), (25, 25))


class Menu:
    def __init__(self, _win):
        self._win = _win
        self._menu_page = MenuPages.MAIN_MENU

    def menu_loop(self):
        run = True
        manager_multi = pygame_gui.UIManager((WIDTH, HEIGHT))
        manager_single = pygame_gui.UIManager((WIDTH, HEIGHT))
        pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 375), (600, 50)),
                                            manager=manager_multi, object_id='#player1_input')

        pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 460), (600, 50)),
                                            manager=manager_multi, object_id='#player2_input')

        pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 375), (600, 50)),
                                            manager=manager_single, object_id='#player1_input')
        p1_name = 'Player 1'
        p2_name = 'Player 2'

        while run:
            pygame.time.Clock().tick(FPS)
            self._win.fill(WHITE)
            draw_text(self._win, "PyGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
            draw_text(self._win, "An open-source Backgammon", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)

            mouse_pos = pygame.mouse.get_pos()

            if self._menu_page == MenuPages.MAIN_MENU:
                run = self.main_menu(mouse_pos)
            elif self._menu_page == MenuPages.GAMEMODE_MENU:
                run = self.gamemode_menu(mouse_pos)
            elif self._menu_page == MenuPages.SINGLEP_MENU:
                run, p1_name, p2_name = self.singlep_menu(mouse_pos, manager_single, p1_name)
            elif self._menu_page == MenuPages.MULTIP_MENU:
                run, p1_name, p2_name = self.multip_menu(mouse_pos, manager_multi, p1_name, p2_name)
            elif self._menu_page == MenuPages.DEV_WARNING:
                run = self.dev_warning(mouse_pos)
            elif self._menu_page == MenuPages.DEV_MENU:
                run = self.dev_menu(mouse_pos)

    def main_menu(self, mouse_pos):
        # Renders the main menu text
        run = True

        version_text = draw_text(self._win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)

        play_rect = draw_text(self._win, "PLAY", 30, "Inter-Bold", BLACK, WIDTH / 3, 380, center=False)
        if play_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 385))

        load_rect = draw_text(self._win, "LOAD GAME", 30, "Inter-Bold", BLACK, WIDTH / 3, 460, center=False)
        if load_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 465))

        exit_rect = draw_text(self._win, "EXIT", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if exit_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 545))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.GAMEMODE_MENU
                if load_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop(True)
                    run = False
                if version_text.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.DEV_WARNING
                if exit_rect.collidepoint(mouse_pos):
                    run = False
                    pygame.quit()

        return run

    def gamemode_menu(self, mouse_pos):
        # Menu shown after clicking play
        run = True

        singleplayer_rect = draw_text(self._win, "SINGLEPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, 380, center=False)
        if singleplayer_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 385))

        multiplayer_rect = draw_text(self._win, "MULTIPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, 460, center=False)
        if multiplayer_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 465))

        back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if back_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 545))

        pygame.display.update()

        for event in pygame.event.get():
            # Actions after clicking on menu buttons
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.SINGLEP_MENU
                if multiplayer_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.MULTIP_MENU
                if back_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.MAIN_MENU

        return run

    def multip_menu(self, mouse_pos, manager, p1_name, p2_name):
        run = True
        draw_text(self._win, "Player 1 Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 380, center=False)
        draw_text(self._win, "Player 2 Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 465, center=False)

        play_rect = draw_text(self._win, "PLAY", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if play_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 545))

        back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, 620, center=False)
        if back_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 625))

        manager.update(pygame.time.Clock().tick(60) / 1000)

        manager.draw_ui(self._win)

        pygame.display.update()

        for event in pygame.event.get():

            manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player1_input':
                p1_name = event.text

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player2_input':
                p2_name = event.text

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_rect.collidepoint(mouse_pos):
                    run = False
                    game = Game(self._win, True, p1_name, p2_name)
                    game.gameloop()

                if back_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.GAMEMODE_MENU

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        return run, p1_name, p2_name

    def singlep_menu(self, mouse_pos, manager, p1_name):
        run = True
        draw_text(self._win, "Player Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 380, center=False)

        play_rect = draw_text(self._win, "PLAY", 30, "Inter-Bold", BLACK, WIDTH / 3, 465, center=False)

        back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, 550, center=False)

        if back_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 555))

        if play_rect.collidepoint(mouse_pos):
            self._win.blit(TRIANGLE, (WIDTH / 3 - 30, 470))

        manager.update(pygame.time.Clock().tick(60) / 1000)

        manager.draw_ui(self._win)

        # funguje, nesahat, neukazovat u zkousky

        # hotfix = pygame.draw.rect(self._win, WHITE, (WIDTH / 3, 460, 600, 50))

        pygame.display.update()

        for event in pygame.event.get():

            manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player1_input':
                p1_name = event.text

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_rect.collidepoint(mouse_pos):
                    run = False
                    game = Game(self._win, False, p1_name, 'AI')
                    game.gameloop()

                if back_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.GAMEMODE_MENU

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        return run, p1_name, 'AI'

    def dev_warning(self, mouse_pos):
        run = True
        self._win.fill(WHITE)
        draw_text(self._win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)
        draw_text(self._win, "PyGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
        draw_text(self._win, "Development mode", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)

        draw_text(self._win, "WARNING!", 40, "Inter-Medium", EXTREME_RED, WIDTH / 2, HEIGHT / 2 - 150, center=True)
        draw_text(self._win, "Things might break. ", 30, "Inter-Medium", EXTREME_RED, WIDTH / 2, HEIGHT / 2 - 115, center=True)
        draw_text(self._win, "The developers of this application are not liable for any damage", 15, "Inter-Medium", BLACK, WIDTH / 2, HEIGHT / 2 - 70, center=True)
        draw_text(self._win, "caused by the use of the development mode, whether it be to you, your loved ones, any third party.", 15, "Inter-Medium", BLACK, WIDTH / 2, HEIGHT / 2 - 50, center=True)

        crybaby_rect = draw_text(self._win, ":'(", 30, "Inter-Bold", SABINY_OCI, WIDTH / 2 + 200, HEIGHT / 2, center=True)
        chad_rect = draw_text(self._win, "YES DADDY", 30, "Inter-Bold", SABINY_OCI, WIDTH / 2 - 200, HEIGHT / 2, center=True)

        if crybaby_rect.collidepoint(mouse_pos):
            crybaby_rect = draw_text(self._win, ":'(", 30, "Inter-Bold", FAWN, WIDTH / 2 + 200, HEIGHT / 2, center=True)
        elif chad_rect.collidepoint(mouse_pos):
            chad_rect = draw_text(self._win, "YES DADDY", 30, "Inter-Bold", FAWN, WIDTH / 2 - 200, HEIGHT / 2, center=True)
        pygame.display.update()

        for event in pygame.event.get():
            # Actions after clicking on menu buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                if crybaby_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.MAIN_MENU
                elif chad_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.DEV_MENU

        return run


    def dev_menu(self, mouse_pos):
        run = True
        self._win.fill(WHITE)
        draw_text(self._win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)
        draw_text(self._win, "DevGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
        draw_text(self._win, "An open-source developer menu.", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)

        back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", SABINY_OCI, 35, 820, center=False)
        gammon_rect = draw_text(self._win, "GAMMON WIN", 30, "Inter-Bold", SABINY_OCI, 200, HEIGHT / 2 - 100, center=True)
        backg_rect = draw_text(self._win, "BACKGAMMON WIN", 30, "Inter-Bold", SABINY_OCI, 600, HEIGHT / 2 - 100, center=True)
        norm_rect = draw_text(self._win, "NORMAL WIN", 30, "Inter-Bold", SABINY_OCI, 1100, HEIGHT / 2 - 100, center=True)

        if back_rect.collidepoint(mouse_pos):
            back_rect = draw_text(self._win, "BACK", 30, "Inter-Bold", FAWN, 35, 820, center=False)
        elif gammon_rect.collidepoint(mouse_pos):
            gammon_rect = draw_text(self._win, "GAMMON WIN", 30, "Inter-Bold", FAWN, 200, HEIGHT / 2 - 100, center=True)
        elif backg_rect.collidepoint(mouse_pos):
            backg_rect = draw_text(self._win, "BACKGAMMON WIN", 30, "Inter-Bold", FAWN, 600, HEIGHT / 2 - 100, center=True)
        elif norm_rect.collidepoint(mouse_pos):
            norm_rect = draw_text(self._win, "NORMAL WIN", 30, "Inter-Bold", FAWN, 1100, HEIGHT / 2 - 100, center=True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    self._menu_page = MenuPages.MAIN_MENU
                if gammon_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop(True)
                    run = False
                if backg_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop(True)
                    run = False
                if norm_rect.collidepoint(mouse_pos):
                    game = Game(self._win, False, 'Player1', 'Player2')
                    game.gameloop(True)
                    run = False

        return run
