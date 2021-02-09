#Main game file

import pygame, sys
from pygame.locals import *
from snake import *
from apple import *
#Setup some constants/colors
DARKGREEN = (162, 209, 73)
LIGHTGREEN = (170, 215, 81)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

FPS = 20
BOX_SIZE = 30
DISPLAYX = 540
DISPLAYY = 540

pygame.init()
dis=pygame.display.set_mode((DISPLAYX, DISPLAYY))
pygame.display.update()
pygame.display.set_caption("Snake game by Joshua Kim and Vartan Yildiz")
<<<<<<< HEAD
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
        
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()
=======
# game_over=False

def game_loop():

    #Create new snake
    snake_obj = Snake(BLUE, "RIGHT", dis, BOX_SIZE)
    #Create new apple
    apple = Apple(RED, dis, BOX_SIZE)
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        

        
        dis.fill(BLACK)
        draw_game_area()
        snake_obj.draw()
        apple.draw()
        pygame.display.update()

def draw_game_area():
    #Loop through all the rows and corresponding columns to create "boxes"/grids 
    #on the play-area via Pygame rect objects.
    for boxx in range(DISPLAYX):
        for boxy in range(DISPLAYY):
            # box_width = boxx* BOX_SIZE
            # box_length = boxy* BOX_SIZE

            grid_box = pygame.Rect(boxx * BOX_SIZE, boxy * BOX_SIZE, BOX_SIZE, BOX_SIZE)
            if boxx % 2 == 0:

                if boxy % 2 == 0:
                    pygame.draw.rect(dis, LIGHTGREEN, grid_box)
                else:
                    pygame.draw.rect(dis, DARKGREEN, grid_box)
                
            elif boxy % 2 != 0:
                pygame.draw.rect(dis, LIGHTGREEN, grid_box)
            
            else:
                pygame.draw.rect(dis, DARKGREEN, grid_box)
    
    


def main():

    while True:
        game_loop()

main()
>>>>>>> 109f2aeef3b54a4d8ad411c590a41655b5e5faea
