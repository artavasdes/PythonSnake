#Apple object
import pygame, random
from pygame.locals import *

class Apple():

    def __init__(self, color, screen):
        self.screen = screen
        self.color = color
        self.position = ()
    
    def place_on_grid(self, gridx, gridy):
        #Sets to a new, random position on the grid/playarea.
        self.position = ((random.randrange(0, gridx), random.randrange(0, gridy)))
        self.draw()
    def draw(self):
        #To do once grid/surface object setup:
        #Draws a new apple in the new position.
        pass


