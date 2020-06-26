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
            Game.check_keyboard(self)
            self.snake.move()
            Game.update_screen(self)

    def update_screen(self):
        self.screen.fill(self.settings.background_color)

        Game.draw_obj(self, self.screen, self.settings.snake_color, self.snake.rect)

        pygame.display.flip()

    def draw_obj(self, screen, color, rect):
        pygame.draw.rect(screen, color, rect)

    def check_keyboard(self):
        for event in pygame.event.get():
            Game.check_input(self, event)

    def check_input(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and self.snake.direction != 'up':
                self.snake.change_direction('down')
            elif event.key == pygame.K_UP and self.snake.direction != 'down':
                self.snake.change_direction('up')
            elif event.key == pygame.K_LEFT and self.snake.direction != 'right':
                self.snake.change_direction('left')
            elif event.key == pygame.K_RIGHT and self.snake.direction != 'left':
                self.snake.change_direction('right')

class Snake:
    def __init__(self):
        self.settings = Settings()
        self.size = self.settings.block_size
        self.rect = pygame.Rect(20, 50, self.size * 3, self.size * 8)

        self.direction = 'down'
        self.pos_float = [self.rect[0], self.rect[1]]

    def move(self):
        if self.direction == 'down':
            self.pos_float[1] += self.settings.snake_speed
            self.rect.bottom = int(self.pos_float[1])
        elif self.direction == 'up':
            self.pos_float[1] -= self.settings.snake_speed
            self.rect.top = int(self.pos_float[1])
        elif self.direction == 'right':
            self.pos_float[0] += self.settings.snake_speed
            self.rect.right = int(self.pos_float[0])
        elif self.direction == 'left':
            self.pos_float[0] -= self.settings.snake_speed
            self.rect.left = int(self.pos_float[0])

    def change_direction(self, direction):
        self.direction = direction


class Settings:
    def __init__(self):
        self.screen_size = [600, 600]
        self.background_color = (0, 0, 10)

        self.block_size = 8
        self.snake_color = (68, 198, 59)
        self.snake_speed = 0.3

game = Game()
game.start_game()
