#Apple object
import pygame, random
from pygame.locals import *

class Apple():

    def __init__(self, color, screen, box_size, snake, obstacles):
        self.screen = screen
        self.color = color
        self.position = [350, 245]
        self.box_size = box_size
        self.snake = snake
        self.graphic = pygame.image.load("graphics/snake_apple_graphic.png")
        self.obstacles = obstacles
    def place_on_grid(self, gridx, gridy):
        '''Sets to a new, random position on the grid/playarea.'''
        self.position = [random.randrange(0, (gridx - self.box_size) // self.box_size) * self.box_size, 
        random.randrange(0, (gridy - self.box_size) // self.box_size) * self.box_size]

        while self.position in self.snake.positions or self.position in self.obstacles.all_obstacles:
            #Find a new position so that it's not the same as one of the snake's.
            self.position = [random.randrange(0, (gridx - self.box_size) // self.box_size) * self.box_size, 
            random.randrange(0, (gridy - self.box_size) // self.box_size) * self.box_size]

    def draw(self):
        '''Draws a new apple in the new position.'''
        # apple_box = pygame.Rect(self.position[0], self.position[1], self.box_size, self.box_size)
        # pygame.draw.rect(self.screen, self.color, apple_box)
        self.screen.blit(self.graphic, (self.position[0], self.position[1]))
