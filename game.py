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
BOX_SIZE = 25
DISPLAYX = 425
DISPLAYY = 425

#DIRECTIONS
UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"


pygame.init()
dis=pygame.display.set_mode((DISPLAYX, DISPLAYY))
CLOCK = pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("Snake game by Joshua Kim and Vartan Yildiz")

# game_over=False

def game_loop():

    #Create new snake
    snake_obj = Snake(BLUE, "RIGHT", dis, BOX_SIZE)
    #Create new apple
    apple = Apple(RED, dis, BOX_SIZE)
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == K_LEFT:
                    if snake_obj.direction != RIGHT:
                        snake_obj.direction = LEFT
                        

                elif event.key == K_RIGHT:
                    if snake_obj.direction != LEFT:
                        snake_obj.direction = RIGHT
                        
                elif event.key == K_UP:
                    if snake_obj.direction != DOWN:
                        snake_obj.direction = UP
                        
                elif event.key == K_DOWN:
                    if snake_obj.direction != UP:
                        snake_obj.direction = DOWN
                        
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        if snake_obj.direction == LEFT:
            snake_obj.move(LEFT)
        elif snake_obj.direction == RIGHT:
            snake_obj.move(RIGHT)
        elif snake_obj.direction == UP:
            snake_obj.move(UP)
        elif snake_obj.direction == DOWN:
            snake_obj.move(DOWN)
        del(snake_obj.positions[-1])

        draw_game_area()
        snake_obj.draw()
        apple.draw()
        pygame.display.update()
        CLOCK.tick(FPS)
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
