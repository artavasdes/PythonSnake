#Snake object
import pygame
from pygame.locals import *
class Snake():

    def __init__(self, color, start_direction, screen, box_size):
        #maybe make color customizable by player later
        self.x = 75
        self.y = 200

        self.positions = [(self.x, self.y), (self.x - box_size, self.y), (self.x - box_size * 2, self.y)]
        self.direction = start_direction
        self.color = color
        self.head_coords = self.positions[0]
        self.screen = screen
        self.box_size = box_size

    def move(self, direction):

        
        if direction == 'UP':
            self.head_coords = (self.head_coords[0], self.head_coords[1] - self.box_size)
        elif direction == "DOWN":
            self.head_coords = (self.head_coords[0], self.head_coords[1] + self.box_size)
        elif direction == "RIGHT":
            self.head_coords = (self.head_coords[0] + self.box_size, self.head_coords[1])
        elif direction == "LEFT":
            self.head_coords = (self.head_coords[0] - self.box_size, self.head_coords[1])
        
        self.positions.insert(0, self.head_coords)

    

    def draw(self):
        #to do once grid/area is complete:
        #draw the snake based on its positions
        for segment in range(len(self.positions)):
           box = pygame.Rect(self.positions[segment][0], self.positions[segment][1], self.box_size, self.box_size)
           pygame.draw.rect(self.screen, self.color, box)



    # def controls(self):
    #     self.left = 
    #     self.right = 
        


    # def movement(self):
    #     self.speed = 

