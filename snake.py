#! python3

import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)

    def start_game(self):
        while True:
            Game.check_input(self)
            Game.update_screen(self)

    def update_screen(self):
        self.screen.fill(self.settings.background_color)
        pygame.display.flip()

    def check_input(self):
        for event in pygame.event.get():
            Game.check_quit(self, event)

    def check_quit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()


class Settings:
    def __init__(self):
        self.screen_size = [600, 600]
        self.background_color = (0, 0, 10)

game = Game()
game.start_game()
