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
        self.running = True

    def start_game(self):
        while True:
            Game.check_keyboard(self)
            if self.running:
                Game.update_snake(self)
            Game.update_screen(self)

    def update_snake(self):
        if self.snake.check_hit_border(self.snake.rect):
            self.running = False
            
        self.snake.update()

    def update_screen(self):
        self.screen.fill(self.settings.background_color)

        Game.draw_obj(self, self.screen, self.snake.color, self.snake.rect)

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
            if event.key == pygame.K_DOWN:
                self.snake.change_direction('down')
            elif event.key == pygame.K_UP:
                self.snake.change_direction('up')
            elif event.key == pygame.K_LEFT:
                self.snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                self.snake.change_direction('right')

class Snake:
    def __init__(self):
        self.settings = Settings()

        self.color = (68, 198, 59)
        self.speed = 0.5

        self.x = 10
        self.y = 10
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.direction = 'down'

    def moveDown(self):
        self.y += self.speed
        self.rect.y = int(self.y)

    def moveUp(self):
        self.y -= self.speed
        self.rect.y = int(self.y)

    def moveRight(self):
        self.x += self.speed
        self.rect.x = int(self.x)

    def moveLeft(self):
        self.x -= self.speed
        self.rect.x = int(self.x)

    def update(self):
        if self.direction == 'down' and self.direction != 'up':
            Snake.moveDown(self)
        elif self.direction == 'up' and self.direction != 'down':
            Snake.moveUp(self)
        elif self.direction == 'left' and self.direction != 'right':
            Snake.moveLeft(self)
        elif self.direction == 'right' and self.direction != 'left':
            Snake.moveRight(self)

    def change_direction(self, direction):
        self.direction = direction

    def check_hit_border(self, rect):
        if rect.bottom == 600 or rect.top == 0 or rect.right == 600 or rect.left == 0:
            return True

# class Food:
#     def __init__(self):
#


class Settings:
    def __init__(self):
        self.screen_size = [600, 600]
        self.background_color = (0, 0, 10)



game = Game()
game.start_game()
