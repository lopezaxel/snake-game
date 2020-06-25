#! python3

import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.init()

        self.settings = Settings()
        self.snake = Snake()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption("Snake")

    def start_game(self):
        while True:
            Game.check_input(self)
            Game.update_screen(self)

    def update_screen(self):
        self.screen.fill(self.settings.background_color)

        Game.draw_obj(self, self.screen, self.settings.snake_color, self.snake.rect)
        
        pygame.display.flip()

    def draw_obj(self, screen, color, rect):
        pygame.draw.rect(screen, color, rect)

    def check_input(self):
        for event in pygame.event.get():
            Game.check_quit(self, event)

    def check_quit(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

class Snake:
    def __init__(self):
        self.settings = Settings()
        self.size = self.settings.block_size
        self.rect = pygame.Rect(self.size, self.size * 2, 30, 40)


class Settings:
    def __init__(self):
        self.screen_size = [600, 600]
        self.background_color = (0, 0, 10)

        self.block_size = 15
        self.snake_color = (68, 198, 59)

game = Game()
game.start_game()
