import pygame.time
from game import *
import pygame_gui


class MenuPages(Enum):
    MAIN_MENU = 0
    GAMEMODE_MENU = 1
    SINGLEP_MENU = 2
    MULTIP_MENU = 3


class Menu:
    def __init__(self, win):
        self.win = win
        self.triangle = pygame.transform.scale(pygame.image.load(os.path.join('../assets/menu', 'triangle.png')),
                                               (25, 25))
        self.menu_page = MenuPages.MAIN_MENU

    def menu_loop(self):
        run = True
        manager_main = pygame_gui.UIManager((WIDTH, HEIGHT))
        manager_multi = pygame_gui.UIManager((WIDTH, HEIGHT))
        p1_in = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 375), (600, 50)),
                                                    manager=manager_main, object_id='#player1_input')

        p2_in = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 460), (600, 50)),
                                                        manager=manager_main, object_id='#player2_input')

        pm_in = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((WIDTH / 3, 375), (600, 50)),
                                                    manager=manager_multi, object_id='#player1_input')
        p1_name = 'Player 1'
        p2_name = 'Player 2'

        while run:
            pygame.time.Clock().tick(FPS)
            self.win.fill(WHITE)
            draw_text(self.win, "PyGammon", 90, "Inter-Medium", BLACK, WIDTH / 3, 100, center=False)
            draw_text(self.win, "An open-source Backgammon", 20, "Inter-Medium", BLACK, WIDTH / 2 + 20, 205)
            draw_text(self.win, f"Build {BUILD_NUM}", 15, "Inter-Medium", BLACK, WIDTH / 150, 10, center=False)

            mouse_pos = pygame.mouse.get_pos()

            if self.menu_page == MenuPages.MAIN_MENU:
                run = self.main_menu(mouse_pos)
            elif self.menu_page == MenuPages.GAMEMODE_MENU:
                run = self.gamemode_menu(mouse_pos)
            elif self.menu_page == MenuPages.SINGLEP_MENU:
                run, p1_name, p2_name = self.singlep_menu(mouse_pos, manager_main, p1_name, p2_name)
            elif self.menu_page == MenuPages.MULTIP_MENU:
                run, p1_name, p2_name = self.multip_menu(mouse_pos, manager_multi, p1_name)

    def main_menu(self, mouse_pos):
        # Renders the main menu text
        run = True

        play_rect = draw_text(self.win, "PLAY", 30, "Inter-Bold", BLACK, WIDTH / 3, 380, center=False)
        if play_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 385))

        load_rect = draw_text(self.win, "LOAD GAME", 30, "Inter-Bold", BLACK, WIDTH / 3, 460, center=False)
        if load_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 465))

        exit_rect = draw_text(self.win, "EXIT", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if exit_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 545))

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
                if exit_rect.collidepoint(mouse_pos):
                    run = False
                    pygame.quit()

        return run

    def gamemode_menu(self, mouse_pos):
        # Menu shown after clicking play
        run = True

        singleplayer_rect = draw_text(self.win, "SINGLEPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, 380, center=False)
        if singleplayer_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 385))

        multiplayer_rect = draw_text(self.win, "MULTIPLAYER", 30, "Inter-Bold", BLACK, WIDTH / 3, 460, center=False)
        if multiplayer_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 465))

        back_rect = draw_text(self.win, "BACK", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if back_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 545))

        pygame.display.update()

        for event in pygame.event.get():
            # Actions after clicking on menu buttons
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.SINGLEP_MENU
                if multiplayer_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.MULTIP_MENU
                if back_rect.collidepoint(mouse_pos):
                    self.menu_page = MenuPages.MAIN_MENU

        return run

    def singlep_menu(self, mouse_pos, manager, p1_name, p2_name):
        run = True
        p1_text = draw_text(self.win, "Player 1 Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 380, center=False)
        p2_text = draw_text(self.win, "Player 2 Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 465, center=False)

        play_rect = draw_text(self.win, "Play", 30, "Inter-Bold", BLACK, WIDTH / 3, 540, center=False)
        if play_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 545))





        manager.update(pygame.time.Clock().tick(60) / 1000)

        manager.draw_ui(self.win)

        pygame.display.update()

        for event in pygame.event.get():

            manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player1_input':
                p1_name = event.text

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player2_input':
                p2_name = event.text

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_rect.collidepoint(mouse_pos):
                    game = Game(self.win, False, p1_name, p2_name)
                    game.gameloop()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



        return run, p1_name, p2_name

    def multip_menu(self, mouse_pos, manager, p1_name):
        run = True
        p1_text = draw_text(self.win, "Player Name", 30, "Inter-Bold", BLACK, WIDTH / 6, 380, center=False)


        play_rect = draw_text(self.win, "Play", 30, "Inter-Bold", BLACK, WIDTH / 3, 465, center=False)

        if play_rect.collidepoint(mouse_pos):
            self.win.blit(self.triangle, (WIDTH / 3 - 30, 470))

        manager.update(pygame.time.Clock().tick(60) / 1000)

        manager.draw_ui(self.win)

        #funguje, nesahat, neukazovat u zkousky

        # hotfix = pygame.draw.rect(self.win, WHITE, (WIDTH / 3, 460, 600, 50))

        pygame.display.update()

        for event in pygame.event.get():

            manager.process_events(event)

            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED and event.ui_object_id == '#player1_input':
                p1_name = event.text

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_rect.collidepoint(mouse_pos):
                    game = Game(self.win, False, p1_name, 'AI')
                    game.gameloop()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        return run, p1_name, 'AI'

    #     base_font = pygame.font.Font(None, 32)
    #     user_text = ''
    #
    #     # create rectangle
    #     input_rect = pygame.Rect(200, 200, 140, 32)
    #
    #     # color_active stores color which
    #     # gets active when input box is clicked by user
    #     color_active = pygame.Color(SAGE)
    #
    #     # color_passive store color which is
    #     # color of input box.
    #     color_passive = pygame.Color(SABINY_OCI)
    #     color = color_passive
    #
    #     active = False
    #
    #     while True:
    #         for event in pygame.event.get():
    #
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if input_rect.collidepoint(event.pos):
    #                     active = True
    #                 else:
    #                     active = False
    #
    #             if event.type == pygame.KEYDOWN:
    #
    #                 # Check for backspace
    #                 if event.key == pygame.K_BACKSPACE:
    #
    #                     # get text input from 0 to -1 i.e. end.
    #                     user_text = user_text[:-1]
    #
    #                 # Unicode standard is used for string
    #                 else:
    #                     user_text += event.unicode
    #
    #
    #
    #         if active:
    #             color = color_active
    #         else:
    #             color = color_passive
    #
    #         # draw rectangle and argument passed which should
    #         # be on screen
    #         pygame.draw.rect(self.win, color, input_rect)
    #
    #         text_surface = base_font.render(user_text, True, (BONE_WHITE))
    #
    #         # render at position stated in arguments
    #         self.win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    #
    #         # set width of textfield so that text cannot get
    #         # outside of user's text input
    #         input_rect.w = max(100, text_surface.get_width() + 10)
    #
    #         # display.flip() will update only a portion of the
    #         # screen to updated, not full area
    #         pygame.display.flip()
