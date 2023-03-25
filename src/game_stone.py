class GameStone:
    def __init__(self, player):
        self.position = []
        self.player = player
        self.color = player.color
        self.image = B_STONE if self.color else W_STONE

    def draw(self, win, x, y):
        win.blit(self.image, (x, y))
