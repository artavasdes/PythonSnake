#Apple object
import pygame, random
from pygame.locals import *

class Apple():

    def __init__(self, color, screen, box_size):
        self.screen = screen
        self.color = color
        self.position = (450, 270)
        self.box_size = box_size
    
    def place_on_grid(self, gridx, gridy):
        #Sets to a new, random position on the grid/playarea.
        self.position = ((random.randrange(0, gridx), random.randrange(0, gridy)))
        self.draw()
    def draw(self):
        #To do once grid/surface object setup:
        #Draws a new apple in the new position.
        apple_box = pygame.Rect(self.position[0], self.position[1], self.box_size, self.box_size)
        pygame.draw.rect(self.screen, self.color, apple_box)


