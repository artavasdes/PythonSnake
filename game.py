#Main game file

import pygame


pygame.init()
dis=pygame.display.set_mode((400,400))
pygame.display.update()
pygame.display.set_caption("Snake game by Joshua Kim and Vartan Yildiz")
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