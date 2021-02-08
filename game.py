#Main game file

import pygame


pygame.init()
dis=pygame.display.set_mode((400,400))
pygame.display.update()
pygame.display.set_caption("Snake game by Joshua Kim and Vartan Yildiz")
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()